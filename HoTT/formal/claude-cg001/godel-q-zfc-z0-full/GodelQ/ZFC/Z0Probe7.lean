import GodelQ.ZFC.Z0Full
import GodelQ.ZFC.Z0PA
import GodelQ.ZFC.Z0Shadow

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open FFL.FirstOrder.Arithmetic.R0

namespace GodelQ.Z0Probe7

open Classical

/-- Test: is `Provable 𝗭𝗙𝗖 (⌜σ⌝ : V)` carrier-rewritable to `: ℕ` via TProvable.iff_provable? -/
example {V : Type} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
    (σ : SetTheorySentence)
    (h : Provable 𝗭𝗙𝗖 (⌜σ⌝ : V)) : Provable 𝗭𝗙𝗖 (⌜σ⌝ : ℕ) := by
  have e1 : 𝗭𝗙𝗖.internalize V ⊢ ⌜σ⌝ := (tprovable_tquote_iff_provable_quote (T := 𝗭𝗙𝗖)).mpr h
  have e2 : 𝗭𝗙𝗖.internalize ℕ ⊢ ⌜σ⌝ := e1
  exact (tprovable_tquote_iff_provable_quote (T := 𝗭𝗙𝗖)).mp e2

end GodelQ.Z0Probe7
