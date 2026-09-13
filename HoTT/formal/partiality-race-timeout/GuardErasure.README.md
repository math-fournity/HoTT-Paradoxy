# MP-GUARD-ERASURE-001：阶段擦除与不动点的等价

状态：`MACHINE_PROVED_LOCAL_UNCOMMITTED / GUARD_ERASURE_EQUIVALENT_TO_FIXED_POINT_EXISTENCE`

本包把 `DIR-L-GUARD-ERASURE` 的候选做成第一机器构造，并以显式源演算（分阶段流）与显式忘却翻译细化历史 `ZCore.agda` 的条件引理（historical aggregate，需要重放才能重新交付）：**「保更新律地擦除阶段」与本法律存在不动点，是同一件事。**

## 固定构造

- 源演算：显式阶段的流 `ℕ → X`，推进算子 `shift s n = s (suc n)`；
- 忘却翻译：`g : (ℕ → X) → X`，同时要求
  - 阶段不变性：`∀ s, g (shift s) ≡ g s`（忘掉阶段）；
  - 保更新律：`∀ s, g (shift s) ≡ f (g s)`（记住律 `f`）。

## 冻结命题

- `C-92`（必要性）：满足上述两条的 `g` 存在 ⇒ `Σ[ x ∈ X ] (x ≡ f x)`（用任一 `s₀` 取值）。
- `C-93`（否定律实例）：`X = Bool`、`f = not` 时不存在这样的 `g`（否则 `x ≡ not x`，与 Bool 无不动点矛盾）。
- `C-94`（充分性）：任何不动点 `x₀`（`x₀ ≡ f x₀`）给出常值翻译 `g := const x₀`，满足两条要求。
- `C-95`（具体轨道）：`orbit (suc n) = not (orbit n)` 在源演算中可实现，且 `¬ (orbit 0 ≡ orbit 1)`——阶段在源演算中是可观察的，不能免费擦除。

## 解释边界（判词）

判词：`GUARD_ERASURE_EQUIVALENT_TO_FIXED_POINT_EXISTENCE`，即判词阶梯的第二级（表示/资格边界）的结构性版本：

- 该结果不是 HoTT 悖论，而是把"何时允许忘掉阶段"精确化为一个等价的代数条件（不动点存在）；振荡律下阶段擦除被正确拒绝，常值/幂等律下擦除可构造；
- 它同时给出正向控制（`C-94`）与具体反例（`C-95`），避免"阶段擦除全都不可行"的过强论断。

## 不证明（非目标）

- 不证明 guarded/clocked 类型论（如 gDTT/Clocked TT）的完整翻译等价；本包使用 ℕ-indexed 显式阶段模型；
- 不证明任何现实过程/物理时间主张，也不主张 HoTT 独有；
- 不认领原创性：条件引理的历史形式见 `../self-contained/ZCore.agda`（historical aggregate）。

## 证明身份

- proof ID：`MP-GUARD-ERASURE-001`
- claim IDs：`C-92`–`C-95`
- final run：`20260912-MP-GUARD-ERASURE-001-01`
- source：`GuardErasure.agda`
- toolchain：同目录 `TOOLCHAIN.json` + `AGDA_LIBRARIES`
- index：`../../CLAIM_EVIDENCE_MATRIX.md`

Agda 2.8.0/Cubical v0.9 在 `--safe --cubical --guardedness --ignore-interfaces` 下实际接受本文件。运行原件见 `../../verification/runs/20260912-MP-GUARD-ERASURE-001-01/`。当前未获 Git commit/tag 授权，不能称 `MACHINE_PROVED_VERSION_CLOSED`。
