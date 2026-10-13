import GodelQ.ZFC.CG008GapSharp

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008FixpointProbe
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Z0Full GodelQ.Translate
variable {V : Type} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- Fixpoint.induction 的完整路径
#check @FFL.FirstOrder.Arithmetic.Fixpoint.Construction.induction

-- **关键发现**：`Derivation 𝗭𝗙𝗖` 的 construction **是** `StrongFinite`（自动合成）。
example : (Bootstrapping.Derivation.construction (V := V) 𝗭𝗙𝗖).StrongFinite := inferInstance

-- **因此 `Fixpoint.induction` 可用**——它是 **V 内部**的归纳原理：
-- 谓词 `P` 只需 `Σ₁-Predicate`，量化的是 V 的集合 `C : Set V`，
-- 前提是 `∀ x ∈ C, c.Fixpoint v x ∧ P x → c.Φ v C x → P x`。
-- **这正是「在 𝗜𝚺₁ 内对 `derivation 𝗭𝗙𝗖` 做归纳」所需的机器**——
-- `CG008InternalInduction.lean` 曾记「Foundation 无内部版」，**这条更正它**。

-- 归纳的**目标形状**（缺口的最窄形式，此处只固定类型）：
example : Prop :=
  ∀ {σ : ArithmeticSentence}, ℬ[<, ℒₒᵣ].Hierarchy 𝚺 1 σ →
    Provable 𝗜𝚺₁ (⌜σ⌝ : V) → Provable 𝗭𝗙𝗖 (⌜arithTrln.translate σ⌝ : V)

-- **本探针到此为止**：归纳原理**可用**，但归纳步要逐条处理
-- `Derivation.blueprint` 的十种规则（见 `Basic.lean:412`），
-- 其中九种与 `T` 无关、`axm` 步要 `T.Δ₁Class`——
-- 而把 `𝗜𝚺₁` 的公理经 `arithTrln` 送到 `𝗭𝗙𝗖` 的证明码，
-- 正是 `PAModel.lean` 的模型论论证要**在 V 内**重做的那一步。
-- **所以缺口没变，但「用什么机器」现在有了答案。**

end GodelQ.CG008FixpointProbe
