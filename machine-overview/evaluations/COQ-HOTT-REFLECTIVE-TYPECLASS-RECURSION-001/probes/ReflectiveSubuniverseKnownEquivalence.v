From HoTT Require Import Basics Types Modalities.ReflectiveSubuniverse.

Existing Instance isequiv_O_inverts.

Section PositiveControl.
  Context (O : ReflectiveSubuniverse).
  Context {A : Type} `{In O A}.

  Goal IsEquiv (fun x : A => x).
    typeclasses eauto.
  Qed.
End PositiveControl.
