<!-- governance-shard:v2
logical_id: ATRIA-MACHINE-OVERVIEW-PLAN-REVISION
shard_id: 015
index: ../修订片.md
-->

# V2 片段设计与 delay→V2 的门槛判定规程

来源：SOP（hott-paradox-search-sop）穿越压缩边界后的方案复核 + 修订片 014 §2.3 门槛问题。
身份：方案修订（reflection=post-compaction-review + v2-gate-answer）。本片**不做 P3/P4 判定，
不产生数学结论**（F-011）。AI 全自动执行（修订片 009），本片全部进审计层。

## 1. 复核结论（穿越压缩边界后）

- 014 的结论（delay 片段 V1 族用尽；现象层 `separation_kind` 3 值饱和；发现侧唯一出口在
  V2 片段）经本复核**仍成立**：五族交付物、step-6 审计与 014 之后无新证据推翻它。
- **一处方案优化（本片实质内容）**：V2 首单元与 delay 族**不同形**。delay 族"声明任意新
  continuation map 即可用，无需改引擎"（010 §3 事实 1）；V2 首族**必须先完成片段扩展**
  （新 ground 值域/ops/`separation_kind` 取值 + Agda mirror 一致性），否则引擎能力缺口
  会被误记为"该族链不通"。014 §2.3 只问了"是否应由 delay 承担"，未区分这一层工程差异；
  本片补上。

## 2. 014 §2.3 门槛的判定规程（三条充分条件，可机械核对）

一个 omission shape **必须**由非 delay 片段承担，当且仅当以下任一成立：

| 条件 | 内容 | delay 片段为何承担不了 | 锚定前提 |
|---|---|---|---|
| **G-a 序/稠密** | 分离依赖"两个位置之间是否还有位置"这类**稠密可分**结构 | delay 值只有离散自然数索引 n，任意两值之间无中间结构；`later` 只能 +1 | PREMISE-D-01（区间/连接） |
| **G-b 存在≠可用（双坐标）** | 分离依赖"填充物存在"与"填充物已就位"分属**两个可独立变化的坐标** | delay 中 `ret(n,b)` 的存在即立即可用，二者不可分离观察 | PREMISE-D-04 / PREMISE-G-05（Kan 填充 / 可填充性当作构造可用） |
| **G-c 层级塔** | 分离依赖"第 k 层的见证不决定第 k+1 层"的**塔结构** | delay 无层级维度，所有结构都被坍缩到单一索引 | PREMISE-G-03 / PREMISE-E-04（高阶相等无限迭代 / 截断塔稠密） |

反之，若分离只需**单离散索引 + 有界观察窗**（race 截断 / deadline 窗口 / bind 索引累加），
仍由 delay 承担，014 §2.1–2.2 的 map 覆盖率与现象饱和披露照常适用。

**登记要求**：每个 V2 候选族必须在 SUPPLY_REGISTRATION 中显式标注命中 G-a/G-b/G-c 的哪一条
（可多条），并给出该 shape 在 delay 片段的**不可承担性机械论证**（对照上表"delay 为何"一列）。

## 3. V2 片段的最小设计（`L2-cofibration` 片段）

设计目标：把 G-a/G-b/G-c 变成**可枚举、可归约、可送原生核**的声明文法，安全性质
（分母可枚举、remainder=0、越界理由唯一）与 delay 片段一致。

### 3.1 值域（声明界，有限）

- 计算轴沿用 delay：`omega` / `ret(n, b)`（n ≤ `delay_index_max`，b : Bool）。
- **结构轴（新）**：每个值携带一个**面/层级坐标**：
  - `face`：一个**声明有限的 cofibration 面集** `FACES` 中的元素（对区间变量的
    连接 ∧/∨ 闭包取有限代表元；具体集合在实现时机械生成并登记大小，不预设"应该多大"）；
  - `level`：一个**声明有限的截断塔层级** `0..TOWER_MAX`（G-c）。
- **可用性态（新，G-b 的核心）**：`available` / `pending` / `absent`。
  理论侧"存在填充物"对应值存在；"已就位"对应 `available`。二者可**独立**被观察层查询。

### 3.2 ops（声明有限集合）

- 沿用：`race_left` / `race_right` / `bind` / `deadline`（语义不变，作用于计算轴）。
- **新增**：`fill(face)`（申请某面的填充物；返回值的可用性态按该面是否在**已供给面集**
  `SUPPLIED` 中变化）、`supply(face)`（把面加入 SUPPLIED，模仿"胎具已制造到位"）、
  `tower(level)`（把观察层抬到指定塔层）、`between(face_a, face_b)`（稠密性查询，G-a）。

### 3.3 分离语义与 `separation_kind` 的新取值

- `separates` 的定义不变（观察后不等即分离），但**观察层**可作用于结构轴，于是
  `separation_kind`（delay 片段 3 值已饱和）获得**新取值**：
  `availability_observation`（G-b）、`level_observation`（G-c）、`density_observation`（G-a）。
- **这就是 014 O-5 指出的现象新颖性出口**：新取值不是 delay 棋盘上的新落子，而是
  新的**观察维度**。是否真的产出新现象，仍须按 012 片三问在首族 REPORT 中判定，本片不预判。

### 3.4 ground 表示的候选与验收方式（诚实留白）

ground 值的具体编码（面如何表示、`SUPPLIED` 如何建模）有至少两种可行表示：
(A) 显式有限枚举面 + 集合语义；(B) 自由 De Morgan 代数商的规范代表元。
本片**不替实现做决定**；判据是**阶段 1 验收**（§5）中的两条机械检查：
(i) Python ground 语义与 Agda mirror 在全部 ground 项上一致（逐项对照，不是抽样）；
(ii) 声明的 `FACES` / `SUPPLIED` / `TOWER_MAX` 有限性与 ops 封闭性自测全过。

## 4. 首族供给登记（SUPPLY-009 · V2-A）

```text
SUPPLY_REGISTRATION
  / id: SUPPLY-009 (V2-A)
  / strategy: S6 现实对齐（修订片 006 §2）+ S3 理论经济（被省略者）
  / kc_anchor: KC-000044 / KC-000045 / KC-000046（S6）；KC-000029 / KC-000030（S3）
  / premise_id: PREMISE-D-04 + PREMISE-G-05（双成员族，沿用 013 §2.1 的 Q4 纪律）
  / gate: G-b（存在≠可用，双坐标）——delay 不可承担性机械论证见 §2 表
  / human_supply: 冻结任务族 = "胎具存在但未就位"：一个面其填充物在理论侧存在
      （可填充性是 cofibration 的定义条件），但可用性态为 pending；观察层固定为
      可用性查询而非结果查询（S1 ASK 移位在 V2 中的具体形态）
  / program_role: 引擎在冻结的 V2 声明文法上枚举/归约，分母固定、remainder=0；
      不声称覆盖未声明的面或层级
  / kernel_role: 只有原生核（Cubical Agda + cubical 库）给 oracle verdict；
      Python 枚举/归约不得冒充结论（F-011 / 修订片 009）
  / confidence_disclosure: D-04/G-05 是本批置信度最低一对（可填充性是定义条件，
      首要风险是 AI 漏判现实不对应），前提判定保持 AI_ADJUDICATED_PENDING_EXTERNAL_AUDIT
```

**同族坍缩 Q4 预答（013 §2.1）**：D-04 与 G-05 在 V2 片段**预期不再共享同一机制
pattern——G-b 的双坐标正是为区分二者而引入的结构**。但预期不等于证明：Q4 仍须在首族
执行后按 013 §2.1 实答，若仍坍缩则照常登记 `PATTERN_REDUCED`。本片不预判结果。

## 5. V2 首单元的分阶段验收（本片新增，仅对 V2 片段生效）

- **阶段 1（片段扩展验收）**：ground 语义模块 + 自测 + Agda mirror 一致性（§3.4 两条）。
  判词 `FRAGMENT_EXTENDED_WITH_SCOPE`。**这是工程能力验收，不是数学结论，
  `registers_new_claim: false`**，不进 `HoTT/CLAIM_EVIDENCE_MATRIX.md`，
  也不计入 GEN-001 的族数。
- **阶段 2（首族链贯通）**：`GEN-001-V2-1`，沿用 003/011/012/013/014 的**全部**纪律
  （越界理由唯一、现象新颖性三问 + map 覆盖率与形状归类、同族坍缩 Q4、方向覆盖声明、
  现象饱和声明）。`separation_kind` 的新取值是否被实际用到，是阶段 2 现象新颖性判定的
  主证据之一。
- 两阶段必须**分开提交、分开登记**，不得把阶段 1 的工程验收冒充阶段 2 的链贯通。

## 6. 对现有条款的影响

| 条款 | 影响 |
|---|---|
| 014 §2.3（门槛） | 补 §2 的三条充分条件与不可承担性机械论证要求；不禁止继续加 delay 族 |
| 014 §2.1（map 覆盖率） | V2 片段的 map 空间结构不同（ops 集合变了），覆盖率分母须按 V2 声明界重算，不能沿用 49 |
| 003 片（GEN-001 验收单元） | V2 族增加阶段 1 前置；阶段 2 的判词与纪律不变 |
| 006 片（发现引擎） | S6/S3 的下一个具体执行单元 = SUPPLY-009；S6 的 `reality_skeleton`（P2 已登记：制造工装域）是本族的现实母域 |
| 010 §3（引擎能力事实） | 新增事实：V2 片段**必须**改引擎（与 delay 族相反）；symbolic renderer 封闭性对 V2 不适用，V2 走 L2 mirror 路线 |

## 7. 本片不声称

- 不声称 V2 片段一定能产出现象新颖的候选（沿用 014 §5）。
- 不声称 §3.4 的 ground 表示选型已定；阶段 1 验收才有权定。
- 不声称 SUPPLY-009 的双成员不会坍缩（§4 已明说 Q4 须实答）。
- 不声称 delay 片段的 31 个未用 map 不值得声明（沿用 014 §5）。
- 本片无数学结论（F-011）；`FRAGMENT_EXTENDED_WITH_SCOPE` 与 `GENERATOR_LINK_*` 一样是
  能力验收判词，不是数学判词。
