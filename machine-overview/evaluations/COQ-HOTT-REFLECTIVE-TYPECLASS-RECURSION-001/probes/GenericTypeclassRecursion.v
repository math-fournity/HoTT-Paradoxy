Inductive N : Type := z | s : N -> N.

Class P (n : N) : Prop := p_intro {}.

Axiom step : forall n, P (s n) -> P n.

#[export] Hint Resolve step : typeclass_instances.

Goal P z.
  typeclasses eauto.
Abort.
