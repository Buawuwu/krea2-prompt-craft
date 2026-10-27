#!/usr/bin/env python3
# ─────────────────────────────────────────────────────────────
# 色调三项 · 把「旧/新」落成可比数（2026-09-19 · 为「甲照库 vs 乙当代」对照写）
#
#   本机无 PIL / numpy / cv2 → 纯 Python（zlib + struct）自己解 PNG。
#   用法:  python3 tone3.py <图1.png> [图2.png ...]        # 整幅
#          python3 tone3.py --box x0 y0 x1 y1 <图1.png> …  # 指定区域（判读段位不同不可比）
#
#   三项读数:
#     平均亮度 L        —— 偏亮/偏暗
#     平均 (R−B)        —— 正=偏暖（旧胶片向）· 负=偏冷（当代冷白向）★ 主判别项
#     暖色像素占比      —— R−B>25 且 R−G>8 且 L>70（与 rust.py 同口径）
#     平均彩度 C        —— max(RGB)−min(RGB)，看"灰不灰"
# ─────────────────────────────────────────────────────────────
import struct, zlib, sys

def load(p):
    d = open(p, 'rb').read(); i = 8; idat = b''; w = h = ct = bd = None
    while i < len(d):
        ln = struct.unpack('>I', d[i:i+4])[0]; typ = d[i+4:i+8]; data = d[i+8:i+8+ln]
        if typ == b'IHDR': w, h, bd, ct = struct.unpack('>IIBB', data[:10])
        elif typ == b'IDAT': idat += data
        elif typ == b'IEND': break
        i += 12 + ln
    raw = zlib.decompress(idat)
    ch = {0: 1, 2: 3, 3: 1, 4: 2, 6: 4}[ct]; bpp = ch * (bd // 8); stride = w * bpp
    out = bytearray(); prev = bytearray(stride); pos = 0
    for _ in range(h):
        f = raw[pos]; pos += 1; line = bytearray(raw[pos:pos+stride]); pos += stride
        if f == 1:
            for x in range(bpp, stride): line[x] = (line[x] + line[x-bpp]) & 255
        elif f == 2:
            for x in range(stride): line[x] = (line[x] + prev[x]) & 255
        elif f == 3:
            for x in range(stride):
                a = line[x-bpp] if x >= bpp else 0
                line[x] = (line[x] + ((a + prev[x]) >> 1)) & 255
        elif f == 4:
            for x in range(stride):
                a = line[x-bpp] if x >= bpp else 0; b = prev[x]; c = prev[x-bpp] if x >= bpp else 0
                pa = abs(b-c); pb = abs(a-c); pc = abs(a+b-2*c)
                pr = a if (pa <= pb and pa <= pc) else (b if pb <= pc else c)
                line[x] = (line[x] + pr) & 255
        out += line; prev = line
    return w, h, bpp, bytes(out)

def metrics(path, box=None, step=2):
    w, h, bpp, px = load(path)
    x0, y0, x1, y1 = box if box else (0, 0, w, h)
    x1 = min(x1, w); y1 = min(y1, h)
    n = 0; L = RB = C = 0.0; warm = 0
    for y in range(y0, y1, step):
        base = y * w * bpp
        for x in range(x0, x1, step):
            o = base + x * bpp
            R = px[o]; G = px[o+1]; B = px[o+2]
            l = 0.299*R + 0.587*G + 0.114*B
            hi = R if R > G else G
            if B > hi: hi = B
            lo = R if R < G else G
            if B < lo: lo = B
            L += l; RB += (R - B); C += (hi - lo)
            if (R - B) > 25 and (R - G) > 8 and l > 70: warm += 1
            n += 1
    name = path.split('/')[-1]
    return dict(name=name, size=f'{w}×{h}', n=n, L=L/n, RB=RB/n, C=C/n, warm=100.0*warm/n)

def show(r):
    print('%-42s %-11s 亮度 %6.1f | 平均(R−B) %+7.2f | 暖色占比 %5.2f%% | 平均彩度 %5.1f'
          % (r['name'][:40], r['size'], r['L'], r['RB'], r['warm'], r['C']))

if __name__ == '__main__':
    a = sys.argv[1:]
    box = None
    if a and a[0] == '--box':
        box = tuple(int(v) for v in a[1:5]); a = a[5:]
    if not a:
        print(__doc__ or '用法: python3 tone3.py [--box x0 y0 x1 y1] <图1.png> ...'); sys.exit(2)
    for p in a:
        show(metrics(p, box))
    if len(a) >= 2:
        print('\n★ 主判别项 = 平均(R−B)：**数字更负的那张更「当代」**；暖色占比同向。')
