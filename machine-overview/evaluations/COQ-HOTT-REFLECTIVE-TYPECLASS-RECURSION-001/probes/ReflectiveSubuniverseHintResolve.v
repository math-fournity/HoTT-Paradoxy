From HoTT Require Import Basics Types Modalities.ReflectiveSubuniverse.

Section Candidate.
  Context (O : ReflectiveSubuniverse).
  Context {A B : Type} `{In O A} `{In O B}.
  Hint Resolve isequiv_O_inverts : typeclass_instances.
  Variable f : forall _ : A, B.

  Goal IsEquiv f.
    typeclasses eauto.
  Abort.
End Candidate.
