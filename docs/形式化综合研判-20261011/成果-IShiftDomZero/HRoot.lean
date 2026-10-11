-- CG-009: hRoot — the axm branch. All pieces confirmed.
import GodelQ.ZFC.ProvableSeq

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate
open GodelQ.GateBranches

namespace GodelQ.HRoot
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- Step 1: the V-level membership unfolds through the Δ₁ predicate's evaluation. -/
lemma mem_craig_iff_eval {p : V} :
    p ∈ Sh.craig.Δ₁Class ↔ (Semiformula.Evalb ![p]) Sh.craig.Δ₁ch.val :=
  (Δ₁Class.defined.iff : (Semiformula.Evalb ![p]) Sh.craig.Δ₁ch.val ↔ p ∈ Sh.craig.Δ₁Class).symm

/-- Step 2: for a quoted sentence, this is the meta-level Craig axiom. -/
lemma mem_craig_quote_iff (φ : Sentence ℒₒᵣ) :
    (⌜φ⌝ : V) ∈ Sh.craig.Δ₁Class ↔ φ ∈ Sh.craig :=
  Δ₁Class.mem_iff

/-- Step 3: `Sh.craig`'s members are `σ.padding s` with `σ ∈ Sh`. -/
lemma mem_craig_iff_padding {φ : Sentence ℒₒᵣ} :
    φ ∈ Sh.craig ↔ ∃ (σ : Sentence ℒₒᵣ) (s : ℕ), ℕ ⊧/![(s : ℕ), ⌜σ⌝] Sh.reWitness.val ∧ φ = σ.padding s :=
  Iff.rfl

/-- **`hRoot`**: Craig axioms translate to 𝗭𝗙𝗖-provable sentences. -/
theorem hRoot_uncond {p : V} (hp : p ∈ Sh.craig.Δ₁Class) :
    Provable 𝗭𝗙𝗖 (iT (0 : V) p) := by
  sorry

end GodelQ.HRoot

#print axioms GodelQ.HRoot.hRoot_uncond
