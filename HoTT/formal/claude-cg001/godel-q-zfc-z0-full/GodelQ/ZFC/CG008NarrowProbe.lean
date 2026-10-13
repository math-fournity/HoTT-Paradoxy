import GodelQ.ZFC.CG008GapSharp
import GodelQ.ZFC.Z0PA

/-! # 探针（非收据）：窄命题的形状 -/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008NarrowProbe
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Z0Full GodelQ.Translate
variable {V : Type} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- 1. 𝗜𝚺₁ 的定义（缩写展开）
noncomputable example : ArithmeticTheory := 𝗜𝚺₁
#check @ISigma
#check @InductionOnPrenexHierarchy

-- 2. `interpret_theory` 给出的是什么（元层）
#check @DirectInterpretation.interpret_theory

-- 3. `internalize_provability` 的前提（元层）
#check @Bootstrapping.Arithmetic.internalize_provability

-- 4. 缺口需要的（V 内部）
example : Prop := ∀ {σ : ArithmeticSentence}, ℬ[<, ℒₒᵣ].Hierarchy 𝚺 1 σ →
    Provable 𝗜𝚺₁ (⌜σ⌝ : V) → Provable 𝗭𝗙𝗖 (⌜arithTrln.translate σ⌝ : V)

-- 5. 𝗭𝗙𝗖 的公理集是 Δ₁（缺口右侧要的）
#check @GodelQ.ZFCArith.zfc_delta1

end GodelQ.CG008NarrowProbe
