Require Import Inconsistency.

Definition regular_replacement_contradiction : False := Unnamed_thm.

Print Assumptions contradiction.
Print Assumptions regular_replacement_contradiction.

Require Import FibRepl.

Check Fib_repl.
Check repl_ind'.
Check repl_rec'.
Check repl_f_compose.
Check RFib_DFib.
Check RFib_Trans.
Check TransFib_HFib.
Check repl_J.

Print Assumptions Fib_repl.
Print Assumptions repl_ind'.
Print Assumptions repl_rec'.
Print Assumptions repl_f_compose.
Print Assumptions RFib_DFib.
Print Assumptions RFib_Trans.
Print Assumptions TransFib_HFib.
Print Assumptions repl_J.
