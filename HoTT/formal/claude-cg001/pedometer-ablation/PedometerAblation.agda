{-# OPTIONS --safe --cubical --guardedness #-}
{-
  The pedometer ablation (Claude, session 91a6cdaa, 2026-09-25).

  Why.  Reply 008 (section 5) and CN-028 (section 4.4) predicted that in a
  directed type theory, where going back is a new arrow rather than an
  inverse, a carried pedometer would count round trips, so the stop-at-+2
  process of C-47 would halt.  The user asked for a machine check with
  whatever systems and methods are available.  This file is the Cubical Agda
  part.  A Lean 4 cross-check of C-51 and a Rzk (simplicial HoTT) check of
  C-49 in the directed theory itself live in the sibling packages
  pedometer-ablation-lean and pedometer-ablation-rzk.

  proof id : MP-CG001-PEDOMETER-ABLATION-001
  claims   : CG001-C-49, CG001-C-50, CG001-C-51 (full statements in CLAIM.md)

  C-49 (HoTT; any type, any path, any family): every change carried along a
       path can be undone by carrying along another path.
       (a) advance forces retreat: if carrying along p raises a reading by k,
           carrying back along sym p lowers it by k;
       (b) monotone is invariant: a reading that no carrying ever lowers is
           never raised either (for any antisymmetric relation);
       (c) no two-way pedometer: walking a road and walking the same road
           back cannot both add one step;
       (d) no irreversible step: if the reading 0 occurs at the far end, no
           carrying along a path adds one to a natural-number reading; in
           particular no path in the universe from N to N acts as suc;
       (e) counting both legs of a round trip go, back forces back to differ
           from sym go, and makes sym go a walk that lowers the count.
  C-50 (HoTT; the escape "going back is a second, independent path"):
       (a) on the HIT with two points and two paths go, back, the family with
           fibre Z and sucZ along both paths counts: one round trip adds two
           (refl), and the stop-at-+2 search halts at fuel 1;
       (b) the price: the theory also supplies sym go, a walk from east to
           west along which the count goes from 0 to -1 (refl); the round trip
           is not refl, back is not sym go, and the type of places is not a
           set.
  C-51 (the directed model, set level): the free category on the graph
       west -go-> east -back-> west.
       (a) walks form a category (unit and associativity laws);
       (b) the pedometer (fibre N at each town, suc along each step) is a
           functor, and a covariant family in the 1-categorical sense
           (unique lifts);
       (c) every walk advances the pedometer by its length, so no walk lowers
           it and every nonempty walk strictly raises it; the round trip adds
           two (refl);
       (d) the stop-at-+2 search halts at fuel 1 (refl);
       (e) go has no inverse walk; the round trip is not the identity walk;
       (f) realised in the HIT of C-50, every directed walk carries the
           Z-pedometer exactly as the directed pedometer does; what the HIT
           adds are the reverse paths of C-50 (b).

  C-51 is a statement about a model (the intended categorical semantics of
  directed type theory: types as categories, covariant families as
  functors); it is not a theorem inside a directed type theory.
  Bridge labels (walker, road, pedometer, stop) prove no physical fact.
-}
module PedometerAblation where

open import Cubical.Foundations.Prelude
open import Cubical.Foundations.Transport using (subst⁻; subst⁻Subst; substSubst⁻; substComposite)
open import Cubical.Foundations.GroupoidLaws using (rCancel)
open import Cubical.Data.Sigma
open import Cubical.Data.Empty as ⊥ using (⊥)
open import Cubical.Data.Nat using (ℕ; zero; suc; _+_; snotz; znots)
open import Cubical.Data.Nat.Properties using (m+n≡n→m≡0; discreteℕ; +-suc)
open import Cubical.Data.Nat.Order using (_≤_; _<_; ≤-antisym)
open import Cubical.Data.Int using (ℤ; pos; negsuc; sucPathℤ; injPos; discreteℤ)
open import Cubical.Data.Maybe using (Maybe; nothing; just)
open import Cubical.Relation.Nullary using (¬_; Dec; yes; no)

private
  variable
    ℓ ℓ' ℓ'' : Level

------------------------------------------------------------------------
-- a stopping-time search with fuel: the first k <= fuel satisfying P
-- (as in PedometerHalting, C-47, plus a lemma for halting at fuel 1)

module Search {ℓ} (P : ℕ → Type ℓ) (dec : (k : ℕ) → Dec (P k)) where

  pick : (k : ℕ) → Dec (P k) → Maybe ℕ → Maybe ℕ
  pick k (yes _) _    = just k
  pick k (no _)  rest = rest

  scan : ℕ → ℕ → Maybe ℕ
  scan k zero       = pick k (dec k) nothing
  scan k (suc fuel) = pick k (dec k) (scan (suc k) fuel)

  run : ℕ → Maybe ℕ
  run fuel = scan 0 fuel

  haltsAtOne : ¬ P 0 → P 1 → run 1 ≡ just 1
  haltsAtOne n0 p1 = first (dec 0)
    where
    second : (d : Dec (P 1)) → pick 1 d nothing ≡ just 1
    second (yes _)  = refl
    second (no np1) = ⊥.rec (np1 p1)
    first : (d : Dec (P 0)) → pick 0 d (scan 1 0) ≡ just 1
    first (yes p0) = ⊥.rec (n0 p0)
    first (no _)   = second (dec 1)

------------------------------------------------------------------------
-- C-49  every carried change can be undone (any type, any family)

module _ {A : Type ℓ} (B : A → Type ℓ') where

  -- carrying there and back returns what was carried
  thereAndBack : {x y : A} (p : x ≡ y) (u : B x) → subst B (sym p) (subst B p u) ≡ u
  thereAndBack p u = subst⁻Subst B p u

  -- (a) advance forces retreat: along sym p the reading goes back down by k
  advanceForcesRetreat : (r : (x : A) → B x → ℕ) {x y : A} (p : x ≡ y) (u : B x) (k : ℕ)
    → r y (subst B p u) ≡ k + r x u
    → r y (subst B p u) ≡ k + r x (subst B (sym p) (subst B p u))
  advanceForcesRetreat r {x} p u k adv = adv ∙ cong (λ w → k + r x w) (sym (thereAndBack p u))

  -- (b) monotone is invariant, for any antisymmetric relation
  module Monotone {N : Type ℓ''} (_≼_ : N → N → Type ℓ'')
                  (antisym : {m n : N} → m ≼ n → n ≼ m → m ≡ n)
                  (r : (x : A) → B x → N) where

    NeverLowered : Type (ℓ-max (ℓ-max ℓ ℓ') ℓ'')
    NeverLowered = {x y : A} (p : x ≡ y) (u : B x) → r x u ≼ r y (subst B p u)

    NeverChanged : Type (ℓ-max (ℓ-max ℓ ℓ') ℓ'')
    NeverChanged = {x y : A} (p : x ≡ y) (u : B x) → r y (subst B p u) ≡ r x u

    monotoneIsInvariant : NeverLowered → NeverChanged
    monotoneIsInvariant mono {x} {y} p u = antisym down (mono p u)
      where
      down : r y (subst B p u) ≼ r x u
      down = subst (λ w → r y (subst B p u) ≼ r x w) (thereAndBack p u) (mono (sym p) (subst B p u))

  -- the natural-number instance: a pedometer that no walk lowers is never raised
  monotoneIsInvariantℕ : (r : (x : A) → B x → ℕ)
    → ({x y : A} (p : x ≡ y) (u : B x) → r x u ≤ r y (subst B p u))
    → {x y : A} (p : x ≡ y) (u : B x) → r y (subst B p u) ≡ r x u
  monotoneIsInvariantℕ r = Monotone.monotoneIsInvariant _≤_ ≤-antisym r

  noMonotoneAdvance : (r : (x : A) → B x → ℕ)
    → ({x y : A} (p : x ≡ y) (u : B x) → r x u ≤ r y (subst B p u))
    → {x y : A} (p : x ≡ y) (u : B x) → ¬ (r y (subst B p u) ≡ suc (r x u))
  noMonotoneAdvance r mono p u adv =
    snotz (m+n≡n→m≡0 {m = 1} (sym adv ∙ monotoneIsInvariantℕ r mono p u))

-- (c) walking a road and walking the same road back cannot both add one step
noTwoWayPedometer : {A : Type ℓ} {a b : A} (p : a ≡ b) (B : A → Type ℓ')
  (ra : B a → ℕ) (rb : B b → ℕ) (start : B a)
  → ¬ ( ((u : B a) → rb (subst B p u) ≡ suc (ra u))
      × ((v : B b) → ra (subst B (sym p) v) ≡ suc (rb v)) )
noTwoWayPedometer p B ra rb start (there , back) =
  snotz (m+n≡n→m≡0 {m = 2} (sym twice ∙ cong ra (thereAndBack B p start)))
  where
  twice : ra (subst B (sym p) (subst B p start)) ≡ 2 + ra start
  twice = back (subst B p start) ∙ cong suc (there start)

-- (d) no irreversible step: every state at the far end came from the near end
noIrreversibleStep : {A : Type ℓ} {a b : A} (p : a ≡ b) (B : A → Type ℓ')
  (ra : B a → ℕ) (rb : B b → ℕ) (v₀ : B b) → rb v₀ ≡ 0
  → ¬ ((u : B a) → rb (subst B p u) ≡ suc (ra u))
noIrreversibleStep p B ra rb v₀ z step =
  znots (sym z ∙ cong rb (sym (substSubst⁻ B p v₀)) ∙ step (subst⁻ B p v₀))

noSucPath : ¬ (Σ[ P ∈ ℕ ≡ ℕ ] ((n : ℕ) → transport P n ≡ suc n))
noSucPath (P , act) = noIrreversibleStep P (λ X → X) (λ n → n) (λ n → n) 0 refl act

-- (e) counting both legs of a round trip forces an anti-walk
countingForcesAntiWalk : {A : Type ℓ} {a b : A} (go : a ≡ b) (back : b ≡ a)
  (B : A → Type ℓ') (ra : B a → ℕ) (rb : B b → ℕ)
  → ((u : B a) → rb (subst B go u) ≡ suc (ra u))
  → ((v : B b) → ra (subst B back v) ≡ suc (rb v))
  → (B a → ¬ (back ≡ sym go))
    × ((v : B b) → rb v ≡ suc (ra (subst B (sym go) v)))
countingForcesAntiWalk go back B ra rb there backAdds =
    (λ start q → noTwoWayPedometer go B ra rb start
                   (there , λ v → cong (λ c → ra (subst B c v)) (sym q) ∙ backAdds v))
  , (λ v → cong rb (sym (substSubst⁻ B go v)) ∙ there (subst⁻ B go v))

------------------------------------------------------------------------
-- C-50  the escape: going back is a second, independent path

module Escape where

  data Places : Type where
    west east : Places
    go   : west ≡ east
    back : east ≡ west

  -- the pedometer as a reversible counter: fibre Z, one step up along both paths
  Ped : Places → Type
  Ped west     = ℤ
  Ped east     = ℤ
  Ped (go i)   = sucPathℤ i
  Ped (back i) = sucPathℤ i

  goAdds : subst Ped go (pos 0) ≡ pos 1
  goAdds = refl

  backAdds : subst Ped back (pos 1) ≡ pos 2
  backAdds = refl

  roundTrip : west ≡ west
  roundTrip = go ∙ back

  roundTripAddsTwo : subst Ped roundTrip (pos 0) ≡ pos 2
  roundTripAddsTwo = refl

  rounds : ℕ → west ≡ west
  rounds zero    = refl
  rounds (suc n) = rounds n ∙ roundTrip

  after : ℕ → ℤ
  after n = subst Ped (rounds n) (pos 0)

  Advanced : ℕ → Type
  Advanced n = after n ≡ pos 2

  decAdvanced : (n : ℕ) → Dec (Advanced n)
  decAdvanced n = discreteℤ (after n) (pos 2)

  run : ℕ → Maybe ℕ
  run = Search.run Advanced decAdvanced

  notAtStart : ¬ Advanced 0
  notAtStart adv = znots (injPos (sym (substRefl {B = Ped} {x = west} (pos 0)) ∙ adv))

  afterOne : Advanced 1
  afterOne = substComposite Ped refl roundTrip (pos 0)
           ∙ cong (subst Ped roundTrip) (substRefl {B = Ped} {x = west} (pos 0))
           ∙ roundTripAddsTwo

  halts : run 1 ≡ just 1
  halts = Search.haltsAtOne Advanced decAdvanced notAtStart afterOne

  -- (b) the price
  antiWalk : subst Ped (sym go) (pos 0) ≡ negsuc 0
  antiWalk = refl

  roundTripIsNotStaying : ¬ (roundTrip ≡ refl)
  roundTripIsNotStaying q =
    snotz (injPos (sym roundTripAddsTwo
                   ∙ cong (λ c → subst Ped c (pos 0)) q
                   ∙ substRefl {B = Ped} {x = west} (pos 0)))

  backIsNotTheReverse : ¬ (back ≡ sym go)
  backIsNotTheReverse q = roundTripIsNotStaying (cong (go ∙_) q ∙ rCancel go)

  placesAreNotASet : ¬ isSet Places
  placesAreNotASet s = roundTripIsNotStaying (s west west roundTrip refl)

------------------------------------------------------------------------
-- C-51  the directed model: the free category on west -> east -> west

module Directed where

  data Town : Type where
    west east : Town

  data Step : Town → Town → Type where
    go   : Step west east
    back : Step east west

  infixr 5 _then_ _++_

  data Walk : Town → Town → Type where
    stay   : {x : Town} → Walk x x
    _then_ : {x y z : Town} → Step x y → Walk y z → Walk x z

  _++_ : {x y z : Town} → Walk x y → Walk y z → Walk x z
  stay       ++ v = v
  (s then w) ++ v = s then (w ++ v)

  -- (a) the category laws (stay ++ w = w holds by definition)
  ++-stay : {x y : Town} (w : Walk x y) → w ++ stay ≡ w
  ++-stay stay       = refl
  ++-stay (s then w) = cong (s then_) (++-stay w)

  ++-assoc : {x y z t : Town} (u : Walk x y) (v : Walk y z) (w : Walk z t)
    → (u ++ v) ++ w ≡ u ++ (v ++ w)
  ++-assoc stay       v w = refl
  ++-assoc (s then u) v w = cong (s then_) (++-assoc u v w)

  length : {x y : Town} → Walk x y → ℕ
  length stay       = 0
  length (s then w) = suc (length w)

  -- (b) the pedometer: fibre N at each town, suc along each step
  carry : {x y : Town} → Walk x y → ℕ → ℕ
  carry stay       n = n
  carry (s then w) n = carry w (suc n)

  carryFunctor : {x y z : Town} (w : Walk x y) (v : Walk y z) (n : ℕ)
    → carry (w ++ v) n ≡ carry v (carry w n)
  carryFunctor stay       v n = refl
  carryFunctor (s then w) v n = carryFunctor w v (suc n)

  -- covariance, 1-categorically: each walk lifts uniquely from each value
  uniqueLift : {x y : Town} (w : Walk x y) (n : ℕ) → isContr (Σ[ m ∈ ℕ ] carry w n ≡ m)
  uniqueLift w n = isContrSingl (carry w n)

  -- (c) the pedometer adds the length of the walk
  carryIsLength : {x y : Town} (w : Walk x y) (n : ℕ) → carry w n ≡ length w + n
  carryIsLength stay       n = refl
  carryIsLength (s then w) n = carryIsLength w (suc n) ∙ +-suc (length w) n

  neverLowers : {x y : Town} (w : Walk x y) (n : ℕ) → n ≤ carry w n
  neverLowers w n = length w , sym (carryIsLength w n)

  everyStepRaises : {x y z : Town} (s : Step x y) (w : Walk y z) (n : ℕ) → n < carry (s then w) n
  everyStepRaises s w n = length w , sym (carryIsLength w (suc n))

  roundTrip : Walk west west
  roundTrip = go then back then stay

  roundTripAddsTwo : (n : ℕ) → carry roundTrip n ≡ 2 + n
  roundTripAddsTwo n = refl

  -- (d) the stop-at-+2 process halts
  rounds : ℕ → Walk west west
  rounds zero    = stay
  rounds (suc k) = rounds k ++ roundTrip

  after : ℕ → ℕ
  after k = carry (rounds k) 0

  Advanced : ℕ → Type
  Advanced k = after k ≡ 2

  run : ℕ → Maybe ℕ
  run = Search.run Advanced (λ k → discreteℕ (after k) 2)

  halts : run 1 ≡ just 1
  halts = refl

  -- (e) no inverses
  goHasNoInverse : ¬ (Σ[ w ∈ Walk east west ] (go then w) ≡ stay)
  goHasNoInverse (w , q) = snotz (cong length q)

  roundTripIsNotStaying : ¬ (roundTrip ≡ stay)
  roundTripIsNotStaying q = snotz (cong length q)

  -- (f) realised in the HIT of C-50, directed walks carry the Z-pedometer alike
  place : Town → Escape.Places
  place west = Escape.west
  place east = Escape.east

  realiseStep : {x y : Town} → Step x y → place x ≡ place y
  realiseStep go   = Escape.go
  realiseStep back = Escape.back

  realise : {x y : Town} → Walk x y → place x ≡ place y
  realise stay       = refl
  realise (s then w) = realiseStep s ∙ realise w

  start : (x : Town) → ℕ → Escape.Ped (place x)
  start west n = pos n
  start east n = pos n

  stepAgrees : {x y : Town} (s : Step x y) (n : ℕ)
    → subst Escape.Ped (realiseStep s) (start x n) ≡ start y (suc n)
  stepAgrees go   n = transportRefl (pos (suc n))
  stepAgrees back n = transportRefl (pos (suc n))

  realiseCarry : {x y : Town} (w : Walk x y) (n : ℕ)
    → subst Escape.Ped (realise w) (start x n) ≡ start y (carry w n)
  realiseCarry {x} stay n = substRefl {B = Escape.Ped} {x = place x} (start x n)
  realiseCarry (_then_ {x} s w) n =
      substComposite Escape.Ped (realiseStep s) (realise w) (start x n)
    ∙ cong (subst Escape.Ped (realise w)) (stepAgrees s n)
    ∙ realiseCarry w (suc n)
