import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000
namespace GodelQ.ProbeW1
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! ## `W n`：`iT_subst_W` 的代入向量（2026-10-12）

`W n = ?[^#0, ^#1, …, ^#(n-1), ^&0]`（`n + 1` 个分量，层数 `n`）。
关键恒等式 **`W (n+1) = qVec (W n)`** ——正是 `substs_all` 需要的形状。 -/

section W

noncomputable def W.blueprint : PR.Blueprint 1 where
  zero := .mkSigma “y b. ∃ f, !qqFvarDef f 0 ∧ !adjoinDef y f 0”
  succ := .mkSigma “y ih n. ∃ h, !qqBvarDef h 0 ∧ ∃ t, !(termBShiftVecGraph ℒₛₑₜ) t (n + 1) ih ∧ !adjoinDef y h t”

noncomputable def W.construction : PR.Construction V W.blueprint where
  zero := fun _ ↦ (?[^&0] : V)
  succ := fun _ n ih ↦ ^#(0:V) ∷ termBShiftVec ℒₛₑₜ (n + 1) ih
  zero_defined := .mk fun v ↦ by simp [W.blueprint]
  succ_defined := .mk fun v ↦ by simp [W.blueprint]

noncomputable def WDef : 𝚺ᴬ₁.Semisentence 2 := W.blueprint.resultDef

instance W_defined : 𝚺ᴬ₁-Function₁ (W : V → V) via WDef := .mk
  fun v ↦ by simp [W.construction.result_defined_iff, WDef]; rfl

instance W_definable : 𝚺ᴬ₁-Function₁ (W : V → V) := W_defined.to_definable

instance W_definable' (Γ m) : Γᴬ_[m + 1]-Function₁[V] W := W_definable.of_sigmaOne

noncomputable def W (n : V) : V := W.construction.result ![0] n

@[simp] lemma W_zero : W (V := V) 0 = (?[^&0] : V) := by simp [W, W.construction]

@[simp] lemma W_succ (n : V) :
    W (V := V) (n + 1) = ^#(0:V) ∷ termBShiftVec ℒₛₑₜ (n + 1) (W (V := V) n) := by
  simp [W, W.construction]

/-- `W n` 是项向量（长度 `n+1`、层数 `n`）。 -/
lemma isUTermVec_W : ∀ n : V, IsUTermVec ℒₛₑₜ (n + 1) (W (V := V) n) := by
  intro n
  induction n using ISigma1.sigma1_succ_induction
  · definability
  case zero => simp [W_zero]
  case succ n ih =>
    rw [W_succ, show n + 1 + 1 = (n + 1) + 1 by ring]
    exact IsUTermVec.adjoin ih.termBShiftVec (IsUTerm.bvar (z := (0:V)))

/-- **关键恒等式**：`W (n+1) = qVec (W n)`。 -/
lemma W_succ_eq_qVec (n : V) : W (V := V) (n + 1) = qVec ℒₛₑₜ (W (V := V) n) := by
  rw [W_succ, Bootstrapping.qVec, show len (W (V := V) n) = n + 1 from (isUTermVec_W n).lh]

/-- `W n` 的分量：`i < n` 时是 `^#i`。 -/
lemma W_nth : ∀ n : V, ∀ i < n, (W (V := V) n).[i] = (^#i : V) := by
  intro n
  induction n using ISigma1.sigma1_succ_induction
  · definability
  case zero => intro i hi; exact absurd hi (by simp)
  case succ n ih =>
    intro i hi
    rcases zero_or_succ i with (rfl | ⟨j, rfl⟩)
    · rw [W_succ, nth_adjoin_zero]
    · rw [W_succ, nth_adjoin_succ]
      rw [show (n + 1 : V) = len (W (V := V) n) from ((isUTermVec_W n).lh)]
      rw [nth_termBShiftVec (isUTermVec_W n) (by simpa using hi), ih j (by simpa using hi),
        termBShift_bvar]

/-- `W n` 的末分量（下标 `n`）是 `^&0`。 -/
lemma W_nth_self (n : V) : (W (V := V) n).[n] = (^&0 : V) := by
  induction n using ISigma1.sigma1_succ_induction
  · definability
  case zero => simp [W_zero]
  case succ n ih =>
    rw [W_succ, nth_adjoin_succ]
    rw [show (n + 1 : V) = len (W (V := V) n) from ((isUTermVec_W n).lh)]
    rw [nth_termBShiftVec (isUTermVec_W n) (by simp [(isUTermVec_W n).lh]), ih,
      termBShift_fvar]

end W

end GodelQ.ProbeW1
