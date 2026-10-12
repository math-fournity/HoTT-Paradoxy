import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.ZFCZ0 GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000
namespace GodelQ.ProbeI
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! ## 用 `subst_eq_self` 绕开 `termSubstVec` 的 numeral 问题

`keyL` 的目标是
`subst (^#0 ∷ ^#2 ∷ 0) (^rel 2 cEqN (^#0 ∷ ^#1 ∷ 0)) = ^rel 2 cEqN (^#0 ∷ ^#2 ∷ 0)`。

**换个视角**：这条等式说的是「把 `^#1` 换成 `^#2`」——正是 `subst` 的定义行为。
但也可以用 `subst` 的**复合律**：
`subst w (subst v p) = subst (termSubstVec _ w v) p`（`subst_substs`），
或直接用 `substs_rel` 但**让 `v` 匹配目标**。

先测最直接的：`termSubstVec` 对**具体**向量的计算（用 `decide` 不行，用 `simp`）。 -/

-- `termSubstVec 2 (^#0 ∷ ^#2 ∷ 0) (^#0 ∷ ^#1 ∷ 0) = ?`
example : termSubstVec ℒₛₑₜ 2 ((^#(0:V) : V) ∷ ((^#(2:V) : V) ∷ (0 : V)))
    ((^#(0:V) : V) ∷ ((^#(1:V) : V) ∷ (0 : V))) = ((^#0 : V) ∷ ((^#2 : V) ∷ (0 : V))) := by
  rw [show (2 : V) = 0 + 1 + 1 by norm_num]
  rw [termSubstVec_cons (IsUTerm.bvar (z := (0:V)))
        (IsUTermVec.adjoin IsUTermVec.empty (IsUTerm.bvar (z := (1:V)))),
      termSubstVec_cons (IsUTerm.bvar (z := (1:V))) IsUTermVec.empty,
      termSubstVec_nil, termSubst_bvar, termSubst_bvar]
  simp only [nth_adjoin_zero, nth_adjoin_one]

end GodelQ.ProbeI
