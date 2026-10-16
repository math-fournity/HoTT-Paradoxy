-- CG-009: the KEY identity for hAll's hAB.
--   A := iT 0 (free p)              (what ih gives)
--   B := free (imp domZero (iT 1 p)) = imp (x∈ω) (subst ?[^&0] (iT 1 (shift p)))
-- If A = subst ?[^&0] (iT 1 (shift p)), then B = (x∈ω) → A, so A → B is trivial.
import GodelQ.ZFC.HAllProof
import GodelQ.ZFC.ITSubstOpen9

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
  -- 这是 `iT_subst_open` 的 **m = 0 实例**（`QvecVOr 0 = QvecV 0 = ?[^&0]`）：
  --   iT 0 (subst ℒₒᵣ (QvecVOr 0) q) = subst ℒₛₑₜ (QvecV 0) (iT (0+1) q),  q : 层 1
  have h1 : IsSemiformula ℒₒᵣ ((0 : V) + 1) (shift (L := ℒₒᵣ) p) := by
    rw [show (0 : V) + 1 = 1 from _root_.zero_add 1]
    exact IsSemiformula.shift hp
  have h := GodelQ.ITSubstOpen9.iT_subst_open (V := V) 0 (shift (L := ℒₒᵣ) p) h1
  rw [GodelQ.QvecVDefs.QvecVOr_zero, GodelQ.QvecVDefs.QvecV_zero] at h
  rw [show (0 : V) + 1 = 1 from _root_.zero_add 1] at h
  exact h

end GodelQ.HABKey

#print axioms GodelQ.HABKey.iT_free_eq
