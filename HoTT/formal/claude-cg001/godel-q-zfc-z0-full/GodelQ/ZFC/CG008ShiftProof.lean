import GodelQ.ZFC.CG008Conj

/-!
# CG-008 · `shiftVec` 的项向量性（对任意 `n : V`）
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008ShiftProof
open GodelQ.ZFCArith GodelQ.Translate
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

set_option maxHeartbeats 3200000 in
/-- **`shiftVec b n` 是项向量**（对任意 `n : V`）。

单条归纳，不引递归调用：递推步要的 `IsUTermVec (termBShiftVec n (shiftVec b n))`
由 `IsUTermVec.termBShiftVec`（`Term/Functions.lean:468`）**从归纳假设直接给出**，
不需要在 `b + 1` 上重来。 -/
theorem isUTermVec_shiftVec (b : V) : ∀ n : V,
    Bootstrapping.IsUTermVec ℒₛₑₜ n (Translate.shiftVec b n) := by
  haveI : V↓[ℒₒᵣ] ⊧* 𝗜𝚺⁺₁ := inferInstance
  intro n
  induction n using ISigma1.sigma1_succ_induction with
  | hP => definability
  | zero => simp
  | succ n ih =>
    have hb : Bootstrapping.IsUTerm ℒₛₑₜ (^#b : V) :=
      Bootstrapping.IsUTerm.bvar (L := ℒₛₑₜ) (z := b)
    rw [Translate.shiftVec_succ]
    exact ih.termBShiftVec.adjoin hb

/-- 替换向量 `^#i ∷ shiftVec b n` 是项向量。 -/
lemma isUTermVec_conjunctVec (b n i : V) :
    Bootstrapping.IsUTermVec ℒₛₑₜ (1 + n) (^#i ∷ Translate.shiftVec b n) := by
  have hb : Bootstrapping.IsUTerm ℒₛₑₜ (^#i : V) :=
    Bootstrapping.IsUTerm.bvar (L := ℒₛₑₜ) (z := i)
  have hadj := (isUTermVec_shiftVec (V := V) b n).adjoin hb
  simpa [add_comm] using hadj

/-- **`conjunct` 的第二块**：`subst (#i ∷ shiftVec b n) y` 是公式（`y` 在层 `1 + n`）。

替换向量的层是 `1 + n`（长度），故 `y` 必须恰在层 `1 + n`。
结果层由 `listMax (termBVVec …)` **算出**——**不需要算术界**。 -/
theorem conjunct_snd_isUFormula (b n i y : V)
    (hy : Bootstrapping.IsSemiformula ℒₛₑₜ (1 + n) y) :
    Bootstrapping.IsUFormula ℒₛₑₜ
      (Bootstrapping.subst ℒₛₑₜ (^#i ∷ Translate.shiftVec b n) y) :=
  (Bootstrapping.IsSemiformula.subst hy
    (isUTermVec_conjunctVec b n i).isSemitermVec).isUFormula

/-- **`conjunct b n i y` 是公式**（`y` 在层 `1 + n`）。 -/
theorem conjunct_isUFormula (b n i y : V)
    (hy : Bootstrapping.IsSemiformula ℒₛₑₜ (1 + n) y) :
    Bootstrapping.IsUFormula ℒₛₑₜ (Translate.conjunct b n i y) := by
  rw [Translate.conjunct]
  refine Bootstrapping.IsUFormula.and.mpr ⟨?_, ?_⟩
  · exact GodelQ.CG008VeParts.subst_singleton_isUFormula (V := V) i
      (GodelQ.CG008Ve2.cDomN_isSemiformula (V := V))
  · exact conjunct_snd_isUFormula b n i y hy

end GodelQ.CG008ShiftProof

#print axioms GodelQ.CG008ShiftProof.conjunct_isUFormula
#print axioms GodelQ.CG008ShiftProof.isUTermVec_shiftVec
#print axioms GodelQ.CG008ShiftProof.isUTermVec_conjunctVec
