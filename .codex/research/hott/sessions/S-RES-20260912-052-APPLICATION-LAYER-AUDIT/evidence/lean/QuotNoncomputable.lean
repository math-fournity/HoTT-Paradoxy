-- N10 probe A9: the noncomputable fence.  A consumer that needs classical
-- choice is rejected by the evaluator rather than delivered.

noncomputable def pickBool : Bool := Classical.choice (⟨true⟩ : Nonempty Bool)

-- Expected: the evaluator refuses to compile a noncomputable definition.
#eval pickBool
