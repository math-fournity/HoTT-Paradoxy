# 从"统观"到编码线：技术报告（供外部独立审计，2026-09-13）

> **报告性质**：`CURRENT_WORK_PACKAGE_REPORT / AUDIT_INPUT`。本文是一次性成文的审计输入（不是长期 owner 文档、
> 不是 append-only 台账、不新增数学 claim、不改变任何既有判词）。它把"从统观开始"这一段时间线
> （revision 101 → 118）的**方法、结论、机器证据、边界与已知弱点**整理成可逐条反驳的形式。
>
> **给审计者的最短路径**：先读 §0 摘要 → §10 已知弱点 → §11 审计问题清单 → §12 复现命令。
> 本文所有事实性主张都给出文件路径、claim ID、run ID 或 Git 提交；凡是没有这三类锚点的句子都应视为叙述而非证据。
>
> **不升级声明**：本报告不把 `DOCUMENTED`、`PAPER_ONLY`、`VERIFIED_WITH_SCOPE` 与 `MACHINE_PROVED_LOCAL_UNCOMMITTED`
> 互相冒充；ERCF-3 本体保持 `GATED`；门 A／门 B 状态不变；报告中不含任何"HoTT 已被证明有内部矛盾"的主张。

---

## 0. 一页摘要

**起点**：用户的目标不是"再找一个 Gödel 式口号"，而是问：HoTT（及其现实观）为了理论的经济性**悬置/否定了哪些现实因子**，
以及这些悬置是否会在某个真实任务上变成"非现实"（现象与现实不相容）。此前另一位 AI（Astra-1/Astra-2）在同一 repo
做过两段工作，用户认为它们没有做到。

**四个阶段、一条转向、两扇门、一条编码链**：

| 阶段 | 做了什么 | 判词 / 状态 |
|---|---|---|
| 轨迹审计（rev101） | 用 canonical session trajectory 工具回放 Astra-1/Astra-2，识别"为什么没做到" | 登记为历史与方法诊断（`DOCUMENTED`） |
| 统观立账（rev102） | 把"先找题再证明"改为"**先立账、再找题**"：C11 理论经济账本（11 行 + 六字段 + 四坐标 + 补偿动作三分） | `A-THEORY-ECONOMY-LEDGER-001`（`DOCUMENTED`） |
| 账本检验（rev103–104） | P1 时序线、P2/P3 判别格应用、18 包回溯检验、三语料粗域接口扫描 | P1 `P1_BOUNDED_NEGATIVE_PAYMENT_DEVICE_AVAILABLE`；P2/P3 `P2/P3_PREDICTION_HOLDS_NO_CONSUMER`；扫描 `COARSE_CONSUMER_SCAN_BOUNDED_NEGATIVE_WITH_TRIAGE_QUEUE` |
| 外部评审（rev105–106） | 吸收独立 AI 对 C11 的评审（5 主条 + 5 细节全部成立），C11 原位修订为 v2，corrective 重绑哈希 | `A-C11-REVIEW-ABSORPTION-001`；C11 v2 |
| triage 与自主构造（rev107–109） | 词汇 triage 判负并关闭；自主构造三轮：候选 #1 退化、不敏感+义务为空集、身份轴与表达轴判负 | `TRIAGE_LINE_CLOSED_PRECISION_LIMIT_REACHED`、`DEGENERATION_TEST_FAILED_KNOWN_PACKAGE`、`INVARIANT_OBSTRUCTION_EMPTY_BY_CONSTRUCTION`、两轴判负 |
| 搜索空间收口（rev109） | 收口为**门 A**（任务在 HoTT 中不可形式化，先需可对象化规格）与**门 B**（同层自我担保，ERCF-3/W51-3，`GATED` 缺消费者） | 收口命题标 `PAPER_ONLY`、可反驳 |
| 编码线 T3（rev110–118） | ERCF-3 前置工作中**自足**的部分：八个 claim-bearing package（C-157–C-183） | 全部 `MACHINE_PROVED_LOCAL_UNCOMMITTED` |

**关键数字（本报告撰写时 rev118；登记后 revision 见文末附记）**：冻结证明包 17 个（90 claims）+ 追加包 **9** 个（**34** claims）；
六个 canonical verifier 全 PASS；`plan --profile governance` 总量 930,146 B；工作树干净（除设计上不提交的 `dev-notes/`）；
**未 push、未打新 tag**。

**最重要的诚实边界**：编码线解决的是"**编码/解码/替换/引用**"这一层的前置义务；证明谓词 `P` 的表示性、反射与对角不动点
**都没有做**，而且按 repo 既有判定，没有门 B 的真实消费者时它们只会落入 `GENERIC_BOUNDARY_NOT_HOTT_SPECIFIC`（通用 Gödel 机制，
不是 HoTT 特有的非现实性）。

---

## 1. 任务背景与研究问题

### 1.1 用户的问题意识（常驻第四件）

用户的核心文本层是四件套（`核心认知.md` → `方向追踪.md` → `全景视野.md` → `从抽象到悖论——HoTT研究的核心问题意识与思想展开.md`），
其中第四件是 AI 阐释层、不是用户原文权威。用户的原始要求可压缩为三点（详见 `理解章节/A1-Z铁律.md`、`理解章节/A0-总目标.md`）：

1. 找到 HoTT（或任何被考察的理论）在**现实中不可完成、却被理论当作已完成**的情形（方向 B），或反向（方向 A）；
2. 不接受"理论内部矛盾"作为默认结论：HoTT 是**设计出来防御**悖论的（截断、商、ua、消去器义务）；
3. 要求**统观**：不是再采样一个熟悉题型，而是从理论为经济性做了哪些"否定现实"的决策出发，定位可能的非现实位置。

### 1.2 既有判词阶梯与 ERCF-3 的前置表

- 判词阶梯（`理解章节/C3`、`理解章节/C5`、`audit/paradox-failure-ledger-20260913.md`）：
  `DEFENSE_WORKS` → `REPRESENTATION_BOUNDARY` → `NATURAL_USAGE_MISMATCH` → `INTERNAL_INCONSISTENCY`。
  当前所有结论最高只到第二类；`NATURAL_USAGE_MISMATCH` 从未达到。
- ERCF-3（"自反真理验证回环"）：`理解章节/C8-ERCF-3前置评估与最小代理任务-20260912.md` 把它分解为 P1–P8 前置条件与 T1–T5 代理任务。
  结论：**ERCF-3 保持 `GATED`，不启动 diagonal 本体**；唯一升级路径是 P8（真实 natural consumer），N1–N10 四层审计均未找到。
  本报告的 T3 部分就是该表中的 T3 线（最小 Gödel 句/无健全完备总认证器）在**机械可做部分**上的推进。

---

## 2. 起点：为什么从"统观"开始（Astra-1/Astra-2 的失败形状）

**证据**：`audit/astra-1-astra-2会话轨迹审计-20260913.md`（方法：`repo-cognitive-closure` + `repo-agent-session-trajectory`；
轨迹经 canonical `/Users/aurolafly/codex/tools/session_trajectory.py` 读取；只使用公开可见 user/assistant 消息与工具结果）。

报告中由**文档 + 直接证据**共同支持的四条方法原因：

1. **目标被收窄成可形式化的小问题**：宽的问题意识（理论如何改变现实前提）被换成熟悉题型（保存/擦除信息、时标归属、不可恢复性）。
   两处收窄点被 Astra-1 自己的阅读定位到：`理解章节/C10-N11-A方向候选生成-20260912.md:20` 把"关键 HoTT 规则不可被普通类型论替代"
   设为必填门槛，而用户 KC-000015 只要求"在 HoTT 中有具体表现"；`理解章节/C5-十机证明后的悖论距离与自然消费者审计-20260912.md:56`
   与失败台账把 E6 写成唯一决定性缺口，候选生成据此转向历史主张抽样。
2. **工作单元颗粒度过小，产生与推进幅度不相称的进度感**：例 `HoTT/formal/ercf3-t3/TermIdentityFinal.agda:38` 把共享判定联合递归留在注释里，
   新增声明只是 `remainingStep : Set` / `remainingStep = Nat`；T3 从 S067 到 S080 共 13 个"脉冲"都停在同一恒等式的边界上。
3. **逐 KC 回评的执行证据缺口**：`.codex/research/hott/sessions/S-RES-20260913-067…085` 中 19 个 session 缺 `CORE_COGNITION_AUDIT.md`，
   与既有 `A-KC-AUDIT-GAP-001` 一致；这不证明那些 AI 没读核心认知，但使"本轮是否服务航向"缺少可查证据。
4. **并行写者导致后续工作整体移出 repo**：此后 Astra-1 的候选/实例/交接写在 `/Volumes/D/HoTT独立答复/`，使用独立收据格式——
   并发安全得到保护，但使工作只能事后吸收进当前真值。

**工程侧（可复核的一部分）**：Astra-1 第 7 轮确有可复核机器工作（主证明 exit 0、精确负数校准 exit 42、异目录重放一致），
但它证明的是**自建有限模型内部**的时标边界，不是 HoTT 自身的非现实性；其外部 9 个 run 不等于本 repo 的
`MATH_PROOF_BEFORE_DELIVERY_V1` 收据。

**不得升格的部分**：不能把 Astra-1/Astra-2 的自我诊断升格为"HoTT 已被充分搜索、所以没有问题"或反之"HoTT 必有 bug"；
`gpt-6-astra` 的"内在智能性"不可由轨迹量测；未复核 Astra-1 关于历史 WebGPT/LocalGPT 的每条引文。

**由此产生的转向**：不再从"熟悉题型"出发，而是先建立**理论经济账本**——理论为了经济性做了什么决策、悬置了哪些现实因子、
补偿操作是什么、在什么任务形状下这些被悬置的因子会"复活"——再由账本生成任务。

---

## 3. 统观方法：C11 理论经济账本（v2）

**主文档**：`理解章节/C11-HoTT理论经济账本与悖论位置判别-20260913.md`（178 行，v2）。
**登记记录**：`A-THEORY-ECONOMY-LEDGER-001`（`DOCUMENTED`），session `S-RES-20260913-102-THEORY-ECONOMY-LEDGER/`。

### 3.1 六字段与四坐标

账本每行必须写清六个字段：**行类型 / 经济决策 / 被悬置（或被加入）的因子 / 补偿操作 / 复活条件（任务形状）/ 现有判词**。
四个必须**分别记账**的坐标：① 层（对象层 vs 元层）；② 是否换理论/加规则（如 2LTT、QIIT、内部模型）；
③ 表示 vs 规则 vs 输入的改变；④ 阶段（同一阶段的因子不能被后一阶段的补偿"带回来"）。

### 3.2 补偿动作三分（评审 D-3／V3）

每一行的补偿动作必须逐例写成三类之一，否则"表示更细"会掩盖"换了任务"：
**恢复**（原任务输入不变、把因子取回）／**预先保留**（把因子提前存进输入）／**新增**（加入新的结构或规则）。

### 3.3 账本 11 行（v2 重排；含 2b/6a/6b 三个补行）

| # | 经济决策（要点） | 被悬置/加入的因子 | 现有判词锚点 |
|---|---|---|---|
| 1 | 命题截断 `∥A∥` 只保留存在（**加入**"命题"层） | 见证身份、代表元 | C-67–C-70；C-134–C-141；C-142–C-148 |
| 2 | 集合商：等价类当元素（**不**等于丢掉路径与构造史） | 代表元 | C-71–C-76；C-84–C-88；C-77–C-91 |
| 2b | univalence/SIP：等价结构即相等结构 | 载体与呈现的身份；签名外观察量 | C-100–C-105；C-124–C-128；C-129–C-133 |
| 3 | HIT：消去原理随构造不同 | 依具体 HIT | C-154/C-155 |
| 4 | 判断相等 | 判断的构造路径（不承诺校验器成本） | N10 应用层审计 |
| 5 | 计算规则/归一化 | 具体归约步骤与资源消耗 | C-96–C-99（表示边界） |
| 6a | 归纳消去 + 语言内总性 | "尚未落定/此刻不可用" | C-106–C-109；C-118–C-123 |
| 6b | 显式阶段流 + 忘却翻译 | 阶段区分 | C-92–C-95 |
| 7 | 命题无关 | 证明的构造史 | 与 #1 同族（C-70） |
| 8 | 宇宙 + 自描述 | 对象层/元层分界 | C-59–C-66；S053 对角核；S054 路线 (a)；ERCF-3 `GATED` |
| 9 | 无全局选择（不可导出，非公理） | 现实中"选定一个代表"这一动作 | C-142–C-148；C-141；C-84；外部库 C-05 |

### 3.4 检查坐标（**不是**分类、**不是** Gate）

v2 明确把 v1 的"判别格"**降级为检查坐标**：判别格（支付装置可用 / 昂贵 / 不存在）只描述候选的处境，
**不能决定它是否有资格被研究**；三格中任何一格都可进入机器化讨论，区别只在补偿操作是否写清。
总账不变量（"可形式化且合理的任务若不可完成，必依赖某个被悬置因子"）被明确标为**待检验猜想**，不是判据。

### 3.5 尚未完成的部分（v2 自述，原文保留）

- 复活条件列**尚未逐行完成**（表中是概括形状，不是逐行任务生成）；
- 时间/运动结构、量词与完成顺序**尚未落进九行**；
- B 方向（把"尚未完成"当作"已经取得"）在表中只有间接位置，**尚未独立成行**。

---

## 4. 账本的第一次检验（第一工作包，rev103–104）

### 4.1 P1（时序线）

**文档**：`audit/p1-时序线候选与支付装置审计-20260913.md`（含 D1–D6 支付装置口径重写）。
**判词**：**`P1_BOUNDED_NEGATIVE_PAYMENT_DEVICE_AVAILABLE`**——在"阶段可用性 + 截止期"这类**已被对象化**的任务形状上，
理论侧的支付装置（加索引、细化表示、显式 cost/step、partial/guarded/clock 扩展）是**可用**的，因此这些形状停在
`REPRESENTATION_BOUNDARY`，**不构成悖论候选**。

### 4.2 P2/P3 + 粗域接口搜索

**文档**：`audit/p2-p3与粗域接口搜索-20260913.md`；**扫描数据**：`audit/coarse-consumer-scan-20260913.json`。

- **P2（同层不可用）**：`P2_PREDICTION_HOLDS_NO_CONSUMER`。自指担保的支付装置是"层级上升"，
  而升层等于离开被担保的理论；但 checklist 第 1 项（真实粗域接口）在已审计集合内不存在（P8 缺失、ERCF-3 `GATED`）。
- **P3（交叉线）**：`P3_PREDICTION_HOLDS_NO_CONSUMER`。形式要件在本 repo 最齐（`MP-NOCANONICAL-001` 机器证明"无统一选点"，
  `MP-ONLINE-CAUSALITY-001` 给阶段边界），合并二者只需一个**真实接口**。
- **粗域接口扫描**（首轮 v1 规则）：三语料共 4181 文件，239 条"粗域 + 箭头"命中（Cubical 70 / agda-unimath 161 / 本 repo formal 8），
  其中 93 条带义务 token、146 条进入 triage 队列；固定 10 例人工抽样全部落入三类无害形态（截断类型构造子、余域本身截断、
  本 repo 自己的不可能性定理）。判 `COARSE_CONSUMER_SCAN_BOUNDED_NEGATIVE_WITH_TRIAGE_QUEUE`。
  **注意**（审计要点）：现存扫描 JSON 是**收紧后的 v2 规则**重跑结果（7 个 token，86 命中 / 43 带义务 token），
  与 P2/P3 报告引用的 v1 数字（239/93/146）**不是同一规则**；该差异只在 triage 报告里一句话说明，JSON 内未标 rule-version。

### 4.3 18 包回溯检验（机器记账）

**判词**：`A-LEDGER-RETRODICTION-CHECK-001`（`VERIFIED_WITH_SCOPE`）；
**脚本**：`scripts/audit/verify_ledger_retrodiction.py`；**数据**：`audit/ledger-retrodiction-check-20260913.json`。

结果：`packages_checked = 18`，`device_available = 17`，`device_absent = ["MP-NOCANONICAL-001"]`，`errors = 0`（PASS）。
脚本自带的**语义边界**必须一并阅读：它只验证机械记账（矩阵行、claim 行、最终 run、源码哈希、声明的装置格），
**不验证账本行的语义内容**，也不创建或升级任何数学 claim。

**这一点是审计重点**：回溯检验说明"账本与既有 18 个机器包的归类一致"，**不说明**账本本身正确。

---

## 5. triage 关闭与自主构造三轮（rev107–109）

### 5.1 线 A：triage 判负并关闭

**文档**：`audit/triage批次与自主构造第一轮-20260913.md`；判词 **`TRIAGE_LINE_CLOSED_PRECISION_LIMIT_REACHED`**。

- v1 规则（含 `Trunc`/`trunc-` 等前缀）→ 146 条队列，批次 1（前 20）**20/20 假阳性**（`Truncated-Type` 记录名等）；
- 收紧为"算子位置"（v2，43 条队列）→ 批次 2（前 20）**20/20 假阳性**（`mere-emb`/`mere-eq`/`is-mere-path-cosplit` 等谓词名）；
- 两批 40 条分类：类型/记录构造子 24 条、谓词或关系名 16 条、**真正的"从粗类型取值"消费者 0 条**。

结论：假阳性来源是**命名约定**而非词表不全，继续调词表是"打地鼠"；43 条队列保留为附录（不再逐条读）。

### 5.2 自主构造三轮

| 轮次 | 文档 | 判词 | 内容要点 |
|---|---|---|---|
| 第 1 轮 | `audit/triage批次与自主构造第一轮-20260913.md` | `DEGENERATION_TEST_FAILED_KNOWN_PACKAGE` | 候选 #1（"加入义务"读法）逐步退化到已知包 C-142–C-148，不构成新机制 |
| 第 2 轮 | `audit/自主构造第二轮-识别不敏感与相干义务-20260913.md` | `INVARIANT_OBSTRUCTION_EMPTY_BY_CONSTRUCTION` | 结构论证：消去器义务 ≡ "对关系同余" ≡ "对识别不敏感" ⇒ "不敏感 + 不可满足义务"是**空集** |
| 第 3 轮 | `audit/自主构造第三轮-表达与身份两轴-20260913.md` | 两轴均判负 | 身份轴（识别改变对象身份）退化为**解释冲突**；表达轴三个候选**没有 HoTT 特有表达缺口** |

---

## 6. 搜索空间收口：两扇门（rev109）

`audit/自主构造第三轮-表达与身份两轴-20260913.md` §3 给出收口表（关键行）：

| 形状 | 状态 | 依据 |
|---|---|---|
| 支付装置可用 | 关闭（表示边界） | P1；C-71–C-141 |
| 支付装置存在但昂贵（升层/换理论） | 未关闭，但等于门 B | P2；ERCF-3 `GATED` |
| 支付装置不存在（无统一选点） | 关闭（缺真实消费者/呈现依赖） | P3；C-142–C-148 |
| 词汇级接口 triage | 关闭（精度极限） | S107 线 A |
| 不敏感任务 + 身份原则义务 | 关闭（空集） | S108 |
| 识别改变对象身份 | 关闭（退化为解释冲突） | S109 §1 |
| 表达/覆盖缺口 | 关闭（无 HoTT 特有实例） | S109 §2 |
| **门 A：任务在 HoTT 中不可形式化** | **开放** | KC-000031/000035；coverage `NOT_PROVEN` |
| **门 B：同一层内的自我担保** | **开放（gated）** | C8/S053 P8；W51-3；ERCF-3 |

**收口命题（`PAPER_ONLY`，可反驳）**：在 HoTT 的商/截断/ua/消去器语义下，一个**可形式化**的任务若"合理 + 合法推演 + 不可完成"，
必须依赖某个被理论识别或悬置的因子；而消去器的义务恰是"该依赖良定义"的判据。因此可形式化的候选会被正确拒绝或被细化表示修复——
**现实相对悖论只能出现在理论上不可形式化之处，或自我担保的层级要求之处。**

两条门的最小可验动作（登记，不预先承诺结果）：

1. **门 A**：先给出一个**可对象化的现实量规格**（"阶段可用性 + 截止期"已可对象化，因此不能作候选），再检查 HoTT 能否形成该对象；
2. **门 B**：构造或找到一个**自我担保消费者**，按 C8 的 P1–P8 检查（W51-3 = E6 的自指版本）。

两条门都需要**新的真实输入**；该结论明确写了"本轮不再投入更多同型枚举"。

---

## 7. 外部评审的吸收与 C11 v2（rev105–106）

**文档**：`audit/c11评审吸收与独立核验-20260913.md`（60 行）；**导入原件**：`audit/imports/c11-review-20260913/`（含 `IMPORT.json`）；
**评审核验记录**：`A-C11-REVIEW-ABSORPTION-001`（`DOCUMENTED`）。

处理方式（可审计的行为模式）：外部评审被**逐字保全导入**，然后**逐项独立核验**，而不是直接采纳或直接拒绝。
核验结论：**5 个主条 + 5 个细节全部成立**（一条附范围限定）。由此 C11 原位修订为 **v2**：

1. 判别格**降级**为检查坐标（§3.4 已述）；
2. 账本改为六字段；补偿动作三分；四坐标分离；
3. 补时间结构与 B 方向；回溯结论降级为"归类一致性"；
4. 新增**退化测试**（删去阶段/自证要求后若不退化为已知问题，才算新增机制）——这是此后自主构造轮次的准入判据。

**corrective 重绑**：文档原位重写会连带改动三类哈希（文档 record pin、校验脚本契约、派生 manifest），
因此 S105/S106 是两个独立 checkpoint：修订 + 重新绑定 16 条 record；随后六个 verifier 全 PASS。
**审计要点**：v2 的修订记录在 §9 修订记录中；核对脚本 `scripts/audit/verify_understanding_merge.py` 等是否与 v2 的行标签一致
（S106 正是靠 verifier 发现 v2 误删了 univalence 行才做了 corrective）。

---

## 8. 第二线 T3：编码链（C-157–C-183，rev110–118）

### 8.1 立链背景与预期判词

T3 是 C8 §9 的代理任务之一（最小 Gödel 句与"无健全完备总认证器"）。C8 的**事前预测**必须一并阅读：
T2（S054）显示语法层可由**纯 Agda builtins** 承载（无 cubical 特征），因此 T3 的机械部分预计为
**`GENERIC_BOUNDARY_NOT_HOTT_SPECIFIC`**——除非出现 HoTT 特有规则的**不可替代**使用，或 P8 成立。
本报告 §8 的全部机器结果都落在这个预测之内：它们推进的是**前置义务**，不是 HoTT 特有的非现实性结论。

### 8.2 八个 claim-bearing package

| Package ID | Claims | 源码 | canonical run | 判词（verdict） |
|---|---|---|---|---|
| `MP-ERCF3-T3-JOINT-001` | C-157–C-159 | `HoTT/formal/ercf3-t3/JointRecursion.agda` | `20260913-MP-ERCF3-T3-JOINT-001-02` | `ERCF3_T3_SHARED_DECISION_JOINT_RECURSION` |
| `MP-ERCF3-T3-DECODING-001` | C-160–C-162 | `…/DecodingFence.agda` | `20260913-MP-ERCF3-T3-DECODING-001-01` | `ERCF3_T3_DECODABILITY_FENCE` |
| `MP-ERCF3-T3-REPAIR-SPEC-001` | C-163–C-165 | `…/CodingRepair.agda` | `20260913-MP-ERCF3-T3-REPAIR-SPEC-001-01` | `ERCF3_T3_REPAIR_SPECIFICATION` |
| `MP-ERCF3-T3-ARITH-TAGS-001` | C-166–C-168 | `…/ArithmeticTags.agda` | `20260913-MP-ERCF3-T3-ARITH-TAGS-001-01` | `ERCF3_T3_ARITHMETIC_TAGS_FRAGMENT` |
| `MP-ERCF3-T3-BIT-CODING-001` | C-169–C-172 | `…/BitCoding.agda` | `20260913-MP-ERCF3-T3-BIT-CODING-001-01` | `ERCF3_T3_BIT_SUBSTRATE` |
| `MP-ERCF3-T3-STREAMING-PARSER-001` | C-173–C-176 | `…/StreamingParser.agda` | `20260913-MP-ERCF3-T3-STREAMING-PARSER-001-01` | `ERCF3_T3_REPAIRED_NAT_CODING` |
| `MP-ERCF3-T3-FORMULA-CODING-001` | C-177–C-180 | `…/FormulaCoding.agda` | `20260913-MP-ERCF3-T3-FORMULA-CODING-001-01` | `ERCF3_T3_REPAIRED_FORMULA_CODING` |
| `MP-ERCF3-T3-REPAIRED-SYNTAX-001` | C-181–C-183 | `…/RepairedSyntax.agda` | `20260913-MP-ERCF3-T3-REPAIRED-SYNTAX-001-01` | `ERCF3_T3_REPAIRED_SUBSTITUTION_AND_QUOTATION` |

包内细节（精确命题、源码标识、禁止外推）见 `HoTT/formal/ercf3-t3/README.md` 的 §1–§8 与
`HoTT/CLAIM_EVIDENCE_MATRIX.md` 文末的四节追加登记（C-157–159 / C-160–176 / C-177–180 / C-181–183）。

### 8.3 逐段叙述

**（a）C-157–C-159：共享判定联合递归。** 问题是"码级替换"与"语法级替换"必须一致：`substFixT k i t ≡ codeT (substT k i t)`。
这一族在 S067–S080 共 13 个脉冲都停在同一边界；本包给出三条精确命题：显式共享判定版本一致（C-157）、
**原始逐出现判定的项层恒等式**（C-158）、以及**修正后的公式层恒等式**（C-159）。
副产品（必须单独指出）：公式层证明失败暴露了历史脉冲 `CodeStoreFixF.agda` 在 `all` 的**影子分支**把 `codeF φ` 误写成
`codeF (all m φ)`（双重编码）；本包在**新模块**给出修正函数 `substFixFc` 并机器检查，**历史脉冲文件逐字节未改**。

**（b）C-160–C-162：可解码性围栏（否定结论）。** `codeT (var 2) ≡ codeT (num 0)` 而 `var 2 ≢ num 0` ⇒
不存在单射解码器（C-160）；同一碰撞提升到公式层（C-161）；数字片段有正控制（C-162）。
这条否定的意义：`ObjectSyntax` 明文把 "Gödel coding with decodability/injectivity" 列为 T3 义务，而**当前编码不满足它**，
所以任何在旧编码上做 P 表示性/对角化的路线都必须先修编码。

**（c）C-163–C-165：修复规格。** 通用引理：任意类型 `A` 上，若 `c : Tm → A` 有往返解码器则 `c` 单射（C-164）；
结构化树编码给出正控制（C-163）；旧 Nat 编码**不存在解码器**（C-165：`Σ (dec : Nat → Tm), (∀ t → dec (codeT t) ≡ t)` 蕴含 `Empty`）。
由此"修复义务"被固定为：**给出 Nat 值编码 + 全解码器 + 像上往返**。

**（d）C-166–C-168：算术半第一片。** 偶/奇标签算术（`double` 单射、`double n ≢ odd m`，C-166）；
var/num 片段 Nat 值编码 `codeAtom`（`2n` / `2n+1`）**单射**（C-167，链条中第一个 Nat 值单射编码）；
编码**非满射**（`1` 无原像）⇒ 任何全解码器必须有**缺省分支**（C-168）。

**（e）C-169–C-172：位级底座。** 最低位/折半数字算术 `parity`/`half`/`twice`（C-169）；
捆绑编码 `codeBits`（`[] ↦ 1`，`b∷bs ↦ pack b …`）与抽取 `unbits` 的两侧引理（C-170）与**已知长度**往返
`unbits (LEN bs) (codeBits bs) ≡ bs`（C-171）；**码支配自身长度** `suc (LEN bs) ≤ codeBits bs`（C-172）——
这条界是后面"燃料取自码本身"的机器依据。

**（f）C-173–C-176：符号层 + 流式解析器 + Tm 修复编码。** 自定界一元索引层（C-173）；
符号层 `bits`（`var`/`num` 两位标签 + 一元索引；应用结点一位标签）与**燃料精确**的流式解析器 `run`（C-174）；
长度对账、界即和分解、`unbits` 多余燃料分解（C-175）；
`codeT' = codeBits ∘ bits` 带**全**解码器 `dec`（含缺省分支）与往返 `dec (codeT' t) ≡ t`，故由 C-164 **单射**（C-176）。

> **工程要点（对本报告的完整性重要）**：`(t +t u)` 的自然解析是"先解析 t、再解析 u"，第二次调用要用第一次**返回**的燃料——
> 这在 Agda 里既不是结构递归也不被终止检查接受。解法是把待解析的右子做成**显式框架栈**，
> 让一步迭代恰消费一位、消耗一个燃料单位，于是结构递归成立而往返定理仍是**精确**形式（剩余燃料即 `k`）。

**（g）C-177–C-180：公式层（Fml）。** 对角化真正引用的是公式，因此同一义务再上一层。本包**复用**项层解析器：
`tmFrom bs = SP.run (LEN bs) bs (SP.startSub SP.ε)`（C-178，燃料=剩余位数）；
公式符号层 `bitsF`/`STEPS` 与**迭代数精确**的流式 `run`（C-177）；长度界 `STEPS φ ≤ LEN (bitsF φ)`（C-179）；
`codeF' = codeBits ∘ bitsF` 带全解码器 `decF` 与往返，故单射（C-180）。

> **工程要点**：`run` 的第一个参数是 `Mode`（永远是构造子）而不是位串——否则 `eqRight` 那一步的位串是卡住的
> `bits u ++ rest`，Agda 无法选择子句，连"定义上相等"的等式都证不出来；此外 `tmFrom … ≡ res …` 是**命题**等式，
> 直接 `refl` 必然失败，必须写成独立引理并显式搬运燃料/位串。

**（h）C-181–C-183：替换一致与引用。** 有了解码器之后，码级替换定义为"解码—替换—编码"：
`substCodeT k n (codeT' t) ≡ codeT' (substT k n t)`（C-181）、公式层同型（C-182）；
引用 `⌜φ⌝' = num (codeF' φ)` **单射**、对角实例 `diagonalize' φ = substF (codeF' φ) 0 φ` 是替换实例且
`codeF' (diagonalize' φ) ≡ substCodeF (codeF' φ) 0 (codeF' φ)`（C-183）。

### 8.4 修复链条：否定 → 规格 → 存在性修复

```
C-160/C-161  旧编码有碰撞（否定）
C-165        旧编码不存在解码器（否定的精确形式）
C-163/C-164  修复规格：往返 ⇒ 单射（通用引理）
C-166..C-172 算术半：标签不相交 → 位级底座 + 燃料界
C-173..C-176 Tm 修复编码 codeT' + 全解码器 dec + 往返  ⇒ 单射
C-177..C-180 Fml 修复编码 codeF' + 全解码器 decF + 往返 ⇒ 单射
C-181..C-183 码级替换一致（推论） + 引用单射 + 对角实例形状
```

### 8.5 这一段的诚实边界（必须与结论同读）

1. **不是 HoTT 特有的**：以上全部只用 Agda builtins，不含 univalence/Path/HIT/truncation 的实质使用；
   按 C8 的事前预测，该线的机械部分应记 `GENERIC_BOUNDARY_NOT_HOTT_SPECIFIC`，本报告不改变这一判定。
2. **表示性未做**：`substCodeT`/`substCodeF` **经由解码器定义**（解码—替换—编码）。"一致"是精确的，
   但**不主张对象理论（`⊢_` 系统）能表示该替换或引用函数**——那才是表示性义务。
3. **编码是存在性修复，不是高效编码**：公式层的索引位用一元表示，码值增长很快；本线只主张可解码性与单射性。
4. **未做**：证明谓词 `P` 的表示性、反射、对角不动点；ERCF-3 本体保持 `GATED`。
5. **局部修正 vs 历史文件**：C-159 只在新模块给出修正；历史脉冲文件（`ObjectSyntax`…`TermIdentityFinal`）逐字节未改
   （可交叉核对：`ObjectSyntax.agda` 在 9 个 run 的 manifest 中哈希恒为 `88cb7b85eaa6`；
   `DiagonalCore.agda` 9 个 run 恒为 `3c97a4a354c5`；`CodeStoreFix.agda` / `MutualInduction2.agda` / `DecisionParam.agda`
   各自在 2 个 run 中哈希唯一不变）。

---

## 9. 证据与治理基建（审计者需要知道的机制）

### 9.1 机器证明交付门禁（`MATH_PROOF_BEFORE_DELIVERY_V1`）

本 repo 的 AGENTS 规定：任何数学命题作为**结论**交付前，必须（1）固定 claim/proof ID 与精确命题；（2）源码进 `HoTT/formal/`；
（3）用能验证该命题真实语义的 kernel 实际运行；（4）每次运行的 `RUN.json`/`stdout.txt`/`stderr.txt`/`environment.txt`/
`source-manifest.json` 存进 `HoTT/verification/runs/<run-id>/`；（5）在 `HoTT/CLAIM_EVIDENCE_MATRIX.md` 建唯一索引行；
（6）只有 1–5 全过才可用 `MACHINE_PROVED`/`FORMAL_CHECKED_WITH_SCOPE` 等措辞，并另标 `LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED`。

### 9.2 索引、冻结与 append-only 矩阵

- 每个 run 有 `index-row-manifest.json`：冻结 proof 行与各 claim 行的**精确行哈希**（后续只追加新节，旧行不得改写）。
- `HoTT/verification/PROOF_VERSION_CLOSURE.json`：17 个冻结包（在 commit `d3dfb0e` 上做版本闭环）+ `later_packages` 追加登记
  （当前 9 条，含源码/工具链/run 的 Git-tracked 检查与 `exit_code = 0`、`index_status = INDEXED_IN_CLAIM_EVIDENCE_MATRIX` 校验）。
- 当前计数：90（冻结）+ 34（追加）claims。

### 9.3 canonical checkpoint 与六个 verifier

本 repo 的**唯一**写入路径是 `python3 -B .codex/tools/cognition_runtime.py checkpoint --snapshot <plan快照> --payload <json> --apply`。
它写出 `SESSION.md`/`RUNS.json`/`CORE_COGNITION_AUDIT.md` 与 `checkpoints/<session>/transaction.json`、before/after 副本、`result.json`；
只有 `result.json.status = CHECKPOINT_COMMITTED` 才算应用成功。**每个**修订后必须全过六个 verifier：

| verifier | 覆盖 |
|---|---|
| `verify_governance_shards.py` | 索引/分片结构（当前 176 个 index；soft-target notice 非阻塞） |
| `verify_three_way_cognition.py` | 三件套/四件套固定顺序、KC 数（36）、方向/成果计数 |
| `verify_understanding_merge.py` | 理解章节与历史来源合并对账（不声称数学等价） |
| `verify_fresh_three_way.py` | 新鲜上下文按固定顺序的覆盖与负例（含 wrong_snapshot 等 4 个负例） |
| `verify_ledger_retrodiction.py` | C11 账本与 18 个机器包的机械记账对账 |
| `verify_proof_version_closure.py` | 冻结包/追加包/矩阵 append-only/state closure record |

### 9.4 状态与提交（本地，未 push）

- 撰写时 `revision 118`，`latest_session = S-RES-20260913-118-ERCF3-T3-REPAIRED-SYNTAX`（登记本报告后的 revision 见文末附记）；
  `plan --profile governance` 总量 930,146 B；工作树干净（除设计上不提交的 `dev-notes/`）。
- 本线提交（旧→新）：`8dd03d5`+`b933dfd`(rev101) → `7eca45c`(rev102) → `1136ba5`(rev103) → `6f98ac7`(rev104) →
  `7774596`(rev105/106) → `28d26c1`(rev107) → `8f0317c`(rev108) → `17e9f76`(rev109) → `b4432ac`(rev110) →
  `7f7a2ef`+`8de12a5`(rev111) → `4edb83f`+`3bef6ba`(rev112) → `00fa3ac`+`bf00bff`(rev113) → `00187d6`(rev114) →
  `8f9267b`+`27e79dd`(rev115) → `9644a5e`+`0270c01`(rev116) → `0002c9d`+`a4d201a`(rev117) → `9f822b7`+`fc79094`(rev118)。
  两条哈希并列处，后者是"刷新 fresh-three-way 收据"或"索引 / 作用域说明"的治理提交。
- **未 push、未打新 tag**；`governance-v4.0.0` 是既有 tag，本段工作不改动它。

---

## 10. 已知弱点与自查（建议审计者优先攻击）

1. **C11 的语义未被机器验证**：18 包回溯只验证记账；账本行（"被悬置因子""补偿操作"）是**人工语义判断**，
   没有独立 AI 或形式化对账。审计应重点攻击 11 行的归类与"复活条件"的充分性。
2. **收口命题是 `PAPER_ONLY`**："可形式化 ⇒ 会被拒绝或被修复"是结构论证，**不是定理**；它可被一个反例推翻，
   而反例只需满足：可形式化 + 合理 + 不可完成 + 不依赖被悬置因子。
3. **门 A/门 B 都依赖外部输入**：本线在此停住不是"做完了"，而是"现有材料无法再自动产生候选"。
4. **triage 关闭是精度判断，不是不存在性证明**：40/40 假阳性只覆盖两批 20+20 条；43 条队列未读。
5. **扫描 JSON 与报告数字的规则版本不一致**（v1: 239/93/146 vs 现存 JSON: v2 86/43）；JSON 内未标 rule-version。
6. **C11 v1 的"判别格"曾被当作准入门槛**：v2 已降级，但 P2/P3 报告正文仍保留"最优先"字样（同页有 v2 备注）。
7. **T3 的八个包都在 builtins-only 链上**：它们**不使用** HoTT 特有规则（无 univalence/Path/HIT），
   因此按 C8 预测应为 `GENERIC_BOUNDARY_NOT_HOTT_SPECIFIC`；任何把这批结果讲成"HoTT 悖论进展"的说法都是越级。
8. **`verify_formal_proof_run.py` 对这些包不适用**（会报 `AGDA_SAFE_CUBICAL_OPTIONS_REQUIRED`）：
   这是适用域限制，已在 `HoTT/formal/ercf3-t3/README.md` 与 runs README 注明；canonical 入口是 closure verifier。
   审计者若只看该脚本的输出，会误判失败。
9. **单射性结论依赖具体构造**：C-176/C-180 只声称这两个编码（及其解码器）的性质，不是"任何 Nat 值编码都不可能"。
10. **`⌜-injective'` 与 `DiagonalCore.⌜-injective` 名字相近但含义不同**：前者是引用映射单射，
    后者只是"沿码相等的替换同余"（`cong-here`）。命名相似是潜在误读点。
11. **K C 回评是 AI 自评**：每轮的 `CORE_COGNITION_AUDIT.md` 逐 KC 回评由当轮 AI 写，属"自证"性质，
    不是独立验证；历史 session（S067–S085）存在 19 个缺失回评的登记缺口（`A-KC-AUDIT-GAP-001`）。
12. **`TermIdentityFinal.agda` 无 claim 行、也不在任何 run manifest 中**：它属"脉冲证据"谱系；
    如果审计者要求"每个 formal 文件都有 run"，这条会失败——它是有意的历史遗留。
13. **`JointRecursion.agda` 有两个不同哈希**（`-01` 失败尝试含 `--safe` pragma；`-02` 是 canonical）；
    审计者若只取 `-01` 会看到 `CoInfectiveImport` 失败。
14. **编码膨胀未量化**：公式层用一元索引，`codeF'` 的码值增长未给出界；若未来要做 P 表示性，
    这会直接影响"码值是否可被对象算术承载"。

---

## 11. 给外部审计的问题清单（逐条可答）

**A. 方法与账本（C11）**

1. C11 的 11 行是否覆盖了 HoTT 为经济性所做的主要决策？有没有**明显缺失**的行（例如：宇宙多义性、η/β 规则选择、
   guard 条件、`funext` 与 `ua` 的相互作用、`Prop` 与 `Set` 的分层）？
2. 六字段是否真的阻止了"先有结论再找证据"？请检查每一行的"被悬置因子"是否**先于**判词给出，还是事后回填。
3. 补偿动作三分（恢复/预先保留/新增）是否可机械判定？能否给出一个**被误分类**的例子？
4. "四坐标必须分别记账"是否足以防止"跨阶段把因子带回来"？请攻击第 4 坐标（阶段）。
5. 18 包回溯的 `device_available/absent` 赋值是否**事后**？有哪个包的归类可能被推翻？

**B. 否定结论与收口**

6. 收口命题（§6）是否可反驳？请尝试给出一个**可形式化 + 合理 + 不可完成 + 不依赖被悬置因子**的反例。
7. triage 关闭（40/40 假阳性）是否过早？请从 43 条队列里挑 1–2 条判定是否存在被漏掉的真实消费者。
8. `INVARIANT_OBSTRUCTION_EMPTY_BY_CONSTRUCTION`（S108）的结构论证是否成立？它的前提（"消去器义务 ≡ 对识别不敏感"）是否过强？

**C. 编码线（T3）**

9. C-165 的"无解码器"是否被 C-176/C-180 **正确**取代（即：是否真的回答了同一个问题，而不是换了目标）？
10. `tmFrom` 复用项层解析器（C-178）隐藏了哪些假设？燃料取"剩余位数"是否在公式层总成立？
11. `run` 的**迭代数**语义（`STEPS`）与**位数**（`LEN`）不同：`STEPS ≤ LEN` 的界是否足够？
    有没有反例使命题在边界情形（空公式、深嵌套 `all`）失效？
12. C-181/C-182 的"一致"是否**循环**？`substCodeT` 经 `dec` 定义，而 `dec` 由 C-176 给出——
    这是否构成"用要证的东西证明自己"？（本报告的立场：不是循环，但确实**不构成表示性**。）
13. 八个包的 claim 是否有任何一条越级（把 `PAPER_ONLY`/`DOCUMENTED` 写成 `MACHINE_PROVED`）？
    请抽查 `HoTT/CLAIM_EVIDENCE_MATRIX.md` 的对应行与 run 的 `RUN.json`。
14. `index-row-manifest.json` 的行哈希冻结是否真的能防止"事后改行"？请尝试构造一次改写并观察 verifier 是否 fail closed。
15. `MACHINE_PROVED_LOCAL_UNCOMMITTED` 与"跨机器可恢复"的区分是否被严格维持？（本 repo 要求未提交时必须另标 `LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED`。）

**D. 治理与证据**

16. 六个 verifier 的**盲点**在哪？尤其：`verify_fresh_three_way.py` 明确声明
    `model_behavior: NOT_RUN_NO_FRESH_MODEL_INVOCATION_AUTHORIZED`——它验证的是文件与覆盖，不是模型行为。
17. 逐 KC 回评（`CORE_COGNITION_AUDIT.md`）是 AI 自评；请判断它是否**只是形式合规**，
    并指出至少一条"看起来对齐、实际未服务航向"的评估。
18. 本报告的 14 条已知弱点中，哪一条会**实质削弱**主结论？请排序并说明理由。

---

## 12. 复现与核验命令（在 repo 根执行）

```bash
# 0. 身份与状态
git -C . log --oneline -3
python3 -B .codex/tools/cognition_runtime.py plan --profile governance | head -40

# 1. 六个 canonical verifier（应全 PASS）
for v in verify_governance_shards verify_three_way_cognition verify_understanding_merge \
         verify_fresh_three_way verify_ledger_retrodiction verify_proof_version_closure; do
  python3 -B scripts/audit/$v.py | tail -2
done

# 2. 重放某一个 T3 包（Agda 2.8.0 + 固定工具链；run 收据比对 stdout/stderr 哈希）
cat HoTT/verification/runs/20260913-MP-ERCF3-T3-REPAIRED-SYNTAX-001-01/RUN.json
python3 -B scripts/audit/capture_agda_proof_run.py \
  --run-id <新 run-id> --proof-id MP-ERCF3-T3-REPAIRED-SYNTAX-001 --claim-id C-181 \
  --source HoTT/formal/ercf3-t3/RepairedSyntax.agda \
  --toolchain HoTT/formal/ercf3-t3/TOOLCHAIN.json \
  --manifest-file HoTT/formal/ercf3-t3/{ObjectSyntax,DiagonalCore,CodingRepair,BitCoding,StreamingParser,FormulaCoding}.agda \
  --scope 'replay' --non-goal 'no new claim'

# 3. 账本回溯检验（机械记账）
python3 -B scripts/audit/verify_ledger_retrodiction.py | tail -3

# 4. 版本闭环（17 冻结 + 9 追加；矩阵 append-only）
python3 -B scripts/audit/verify_proof_version_closure.py | tail -3

# 5. 若要在无网络环境手工重编译（builtins-only 链，**不要**加 --safe）
/Volumes/D/HoTT-toolchain-cache/agda-v2.8.0-macos-arm64/agda --no-libraries --ignore-interfaces \
  -i HoTT/formal/ercf3-t3 HoTT/formal/ercf3-t3/RepairedSyntax.agda
```

---

## 13. 术语表

| 术语 | 含义 |
|---|---|
| 统观 | 从"理论为经济性做了哪些决策、悬置了哪些现实因子"出发做全局分析，而不是在熟悉题型附近采样 |
| 支付装置（payment device） | 把被理论悬置/识别的现实因子在**任务需要的同一阶段、同一层**带回来的构造；分"可用/昂贵（升层）/不存在" |
| 补偿动作 | 让任务可完成的动作，必须逐例写成 恢复／预先保留／新增 |
| 门 A | 任务在 HoTT 中**不可形式化**（先需可对象化的现实量规格） |
| 门 B | 要求理论在**同一层内担保自身判断**（自指担保；W51-3 = E6） |
| ERCF-3 | "自反真理验证回环"候选；前置条件 P1–P8；**保持 `GATED`** |
| T3 | C8 代理任务之一（最小 Gödel 句/无健全完备总认证器）；本报告的编码线 |
| claim 等级 | `QUESTION`/`CONJECTURE`/`PAPER_ONLY`/`SOURCE_REPORTED_NOT_REPLAYED` → `MACHINE_PROVED_LOCAL_UNCOMMITTED` / `FORMAL_CHECKED_WITH_SCOPE` |
| 判词阶梯 | `DEFENSE_WORKS` → `REPRESENTATION_BOUNDARY` → `NATURAL_USAGE_MISMATCH` → `INTERNAL_INCONSISTENCY`（当前最高只到第二类） |

---

## 附录 A：claim ↔ 包 ↔ run ↔ 源码（C-157–C-183）

| Claims | Package | 源码 | canonical run |
|---|---|---|---|
| C-157–C-159 | `MP-ERCF3-T3-JOINT-001` | `HoTT/formal/ercf3-t3/JointRecursion.agda` | `HoTT/verification/runs/20260913-MP-ERCF3-T3-JOINT-001-02/` |
| C-160–C-162 | `MP-ERCF3-T3-DECODING-001` | `…/DecodingFence.agda` | `…/20260913-MP-ERCF3-T3-DECODING-001-01/` |
| C-163–C-165 | `MP-ERCF3-T3-REPAIR-SPEC-001` | `…/CodingRepair.agda` | `…/20260913-MP-ERCF3-T3-REPAIR-SPEC-001-01/` |
| C-166–C-168 | `MP-ERCF3-T3-ARITH-TAGS-001` | `…/ArithmeticTags.agda` | `…/20260913-MP-ERCF3-T3-ARITH-TAGS-001-01/` |
| C-169–C-172 | `MP-ERCF3-T3-BIT-CODING-001` | `…/BitCoding.agda` | `…/20260913-MP-ERCF3-T3-BIT-CODING-001-01/` |
| C-173–C-176 | `MP-ERCF3-T3-STREAMING-PARSER-001` | `…/StreamingParser.agda` | `…/20260913-MP-ERCF3-T3-STREAMING-PARSER-001-01/` |
| C-177–C-180 | `MP-ERCF3-T3-FORMULA-CODING-001` | `…/FormulaCoding.agda` | `…/20260913-MP-ERCF3-T3-FORMULA-CODING-001-01/` |
| C-181–C-183 | `MP-ERCF3-T3-REPAIRED-SYNTAX-001` | `…/RepairedSyntax.agda` | `…/20260913-MP-ERCF3-T3-REPAIRED-SYNTAX-001-01/` |

**冻结 17 包（供对照，不属本段新增）**：`MP-ERCF-001`(C-59…C-66)、`MP-ERCF-TRUNC-001`(C-67–C-70)、
`MP-RACE-TIMEOUT-001`(C-71–C-76)、`MP-CONTEXTUAL-EQUIV-001`(C-77–C-83)、`MP-QUOTIENT-MONAD-001`(C-84–C-88)、
`MP-CONTEXT-CHARACTERIZATION-001`(C-89–C-91)、`MP-GUARD-ERASURE-001`(C-92–C-95)、`MP-COST-FACTORIZATION-001`(C-96–C-99)、
`MP-PATH-CERTIFICATE-001`(C-100–C-105)、`MP-ONLINE-CAUSALITY-001`(C-106–C-109)、`MP-TRANSITION-LIFT-001`(C-110–C-117)、
`MP-PARTIAL-DECISION-001`(C-118–C-123)、`MP-SIP-REPRESENTATION-001`(C-124–C-128)、`MP-CAUCHY-MODULUS-001`(C-129–C-133)、
`MP-TRUNC-NORECOVERY-001`(C-134–C-141)、`MP-NOCANONICAL-001`(C-142–C-148)、`MP-UNIMATH-NOSECTION-REPLAY-001`(C-05)。
另有追加包 `MP-VERIFICATION-EVENT-001`(C-149–C-156，外部独立来源在项目内重放)。

---

## 附录 B：文件地图（哪些是当前真值，哪些是历史/证据）

| 类别 | 路径 | 说明 |
|---|---|---|
| 宪法/路由 | `AGENTS.md`（全局 + 项目） | always-on 规则；项目规范在 `~/.codex/AGENTS.md` 的项目段 |
| 常驻认知 | `核心认知.md`（36 KC，generation-4）、`方向追踪.md`、`全景视野.md`、`从抽象到悖论——…md`（第四件，AI 阐释层） | 固定顺序全文加载 |
| 当前态 | `MEMORY.md`（+ `MEMORY/` 分片）、`.codex/research/hott/STATE.json`、`FRONTIER.md`/`LESSONS.md`/`RESUME.md` | 当前方向、验证状态、顺序日志 |
| 稳定知识 | `理解章节/`（A/B/C 系列，含 C8 前置表、C11 账本 v2） | 历史认知闭包与当前候选 |
| 审计输入/结果 | `audit/`（本报告、Astra 审计、P1/P2P3、triage、自主构造三轮、评审吸收、失败台账、扫描 JSON、回溯检验 JSON） | dated artifacts，不自动成为规则 |
| 机器证明 | `HoTT/formal/ercf3-t3/*.agda`、`HoTT/verification/runs/**`、`HoTT/CLAIM_EVIDENCE_MATRIX.md`、`HoTT/verification/PROOF_VERSION_CLOSURE.json` | 唯一可升级为 `MACHINE_PROVED` 的地方 |
| 会话/事务 | `.codex/research/hott/sessions/<session-id>/`、`.codex/cognition/checkpoints/<session-id>/` | SESSION/RUNS/逐 KC 回评/事务收据 |
| 历史（不可改） | `HoTT/formal/ercf3-t3/ObjectSyntax.agda`、`DiagonalCore.agda`、`DiagonalLemma.agda`、`CodeStoreFix.agda`、`CodeStoreFixF.agda`、`MutualInduction2.agda`、`DecisionParam.agda`、`TermIdentityFinal.agda` | 早期脉冲谱系；新结论只进新模块 |
| 私有审计（不入库） | `private-audit/`、`~/.codex/sessions/` | 原始 trajectory；只读 |

---

---

## 附记：本报告自身的登记历史（审计者应把它当作治理机制的活样本）

本报告**撰写时**对应 revision 118；交给外部审计前，它自身经过了五次治理事务，其中**两次是同一个错误的重犯**，
且两次都**由 verifier 机械抓住**（这是审计者可以据此评估治理机制的地方）：

| Revision | Session | 做了什么 | 结果 |
|---|---|---|---|
| 119 | `S-GOV-20260913-119-AUDIT-REPORT-FOR-EXTERNAL-AUDIT` | 登记本报告（记录 `A-AUDIT-REPORT-TONGGUAN-001`，`DOCUMENTED`，哈希钉住）+ 顺序日志 | `verify_three_way_cognition` **FAIL**：`DIRECTION_STATE_REVISION_STALE`（只 bump 了 `STATE.revision`，没同步投影 index 的 `source_state_revision`） |
| 120 | `S-GOV-20260913-120-PROJECTION-REVISION-REPAIR` | corrective：同步投影 index 版本行 | 仍然 **FAIL**——该 corrective 把投影写成 `119` 却又把 `STATE.revision` bump 到 `120`，错误依旧 |
| 121 | `S-GOV-20260913-121-PROJECTION-REVISION-REPAIR-2` | corrective #2：把投影与 STATE 都对齐到 `121` | **六个 verifier 全 PASS**（`verify_fresh_three_way` 报 `revision 121`） |
| 122 | `S-GOV-20260913-122-AUDIT-REPORT-ADDENDUM-REPIN` | 给报告加本附记并重绑报告哈希 | 报告侧成功；但该事务**再次**只 bump `STATE.revision=122` 而没同步投影 ⇒ `verify_three_way_cognition` **FAIL**（同一个错误重犯） |
| 123 | `S-GOV-20260913-123-PROJECTION-REVISION-REPAIR-3` | corrective #3：投影与 STATE 同事务对齐到 `123`，并再次重绑报告哈希 | **六个 verifier 全 PASS** |

**这段历史对本报告的意义（请审计者据此评估治理机制，而不是跳过它）**：

1. 投影 index 的 `source_state_revision` 是**人工维护**的字段，容易与 `STATE.revision` 脱钩；S119 与 S122 两次犯了**同一个错**
   （只 bump STATE、不 bump 投影），两次都由 `verify_three_way_cognition` 的机械检查捕获（`DIRECTION_STATE_REVISION_STALE`），
   说明该 verifier 在这一点上是 fail-closed 的；但也说明这条链**在无 verifier 时并不可靠**。
2. 三次修正都以**新事务**进行（S105/S106 先例："修正走新 checkpoint，不改写已应用事务"），
   失败事务的 `result.json` 与 after 副本仍留在 `.codex/cognition/checkpoints/` 下可查——包括那次写错版本号的记录。
3. 本报告正文（§0–§13 与附录）在修订 119–123 中**内容未变**，只有版本号引用与本附记被更新；
   claim、判词、run、全部研究结论均未改动。报告哈希钉在 `A-AUDIT-REPORT-TONGGUAN-001.source_hashes`，
   最后一次由 revision 123 重新钉住。
4. **因此报告正文里的"rev118"必须与本节一起读**；当前状态请以 `STATE.json`、`PROOF_VERSION_CLOSURE.json`
   与六个 verifier 的最新输出为准。

---

*本报告由当前 repo 的 main agent 于 2026-09-13 依据 revision 118 的实际状态撰写（附记更新于 revision 123）；
如状态推进，请以 `STATE.json`、`PROOF_VERSION_CLOSURE.json` 与六个 verifier 的最新输出为准。*
