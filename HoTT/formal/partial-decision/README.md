# MP-PARTIAL-DECISION-001：strict classifier 与 partial classifier 的最小原生边界

状态：`MACHINE_PROVED_LOCAL_UNCOMMITTED / PARTIAL_DECISION_BOUNDARY_WITH_POSITIVE_CONTROL`

本包把 N5 审计中 D1（Altenkirch–Danielsson–Kraus, *Partiality, Revisited* §5.2）的边界做成最小原生 Cubical 机器构造：**同一个分类器在代表层是 strict 的，在商层只以 weak-bisimilarity 意义可交付；要求 strict 交付的消费者无法下降到商。**

## 固定构造

- 源状态 `A = {a,b,c}`；关系 `R_A` 只识别 `a,b`；商 `Q = A / R_A`；
- 最小 delay/partiality 片段 `Delay Bool = now Bool | later (Delay Bool)`；
- 弱互模拟式关系 `R_D`：`R_D (now x) (later (now y)) = (x ≡ y)`；商 `D≈ = Delay Bool / R_D`；
- 代表层分类器 `P0 a = now true`、`P0 b = later (now true)`、`P0 c = now false`；
- strict 观察 `strict (now _) = true`、`strict (later _) = false`。

## 冻结命题（`C-118`–`C-123`）

| claim | 形式化结果 |
|---|---|
| `C-118` | 代表层 strict 分类器存在（`C-118-P0`）。 |
| `C-119` | strict 观察区分 `now` 与 `later`（`C-119-strict-separates`）。 |
| `C-120` | 不存在 `g : Q → Delay Bool` 同时满足 `g [a] ≡ now true` 与 `g [b] ≡ later (now true)`（`C-120-no-strict-quotient`）；因为 `[a] ≡ [b]` 会迫使 `now true ≡ later (now true)`。 |
| `C-121` | `P0` 只到 `R_D` 意义下不变，因而下降到 partial classifier `P : Q → D≈`（`C-121-partial-classifier`）——正控制。 |
| `C-122` | 不存在 strict 的 `Bool` 消费者 `h : Q → Bool` 同时取 `h [a] ≡ true`、`h [b] ≡ false`（`C-122-no-strict-consumer`）。 |
| `C-123` | 在代表层，strict 消费者存在并区分 `a,b`（`C-123-representative-consumer`）；信息只在商化时丢失。 |

## 解释边界（判词）

判词：`PARTIAL_DECISION_BOUNDARY_WITH_POSITIVE_CONTROL`（第二级结构性结果）：

- 商层可交付的是 **up-to-weak-bisimilarity 的 partial classifier**（`Q → D≈`），不是 strict delay 值（`Q → Delay Bool`），也不是 strict Bool 消费者；
- 这正是 D1 §5.2 的结构：`isPositive : ℝq → 𝟐⊥` 的 partial 版本存在，而 strict/total 版本需要额外 modulus/decidability/section；
- 不是 HoTT 内部矛盾：理论正确地把“结果值”与“完成时刻/严格展示”分开；
- 需要 strict 时序的消费者必须保留代表（`A → Bool` 正控制）或显式添加时序/表示数据。

## 不证明（非目标）

- 不构造完整 partiality monad，也不形式化 `ℝq → 𝟐⊥`（本包是 delay 片段的最小实例）；
- 不证明一般商的 strict/partial 二分；
- 不证明任何真实库或系统存在错误消费者；
- 不认领原创性（partial-vs-total/weak-bisimilarity 边界由 D1 及既有 partiality 文献给出）。

## 证明身份

- proof ID：`MP-PARTIAL-DECISION-001`
- claim IDs：`C-118`–`C-123`
- source：`PartialDecision.agda`
- toolchain：`TOOLCHAIN.json` + `AGDA_LIBRARIES`
- final run：`20260912-MP-PARTIAL-DECISION-001-01`
- index：`../../CLAIM_EVIDENCE_MATRIX.md`

Agda 2.8.0/Cubical v0.9 在 `--safe --cubical --guardedness --ignore-interfaces` 下实际接受本文件；运行原件、外部依赖哈希与命令在 `../../verification/runs/20260912-MP-PARTIAL-DECISION-001-01/`。当前未获 Git commit/tag 授权，因此不能称 `MACHINE_PROVED_VERSION_CLOSED`。
