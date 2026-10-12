import GodelQ.ZFC.ShiftTools

/-!
# CG-007 · W8 第二层（十七·附）：`subst` 与 `imp` 的相容律

从 `ITSubsts1.lean` 抽出的单条引理，让只依赖它的文件（如 `HAllKey.lean`）
能在不拉入未完成的桥 `iT_substs1` 的前提下过 F-011 收据门禁。

`imp L p q = neg L p ^⋎ q`（`imp` 的定义），于是
`subst w (imp p q) = subst w (¬p ^⋎ q) = (subst w (¬p)) ^⋎ (subst w q)`；
`subst w (¬p) = ¬(subst w p)` 由 Foundation 的 `substs_neg` 给出。
-/

set_option maxHeartbeats 8000000

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.SeqTranslate

namespace GodelQ.ITSubsts1

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- `subst` 与 `imp` 相容。 -/
lemma subst_imp {n p q m w : V} (hp : IsSemiformula ℒₛₑₜ n p) (hq : IsSemiformula ℒₛₑₜ n q)
    (hw : IsSemitermVec ℒₛₑₜ n m w) :
    subst ℒₛₑₜ w (imp ℒₛₑₜ p q) =
      imp ℒₛₑₜ (subst ℒₛₑₜ w p) (subst ℒₛₑₜ w q) := by
  rw [imp, imp, substs_or hp.neg.isUFormula hq.isUFormula]
  congr 1
  exact substs_neg hp hw

end GodelQ.ITSubsts1
