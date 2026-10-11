import GodelQ.ZFC.CG008GapShape

/-!
# CG-008 · V 内部的逻辑砖块：`proof → provable`

## 动机

缺口的两半：
- **平凡的一半**：前提 `Provable 𝗭𝗙𝗖 ⌜translate τ⌝` 给出 `d : V` 与
  `Proof 𝗭𝗙𝗖 d ⌜translate τ⌝`；由 `provable` 的编码定义
  （`Basic.lean:556`：`provable T = ∃d, proof T d`）与 `proof` 的定义
  （`Basic.lean:552`：`proof T d φ = ∃s, insertDef s φ 0 ∧ derivationOf T d s`），
  **一步 ∃-引入**就得到「`provable 𝗭𝗙𝗖` 在 `⌜translate τ⌝` 处成立」。
- **不平凡的一半**：还要它在 `⌜translate (zfcTr τ)⌝` 处成立——
  结论句**换了**，不是同一个 φ。这一半需要内部化解释。

本文件把**平凡的一半**机器化。

## 治理

- Foundation 只读；本文件纯下游。
- 本文件不含任何未证标记，可进入收据。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008ProofToProvable

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full GodelQ.ZFCSetSigma1
  GodelQ.ZFCSetInternal GodelQ.CG008Reduce GodelQ.CG008SetAll GodelQ.CG008Raw
  GodelQ.CG008RawSigma1

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **查实 1**：`proof` 的编码定义（`Basic.lean:552`）是 `𝚫ᴬ₁.Semisentence 2`。 -/
noncomputable example : 𝚫ᴬ₁.Semisentence 2 := proof 𝗭𝗙𝗖

/-- **查实 2**：`provable` 的编码定义（`Basic.lean:556`）是 `𝚺ᴬ₁.Semisentence 1`。 -/
noncomputable example : 𝚺ᴬ₁.Semisentence 1 := provable 𝗭𝗙𝗖

/-- **查实 3**：`Provable` 的元层定义（`Basic.lean:541`）就是 `∃ d, Proof T d φ`。 -/
example (ψ : V) : Provable 𝗭𝗙𝗖 ψ ↔ ∃ d, Proof 𝗭𝗙𝗖 d ψ := Iff.rfl

/-- **主定理（平凡的一半）**：`Proof T d φ → Provable T φ`。

这是 `Provable` 的定义展开——多一个 `∃ d`。**不需要任何理论**，
因为见证 `d` 已经在手上。这正是「V 内部有一条推导」到
「V ⊨ `provable` 的见证存在」的那一步。 -/
theorem provable_of_proof {d ψ : V} (h : Proof 𝗭𝗙𝗖 d ψ) : Provable 𝗭𝗙𝗖 ψ :=
  ⟨d, h⟩

/-- **推论**：缺口的前提 `Provable 𝗭𝗙𝗖 ⌜translate τ⌝` 在**同一个句子**上
直接给出 `Provable`——这就是平凡的一半的完整形式。

**注意它不解决缺口**：缺口的结论句是 `⌜translate (zfcTr τ)⌝`，
与前提的 `⌜translate τ⌝` **不是同一个句子**。
两者相等需要内部化解释（见 `CG008GapShape.lean` 的六步链）。 -/
theorem trivially_half (τ : ArithmeticSentence)
    (h : Provable 𝗭𝗙𝗖 (⌜arithTrln.translate τ⌝ : V)) :
    Provable 𝗭𝗙𝗖 (⌜arithTrln.translate τ⌝ : V) := h

end GodelQ.CG008ProofToProvable
