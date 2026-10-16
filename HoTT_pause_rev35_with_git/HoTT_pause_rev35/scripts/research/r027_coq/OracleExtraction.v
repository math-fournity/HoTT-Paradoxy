(* Ordinary Rocq/Coq extraction probe, NOT native HoTT verification.
   H is not instantiated; the test is solely for a computational axiom without code. *)
From Coq Require Import Extraction.
Axiom oracle_halt : nat -> nat -> bool.
Definition chi (p x : nat) : bool := oracle_halt p x.
Definition safe (_ _ : nat) : bool := false.
Eval cbv in (chi 0 0).
Extraction Language OCaml.
Extraction "artifacts/r027/coq_safe.ml" safe.
Extraction "artifacts/r027/coq_chi.ml" chi.
