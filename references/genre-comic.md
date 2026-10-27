# 漫画分册（漫画 Comic / Manga）

> 本册 = **漫画题材专属内容**。通用骨架见 `SKILL.md`，通用词库见 `layer-vocabulary.md`，风格预设见 `style-presets.md`。
> 本册的 L2 锚定法 = **绘画工序痕迹 + 线条语言一贯性**。
> 边界：本册**只做"画出来的"漫画媒介**，覆盖 **日式黑白**、**日式全彩（赛璐璐）** 与 **美式英雄** 三个流派。不做写实人像（真人 / 人像册待立）、不做文字排版海报、不做纯 3D 卡通渲染。
> 形制覆盖：**单幅漫画插图** + **多格漫画页**（含条漫降级形态）。

---

## 本册的分册判据边界（为什么两个流派装在一本）

`SKILL.md` §0 的判据是「**L1 主体 / L2 锚定 / L3 材质 / L4 占据** 需要重构 → 新建分册」。**日式黑白**与**美式英雄**本可拆两册，但拆册会重复约 60%，故判为**一本册 + 两个流派小节**：

| 层 | 日式黑白 vs 美式英雄 |
|---|---|
| **L2 锚定法** | **完全相同**（都是"工序痕迹 + 线条一贯性"） |
| **L1 图幅形制** | **完全相同**（单幅 / 多格页 / 跨页 / 条漫） |
| **L4 叙事元件** | **完全相同**（气泡 / 框线 / gutter / 阅读顺序），仅拟声词语言不同 |
| **L6 镜头** | **完全相同** |
| **L3 材质** | **仅此一层内部两套词表**（墨线工具与重量、网点体系） |
| **L7 媒介词** | 两句话不同 |

> ⚠️ 这是判据的**边界应用**，不是判据失效。**下面三件事要分开看**：
> - **日式全彩（赛璐璐）** → 只动 L3 上色词表 + L5/L7，L1 形制 / L2 锚定 / L4 叙事元件 / L6 镜头**完全相同** → **判为第三流派小节（本册内），不拆册**（见 `### C · 日式全彩`）。
> - **条漫（竖向滚动）** → 会动 **L1 形制 + L4 阅读顺序** → 这才是**真边界**，届时须重估、可能拆册。
> - **美式独立分支**（underground comix / ligne claire / 法比漫画）→ 逐项按判据复核。

---

## 本册的 L2 锚定法：绘画工序痕迹 + 线条语言一贯性

**漫画题材"假"在哪里**：不是不够好看，而是**一眼就看出"这不是画出来的，是算出来的"**——线条从头到尾一个粗细、没有起笔收笔；上色是塑料渐变而不是色块；网点糊成噪点；一只眼睛是日式的、另一只手是写实的；分格的先后读不出来。

所以本册**不锚"像不像漫画"，锚"能不能看出这是人画的"**。**主力三件事，至少写中两件**；另有一件**可选氛围词**（低命中，别当主力）：

- **主力**：① 线条语言一贯（工具 + 粗细层级）② 网点与排线的规则性 ③ 媒介声明（**必填**）
- **可选氛围词**：工序痕迹 —— **两连败实测**，见下

### 1. 线条语言一贯（最有效）

**把工具写出来——工具决定线的性格**：

- 日式：`inked with a G-pen, the line swelling and tapering at every stroke` · `maru-pen outlines of dead-even thickness` · `a dry brush stroke breaking into scratchy fibres`
- 美式：`brush-inked contours with brutal weight shifts, thick outside edges and hairline interiors` · `a nib pen hatching the shadows in one strict direction`
- 两者共用的一句：`a deliberate weight hierarchy — heaviest on the outer silhouette, thinnest on interior detail`

> ❌ 反面：`clean vector lines` / `crisp line art` —— 这两个词必得"AI 描边感"，线的重量全一样。

### 2. 工序痕迹（⚠️ 可选氛围词 · 低命中 · 别当主力）

> **实测结论（2026-09-13 · 两连败）**：**页面外框类**痕迹（原稿纸边、四角裁切标记）模型会丢；**换成画面内的痕迹**（实黑漏白 / 套印偏移 / 铅笔底稿）之后，**第二版仍然看不出来**。
> → **判定：「原稿感 / 印刷瑕疵」这类锚定对 Krea 2 疑似整体无效**——它交付的永远是"干净的数字化漫画"。
> ✅ **v2.19.23 第三次复现，且跨出漫画题材**：换到"**九十年代复古赛璐璐动画**"这一风格（同稿同种子 · ①段 1728×3072 · 种子 268 · **3 档**），稿里写死的 **胶片颗粒 / 红绿两色的轻微错位 / 四角比中心暗一档** → **3/3 三样全部没出**；而且"细密的胶片颗粒"被三档统一理解成**黑板表面的斑驳小点**（局部污迹），**不是覆盖全画面的均匀颗粒**。
> → **同族结论从"漫画的印制痕迹"扩到"动画的胶片痕迹"**：**凡"介质本身有瑕疵"这类锚定，Krea 2 一律交付干净版**—— **别再为它花稿子里的位置**。**[观测 · n=5 累计（2+3）]**
> → **本条降级为可选氛围词，不参与锚定主力**：想写可以写，但**不要指望它生效**，更不要为它牺牲主力三项。

**✅ 高效：画面内部看得见的痕迹（首选，主力）**

- **实黑块边缘的漏白 / 鬼影边**：`the solid black shapes carry a thin unprinted white edge where the screen fell short of the line`
- **网点套印偏移**：`halftone registration slightly off, leaving a ghost edge on the flat tone`
- **修正白**：`small correction marks in opaque white paint over the ink`
- **露出的铅笔底稿**：`faint pencil underdrawing still visible beneath the ink on the wall and the ground`
- **手绘的不齐**：`even the ruled lines wobble very slightly, as if drawn by hand`
- **助手残留线**：`a stray assistant's line left uncorrected at the panel edge`

**⚠️ 低效：页面外框类（模型常丢，别当主力）**

`the page sits on visible manuscript paper with the ruled margin still showing` · `untrimmed bleed edge and crop marks along the border` · `a page number and a small author credit in the outer margin`

> 要用就**明写"画面最外缘可见"**并放在构图段，但仍属低命中项——**锚定的主力必须是上面那组画面内痕迹**。

### 3. 网点与排线的规则性（防"脏"）

网点必须是**规则点阵**，不是噪点：

`screentone applied as an even, machine-ruled dot grid at one fixed angle` · `a fine 60-line dot screen, dots uniform in size and spacing` · `Ben-Day dots in flat cyan, magenta and yellow, evenly spaced and never overlapping` · `cross-hatching laid down in one consistent direction, never doubled or crossed`

> ⚠️ 全册最容易翻车的一条：一旦写出 `noise` / `grain` / `texture`，网点会被理解成照片噪点，**整页立刻变脏**。要"质感"请写**点阵的规则性**，不要写"噪"。

**落点也要指名（首验结论）**：**大块背景（夜空、暗部）写 `solid black` 比写"70% 网点"更稳**；**网点最可靠的落点是反光面、中景与渐变过渡区**。首验那张里，**水面倒影的网点出得很漂亮**，而"整片夜空压 70% 网点"最后变成了整块实黑。

- ✅ 想网点：**指名区域** —— `整条路面反光处的网点由密到疏` · `人物身后的中景墙面铺一层 40% 点阵`
- ✅ 想暗部：直接写 `solid black` / `实黑填满`，别绕道"高密度网点"

### 4. 媒介声明（必填，不是可选）

- 日式：`black-and-white manga page, screen-tone printing, ink on paper`
- 日式全彩：`full-colour Japanese manga illustration, cel-shaded flat colour over ink lines`
- 美式：`American comic book page, four-colour flat printing on newsprint, brush ink over pencil`

> 不写媒介 → 模型默认给"3D 渲染的伪二次元"。本册与其它册不同：**媒介词是硬性必填项**。
>
> ⚠️ **但媒介词压不住模型（2026-09-13 实测）**：**同一条全彩漫画词**，挂 `Krea2-Moody-Mix` → **出漫画**；挂 `Krea2-SATDirtyrealism`（摄影向）→ **出写实照片**，而且加写"印刷在纸上 / 2D 插画 / 不是照片"**也压不住**。
> → **漫画题材禁用摄影向模型。** 本机实测可用：`Krea2-Moody-Mix-premium_int8_convrot`（黑白 3 次 + 全彩 1 次，全中）、`Krea2-seeKrea2_genesisInt4Convrot_int4_convrot`（赛璐璐插画 1 次，全彩本册首选）。模型分档表见 `SKILL.md` §3.1。
>
> ⚠️ **换模型 ≠ 换好坏，是换"偏题方式"（2026-09-13 同词对照）**：**同一条纯中文赛璐璐插画词**，`genesis` **守着册子的规矩画**；`Moody-Mix` **也出画、也好看，但会自作主张**——把暖色小灯换成**提灯并加光晕**（词里明写"不画光晕"）、把"一支苹果糖"画成**三颗糖葫芦**、主体由"偏左三分"改成居中。→ **要按册子施工就固定 `genesis`**；换模后出现的差异，**先怀疑模型，别急着改词**（A/B 铁律）。

**通用锚定原则**（优先具体物 > 数字 > 形容词）见 `layer-vocabulary.md` 的 L2 一节。

---

## 本册 L1 · 图幅形制与主体形态语法

### 三种形制（**选一个写死**，不要含糊）

| 形制 | 提示词写法 |
|---|---|
| **单幅插图** | `a single finished manga illustration, no panels` |
| **多格页** | 日式：`a four-panel manga page laid out in a 2×2 grid, read right to left and top to bottom`<br>**美式：把方向换成 `read left to right and top to bottom`**（两流派阅读方向相反，别照抄日式那句） |
| **条漫降级形态** | `a vertical three-panel webtoon strip, read top to bottom` |

> **条漫是"多格页"的回滚方案**：当模型画不出 2×2 的阅读顺序时，先降到竖向 3–4 格。

### 分格词汇（多格页必用）

`an establishing panel spanning the top third` · `an inset close-up panel breaking the frame at the lower right` · `a full-bleed splash panel with no border` · `a narrow vertical panel isolating the eyes` · `gutters of even white width separating every panel` · `a panel border broken open where the figure bursts through it` · `a borderless panel dissolving into the next`

### 主体与形态语法（人/物在漫画里怎么画）

`a figure struck in a low dynamic pose with the weight on the back foot` · `a face in three-quarter view with the far eye reduced to a single dot` · `chibi-proportioned side characters crowding the margin` · `speed lines converging on the point of impact` · `a crowd drawn as repeating silhouette units, no two faces detailed`

### 重复单元（至少写 2 个，防糊）

`rows of identical background windows` · `a strict fan of speed lines` · `evenly spaced tone dots` · `one sound effect stamped identically across two panels` · `repeating rain strokes at a single angle`

### 小物件与道具的位置写法（首验教训）

**首验踩到的坑**：写"硬币和被踩扁的烟盒**浮在水面**"，出来是两个烟盒**躺在旱地上**。

→ **"漂 / 浮 / 浸"这类状态，必须写到受力与接触点**：

| 想要的状态 | ❌ 别这么写 | ✅ 要这么写 |
|---|---|---|
| 漂在水面 | `浮在水面` | `半个浸在水里，随水纹微微起伏，湿透的纸盒边缘发软下垂` |
| 挂在绳上 | `挂在绳上` | `用木夹夹在绳上，布面被自重拉成向下的弧形` |
| 靠在墙边 | `靠在墙边` | `斜靠在墙上，底端抵住地面，上端与墙面留出一道三角空隙` |
| 被风吹起 | `被风吹起` | `一角被风掀起，翻折过去贴住另一面` |

> **通则**：凡是有状态描述的物件，**就写它与支撑物的接触点与受力方向**——与"人物接触点"是同一条原理（见人物主体四条）。

---

## 本册 L3 · 两个流派（本册唯一"两套词表"的一层）

### A · 日式黑白（网点 + 压线）

**线**：`G-pen main lines with pronounced taper` · `maru-pen outlines of constant weight` · `ink pooling slightly where strokes cross` · `dry-brush textures on cloth and stone`

**网点**：`screentone gradations built from dot screens at 10% to 90% density` · `solid beta-flash blacks filling the shadow shapes` · `a gradient screen fading out from one corner` · `a delicate 5% screen laid over the whole background`

**留白**：`uninked paper left as pure white highlights on wet skin and metal` · `negative space carrying the shape of the light`

> ⚠️ **"留白" = 不落墨（纸白），不是"画一块白色"。** 写 `用一块纯白留白表现眩光` 会得到**一个白色矩形块**（2026-09-13 B 版实测：街上那几个白方块就是这么来的）。
> - 要留白 → **`不落墨、保持纸白，只把周围压暗来反衬`**
> - 要白色形状 → 明确写 `画一个纯白的圆形光晕，边缘不带轮廓线`

**影**：`shadow shapes blocked in as solid black, hard-edged, never airbrushed`

**拟声词**：日语假名，竖排 —— `"ドドド"` / `"バキッ"` / `"シーン"`

### B · 美式英雄（粗墨线 + 半调）

**线**：`brush-inked contour with extreme weight variation` · `heavy black spotting for cast shadow` · `a nib-pen hatch screen carrying the mid-tones` · `a bold contour that closes the silhouette completely`

**网点**：`Ben-Day halftone in flat cyan, magenta and yellow, dot size constant, spacing even`

**色**：`four-colour flat printing, no gradients, hard-edged where one colour meets the next` · `a single spot colour dropped in for the background`

**影**：`solid black shadow masses with one hard-edged highlight shape per form`

**拟声词**：英语，斜排，空心描边字 —— `"KRAKOOM!"` / `"THWIP"` / `"BAM"`

> **三派不许混写。** 同一张提示词里出现 `G-pen` 又出现 `brush-inked`，或 `screentone` / `Ben-Day` / `cel-shaded` 三者混写，结果必漂移。**选一派，写到底。**

### C · 日式全彩（赛璐璐上色）

> **判据**：与「A · 日式黑白」**只差 L3 上色词表 + L5/L7**；L1 形制 / L2 锚定 / L4 叙事元件 / L6 镜头完全相同 → **同一册内的第三流派小节，不拆册**（与 B 小节同理）。

**线**：与 A **完全相同** —— `G-pen main lines with pronounced taper` · `ink pooling slightly where strokes cross`。**赛璐璐的墨线仍然在**，不是无线上色；粗细层级照旧要明示。

**上色（本派的核心，关键词只有两个：硬边 + 单层平涂）**：

`flat cel-shaded colour, every colour held inside the ink lines and never bleeding past them` · `two-tone shading per material — one base tone and one hard-edged shadow tone, nothing in between` · `flat white highlight shapes on hair and eyes, hard-edged, never a soft bloom` · `a warm rim light on hair and shoulders laid in as a separate flat shape`

**影**：`shadow shapes drawn as a single flat darker tone with a hard edge, never airbrushed` · `one shadow tone per material, reused everywhere that material appears`

**色**：`a restrained palette of warm grey, dusty blue and one accent colour` · `background held slightly desaturated so the figure reads first` · `sky and walls as flat colour blocks, no gradient mesh`

**媒介声明（必填）**：`full-colour Japanese manga illustration, cel-shaded flat colour over ink lines`

> ⚠️ **赛璐璐的头号翻车信号**：`soft airbrush gradient` / `smooth 3D shading` / `painterly blending` / `watercolour wash` —— 任何一个都会把赛璐璐**拉成厚涂或 3D 渲染**。想回到赛璐璐，只加两个词：**硬边（hard-edged）+ 单层（one flat tone）**。

**中文对照（出词用。自 2026-09-13 起输出一律纯中文，左边英文仅供参考）**：

| 英文原词（册内参考） | **中文写法（写进提示词的用这个）** |
|---|---|
| `full-colour Japanese manga illustration, cel-shaded flat colour over ink lines` | 日式全彩插画，墨线之上单层平涂（赛璐璐）上色 |
| `G-pen main lines with pronounced taper` | 漫画蘸水笔的主线，起笔收笔有明显粗细变化 |
| `two-tone shading per material — one base tone and one hard-edged shadow tone, nothing in between` | 每种材质只用两层平涂：一层底色 + 一层硬边暗部，中间没有过渡 |
| `flat white highlight shapes…, hard-edged, never a soft bloom` | 高光是边界清楚的实色块，不是发光晕 |
| `every colour held inside the ink lines and never bleeding past them` | 所有颜色严格限制在墨线之内，不外溢也不混色 |
| `shadow shapes… single flat darker tone with a hard edge, never airbrushed` | 暗部是一整块硬边平色，没有任何喷枪式过渡 |
| `a restrained palette of…` / `no gradient mesh` | 克制的配色，只用几个平色；天空与墙面都是平涂色块，画面里没有渐变 |
| `flat dark background, light sources laid in as flat colour shapes rather than glows`（夜景口味） | 背景整体压暗成平涂色块，光源画成平涂的色块而不是光晕 |

> ⚠️ **术语不要临场另译**：上表是**册内定死的中文对照**，出词时照抄右列——避免同一条规则每次译法不同。**翻得不对的地方，跑完图就回来改这张表。**

### D · 少女漫画（**v2.19.23 新增小节**）

> **为什么是"小节"而不是新册**：与 C 流派（日式全彩）**共用 L2 的线条 / 网点锚定与媒介声明**，差异落在 **L1 形态语法**（巨大眼睛 · 星形高光 · 细长脖颈）+ **L4 装饰元件**（星形闪光 · 花瓣）+ **L7 配色**。拆册会重复 L2 与媒介声明约一半 → **判为册内第四小节**。**重估条件**：若将来少女漫需要**独立的 L1 骨架**（例如整幅以装饰符号为主体、人只占一角），再考虑拆册。

**形态语言（写"可量"的形，别写"很可爱"）**：

- 眼睛：`眼睛的高度约等于脸宽的三分之一` · `瞳孔里散布着大小不等的星形高光点，其中最大的一颗落在瞳孔的左上角`
- 睫毛：`上睫毛画成一根一根分开的短粗线` · `下睫毛用更细的短线表示`
- 脖子：`脖子是细长的，宽度大约是头宽的三分之一`
- 腮红：`两颊各有一小片斜排线表示的腮红`
- 头发：`头发上有一条横向的实色高光带、边缘是硬的`

**装饰元件（落点要指名）**：`大小不一的四角星形闪光符号` · `两片飘落的花瓣、一上一下，每片是平涂的色块加一条细中线` · `斜向排线从画面左上角向右下角拉过去`

**配色与线**：`淡粉、奶油白、浅水蓝三个主色加一点深褐做线` · `主线是极细的均匀墨线，只有眼睛周围与发梢收笔的地方稍微加重`

> ⚠️ **必须声明刻意的变形**：少女漫的细长比例正落在本册反模式「**比例无意义拉长**」上——**册内原文要求"刻意做变形风格就必须声明"**。稿里要明写 `这是刻意做出的少女漫画变形比例`，否则会被当成走形。

**实测记录（2026-10-01 · 单批 · 3 档 · 同稿同种子 · ①段 1728×3072 · 种子 268）**

- ✅ **星形闪光与花瓣 3/3 全出**（"可指认的形 > 形容词"又一次正面复现）
- ✅ 大眼 · 星形高光（最大一颗在左上角）· 分开的短粗睫毛 · 斜排线腮红 —— 1:1 放大**逐条兑现**
- ❌ **「脖子细到三分之一」压不住**（与册内"锁比例要给一组互相制约的锚、只锁一条＝其余放羊"一致）
- ⚠️ **本小节的稿漏写了服装**（起草时漏句、交付前未核）→ 三档**各自自加**了一件 T 恤（左粉 / 中蓝粉拼色 / 右浅蓝），**不是款式漂移**。
  → ✅ **已验成（v2.19.24 · 同日 · 同种子 268 · 单变量 A/B · 3 档）**：**只把服装那一段换成写死构造件的版本**（其余逐字不动，已用逐字 diff 证明只多这一句）→ **三档全部出「白衬衫 + 深褐领结」**；1:1 复核可见 **尖角翻领 · 前襟一列圆扣 · 方结 + 两片垂角 · 袖口翻边**，而未写服装的对照稿三档都只出**素 T 恤**。→ **构造件锁款式成立**。⚠️ **相对量不兑现**：稿写「两片垂角一长一短」→ 三档都出成差不多长。
- ⚠️ **网点 1/3**（只有 `raySemiReal` 出了规则网点；`genesis_v2` 出成纯平涂、`kALUAN` 几乎无网点）
- ⚠️ 三档取向：`raySemiReal` **最像原稿** · `genesis_v2` 最"少女漫"但背景纯平涂 · `kALUAN` **最像现代日系插画**

> ⚠️ **本小节的句子均为 n=1/档、尚未复现 → 一律【不得照抄】**（等同"仅示意"）；要用先按 §1.5 单变量跑一遍，同型攒到 n≥3 且换种子仍成立才可升格。

---

## 本册 L4 · 叙事元件（漫画的"占据物"）

> 都市册的 L4 是"**有人在用这个空间**"；漫画册的 L4 是"**这一页在讲故事**"。至少写 2 个。

### 气泡四型（**写清形状，别只写 `speech bubble`**）

`a round speech balloon with a clean tail pointing at the speaker's mouth` · `a scalloped burst balloon for a shout` · `a cloud-shaped thought balloon trailing small round bubbles` · `a plain rectangular caption box tucked into the panel corner` · `a rectangular narration box overlapping two panels`

### 框与页面规则

`even gutters of pure white between panels` · `panel borders ruled straight with squared corners` · `one border deliberately left open where the action continues` · `a page number and a small author credit in the outer margin`

### 拟声词（怎么写才点得着）

`the onomatopoeia "ドン" hand-lettered in bold vertical katakana filling the empty corner` · `"KRAKOOM" in outlined block letters arcing across the sky` · 音效字与画面动势**同方向倾斜**

**五条写法（缺一条就会落空或被忽略）**：

1. **先说落在哪，而且要与画面元素协调** —— 落点必须**真的空着**，否则整句会被丢掉。
   - ❌ `填满画面右上角那片空白雨幕` —— **实测翻车**：那条词的右上角其实是便利店，空雨幕在左上 → 模型找不到落点，**拟声词整句没出**
   - ✅ 用**相对描述**：`填满雨幕里最空的那片区域` · `压在左侧街道上方的雨幕空白处`
   - ✅ 或**先确认方位**：写落点前回看一遍「构图」段与「中景」段，确认那个方位没被别的东西占用
   - ⚠️ **落点句会被"换载体"**（v2.19.9 · n=2）：稿写"右上方那片**网点天空**"→ 两张都把字压在**墙面**上（字确实在右上，但"天空"这个载体没给）→ **落点写相对位置（"右上方那片最空的地方"）比写具体载体稳**。
2. **写清字体与排布** —— 日式：`竖排手写假名、实黑粗体`；美式：`空心描边粗体英文、沿弧线排布`。**排布方向与画面动势同向**（雨就斜下、冲击就向内收）。
   - **空心字要把"空"拆成两半写**（**v2.19.10 升格 · 【可照抄 · n=4 · 跨 2 档（`ray` / `raySemiReal`）· 含换种子复现（`…4684` / `…4685`）· 判读段位 ①段 2048×1152】**）：写成——`字母的笔画内部保持空心、透出后面的网点` ＋ `只有一圈均匀的黑色粗描边勾出字形`；**两档 × 两种子 4/4 都兑出"真空心"**（背景的颗粒 / 半调网点 / 砖缝 / 速度线**直接穿进笔画内部**）。⚠️ **档位限定（同批 2 档反例）**：**强制照片档 `SATDirtyrealism` → 字出，但内部被做成"平色实填"（背景不穿过）＝ 假空心**；**强制插画档 `genesis` → 字被塞进纯白对话气泡、载体变白 → 空心与白填分不出来、判读失效**。→ **这条只在"跟随媒介"档上成立。**
   - **判读前提：字要压在"有底纹的地方"**（网点 / 砖墙 / 排线）—— 白底上"真空心"与"白填实"**长得一样、分不出来**。**实测两票**：`genesis` 那张把字塞进**纯白气泡** → 判不了；`SATDirtyrealism` 那张字底是**平色块** → 判成"填实"。
3. **写清字号层级** —— 给相对量：`字号约占画面高度的六分之一`。要冲击就大，要安静就小（`小而克制，不抢画面`）。
4. **不要塞进气泡** —— 气泡是**台词**，拟声词是**直接手写在画面上**的，两者别混。
   - **实测 1 票**（v2.19.10）：`genesis` 档把拟声词**整个塞进了一个大白气泡**里（同稿其它档都写在墙上）→ **这条在"强制插画"档上会被违反**。
5. **多格页要指名格** —— `拟声词压在第二格与第三格之间`，否则它会随机落在某一格。

**流派语言必须一致**：日式用假名（`"ザアアア"` / `"バキッ"`），美式用英文（`"KRAKOOM!"` / `"THWIP"`）。**日式画面里出现 `"BAM!"` 就是扣分项。**

**风险与回退**：影像内文字是本册唯一的高风险项（见下），若出字崩坏 → **退回"只写字的形状、位置与颜色，不写具体字义"**（如 `一处竖排的粗黑手写字符压在空白处，字形刚硬`），把具体内容留给后期加字。

> ⚠️ **v2.19.23 反证（重要 · 这条回退方案本身有问题）**：把拟声词**只写字形、不写字义**（`画面右上角有一处斜排的空心描边粗体字，字母的笔画内部保持空心、透出后面的网点`）挂 `raySemiReal` 与 `genesis_v2` 两档（同稿同种子 · ①段 1728×3072 · 种子 268）→ **两支都是一个字都没出，字整段丢失**（n=2）；1:1 放大后确认画面上没有任何文字，原先误认成"字"的其实是**蛛丝的缠绕结**。对照册内那条 **【可照抄 · n=4】** 的空心字，当年写的是**具体字义**（`"BAM"`）→ **4/4 全中**。
> → **推测：「字义」本身就是触发条件；只给字形＝模型不把它当成文字去画**。
> **处置**：① 要出字 → **必须写出字义**（那就要在稿里放字母或假名，**与"纯中文"语言政策冲突，需用户点头**）；② 不出字也行 → 但**别指望"只写形状"能落字**，那句只能当**氛围词**用。**[观测 · n=2 · 跨 2 档]**

> ⚠️ **影像内文字渲染：逐项盘过（2026-09-19 更新）** —— **中文短词 ✅**（都市册灯箱"招待所" / 真人册招牌"早点"）· **日文假名 ✅**（`"ミーンミーン"` 全彩单幅 / `"シーン"` 教学场景）· **拟声词 ✅**（连续 4 次）· **空心英文 ✅**（**v2.19.9** · 【观测 · n=2 · 跨 2 档 · 同种子 `…4684` · 判读段位 ①段 2048×1152】：美式单幅 `"BAM"` 两张，笔画内部**真空心**）。**仍未验的只剩整句中文台词**（多字长句）。→ 属高风险项，先小样试一条；若出字崩坏，退回**只写气泡形状与排版、不写具体台词**（台词留给后期加字）。

### 阅读顺序（**多格页必写**）

日式：`read right to left and top to bottom, each panel advancing exactly one beat` · **美式：`read left to right and top to bottom`** · `the last panel holds the punchline, largest and quietest`

---

## 本册 L5 · 口味表（漫画的光是"用线画的"）

> 与其它册不同：漫画的 L5 **不是摄影布光**，而是"**光在线稿里怎么表达**"。六行共用同一套 L1/L2/L3/L4/L6。

| 口味 | L5 光（在线稿里怎么表达） | L7 调色 / 质感 | 流派 |
|---|---|---|---|
| **日式·日常** | `flat interior light, shading reduced to one single tone screen, no cast shadows at all` | 纯黑白 + 细网点 | 日式 |
| **日式·动作爆发** | `one hard key from the side, shadows blocked as solid black shapes, speed lines filling the whole background` | 高对比、大块实黑 | 日式 |
| **日式·夜景** | `street light left as uninked white glare, everything else filled with a 70% dot screen` | 深网点 + 纯白反光 | 日式 |
| **美式·日光** | `hard noon key, cast shadow spotted in solid black, one hard-edged highlight shape across the shoulders` | 四色平涂 + Ben-Day | 美式 |
| **美式·夜战** | `figures lit by their own energy source, background dropped out to a flat spot colour with hatching` | 暗底 + 高饱和强调色 | 美式 |
| **美式·雨中** | `rain drawn as bold white slashes, the shadow spots merging into one black mass` | 冷蓝四色、低明度 | 美式 |
| **日式·全彩日常** | `flat even interior light, one flat shadow tone per form, no gradient anywhere` | 赛璐璐平涂：暖灰 + 一点强调色 | 日式全彩 |
| **日式·全彩黄昏** | `low warm key from the window, long flat shadow shapes, warm rim light on the hair` | 橙红 + 青灰对冲，背景压灰 | 日式全彩 |
| **日式·全彩夜景** | `flat dark background, light sources laid in as flat colour shapes rather than glows` | 深蓝底 + 霓虹平涂色块 | 日式全彩 |

---

## 本册 L6 · 漫画镜头与构图

**漫画特有的构图单元**（比焦距更重要）：

`a top-tier establishing panel with three smaller beats beneath it` · `a double-page spread with the horizon running unbroken across the gutter` · `a low-angle hero shot with the figure filling two-thirds of the panel height` · `an extreme close-up of one eye occupying the entire panel` · `a wide empty panel of the city, the figure reduced to a tiny silhouette in the lower left` · `a vanishing point forced to the exact centre of the panel` · `foreground hands breaking into the bottom of the frame`

**视线引导**：`the eye dragged from the white of the shout balloon down the speed lines into the impact point` · `the tail of the last balloon pointing back toward the previous panel`

**焦距**（沿用通用层，但注意语义）：漫画里写焦距是为了**背景的透视处理方式**，不是为了景深 —— `drawn with a wide-angle feel, the background buildings curving away at the edges`

---

## 本册专属反模式（写了就扣分）

- ❌ **画风混杂**：脸是日式的、手是写实的、背景像照片 —— **本册头号死因**
- ❌ **线粗细一致**：`clean vector lines` / `crisp line art` / `neat outlines`
- ❌ **上色是塑料渐变**：`soft airbrush gradient` / `smooth 3D shading` / `glossy render`
- ❌ **网点当噪点**：写 `noise` / `grain` / `texture` → 整页变脏（改用"规则点阵"表述）
- ❌ **三流派混写**：同一张里既有 `G-pen` 又有 `brush ink`，或 `screentone` / `Ben-Day` / `cel-shaded` 混着写
- ❌ **赛璐璐写成厚涂/3D**：全彩时最容易翻车的一条 —— `soft airbrush gradient` / `painterly blending` / `watercolour wash` / `smooth 3D shading`。赛璐璐只认两个词：**硬边 + 单层平涂**
- ❌ **气泡排版乱**：气泡压住脸、尾巴指向错误、气泡之间无留白
- ❌ **分格无阅读顺序**：只画几个框，彼此没有先后
- ❌ **比例无意义拉长**：腿占画面一半、头身比崩坏（除非刻意做变形风格，那就必须声明）
- ❌ **媒介词缺失**：不写"漫画 / 墨线 / 网点" → 得到 3D 伪二次元
- ❌ **拟声词语言混乱**：日式画面里出现 `"BAM!"`
- ❌ **把"留白"写成"一块纯白"**：`用一块纯白留白表现眩光` → 得到**白色矩形块**（B 版实测）。留白要写"**不落墨 / 保持纸白 / 周围压暗反衬**"
- ❌ **"留白"与"倒影"同时写**：既写"水面反光处全部留白"又想要倒影 → 模型只能二选一（B 版实测它选了倒影）。**两者择一明写**：要倒影写"水面上映出人物与伞的倒影"；要印刷感写"水面反光处理成整片纯白，不画倒影"

---

## 组装模板

### 单幅版

```
<媒介声明：日式黑白 / 日式全彩（赛璐璐）/ 美式英雄，三选一 + 单幅>.
<L1 主体 + 姿态 + 重复单元>.
<L2 锚定①：墨线工具 + 明示的粗细层级>.
<L3 明暗体系（按流派三选一）：网点与排线的规则性 / 赛璐璐的硬边单层平涂 / Ben-Day 半调>.
<L4 叙事元件（气泡形状 / 拟声词落点 / 页面留白）>.
<L5 光的表达（线稿舞台 / 平涂色块）+ L7 调色>.
<L6 画幅 + 构图 + 视线引导>.
```

> **单幅请用 11 段**：通用十段 + 第 11 段「**叙事元件**」（气泡形状 / 拟声词 / 框线 / 页面留白）—— 见 `SKILL.md` §1.4。
> ⚠️ **工序痕迹不进模板**：自 v2.3.2 起已**降级为可选氛围词**（两连败实测）。想加就单独补一句，别占主力位置。

### 多格页版（**不走十段式**，见下）

```
<媒介声明（三选一）+ 格数与版式 + 阅读顺序>.
<逐格一句：这一格画什么、什么景别、这一拍做什么>.
<gutter 宽度与框线规则>.
<L2 锚定：墨线工具 + 明示的粗细层级>.
<L3 明暗体系（按流派三选一：网点 / 赛璐璐平涂 / Ben-Day）>.
<L4：气泡四型分别落在哪一格 + 拟声词落在哪>.
<L5 + L7：全页统一的光与调色（跨格必须一致）>.
```

> ⚠️ **多格页不套十段式**：十段的"前景/中景/背景"是**同一空间的三层**，而多格页的每格是**不同空间的不同时刻**，硬套会自相矛盾。多格页请用上面的专用模板。

---

## 完整范例

> 沿用 `SKILL.md` 的语言政策（**默认中文**，见其开篇语言结论），范例用**中文**。
> ⚠️ **范例 3 与范例 4 是「实跑原文、逐字未改」的史料**（2026-09-13 出图成功）——它们**自带禁止式**（“不出现网点 / 不画砖缝 / 不画分格 / 不出现任何文字”等），`tools/check-prompt.sh` ② 会照报。**原文不删**（同 `genre-liveaction.md` 那两条实跑范例的处理：删了就没法再证明“这条词真跑过”）；**照抄它们改主体之前，先把这些否定句改成陈述式**（“画面里没有网点”）。**改否定句不会作废已实测的结论**：`cfg=1.0` 下负面词本来就无效（`SKILL.md` §3.3），删掉它不影响出图结果 —— 但脚本报错会让你白跑一轮。

### 范例 1 · 日式黑白 · 天台独白（单幅 · 竖幅）

> 黑白漫画单幅，网点印刷，墨线印在纸上。一个少年背对城市站在居民楼天台的水泥矮墙上，风把校服外套掀到身后，脚边是晾衣绳、一摞塑料凳和一台锈蚀的圆水塔；远处的车流只剩下一排由密到疏的网点渐变，从近处推向地平线，读不出车的形状。天空留成大片空白，只在右上角用一块百分之七十的网点压出暮色，几道笔直的斜线从左下贯到右上，当作风向与速度的记号。人物轮廓用 G 笔画成明显的粗细变化——外侧最重、内侧极细，衣褶只用三五根收笔出锋的短线，阴影一律处理成硬边实黑，没有一处柔和过渡。天台边缘留着铅笔底稿的浅灰痕和一处没擦净的辅助线头，四角有裁切标记，网点套印略偏，在实黑块边上留出一道淡淡的鬼影。整页只有一个圆形对话气泡，细尾从少年嘴边牵出指向画面左上，气泡里竖排写着中文台词"今天也没下雨"。

**中文要点**：锚定靠"G 笔粗细层级 + 百分之七十网点 + 铅笔底稿痕 + 裁切标记"四件工序痕迹；"车流只剩网点渐变"是刻意的——用网点渐变代替车流，避免写实元素污染线条语言。

### 范例 2 · 美式英雄 · 雨中巷战（多格页 · 2×2）

> 美式漫画内页，四格 2×2 版式，从左上读到右下，四色平涂印在新闻纸上。第一格是远景：一条被两栋砖楼夹住的雨巷，雨画成粗白的斜杠，阴影整块处理成实黑，中间没有过渡。第二格切到中景，主角从墙后扑出，轮廓用笔刷墨线勾出极端的粗细反差，肩头只有一块硬边高光。第三格是特写：一只攥紧的拳头占满整个格子，Ben-Day 半调网点在青、品红、黄三色上均匀铺开，点径与间距完全一致，每一点各自独立。第四格回到全景，人物背对镜头站在巷子尽头，背景压成一块平的冷蓝专色，只余排线。全页每格之间的 gutter 是等宽的纯白，框线笔直、四角方正；右上角一块空心描边的拟声词"KRAKOOM"斜压过两格的天空，第一格与第三格各有一个圆形对话气泡，尾部都准确指向说话者的嘴。页面外缘留着裁切标记与页码。

**中文要点**：多格页的成败在**阅读顺序**与**跨格一致性**——四格的光与调色必须同一套；`Ben-Day` 与 `brush-inked` 全程只用美式词，一个日式词都不许混进来。

### 范例 3 · 日式全彩 · 河堤夏日（单幅 · **已实测**）

> 以下为 **2026-09-13 实跑并出图成功的那条原文，逐字未改**（含作者当时写在「要点」里的元信息）。

```
夏日午后，一位少女坐在河堤的草坡上，双膝曲起，一只手撑在身后的草地上，另一只手握着一个喝了一半的汽水罐，脸朝向对岸，风把刘海吹向一侧。 要点： 媒介声明必填且必须含"印刷 / 纸上 / 2D 插画"这类物理锚词（全彩时同样要，别因为禁网点就把它们一起删掉）；主力三条写死——G-pen 的粗细层级、two-tone flat shading（硬边单层平涂）、媒介声明；全画面明暗一律平涂，不出现网点（三派不许混写）；高光是实色块，不是发光晕。 前景： 画面底部是堤坝草坡的近处，草叶画成一组组尖端上翘的细线；一顶草帽搁在坡上，帽檐的投影压成一块硬边暖灰平涂；汽水罐立在草里，罐身上的水珠画成几个实色小白点。 中景： 少女坐在坡上，身体的受光面是一整块浅米色平涂，背光面是一整块硬边暖灰平涂，两者之间没有任何过渡；外套褶皱只用两三根墨线勾出，勾线后在阴影侧压一块更深的平涂；头发受光处是一块实色暖白高光块，边缘是硬的。 背景： 对岸是一排低矮平顶房，屋顶与墙面各用一整块平涂色，不画砖缝与窗格细节；更远处是平涂的天空与河面——天空由浅黄到浅蓝只用两块平涂色相接，硬边界、不做渐变，天空中不画云；河面上几道横向的白色实色块表示水流反光。 构图： 横幅 16:9 单幅，少女位于画面右三分，左侧留出河面与对岸房屋的水平纵深；地平线压在画面下三分之一，上方三分之二交给天空，左上方那片天空是整片平涂、没有任何细节。 视觉引导： 视线由前景草叶的走向引入，沿堤坝斜线向上扫向少女的侧脸，再被她身后那片浅色天空接住；对岸房屋的横向线条提供反向拉扯。 色调： 克制的四色平涂——暖米、浅黄、青灰蓝、草绿，每个色只用一块平色，不叠色、不做渐变、不做光泽。 风格： 全彩日式漫画单幅插图，平涂赛璐璐上色，颜色平铺在墨线之内、如印刷在纸上；轮廓外侧用 G-pen 加重、内侧细节极细，粗细差异是刻意的；颜色严格限制在墨线之内、不外溢也不混色；画面内不出现网点、噪点、颗粒与任何摄影感。 光影氛围： 单一主光——午后阳光自画面右上方斜射，受光面与背光面各是一块硬边单层平涂，没有第三层过渡；头发与肩头各有一块实色暖白高光（不是发光晕、不是泛光）；长影投在草坡上，边缘是硬的。 叙事元件： 在画面左上角那片整片平涂的天空上，用手写竖排日文假名压上拟声词 "ミーンミーン"，字形为深青灰实心粗体，字号约占画面高度的十分之一；该天空区域除这几个字之外不画任何东西；字不放进任何气泡。
```

**实测记录**：模型 `Krea2-Moody-Mix-premium_int8_convrot` · 一采 `euler/simple/8步/cfg 1.0` · 二采 `4步/denoise 0.38` · `ResolutionSelector = 9:16`。
**判读八项全过**：硬边平涂 ✅ / 实色高光 ✅ / 颜色不越墨线 ✅ / **未混进网点** ✅ / 未变厚涂或 3D ✅ / 天空平涂相接 ✅ / 调色克制 ✅ / 拟声词「ミーンミーン」出字 ✅。
**反面对照（同一册内最有价值的一条）**：**同一条词**换成 `Krea2-SATDirtyrealism`（摄影向）→ 输出为**写实照片**。→ **漫画题材的成败首先取决于模型，其次才是提示词。**

---

### 范例 4 · 日式全彩 · 夏夜祭典（单幅 · **已实测 · 纯中文**）

> 以下为 **2026-09-13 实跑并出图成功的那条原文，逐字未改**——**全篇零英文**（916 字 / 802 汉字 / 英文字母 0 个）。用途：赛璐璐单幅插画的**纯中文模板**，可直接改主体与口味复用。

```
夏夜祭典的摊位前，一位穿浴衣的少女侧身站着，一只手举着一支刚买的苹果糖，头微微转向身后，风把浴衣下摆掀起一角。 要点： 媒介声明用上面那句；主力三条写死——漫画蘸水笔的主线、起笔收笔有明显粗细变化、每种材质只用两层平涂（一层底色加一层硬边暗部，中间没有过渡）、媒介声明；全画面明暗一律平涂，不出现网点（三派不许混写）；高光是边界清楚的实色块，不是发光晕；这是单幅插画，不画分格、不画气泡、画面里不出现任何文字。 前景： 画面底部是摊位木台的一角，台面摆着几个玻璃瓶与一小摞纸盘，木纹只画两三根墨线；台边挂着一串暖色小灯，灯罩画成一个个扁平的实色圆块，不画光晕。 中景： 少女站在摊位侧前方，浴衣底色是一整块浅青平涂，花纹只用深一号的平色块表示，不做渐变；头发大部分压成一整块深褐平涂，受光处是一块边界清楚的实色暖白高光；举起的手与苹果糖之间用墨线勾出接触关系。 背景： 两侧是成排摊位，招牌与布帘各用一整块平涂色，不做文字细节；再远处是深蓝平涂的夜空，几簇烟花画成扁平的放射状色块；人群只画成一排排重复的深色剪影单元，不画脸。 构图： 竖幅单幅插画，少女位于画面偏左三分，右侧留出摊位与人群的纵深；地平线压在画面下三分之一，上方交给夜空与烟花。 视觉引导： 视线由前景小灯的暖色串引入，沿摊位招牌的斜线向上扫向少女的侧脸，再被她身后深蓝夜空里的烟花接住；人群剪影的横向排列提供反向拉扯。 色调： 克制的配色，只用深蓝夜空、浅青浴衣、暖橘灯光、奶油白四个主色；每个色只用一块平色，不叠色、不做渐变、不做光泽；天空与墙面都是平涂色块。 风格： 日式全彩插画，墨线之上单层平涂上色；用漫画蘸水笔加重外侧轮廓、内侧细节用极细线，粗细差异是刻意的；所有颜色严格限制在墨线之内、不外溢也不混色；全画面只有底色与硬边暗部两层平涂，中间没有过渡；不出现网点、噪点、颗粒，也不要任何摄影感；不出现任何文字与气泡。 光影氛围： 夜景口味——背景整体压暗成平涂色块，光源画成平涂的色块而不是光晕；单一主光来自画面左下的摊位暖灯，受光面与背光面各是一块硬边单层平涂，没有第三层过渡；头发与肩头各有一块边界清楚的实色暖白高光；深蓝夜空作冷色底，与暖灯冷暖对冲
```

**实测记录**：模型 `Krea2-seeKrea2_genesisInt4Convrot_int4_convrot`（**本册全彩首选**）· 一采 `euler/simple/8 步/cfg 1.0` · 二采 `4 步/denoise 0.38` · `ResolutionSelector = 9:16` · 放大 `OmniSR_X4_DIV2K`（1152×2048 → 1728×3072）。

**判读 · 六命中**：平涂干净（无网点、无颗粒、无摄影感）✅ / **灯罩是扁平实色圆块且不加光晕** ✅ / 苹果糖是**单颗**（没被改成糖葫芦）✅ / 构图**偏左三分**、右侧留出人群纵深 ✅ / 烟花画成**扁平放射状色块** ✅ / 颜色不越墨线、高光是硬边实色块 ✅。

**判读 · 两未锁**：① **数量词被弱化**——词里写"几簇烟花"，实际只出 **1 簇**（→ 要数量就写确数，别用"几"）；② **纯两层平涂被延伸**——浴衣暗部出现**蘸水笔排线**（模型把"蘸水笔主线"延伸到暗部），严格说多了一层排线。

**同词反面对照**：同一条词挂 `Krea2-Moody-Mix-premium_int8_convrot` → 也出画且好看，但**加提灯+光晕、苹果糖变三颗、主体居中** → **按册子施工固定 `genesis`**。

---

### 形态 B 范例（十段式 · 日式黑白单幅）

> 段↔层映射见 `SKILL.md` §1.4。**换口味只改「色调 / 风格 / 光影氛围」三段，换流派要连同「中景 / 前景」的线稿词一起改。**

**主体：** 一位身穿旧制服的少女独自站在雨后的居民楼天台中央，背对城市，双手插在外套口袋里，肩膀因为冷而微微耸起。
**要点：** 靠"G 笔粗细层级、百分之七十网点、铅笔底稿痕、四角裁切标记"四件工序痕迹把"这是画在纸上的漫画"钉死；时段由网点密度而非布光交代。
**前景：** 画面底部是龟裂的水泥天台面，一道裂缝里嵌着碎烟头与一截铁丝，左侧斜靠着一摞塑料凳，凳脚边积着一汪未干的水，水面用大片纯白留白反光。
**中景：** 少女站在齐腰高的水泥矮墙前，外套下摆被风掀向左后方，发丝用三五根收笔出锋的短线甩出；矮墙外侧挂着一根晾衣绳，两件衣服绷成弧形，全部用硬边实黑处理。
**背景：** 她身后是层层退去的旧楼群，屋顶的水塔与太阳能热水器只用轮廓线与少量细网点交代；更远的一条高架路上没有车，只有一排由密到疏的网点渐变，把车流抽象成灰度的流动。
**构图：** 竖幅单幅，人物位于画面下半部中央、约占高度三分之一，上方留出大片空白天空，只在右上角用一块百分之七十的网点压出暮色区块，形成不对称的重心。
**视觉引导：** 视线由左下角水洼的纯白高光起，沿矮墙的横线扫向人物的肩线，最后被右上角那块深网点吸住；斜贯画面的几道直线提供反向拉扯，画面里没有一处让视线停住的地方。
**色调：** 全页只有黑、白与网点灰三个层次；实黑集中在人物外轮廓与衣物暗面，纯白留给水面反光与天空，中间调一律交给点阵，画面里没有灰阶渐变。
**风格：** 黑白漫画单幅，网点印刷，墨线印在纸上，保留原稿纸的纸纹与网点套印的轻微偏移，线条是笔尖拉出来的墨线，画面里没有三维渲染的光泽。
**光影氛围：** 没有摄影意义上的光源——光由网点密度表达：天空最亮处完全留白，越靠画面右上密度越高，人物脸部的暗面用一块 40% 的点阵压住，衣褶内的阴影全部处理成硬边实黑。

---

## 本册的锚定自查（出稿前必过）

- [ ] **媒介词写死了**（日式黑白 / 美式英雄 二选一）
- [ ] 至少一个**墨线工具**（G 笔 / 丸笔 / brush ink / nib pen），且明示**粗细差是有意的**
- [ ] 至少一处**工序痕迹**（原稿纸 / 裁切线 / 铅笔底稿 / 修正白 / 网点套印偏移）
- [ ] 网点写成**规则点阵**，全文**没有** `noise` / `grain` / `texture`
- [ ] **只用一个流派**的词（没有 G-pen 与 brush ink 混写）
- [ ] 多格页写了**阅读顺序**，且每格一句说清"这一拍做什么"
- [ ] 气泡写的是**形状**（圆形 / 锯齿 / 云形 / 方框），不是笼统的 `speech bubble`
- [ ] 有文字时**放进双引号**并说明语言；拟声词语言与流派一致
- [ ] **全彩（赛璐璐）时**：影是**硬边单层平涂**（不是柔和渐变），高光是**实色块**（不是发光晕），颜色**不越出墨线**
