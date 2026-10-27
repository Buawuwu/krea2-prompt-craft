#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LoRA 验证对照表（只读 · 不跑图）
用法: python3 tools/lora-ab.py [output目录] [最多张数]
用途: 扫 ComfyUI output 里的 PNG 元数据，把「底模 / LoRA / 强度 / 种子 / 步数·cfg / 提示词指纹」列成表，
      并按**提示词指纹**分组 → 用户只管跑图，A/B 对照由机器出。
"""
import glob, io, json, os, struct, sys, zlib, hashlib

OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.expanduser("~/ComfyUI/output")
LIM = int(sys.argv[2]) if len(sys.argv) > 2 else 40

def png_text(p):
    d = {}
    with open(p, 'rb') as f:
        if f.read(8) != b'\x89PNG\r\n\x1a\n':
            return d
        while True:
            ln = f.read(4)
            if len(ln) < 4:
                break
            n = struct.unpack('>I', ln)[0]
            typ = f.read(4); data = f.read(n); f.read(4)
            try:
                if typ == b'tEXt':
                    k, _, v = data.partition(b'\x00'); d[k.decode('latin1')] = v.decode('utf-8', 'replace')
                elif typ == b'zTXt':
                    k, _, rest = data.partition(b'\x00'); d[k.decode('latin1')] = zlib.decompress(rest[1:]).decode('utf-8', 'replace')
                elif typ == b'iTXt':
                    parts = data.split(b'\x00', 5)
                    if len(parts) == 6:
                        d[parts[0].decode('latin1')] = zlib.decompress(parts[5]).decode('utf-8', 'replace') if parts[1] == b'\x01' else parts[5].decode('utf-8', 'replace')
            except Exception:
                pass
            if typ == b'IEND':
                break
    return d

def row(p):
    try:
        pr = json.loads(png_text(p).get('prompt', '{}'))
    except Exception:
        return None
    r = dict(file=os.path.basename(p), mtime=os.path.getmtime(p))
    for _, v in pr.items():
        ct = str(v.get('class_type', '')); inp = v.get('inputs', {})
        if ct == 'UNETLoader':
            r['unet'] = str(inp.get('unet_name', ''))
        elif 'LoraLoader' in ct:
            r['lora'] = '%s @%s' % (str(inp.get('lora_name', '')), inp.get('strength_model'))
        elif 'Sampler' in ct:
            r.setdefault('params', []).append('%s步/cfg%s/%s' % (inp.get('steps'), inp.get('cfg'), inp.get('sampler_name')))
            if inp.get('seed') is not None and 'seed' not in r:
                r['seed'] = inp.get('seed')
        elif ct == 'CLIPTextEncode':
            t = str(inp.get('text', ''))
            if len(t) > 120:
                r['ptext'] = t
    r['unet'] = (r.get('unet') or '—').split('\\')[-1].replace('.safetensors', '')
    r['lora'] = (r.get('lora') or '（无）').replace('\\', '/').split('/')[-1].replace('.safetensors', '')
    r['params'] = ' + '.join(r.get('params', [])) or '—'
    if 'ptext' in r:
        r['ph'] = hashlib.md5(r['ptext'].encode('utf-8')).hexdigest()[:8]
        r['phead'] = r['ptext'][:26]
    else:
        r['ph'], r['phead'] = '—', '—'
    return r

files = sorted(glob.glob(os.path.join(OUT, '*.png')), key=os.path.getmtime, reverse=True)[:LIM]
rows = [x for x in (row(p) for p in files) if x]
print('扫到 %d 张（目录：%s）\n' % (len(rows), OUT))
print('%-19s %-26s %-30s %-22s %-7s %s' % ('时间', '底模', 'LoRA @强度', '参数', '提示词', '文件'))
print('-' * 150)
for r in rows:
    import time as _t
    print('%-19s %-26s %-30s %-22s %-7s %s' % (
        _t.strftime('%m-%d %H:%M:%S', _t.localtime(r['mtime'])), r['unet'][:26], r['lora'][:30],
        r['params'][:22], r['ph'], r['file'][:44]))
grp = {}
for r in rows:
    grp.setdefault(r['ph'], []).append(r)
print('\n── 同提示词分组（同指纹 = 可比；组内只该有一个变量）──')
for h, g in grp.items():
    if h == '—' or len(g) < 2:
        continue
    print('\n[%s] %s  共 %d 张' % (h, g[0]['phead'], len(g)))
    for r in g:
        import time as _t
        print('   %s | %s | %s | %s' % (_t.strftime('%m-%d %H:%M', _t.localtime(r['mtime'])), r['unet'], r['lora'], r['params']))
