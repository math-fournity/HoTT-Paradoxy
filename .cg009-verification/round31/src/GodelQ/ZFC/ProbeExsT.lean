import GodelQ.ZFC.GateBranches
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full

namespace GodelQ.ProbeExsT
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- Q: in a valid derivation d of sequent `insert (substs1 t p) s`, does `s` being a
-- layer-0 formula set force `t` to be a CLOSED term (no free variables)?
-- A closed term's value is a numeral, hence in ω.
-- Probe: state what we'd need. If Lean accepts it, it's a plausible (B) route.
example (s p t : V) (hs : IsFormulaSet (L := ℒₒᵣ) s)
    (d : V)
  (hd : DerivationOf (L := ℒₒᵣ) Sh.craig d (insert (substs1 (L := ℒₒᵣ) t p) s)) :
    -- t's free variables are all in ω (or: t is closed)
    True := by
  trivial

end GodelQ.ProbeExsT
