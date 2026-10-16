{-# OPTIONS --safe --without-K #-}
module ConditionalLoeb where

-- Parameterised MLTT fragment. No arithmetisation, no claim that these
-- parameters have been instantiated by the syntax of full HoTT.
-- This file is NOT COMPILED in R031: Agda is absent from PATH.

data Empty : Set where

record Calculus : Set₁ where
  field
    Form : Set
    Der  : Form → Set
    arr  : Form → Form → Form
    box  : Form → Form

    mp : {A B : Form} → Der (arr A B) → Der A → Der B
    compose : {A B C : Form} → Der (arr A B) → Der (arr B C) → Der (arr A C)
    s-rule : {A B C : Form} → Der (arr A (arr B C)) → Der (arr A B) → Der (arr A C)

    -- Der denotes closed derivations in ONE fixed theory. This is not
    -- the unsound operation sending an arbitrary open assumption A to box A.
    nec : {A : Form} → Der A → Der (box A)
    distribution : {A B : Form} → Der (arr (box (arr A B)) (arr (box A) (box B)))
    introspection : {A : Form} → Der (arr (box A) (box (box A)))

module Theorem (C : Calculus) where
  open Calculus C

  loeb-transform :
    (G P : Form) →
    Der (arr G (arr (box G) P)) →
    Der (arr (arr (box G) P) G) →
    Der (arr (box P) P) →
    Der P
  loeb-transform G P forward backward reflection =
    mp h (nec (mp backward h))
    where
      u : Der (arr (box G) (box (arr (box G) P)))
      u = mp (distribution {A = G} {B = arr (box G) P}) (nec forward)

      v : Der (arr (box G) (arr (box (box G)) (box P)))
      v = compose u (distribution {A = box G} {B = P})

      l : Der (arr (box G) (box P))
      l = s-rule v (introspection {A = G})

      h : Der (arr (box G) P)
      h = compose l reflection

  no-bottom-reflection :
    (G bottom : Form) →
    (Der bottom → Empty) →
    Der (arr G (arr (box G) bottom)) →
    Der (arr (arr (box G) bottom) G) →
    Der (arr (box bottom) bottom) → Empty
  no-bottom-reflection G bottom consistent forward backward reflection =
    consistent (loeb-transform G bottom forward backward reflection)
