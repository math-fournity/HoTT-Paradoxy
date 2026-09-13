# N5 审计：派生开发的“可计算/可提取/可交付”自述

> 文档身份：`CURRENT AUDIT EVIDENCE / BOUNDED_DEFENSE (SCOPED)`
> 日期：2026-09-12
> 触发：N4 选定 N5；固定集合为四份一手派生开发与本地 Cubical v0.9 派生模块
> 结论：**固定集合内没有找到 `FOUND_CANDIDATE`。四份派生开发在自述中都显式写出了所需假设（countable choice、proposition extensionality、partiality monad、resource-bounded implementation、modus/modulus 等），没有把较弱资格写成较强交付。判定 `BOUNDED_DEFENSE`。**

## 0. 审计集合与方法

| 编号 | 来源 | 身份 | 本轮可核层级 |
|---|---|---|---|
| D1 | Altenkirch–Danielsson–Kraus, *Partiality, Revisited*（arXiv:1610.09254） | 全文抓取件 SHA-256 `188d3f71…`；纯文本 63,103 chars | 全文关键词 + §5 相关段落 |
| D2 | Chapman–Uustalu–Veltri, *Quotienting the delay monad by weak bisimilarity*（MSCS 29(1)） | Cambridge 页面 SHA-256 `f9f26569…` | 公开摘要级 |
| D3 | Møgelberg–Zwart, *What Monads Can and Cannot Do with a Few Extra Pages*（arXiv:2311.15919） | 摘要页 SHA-256 `8ddb3b9d…`；全文 HTML 不可得 | 公开摘要级 |
| D4 | Niu–Harper, *Cost-Aware Type Theory*（arXiv:2011.03660） | 全文抓取件 SHA-256 `9ee3f929…`；纯文本 225,602 chars | 全文关键词 + 摘要/讨论 |
| D5 | 本地 Cubical v0.9 派生模块 | tag commit `b150186d…`；tree SHA-256 `73ccfbaf…` | `Cubical/Papers`、`MagicTrick`、`Axiom.Choice` 消费者 |

审计问题：文本是否出现 “extract / compute / decide / serialize / normalize / run / implement / delivery” 一类承诺；该承诺依赖定理级资格还是执行级资格；接口是否显式携带所需假设；是否存在同一任务下把较弱资格当较强资格的调用链。

## 1. D1：partiality monad 的自述

### 1.1 摘要级陈述

D1 明确写出：

- 商 delay monad 的单子结构“without assuming (instances of) the axiom of countable choice”不可定义；作者用 QIIT 构造 partiality monad 从而**避免**该假设；
- “in the presence of countable choice, our partiality monad is equivalent to the delay monad quotiented by weak bisimilarity”；
- “we outline several applications”。

假设（choice 的有无、等价成立的条件）被显式写出；没有把 QIIT 构造宣称为无条件优于商表示。

### 1.2 §5.2 Functions from the Reals（`full-1610.09254.txt`，约 chars 52,314–55,554）

这是本轮最接近“派生开发自述升级”的段落，原文明确说：

- 对 Cauchy reals 的商 `ℝq`，“without further assumptions, any definable function (i.e. any closed term) of type `ℝq → 𝟐` is constant for reasons of continuity”；“In particular, we cannot define a function `isPositive` which checks whether a real number is positive.”；
- 但可以定义 “`isPositive : ℝq → 𝟐⊥`”，并且它 “is equal—but not judgmentally/definitionally equal—to `η(1)` if `r` is positive, `η(0)` if `r` is negative, and `⊥` if `r` is zero”；
- 对 HIIT 版本的 reals，“The strategy outlined above does not quite work … because … a comparison such as `f n · n < −2` is undecidable”，并引用 Gilbert 2017 用 partiality monad + semidecidability 解决。

作者没有把 `isPositive : ℝq → 𝟐⊥` 写成“可以判定正负”；他们明确区分了 partial decision 与 total decision，也明确区分了 propositional equality 与 judgmental equality。因此这里不存在隐藏的资格升级：自然函数的确存在，但它的类型就是 partial 的，消费者要得到 Bool 必须自己处理 `⊥`（或额外提供 modulus/decidability）。

### 1.3 §5.3 Operational Semantics（约 chars 55,554–56,700）

作者报告把 definitional interpreters、type soundness、compiler 与 compiler correctness “ported … to the partiality monad”，并注明细节在 accompanying source code。这里是实现级自述，但没有声称 partiality monad 提供超出其接口的**总**交付；编译正确性仍是相对于 partial 语义的定理。

### 1.4 D1 判定

`BOUNDED_DEFENSE`。没有 `FOUND_CANDIDATE`。最强的“可疑句”是 “we can define isPositive”，但原文紧接着限定：值只 propositionally equal 于 `η(1)`/`η(0)`，且总分类 `ℝq → 𝟐` 不可定义/为常值。

## 2. D2：商 delay monad 的假设

D2 摘要明确写出：

- setoid 路线下，“the delay datatype quotiented by weak bisimilarity is still a monad”；
- 商类型路线下，“it is difficult to define the intended monad multiplication for the quotiented datatype”，其解法需要 “proposition extensionality and the (semi-classical) axiom of countable choice”。

该来源把“商表示能得到什么、需要什么假设”写成条件句；没有声称商类可以直接承担含完成先后的操作。判定 `BOUNDED_DEFENSE`。

## 3. D3：delay 与 effects 的组合边界

D3 摘要明确写出：

- “general theorems stating which algebraic effects distribute over the delay monad, and which do not”；
- “we salvage some of the impossible cases by considering distributive laws up to weak bisimilarity”。

即作者把不可分配情形显式记录下来，并用弱互模拟升级的分配律作补救；没有把结果商当作所有 effect 组合的完整程序身份。判定 `BOUNDED_DEFENSE`。

## 4. D4：CATT 的成本自述

全文相关陈述：

- 摘要：“has a primitive notion of cost (the number of evaluation steps)”；“a new dependent function type ‘funtime’ whose semantics can be viewed as a cost-aware version of function extensionality”；“can be simultaneously viewed as a framework for analyzing computational complexity of programs …”。
- 讨论（约 chars 6,806）：语言级复杂度 “do reflect real-life performance, as long as the implementation is resource bounded by the cost semantics”，并说明 cost-preserving compilation 的前提是每一步编译保持成本上界。

也就是说，CATT 通过**新增成本结构**获得自述能力，并把现实性能对应条件写成“implementation is resource bounded by the cost semantics”。这不是“从裸函数恢复成本”；判定 `BOUNDED_DEFENSE`。

## 5. D5：本地 Cubical v0.9 派生模块

- `Cubical/Papers/` 的论文形式化（仿射概形、cohomology rings、Pi4S3 等）是数学定理形式化，没有对“计算/提取/序列化”作超出接口的自述；
- `MagicTrick` 明确写出 `recover : ∥A∥₁ → A` 不能类型检查，并引用 “Composition is not what you think it is!”（N1 已审计）；
- `Cubical/Axiom/Choice.agda` 的消费者（`EilenbergSteenrod.agda`）把 `satAC` 作为**显式函数参数**传入，没有把选择原则隐藏成默认能力（N1 已审计）。

判定 `BOUNDED_DEFENSE`。

## 6. 汇总与 N5 判定

| 来源 | 最接近“升级”的句子 | 实际假设/限定 | 判定 |
|---|---|---|---|
| D1 §5.2 | “we can define `isPositive : ℝq → 𝟐⊥`” | 明确 partial；总 `ℝq → 𝟐` 不可定义/常值；非 definitional equality | `BOUNDED_DEFENSE` |
| D1 §5.3 | compiler correctness “ported to the partiality monad” | 相对 partial 语义；细节在源码 | `BOUNDED_DEFENSE` |
| D2 | 商 delay monad 仍是 monad（setoid 路线） | 商类型路线需 proposition extensionality + countable choice | `BOUNDED_DEFENSE` |
| D3 | 组合 delay 与 effects | 哪些分配律存在/不存在被写成定理；不可能情形 up to weak bisimilarity | `BOUNDED_DEFENSE` |
| D4 | “framework for analyzing computational complexity” | primitive cost + funtime；现实性能需 resource-bounded implementation | `BOUNDED_DEFENSE` |
| D5 | `recover`、`satAC` 消费者 | 类型围栏 + 显式参数 | `BOUNDED_DEFENSE` |

N5 判定：`BOUNDED_DEFENSE (SCOPED)`——固定集合内没有 `FOUND_CANDIDATE`；四份来源在其自述中都携带了接口假设，未发现“同一任务下把较弱资格当较强交付”的真实调用链。

负结论范围：只覆盖 D1–D5 的版本与所核层级；不证明所有派生开发都没有这种升级。

## 7. 下一工作包 N6：partial decision 与 total decision 的最小机器边界

N5 没有找到可机器化的候选，但 D1 §5.2 给出一个可执行的**正向构造**：quotient 上存在 partial classifier，但不存在同规格的 total classifier。按 N5 的备选路由，下一工作包固定为：

> **N6：`MP-PARTIAL-DECISION-001`**——在原生 Cubical Agda 中构造一个最小 quotient + classifier 模型，机器证明：
> 
> 1. 不存在与该 quotient 相容的 total `Bool` classifier（正向反例/ no-go）；
> 2. 存在 partial classifier（进入 delay/partiality 结构），并给出其正控制；
> 3. 任何把 partial classifier 当作 total 交付的消费者要么在指定输入上不返回，要么必须显式添加 modulus/decidability/section。
> 
> 预期判词最多 `REPRESENTATION_BOUNDARY`；不重述 race/timeout 与 R036/R038 的既有反例，机制必须落在“partial vs total decision”上。

完成判据：新 F-011 package（source/run/index）、正反控制、明确的禁止外推；若只能复现“partial 不是 total”的平凡事实而无 quotient 结构参与，则停止该子方向。

## 8. 不升级声明

本审计没有新增数学 claim，没有升级任何既有 claim，没有把 `BOUNDED_DEFENSE` 写成“所有派生开发都安全”，也没有启动 ERCF-3。
