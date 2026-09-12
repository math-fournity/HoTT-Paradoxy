/- Intentionally expected tactic failure, not an unfinished proof claim.
   R024 could not run Lean; see TOOLCHAIN_STATUS.json. -/
import Lean
axiom unknownProp : Prop
example : unknownProp := by
  classical
  decide
