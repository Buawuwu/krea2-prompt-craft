#!/usr/bin/env python3
# ─────────────────────────────────────────────────────────────
# 出图对账：拿「上次真正跑的那条词」跟「这次真正跑的那条词」逐段 diff
#   （v2.17.0 新增 · 2026-09-19 的教训）
#
# 为什么有它：
#   用户会在跑之前改稿 —— 所以「对账的基准是自己的草稿」是错的。
#   唯一可信的基准是**出图 PNG 里的 tEXt 元数据**（ComfyUI 写进去的那条
#   prompt 原文），连同 种子 / 一采档 / 二采档 / 分辨率 一起核。
#   实测事故：用户把「风格」段整段换成手绘版、顺手带走了段内的旧化词
#   → 暖锈色像素占比 7.05% → 0.72%，**只有逐段 diff 才看得出来**。
#
# 用法：
#   python3 tools/run-diff.py <这次的图.png> <上次的图.png>   # 逐段 diff（旧 → 新）
#   python3 tools/run-diff.py <图.png> --draft <稿.md>         # 图 vs 草稿
#   python3 tools/run-diff.py <图.png>                         # 只打元信息
#
# 只用标准库（struct / zlib / json / hashlib / difflib），不依赖 PIL。
# ─────────────────────────────────────────────────────────────
import sys, os, json, zlib, struct, hashlib, difflib

def texts(path):
    out = {}
    with open(path, 'rb') as f:
        if f.read(8) != b'\x89PNG\r\n\x1a\n':
            raise SystemExit('不是 PNG：%s' % path)
        while True:
            head = f.read(8)
            if len(head) < 8:
                break
            ln, typ = struct.unpack('>I4s', head)
            data = f.read(ln)
            f.read(4)
            if typ == b'tEXt':
                k, _, v = data.partition(b'\x00')
                out[k.decode('latin-1')] = v.decode('utf-8', 'replace')
            elif typ == b'zTXt':
                k, _, rest = data.partition(b'\x00')
                try:
                    out[k.decode('latin-1')] = zlib.decompress(rest[1:]).decode('utf-8', 'replace')
                except Exception:
                    pass
            if typ == b'IEND':
                break
    return out

def graph(path):
    t = texts(path)
    if 'prompt' not in t:
        raise SystemExit('这张 PNG 里没有 prompt 元数据（不是 ComfyUI 出的图？）：%s' % path)
    return json.loads(t['prompt'])

def positive_prompt(g):
    """正向提示词 = 文本最长的那条 CLIPTextEncode。"""
    best = ''
    for n in g.values():
        ct = n.get('class_type', '')
        if 'CLIPTextEncode' in ct or ct == 'Text':
            tx = (n.get('inputs') or {}).get('text') or ''
            if len(tx) > len(best):
                best = tx
    return best.strip()

def resolve(g, v, key=None, depth=0):
    """跟着连线找到上游的字面量（下一节点里同名键优先）。找不到就原样返回。"""
    while depth < 8 and isinstance(v, list) and len(v) == 2 and str(v[0]) in g:
        src = g[str(v[0])].get('inputs') or {}
        lit = {k: x for k, x in src.items() if not isinstance(x, list)}
        if key and key in lit:
            return lit[key]
        if len(lit) == 1:
            return list(lit.values())[0]
        return v
    return v

def meta(g):
    """元信息。**跟连线**解析两个采样器各自吃了哪个 UNETLoader（v2.19.6 修）。

    为什么改：旧版把"图里出现的第二个 `unet_name` 节点"当成二采 —— **不打连线**。
    后果：工作流里那个没人引用的 UNETLoader（孤儿）被当成"二采档"，于是"一采 A + 二采 B 混档"
    这种**从没发生过的配方**被写进了库里（2026-09-19 由用户一句怀疑查实）。
    """
    seed, mp, ar, size, loaders = '', '', '', '', {}
    for nid, n in g.items():
        ct, ins = n.get('class_type', ''), (n.get('inputs') or {})
        if 'unet_name' in ins:
            loaders[nid] = str(ins['unet_name']).split('\\')[-1]
        if 'megapixels' in ins and not mp:
            mp = str(ins.get('megapixels'))
        if 'aspect_ratio' in ins and not ar:
            ar = str(ins.get('aspect_ratio'))
        if ct == 'EmptyLatentImage' and isinstance(ins.get('width'), int) and isinstance(ins.get('height'), int):
            size = '%sx%s' % (ins['width'], ins['height'])
        if not seed:
            s = ins.get('noise_seed', ins.get('seed'))
            if s is not None:
                s = resolve(g, s, 'seed')
                if isinstance(s, int):
                    seed = str(s)

    def sampler_model(cls):
        for nid, n in g.items():
            if n.get('class_type') == cls:
                m = (n.get('inputs') or {}).get('model')
                if isinstance(m, list) and str(m[0]) in loaders:
                    return str(m[0]), loaders[str(m[0])]
                return (str(m[0]) if m else '?'), '(未接 UNETLoader)'
        return '?', '(本图无此采样器)'

    one_id, one = sampler_model('KSamplerAdvanced')
    two_id, two = sampler_model('KSampler')
    used = set()
    for n in g.values():
        for v in (n.get('inputs') or {}).values():
            if isinstance(v, list) and str(v[0]) in loaders:
                used.add(str(v[0]))
    orphan = ['#%s %s' % (k, v) for k, v in sorted(loaders.items(), key=lambda x: int(x[0]) if x[0].isdigit() else 10**9)
              if k not in used]
    return dict(seed=seed, one=one, one_id=one_id, two=two, two_id=two_id,
                same=(one == two), orphan=orphan, mp=mp, ar=ar, size=size,
                md5=hashlib.md5(positive_prompt(g).encode('utf-8')).hexdigest()[:12])

def counts(txt):
    han = sum(1 for c in txt if '\u4e00' <= c <= '\u9fff')
    lat = sum(1 for c in txt if ('a' <= c <= 'z') or ('A' <= c <= 'Z'))
    segs = [l for l in txt.split('\n') if l.strip()]
    return han, lat, len(segs)

def segname(line):
    i = line.find('：')
    return line[:i] if 0 < i < 8 else '(无段名)'

def load_draft(path):
    out = []
    for l in open(path, encoding='utf-8'):
        s = l.strip()
        if not s or s.startswith('#') or s.startswith('---') or s.startswith('```'):
            continue
        out.append(s.replace('**', ''))
    return '\n'.join(out)

def report(path, g):
    p = positive_prompt(g); m = meta(g)
    han, lat, segs = counts(p)
    print('#### %s' % os.path.basename(path))
    print('  种子 %s · 一采 #%s %s · 二采 #%s %s%s' % (m['seed'] or '?', m['one_id'], m['one'],
          m['two_id'], m['two'], '  ← 两遍同档' if m['same'] else '  ← 一采≠二采'))
    if m['orphan']:
        print('  ⚠ 孤儿 UNETLoader（没人引用，不参与出图）：%s' % ' / '.join(m['orphan']))
    print('  %s @ megapixels %s%s · %d 段 · %d 字符 · 汉字 %d · 拉丁 %d · prompt md5 %s'
          % (m['ar'] or '?', m['mp'] or '?', (' · ' + m['size']) if m['size'] else '',
             segs, len(p), han, lat, m['md5']))
    return p

def diff(a, b, la, lb):
    al, bl = a.split('\n'), b.split('\n')
    sm = difflib.SequenceMatcher(None, al, bl)
    print('  相似度 %.1f%%' % (sm.ratio() * 100))
    print('--- 逐段 diff（%s → %s）---' % (la, lb))
    n = 0
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == 'equal':
            continue
        for l in al[i1:i2]:
            print('  [%s]  −  %s' % (segname(l), l))
            n += 1
        for l in bl[j1:j2]:
            print('  [%s]  +  %s' % (segname(l), l))
            n += 1
    if n == 0:
        print('  （逐段完全一致）')
    print('  差异行 %d' % n)

def main(argv):
    if len(argv) < 2:
        raise SystemExit('用法：run-diff.py <这次的图.png> [<上次的图.png> | --draft <稿.md>]')
    p1 = argv[1]
    t1 = report(p1, graph(p1))
    if len(argv) >= 4 and argv[2] == '--draft':
        d = load_draft(argv[3])
        print('--- 图 vs 草稿（%s）---' % os.path.basename(argv[3]))
        diff(d, t1, '草稿', '出图')
    elif len(argv) >= 3:
        p2 = argv[2]
        t2 = report(p2, graph(p2))
        diff(t2, t1, os.path.basename(p2), os.path.basename(p1))
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
