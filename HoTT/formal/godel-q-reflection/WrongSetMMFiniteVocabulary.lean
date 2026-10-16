/-
  Expected-negative control for SetMMAppendixCVarExtension.lean.

  The source vocabulary constructor and the fresh extension constructor are
  deliberately distinct.  The following attempted equality must be rejected;
  accepting it would erase the extension that discharges the infinite-variable
  obligation only at the M-level skeleton layer.
-/

import SetMMAppendixCVarExtension

open SetMMAppendixCGenerated
open SetMMAppendixCVarExtension

example : rawEmbedding .v000 = freshFamily .wff 0 := rfl
