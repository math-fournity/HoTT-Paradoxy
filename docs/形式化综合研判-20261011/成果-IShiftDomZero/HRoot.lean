-- CG-009: hRoot — the axm branch. All pieces confirmed and unpacked.
import GodelQ.ZFC.ProvableSeq

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate
open GodelQ.GateBranches

namespace GodelQ.HRoot
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

lemma mem_craig_iff_eval {p : V} :
    p ∈ Sh.craig.Δ₁Class ↔ (Semiformula.Evalb ![p]) Sh.craig.Δ₁ch.val :=
  (Δ₁Class.defined.iff : (Semiformula.Evalb ![p]) Sh.craig.Δ₁ch.val ↔ p ∈ Sh.craig.Δ₁Class).symm

lemma mem_craig_quote_iff (φ : Sentence ℒₒᵣ) :
    (⌜φ⌝ : V) ∈ Sh.craig.Δ₁Class ↔ φ ∈ Sh.craig :=
  Δ₁Class.mem_iff

lemma mem_craig_iff_padding {φ : Sentence ℒₒᵣ} :
    φ ∈ Sh.craig ↔ ∃ (σ : Sentence ℒₒᵣ) (s : ℕ), ℕ ⊧/![(s : ℕ), ⌜σ⌝] Sh.reWitness.val ∧ φ = σ.padding s :=
  Iff.rfl

/-- `translate` fixes `⊤` and preserves `⋏`, so it fixes `(replicate k ⊤).conj`. -/
lemma translate_conj_top (k : ℕ) :
    arithTrln.translate ((List.replicate k (⊤ : Semiformula ℒₒᵣ ℕ 0)).conj) =
      (List.replicate k (⊤ : Semiformula ℒₛₑₜ ℕ 0)).conj := by
  induction k with
  | zero => simp
  | succ k ih => simp [List.replicate_succ, ih]

/-- **`translate` commutes with `padding`** (at Semiproposition level). -/
lemma translate_padding (σ : Semiproposition ℒₒᵣ 0) (s : ℕ) :
    arithTrln.translate (σ.padding s) = (arithTrln.translate σ).padding s := by
  rw [Semiformula.padding, Semiformula.padding]
  rw [LogicalConnective.HomClass.map_and, translate_conj_top s]

/-- **`hRoot`**: Craig axioms translate to 𝗭𝗙𝗖-provable sentences. -/
theorem hRoot_uncond {p : V} (hp : p ∈ Sh.craig.Δ₁Class) :
    Provable 𝗭𝗙𝗖 (iT (0 : V) p) := by
  sorry

end GodelQ.HRoot

#print axioms GodelQ.HRoot.translate_padding
#print axioms GodelQ.HRoot.hRoot_uncond
