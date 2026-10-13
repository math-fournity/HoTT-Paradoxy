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

/-- `translate` fixes `(replicate k ⊤).conj` in any fvar domain. -/
lemma translate_conj_top' {ξ : Type*} (k : ℕ) :
    arithTrln.translate ((List.replicate k (⊤ : Semiformula ℒₒᵣ ξ 0)).conj) =
      (List.replicate k (⊤ : Semiformula ℒₛₑₜ ξ 0)).conj := by
  induction k with
  | zero => simp
  | succ k ih => simp [List.replicate_succ, ih]

/-- **`translate` commutes with `padding`** (any fvar domain, layer 0). -/
lemma translate_padding {ξ : Type*} (σ : Semiformula ℒₒᵣ ξ 0) (s : ℕ) :
    arithTrln.translate (σ.padding s) = (arithTrln.translate σ).padding s := by
  rw [Semiformula.padding, Semiformula.padding]
  rw [LogicalConnective.HomClass.map_and, translate_conj_top' (ξ := ξ) s]

/-- **`hRoot`** (for quoted Craig axioms): `p = ⌜φ⌝` with `φ ∈ Sh.craig`.
    Roadmap (all pieces proven or available):
    1. unpack φ = σ.padding s with σ ∈ Sh;
    2. `iT_quote` (Semisentence view) + `translate_padding` (generalized to any fvar domain)
       give `iT 0 ⌜σ.padding s⌝ = ⌜(translate σ).padding s⌝`;
    3. `Sh_provable_iff` + `σ ∈ Sh` gives `𝗭𝗙𝗖 ⊢ translate σ`;
    4. `Entailment.padding_iff` gives `𝗭𝗙𝗖 ⊢ (translate σ).padding s`;
    5. `provable_iff_provable` converts back.
    Remaining friction: the `Provable.{u_1,0}` vs `Provable.{0,_}` universe mismatch
    and the Sentence/Semiproposition coercion at step 5 — pure API plumbing. -/
theorem hRoot_quoted {φ : Sentence ℒₒᵣ} (hφ : φ ∈ Sh.craig) :
    Provable 𝗭𝗙𝗖 (iT (0 : V) (⌜φ⌝ : V)) := by
  sorry

/-- **`hRoot`**: Craig axioms translate to 𝗭𝗙𝗖-provable sentences. -/
theorem hRoot_uncond {p : V} (hp : p ∈ Sh.craig.Δ₁Class) :
    Provable 𝗭𝗙𝗖 (iT (0 : V) p) := by
  sorry

end GodelQ.HRoot

#print axioms GodelQ.HRoot.translate_padding
#print axioms GodelQ.HRoot.hRoot_uncond
