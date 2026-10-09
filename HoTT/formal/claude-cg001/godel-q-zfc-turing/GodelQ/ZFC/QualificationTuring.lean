import GodelQ.ZFC.TuringZFC

/-!
# CG-007 · W1：命题对照（CG001-C-104、C-105）

每条命题的类型逐字写在这里，证明只引用前面文件中的定理。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory
open scoped FFL.FirstOrder.Arithmetic

namespace GodelQ.QualTuring

open GodelQ.ZFCNum GodelQ.ZFCArith GodelQ.ZFCEff GodelQ.ZFCSound GodelQ.ZFCTuring

/-- **CG001-C-104（抽象层，图灵路线）**：
(1) 任一可靠、可枚举的永不完成观察者，漏点集不可枚举、无穷；
(2) 补上任意有限个确实永不完成的点之后仍然如此，补丁只拿走那几个点；
(3) 任一有效理论 Q 不完备，漏掉的“永不完成”列不全、无穷，且每个漏点的每个有限时刻都被确认“尚未完成”。 -/
theorem qual_C104 :
    (∀ O : NeverObserver, ¬ REPred (· ∈ O.Misses) ∧ O.Misses.Infinite) ∧
    (∀ (O : NeverObserver) (F : Set Process) (hF : F.Finite) (hnever : ∀ e ∈ F, ¬ Done e),
      (O.patch F hF hnever).Misses = O.Misses \ F ∧
        ¬ REPred (· ∈ (O.patch F hF hnever).Misses) ∧ (O.patch F hF hnever).Misses.Infinite) ∧
    (∀ T : EffectiveTheory, ¬ T.CompleteForNever ∧ ¬ REPred (· ∈ T.Misses) ∧ T.Misses.Infinite ∧
      ∀ e ∈ T.Misses, ∀ k, T.provesNotYet e k) :=
  ⟨fun O => ⟨O.misses_not_re, O.misses_infinite⟩,
   fun O F hF hnever => O.patch_misses F hF hnever,
   fun T => ⟨T.not_completeForNever_turing, T.misses_not_re, T.misses_infinite,
     fun e he k => T.misses_seen_every_instant e he k⟩⟩

/-- **CG001-C-105（真实 𝗭𝗙𝗖，图灵路线）**：
𝗭𝗙𝗖 的漏点恰是“永不停机”句独立于 𝗭𝗙𝗖 的过程；它们列不全、有无穷多个；
𝗭𝗙𝗖 对每个漏点的每个有限时刻都证明“尚未停机”；𝗭𝗙𝗖 的 Q 不完备，𝗭𝗙𝗖 不完全；
有限补丁之后，漏点仍列不全、仍无穷。 -/
theorem qual_C105 :
    zfcMisses = {e | 𝗭𝗙𝗖 ⊬ neverS ΦH (Encodable.encode e) ∧ 𝗭𝗙𝗖 ⊬ haltsS ΦH (Encodable.encode e)} ∧
    ¬ REPred (· ∈ zfcMisses) ∧ zfcMisses.Infinite ∧
    (∀ e ∈ zfcMisses, ∀ k : ℕ, 𝗭𝗙𝗖 ⊢ haltsS ΨN (Encodable.encode (e, k))) ∧
    ¬ zfcEffective.CompleteForNever ∧ Entailment.Incomplete 𝗭𝗙𝗖 ∧
    (∀ (F : Set Process) (hF : F.Finite) (hnever : ∀ e ∈ F, ¬ Done e),
      (zfcEffective.observer.patch F hF hnever).Misses = zfcMisses \ F ∧
        ¬ REPred (· ∈ (zfcEffective.observer.patch F hF hnever).Misses) ∧
        (zfcEffective.observer.patch F hF hnever).Misses.Infinite) :=
  ⟨zfcMisses_eq_independent, zfc_misses_not_re, zfc_misses_infinite, zfc_miss_seen_every_instant,
   zfc_not_completeForNever_turing, zfc_incomplete_turing, zfc_patch_misses⟩

end GodelQ.QualTuring

#print axioms GodelQ.QualTuring.qual_C104
#print axioms GodelQ.QualTuring.qual_C105
