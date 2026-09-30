/-
  Negative control for CG001-C-80 (proof id MP-CG001-QUESTIONING-DELAY-LEAN-NEG-001,
  expected KERNEL_REJECTED in the repository's status vocabulary).

  Claims that in the fact world the questioning of the universe is silent at
  fuel 0, as it is in HoTT (CG001-C-78).  Expected: rejected; with the judge
  judgeType the run reduces to some 1, not none.
-/
import QuestioningLean

open CG001.QuestioningLean

theorem wrong : question Type judgeType 0 = none := rfl
