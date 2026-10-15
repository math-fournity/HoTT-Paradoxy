import GodelQ.ZFC.Z0OmegaQuestion

/-!
# 命题对照：CG001-C-427（Z0 作为具体的 ω 追问）

* (1) Z0 的程序停机，当且仅当 𝗭𝗙𝗖 证明 ⊥；(2) Z0 这一 ω 追问完成，当且仅当 𝗭𝗙𝗖 证明 ⊥；
* (3) Z0 永不落定（元层，Foundation 的 `zfc_consistent`）；
* (4) 𝗭𝗙𝗖 每一刻都确认“到第 k 步还没找到矛盾”；
* (5) Foundation 的一致性句在 ℕ 中为真，恰好当 Z0 永不落定；
* (6) 𝗭𝗙𝗖 证明不了这句话的翻译（C-417，导入）；
* (7) P_fin 在 Z0 上被否定；(8) 由 Z0 驱动的哥德尔–芝诺跑者到达；
* (9) 同一个类型 `OmegaQuestion` 里，芝诺与 Z0 都永不落定（C-93 的图式，两个具体实例）。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping SetTheory
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.Z0Omega

open GodelQ GodelQ.ZFCZ0 GodelQ.ZFCEff GodelQ.ZFCArith

/-- CG001-C-427：Z0 作为具体的 ω 追问。 -/
theorem qual_C427 :
    (Done z0Code ↔ 𝗭𝗙𝗖 ⊢ (⊥ : Sentence ℒₛₑₜ)) ∧
    (z0Q.Done ↔ 𝗭𝗙𝗖 ⊢ (⊥ : Sentence ℒₛₑₜ)) ∧
    z0Q.Never ∧
    (∀ k, zfcEffective.provesNotYet z0Code k) ∧
    ((𝗭𝗙𝗖.consistent : ArithmeticSentence).Evalb (M := ℕ) ![] ↔ z0Q.Never) ∧
    (𝗭𝗙𝗖 ⊬ arithTrln.translate (𝗭𝗙𝗖.consistent : ArithmeticSentence)) ∧
    (∀ FormalDone : Prop, FormalDone → ¬ (FormalDone → z0Q.Done)) ∧
    Arrives z0Code ∧
    (zenoQ.Never ∧ z0Q.Never) :=
  ⟨z0Code_done_iff, z0Q_done_iff, z0Q_never, zfc_confirms_every_stage,
    consistent_true_iff_z0_never, GodelQ.SetNum.zfc_z0_unconditional,
    fun F hF => z0Q.P_fin_refuted z0Q_never F hF, z0_runner_arrives, ⟨zenoQ_never, z0Q_never⟩⟩

end GodelQ.Z0Omega

#print axioms GodelQ.Z0Omega.qual_C427
