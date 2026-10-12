import GodelQ.ZFC.ShCraigElimSetupQ

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat

set_option maxHeartbeats 800000

namespace GodelQ.ProbeW
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! ## `W n`：`free` 在 `iT` 上的代入向量

`free X = subst ℒₛₑₜ ?[^&0] (shift X)`。把 `subst` 推过 `iT` 内部的 `n` 层量词后，
向量变成 `qVec^n ?[^&0]`。本文件把它写成**原始递归**（照 `shiftVec` 的先例）：

```
W n = ?[^#0, ^#1, …, ^#(n-1), ^&0]      （n + 1 个分量）
```

即 `W 0 = ?[^&0]`，`W (n+1) = ^#0 ∷ termBShiftVec (W n)`。

先证三条基本性质（照 `shiftVec` 的写法）。 -/

section W

/-! **`W n` 的构造**：`W 0 = ?[^&0]`，`W (n+1) = ^#0 ∷ termBShiftVec n (W n)`。

**长度与层数的账**（照 `shiftVec` 的 `b n` 两参形式）：
`W n` 有 `n + 1` 个分量（`n` 个 bvar 加一个 fvar），层数为 `n + 1`。
`termBShiftVec k v` 保持 `len v` 不变、把层数加一。
所以 `W_succ` 里 `termBShiftVec` 的第一个参数（长度）应是 `len (W n) = n + 1`。
下面的定义把 `n` 作为**索引**传入，`W_succ` 的等式里用 `n + 1` 写长度——
与 `shiftVec_succ`（那里 `termBShiftVec n ih` 的 `n` 恰好是长度）不同，
因为 `shiftVec` 的 `zero` 是空向量而 `W` 的 `zero` 已有一个分量。 -/

noncomputable def W.blueprint : PR.Blueprint 1 where
  zero := .mkSigma “y b. ∃ f, !qqFvarDef f 0 ∧ !adjoinDef y f 0”
  succ := .mkSigma “y ih n. ∃ h, !qqBvarDef h 0 ∧ ∃ t, !(termBShiftVecGraph ℒₛₑₜ) t (n + 1) ih ∧ !adjoinDef y h t”

noncomputable def W.construction : PR.Construction V W.blueprint where
  zero := fun _ ↦ (?[^&0] : V)
  succ := fun _ n ih ↦ ^#(0:V) ∷ termBShiftVec ℒₛₑₜ (n + 1) ih
  zero_defined := .mk fun v ↦ by simp [W.blueprint]
  succ_defined := .mk fun v ↦ by simp [W.blueprint]

/-- `W n = ?[^#0, ^#1, …, ^#(n-1), ^&0]`（`n + 1` 个分量）。 -/
noncomputable def W (n : V) : V := W.construction.result ![0] n

@[simp] lemma W_zero : W (V := V) 0 = (?[^&0] : V) := by
  simp [W, W.construction]

@[simp] lemma W_succ (n : V) :
    W (V := V) (n + 1) = ^#(0:V) ∷ termBShiftVec ℒₛₑₜ (n + 1) (W (V := V) n) := by
  simp [W, W.construction]

-- 首分量恒为 `^#0`（`conjunct` 的换名靠它）
@[simp] lemma W_head (n : V) : (W (V := V) (n + 1)).[0] = (^#(0:V) : V) := by
  rw [W_succ, nth_adjoin_zero]

-- `W n` 是项向量（长度 `n+1`、层数 `n+1`）——`V` 层的 `len` 账用 `IsUTermVec` 绕开
lemma isUTermVec_W : ∀ n : ℕ, IsUTermVec ℒₛₑₜ ((n : V) + 1) (W (V := V) (n : V)) := by
  intro n
  induction n with
  | zero =>
    rw [Nat.cast_zero, W_zero]
    exact IsUTermVec.adjoin (IsUTermVec.empty (L := ℒₛₑₜ) (V := V)) (IsUTerm.fvar (x := (0:V)))
  | succ k ih =>
    rw [show ((k + 1 : ℕ) : V) = (k : V) + 1 by push_cast; ring, W_succ]
    exact IsUTermVec.adjoin (ih.termBShiftVec) (IsUTerm.bvar (z := (0:V)))

end W

end GodelQ.ProbeW
