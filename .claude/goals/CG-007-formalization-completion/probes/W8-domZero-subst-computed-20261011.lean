import GodelQ.ZFC.ShCraigElimBranches
import GodelQ.ZFC.TranslateShiftCompat

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.TranslateShiftCompat

set_option maxHeartbeats 800000

namespace GodelQ.ProbeAE
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- 分两步，每步都用 have 固定类型
lemma termSubstVec_fvar_of_bvar :
    termSubstVec ℒₛₑₜ (1 : V) (?[^&0] : V) (?[^#0] : V) = ?[^&0] := by
  rw [show (1 : V) = 0 + 1 by norm_num,
      termSubstVec_cons (L := ℒₛₑₜ) (IsUTerm.bvar (z := 0)) IsUTermVec.empty,
      termSubst_bvar, termSubstVec_nil]
  simp

lemma subst_domZero_expand : subst ℒₛₑₜ (?[^&0] : V) (domZero (V := V))
    = subst ℒₛₑₜ (?[^&0] : V) ((cDomN : ℕ) : V) := by
  have h1 : IsSemitermVec ℒₛₑₜ (1 : V) (1 : V) (?[^#0] : V) :=
    isSemitermVec_single_bvar (n := 1) (by simp)
  have h2 : IsSemitermVec ℒₛₑₜ (1 : V) (1 : V) (?[^&0] : V) :=
    IsSemitermVec.singleton.mpr (IsSemiterm.fvar 1 0)
  have hstep : subst ℒₛₑₜ (?[^&0] : V) (subst ℒₛₑₜ (?[^#0] : V) ((cDomN : ℕ) : V))
      = subst ℒₛₑₜ (termSubstVec ℒₛₑₜ (1 : V) (?[^&0] : V) (?[^#0] : V)) ((cDomN : ℕ) : V) :=
    substs_substs (L := ℒₛₑₜ) (l := (1 : V)) (n := (1 : V)) (m := (1 : V))
      (isSemiformula_cDomN) h2 h1
  show subst ℒₛₑₜ (?[^&0] : V) (subst ℒₛₑₜ (?[^#0] : V) ((cDomN : ℕ) : V))
      = subst ℒₛₑₜ (?[^&0] : V) ((cDomN : ℕ) : V)
  rw [hstep, termSubstVec_fvar_of_bvar]

end GodelQ.ProbeAE
