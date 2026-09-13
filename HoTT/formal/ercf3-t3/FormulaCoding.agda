module FormulaCoding where

open import Agda.Builtin.Nat
open import Agda.Builtin.Equality
open import Agda.Builtin.Bool using (Bool; true; false)
open import Agda.Builtin.List using (List; []; _∷_)
open import ObjectSyntax
open import DiagonalCore
import StreamingParser as SP
import BitCoding as BC

open SP using (_++_; unary; bits)
open BC using (LEN; codeBits; unbits; _≤_; z≤n; s≤s; ≤-refl; ≤-suc; ≤-trans)

-- T3 twentieth pulse (bounded): the *formula layer* of the repaired coding.
--
-- `StreamingParser` (C-173-C-176) closed the repair obligation for `Tm`.  The
-- diagonal machinery, however, codes *formulas* (`⌜ φ ⌝`), so the same
-- obligation has to be discharged one level up.  This module does that by
-- reusing the term-level parser as a black box: a formula node is decoded here,
-- but its `Tm` children are handed to `SP.run` with a fuel read off the very
-- bit list that is still available.
--
--   C-177  the formula symbol layer (`bitsF`/`STEPS`: two tag bits for
--          `=f`/`bot`/`=>f`/`all`, one unary binder index for `all`), and a
--          *streaming* parser (`run`) whose round trip is exact in the
--          iteration count;
--   C-178  the `Tm` children of `=f` are parsed by the term-level parser
--          (`tmFrom`), whose fuel is the length of the remaining bit list;
--   C-179  length bookkeeping: `STEPS φ ≤ LEN (bitsF φ)`, so the repaired
--          formula code `codeF'` can again be its own fuel;
--   C-180  the repaired formula coder `codeF'` with a total decoder `decF` and
--          the round trip `decF (codeF' φ) ≡ φ`, hence injectivity.
--
-- ERCF-3 itself stays `GATED`: nothing here touches the proof predicate `P`,
-- reflection or the diagonal fixed point, and no historical pulse file (and no
-- earlier module of this chain) is modified.

------------------------------------------------------------------------
-- C-177: the formula symbol layer.

bitsF : Fml → List Bool
bitsF (_=f_ t u) = false ∷ false ∷ (bits t ++ bits u)
bitsF bot = false ∷ true ∷ []
bitsF (φ =>f ψ) = true ∷ false ∷ (bitsF φ ++ bitsF ψ)
bitsF (all n φ) = true ∷ true ∷ (unary n ++ bitsF φ)

-- Number of parser iterations needed to read one formula node, counting one
-- iteration per tag bit, per binder-index digit and per term child.
STEPS : Fml → Nat
STEPS (_=f_ t u) = suc (suc (suc zero))
STEPS bot = suc (suc zero)
STEPS (φ =>f ψ) = suc (suc (STEPS φ + STEPS ψ))
STEPS (all n φ) = suc (suc (suc (n + STEPS φ)))

------------------------------------------------------------------------
-- Pending frames, control state and results.

data Slot : Set where
  wantImp : Slot
  haveImp : Fml → Slot
  wantAll : Nat → Slot

data Stack : Set where
  ε : Stack
  _▷_ : Slot → Stack → Stack

infixr 5 _▷_

data Mode : Set where
  wantFml : Stack → Mode
  tag2 : Bool → Stack → Mode
  index : Nat → Stack → Mode
  eqRight : Tm → Stack → Mode

data Verdict : Set where
  finish : Fml → Verdict
  next : Mode → Verdict

record Result : Set where
  constructor res
  field rVal : Fml
        rBits : List Bool

open Result

-- Completing `φ` in the context `stk`.
close : Fml → Stack → Verdict
close φ ε = finish φ
close φ (wantImp ▷ stk) = next (wantFml (haveImp φ ▷ stk))
close φ (haveImp l ▷ stk) = close (l =>f φ) stk
close φ (wantAll n ▷ stk) = close (all n φ) stk

-- The term child of `=f` is read by the term-level parser: its fuel is the
-- length of the bit list that is still present, which is exactly what the
-- term-level round trip needs (C-178).
tmFrom : List Bool → SP.Result
tmFrom bs = SP.run (LEN bs) bs (SP.startSub SP.ε)

-- One iteration consumes one unit of fuel.  `zero` and `[]` are the default
-- branches C-168 requires.
--
-- The *mode* is the first argument on purpose: it is always a constructor, so
-- the clause tree can be decided without knowing the bit list.  With the bit
-- list first, the `eqRight` step (whose bits are a stuck `bits u ++ rest`)
-- would not reduce definitionally, which would make the round trip unprovable
-- for the reason recorded in `LESSONS` #96.
mutual
  run : Mode → Nat → List Bool → Result
  run (wantFml stk) (suc f) (true ∷ rest) = run (tag2 true stk) f rest
  run (wantFml stk) (suc f) (false ∷ rest) = run (tag2 false stk) f rest
  run (tag2 false stk) (suc f) (true ∷ rest) = resume (close bot stk) rest f
  run (tag2 false stk) (suc f) (false ∷ rest) =
    run (eqRight (SP.Result.rTerm (tmFrom rest)) stk) f (SP.Result.rBits (tmFrom rest))
  run (eqRight t stk) (suc f) rest =
    resume (close (t =f SP.Result.rTerm (tmFrom rest)) stk) (SP.Result.rBits (tmFrom rest)) f
  run (tag2 true stk) (suc f) (false ∷ rest) = run (wantFml (wantImp ▷ stk)) f rest
  run (tag2 true stk) (suc f) (true ∷ rest) = run (index 0 stk) f rest
  run (index n stk) (suc f) (true ∷ rest) = run (index (suc n) stk) f rest
  run (index n stk) (suc f) (false ∷ rest) = run (wantFml (wantAll n ▷ stk)) f rest
  run m zero bs = res bot bs
  run m (suc f) [] = res bot []

  resume : Verdict → List Bool → Nat → Result
  resume (finish φ) rest f = res φ rest
  resume (next m) rest f = run m f rest

open import CodingRepair
open Σ'

------------------------------------------------------------------------
-- C-178: the term children of `=f` are read by the term-level parser.

tmFrom-run : (t : Tm) (rest : List Bool) → tmFrom (bits t ++ rest) ≡ SP.res t rest
tmFrom-run t rest
  rewrite SP.LEN-++ (bits t) rest
        | SP.bits-length t = SP.parse-run t SP.ε rest (LEN rest)

------------------------------------------------------------------------
-- C-177 (reader side): the binder index of `all`.

index-run :
  (m k : Nat) (stk : Stack) (rest : List Bool) (f : Nat)
  → run (index k stk) (suc (m + f)) (unary m ++ rest)
  ≡ run (wantFml (wantAll (k + m) ▷ stk)) f rest
index-run zero k stk rest f rewrite SP.+-zero k = refl
index-run (suc m) k stk rest f rewrite SP.+-suc k m =
  index-run m (suc k) stk rest f

-- The second term child of `=f`: the right child is read while the left one is
-- already in hand, so the completion of the node happens in the same iteration.
eqRight-step :
  (t u : Tm) (stk : Stack) (rest : List Bool) (f : Nat)
  → resume (close (t =f SP.Result.rTerm (tmFrom (bits u ++ rest))) stk)
           (SP.Result.rBits (tmFrom (bits u ++ rest))) f
  ≡ resume (close (t =f u) stk) rest f
eqRight-step t u stk rest f rewrite tmFrom-run u rest = refl

-- The `=f` node: the first term child is read inside the tag iteration, the
-- second one while the left child is already in hand.
eq-node :
  (t u : Tm) (stk : Stack) (rest : List Bool) (f : Nat)
  → run (eqRight (SP.Result.rTerm (tmFrom (bits t ++ (bits u ++ rest)))) stk)
       (suc f) (SP.Result.rBits (tmFrom (bits t ++ (bits u ++ rest))))
  ≡ resume (close (t =f u) stk) rest f
eq-node t u stk rest f rewrite tmFrom-run t (bits u ++ rest) =
  eqRight-step t u stk rest f

------------------------------------------------------------------------
-- C-177: the streaming round trip of the formula symbol layer.

parse-run :
  (φ : Fml) (stk : Stack) (rest : List Bool) (f : Nat)
  → run (wantFml stk) (STEPS φ + f) (bitsF φ ++ rest)
  ≡ resume (close φ stk) rest f
parse-run (_=f_ t u) stk rest f
  rewrite SP.++-assoc (bits t) (bits u) rest = eq-node t u stk rest f
parse-run bot stk rest f = refl
parse-run (φ =>f ψ) stk rest f
  rewrite SP.+-assoc (STEPS φ) (STEPS ψ) f
        | SP.++-assoc (bitsF φ) (bitsF ψ) rest
  = trans' (parse-run φ (wantImp ▷ stk) (bitsF ψ ++ rest) (STEPS ψ + f))
           (parse-run ψ (haveImp φ ▷ stk) rest f)
parse-run (all n φ) stk rest f
  rewrite SP.+-assoc n (STEPS φ) f
        | SP.++-assoc (unary n) (bitsF φ) rest
  = trans' (index-run n 0 stk (bitsF φ ++ rest) (STEPS φ + f))
           (parse-run φ (wantAll n ▷ stk) rest f)

------------------------------------------------------------------------
-- C-179: `STEPS` never exceeds the bit length, so the repaired formula code
-- can again be its own fuel.

-- (`≤` and `+` share the default fixity, so the sums are parenthesised.)
≤-self-add-right : (n m : Nat) → n ≤ (n + m)
≤-self-add-right zero m = z≤n
≤-self-add-right (suc n) m = s≤s (≤-self-add-right n m)

≤-add-right : (c n : Nat) → c ≤ (n + c)
≤-add-right zero n = z≤n
≤-add-right (suc c) n rewrite SP.+-suc n c = s≤s (≤-add-right c n)

+-right-mono : (n m c : Nat) → n ≤ m → (n + c) ≤ (m + c)
+-right-mono zero m c z≤n = ≤-add-right c m
+-right-mono (suc n) (suc m) c (s≤s p) = s≤s (+-right-mono n m c p)

+-left-mono : (c n m : Nat) → n ≤ m → (c + n) ≤ (c + m)
+-left-mono zero n m p = p
+-left-mono (suc c) n m p = s≤s (+-left-mono c n m p)

≤-add : (a b c d : Nat) → a ≤ b → c ≤ d → (a + c) ≤ (b + d)
≤-add a b c d p q = ≤-trans (+-right-mono a b c p) (+-left-mono b c d q)

BLEN-nonzero : (t : Tm) → suc zero ≤ SP.BLEN t
BLEN-nonzero (var n) = s≤s z≤n
BLEN-nonzero (num n) = s≤s z≤n
BLEN-nonzero (t +t u) = s≤s z≤n

one≤bits : (t : Tm) → suc zero ≤ LEN (bits t)
one≤bits t rewrite SP.bits-length t = BLEN-nonzero t

STEPS≤LEN : (φ : Fml) → STEPS φ ≤ LEN (bitsF φ)
STEPS≤LEN (_=f_ t u)
  rewrite SP.LEN-++ (bits t) (bits u) =
  s≤s (s≤s (≤-trans (one≤bits t) (≤-self-add-right (LEN (bits t)) (LEN (bits u)))))
STEPS≤LEN bot = s≤s (s≤s z≤n)
STEPS≤LEN (φ =>f ψ)
  rewrite SP.LEN-++ (bitsF φ) (bitsF ψ) =
  s≤s (s≤s (≤-add (STEPS φ) (LEN (bitsF φ)) (STEPS ψ) (LEN (bitsF ψ))
                   (STEPS≤LEN φ) (STEPS≤LEN ψ)))
STEPS≤LEN (all n φ)
  rewrite SP.LEN-++ (unary n) (bitsF φ)
        | SP.LEN-unary n =
  s≤s (s≤s (s≤s (+-left-mono n (STEPS φ) (LEN (bitsF φ)) (STEPS≤LEN φ))))

------------------------------------------------------------------------
-- C-180: the repaired formula coder, its total decoder and the round trip.

codeF' : Fml → Nat
codeF' φ = codeBits (bitsF φ)

decF : Nat → Fml
decF c = rVal (run (wantFml ε) c (unbits c c))

codeF'-roundtrip : (φ : Fml) → decF (codeF' φ) ≡ φ
codeF'-roundtrip φ = stepFuel
  where
    c : Nat
    c = codeBits (bitsF φ)

    len-bound : LEN (bitsF φ) ≤ c
    len-bound = ≤-trans (≤-suc (LEN (bitsF φ))) (BC.codeBits-dominates (bitsF φ))

    steps-bound : STEPS φ ≤ c
    steps-bound = ≤-trans (STEPS≤LEN φ) len-bound

    steps-split : Σ' Nat (λ k → c ≡ STEPS φ + k)
    steps-split = SP.≤-split steps-bound

    k : Nat
    k = fst' steps-split

    eqS : c ≡ STEPS φ + k
    eqS = snd' steps-split

    len-split : Σ' Nat (λ j → c ≡ LEN (bitsF φ) + j)
    len-split = SP.≤-split len-bound

    j : Nat
    j = fst' len-split

    eqL : c ≡ LEN (bitsF φ) + j
    eqL = snd' len-split

    junk : List Bool
    junk = unbits j (SP.halfs (LEN (bitsF φ)) c)

    bitsEq : unbits c c ≡ bitsF φ ++ junk
    bitsEq = trans' stepA stepB
      where
        stepA : unbits c c ≡ unbits (LEN (bitsF φ)) c ++ junk
        stepA = SP.subst'
          (λ fuel → unbits fuel c ≡ unbits (LEN (bitsF φ)) c ++ junk)
          (sym' eqL)
          (SP.unbits-split (LEN (bitsF φ)) j c)

        stepB : unbits (LEN (bitsF φ)) c ++ junk ≡ bitsF φ ++ junk
        stepB = cong-here (λ xs → xs ++ junk) (BC.unbits-code (bitsF φ))

    reduced : rVal (run (wantFml ε) (STEPS φ + k) (bitsF φ ++ junk)) ≡ φ
    reduced = cong-here rVal (parse-run φ ε junk k)

    stepBits : rVal (run (wantFml ε) (STEPS φ + k) (unbits c c)) ≡ φ
    stepBits = SP.subst'
      (λ bs → rVal (run (wantFml ε) (STEPS φ + k) bs) ≡ φ)
      (sym' bitsEq) reduced

    stepFuel : rVal (run (wantFml ε) c (unbits c c)) ≡ φ
    stepFuel = SP.subst'
      (λ fuel → rVal (run (wantFml ε) fuel (unbits c c)) ≡ φ)
      (sym' eqS) stepBits

roundtrip-implies-injective-F :
  {A : Set} (c : Fml → A) (d : A → Fml)
  → ((φ : Fml) → d (c φ) ≡ φ)
  → (φ ψ : Fml) → c φ ≡ c ψ → φ ≡ ψ
roundtrip-implies-injective-F c d rt φ ψ p =
  trans' (sym' (rt φ)) (trans' (cong-here d p) (rt ψ))

codeF'-injective : (φ ψ : Fml) → codeF' φ ≡ codeF' ψ → φ ≡ ψ
codeF'-injective = roundtrip-implies-injective-F codeF' decF codeF'-roundtrip
