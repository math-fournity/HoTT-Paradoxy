-- CG-009: the KEY identity for hAll's hAB.
--   A := iT 0 (free p)              (what ih gives)
--   B := free (imp domZero (iT 1 p)) = imp (x∈ω) (subst ?[^&0] (iT 1 (shift p)))
-- If A = subst ?[^&0] (iT 1 (shift p)), then B = (x∈ω) → A, so A → B is trivial.
import GodelQ.ZFC.HAllProof

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate

namespace GodelQ.HABKey
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **The key identity**: `iT 0 (free p) = subst ?[^&0] (iT 1 (shift p))`.
    LHS frees p's bound var 0 then translates; RHS translates (fvar-shifted) p then
    frees the outer bound variable. Both mean "the translation of p with its
    bound variable replaced by the free variable 0". -/
theorem iT_free_eq (p : V) (hp : IsSemiformula ℒₒᵣ 1 p) :
    iT (0 : V) (free (L := ℒₒᵣ) p) =
      subst ℒₛₑₜ ?[^&0] (iT (1 : V) (shift (L := ℒₒᵣ) p)) := by
  show iT (0 : V) (subst ℒₒᵣ (?[^&0] : V) (shift (L := ℒₒᵣ) p)) =
    subst ℒₛₑₜ (?[^&0] : V) (iT (1 : V) (shift (L := ℒₒᵣ) p))
  -- LHS: iT 0 of (bvar0 ↦ ^&0 substitution into shift p)
  -- RHS: bvar0 ↦ ^&0 substitution into the translation of shift p
  -- These agree because iT sends bvar z to the *bound* var of eqAtom (z+1), and
  -- the substitution ?[^&0] targets bvar 0 — need the iT/subst interaction at bvar 0.
  sorry

end GodelQ.HABKey
