import GodelQ.ZFC.Z0Full

/-!
# CG-007 · W8：唯一的阻塞引理（未证，不作为收据源）

`Z0Full.lean` 证明了：除了 Hilbert–Bernays 可导性条件 D3 之外，Z0 的完整形式
`𝗭𝗙𝗖 ⊬ (𝗭𝗙𝗼.consistent)ᵗ` 的全部前提都已具备。本文件把 D3 逐字写成一条 Lean 命题。

它带 `sorry`，因此**不是**任何运行收据的编译源（`zfc_lean_check.py` 会拒绝 `sorry`）；
它存在的目的是把“还差什么”固定成一条可以交给下一个工作单元、也可以交给外部复核的精确命题。

内容见命题的 docstring。`Z0Full.zfc_z0_full_of_D3_internalize` 表明：这条引理一旦成立，
完整形式立即随之成立。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate

namespace GodelQ.Z0Blocked

/-- **阻塞引理（D3 的唯一实质内容）**：在 𝗜𝚺₁ 的每个模型 V 中，
`𝗭𝗙𝗖 ⊢ ⌜σᵗ⌝ → 𝗭𝗙𝗖 ⊢ ⌜(zfcTr σ)ᵗ⌝`，即“𝗭𝗙𝗖 证明了 σ 的翻译，就也能证明
‘𝗭𝗙𝗖 证明 σ 的翻译’这句话的翻译”。

Foundation 的 `of_provability`（`LK/Interpretation.lean:443`）用完备性定理**语义地**证明
`U ⊢ σ → T ⊢ π.translate σ`；它不经过一条可搬进 𝗜𝚺₁ 的语法证明翻译。本文件没有证明这条引理。
它是 `zfcTr.HBL3`（D3）的唯一实质内容；`zfc_z0_full_of_D3_internalize` 表明它一旦成立，
Z0 的完整形式 `𝗭𝗙𝗖 ⊬ (𝗭𝗙𝗖.consistent)ᵗ` 立即随之成立。 -/
theorem zfcTr_D3_internalize {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
    (τ : ArithmeticSentence)
    (h : Provable 𝗭𝗙𝗖 (⌜arithTrln.translate τ⌝ : V)) :
    Provable 𝗭𝗙𝗖 (⌜arithTrln.translate (zfcTr τ)⌝ : V) := by
  sorry

end GodelQ.Z0Blocked
