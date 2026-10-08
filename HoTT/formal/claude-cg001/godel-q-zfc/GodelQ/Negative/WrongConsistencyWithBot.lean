import GodelQ.ZFC.Effective

/-!
# 负控制 NEG-CONSISTENCY：一致性字段不能省

把 `zfcEffective` 的一致性证明原样用于 `insert ⊥ 𝗭𝗙𝗖`：`Entailment.Consistent` 实例找不到（这个理论
确实不一致）。预期：在一致性实例处被拒（细化阶段）。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory
open GodelQ.ZFCNum GodelQ.ZFCArith GodelQ.ZFCEff

example (e : GodelQ.Process)
    (h1 : (insert ⊥ 𝗭𝗙𝗖 : SetTheory) ⊢ haltsS ΦH (Encodable.encode e))
    (h2 : (insert ⊥ 𝗭𝗙𝗖 : SetTheory) ⊢ neverS ΦH (Encodable.encode e)) : False := by
  have h2' : (insert ⊥ 𝗭𝗙𝗖 : SetTheory) ⊢ ∼ haltsS ΦH (Encodable.encode e) := h2
  apply Entailment.Consistent.not_bot (𝓢 := (insert ⊥ 𝗭𝗙𝗖 : SetTheory))
  cl_prover [h1, h2']
