# KB-INDEX · GUI-LINEAGE-KB 总入口

> GUI-LINEAGE-KB 把八条 GUI 对话线的研究脉络、D3 六百一十九条认知资产、跨线传播图与五概念演变史
> 组织成一份可检索、可回溯、可审计的知识库。本文件是**唯一总入口**：任何问题从这里出发，
> 按 §1 路由表走，最多三跳；本库确实答不了的那些问题，§13 逐条列明去哪找、为什么本库不答。
>
> **本文件不产出任何数学结论（R7）**：全库只登记脉络、判词身份、资产归宿、断链与未知；
> 任何命题的数学地位由 `HoTT/CLAIM_EVIDENCE_MATRIX.md` 与项目 F-011 门禁拥有。
>
> 修订记录：v1 2026-10-10（N9 初版）；v2 2026-10-10（N9 修订：补编号词汇表、C 编号索引、
> 祖先线轮次表、ref 限定路径解析指南、共同前段 open 资产层粒度答案、状态比对入口；修正规模数字与工具路径）。

## 1. 怎么用这份知识库（路由表：八类问题 → 入口行）

| # | 你想知道 | 从这里进（第 1 跳）| 然后（第 2、3 跳）| 跳数 |
|---|---|---|---|---|
| 1 | **某条线在某个阶段想做什么** | §4 八线卡片 → `dev-0X/THREAD.md` | 每层「这一层在做什么」/「目标-SOP」；单轮粒度再读该线 `DISCOVERIES.tsv` 的 claim 列 | 2（单轮最坏 3）|
| 2 | **某轮得到了什么判词** | §4 卡片 → THREAD 每层「发现与判词（逐字）」；或 §5 表 → `ROUTE-GRAPH.md` §2 节点表「该层判词」列 | 单轮级读 TSV `verdict_token` 列（列义见 §3.3）| 2 |
| 3 | **为什么转向** | `ROUTE-GRAPH.md` §4 边表 B「否决」（11 条，逐条带用户原话＋后果）| 或回该线 THREAD 每层的「为什么转向」段（八线每层都有）| 2 |
| 4 | **一条发现怎么传到下游** | `ROUTE-GRAPH.md` §3–§5（供给 8／否决 11／接走 29）| 撞号区资产再看 §6 与 `CROSS-FEED.md` §2.1 | 2 |
| 5 | **P/Q/Done/Z0/想法 T 怎么变的** | `EVOLUTION.md` §1–§5（54 步）| 每步有 `线/round`＋导出行号，可逐条回读 | 2 |
| 6 | **某个资产现在何处** | 有 A-ID：`CROSS-FEED.md` §3 五张表 | 有 C 编号：§6 C 编号索引 → claim matrix 行＋formal 路径＋GUI 来源 | 2 |
| 7 | **`origin/dev-0X:<path>` 现在哪个提交、拉得下来吗** | §7 ref 限定路径解析指南（含本机实测的八个分支当前 tip 与命令）| 按表中命令自查 | 1 |
| 8 | **共同前段那批 open 资产被谁接走了** | §9 共同前段 open 资产层粒度答案（190 条按 CG-006 层区间归组）| 单条查 `CROSS-FEED.md` §3 → 首现列 → QA 树 | 2 |

还有两类问题走专节：**祖先分叉线**（§8）、**知识库与当前研究状态对不对得上**（§10）。

**检索工具（在 CG-006 包内，不在本 workflow 产物内）**：

```bash
# 相对仓库根执行；工具实际位置在 CG-006 包的 tools/ 下（2026-10-10 实测 find 确认）
python3 .claude/goals/CG-006-zfc-complete-formalization/tools/gui_find.py --show dev-08/0117
python3 .claude/goals/CG-006-zfc-complete-formalization/tools/gui_backtrace.py dev-01 --from 14 --to 20
```

## 2. 三套坐标系与记号约定（不可互换；读任何表前先确认）

### 2.1 三套坐标

| 坐标 | 权威来源 | 用途 | 禁 |
|---|---|---|---|
| QA 块坐标 `线/round`（八线自有 239 轮，机械轮也计）| `wflow-lineage/scope.json` 每线 `docs[]` | 逐轮身份、轮次归属 | 不得与裁决 #3 互换 |
| GUI 导出行号 `L14846` | 各线 `THREAD.md` / `DISCOVERIES.tsv` 的 `export_line`，取 scope 锚点 | 回读原文 | 不得把 `audit/GUI-SYNTH-REDO/qa/<线>/_index.jsonl` 的 rollout 行号当导出行号 |
| 裁决 #3 分线轮数（八线合计 124）| `认知闭包/GUI-ASSET-RECOVERY-001.md` §8 | 只作并列引用 | 定义在 raw rollout 上，冻结输入层内不可重算；不得用于逐轮定位 |

### 2.2 记号约定（三处最容易踩）

1. **`L` 有两个意思**：写「`dev-06/THREAD.md` 层 L6」时 L6 是**层名**；写「L14846」时是**GUI 导出行号**。
   本库自己的文本已尽量写成「层 6」与「导出行 14846」两种措辞；遇到旧写法按上下文分辨——层名只有个位数（L0–L10 且带线名前缀），
   导出行号是 4–5 位数（1132–18698）。
2. **层号是各线私有的倒序年代编号**：每条线都从分叉点往尾数，所以 dev-08 的「L4」与 dev-01 的「L4」**不是同一阶段**；跨线比较请用 §5 的轮次锚或 `EVOLUTION.md` 的概念步号。
3. **「裁决 #3」是口径名，不是第三条判决**：它指 `认知闭包/GUI-ASSET-RECOVERY-001.md` §8 里按 raw `role=user` 记录剔机械前缀得到的**分线轮数**（八线合计 124）。
   名字里的「#3」是闭包文档内裁决的序号；凡写「裁决 #3 口径」处都指这套计数，与本库默认使用的 QA 块坐标（239 轮）是两套口径，不可互换（R4 / ledger PRE-4 DECISION）。

## 3. 编号与缩写词汇表（本库全部内部约定，权威出处一并给出）

### 3.1 workflow 规则、门禁与登记号

| 记号 | 含义 | 权威出处 |
|---|---|---|
| `R1`–`R9` | 本 workflow 的九条硬口径：R1 双锚／R2 判词逐字／R3 身份四分离／R4 轮数口径／R5 不重算只引用、冲突并陈／R6 冻结输入只写自己路径／R7 无数学结论／R8 幂等与断点（ledger 追加）／R9 语料固有缺口 | `dev-docs/GUI研究脉络知识库提取workflow方案.md` §4 |
| `G1`–`G8` | 完成门禁：G1 覆盖／G2 双锚／G3 判词保真／G4 不丢／G5 传播图闭合／G6 链接／G7 口径一致／G8 零未申报未知 | 同上 §5 |
| `PRE-1`…`PRE-15`、`N0`/`N-dev-0X`/`N-corr` | `wflow-lineage/ledger.jsonl` 里的节点号：PRE＝开工前预处置与运行中期补登记，N＝本 workflow 派发的节点 | `wflow-lineage/ledger.jsonl`（append-only，Master 与各 agent 各写各的）|
| `N-1`…`N-9` | 本文件 §12 的缺口编号 | 本文件 §12 |
| `S-n`/`V-n`/`C-an`/`C-bn`/`C-cn` | `ROUTE-GRAPH.md` 的边号：S＝供给（父→子）、V＝否决、C-a＝下游接走、C-b＝线间横向接走、C-c＝版本化落点 | `ROUTE-GRAPH.md` §3–§5 |
| `C-1`…`C-8` | `CROSS-FEED.md` §2.2 的两说并陈编号（本 agent 不裁决）| `CROSS-FEED.md` §2.2 |

### 3.2 资产与编号空间

| 记号 | 含义 | 权威出处 |
|---|---|---|
| `A-0001`…`A-0624` | D3 资产账本编号（619 条，5 个号在账本中即不存在：A-0337、A-0424–A-0427）| `audit/GUI-ASSET-RECOVERY/assets-ledger.md`；归并视图 `audit/GUI-ASSET-RECOVERY/D3-资产登记v2-20261007.md` |
| `D3` | 上表的文件名简称（资产登记 v2）；其五类＝概念 72／方法 212／形式化 46／来源 134／开放候选 155 | 同上 |
| `K4` | 审计预登记的 claim 编号撞号区：C-359~C-365（`dev` 与 dev-02 同号异组）、C-369 三义、C-370 起（dev-01／dev-09／`dev` 各指一组）| `dev-docs/GUI研究脉络知识库提取workflow方案.md` §5 G5；`.claude/goals/CG-006-zfc-complete-formalization/八线分叉后复盘.md` §9.5 |
| `C-nnn` | **claim 编号，有三套前缀空间**（见 §6）：无前缀＝`HoTT/CLAIM_EVIDENCE_MATRIX.md` 的 canonical 编号；`CG001-C-nnn`＝主线 CG-001 的 Cubical Agda 包编号；`D01-C-nnn`／`D09-C-nnn`＝dev-01／dev-09 分支并入时为消歧加的前缀 | `HoTT/CLAIM_EVIDENCE_MATRIX.md`（1995 行，本机在）|
| `H0`/`Z0`/`Q`/`P`/`A`/`B` | 研究对象层概念（H0＝main 固定 HoTT 追问程序；Z0＝H0 在 ZFC 侧的对应物；Q＝缺失的观察力；P＝无桥完成提升；A/B＝芝诺侧与 HoTT 侧结果）| `EVOLUTION.md` §1–§5；`Targets与Profile.md` §3 |
| `SOP` 名 | 各线研究程序名（`T-PRECISION-DIAGONAL-SOP`、`GODEL-ZFC-CONVERGENCE-SOP`、`ZFC-META-SUBTHEORY-ADEQUACY-SOP` 等），逐条在各线 `THREAD.md` | 各线 `THREAD.md`；`Targets与Profile.md` §2 |

### 3.3 `DISCOVERIES.tsv` 的 12 列（无表头，制表符分隔）

```text
id  line  layer  round  export_line  type  claim  verdict_token  artifact_ref  status  propagated_to  notes
```

- 列义逐字定义（12 列约定、`type`/`status` 枚举、判词逐字规则、机械轮 `MISSING` 规则）见 `dev-01/THREAD.md` 第 11 行；
  机器可执行版本见 `wflow-lineage/tools/check_lineage.py:42`。
- `status` 五枚举：`carried`／`parked`／`superseded`／`cold`／`open`（含义与 `CROSS-FEED.md` §1 的处置规则一致）。
- `propagated_to` 列给该行发现的下游落点；`artifact_ref` 列给 `路径@git-ref`（ref 解析见 §7）。

### 3.4 层号 `L0` 的三义与「有没有 L0」

| 线 | 层的编号方式 | 层数 | `L0` 是什么 |
|---|---|---|---|
| dev-08 | `L0`–`L8`（尾→分叉）| 9 | **共享前缀骨架层**（#0001–#0075，只建层名＋一句话）|
| dev-03／dev-04／dev-06／dev-07／dev-09 | `L0` 起（尾→分叉）| 7／6／8／6／9 | **机械轮**（无 prose 的 environment／page／goal 注入轮）|
| dev-01 | `层 1`–`层 10`（ numbered by 汉字「层 N」）| 10 | **没有 L0**：最末层是 `层 10`（分叉点层）|
| dev-02 | `L1`–`L8`（L1 在最尾）| 8 | **没有 L0**：最末层是 `L8`（机械前缀层与分叉基座）|

> 因此两条线的「L3」几乎从不指同一阶段；`ROUTE-GRAPH.md` §2 的节点表已把每条线的层名连同轮次区间逐字列出，跨线比较请以轮次区间为准。

## 4. 八线卡片（每张＝一个 `lineage/<线>/` 目录）

| 线 | GUI 标题 | 分叉点 | 自有轮（块坐标／裁决#3）| 层数 | 层号方向 | THREAD 行数 | DISCOVERIES 行数 | THREAD | DISCOVERIES |
|---|---|---|---|---|---|---|---|---|---|
| **dev-01** | # 🌟 01 - ZFC-1 | dev-08 #111 | 21／10 | 10 | 层 1（尾）→ 层 10（分叉） | 123 | 53 | `dev-01/THREAD.md` | `dev-01/DISCOVERIES.tsv` |
| **dev-02** | # 02 - ZFC-1 | dev-08 #86 | 13／10 | 8 | L1（尾）→ L8（分叉） | 257 | 129 | `dev-02/THREAD.md` | `dev-02/DISCOVERIES.tsv` |
| **dev-03** | # 03 - ZFC-1 | dev-08 #75 | 26／18 | 7 | L6（尾）→ L0（分叉/机械） | 139 | 108 | `dev-03/THREAD.md` | `dev-03/DISCOVERIES.tsv` |
| **dev-04** | # 04 - ZFC-1 | dev-03 #13 | 15／11 | 6 | L5（尾）→ L0（分叉/机械） | 145 | 114 | `dev-04/THREAD.md` | `dev-04/DISCOVERIES.tsv` |
| **dev-06** | # 🌟 06 - ZFC-1 | dev-08 #97 | 13／7 | 8 | L1（尾）→ L0（分叉/机械） | 279 | 55 | `dev-06/THREAD.md` | `dev-06/DISCOVERIES.tsv` |
| **dev-07** | # 🌟 07 - ZFC-2 ω 的完成性 | dev-06 #3 | 8／4 | 6 | L1（尾）→ L0（分叉/机械） | 324 | 64 | `dev-07/THREAD.md` | `dev-07/DISCOVERIES.tsv` |
| **dev-08** | # 🌟 08 - 哥德尔（主干；主 checkout 的 dev） | archive-01a0fb73 #10 | 127／56 | 9 | L8（尾）→ L0＝共享前缀（分叉） | 127 | 154 | `dev-08/THREAD.md` | `dev-08/DISCOVERIES.tsv` |
| **dev-09** | # 🌟 09 - 哥德尔 | dev-08 #113 | 16／8 | 9 | L8（尾）→ L0（分叉/机械） | 131 | 50 | `dev-09/THREAD.md` | `dev-09/DISCOVERIES.tsv` |

每个 `lineage/<线>/` 目录只有这两个文件（R6：子代理只写自己被分配的路径；未改动任何既有产物）。
「THREAD 行数／DISCOVERIES 行数」是 2026-10-10 实测值（`wc -l`），与 §5 的规模数字同源。

## 5. 四个综合文件（本 workflow 的 N9 产物；规模为 2026-10-10 实测）

| 文件 | 内容 | 实测规模 | 机验 |
|---|---|---|---|
| `ROUTE-GRAPH.md` | 分叉树＋63 个层节点＋48 条跨线边（供给 8／否决 11／接走 29）| **202 行** | 分叉父子 8/8 与 `qa/_tree.json` 一致 |
| `EVOLUTION.md` | P/Q/Done(OriginDone)/Z0/想法 T 五概念跨线演变 | **154 行、54 步** | 每步带 `线/round`＋导出行号 |
| `CROSS-FEED.md` | D3 619 条资产逐条归宿 | **754 行** | 619 A-ID 唯一、归宿枚举合法 619/619 |
| `KB-INDEX.md`（本文件）| 总入口＋编号词汇表＋C 编号索引＋ref 解析指南＋链接校验表 | 见文件末 | 见 §11 |

### 5.1 `carried`（已接走）的两档强弱——读 `CROSS-FEED.md` 前必看

`CROSS-FEED.md` §0 把 316 条 `carried` 合在一列，但它们由四种证据得来，强度不同。逐条的强弱写在
那一行的「一句理由」里（本表只给汇总，便于先建立预期）：

| 档 | 证据 | 条数 | 读法 |
|---|---|---|---|
| **强：资产级落点** | ①八线 TSV 的 `carried` 行给显式 `propagated_to`；②CG-006 三文件点名该资产内容；③账本注记进入 canonical owner（rulings／核心认知／KC／落盘）；⑤撞号区内有 D01-／D09- 前缀消歧并入或 CG-005 重放 | **161** | 可当作「这个资产已被下游吸收」|
| **弱：轮次级线头** | ④所在轮被 CG-006 列为线头（`GUI查阅索引.md` §1 主题表的「位置」列／`Targets与Profile.md` 线头列）| **155** | 只表示「该轮是 CG-006 的检索入口」；**不等于该资产被单条吸收**——需回那一轮原文确认 |

> 分档计数为 N9 在 2026-10-10 用同一套判据复算的实测值（161＋155＝316，与 `CROSS-FEED.md` §0 合计一致）；分档判据逐字写在 `CROSS-FEED.md` §1 表第 3 行，
> 逐条理由列在 §3 每一行。N10 若把第④档改判为 `open`，`carried` 总数会降到 161，其余四归宿不变。

## 6. C 编号索引（C-nnn 是什么、现在何处、属于哪一组、能不能取用）

claim 编号有三套前缀空间，**同名不同物**是本库最硬的坑：

| 前缀 | 含义 | 现在何处 |
|---|---|---|
| 无前缀 `C-nnn` | canonical claim 编号 | `HoTT/CLAIM_EVIDENCE_MATRIX.md`（本机在，1995 行；每行给命题、状态、formal 路径、run 收据）|
| `CG001-C-nnn` | 主线 CG-001 的 Cubical Agda 包编号（如 `CG001-C-83` 截断追问）| 同上，矩阵内有带前缀的行 |
| `D01-C-nnn`／`D09-C-nnn` | dev-01／dev-09 分支并入 `dev` 时为消歧撞号而加的前缀；矩阵内逐字标注「（分支原编号 C-nnn）」| 同上（如 `D01-C-369`＝L1914、`D09-C-370`＝L1931）|

### 6.1 常见 C 编号索引（按编号排序；「GUI 来源」指该编号在八线导出中的首次出现）

| C 编号 | claim matrix 行 | 状态（矩阵原文截断）| formal 路径（矩阵内）| GUI 来源（线/round＋A-ID）| 归属组与可用性 |
|---|---|---|---|---|---|
| C-83 | L131／L1748 | `MACHINE_PROVED_LOCAL_UNCOMMITTED`／`FORMAL_CHECKED_WITH_SCOPE` | `formal/claude-cg001/truncation-questioning/TruncationQuestioning.agda` | dev-04/0006、0008（A-0473） | **CG001 组**（Cubical Agda 截断追问）。可用；`origin/dev-04` 上可解析 |
| C-90 | L138／L1882 | `MACHINE_PROVED_LOCAL_UNCOMMITTED`／`FORMAL_CHECKED_WITH_SCOPE` | `formal/claude-cg001/godel-q/…`（CG001-C-90 魔鬼交易族） | （CG-005/006 侧；GUI 线只在 THREAD 转述中出现） | **CG001 组**。可用；GUI 各线无独立 A-ID |
| C-93 | L141／L1885 | `MACHINE_PROVED_LOCAL_UNCOMMITTED`／`FORMAL_CHECKED_WITH_SCOPE` | `formal/claude-cg001/godel-q/…`（同一 ω 追问图式） | dev-07/0006 转述（A-0561 一带） | **CG001 组**。可用 |
| C-94 | L142／L1886 | 同上 | `formal/claude-cg001/godel-q/…`（`AGeneral ↔ CompleteForNever`） | dev-03/0009–0013、dev-07/0006 转述 | **CG001 组**。可用 |
| C-101 | L149／L1893 | 同上 | `formal/claude-cg001/godel-q/…`（ZFC 版） | dev-03/dev-07 THREAD 转述 | **CG001 组**。可用 |
| C-103 | L151／L1962 | 同上 | `formal/claude-cg001/godel-q-zfc-z0/…` | dev-06/dev-07 THREAD 转述（Z0 条件形式） | **CG001 组**。可用 |
| C-275 | L1164 | `FORMAL_CHECKED_WITH_SCOPE` | （矩阵内路径） | dev-03/0008（A-0420） | **dev-03 组**（实几何对齐）。可用 |
| C-357 | L1749 | `KERNEL_ACCEPTED_WITH_SCOPE` | `formal/claude-cg001/observation-completion-bridge/ObservationCompletionBridge.agda` | dev-08/0080（A-0293） | **CG001 命名组**（八线复盘 §8 注 A7：这两条用 Claude 线 `-CG001-` 命名）。可用 |
| C-358 | L1750 | `KERNEL_ACCEPTED_WITH_SCOPE` | `formal/claude-cg001/completion-reflection-failure/CompletionReflectionFailure.agda` | dev-08/0080（A-0294） | **CG001 命名组**。可用 |
| C-359 | L1778 | `KERNEL_ACCEPTED_WITH_SCOPE` | `formal/zfc-actual-q-policy/ZFC1IllusionPolicy.lean` | dev-08/0088（A-0319）＋dev-02/0003（A-0505） | **K4 撞号**：`dev` 组与 dev-02 组同号异组。`dev` 组在矩阵内；dev-02 组在 `origin/dev-02`，并入前须重编号 |
| C-360 | L1779 | `KERNEL_ACCEPTED_WITH_SCOPE` | `formal/zfc-actual-q-policy/HoTTCounterexample.agda` | dev-08/0088（A-0320）＋dev-02/0003 | **K4 撞号**（同上）；CG-005 已重放通过（复盘 §3【实物】）|
| C-361 | L1780 | `KERNEL_ACCEPTED_WITH_SCOPE` | `formal/zfc-actual-q-policy/ZenoLimitControl.lean` | dev-08/0088（A-0321）＋dev-02/0003 | **K4 撞号**（同上）|
| C-362 | L1781 | `KERNEL_ACCEPTED_WITH_SCOPE` | `formal/zfc-actual-q-policy/ZenoSourceCompletionContract.lean` | dev-08/0090（A-0328）＋dev-02/0006（A-0517） | **K4 撞号**（同上）|
| C-363 | L1782 | `KERNEL_ACCEPTED_WITH_SCOPE` | `formal/zfc-actual-q-policy/HoTTCompletionContract.agda` | dev-08/0090（A-0329）＋dev-02/0006（A-0518） | **K4 撞号**（同上）|
| C-364 | L1783 | `KERNEL_ACCEPTED_WITH_SCOPE` | `formal/bare-zfc-q-precision/BareZFCPrecision.lean` | dev-08/0096（A-0339）＋dev-02/0007（A-0522） | **K4 撞号**（同上）|
| C-365 | L1784 | `KERNEL_ACCEPTED_WITH_SCOPE` | `formal/zfc-h0-final-closure/H0TraceObservation.agda` | dev-02/0007（A-0523）＋dev-04/0008（A-0480） | **K4 撞号**：`dev` 组＝H0 trace；dev-02 组＝成员语言不变性。**两个命题同名不同物**，取用前必须看矩阵行 |
| C-366 | L1785 | `KERNEL_ACCEPTED_WITH_SCOPE` | `formal/zfc-h0-final-closure/H0ProcessRepresentation.lean` | dev-08/0105（A-0356） | **dev 组**。可用 |
| C-367 | L1786 | `KERNEL_ACCEPTED_WITH_SCOPE` | `formal/t-precision-observation/ObservationPrecision.lean` | dev-09/0006（A-0601）＋dev-08/0116（A-0369） | **dev 组**（T-OBS）。可用；`GUI查阅索引.md` #9 线头 |
| C-368 | L1787 | `KERNEL_ACCEPTED_WITH_SCOPE` | `formal/t-precision-diagonal/AcceptanceDiagonal.lean` | dev-09/0008（A-0605） | **dev 组**（T-DIAG 条件性对角铰链）。可用 |
| C-369 | L1801 | `KERNEL_ACCEPTED_WITH_SCOPE` | `formal/godel-q-reflection/SetMMAppendixCVarExtension.lean` | dev-08/0123（A-0387） | **K4 三义**：①矩阵内 dev 组＝set.mm Appendix C 变量扩张；②`D01-C-369`＝dev-01 的 ApplicationAdequacy（L1914）；③dev-02 的 C-369 收据链。取用必须带前缀或看矩阵行 |
| C-370 | L1816 | `KERNEL_ACCEPTED_WITH_SCOPE` | （矩阵内 `zfc-normative-process-audit` 族） | dev-01/0019（A-0590）＋dev-09/0012（A-0620） | **K4 三组**：dev 组（L1816）；`D01-C-370`＝量化半步第 4 步完成（L1915）；`D09-C-370`＝CCTTmini 正例（L1931）|
| C-371 | L1817 | `KERNEL_ACCEPTED_WITH_SCOPE` | （同上族） | dev-01/0019（A-0590） | **K4 三组**：`D01-C-371`＝稠密 vs 量化 finite-stage Done 不等价（L1916）|
| C-375 | L1835 | `KERNEL_ACCEPTED_WITH_SCOPE` | `formal/zfc-mss-domain-time-control/…` | dev-08/0126（A-0397） | **dev 组**（MSS 定义域控制）。可用 |
| C-376 | L1836 | `KERNEL_ACCEPTED_WITH_SCOPE` | 同上 | dev-08/0126（A-0397） | **dev 组**。可用 |
| C-377 | L1851 | `KERNEL_ACCEPTED_WITH_SCOPE` | `formal/zfc-mss-phase-order-control/…` | dev-08/0126（A-0398） | **dev 组**（参数顺序控制）。可用 |
| C-378 | L1852 | `KERNEL_ACCEPTED_WITH_SCOPE` | 同上 | dev-08/0126（A-0398） | **dev 组**。可用 |
| C-379..C-386 | — | （D09 组，矩阵 `D09-C-375`–`D09-C-386` 段） | `formal/cubical-godel-fragment/…` | dev-09/0012–0013（A-0620） | **D09 组**（CCTTmini）。已并入 `dev`，可用 |

> 表中「claim matrix 行」为 2026-10-10 本机 `grep` `HoTT/CLAIM_EVIDENCE_MATRIX.md` 的实测行号；
> 状态列逐字照录矩阵原文（不升级、不改写，R7）。K4 撞号区的**逐条**资产处置见 `CROSS-FEED.md` §2.1
> （本表只答「属于哪一组、现在何处」；「能不能取用」的最终形态由研究发起人/审计员裁定，本库按方案 §5 G5 预登记记 parked）。

## 7. `origin/dev-0X:<path>` 形式的 ref 限定路径：现在何处、怎么验

八线 `DISCOVERIES.tsv` 的 `artifact_ref` 列大量使用 `<路径>@<git-ref>`（如
`audit/20261003-ZFC-CIRCLE-Q0-…md@origin/dev-03`）。这类路径的含义是「该 ref 上的该文件」，不是本工作区的文件。

### 7.1 八个远端分支的当前 tip（2026-10-10 本机实测）

```bash
git ls-remote --heads origin | grep -E "dev-0[0-9]"     # 远端真值（需网络）
git rev-parse --short origin/dev-0X                     # 本地 remote-tracking（fetch 后同步）
```

| 分支 | 远端实测 tip（2026-10-10）| 本地 `origin/<分支>` | 与八线复盘 §0（2026-10-08 fetch）| 导出自述落点 |
|---|---|---|---|---|
| `origin/dev-01` | `f10899cb` | `f10899cb`（一致）| `f10899cb` | `ca1259fe`→`cd9e34b2`（dev-01/0007、0021）|
| `origin/dev-02` | `4005fa80` | `4005fa80`（一致）| `4005fa80` | `4ab6bf54`→`4005fa80`（dev-02/0010–0013）|
| `origin/dev-03` | `854a6aba` | `854a6aba`（一致）| `854a6aba` | `854a6aba`（dev-03/0026）|
| `origin/dev-04` | `f97bbcb4` | `f97bbcb4`（一致）| `f97bbcb4` | `69aa5aab`（dev-04/0015）——导出后仍有提交 |
| `origin/dev-06` | `af0d9c5c` | `af0d9c5c`（一致）| `af0d9c5c` | `86ad33c4`（dev-06/0013）——导出后仍有提交 |
| `origin/dev-07` | `a753f9bc` | `a753f9bc`（一致）| `a753f9bc` | `49624878`→`9dd0b61b`（dev-07/0007–0008）——导出后仍有提交 |
| `origin/dev-08` | `3cb6a6b4` | `3cb6a6b4`（一致）| `81e2f12c` | `7b1f7f60`（dev-08/0127）——2026-10-08 之后又有提交 |
| `origin/dev-09` | `ac6391b6` | `ac6391b6`（一致）| `ac6391b6` | `1c34aaee`→`ac6391b6`（dev-09/0009、0016）|

**remote**：`https://github.com/math-fournity/HoTT-Paradoxy.git`（本机 `git remote -v` 实测）。
八条线全部可 fetch（本次实测网络可达、8/8 tip 取到）。

### 7.2 逐条 ref 限定路径怎么验

```bash
# 单条：把 <路径>@<ref> 拆成 "ref:路径"
git cat-file -e "origin/dev-03:audit/20261003-ZFC-CIRCLE-Q0-连续统完成与圆环复原候选卡.md" && echo OK
# 列目录：某个 ref 上某个目录下有什么
git ls-tree -r --name-only origin/dev-09 -- HoTT/formal/external-cctt-r4
```

**N9 实测规模（2026-10-10）**：把八线 TSV 的 `artifact_ref`/`propagated_to`/`notes` 三列里全部 `<路径>@<ref>` 抽出，
共 **99 个不同 (ref, 路径) 对**，逐条 `git cat-file -e`：**99/99 解析成功**（其中 1 条初判 FAIL 是因我的正则把含空格的
中文路径 `…/003 - P3 构造状态与准入次序.md` 截断了，用完整路径复测即 OK——这条路径本身没问题）。

### 7.3 「本工作区没有、但 ref 上有」的两个路径

| 路径 | 本工作区 | `origin/dev-09` | 说明 |
|---|---|---|---|
| `HoTT/formal/external-cctt-r4/`（Positive/Hole/Recursive/TypeError.cctt、restricted_profile.py、verify_cctt_r4_run.py 等 9 个文件）| **不存在**（`ls` 实测 No such file or directory）| **存在**（`git ls-tree` 实测 9 个文件）| 即 `CROSS-FEED.md` §3 A-0616 行的 carried 落点（那一行写「`HoTT/formal/external-cctt-r4/`…」）；dev-09/0012 的 cctt R4 输入域资格化实物。本工作区看不到它，是因为它在 dev-09 线上、未并入本 checkout —— 本节与 `CROSS-FEED.md` 那一行说的是同一件事的两种状态（路径在 ref 上有效、在当前 checkout 中无副本）|
| `HoTT/formal/external-foundation-incompleteness/`（Qualification.lean、WrongMissingSoundness.lean、CLAIM-R3-…md 等）| **不存在** | **存在**（实测）| dev-09/0012 的 Foundation 重放实物。`dev-09/THREAD.md` 与 `GUI查阅索引.md` §2 都说「检出在 `/tmp`，已失」——那指的是**该轮当时的运行检出物**，后来已作为项目文件提交到 `origin/dev-09`（本机实测可读）|

## 8. 两条祖先分叉线（`archive-01a0fb08`、`archive-01a0fb73`）发生了什么

本 workflow 没有为祖先线建 `THREAD.md`/`DISCOVERIES.tsv`（R6 只派八线），但**问答树里有它们的轮次切片**：
`audit/GUI-SYNTH-REDO/qa/archive-01a0fb08/`（3 轮）、`…/archive-01a0fb73/`（10 轮）。
下表逐轮给锚与首句用户原话（2026-10-10 本机读切片实测），回答「祖先线某一轮在做什么」。

| 祖先线/轮 | 该轮在做什么（据切片首句用户块）| 下游关系 |
|---|---|---|
| archive-01a0fb08/0001 | 机械轮（`external_codex_apps_open_page`），无 prose | — |
| archive-01a0fb08/0002 | **选靶**：菲尔兹奖得主工作已入库并要求 minerU 转码；「既然我们找到了 HoTT 的问题……下一个最值得进攻的目标是哪一个？」| 成为 `Targets §2.0` 的 R00 段 |
| archive-01a0fb08/0003 | 用户贴入另一 AI 的选靶回答，要求比较 | 同上 |
| ↓ 分叉 | `_branch.json`：parent_doc=3，cutoff end_ordinal_exclusive=1490 | archive-01a0fb08 → archive-01a0fb73 |
| archive-01a0fb73/0001、0002 | 机械轮（environment_context／external page），无 prose | — |
| archive-01a0fb73/0003 | **靶的层级裁定**：「芝诺悖论打的是微积分的基础理论……罗素悖论打的是当年的朴素集合论。今天，我们打的是 HoTT……而实数理论，是整个微…」| 成为 dev-08 `THREAD` L0-a 与 A-0001；`Targets §2.0` R01 段 |
| archive-01a0fb73/0004 | 用户贴另一 AI 的选靶回应 | 同上 |
| archive-01a0fb73/0005 | 用户要求把分层分析落盘成路线图 | A-0006（路线图索引＋5 分片 417 行）|
| archive-01a0fb73/0006 | **Gemini 来源审计任务**：「Google Gemini 有很大的数学幻觉……它曾经声称自己找到了 ZFC 的悖论」| A-0007/A-0010/A-0011（三类叙事判定表、四项检查＋三反控制）|
| archive-01a0fb73/0007 | annotation 轮：把 Gemini「表征不协调」降级为非形式矛盾，转化为未来 ZF(C) 候选的四项检查＋三反控制 | A-0011 |
| archive-01a0fb73/0008 | 「你为什么总要去找菲尔兹奖入口呢？」→ GPT 承认误升级为硬门 | 选靶纪律进入 rulings |
| archive-01a0fb73/0009 | annotation 轮；「这个方向，继续」| A-0015（Mumford）、A-0017（mathlib IsIso/Skeletal 消费者防线）|
| archive-01a0fb73/0010 | **启发式授权**：「这些理论的知识都在你的内在的神经网络中……ZFC 到底有什么问题？尤其是……理论抽象，必然导致悖论」| 直接开出 dev-08 的 Q0/H0-Z0 线与 A-0028（模式 P 先于靶标）|
| ↓ 分叉 | `_tree.json`：parent_doc=10，cutoff end_ordinal_exclusive=4120 | archive-01a0fb73 → dev-08（主干）|

> dev-08 的前 1161 行导出（其 `THREAD` 的 `0001`/`0002` `anchor_window` [2,1162]）就是 archive-01a0fb73 的 #0003–#0010 内容，
> 归属判定见 `dev-08/THREAD.md` 附录 A.1。祖先线的判词逐字登记在 D3 账本的 A-0001–A-0037 一带（首现列写 `dev-08:L…`）。

## 9. 共同前段那 190 条 `open` 资产：层粒度答案

`CROSS-FEED.md` 判 `open` 的 230 条里，190 条属 dev-08 共同前段。它们在库内的答案是**层粒度**的：
CG-006 对共同前段只按层名／层区间登记（`八线分叉后复盘.md` §0、`Targets与Profile.md` §2.0），没有资产级落点。
按 CG-006 的层区间归组如下（2026-10-10 实测分档）：

| 轮次区间 | CG-006 层名登记（逐字）| 该区间的 `open` 资产 | 怎么查单条 |
|---|---|---|---|
| `L1–1161`（前缀区；内容＝archive-01a0fb73 #0003–#0010）| `Targets §2.0`「R00 #2–#3：在菲尔兹奖工作中选靶」「R01 #3–#10（KC-000056–058）：靶是基础理论；不必找菲尔兹入口；『ZFC 到底有什么问题？』」| 20 条（A-0004…A-0174 一带）| §8 祖先线表给轮次；资产见 `CROSS-FEED.md` §3.5「开放候选」/§3.2「方法」|
| `#0007–#0055` | `Targets §2.0`「#7–#55 模式 P 的三把刀与子代理盲测」（#7 授权 Terra/Max、#9、#10、#12–#17 建立 P2/P3 与三刀体系、#18–#24 锻打、#28 锻刀即发现、#30 动态 DAG、#48–#50 P-FORGE-SOP）| **133 条**（主要落在 0040/0041/0048/0052 等锻打与校准轮）| `CROSS-FEED.md` §3 按 A-ID → 首现列给 round → `qa/dev-08/00NN.md` 读该轮 |
| `#0056–#0073` | `八线分叉后复盘.md` §0「#56–#73 锻刀与发现 Q 是同一件事（#58【原话】）」；终点【自述】`TOOL_ONLY_DRIFT`、`ZFC_Q_NOT_LOCATED`（#72–#73）| **37 条** | 同上 |

**一句话答案**：这 190 条里没有任何一条被 CG-006 单条接走；它们的集体归宿是「锻刀期方法与来源弹药」，
其中方法族（P-DAG／校准／盲测／Battle）在 `Targets` 方向 Ⅰ 被判 ○/⊘ 并已单独记为 `cold`（`CROSS-FEED.md` §3），
剩下的就是 `open`。若要压低 `open` 数，需要 CG-006 侧补资产级索引（把 `GUI查阅索引.md` §1 的「位置」列细化到 A-ID），
或授权把 `~/.codex/archived_sessions/` 的 raw rollout 纳入输入层以补不可见轮（ledger PRE-4 已列为 UNKNOWN，未结）。

## 10. 截面声明：本库与当前研究状态怎么比对

本库登记的是**语料截面**：八份 GUI 导出（2026-10-04/05）＋`audit/GUI-ASSET-RECOVERY/`（2026-10-07）＋
CG-006 三份理解层文件与终局报告（2026-10-08）。**它不是当前研究状态的真值**。

| 问题 | 真值 owner | 怎么比对（命令／路径）|
|---|---|---|
| 当前研究状态、队列、开放问题 | `.codex/research/hott/STATE.json` ＋ `MEMORY.md`（分片 `MEMORY/001`–`003`）| 命令见下方代码块 |
| 形式化主张的当前地位 | `HoTT/CLAIM_EVIDENCE_MATRIX.md`（1995 行，本机在）| §6 的 C 编号索引直接给行号；矩阵的状态列逐字为 `KERNEL_ACCEPTED_WITH_SCOPE`／`FORMAL_CHECKED_WITH_SCOPE`／`MACHINE_PROVED_LOCAL_UNCOMMITTED` 一类 |
| CG-006 的实时进度 | `.claude/goals/CG-006-zfc-complete-formalization/{STATE.json,LOG.md,工作台.md}` | 该包自述「现状以 `形式化追踪/` 为准」|
| 某判词今天还成立吗 | 底层 proof／run 收据＋claim matrix | 本库只记「该判词在某线某轮被自述/被机器接受」的身份与范围，不记它今天是否仍是最新结论（R7）|

> 因此「本库登记的判词跟 MEMORY/STATE 还对得上吗」这个问题，本库答不了、也不该答：它需要用上表命令现取现比。

```bash
# 取 STATE 的 hot 字段（项目 AGENTS.md T1 档给定的命令，2026-10-10 可用）
python3 -c "import json;s=json.load(open('.codex/research/hott/STATE.json'));print(json.dumps({k:s[k] for k in ('current_core','active','latest_session','unresolved','revision')},ensure_ascii=False,indent=1))"
```

> 本库能答的是「这个判词是在哪条线哪一轮、以什么身份、在什么范围内说的」。

## 11. 相对链接校验表（G6）

**基准**：以各文件自身所在目录（`wflow-lineage/lineage/`）为解析基准。

**机验命令与结果**（2026-10-10 本机实跑，修订后复跑一次）：

```text
对 KB-INDEX.md / ROUTE-GRAPH.md / EVOLUTION.md / CROSS-FEED.md 四个文件，
提取 markdown 行内链接 ](...) 与反引号中的仓库路径，剔除 glob/模板（含 * { } < > … 的），
逐个 os.path.exists 解析：
  v1（2026-10-10 初版核验）：检查 73 条，解析成功 68 条，未解析 5 条
     （3 个 glob/目录占位符；2 条「本工作区不存在」的引文）
  v2（同日修订后复跑，本文件为修订版）：检查 76 条，解析成功 71 条，未解析 5 条
     未解析 5 条全部是已在 §7.3 显式登记的「本工作区不存在、origin/dev-09 上存在」的
     2 个路径（KB-INDEX 与 CROSS-FEED 各提 2 次，共 4 条）加 1 个目录占位符 `lineage/`；
     这 2 个路径在 origin/dev-09 上已实测可解析（§7.2 的 git ls-tree），因此不构成断链。
     glob 模板（含 * { } < > …）按规则剔除，不计入 76 条。
```

| 类别 | 条数 | 状态 |
|---|---|---|
| `lineage/` 内部四个综合文件互链 | 12（文件级）| 全部解析成功 |
| `lineage/<线>/THREAD.md`、`DISCOVERIES.tsv` | 16 | 全部解析成功 |
| 工作树内其它路径（`audit/GUI-ASSET-RECOVERY/…`、`.claude/goals/CG-006-…/…`、`dev-docs/…`、`sources/prompts/…`、`HoTT/CLAIM_EVIDENCE_MATRIX.md`、`.codex/…`）| 主要部分 | 存在的均解析成功 |
| `origin/dev-0X:<path>` 形式的 ref 限定路径 | 99 个不同 (ref,路径) 对 | **99/99 解析成功**（§7.2 实测；v1 时 N9 未复跑，v2 已补跑）|
| `HoTT/formal/external-cctt-r4/`、`HoTT/formal/external-foundation-incompleteness/` | 2 | 本工作区不存在，`origin/dev-09` 上存在（§7.3 实测）|
| glob/占位符（`dev-0{1,2,3,4,6,7,8,9} - *.md`、`lineage/*/DISCOVERIES.tsv`、`lineage/`）| 3 | 非可解析链接，已剔除 |

## 12. 完成门禁状态（按方案 §5，G1–G8；N10 未跑，此处登记 N9 侧可自证的部分）

| 门 | 要求 | N9 侧状态（2026-10-10）| 谁终审 |
|---|---|---|---|
| G1 覆盖 | 8 线 THREAD 齐备；每线自有轮 100% | ✅ 齐备；轮覆盖由各线 agent 自报并经 Master 机验：dev-08 127/127、dev-03 26/26、dev-02 13/13、dev-04 15/15、dev-01 21/21、dev-09 16/16、dev-06 13/13、dev-07 8/8 | N10 |
| G2 双锚 | TSV 每行 R1 满足 | 各线 agent 自报＋Master 跑 `check_lineage.py`（PRE-7 修复、PRE-15 修订后 PASS）| N10 |
| G3 判词保真 | 抽 30 个 `verdict_token` 逐字比对 | **N9 已自跑一次（v2 新增）**：种子 `20261010`、限定 token 式判词（形如 `KERNEL_ACCEPTED_WITH_SCOPE`／`ACTUAL_Z0_NOT_LOCATED`，共 124 个候选）→ **30/30 命中**；同口径全量 **124/124 逐字命中本线导出原文**。这不替代 N10 用自己新种子的独立复跑 | N10 |
| G4 不丢 | 619 条逐条有归宿＋一句理由 | ✅ `CROSS-FEED.md` §3 共 619 行、A-ID 唯一 619/619、归宿枚举合法 619/619 | N10 逐条核语义 |
| G5 传播图闭合 | carried 有落点，撞号区降级 parked | ✅ `ROUTE-GRAPH.md` §6；撞号区按 §5 G5 预登记降级（`CROSS-FEED.md` §2.1）；另 N9 实跑 99 个 ref 限定路径 99/99 可解析（§7.2）| N10 |
| G6 链接 | KB-INDEX 全部相对链接解析成功 | ◐→✅ 见 §11：v2 复跑 71/76，余 5 条为 §7.3 已登记的存在性说明（4 条）与目录占位符（1 条）| N10 |
| G7 口径一致 | R-4（块坐标 round＋裁决#3 总数分列）| ✅ 四个综合文件只用块坐标作逐轮身份，裁决 #3 只以「N／M」分列出现；术语误导已在 §2.2 第 3 条说明 | N10 |
| G8 零未申报未知 | ledger 无 OPEN 的 CONFLICT/UNKNOWN 未结 | ◐ ledger 仍有 OPEN 条目（PRE-8/9/10/11/12/14）；两说并陈见 `CROSS-FEED.md` §2.2 与 `ROUTE-GRAPH.md` §7，其余需 Master 结清或转写 | Master/N10 |

## 13. 已知缺口与未决（按方案 R9，不算任何 agent 失职）

| # | 缺口 | 影响 | 库内能否自答 |
|---|---|---|---|
| N-1 | dev-08 第 0127 轮在 A 层 GUI 导出无原文（导出止于 0126）| 该轮只能以 QA 轮号锚定，判词只能引 QA 文档 `qa/dev-08/0127.md` | 能（2 跳）|
| N-2 | 9 个不可见用户轮（8 个 rollout 的 `user_turns_not_visible`）| 任何 agent 都无法覆盖 | 不能；须扩输入层（ledger PRE-4）|
| N-3 | goal 续跑块逐字嵌入用户早先提问 | 可能把判词归错轮次 | 能（各线 THREAD「已知陷阱」已逐条登记）|
| N-4 | 裁决 #3 逐轮身份需 raw rollout（超出冻结五层）| 只能并列引用总数 | 能（§2.1/§2.2 已说明口径与命名）|
| N-5 | `check_lineage.py` 曾有两处缺陷（G1 `UnboundLocalError`；G3_full 误报字面量；G2 误报 round 写 `-`）| 已由 Master 修复/修订（PRE-7、PRE-15）| 能（ledger）|
| N-6 | 共同前段 190 条无资产级下游落点 | `CROSS-FEED.md` 判 `open` | 能到层粒度（§9）|
| N-7 | 撞号区 C-359~C-365／C-369／C-370 起 | 合并前必须重新编号；本库按 parked 登记 | 能到「属于哪一组」（§6）|
| N-8 | `type` 枚举缺「证明/判词/门规格/开放候选」项 | 机器证明行记 `type=发现`，身份由 claim 的【证明】前缀承载 | 能（`dev-01/THREAD.md` 第 11 行列约定＋§3.3）|
| N-9 | 本库不含当前研究状态 | 「是否仍然有效」须现取现比 | 能（§10 给出真值 owner 与命令）|

## 14. 上游与下游参照（只读，不在本 workflow 产物内）

### 14.1 输入层（冻结；A–E 五层）

| 类别 | 路径 |
|---|---|
| 八份 GUI 导出 | `git-worktree对话录/dev-0{1,2,3,4,6,7,8,9} - *.md`（SHA-256 见 `audit/GUI-ASSET-RECOVERY/manifest.json`）|
| QA 问答树（八线＋两条祖先线）| `audit/GUI-SYNTH-REDO/qa/<线>/`：每轮 `NNNN.md`、源 rollout 坐标 `_index.jsonl`、分叉 `_branch.json`；全局 `_tree.json`、`_manifest.json` |
| 资产审计 | `audit/GUI-ASSET-RECOVERY/`：`D3-资产登记v2-20261007.md`、`assets-ledger.md`、`manifest.json`、`coverage.json`、`notes/`、`D3-FILECHANGE-INDEX.md`、`D3-FILECHANGE-TIMELINE.tsv` |
| 认知闭包 | `认知闭包/GUI-ASSET-RECOVERY-001.md`（§8 裁决 #3 轮数口径）|
| 范围投影 | `wflow-lineage/scope.json`（每线 `docs[]` 锚点）、`wflow-lineage/context/`、`wflow-lineage/tools/`（`build_scope.py`、`check_lineage.py`）|

### 14.2 下游理解层（CG-006）

| 路径 | 作用 |
|---|---|
| `.claude/goals/CG-006-zfc-complete-formalization/GUI查阅索引.md` | 25 行主题表＋分叉后原话表；本库 `carried` 判定的主要落点来源 |
| `.claude/goals/CG-006-zfc-complete-formalization/Targets与Profile.md` | 五方向与 44 个要点的完成对照；线头列 |
| `.claude/goals/CG-006-zfc-complete-formalization/八线分叉后复盘.md` | 逐线【可吸收】清单与新风险 §9.5（K4 撞号）|
| `.claude/goals/CG-006-zfc-complete-formalization/{GOAL.md,LOG.md,STATE.json,工作台.md}` | CG-006 自身状态 |
| `docs/ZFC时间维度观察力不完备-哥德尔式Q终局报告-20261008.md` | 终局报告；§6「这一次不是侧移」回应 dev-01 #0013 |
| `.claude/goals/CG-006-zfc-complete-formalization/tools/{gui_find.py,gui_backtrace.py}` | 检索工具（§1 给出可执行命令）|

## 15. 维护规则

- 本文件是 `wflow-lineage/lineage/` 四产物的总入口；四产物内容变化时**必须同步** §4/§5 的规模数字与 §11 校验表（数字一律实测，不手写估计）。
- **不得**在本目录内建立第二份当前真值：研究状态的真值在 `.codex/research/hott/STATE.json` 与 `MEMORY.md`，形式化主张的真值在 `HoTT/CLAIM_EVIDENCE_MATRIX.md`，CG-006 的理解层在 `.claude/goals/CG-006-zfc-complete-formalization/`（见 §10）。
- 新线或新轮进入输入层时，先跑 `python3 -B wflow-lineage/tools/build_scope.py` 重建 `scope.json`，再按 §1 路由表补卡片与边。
- 发现冲突不改判：两说并陈写入 `CROSS-FEED.md` §2.2 或 `ROUTE-GRAPH.md` §7，并交 Master 登记 `CONFLICT` 到 `wflow-lineage/ledger.jsonl`。
- 本文件的修订只由综合 agent（N9）或 Master 做；每次修订在文件头「修订记录」加一行。

---

## 附：本目录文件清单与四产物速查

```text
wflow-lineage/lineage/
├── KB-INDEX.md            ← 本文件（总入口；含编号词汇表、C 编号索引、ref 解析指南）
├── ROUTE-GRAPH.md         ← 跨线传播图（63 节点／48 边；§2 节点表含每层判词逐字）
├── EVOLUTION.md           ← 五概念跨线演变（54 步，每步 round＋导出行号）
├── CROSS-FEED.md          ← D3 619 条资产逐条归宿（§2.1 撞号区、§2.2 两说并陈）
├── dev-01/  THREAD.md  DISCOVERIES.tsv    （21 轮／10 层／53 行）
├── dev-02/  THREAD.md  DISCOVERIES.tsv    （13 轮／8 层／129 行）
├── dev-03/  THREAD.md  DISCOVERIES.tsv    （26 轮／7 层／108 行）
├── dev-04/  THREAD.md  DISCOVERIES.tsv    （15 轮／6 层／114 行）
├── dev-06/  THREAD.md  DISCOVERIES.tsv    （13 轮／8 层／55 行）
├── dev-07/  THREAD.md  DISCOVERIES.tsv    （8 轮／6 层／64 行）
├── dev-08/  THREAD.md  DISCOVERIES.tsv    （127 轮／9 层／154 行）
└── dev-09/  THREAD.md  DISCOVERIES.tsv    （16 轮／9 层／50 行）
```

**四条最常用路径（30 秒版）**

1. 「某轮在干什么」→ §4 卡片 → `dev-0X/THREAD.md`（尾→分叉读）。
2. 「某判词怎么说、何时说」→ §4 → `dev-0X/DISCOVERIES.tsv` 的 `verdict_token` 列。
3. 「某资产现在何处」→ 有 A-ID 查 `CROSS-FEED.md` §3；有 C 编号查本文件 §6。
4. 「某实物在哪个提交上」→ 本文件 §7。

