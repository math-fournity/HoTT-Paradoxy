# MP-CONTEXT-CHARACTERIZATION-001 机器证明实施证据（2026-09-12）

状态：`MACHINE_PROVED_LOCAL_UNCOMMITTED / CONTEXTUAL_EQUIVALENCE_FULLY_CHARACTERIZED`。

本文件记录 contextual equivalence 收敛的收束结果：Bool 片段上 `≡c` 恰等于代表相等。

## 1. 触发与依据

- 触发：S036 后 `方向追踪.md` §6 第 4 项（`≡c` 的完整刻画）。
- 依据：`ContextualEquivalence`（`Ctx`/`plug`/`≡c`/分离引理）与 `PartialityRaceTimeout`（模型定义）两个已冻结模块；本包只新增刻画，不改写旧源码。

## 2. 本轮构造

- `lt-trichotomy`（`C-89`）：对 `n m` 三分（相等 / `lt n m` / `lt m n`），归纳证明；
- `timing-separates`（`C-90`）：任意 `n ≢ m` 的时间分离（合并 deadline-0 与单向 `lt` 情形，必要时取 `≡c` 对称）；
- 完整刻画（`C-91`）：用 deadline 观察（`dl-refl`/`dl-lt`/`dl-gt`、`isSomeO`、`fromSome`）在 `ω`/返回、时间、取值三类差异上分别分离，再用 `≡-to-≡c`/`≡c-to-≡` 双向收口。

## 3. 被机器核验的 claim

| claim | 精确内容 | 关键定义 |
|---|---|---|
| `C-89` | `(n ≡ m) ⊎ ((lt n m ≡ true) ⊎ (lt m n ≡ true))` | `lt-trichotomy` |
| `C-90` | `¬ (n ≡ m) → ¬ (ret n a ≡c ret m a)` | `timing-separates` |
| `C-91` | `(p q : Delay Bool) → (p ≡c q) ⇔ (p ≡ q)` | `≡c-iff-≡`，含 `deadline-lt-separates`、`deadline-gt-separates`、`same-time-values` |

## 4. 运行与核验

- final run：`HoTT/verification/runs/20260912-MP-CONTEXT-CHARACTERIZATION-001-01/`；
- 同一 Agda 2.8.0 + Cubical v0.9 工具链；exit 0，stderr 0 字节；
- 独立重放：`KERNEL_ACCEPTED_WITH_SCOPE / INDEXED_IN_CLAIM_EVIDENCE_MATRIX / EXACT_INDEX_SNAPSHOT_MATCH / EXACT_EXIT_STDOUT_STDERR_MATCH`；
- 矩阵第四次增长后重放五个旧包，全部 `ROW_STABLE_AFTER_INDEX_EVOLUTION` + exact replay。

## 5. 失败与修订谱系

本包编译迭代中修正：`_⊎_` 非结合导致的解析歧义（加括号）、`if_then_else_` 未导入、`deadline-gt-separates` 的等式链方向写反。均为机械修正，命题未削弱。

## 6. 判词与边界

判词：`CONTEXTUAL_EQUIVALENCE_FULLY_CHARACTERIZED`。

- 在本片段，最粗的被完整上下文族尊重的等价就是代表相等；代表相等已是最细，因此任何上下文扩展都不能区分更多（"更宽上下文语言"问题在 Bool 片段闭合）；
- 仍不是 HoTT 悖论：HoTT 精确保留完成先后；
- 不推广到一般值类型（缺少两元素分离/`fromSome` 工具）与一般商。

## 7. Git 与版本状态

源码、运行原件与索引均为本地未提交状态（无 commit/tag/push 授权），不能称 `MACHINE_PROVED_VERSION_CLOSED`。
