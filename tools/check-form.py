#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Krea2 出词稿 · 形态 / 下缘 / 姿势机位 / 物锚 / 元信息 / 年龄 / 水词【机器硬查】(⑩–⑰)
用法: python3 tools/check-form.py <稿子.md>      退出码 0=过, 1=不过

为什么有它（2026-10-01）:
  用户原话：「我是真不理解，每次写十段式都会有问题」「这个 skill 提示词你认错多少次了，屡教不改」。
  规则写在 SKILL.md 正文里挡不住（v2.19.18 / 19 / 20 连写三刀，都在同一个坑上翻车）。
  根因：检查项只活在"知识层"，没出现在"交付物"上；而自查是**犯错者自己打勾**，所以永远全绿。
  改法：把两条判据**从我手里拿走，交给机器数**——数字不是助手写的，助手也就改不动。

⑩ 形态选择：形态 B（有段名）必须在稿首自报理由，且**理由必须被正文自证**。
   枚举（`形态选择：B · 理由=<其一>`）：多主体 | 街景 | 全景 | 非对称姿势 | 排他声明 | 叙事元件
   —— 枚举里**没有"单人人像"** → **单主体走十段必然不过**（单主体默认走形态 A，3–6 句）。

⑪ 下缘声明：`画面下缘 / 最近层 / 底部` 这类**同一块画面**的声明，全篇只许 **1 处**。
   十段里只有「前景」要求新增物件、其余九段都在描述已有主体，而「构图」也在描述下缘
   → 模型收到**两个版本的"下缘要有个东西"** → 自己挑一个执行，**挑哪个不可预测**：
     长椅扶手→又大又实 · 无形色块→悬空一坨 · 衣料下缘→放大贴片 · 人→被挤到画面下角。
"""
import io
import os
import re
import sys

SEG_RE = re.compile(
    r'^\*{0,2}(主体|要点|前景|中景|背景|构图|视觉引导|色调|风格|光影氛围|叙事元件)\*{0,2}：')
FORM_RE = re.compile(r'形态选择\s*[:：]')
RSN_RE = re.compile(r'理由\s*[=＝:：]\s*([^ ·|,，。；]*)')
LOW_RE = re.compile(
    r'下缘|最近层|画面底部|画面最下|最下方|底边|画框下|收出画框|切出画框|切下去|裁到|底部')

# 「理由」必须能被正文自证：声明的理由 ≠ 稿子里找得到的证据 → 不过
REASONS = {
    '多主体': r'两个|两位|两人|二人|一对|双人|三个人|三位|三人|一群|人群|他和她|她和他|一男一女|彼此|互相|对方|伴侣|情侣',
    '街景': r'街|巷|马路|路口|店面|招牌|霓虹|行人|城市',
    '全景': r'全景|远景|鸟瞰|俯瞰|广角|辽阔|天际线|地平线',
    '非对称姿势': r'交叉|搭在一起|叠在|岔开|一条腿[^，。；]{0,10}另一条腿|翘起',
    '排他声明': r'画面里只有|画面里没有|墙上没有任何|只有她|只有他',
    '叙事元件': r'分格|气泡|拟声|音效字|空心描边|空心字|条漫|框线|阅读顺序',
}


def body_of(text):
    """与 check-prompt.sh 的 awk 同规则：从「## 主稿」起到判读类标题止；没有则全篇。"""
    out, on = [], False
    for ln in text.splitlines():
        if ln.startswith('## 主稿'):
            on = True
            continue
        if on and ln.startswith('## '):
            if re.search(r'判读|待回写|待落版|待办|阶梯|若这次', ln):
                break
        if on:
            out.append(ln)
    t = '\n'.join(out) if out else text
    # v2.19.25.1：稿首三行元信息（形态选择 / 下缘声明次数 / 挂档）不进画面正文的统计
    return '\n'.join(ln for ln in t.splitlines()
                      if not re.match(r'^\s*(形态选择|下缘声明次数|挂档)\s*[：:]', ln))


def segments(body):
    r = []
    for ln in body.splitlines():
        m = SEG_RE.match(ln)
        if m:
            r.append(m.group(1))
    return r


def low_hits(body):
    """按「段 · 句」扫下缘声明；「要点」段是元信息（不驱动像素），跳过。"""
    cur, hits = '(稿首)', []
    for ln in body.splitlines():
        m = SEG_RE.match(ln)
        if m:
            cur = m.group(1)
            ln = ln[m.end():].lstrip('*').strip()
        if cur == '要点' or not ln.strip():
            continue
        for s in re.split(r'[。；]', ln):
            s = s.strip().lstrip('*').strip()
            if s and LOW_RE.search(s):
                hits.append((cur, s))
    return hits


def main():
    if len(sys.argv) < 2:
        print('用法: python3 tools/check-form.py <稿子.md>')
        return 2
    path = sys.argv[1]
    if not os.path.isfile(path):
        print('找不到文件: ' + path)
        return 2
    text = io.open(path, encoding='utf-8').read()
    body = body_of(text)
    segs = segments(body)
    nseg = len(segs)
    fail = 0

    # ── ⑩ 形态选择 ──────────────────────────────────────────────
    print('⑩ 形态选择（硬项）')
    dline = ''
    for ln in text.splitlines():
        if FORM_RE.search(ln):
            dline = ln.strip()
            break
    if nseg == 0:
        print('✅ ⑩ 未检出段名 → 判为 **形态 A（默认，安全方向）**')
        if dline:
            print('     稿首声明：' + dline[:140])
    else:
        print('ℹ️ ⑩ 检出 %d 段 → **形态 B**，须在稿首自报理由' % nseg)
        if not dline:
            print('❌ ⑩ 形态 B 却没有稿首声明 —— 必须写：`形态选择：B · 理由=<枚举>`')
            print('     合法枚举：' + ' | '.join(REASONS))
            print('     单主体画面（单人人像 / 半身 / 胸像 / 商品图 / 静物）**没有合法理由**')
            print('     → 改走形态 A（3–6 句，七层各一句）；要遮挡 → 出图后裁切')
            fail = 1
        else:
            print('     稿首声明：' + dline[:140])
            m = RSN_RE.search(dline)
            name = m.group(1).strip() if m else ''
            if name in REASONS and re.search(REASONS[name], body):
                print('✅ ⑩ 形态 B 理由「%s」已由正文自证' % name)
            else:
                why = '**不在枚举内**' if name not in REASONS else '**未被正文自证**（稿里找不到对应证据）'
                print('❌ ⑩ 形态 B 的理由「%s」%s' % (name or '(未解析出)', why))
                print('     合法枚举：' + ' | '.join(REASONS))
                print('     单主体画面没有任何合法理由 → **改走形态 A**（3–6 句，七层各一句）')
                fail = 1

    # ── ⑪ 下缘声明次数 ─────────────────────────────────────────
    print()
    hits = low_hits(body)
    n = len(hits)
    print('⑪ 下缘 / 最近层声明次数（硬项 · 须 ≤ 1）')
    if n <= 1:
        print('✅ ⑪ 计数 = %d' % n)
        if n == 1:
            print('     唯一一处 [%s] %s' % (hits[0][0], hits[0][1][:120]))
        else:
            print('     （本稿未声明下缘 / 最近层——可接受；若其实写了，请检查用词是否落在此表内）')
    else:
        print('❌ ⑪ 计数 = %d（须 ≤ 1）—— %d 处都在描述**同一块画面**，模型只会挑一个执行，挑哪个不可预测' % (n, n))
        for i, (seg, s) in enumerate(hits, 1):
            print('     %d. [%s] %s' % (i, seg, s[:140]))
        print('     修法：只留一处。近景 → 留「前景＝主体自身」、删「构图」里裁到哪；')
        print('           全景 → 留「前景＝同质背景」、删「构图」里裁到哪；要遮挡 → 出图后裁切')
        fail = 1


    # ── ⑫ 姿势 × 机位 互斥对（硬项 · v2.19.25 新增）───────────────
    #   起因（2026-10-01）：形态 A 稿写「她头略低着，视线落在画面右下方…」＋「机位与她的视线齐平」
    #   → 出图角度怪。真人册早有「姿势与机位是一件事」，但那条只活在知识层、没出现在交付物上。
    print()
    print('⑫ 姿势 × 机位 互斥对（硬项）')
    PAIRS = [
        (r'(头略低|低着头|低头|垂下眼|垂眼|俯视|视线落[^，。；]{0,14}(下方|下面|膝|杯沿|地面|脚下))',
         r'(机位与[^，。；]{0,6}视线齐平|机位与视线齐平|低机位|仰视|从下往上)',
         '一个"低头 / 视线朝下"的人 + "与视线齐平 / 低机位"的机位 → 只能是低机位仰拍',
         '两条只能留一条：机位句改成「机位与人眼齐平」，或姿势句改成抬头平视'),
        (r'(膝盖朝上|膝头朝上|从身体上方往下|俯拍)',
         r'(脚伸向画面下|脚在画面下缘|画面下缘[^，。；]{0,8}脚)',
         '"膝盖朝上 / 俯拍"与"脚伸向画面下"各自只在一个机位下成立（姿势与机位是一件事）',
         '姿势段与构图段同向：要膝盖朝上 → 机位写俯拍；要脚伸向下 → 别写膝盖朝上'),
    ]
    body_sents = []
    for ln in body.splitlines():
        m = SEG_RE.match(ln)
        if m:
            ln = ln[m.end():]
        for s in re.split(r'[。；]', ln):
            s = s.strip().lstrip('*').strip()
            if s:
                body_sents.append(s)
    hit12 = []
    for a, b, why, fix in PAIRS:
        sa = [s for s in body_sents if re.search(a, s)]
        sb = [s for s in body_sents if re.search(b, s)]
        if sa and sb:
            hit12.append((why, fix, sa[0], sb[0]))
    if not hit12:
        print('✅ ⑫ 未检出姿势 × 机位互斥对')
    else:
        for why, fix, x, y in hit12:
            print('❌ ⑫ 检出互斥对：')
            print('     姿势句：%s' % x[:120])
            print('     机位句：%s' % y[:120])
            print('     为什么不过：%s' % why)
            print('     修法：%s' % fix)
        fail = 1

    # ── ⑬ 窄边 / 悬空 物锚（硬项 · v2.19.25 新增）────────────────
    print()
    print('⑬ 物锚有效性（硬项）')
    NARROW = r'(边沿|沿口|下沿|上沿|棱上|窄边|悬空|没有落点|无处可落|无处可去|悬在)'
    CONTACT = r'(坐在|坐|踩|踏|抵|卡|蹬|压|钉在|锁在|靠在|蹲)'
    hit13 = [s for s in body_sents if re.search(NARROW, s) and re.search(CONTACT, s)]
    if not hit13:
        print('✅ ⑬ 未检出「窄边 / 悬空」物锚')
    else:
        for s in hit13:
            print('❌ ⑬ 窄边或悬空当锚：%s' % s[:130])
        print('     为什么不过：库内实测（n=1~5）——物锚必须是「画面里存在的面」；窄边与缺失锚锁不住几何，模型只能自己折中')
        print('     修法：换成存在的宽面（「坐在靠墙矮台的台面上、台面宽得能放下两只手掌」）或补第二处接触面；实在要那种姿势 → 出图后裁切')
        fail = 1

    # ── ⑭ 稿首元信息三行（硬项 · v2.19.25 新增）──────────────────
    print()
    print('⑭ 稿首元信息（硬项 · 缺 = 没交付完）')
    need = [
        ('形态选择', FORM_RE, '`形态选择：A · 理由=…`（单主体默认 A）'),
        ('下缘声明次数', re.compile(r'下缘声明次数\s*[:：]'), '`下缘声明次数：N`（须与 ⑪ 实测一致）'),
        ('挂档', re.compile(r'挂档\s*[:：]'), '`挂档：<模型名> → 预期年龄读出：<档位表值 或 未登记>`'),
    ]
    miss = [x for x in need if not x[1].search(text)]
    for name, rx, fmt in need:
        print(('✅ ⑭ %s 已写' % name) if rx.search(text) else ('❌ ⑭ 缺 %s' % name))
    if miss:
        print('     必须补在稿首：' + ' · '.join(f for _, _, f in miss))
        fail = 1
    else:
        m = re.search(r'挂档\s*[:：]([^\n]*)', text)
        print('     挂档行：%s' % (m.group(1).strip()[:120] if m else ''))
        if not re.search(r'预期年龄读出', text):
            print('❌ ⑭ 挂档行缺「预期年龄读出」——档位的年龄值是判读基线，必须写出来')
            fail = 1


    # ── ⑯ 年龄锚（硬项 · v2.19.26 新增 · 2026-10-01 改规）──────────
    #   用户原话：「以后必须写年龄，你这个成年看起来起码有50岁」
    #   改规：稿内**必须显式写成年年龄**（22–30 起写）；「成年」这个词本身会被读成 50 岁。
    #   红线不变：仍不得出现幼态年龄信号（未成年 / 少女 / 萝莉 / 学生妹 / 十几岁）。
    print()
    print('⑯ 年龄锚（硬项 · 稿内必须写成年年龄）')
    AGE_OK = re.compile(r'([二三四五六七八九十]{1,3}|[0-9]{1,2})\s*岁|二十(多|出头|上下)|三十(多|出头|上下)')
    AGE_BAD = re.compile(r'(未成年|少女|萝莉|学生妹|(?<![0-9])1[0-7]岁|(?<![0-9])[1-9]岁|(?<![一二三四五六七八九十百千])十[一二三四五六七八九]岁)')
    m = AGE_OK.search(body)
    if m:
        print('✅ ⑯ 稿内有年龄锚：%s' % m.group(0))
    else:
        print('❌ ⑯ 稿内没有写年龄 —— 2026-10-01 改规：**以后必须写年龄**（只写"成年"会被读成 50 岁）')
        print('     修法：在主体句里写具体成年年龄（22–30，例：`二十八岁`），并与档位基调、可量面部特征一起写')
        fail = 1
    b = AGE_BAD.search(body)
    if b:
        print('❌ ⑯ 出现幼态年龄信号：%s —— 成人层红线不许' % b.group(0))
        fail = 1

    # ── ⑰ 水词（硬项 · v2.19.28 新增 · 2026-10-05 定）──────────
    #   来由：用户「把'不许 beautiful/stunning…'从人读变成机器查」。
    #   规格见 references/prose-quality.md §2（源：第三方教学站 output-prose-quality.md，MIT）。
    #   ⚠️ 关键前提（不写清就会做成死代码）：
    #      素材的「机器查表 v0」是**英文**表，而 ① 已经强制正文**零拉丁字母**
    #      → 只查英文，命中数恒为 0。故本项主查**中文对照表 v1**（由 §2.3「空词→落地改写」反推），
    #      英文表 v0 仍一并查（兜底：万一 ① 被绕过，这里还能点名它是"水词"而不是"拉丁字母"）。
    #   豁免口径（**v1 · 助手拟** —— 源只给了「少用或不用，**除非紧跟具体动作/材质**」一句，
    #   没给词边界/大小写/豁免窗口；§2.2 已声明这条是拟定的、待用户校准）：
    #      同一个「分句」（以 。；，、 断）内出现 **强动词 / 材质词 / 光词** → 该处水词豁免。
    #      三类都能落到像素上；「光」是助手加的（§3.2「每段至少 2 层」把光列为同层的"有落点"信息）。
    #   口径校准证据（落版前在 57 份真稿语料上干跑）：真命中 0 处；抓到 2 处误报并修掉 ——
    #      ① `（多留一段腿，好看清比例）` 里的 `好看` 是**子串**（"好看清"≠水词）→ 加 (?!清)
    #      ② 无 `## 主稿` 的回写清单文件不属 check-prompt.sh 的适用范围（非稿子，不管）
    #   已知边界（诚实写在这里，别当成"全查到了"）：
    #      站 / 坐 这类高频动词会把「她站着，很美」放行 —— 本项是**地板，不是天花板**。
    WATER_ZH = [
        '美丽', '漂亮', '好看', '美貌', '绝色', '惊艳', '震撼', '夺目', '华丽', '绝美',
        '艳丽', '完美', '无可挑剔', '惊人', '叹为观止', '可爱', '甜美', '俏丽', '性感',
        '火辣', '妩媚', '撩人', '迷人', '优雅', '高贵', '典雅', '唯美', '氛围感', '高级感',
    ]
    WATER_EN = [
        'beautiful', 'stunning', 'gorgeous', 'perfect', 'amazing', 'lovely', 'sexy',
        'hot', 'elegant', 'beauty', 'stunningly', 'elegance', 'elegantly',
    ]
    # `好看` 要排除「好看清 / 好看得出」这类子串（v2.19.28 干跑抓到：`多留一段腿，好看清比例`）
    WATER_RE_ZH = [(w, re.compile(w + r'(?!清)' if w == '好看' else re.escape(w)))
                   for w in WATER_ZH]
    # 豁免锚：强动词 + 材质 + 光（⚠️ 刻意收窄：不带 转/回/收 这类过泛动词，
    #   否则「她转过头，画面很惊艳」会被放行）
    ANCHOR = re.compile(
        r'压|搭|覆|托|按|夹|垫|抵|贴|搁|捧|握|捏|抓|扶|勾|扣|穿|绕|缠|垂|抬|倾|靠|'
        r'坐|站|蹲|跪|躺|趴|迈|跨|撑|顶|拧|拉|推|拽|提|抱|环|叠|踏|踩|蹬|悬|绷|'
        r'棉|麻|丝|绸|缎|纱|绒|毛|皮|革|呢|布|料|金属|木|石|瓷|陶|玻璃|哑光|亮面|'
        r'织纹|纹理|纹路|褶|帆布|丹宁|雪纺|罗纹|提花|刺绣|珠片|'
        r'主光|辅光|补光|轮廓光|侧光|逆光|顶光|底光|柔光|硬光|窗光|晨光|暮光|夕照|色温|阴影|高光|反光|投影')
    print()
    print('⑰ 水词（硬项 · 空词不驱动像素）')
    # 「要点」段是写给人看的施工说明（里面会合法地出现"别写成很美的空话"这种字样）→ 与 ⑥⑦ 同规则跳过
    body17 = '\n'.join(ln for ln in body.splitlines() if not re.match(r'^\s*\**要点', ln))
    hits17 = []
    for c in re.split(r'[。；，、]', body17):
        c = c.strip().lstrip('*').strip()
        if not c or ANCHOR.search(c):
            continue
        for w, rx in WATER_RE_ZH:
            if rx.search(c):
                hits17.append((w, c))
        low = c.lower()
        for w in WATER_EN:
            if re.search(r'(?<![a-z])' + w + r'(?![a-z])', low):
                hits17.append((w, c))
    if not hits17:
        print('✅ ⑰ 正文无水词（中文表 v1 + 英文表 v0）')
    else:
        print('❌ ⑰ 检出 %d 处水词 —— 空词不落到像素上，模型只能自己编' % len(hits17))
        for w, c in hits17[:8]:
            print('     【%s】%s' % (w, c[:110]))
        if len(hits17) > 8:
            print('     …另有 %d 处' % (len(hits17) - 8))
        print('     豁免口径(v1)：同一分句内出现 强动词/材质/光 即放行 —— 站/坐 这类高频动词会放行')
        print('        「她站着，很美」，所以本项是**地板不是天花板**；要收紧请改本文件 ANCHOR/WATER_ZH')
        print('     修法：按 prose-quality.md §2.3 换成有落点的写法 ——')
        print('       beautiful→柔光下清晰的面部结构 · elegant→重心后坐/颈部拉长/躯干柔和 S 线 ·')
        print('       good lighting→机位左侧大柔主光＋轻补光＋发丝轮廓光 · strong body→硬侧光下的肩线与核心')
        fail = 1

    return 1 if fail else 0


if __name__ == '__main__':
    sys.exit(main())
