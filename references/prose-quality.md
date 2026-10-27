# 正文/散文质量规范（中文草稿）

> **性质**：草稿，供用户中文 ComfyUI 提示词体系吸收用。
> **素材来源**：第三方英文 Krea2 教学站 `skills/figure-photo-prompt/references/output-prose-quality.md`（SFW 全谱人体摄影 · 约 23KB）。
> **范围纪律**：本稿**只收形态无关**的文字质量标准；**全部与英文四段版式绑定的要求已剔除**（见 §6 剔除清单）。
> **不确定标记**：【外来 · 未验】= 素材内容，未经用户体系实测确认；【未明】= 素材本身没给。

---

## 1. 正文质量五标准（强制自检｜已中文化）

| # | 标准 | 合格 | 不合格 |
|---|------|------|--------|
| 1 | **可视** | 每句能对应画面里**一块像素** | 「非常美」「氛围惊艳」这类空喊 |
| 2 | **具体** | 有**可替换的名词/动词/方位** | 「一个女人在摆姿势」 |
| 3 | **单帧** | **一个瞬间**，无 then / after / begins to | 时间线剧本（先…然后…开始…） |
| 4 | **姿态优先** | **重心 + 肩髋 + 手位**可读 | 只写脸美、环境大 |
| 5 | **密度** | 信息密、少水词 | 同义反复、标签刷屏 |

> 口径说明：素材原文说该五标准「适用于 Krea 2 与 Seedream 的形态 A（同一套五标准）」，并自称**强制自检**。素材亦声明「不是私房文案课」——健身、街拍、芭蕾、工地、航拍**各自有合格正文标准**，即五标准是**下限**，不替代题材逻辑。【外来 · 未验】

---

## 2. 水词黑名单 与 改写示例

### 2.1 黑名单原文（英文词表 · 保留原文）

素材口径：**正文少用或不用**，除非**紧跟具体动作/材质**。

```
beautiful, stunning, gorgeous, perfect, amazing, lovely, sexy, hot, elegant
```

### 2.2 机器可查词表（**已机器化 · v2.19.28**）

> **落地状态**：已接进 `tools/check-form.py` 的 **⑰ 硬查**（`tools/check-prompt.sh` 会跑）；命中即判不过。
> **⚠️ 落地时发现的关键前提**：下表 v0 是**英文**表，而 `check-prompt.sh` ① 已强制正文**零拉丁字母** ——
> **只查英文，命中数恒为 0（等于死代码）**。故 ⑰ 主查**中文对照表 v1**（由 §2.3「空词→落地改写」反推），
> 英文表 v0 一并查、只作兜底（万一 ① 被绕过，还能点名它是"水词"而不是"拉丁字母"）。

**中文对照表 v1（⑰ 实际查的表 · 29 词 · 由 §2.3 反推）**

```
美丽 漂亮 好看 美貌 绝色 惊艳 震撼 夺目 华丽 绝美 艳丽
完美 无可挑剔 惊人 叹为观止
可爱 甜美 俏丽
性感 火辣 妩媚 撩人 迷人
优雅 高贵 典雅 唯美 氛围感 高级感
```

> ⚠️ `好看` 加 `(?!清)` 守卫 —— 干跑时抓到 `（多留一段腿，好看清比例）` 被误判（"好看清"不是水词）。
> ⚠️ 刻意**不收** `cool / good / strong / nice / 质感 / 精致 / 端庄` 这类：它们需要
> 「是否跟了具体名词」的上下文判断，误报率高；要收得先给判定规则（见 §7 待定项）。

**英文表 v0（素材原文 · ⑰ 一并查）**

```
beautiful
stunning
gorgeous
perfect
amazing
lovely
sexy
hot
elegant
```

**豁免口径（v1 · 助手拟 · 源只给「少用或不用，除非紧跟具体动作/材质」一句）**：
**同一个「分句」（以 `。；，、` 断）内出现 强动词 / 材质词 / 光词 → 该处水词豁免。**
- **词边界 / 大小写**：英文按**整词**匹配（不看词干 → `stunningly` / `beauty` 单列）；中文按**子串**。
- **「光」是助手加的**：§3.2 把「光在体积上」与形状/表面/接触并列为同层信息，属同类"有落点"词。
- **已知边界（诚实记录）**：`站 / 坐` 这类高频动词会把「她站着，很美」**整句放行**
  → ⑰ 是**地板，不是天花板**。要收紧就改 `check-form.py` 的 `ANCHOR` / `WATER_ZH`。
- **口径校准证据**：落版前在本地 **57 份真稿**（未随仓库发布）上干跑 → **真命中 0 处**（2 处误报已修）。

### 2.3 空词 → 落地改写（对照表）

| 空词 | 落地写法（英文原文保留） | 中文义 |
|------|--------------------------|--------|
| beautiful | `clear facial structure under soft key, calm open expression` | 柔光下清晰的面部结构、平静舒展的表情 |
| elegant pose | `weight back, elongated neck, soft S-curve through torso` | 重心后坐、颈部拉长、躯干柔和 S 线 |
| cool outfit | `camel wool coat, black turtleneck, straight trousers, leather boots` | 驼色羊毛大衣、黑色高领、直筒长裤、皮靴 |
| good lighting | `large soft key from camera-left, gentle fill, hair rim` | 机位左侧大柔主光、轻补光、发丝轮廓光 |
| strong body | `defined shoulders and core under hard side light, athletic stance` | 硬侧光下清晰的肩线与核心、运动站姿 |

**素材给出的单例改写（原文）**：

```
elegant → spine long, chin slightly lifted, fingers relaxed along the coat lapel
```

### 2.4 素材自带的「禁止写法」样例（形态无关部分）

- 标签墙：`1girl, beautiful, masterpiece, best quality, elegant` —— **禁**。
- `score_9` / hashtag 墙 —— **禁**。（素材把它列在交付前质检里，与版式无关）

---

## 3. 形态无关的正文规则（逐条中文化）

### 3.1 动词要强

素材推荐动词（保留原文）：`leans / shifts / twists / plants / elongates / frames / rests / grips / arches / steps`
少用（保留原文）：`is being, looks beautiful, appears elegant`

### 3.2 感官层次：每段/每块至少 2 层

| 层 | 例（英文原文） | 中文义 |
|----|----------------|--------|
| 形状/姿态 | `soft S-curve, weight on back foot, elongated neck` | 柔和 S 线、重心落在后脚、颈部拉长 |
| 表面 | `wool texture, matte jersey, fine dry skin sheen` | 羊毛纹理、哑光针织、细腻干爽肤光 |
| 接触 | `fingers hooked in pocket, palm on hip bone` | 手指勾在口袋、掌心按在髋骨 |
| 光在体积上 | `key light sculpting the near cheek and collarbone` | 主光在近侧脸颊与锁骨上塑形 |

### 3.3 环境不抢戏

- 环境**服务主体、不装修**。
- 锚点数量：**2～5 个锚点**；墙/窗/街/器材**各最多一句特质**；**时代杂物最多 1 个**。
- **避免逐件描写品牌与地毯花纹**。
- 素材的比例口径（原文）：人物 70% 篇幅，环境只留 `large window, pale wall, wood table edge, soft city bokeh`。

### 3.4 可画清单（写完对照 · 10 项）

写完后应能勾选 **≥6 项**；**缺 3 项以上 → 正文不合格，补写再交付**。

- [ ] 年龄/成人身份
- [ ] 人种：默认 East Asian，或用户指定
- [ ] 头～哪一截身体在画内
- [ ] 重心落在哪只脚（或坐姿承重点）
- [ ] 肩与髋的相对朝向
- [ ] 手在做什么
- [ ] 服饰材质 + 一个细节
- [ ] 表情/眼神
- [ ] 主光打在哪块体积
- [ ] （全身时）脚是否在画内

### 3.5 篇幅与压缩纪律（形态无关部分）

| 规则 | 内容 |
|------|------|
| 偏短缺重心/光 | **补层，不补水词** |
| 偏长 | 砍装修与重复，**勿砍姿态/主光** |
| 硬底线 | 主体部分须可指认 **动作 + 材质 ≥1 + 光落点** |

> 【外来 · 未验】素材另给了逐段字数（`This is a` 35–70 词 / Main 100–180 词 / 环境 40–80 词 / 构图 40–75 词 / 全文默认 200–380 词等）。这些**数字与四段版式绑定**，本稿**不作为规则收录**；仅记录于此，待定是否移植为形态 A/B 的字数参照。

### 3.6 交付前正文质检（剥掉版式项后的剩余勾选项）

- [ ] 无水词堆砌
- [ ] 有强动词与方位
- [ ] 单帧无 then
- [ ] 有重心与肩髋关系
- [ ] 成人身份明确
- [ ] 人种已写（默认东亚 / 用户覆盖）
- [ ] 服饰状态精确
- [ ] 主光方向可读
- [ ] 动作与主光未因压缩丢失
- [ ] 无色情升级（SFW）
- [ ] 无 score_9 / hashtag 墙

### 3.7 附带收录的中文释义质量（素材形态无关部分）

素材对「中文释义」的定位是**给用户读的导演/摄影师说明，不是英文机翻**：

| 条 | 要求 |
|----|------|
| 本次分支/组合包 | 一行点名 |
| 镜头 | 角度景别画幅，说人话 |
| 主体 | **重心→肩髋→手→衣→表情**，与正文同构 |
| 勿 | 大段重复英文专有名词不解释 |
| 可 | 点明「防崩：一手插袋」「光：窗光主+脸亮」 |
| 长度 | 素材口径：英文的 40–70%，清楚即可 |

> 提醒：上表「本次分支/组合包」一行来自素材的**组合包**概念。用户体系若不用组合包，这一行作废，其余五条可留。

---

## 4. 姿态/重心/手位/材质/表情/光 词库（保留英文原文 · 按用户体系单独列）

> **收编口径**：这些是**英文词表**，按用户体系规范「英文词表保留原文、单独列」，出词仍写中文。

**姿势 / 重心**
```
weight on the back foot · front knee soft · hip gently popped · soft S-curve ·
three-quarter angle to camera · spine long · chin slightly lifted · mid-stride ·
seated on the edge · one sole against the wall · contrapposto
```

**手 / 肢体**
```
one hand in the pocket · fingers lightly on the hip · hand resting on the railing ·
arms relaxed at her sides · holding the strap of a bag · elbows soft not locked ·
negative space between arm and torso
```

**服饰 / 材质**
```
camel wool coat hanging open · sharp tailored lapel · matte jersey cling of a sports top ·
pressed crease of trousers · knit texture catching side light · silk drape · wind lifting the hem
```

**表情**
```
calm eyes meet the lens · soft half-smile · gaze toward the key light ·
focused athletic concentration · candid mid-expression · looking over the near shoulder
```

**光（写在体积上）**
```
soft window key on the near cheek · Rembrandt triangle under the far eye ·
butterfly light under the nose · hard side light defining the deltoid ·
rim light separating hair from backdrop · golden hour warm key, long soft shadows
```

---

## 5. 差 → 好（正文改写示例 · 已中文化说明）

> 本节两例取自素材 §4 的差→好对照，**已剥掉四段标签**（原文带 `Main subject:` 前缀），只留句子本身，以免把版式带进来。

### 5.1 空泛时尚

**差**（原文，已剥标签）：
```
A beautiful Asian woman in a nice outfit posing elegantly, stunning, masterpiece.
```
**好在哪**（对照五标准逐条）：水词 3 个（beautiful / nice / elegantly）+ 空喊 1 个（stunning）+ 标签 1 个（masterpiece）；标准①②③④⑤全不合格。

**好**（原文，已剥标签）：
```
An East Asian woman in her early twenties stands full-body in frame; long straight black hair falls behind one shoulder. Weight rests on her back leg, front knee soft, near shoulder angled toward the camera while the opposite hip gently pops, forming a soft S-curve. One hand rests lightly on her hip, the other hangs relaxed with fingers slightly curled. She wears a camel wool coat over a black knit turtleneck and straight trousers; the coat hangs open, belt loose. Calm eyes meet the lens, mouth soft, chin slightly lifted under clean butterfly-soft key light.
```
**好在哪**：①每句可落像素 ②具体名词/方位齐 ③单帧 ④重心+肩髋+双手可读 ⑤密度高、零水词；并含材质（wool/knit）与光落点（butterfly-soft key）。

### 5.2 有姿势但不可读

**差**（原文）：
```
She is standing in a cool pose in the gym looking strong.
```
**好**（原文）：
```
She plants a wide athletic stance in the gym, front knee bent in a controlled lunge, back leg long; torso upright, shoulders stacked over hips. Both hands grip a barbell at hip height, knuckles forward. A matte black sports bra and high-waist training shorts read clearly; a fine sweat sheen catches hard side light along her deltoid and oblique. Focused eyes look past the camera, jaw set without grimace.
```
**好在哪**：强动词 `plants / grip`；重心与肩髋关系成句；双手动作具体；材质（matte black / sweat sheen）+ 硬侧光落点在**三角肌与腹斜肌**；表情可读（`jaw set without grimace`）。

### 5.3 环境抢戏

**差**：用 200 词描写咖啡馆菜单与墙纸。
**好**：人物占 70% 篇幅；环境只留 `large window, pale wall, wood table edge, soft city bokeh`。

---

## 6. 剔除清单（从素材中**不收录**的部分）

**A 类 · 英文四段版式合同（与用户形态冲突，全部剔除）**

- 四标签固定顺序与齐全要求：`This is a…` / `Main subject:` / `Environmental background:` / `Composition and atmosphere:`；缺 Env、改名 Subject 即不合格。
- **段间空一行**、禁止四段粘连。
- 首句模板：`This is a [angle] [distance] [aspect] [still] with [photography type]: …`，以及「首句 = 角度+景别+画幅 + with 摄影类型 + 定格瞬间」。
- 「Main 以 `An adult…` 起、≥3 句全链」这类**固定起手式与句数**要求。
- 逐段字数与句数分配表（`This is a` 1 句 35–70 词、Main 100–180 词 3–8 句、额外角色 25–55 词 1–2 句、Env 40–80 词、Comp 40–75 词、全文 200–380 词、420 词起砍 Env）。
- `Composition and atmosphere` 段内的 6 条强制项（占框/绝对视觉中心/主光+fill+rim/景深虚化对象/情绪张力+色盘/质量词+静帧类型）——**其中「质量词 + 静帧类型：masterpiece, best quality, photoreal editorial still」属标签墙，一并剔除**。
- 第二人段「独立段 + 空行 + 只写相对位置/互动手势/距离」的**段落组织**要求。
- 首句摄影类型断言（`editorial / documentary / sports / beauty / street photography`）作为**必写项**的地位。

**B 类 · 形态/平台相关（剔除或仅备注）**

- 「形态 B 短密」整节（素材 §7：单行长串逗号堆叠示范 + 「未指定人种时保留 East Asian / Asian Adult、禁止默认 Caucasian」）——**版式专属**。但其中**「未指定人种不默认 Caucasian」这条取值规则本身与版式无关，已上移到 §3.4 可画清单的人种项**。
- Seedream 平台差异（「Seedream：A 可；鼓励 B，约 30–100 / 5.x 约 50–150 词」）——平台相关，不收录。
- 「形态 E 一套写真分镜」节——分镜形态专属，不收录。
- §11 各「按大区填空」的正文骨架模板（时尚全身/环境职业/运动相位/舞蹈/剪影/私房/舞台色光/攀岩/短光肖像/日系空气/韩系街拍/概念色块/江南旅拍/OOTD/全身镜自拍/窗边私房）——全部是**四段骨架填空模板**，剔除。
- §10 完整金样五例（时尚棚拍/环境职业人像/运动腾空/芭蕾排练/航拍点景）——均为四段完整示范，**不收录正文**；其中**可复用的形态无关技法已抽入 §3/§5**。
- §12 中文释义金样结构（含 `**本次分支/组合包**`、`**画幅建议**：竖 3:4` 的固定栏位）——栏位版式，不收录；释义的**质量要求**见 §3.7。

**C 类 · 素材自身的索引/元信息（不收录）**

- 素材开头「本文件约束形态 A 英文四段与形态 B 短密」的范围声明；「三 skill 统一版式」引用块；指向 `krea2-qwen-te-layered-prompt.md`、`young-asian-women-catalog.md`、`east-asian-portrait-systems.md`、`social-lifestyle-portrait.md`、`asian-young-woman-p0-p2.md` 的外链；「三 skill 统一版式（figure / youth / erotic）」表述。

---

## 7. 不确定 / 待定 → **✅ 已清账（2026-10-06 · 「别整一堆选项」，助手逐条定）**

1. **五标准的"合格 / 不合格"**：**已定 —— 不升为体系铁律**，只作本册参考。理由：`SKILL.md` §1.3 已有 41 条更细的自查，五标准是它们的上位概括，升为铁律只会重复。
2. **黑名单豁免的机器判定规则**：**✅ 已落地（v2.19.28）** —— 英文按整词 / 中文按子串 · 豁免窗口＝同一分句内有 强动词 / 材质 / 光；已接进 `tools/check-form.py` **⑰ 硬查**，并在 57 份真稿上干跑校准（真命中 0）。
3. **字数口径**：**已定 —— 不移植素材的英文词数口径**（与四段版式绑定、素材无中文换算，不能臆造）；**只给形态 B 一个中文上限：≤ 900 字【仅示意 · 助手拟】**，写在本册供出稿自查；**不进 `SKILL.md` 硬项**（目前没有字数机器查）。
4. **「成人身份明确 / 人种默认东亚 / SFW 无色情升级」三条**：**已定 —— 不新增条款**（现状：§3.4 可画清单里已有"年龄 / 成人身份"与"人种默认东亚"，"无色情升级"归 §3.6）。理由：与**成人层 5 条红线** ＋ **⑯ 年龄硬项**重复，再加会三处打架。
5. **素材题材分区 A–I**：**已定 —— 不用**。库按题材分册（真人 / 漫画 / 巨构 / 武侠仙侠 / 都市），再引一套分区＝两套并存。
6. **要不要吸素材 §11 的日系 / 韩系写法**：**已定 —— 分类处置**（⚠️ 2026-10-06 **当日两次更正**后定稿）。
   **① 光位：已经吸过了 → 不重复吸** —— `lens-lighting.md` 内有 `日系逆光溢光`（`jp-backlit-flare`）· `韩系水光高键`（`kr-beauty-highkey`）· `日系奶油窗光`（`ea-jp-cream-window`）· `韩系高键玻璃肌`（`ea-kr-highkey-glass`）· `韩系开阔阴影`（`ea-kr-open-shade`）· `韩系概念色胶`（`ea-kr-concept-gel`）。
   **② 妆 / 调色 5 条：库内确实没有 → 可吸（待补）** —— `jp_bite` 日系咬唇 · `jp_cream` 日系奶油 · `kr_glass` 韩系水光（**妆值**）· `kr_3pt` 韩三点 · `kr_clean` 韩系干净亮；**逐条搜过全库，"咬唇 / 奶油肌 / 玻璃肌 / 三点妆 / 干净亮"作为妆 · 调色值一条都没有**（"奶油/水光/玻璃肌"只在**光位**里出现）。它们与 `terms-zh.md` / `style-presets.md` 同族（**形态无关的词表值**）→ 补进词表即可，与形态 A/B 无关。
   **③ 组合包那一批：不吸** —— `jp-airy-window` / `kr-glass-studio` / `jp-hotel` / `kr-office-chic` / `jp-mori-forest` … 素材把它们组织成 `zone / combo / pose / cloth / prop / set / light` **一整套点菜**，属 v2.19.27 已剔除的**"组合包 / 网站 UI"边界**，不合库内形态。
   **④ 红线点在这里（不是"日韩写法"整体）** —— 素材日韩条目里**确有擦边变体**：**`jp-airy-lewd` · `kr-glass-lewd`** → **这类一律剔**。
   ⚠️ **两次更正留痕**：初稿写"含年轻化描述 → 触红线"（**错**：素材 `未成年 / teen / loli / 校服` 全是**禁止 / 排除口径**，它自己就是 adult-locked）；二稿写"四段骨架模板 → 不吸"（**也不准**：真正不合的是**组合包机制**，而**妆 / 调色 5 条是真缺、可吸**）。**教训**：凡"触红线 / 不吸"这类定性，**先逐条查"库内有没有、素材原文怎么说"，再开口**。
