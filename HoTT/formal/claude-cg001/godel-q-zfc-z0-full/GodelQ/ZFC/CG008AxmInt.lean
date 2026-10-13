import GodelQ.ZFC.CG008AxmStep

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008AxmInt

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full GodelQ.CG008AxmStep

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! # 公理步的**内部化**

元层已证（`CG008AxmStep.lean`）：`sigma ∈ Sh.craig → 𝗭𝗙𝗖 ⊢ translate sigma`。

**内部化用 Foundation 的 `internalize_provability`**（`D1.lean:27`）：
`T ⊢ φ → Provable T (⌜φ⌝ : V)`。

取 `T := 𝗭𝗙𝗖`、`φ := translate sigma`，配合 `iT 0 ⌜sigma⌝ = ⌜translate sigma⌝`
（`iT_quote`），即得 **`sigma ∈ Sh.craig → TrProvable ⌜sigma⌝`**。

这是桥的一半：`provabilityPred Sh.craig sigma → TrProvable ⌜sigma⌝`。 -/

/-- **查实 1**：`iT 0 ⌜sigma⌝ = ⌜translate sigma⌝`（`iT_quote`）。 -/
example (sigma : ArithmeticSentence) :
    iT (0 : V) (⌜sigma⌝ : V) = ⌜(arithTrln.translate sigma : Semisentence ℒₛₑₜ 0)⌝ :=
  iT_quote (V := V) sigma

end GodelQ.CG008AxmInt
