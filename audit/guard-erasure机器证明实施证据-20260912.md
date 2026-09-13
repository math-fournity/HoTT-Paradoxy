# MP-GUARD-ERASURE-001 机器证明实施证据（2026-09-12）

状态：`MACHINE_PROVED_LOCAL_UNCOMMITTED / GUARD_ERASURE_EQUIVALENT_TO_FIXED_POINT_EXISTENCE`。

本文件记录 `DIR-L-GUARD-ERASURE` 第一机器构造：把"忘掉阶段但保留更新律"精确化为一个等价条件。

## 1. 触发与依据

- 触发：S037 后 `方向追踪.md` §6 第 4 项（guard-erasure 第一机器构造）。
- 依据：LocalGPT 历史候选与 `HoTT/formal/self-contained/ZCore.agda` 的条件引理 `guard-erasure-implies-fixed-point`（historical aggregate，需重放才可重新交付）。本包用当前工具链与显式源演算/翻译重做并加强为双向等价。

## 2. 本轮构造

- 源演算：显式阶段的流 `ℕ → X` 与推进算子 `shift`；
- 忘却翻译 `g : (ℕ → X) → X`，要求阶段不变性与保更新律两条；
- 必要性由等式链给出；充分性由常值翻译给出；否定律实例由 Bool 无不动点给出；具体振荡轨道与阶段可观察性由计算给出。

## 3. 被机器核验的 claim

| claim | 精确内容 | 关键定义 |
|---|---|---|
| `C-92` | 两条要求 + 任一 `s₀` ⇒ `Σ[ x ∈ X ] (x ≡ f x)` | `collapse-forces-fixed-point` |
| `C-93` | `Bool`/`not` 下不存在这样的 `g` | `no-fixed-point-of-not`、`no-collapse-for-negation` |
| `C-94` | 不动点 `x₀` ⇒ 常值翻译满足两条 | `collapse-exists-if-fixed-point` |
| `C-95` | `orbit (suc n) = not (orbit n)` 且 `¬ (orbit 0 ≡ orbit 1)` | `orbit`、`orbit-law`、`orbit-stages-differ`、`oscillating-orbit` |

## 4. 运行与核验

- final run：`HoTT/verification/runs/20260912-MP-GUARD-ERASURE-001-01/`；
- 同一 Agda 2.8.0 + Cubical v0.9 工具链；exit 0，stderr 0 字节；
- 独立重放：`KERNEL_ACCEPTED_WITH_SCOPE / INDEXED_IN_CLAIM_EVIDENCE_MATRIX / EXACT_INDEX_SNAPSHOT_MATCH / EXACT_EXIT_STDOUT_STDERR_MATCH`；
- 矩阵第五次增长后重放六个旧包，全部 `ROW_STABLE_AFTER_INDEX_EVOLUTION` + exact replay。

## 5. 失败与修订谱系

本包两次机械修正：`⊥` 需显式导入（Empty.Base 的名称不在 `using ()` 重命名范围内时不可见）、`¬` 需本地定义（未导入 partiality 模块）。命题未削弱。

## 6. 判词与边界

判词：`GUARD_ERASURE_EQUIVALENT_TO_FIXED_POINT_EXISTENCE`（判词阶梯第二级的结构性版本）。

- 阶段擦除并非普遍不可行：常值/幂等律下可构造（`C-94`）；振荡律下被正确拒绝（`C-93`）；
- 该等价把"何时允许忘掉阶段"化为代数条件（不动点存在），并提供正反控制；
- 不是 HoTT 悖论；不主张 HoTT 独有、不主张物理时间、不做 guarded/clocked 类型论完整翻译。

## 7. Git 与版本状态

源码、运行原件与索引均为本地未提交状态（无 commit/tag/push 授权），不能称 `MACHINE_PROVED_VERSION_CLOSED`。
