import GodelQ.ZFC.SeqTranslateFormula

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.SeqTranslate

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

example (n : V) : (1:V) ≤ n + 1 := by
  apply lt_succ_iff_le.mp
  have h := lt_add_self_add_one (1 : V) n
  have e : n + 1 + 1 = (n + 1) + 1 := by ring
  rwa [e] at h

example {z n : V} (h : z < n) : z + 1 < n + 1 := by
  have h' := add_lt_add_right h 1
  -- 看它给什么
  have e : (1 : V) + z = z + 1 := by ring
  have e2 : (1 : V) + n = n + 1 := by ring
  rwa [e, e2] at h'

example {z n : V} (h : z < n) : z + 1 < n + 1 := by
  have h' := add_lt_add_left h 1
  have e : (1 : V) + z = z + 1 := by ring
  have e2 : (1 : V) + n = n + 1 := by ring
  rwa [e, e2] at h'

end GodelQ.SeqTranslate
