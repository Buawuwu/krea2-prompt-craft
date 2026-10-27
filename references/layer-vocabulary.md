# 七层词库（通用层）

> 本文件**只放题材无关的内容**：L1 句式、L2 槽位、L3/L4 通用措辞、L5 光、L6 镜头、L7 媒介、组装模板、通用反模式。
> **题材专属内容一律写在题材分册里**（本册 L1 主体名词表、本册 L2 锚定法、本册 L4 占据物、本册专属反模式），例如 `genre-megastructure.md`、`urban-street.md`。
> ⚠️ 这条边界是维护红线：一旦把某题材的口味写进通用层，它就会污染**所有**题材的产出，且以后每加一个题材都要重读一遍通用层。

---

## L2 · 锚定法（每册自定义的槽位）

L2 是七层里**唯一必须由题材分册定义**的一层。它的任务不是"好看"，而是**让画面可信**。

| 题材分册 | 本册的 L2 锚定法 | 锚什么 |
|---|---|---|
| `genre-megastructure.md` | **尺度锚定** | 让人相信它**大** |
| `urban-street.md` | **时代·地域锚定** | 让人相信它是**真的那条街** |

**通用原则（各册共用）**：

1. **优先用可被看见的具体物**，其次用可测量数字，**最后**才用形容词。形容词（colossal / beautiful / modern / 震撼）对模型的约束力极低。
2. 锚定物要写在**光之后、镜头之前**——此时画面已经铺开，插一个具体物件最能被模型当成实体而非氛围词。
3. 一册写好 L2 之后要写**本册专属的反模式**：凡是"这个题材一眼假"的写法，列出来扣分。

**新增题材时先问一句**：*这个题材"假"在哪里？* 把答案写成锚定手段，就是该册的 L2。
（例：巨构假在"不像那么大"→ 尺度锚定；都市假在"像布景、没人、没时间感"→ 时代地域锚定 + 生活痕迹。）

---

## L1 · CORE 主体

**句式**：`<主体名词>, <形态/结构语法>, <重复单元>, <支撑或立足方式>`

（**主体名词表属题材专属** → 见各题材册）

**通用动词/状态**（加一点更有生命）：`rising out of` · `clinging to` · `striding across` · `half-sunk into` · `overgrown by` · `weathered into` · `collapsing slowly into` · `drifting above` · `flanked by` · `half-hidden behind` · `walled in by` · `cutting through`

---

## L3 · MATERIAL 材质与表面

**模板**：`<主材>, <风化/使用痕迹>, <附着物>, <表面状态>`

（**主材词表属题材专属** → 见各题材册）

> ⚠️ **先选「痕迹的取向」再取词**（2026-09-13 补）：下面三组的词汇**偏衰败向**（v1 巨构册血统）——**"被用过"≠"被毁过"**。四档谱系与默认档、皮肤专用写法、以及对照例，见 `terms-zh.md` 的 **L3 表头**。
> ⚠️ **材质必须逐词写出，而且反向词会把它抹掉**（v2.9.8 新增 · 实测）：
> ① **不写就没有**——只写"装甲/布料/皮革"这类**名词**，模型给的是默认表面（干净、无纹）→ **质感靠"工艺+纹理"的具象词**（`洗旧的深灰粗毛线外套，能看见一针一针的辫子纹路、袖口起了球`）。
> ② **写了反向词就白写**——实测：中景写了 `表面光滑`，同时色调段写 `漆面有橘皮纹、棱边磨出金属底色、接缝积灰` → 出图**光洁得像塑料手办**，质感词**一个都没出来**。**`光滑 / 干净 / 崭新 / 无痕` 这类词与"被用过"的质感是互斥的，同一稿里只能留一边。**
> ③ **微纹理还吃像素**（见 SKILL.md §3.1）：`橘皮纹 · 毛孔 · 织物纹 · 细划痕`属**高频微纹理**，1.0 MP 下多次无效；`锈 · 风化 · 磨损 · 麻点`属**低频大面积材质**，1.0 MP 就出得来。

> ⚠️ **程度 / 量类词会被"放大一档"——一律换成「可数的具体物」（v2.12.0 新增 · 三连实测）**：`细小的毛球`→**磨破大洞** · `一片浅白`→**磨破露纱** · `薄汗`→**像刚冲过水**；改成可数具象物（"两侧膝盖处的布面**各有一道横向的浅色折痕**"）→ **同种子下一次即消**。
> → **凡"量"字打头的词（细小 · 薄 · 一片 · 轻微 · 略）都先怀疑**：改写成**能数出来、能看出来**的东西。**"量"字留给"可数"**（一道折痕 · 两道青筋 · 三颗纽扣），**不留给"程度"**。



> **速记**：①衰败向（风化/锈/剥落/苔）→ 废墟·巨构·老城 ｜ ②**使用向（默认）**：包浆·磨亮·洗旧·起球·压痕·指印·水痕·边角磨圆 ｜ ③生长向：新苔·藤蔓·落花·水汽·湿亮 ｜ ④洁净向：干燥·崭新·未使用·无尘·冷硬光。

**通用风化**（①衰败向）：eroded to rounded edges · pitted and scarred · scorched and blackened · bleached by sun · cracked and spalled · polished smooth by use · stained with drip streaks · salt-crusted · chipped at the corners

**通用附着物/残留**（①衰败向）：accumulated dust in every crevice · dried algae · soot above openings · cobwebs in the corners · vegetation taking hold in the seams

**通用表面状态**（随档取用）：wet and reflective · slick with rain · matte and chalky · dusted with grit · slick with oil · fogged with condensation · scuffed and worn at the edges

**②使用向（默认档·补）**：worn smooth by decades of hands（被几十年的手摸出发亮的包浆）· laundered soft and pilled（洗得发软、起了球）· a crease pressed into the fabric（布料被压出折痕）· fingerprints on the surface（表面留着指印）· a dried waterline（一道干涸的水痕）· corners rounded by use（边角被用圆了）

**③生长向（补）**：new moss and lichen on the stone（石面上新长的苔与地衣）· vines threading the railing（藤蔓穿过栏杆）· fallen petals on the step（台阶上落着花瓣）· dew along the leaf edge（叶缘挂着露）· damp air filming the glass（潮气在玻璃上结成一薄层）

**④洁净向（补）**：bone dry and dustless（干燥无尘）· crisp and unused（崭新未用，边缘锋利）· a surface cleaned to a dull sheen（擦到发哑的干净表面）· hard cold light with nothing in the air（冷硬光，空气里干净得没有一粒尘）

---

### ★ 按媒介选层（2026-09-13 实测 · 最省力的一条规则）

**同一个对象，在不同媒介下要换一套词**——把写实向的层叠到插画媒介上，**不但没用，还会把语气拖硬**。

| 你要的媒介 | **皮肤 / 表面怎么写** | **不要叠的层** |
|---|---|---|
| **写实摄影** | 毛孔 · 细绒毛 · 薄油光 · 小痣 · 细纹（"看得清"这一路） | — |
| **插画 / 彩绘 / 赛璐璐** | **色块 + 笔触的走向**（"皮肤是平涂的色块与笔触"） | ❌ 毛孔 / 绒毛 / 汗毛 / 睫毛影子 / 指节褶皱 |
| **水墨** | 疏笔 · 淡矿物颜料 · 留白；**面不写纹理** | ❌ 照片级皮肤 · ❌ 材质工艺细节 |
| **漫画（黑白）** | 硬边 + 网点 / 实黑的分工；线在皮肤上是**主线与辅线** | ❌ 照片级皮肤 · ❌ 灰阶渐变 |

> **实测（2026-09-13）**：一条插画稿叠了写实皮肤层（毛孔 · 绒毛 · 汗毛 · 睫毛影子 · 指节褶皱）→ **毛孔一根都没出**，用户判语「**太硬了**」；把这一层删掉，画面立刻**软下来**。
> **记忆点**：**写实层只写给写实媒介；"画的味道"靠色块、笔触与光的冷暖。**

## L4 · ENVIRONMENT 环境与占据

**通用大气/天气**：volumetric fog · drifting haze · driving rain · falling ash · salt spray · heat shimmer · still air with visible dust · low cloud · damp air that fogs glass

**通用时间痕迹**：long abandoned · still under construction, scaffolding everywhere · freshly finished · worn by decades of use · half-buried · reclaimed by growth

（**"谁在占据这个空间"属题材专属** → 见各题材册）

---

## L5 · LIGHT 光与大气

**光源方向**：`low sun raking across from the left` · `backlit by a blazing sun` · `single shaft of dawn light` · `lit from below by sodium dock lights` · `god rays piercing the haze` · `overcast diffused light` · `moonlit with cool blue fill` · `self-luminous signage dominating the exposure`

**时间**：`blue hour` · `golden hour` · `dawn` · `pre-dawn cold light` · `high noon harsh light` · `dusk` · `storm light` · `just after rain`

**体积光**：`volumetric shafts through the mist` · `god rays` · `light shaft falling through the opening` · `dusty beams` · `light spilling from a doorway across wet ground`

**对比/色温**：`warm amber against cold blue shadow` · `high contrast, deep crushed blacks` · `soft even light` · `rim light separating subject from background` · `specular highlights along wet edges`

**空气透视**（大场景必写）：`atmospheric perspective with the far section faded to pale blue` · `the distant shapes dissolve into haze`

> 注：近景清晰 → 中景被雾/霭冲淡 → 远端消失，是**深度感**最快的来源。**小空间/室内题材**不需要空气透视，但要写**湿度与反射**（湿地面、玻璃、雾气）来代替它制造层次。

---

## L6 · CAMERA 镜头与构图

**焦距**（Krea 2 真的理解摄影参数，写具体值很有效）

- `14mm` / `16mm` ultra-wide — 极端仰视、强透视畸变（强化高度或压迫感；**要配 `corrected verticals` 否则建筑会歪**）
- `24mm` wide — 环境与主体并重的标准广角
- `28mm` — 巷弄纵深、前景遮挡（**遮挡物怎么写见 `urban-street.md`「前景遮挡怎么写」：小 · 虚 · 无色**）
- `35mm` — 街拍标准，人景关系最自然
- `50mm` — 平实、纪念碑式
- `85mm` / `135mm` — 长焦压缩，把远处的东西压到眼前、把招牌叠在一起
- `100mm macro` — 表面特写
- `tilt-shift` — 微缩/模型感（慎用，会削弱宏大感；除非刻意做"这是模型"的效果）

**角度**：`extreme low angle looking up` · `high aerial view looking down` · `eye level` · `from inside looking out` · `worm's-eye view` · `three-quarter view` · `over-the-shoulder`

**构图**：`subject fills the frame and extends beyond the top edge` · `vertical composition, subject in the right third` · `horizon placed low, vast negative space above` · `symmetrical centered composition` · `framed through an archway in the foreground` · `leading lines receding to a vanishing point` · `layered depth: foreground object → mid scene → far distance` · `shot through a reflection in standing water`

**曝光/质感**：`1/2000s frozen detail` · `long exposure smoothing the water` · `shallow depth of field` · `deep focus front to back` · `anamorphic flare` · `film grain` · `available light, no fill`

---

## L7 · STYLE 风格与渲染

一句话即可，但**必须写出媒介**（不写媒介，模型会随机挑一个）。风格预设见 `references/style-presets.md`（12 组，题材无关）。

**常用媒介词**：cinematic matte painting · photorealistic photograph · documentary street photograph · oil painting · 3D render (Octane / Redshift) · architectural visualization · ink wash painting · gouache illustration · concept art for film · charcoal and graphite study · vintage lithograph poster

---

## 组装模板（通用）

```
<L1 主体 + 形态/结构 + 重复单元>.
<L4 环境 + 天气 + 时间痕迹>.
<L2 锚定：按题材分册的锚定法>.
<L3 材质细节 + 表面状态>.
<L5 光：时间 + 方向 + 体积感 + 空气透视/湿度>.
<L6 镜头：焦距 + 机位 + 构图 + 与画框的关系>.
<L7 媒介 + 调色 + 质感>.
```

**注意**：不用每层都写成独立一句。熟练后把它们自然揉成 3–5 个长句更接近 Krea 2 偏好的自然语言风格；分层只是保证不漏项。

---

## 反模式清单（通用）

- ❌ **元语言**：`This image shows…` / `In this photo…` / `a picture of…`
- ❌ **抽象无物**：`epic, awesome, masterpiece, best quality, 8k, ultra detailed`（这类 tag 对 Krea 2 基本无效，用具体描写替代）
- ❌ **形容词代替具体物**：连续 3 个以上"美/震撼/大气"类词
- ❌ **光源打架**：超过一个主光且没说明强弱关系
- ❌ **层内自相矛盾**：写"浓雾弥漫"又写"远景锐利清晰"；写 `extreme close-up` 又让主体很小
- ❌ **媒介冲突**：`oil painting` + `photorealistic photograph` 同时写，结果必漂移

（**题材专属反模式** → 见各题材册）
