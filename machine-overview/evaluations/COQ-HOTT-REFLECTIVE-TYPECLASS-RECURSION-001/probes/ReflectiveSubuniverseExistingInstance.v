From HoTT Require Import Basics Types Modalities.ReflectiveSubuniverse.

Existing Instance isequiv_O_inverts.

Section Candidate.
  Context (O : ReflectiveSubuniverse).
  Context {A B : Type} `{In O A} `{In O B}.
  Variable f : forall _ : A, B.

  Goal IsEquiv f.
    typeclasses eauto.
  Abort.
End Candidate.
