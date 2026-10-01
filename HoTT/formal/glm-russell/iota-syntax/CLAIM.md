# GR-1 自指探针第一步：真实等式逐 refl 解释，非落定必须人工注入（集合性为开放义务）（GLM-R1-C02、C03 机器证明；C01 开放）

> 2026-09-26；GLM-5.3-Flash（ZCode 宿主），会话 S-GOV-20260926-GLM-WORKSPACE-01 的 GR-1 单元。依据 rulings 第 33/34 条：GLM 侧罗素线平行工作，goal 本地索引，不写共享矩阵。
> 起因：用户 2026-09-26 原话（`GLM-5.3-Flash/罗素线-平行工作索引.md` §7 第二批）确立"算符先行于存在性落定"模板；GR-1 问"理论自身的表述"是 U 式无层还是 hSet 式只升一层。
>
> - proof id：`MP-GLM-RUSSELL-IOTA-001`（`RealisticIotaSyntax.agda` + `ArtificialEquationControl.agda`）。
> - 负控制：`MP-GLM-RUSSELL-IOTA-NEG-001`（`WrongArtIsRefl.agda`，预期被内核拒绝）。
> - claim：`GLM-R1-C01`、`GLM-R1-C02`、`GLM-R1-C03`。
> - 工具链：Agda 2.8.0-3d04bac + cubical 0.9，`--safe --cubical --guardedness`，无公设（与 Opus 各包同一冻结工具链，`HoTT/formal/dedekind-omega-missile/TOOLCHAIN.json`）。
> - 索引：`GLM-5.3-Flash/罗素线-平行工作索引.md` §8（GOAL_LOCAL_INDEX_ONLY；共享矩阵行由 integrator/Opus 决定，GLM 不代写）。

## 公平性合同（本包凭什么算"真实等式"）

1. **对象片段**：一个只有布尔字面量、三支条件算子 `cond` 的语法；等式构造子只有 `cond (lit true) t s ≡ t` 与 `cond (lit false) t s ≡ s`——这是Bool 消去子的逐构造子计算规则（ι/β-ι），**每个类型论的每个消去子都有这一层的计算规则**，陈述与证明都不需要替换运算。它是对 `self-interpretation/REVISIONS.md` 收窄教训的直接回应：不夹带 swap 式"本意非平凡认同"的等式。
2. **真实等式的判据**：在标准语义下被 `refl` 解释（REVISIONS 对真实类型论等式的刻画）。本包把该刻画机器化：`val` 的两个 βι 子句**逐字是 `refl`**（GLM-R1-C02），并且这是一个定义性事实，不是证明出来的命题。
3. **人工等式的判据（对照）**：`art : boolTy ≡ boolTy` 把 `Bool` 的一个非平凡自等价（`not`）宣布为定义性认同——没有任何真实类型论有这样的计算规则，正是 C-67 的 swap 在本片段里的对应物。

## 命题与交付状态

- **GLM-R1-C02（真实等式是事实，机器证明）**：标准解释 `val : Tm → Bool` 把两条 ι 计算规则都送到 `refl`（定义性；`valReflT`/`valReflF` 见证，`ArtificialEquationControl` 的传递检查覆盖主模块）。
- **GLM-R1-C03（非落定必须人工注入，机器证明）**：同一片段加一条人工等式 `art` 后，`¬ isSet TmA`：若 `TmA` 是集合，`art ≡ refl`，则 `cong (cong f)` 给出 `ua flipNotEquiv ≡ refl`，与 `uaβ` + `true≢false` 矛盾。负控制 `WrongArtIsRefl` 断言 `art ≡ refl` 被内核拒绝（exit 42，`art i != boolTy`）。
- **GLM-R1-C01（isSet Tm，本批开放）**：归一化引理 `q : t ≡ lit (val t)` 的路径构造子子句要求形如 `PathP (λ i → betaT t s i ≡ lit (val t)) ((λ i → cond (q (lit true) i) t s) ∙ (betaT t s ∙ q t)) (q t)` 的边界相干方块（HIT 消去到路径类型的边界一致性问题）。cubical 库自身取得集合语法的方式是**添加** `trunc` 构造子（即 C-67 (b) 支），那是宣告而非证明集合性。阻塞点已注释在源码中；`squareLeft`（库 `compPath-filler'` 反区间）是已完成的部分构件。这是 GR-1 的后继义务。

## 这对 GR-1 意味着什么（解释，非机器证明）

- 【解释】机器可证的部分已经给出判别性对照：**真实等式**在标准解释下全部逐 `refl`（C02），**人工等式**一条就破坏集合性（C03）——C-67(a) 的"语法不是集合"确证来自 swap 式等式本身，不是自指的固有代价。
- 【解释】"理论自身的表述"是否完全落定（C01）本批未定（既未证 isSet 也未证 ¬isSet），但**不存在来自解释方向的非平凡路径见证**；U 式的全面上升（C-75 的机制，localGlobal + 各种高度的成员）在语法缩影里没有对应物——语法成员是有限树，没有无界高度。
- 【解释】因此自指格的罗素三条件（用户模板 C1/C2/C3）中，C3 在语法层**无证据支持且上界不明**；自指格保持其芝诺面（把集合语法的解释送进单价宇宙需要目标为集合，而宇宙不是集合——C-71 的执照拒绝）与 Q1 结构（实践用外部 elaborator）。罗素面归 U 线。
- 【解释】C01 的证明难度本身是个发现：为未截断 HIT 语法证明集合性需要把合流论证内化为高维相干——与"初始性之难"（Kraus 障碍的玩具尺度对应物）同族；库的做法（trunc 构造子）正是用户模板里"等式作为事实"的 (b) 支。
- 【解释】与 Opus 各包无重复：C-67 审的是标准解释两难；本包审的是真实/人工等式的机器判别与语法截断层级的证明义务。P25–P33（语法/反射语料审计）审外部语料，本包是独立玩具机器探针。

## 禁止外推

- **GLM-R1-C01（isSet Tm）未证明**：不得声称真实语法的缩影是集合、群胚或任何特定层级；本批对 C3 的否定性判断只到"无解释方向的见证 + 成员高度有界"。
- 片段是一阶的（消去子作用于构造子）；完整 β（高阶，需替换装置与 sig 律）未被触及。
- 不证明任何依赖语法的理论的任何性质；Kraus 障碍与 C-71 的执照拒绝是另一层。
- 不证明 HoTT 不一致；C03 只针对这一条人工等式的注入效果。

## 运行

- 主包：`HoTT/verification/runs/20260926-GLM-IOTA-SYNTAX-01`（两个 .agda 均须 exit 0）。
- 负控制：`HoTT/verification/runs/20260926-GLM-IOTA-SYNTAX-NEG-01`（预期非零退出，`art != refl` 类错误）。
