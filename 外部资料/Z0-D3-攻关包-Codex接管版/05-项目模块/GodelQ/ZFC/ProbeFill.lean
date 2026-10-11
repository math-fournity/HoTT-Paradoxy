import GodelQ.ZFC.Z0Full
import GodelQ.ZFC.SeqTranslate
import GodelQ.ZFC.SeqTranslateFormula
import GodelQ.ZFC.InternalTranslate
import GodelQ.ZFC.ShCraigElimNegLaw

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimNegLaw

namespace GodelQ.ProbeFill

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

def Q (d : V) : Prop := Derivable (L := ℒₛₑₜ) 𝗭𝗙𝗖 (translateSeq (V := V) (fstIdx d))

theorem probe_and {s p q dp dq : V}
    (hs : IsFormulaSet (L := ℒₒᵣ) s)
    (hpq : p ^⋏ q ∈ s)
    (hdp : DerivationOf (L := ℒₒᵣ) Sh.craig dp (insert p s))
    (hdq : DerivationOf (L := ℒₒᵣ) Sh.craig dq (insert q s))
    (ihp : Q dp) (ihq : Q dq) : Q (andIntro s p q dp dq) := by
  simp only [Q, fstIdx_andIntro]
  have hpU : IsUFormula ℒₒᵣ p := (IsUFormula.and.mp ((hs p hpq).isUFormula)).1
  have hqU : IsUFormula ℒₒᵣ q := (IsUFormula.and.mp ((hs p hpq).isUFormula)).2
  have hmem : iT (0 : V) (p ^⋏ q) ∈ translateSeq s :=
    mem_translateSeq_iff.mpr ⟨p ^⋏ q, hpq, rfl⟩
  rw [iT_and hpU hqU] at hmem
  have hdp' : Derivable (L := ℒₛₑₜ) 𝗭𝗙𝗖 (translateSeq (insert p s)) := by
    simpa [Q] using ihp
  have hdq' : Derivable (L := ℒₛₑₜ) 𝗭𝗙𝗖 (translateSeq (insert q s)) := by
    simpa [Q] using ihq
  exact Derivable.and_m hmem hdp' hdq'
end GodelQ.ProbeFill
