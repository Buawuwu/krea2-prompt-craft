# 都市分册（都市街头 Urban / Street）

> 本册 = **都市题材专属内容**。通用骨架见 `SKILL.md`，通用词库（L1 句式 / L3 通用风化 / L5 光 / L6 镜头 / L7 媒介）见 `layer-vocabulary.md`，风格预设见 `style-presets.md`。
> 本册的 L2 锚定法 = **时代·地域锚定**。
> 边界：本册**不做人像主体**（人物只作为"这里有人在生活"的证据）；不做漫画/插画风（另册）。

---

## 本册的 L2 锚定法：时代·地域锚定

**都市题材"假"在哪里**：不是不够大、不够华丽，而是**像影视城的布景**——干净、对称、没人、没有时间感。观众一眼就看出"这不是真的街"。

所以本册的 L2 不锚尺寸，锚**"这里是哪儿、什么时候"**。四件事，**至少写中两件**：

### 1. 地标与符号物（最有效）

一个**具体的、有年代感的物件**，胜过十个"现代都市"形容词：

`a red post box of the old colonial pattern` · `a green metal street sign with white characters` · `utility poles strung with tangled cables` · `a fire hydrant painted over so many times it has lost its shape` · `a stone bollard worn shiny at the top` · `a public telephone with a missing handset`

> 原则：符号物要**可被指认**（什么形状、什么颜色、什么材料）。`modern city` / `繁华都市` 这类词对模型没有约束力，等于没写。

### 2. 年代符号

`CRT monitors glowing in a shop window` · `a payphone` · `vinyl banners faded to pink` · `a hand-painted shop sign`（旧） ↔ `electric scooters parked in a row` · `QR code stickers on every surface` · `a delivery rider's insulated box`（当代）

> 年代符号决定"这是哪一年"。不写年代，模型会给你一个**无年代的通用都市**——这正是塑料感的来源。

### 3. 文字与语言（最直接的地域信号）

画面里出现招牌/涂鸦/报纸时，**写出具体文字**并**放进双引号**（Krea 2 硬规则 3）：

`a shop sign in Chinese characters reading "面馆"` · `a poster reading "禁止停车"` · `a neon sign reading "OPEN 24H"`

> 不确定真品牌名就用通用词 + 文字内容。**别写真实商标**（会触发奇怪的复现）。

### 4. 气候与季节

`damp after rain, everything still dripping` · `the heavy humidity before a summer storm` · `dry grit and dust in late summer` · `breath fogging in the cold` · `salt air near the harbour`

> 气候决定**反光、雾、湿度**三件事，而这三件事是都市画面层次的主要来源。

**通用锚定原则**（优先具体物 > 数字 > 形容词）见 `layer-vocabulary.md` 的 L2 一节。

### 5. 排他句（"不要什么"只能写进正向句）

**原理**：本机 `cfg = 1.0`，**负面提示词在数学上无效**（负面框填了不起作用，详见 `SKILL.md` §3.3）。所以想排除某样东西，**只能写进正向句**。

| 不要什么 | 正向句怎么写 |
|---|---|
| 不要人（要空景） | `空无一人` / `without any people, the street completely empty` |
| 不要现代高层 | `楼群全是低层旧楼，没有一栋是玻璃幕墙大厦` / `none of the buildings are glass office towers` |
| 不要商业霓虹 | `只有零星几盏招牌灯，没有大面积广告屏` |
| 不要"干净"（要旧） | `every surface worn, patched and stained by use` |
| 不要画面出字 | `墙上没有任何文字、标语或招牌字` |

> **首验踩过的坑**：那条词没写"不要玻璃高楼"，模型就在远景自行加了现代 CBD 塔楼，与"老城天台"的语境打架。**没说不要，就等于允许。**

---

## 本册 L1 · 都市主体与形态语法

**主体/空间类型**：街道与巷弄 · 十字路口与人行横道 · 人行天桥与立交桥下 · 地铁站与地下通道 · 天台与消防梯 · 店内外（便利店 / 面馆 / 理发店） · 老居民楼外廊 · 菜市场 · 停车场 · 江边步道 · 楼群天际线（远景）

**形态/结构语法**（写"围合感"与"纵深"，相当于巨构册的"结构可读性"）：

`a narrow street walled in by six-storey walk-ups` · `a canyon of glass towers with the sky reduced to a strip` · `a stepped alley descending between shophouses` · `an elevated highway casting the street below into shadow` · `a covered arcade running the length of the block`

**重复单元**（至少写 2 个，防止糊成一团）：

`rows of identical air-conditioner units` · `repeating window bays in a bare concrete facade` · `shop signs stacked vertically along a pole` · `evenly spaced street lamps` · `fire escapes zigzagging down the facade` · `paving tiles in a strict grid`

---

## 本册 L3 · 都市材质与痕迹

**地面**：wet asphalt with mirror reflections · cracked concrete with weeds in the seams · worn terrazzo steps · patterned paving tiles · cobblestones polished by traffic · oil-darkened garage floor · tactile paving strips

**墙面**：tiled facade grimy with exhaust · peeling painted plaster · rust-streaked roller shutter · hand-painted signage layered over older signage · stained concrete with drip marks · bare brick patched with cement

**玻璃与金属**：steam-fogged glass · scratched acrylic · aluminium window frames gone matte · tangled overhead wiring · stainless steel smeared with fingerprints · shutters chained and padlocked

**软性细节**（都市画面的"呼吸"）：plastic bags snagged on a fence · laundry hanging in rows · puddles holding a strip of sky · cigarette butts clustered at a doorway · a mop and bucket left outside

---

## 本册 L4 · 生活痕迹（occupancy）

**这是本册最要紧的一层**——都市的"真"来自**有人在用这个空间**。至少写 2 个：

`a bicycle leaning against the wall` · `a delivery rider's insulated box resting on the kerb` · `stalls half-packed at closing time` · `an umbrella left open to dry` · `a shopkeeper hosing down the pavement` · `a cat on a windowsill` · `chairs stacked on a table` · `a short queue at a counter` · `steam venting from a noodle shop` · `laundry and mops on a balcony` · `a plastic stool doubling as an ashtray`

> ⚠️ **默认：occupancy ≠ 加主角**。街道上的背影、路人、局部身影只是"这里有人生活"的证据——**默认不写脸、不写正脸特写、不放在画面正中**。这也顺带避开了 Krea 2 硬规则 7 的"人物得体"问题。
>
> **例外（用户明确要人像主体时）** → 走下面一节，**不要**沿用默认写法。

### 人物主体怎么写（2026-09-13 首验后新增）

**先过一条铁律：姿态体裁必须与媒介匹配。**

| 媒介 | 配什么姿态 |
|---|---|
| 写实摄影 / 街拍式自然质感 | **抓拍中的某一瞬**——正在做一个动作、被叫住回头、低头点烟 |
| 电影感概念摄影 / 时尚大片 | 仪式感姿态（对称、舒展、静态）才成立 |

> **首验踩到的坑（实例）**：媒介写"写实摄影、街拍式自然质感"，姿态却写"双臂向两侧平展张开、掌心朝上、身体展开成十字形"——模型**一字不差照做了**，但在写实街拍语境里读出来就是 **T-pose 摆拍**。**不是模型不听话，是两种语言互相打架。**

**❌ 摆拍信号（写了就出"AI 摆姿感"，首验实测确认）**：
`双臂对称平展张开` · `掌心朝上摊开` · `正面对镜站定` · `身体展开成对称的十字形` · `人物居中且轮廓完整`

**✅ 正向写法四条**：

1. **写动作的因果与重心**：`一只手撑在栏杆上，身体前倾，重心落在后脚`（不是"站着"，是"正在做某事，因此身体这样"）
2. **手里有东西**：`hand resting on a plastic stool` · `holding a phone up to the light` —— 手有事做，姿态自然就真
3. **人景关系**：人物要**嵌在环境里**，而不是"站在环境前面"。写出他与周围物件的**接触点**（靠着、扶着、跨过、回头看向某块招牌）
4. **视线有落点**：看向画面外的某物、看手机、低头看水洼；**避免"直视镜头站定"**（那是证件照语言）

**范例（写实街拍 · 人物为主体，可直接抄结构）**：

> 一个穿旧夹克的年轻人蹲在天台矮墙边收晾干的衣服，一只手把衣架从绳上摘下来，另一只手虚扶着绳，重心压在右脚，肩膀因为伸手而略微耸起；他的视线落在手上那件衣服上，没有看镜头。

**要点**：动作（收衣服）+ 接触点（绳）+ 重心（右脚）+ 视线（看手）—— 四条齐了，就不可能是摆拍。

---

## 本册 L5 · 时段光 × 口味预设表（6 行，共用同一套词库）

**口味不是分册**——它们只换 L5 光 + L7 调色/质感，L1/L2/L3/L4/L6 完全共用。要加口味，往这张表加一行即可。

| 口味 | L5 光 | L7 调色/质感 | 媒介指向 |
|---|---|---|---|
| **写实街拍·电影感** | `overcast diffused light, flat soft shadows, no fill` | muted teal-grey, low contrast, subtle grain | style-presets #2 |
| **阴雨日常** | `light just after rain, wet surfaces doubling every source, rain streaking the lens` | cool cyan with warm sodium accents | style-presets #2 |
| **赛博霓虹** | `self-luminous signage dominating the exposure, magenta and cyan spill on wet ground` | high saturation, crushed blacks, blooming highlights | style-presets #1 / #2 |
| **商业繁华夜景** | `blue hour, shop windows glowing warm against a cooling sky, car light trails` | cool blue base with warm window pools | style-presets #1 |
| **清晨通勤** | `low raking sun, long shadows across the pavement, thin cold mist` | desaturated with warm highlights, crisp micro-contrast | style-presets #2 |
| **老城旧巷** | `hard afternoon sun broken by overhead cables into dappled patches` | warm grey and ochre, matte, slightly faded | style-presets #2 / #9 |

---

## 本册 L6 · 都市镜头组合

- **`35mm`** — 街拍标准，人景关系最自然，"像走在街上随手拍的"
- **`28mm`** — 巷弄纵深、前景遮挡
- **`16–24mm` 低角度** — 高楼压迫感（**必须配 `corrected verticals`**，否则楼是歪的）
- **`85–135mm`** — 压缩人群与招牌，制造都市特有的**层叠感**
- **`reflection shot`** — 透过积水/玻璃拍，天然多一层信息
- 构图：`leading lines of the street receding to a vanishing point` · `framed through a doorway` · `foreground occlusion` · `layered depth: foreground object → mid street → far towers`

---

## 前景遮挡怎么写（2026-09-13 新增 · 有实测对照）

> **为什么单立一节**：本册反模式写着"街道要有遮挡"，但**从没写过遮挡怎么落笔**（skill 缺口："有主张、无写法"）→ 照 `foreground occlusion` 抄了个句型就交出去，两次出**又大又实**的挡光物。
> **一句话**：**遮挡要"小、虚、无色"，不能"大、实、有色"。**

**四件事，缺一不可**

| # | 写什么 | ✅ 好例 | ❌ 坏例 |
|---|---|---|---|
| ① | **是什么部件**（**越小越好**） | "车把与铃铛**那一小段**" · "一只手肘的一角" | "一辆共享单车" · "别人的**肩膀与手臂**" |
| ② | **占画面多少** | "只占右下角**一小块**" | （不写） |
| ③ | **虚化到什么程度** | "完全失焦成**一片深灰的色块**" | （不写） |
| ④ | **颜色与「色调」段相容** | 色调写"低饱和冷灰" → 遮挡物写"深灰的色块" | 色调写"没有高饱和色块"，遮挡物却是**黄黑隔离柱 + 明黄单车** |

**★ 三条实测规律**

1. **写整个物件，就得到整个物件**：都市白领首验写"透过**前景单车的横梁**取景" → 出了**整辆**黄色共享单车的车头与车轮，**又大又不糊**，还被画框切得难看。
2. **写"身体部位名"同样会出整个人**：电车稿写"右下角是**别人的肩膀与手臂**" → 出了**半个清晰的背影**（布褶、耳朵都在），**根本没有失焦**。
3. **"不给形状"的色块写法（【仅示意 · 未验 · 2026-09-30 由「最稳」降级】）**：要色块就写 **"一块看不出是什么东西的深蓝色块、边缘完全化开"**，再补一句 **"它跟主体之间还隔着一小段板面"**。
   ⚠️ **反例（n=1 · 2026-09-30 · Krea2 十段式真人稿）**：照此写（`画面下方只占一小块的，是一小片看不清是什么东西的浅绿色块，边缘完全化开；它跟人物之间空着一小段长椅的板面`）→ **画面底部正中出一坨悬空的绿块，跟任何表面都不接**。→ **色块写法不保证「不长大、不悬空」**；**取景类压不住**这条对它同样成立。**要干净的最近层：写「主体所在物件的自然延续」，或出图后裁切。**

⚠️ **下面这条是 n=1（「首试即成」）、未换种子复现 → 按元规则算【仅示意】、不得照抄**；要采用先按 §1.5 单变量跑一遍。

**对照 · 成功的写法长什么样**（都市白领修正版 v2）：
> "右下角**只有车把与铃铛那一小段**、**完全失焦成一片深灰**、**只占一小块**、**车身与车轮在画框外**"
> → 出图 **✅✅ 首试即成**（主体完整可见、下半身没被挡）。

---

## 本册专属反模式（写了就扣分）

- ❌ **空城**：街道干净、没人、没杂物 —— "布景感"的头号来源
- ❌ **无时段**：不写时间/天气 → 光变平、看不出早晚
- ❌ **泛化**：`a modern city street` / `繁华的都市` —— 零约束力
- ❌ **霓虹与日光打架**：写 `daylight` 又写霓虹 `glowing at full strength`
- ❌ **广角畸变未声明**：写 `16mm` 却不写 `corrected verticals`
- ❌ **全对称构图**：街道默认要"偏"、要有遮挡，正对称容易变成效果图 —— **遮挡怎么写见上文「前景遮挡怎么写」：小、虚、无色**（写"整个物件"或"身体部位名"都会出又大又实的挡光物）
- ❌ **无人味的整洁**：只有建筑没有人用过这个空间的痕迹
- ❌ **摆拍姿态**：对称平展双臂 / 掌心朝上 / 正面对镜站定 —— 写实媒介下必出 T-pose 感（**首验实测**）
- ❌ **忘了排他句**：不写"空无一人 / 没有玻璃幕墙"，模型就会自行塞人或塞现代 CBD（**cfg=1.0 下负面框无效**，必须写正向句）
- ❌ **反射不写内容**：写了水面 / 玻璃却不写它映什么 → 反射面变成一块亮斑（**首验实例**：水洼只映了天光，人没有倒影）
- ❌ **"反射"与"留白"同时写**：既写"反光处全部留白"又想要倒影 → 模型只能二选一（漫画册 B 版实测它选了倒影）。**两者择一明写**：要倒影写 `水面上映出人物与伞的倒影`；要干净反光写 `反光面处理成整片纯白，不画倒影`
- ❌ **悬挂物不写受力**：晾衣只写"在风里鼓动" → 衣服贴栏杆浮着；要写"夹子夹住、绷成弧形"

---

## 组装模板（都市版）

```
<L1 空间/街道 + 围合方式 + 纵深>.
<L4 生活痕迹 ≥2 个>.
<L2 锚定：一个具体物件 + 一个年代符号 + 一句具体文字>.
<L3 地面/墙面材质 + 使用痕迹 + 天气残留>.
<L5 时段光 + 光源方向 + 反射/散射>.
<L6 焦距 + 机位 + 构图 + 层叠关系>.
<L7 媒介 + 调色 + 质感>.
```

---

## 完整范例

### 范例 1 · 阴雨日常 · 巷口面馆（35mm 街拍）

> A narrow side street walled in by six-storey walk-ups, air-conditioner units and laundry strung across the gap, wet asphalt holding a doubled strip of sky. A delivery rider's insulated box rests against a rust-streaked roller shutter, a shopkeeper hoses down the pavement, plastic bags snagged on a fence. A hand-painted sign in Chinese characters reads "面馆" above a steam-fogged window. Light just after rain, every surface still dripping, puddles doubling the warm glow from inside the shop. Shot on 35mm at f/2 from eye level under an awning, layered depth from foreground puddle to mid street to far towers softened by haze. Photorealistic street photograph, muted teal-grey, low contrast, subtle film grain.

**中文要点**：锚定靠"面馆招牌 + 电动车外卖箱 + 卷帘门"，生活痕迹 3 个；层次靠雨后反光而非空气透视。

### 范例 2 · 赛博霓虹 · 十字路口（24mm 低角度）

> A rain-slicked crossroads at night in a canyon of towers, the sky reduced to a strip, shop signs stacked vertically along every pole. Self-luminous signage dominates the exposure — magenta and cyan spilling across wet asphalt, signage in Chinese and English characters, one steamy noodle stall still open at the kerb with stools stacked beside it. Tangled overhead cables cross the frame. A single pedestrian's silhouette at the crossing, umbrella closed. Shot on 24mm from a low angle with corrected verticals, leading lines of the street receding to a vanishing point, reflections doubling every light source. Photorealistic night photograph, high saturation, crushed blacks, blooming highlights, anamorphic flare.

**中文要点**：口味差异**全在 L5/L7**——L1/L2/L3/L4/L6 与范例 1 同一套词库，只换了光与调色。

---

## 本册的锚定自查（出稿前必过）

- [ ] 至少一个**可被指认的具体物件**（形状/颜色/材料说得出来）
- [ ] 至少一个**年代符号**（哪一年看得出来）
- [ ] **生活痕迹 ≥2 个**（有人用过这个空间）
- [ ] **时段/天气写明**（不写就不算完成）
- [ ] 画面里有文字时，文字**放进双引号**并说明语言
- [ ] 写了 `16–24mm` 就配 `corrected verticals`
- [ ] 没有出现"泛化都市词"（modern / 繁华 / 未来感）
- [ ] **要人时**：动作有因果、手有落点、人物不居中——**没有摆拍信号**（双臂对称平展 / 掌心朝上 / 正面对镜站定）
- [ ] **姿态与媒介匹配**（写实街拍**不配**仪式感对称姿势；要仪式感就改媒介）
- [ ] 写了**反射面**（水面 / 玻璃）就写了**它映什么**；写了**悬挂物**就写了**它怎么受力**
- [ ] 不想要的东西写了**排他句**（cfg=1.0 负面框无效）

---

## 形态 B 范例（十段式长文 · 可直接照抄结构）

> 段↔层映射见 `SKILL.md` §1.4。**换口味只改「色调 / 风格 / 光影氛围」三段，换视角只改「构图 / 视觉引导」两段**，其余段一字不动。

**青砖巷晨光（暖灰赭石 · 老城早市）**

**主体：** 画面核心是一条尚未完全醒来的老城窄巷，两侧四层居民楼的漆皮剥落，外挂空调机一排排咬在立面上，巷子尽头是一小段被晨雾吃掉的天光。
**要点：** 靠"手写招牌、蒸汽白柱、冲刷门前的地面"三件具体物立住"这里住着人、这是清晨"两个判断；时段感由低角度侧光与长影交代。
**前景：** 画面底部是一级被踩得发亮的水磨石台阶，阶前地面被水冲得反光，一摞塑料筐斜靠在墙根，筐边搭着一块湿抹布，缝里卡着几个烟头。
**中景：** 巷子中段是一家挤在门洞里的早点摊，掀开蒸笼的热气在光里立成一道白柱，摊主正拎着水桶冲刷地面，门楣上方一块手写招牌写着"生煎"两个中文字，旁边靠墙斜着一辆自行车，头顶横拉的电线上晾着两件衣服。
**背景：** 巷子尽头是几栋更旧的坡顶屋，屋脊轮廓在薄雾里逐层淡去，远处电线杆与交错的电缆把天光切成细条，一只麻雀停在电线上。
**构图：** 竖版偏左重心，主体（早点摊）位于中右三分之一，前景台阶压住画面底部约四分之一形成基座，巷子纵深沿透视线向画面右上收敛。
**视觉引导：** 由前景台阶的走向引入，沿地面水光与蒸汽柱向上，最终落在招牌"生煎"与摊主的动作上；背景电缆的斜线提供反向拉扯，画面里没有一处让视线停住的地方。
**色调：** 暖灰与赭石为主，湿地面反射冷青天光形成冷暖对冲，蒸汽与薄雾处偏乳白，整体低饱和、层次靠明度拉开。
**风格：** 写实街拍摄影，保留自然的镜头畸变与手持感，纪实取向，边缘是自然的软、保留胶片微粒。
**光影氛围：** 单一主光——清晨低角度日光自街道右侧斜射入巷，在石板与水面上拖出长影，蒸汽被光打透成半透明的白柱，背光处压深但不死黑，空气中有可见的细微浮尘。

> **同场景换口味示例**：只把「色调」改成"低饱和青灰、冷调"、「风格」改成"电影感写实摄影、低对比"、「光影氛围」改成"阴天漫射、影子平而软、无补光"，其余七段原文不动 —— 即成"阴雨/阴天"版本。
