import GodelQ.ZFC.ShCraigElimBranches
import GodelQ.ZFC.TranslateShiftCompat

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.TranslateShiftCompat

set_option maxHeartbeats 800000

namespace GodelQ.ProbeS

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- ═══ 决定性检验 ①：domZero 是否对 subst ?[^&0] 不变？ ═══
-- domZero = subst ℒₛₑₜ ?[^#0] cDomN，cDomN 是引号化句子（无自由变量、无自由 bvar）
example : subst ℒₛₑₜ (?[^&0] : V) (domZero (V := V)) = domZero (V := V) := by
  show subst ℒₛₑₜ (?[^&0] : V) (subst ℒₛₑₜ (?[^#0] : V) ((cDomN : ℕ) : V))
      = subst ℒₛₑₜ (?[^#0] : V) ((cDomN : ℕ) : V)
  rw [substs_substs (L := ℒₛₑₜ) (l := 1) (n := 1) (m := 1)
      isSemiformula_cDomN
      (isSemitermVec_single_bvar (n := 1) (by simp))
      (isSemitermVec_single_bvar (n := 1) (by simp))]
  -- termSubstVec ℒₛₑₜ 1 ?[^&0] ?[^#0] = ?
  rw [show (termSubstVec ℒₛₑₜ 1 (?[^&0] : V) (?[^#0] : V)) = ?[^&0] from by
    rw [show (1 : V) = 0 + 1 by norm_num, termSubstVec_cons
        (IsUTerm.bvar (z := 0)) IsUTermVec.empty, termSubst_bvar,
      termSubstVec_nil, nth_adjoin_zero]]

-- ═══ 决定性检验 ②：imp domZero X 对 subst ?[^&0] 的行为 ═══
example (X : V) (hX : IsUFormula ℒₛₑₜ X) :
    subst ℒₛₑₜ (?[^&0] : V) (imp ℒₛₑₜ (domZero (V := V)) X)
      = imp ℒₛₑₜ (domZero (V := V)) (subst ℒₛₑₜ (?[^&0] : V) X) := by
  show subst ℒₛₑₜ (?[^&0] : V) (neg ℒₛₑₜ (domZero (V := V)) ^⋎ X)
      = neg ℒₛₑₜ (domZero (V := V)) ^⋎ subst ℒₛₑₜ (?[^&0] : V) X
  rw [substs_or (L := ℒₛₑₜ)
      (IsUFormula.neg (isSemiformula_domZero' (V := V)).isUFormula) hX,
    substs_neg (L := ℒₛₑₜ) (isSemiformula_domZero' (V := V))
      (isSemitermVec_single_bvar (n := 1) (by simp))]

end GodelQ.ProbeS
