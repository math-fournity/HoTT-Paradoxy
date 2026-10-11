import GodelQ.ZFC.SeqTranslateFormula

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.SeqTranslate

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

lemma two_lt_three_add (n : V) : (2:V) < 3 + n := by
  have h := lt_add_self_add_one (2 : V) n
  have e : n + 2 + 1 = 3 + n := by ring
  rwa [e] at h

example (n : V) : (2:V) < 2 + 1 + n := by
  simpa [show (3:V) = 2 + 1 by norm_num, add_assoc] using two_lt_three_add n

example (n : V) : (1:V) < 1 + 1 + 1 + n := by
  have h := lt_add_self_add_one (1 : V) (n + 1)
  have e : (n + 1) + 1 + 1 = 1 + 1 + 1 + n := by ring
  rwa [e] at h

end GodelQ.SeqTranslate
