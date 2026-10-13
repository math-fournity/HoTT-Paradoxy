import GodelQ.ZFC.ShCraigElimBranches
import GodelQ.ZFC.TranslateShiftCompat

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.TranslateShiftCompat

set_option maxHeartbeats 800000

namespace GodelQ.ProbeAK
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- 正确形状：t 是层数 ≤ 1 的项（只含 #0/#1 与 fvar）
-- 此时 termSubstVec 2 (^#0 ∷ s ∷ 0) 与 termSubstVec 1 ?[s] 在 t 上一致
-- （两者 [0] = ^#0、[1] = s 相同；t 不含 ≥ 2 的 bvar）
lemma subst_eqAtom_qVec (s t : V) (ht : IsUTerm ℒₛₑₜ t)
    (hbv : termBV ℒₛₑₜ t ≤ 1) :
    subst ℒₛₑₜ ((^#0 : V) ∷ (s ∷ (0 : V))) (eqAtom t)
      = eqAtom (subst ℒₛₑₜ (?[s] : V) t) := by
  have hb : IsUTerm ℒₛₑₜ (^#0 : V) := IsUTerm.bvar (z := 0)
  have h1 : IsUTermVec ℒₛₑₜ (1 : V) (t ∷ (0 : V)) := by
    simpa using IsUTermVec.adjoin IsUTermVec.empty ht
  have hv2 : IsUTermVec ℒₛₑₜ (2 : V) ((^#0 : V) ∷ (t ∷ (0 : V))) := by
    simpa [show (2 : V) = 1 + 1 by norm_num] using IsUTermVec.adjoin h1 hb
  show subst ℒₛₑₜ ((^#0 : V) ∷ (s ∷ (0 : V)))
      (^rel 2 (↑cEqN) ((^#0 : V) ∷ (t ∷ (0 : V))))
    = ^rel 2 (↑cEqN) ((^#0 : V) ∷ (subst ℒₛₑₜ (?[s] : V) t ∷ (0 : V)))
  rw [substs_rel (by rw [cEqN]; exact codeIn_rel_quote _) hv2]
  congr 1
  -- 关键：termSubstVec 2 (^#0 ∷ s ∷ 0) ?[^#0, t] = ?[^#0, subst ?[s] t]
  rw [show (2 : V) = 1 + 1 by norm_num,
      termSubstVec_cons hb (by simpa using IsUTermVec.adjoin IsUTermVec.empty ht),
      termSubst_bvar,
      show (1 : V) = 0 + 1 by norm_num,
      termSubstVec_cons ht IsUTermVec.empty,
      termSubstVec_nil]
  -- 两边都化成 `^#0 ∷ (_ ∷ 0)` 形式，然后逐分量
  rw [show ((^#0 : V) ∷ (s ∷ (0:V))).[0] = (^#0 : V) from nth_adjoin_zero _ _]
  show (^#0 : V) ∷ (termSubst ℒₛₑₜ ((^#0 : V) ∷ (s ∷ (0:V))) t ∷ (0:V))
      = (^#0 : V) ∷ (subst ℒₛₑₜ (?[s] : V) t ∷ (0:V))
  congr 1
  -- `termSubst (^#0 ∷ s ∷ 0) t = termSubst (s ∷ 0) t`（前 `termBV t + 1` 格一致）
  -- `IsUTerm t` ⟹ `IsSemiterm (termBV t) t`，再 `semi_mono` 抬到 `termBV t + 1`
  have hst : IsSemiterm ℒₛₑₜ (termBV ℒₛₑₜ t + 1) t :=
    semi_mono (n := termBV ℒₛₑₜ t) (ht.isSemiterm)
      (show termBV ℒₛₑₜ t ≤ termBV ℒₛₑₜ t + 1 from by
        have h := lt_add_self_add_one (0:V) (termBV ℒₛₑₜ t)
        have e : termBV ℒₛₑₜ t + 0 + 1 = termBV ℒₛₑₜ t + 1 := by ring
        rwa [e] at h)
  refine termSubst_congr' (L := ℒₛₑₜ) (n := termBV ℒₛₑₜ t + 1) ?_ t hst
  intro i hi
  rcases zero_or_succ i with (rfl | ⟨j, rfl⟩)
  · rw [show ((^#0 : V) ∷ (s ∷ (0:V))).[0] = (^#0 : V) from nth_adjoin_zero _ _,
      show (s ∷ (0:V)).[0] = s from nth_adjoin_zero _ _]
  · rw [show ((^#0 : V) ∷ (s ∷ (0:V))).[j + 1] = (s ∷ (0:V)).[j] from nth_adjoin_succ _ _ _,
      show (s ∷ (0:V)).[j + 1] = (0:V).[j] from nth_adjoin_succ _ _ _]
    have hj : j < termBV ℒₛₑₜ t := by simpa using hi
    exact absurd hj (by
      have hz : (0:V).[j] = (0:V) := nth_lt_len (by rw [len_zero_iff_eq_nil]; rfl)
      rw [hz] at hj
      exact not_lt_of_ge (zero_le j))

end GodelQ.ProbeAK
