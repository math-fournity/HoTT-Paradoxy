import GodelQ.ZFC.ShCraigElimSetup
/-!
裁决探针 3（**不是收据**：定 `axm` 支的形状）。

第一探针已定：`p ∈ (Sh.craig).Δ₁Class ↔ Theory.IsCraigAxiom (T := Sh) p`（`defined (T := Sh)`），
特征式是 `Sh.reWitness`；`(Sh.craig).Δ₁ch = Sh.craigCh` 是 `rfl`。
`axm` 支要的是 `p ∈ (Sh.craig : Theory ℒₒᵣ)`。Foundation 有现成引理把两者接起来（**ℕ 层**）：
`Δ₁Class.mem_iff`：`(⌜φ⌝ : V) ∈ T.Δ₁Class ↔ φ ∈ T`。
-/
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup

namespace GodelQ.ProbeAdjudicateCraig3

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- 现成件：V 层的 Δ₁Class.mem_iff
#check @Δ₁Class.mem_iff
#check @Theory.IsCraigAxiom.defined

-- axm 支义务的精确形状（用现成接口把它写成一句）
example (σ : Sentence ℒₒᵣ) (h : (⌜σ⌝ : V) ∈ (Sh.craig).Δ₁Class) : σ ∈ Sh.craig :=
  (Δ₁Class.mem_iff (V := V)).mp h

-- 反过来：这是 `isCraigAxiom_quote_iff` 的对照，说明 Δ₁Class 就是「引号化的理论成员」
example (σ : Sentence ℒₒᵣ) (h : σ ∈ Sh.craig) : (⌜σ⌝ : V) ∈ (Sh.craig).Δ₁Class :=
  (Δ₁Class.mem_iff (V := V)).mpr h

end GodelQ.ProbeAdjudicateCraig3
