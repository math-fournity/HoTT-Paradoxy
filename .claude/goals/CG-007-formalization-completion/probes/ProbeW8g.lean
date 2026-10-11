import GodelQ.ZFC.SeqTranslateFormula

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.SeqTranslate

open GodelQ.Translate GodelQ.ZFCArith

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- V 算术基础
example (n : V) : (0:V) < n + 3 := by
  have h := lt_add_self_add_one (0 : V) (n + 2)
  have e : n + 2 + 0 + 1 = n + 3 := by ring
  rwa [e] at h

example (n : V) : (1:V) < n + 3 := by
  have h := lt_add_self_add_one (1 : V) (n + 1)
  have e : n + 1 + 1 + 1 = n + 3 := by ring
  rwa [e] at h

example (n : V) : (2:V) < n + 3 := by
  have h := lt_add_self_add_one (2 : V) n
  have e : n + 2 + 1 = n + 3 := by ring
  rwa [e] at h

end GodelQ.SeqTranslate
