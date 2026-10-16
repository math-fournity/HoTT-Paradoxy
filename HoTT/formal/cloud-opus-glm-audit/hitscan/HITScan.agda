{-# OPTIONS --safe --cubical --guardedness #-}
{-
  HITScan: name-level dependency closure and higher-inductive-type detector.
  (Cloud-Opus audit of the GLM line, 2026-09-27; audit item R1.)

  Given the name of a checked definition, `scan` walks, by Agda reflection,
  every name that occurs in its type and in its definition (clause
  telescopes, patterns, bodies; with reconstructed hidden arguments), and
  recursively in the types and definitions of those names, until closure.
  For every data type met in the closure it normalises the types of all of
  its constructors and records the data type as a HIT when some
  constructor's codomain is a path type (a path constructor, which is the
  only way a HIT can be declared in Cubical Agda).  Under normalisation
  `isSet`, `isProp`, `Path`, ... unfold; the result's head is PathP or the
  BUILTIN PATH `_≡_` (which the normaliser keeps folded); both count.

  Macros (usable in types, so the kernel checks the stated equations):
    hitsOf   n  : List Name   -- data types with path constructors
    axiomsOf n  : List Name   -- leaves reported as postulates/axioms
    sizeOf   n  : Nat         -- number of names in the closure
  and `reportClosure n` prints every name of the closure with its kind via
  debugPrint (visible with -v hitscan:10).

  Soundness boundary (stated, not hidden): the closure is exactly what
  Agda's reflection API reveals.  A definition whose body is not revealed
  (abstract/opaque, or a postulate) is a leaf and is listed by axiomsOf;
  a certificate `hitsOf n ≡ []` is therefore read together with
  `axiomsOf n`, whose members must each be a builtin/primitive.
-}
module HITScan where

open import Agda.Primitive
open import Agda.Builtin.Reflection
open import Agda.Builtin.List
open import Agda.Builtin.Nat
open import Agda.Builtin.Bool
open import Agda.Builtin.Unit
open import Agda.Builtin.String
open import Agda.Builtin.Sigma
open import Agda.Builtin.Word
open import Agda.Primitive.Cubical using (PathP)
open import Agda.Builtin.Cubical.Path using (_≡_)

infixl 1 _>>=_
infixr 1 _>>_

private
  _>>=_ : ∀ {a b} {A : Set a} {B : Set b} → TC A → (A → TC B) → TC B
  _>>=_ = bindTC

  _>>_ : ∀ {a b} {A : Set a} {B : Set b} → TC A → TC B → TC B
  m >> k = bindTC m (λ _ → k)

  return : ∀ {a} {A : Set a} → A → TC A
  return = returnTC

  if_then_else_ : ∀ {a} {A : Set a} → Bool → A → A → A
  if true  then x else y = x
  if false then x else y = y

  _++_ : ∀ {a} {A : Set a} → List A → List A → List A
  []       ++ ys = ys
  (x ∷ xs) ++ ys = x ∷ (xs ++ ys)

  length : ∀ {a} {A : Set a} → List A → Nat
  length []       = 0
  length (_ ∷ xs) = suc (length xs)

  reverse-onto : ∀ {a} {A : Set a} → List A → List A → List A
  reverse-onto []       acc = acc
  reverse-onto (x ∷ xs) acc = reverse-onto xs (x ∷ acc)

  reverse : ∀ {a} {A : Set a} → List A → List A
  reverse xs = reverse-onto xs []

------------------------------------------------------------------------
-- A name set: an (unbalanced) binary search tree on a hashed key, with
-- collision buckets compared by primQNameEquality.

private
  key : Name → Nat
  key n with primQNameToWord64s n
  ... | (w1 , w2) = mod-helper 0 2305843009213693950
                      (primWord64ToNat w1 + primWord64ToNat w2 * 2654435761)
                      2305843009213693950

  data NameSet : Set where
    leaf : NameSet
    node : NameSet → Nat → List Name → NameSet → NameSet

  memberB : Name → List Name → Bool
  memberB x []       = false
  memberB x (y ∷ ys) = if primQNameEquality x y then true else memberB x ys

  member' : Nat → Name → NameSet → Bool
  member' k x leaf = false
  member' k x (node l k' b r) =
    if k < k' then member' k x l
    else (if k' < k then member' k x r else memberB x b)

  member : Name → NameSet → Bool
  member x s = member' (key x) x s

  insert' : Nat → Name → NameSet → NameSet
  insert' k x leaf = node leaf k (x ∷ []) leaf
  insert' k x (node l k' b r) =
    if k < k' then node (insert' k x l) k' b r
    else (if k' < k then node l k' b (insert' k x r)
          else node l k' (x ∷ b) r)

  insert : Name → NameSet → NameSet
  insert x s = insert' (key x) x s

------------------------------------------------------------------------
-- Names occurring in reflected syntax (accumulating, duplicates allowed).

private
  mutual
    nmT : Term → List Name → List Name
    nmT (var x args)       acc = nmArgs args acc
    nmT (con c args)       acc = c ∷ nmArgs args acc
    nmT (def f args)       acc = f ∷ nmArgs args acc
    nmT (lam v (abs s t))  acc = nmT t acc
    nmT (pat-lam cs args)  acc = nmCls cs (nmArgs args acc)
    nmT (pi (arg i a) (abs s b)) acc = nmT a (nmT b acc)
    nmT (agda-sort s)      acc = nmS s acc
    nmT (lit l)            acc = nmL l acc
    nmT (meta x args)      acc = nmArgs args acc
    nmT unknown            acc = acc

    nmArgs : List (Arg Term) → List Name → List Name
    nmArgs []               acc = acc
    nmArgs (arg i t ∷ args) acc = nmT t (nmArgs args acc)

    nmS : Sort → List Name → List Name
    nmS (set t)     acc = nmT t acc
    nmS (lit n)     acc = acc
    nmS (prop t)    acc = nmT t acc
    nmS (propLit n) acc = acc
    nmS (inf n)     acc = acc
    nmS unknown     acc = acc

    nmL : Literal → List Name → List Name
    nmL (name x) acc = x ∷ acc
    nmL _        acc = acc

    nmP : Pattern → List Name → List Name
    nmP (con c ps) acc = c ∷ nmPs ps acc
    nmP (dot t)    acc = nmT t acc
    nmP (var x)    acc = acc
    nmP (lit l)    acc = nmL l acc
    nmP (proj f)   acc = f ∷ acc
    nmP (absurd x) acc = acc

    nmPs : List (Arg Pattern) → List Name → List Name
    nmPs []              acc = acc
    nmPs (arg i p ∷ ps)  acc = nmP p (nmPs ps acc)

    nmTel : List (Σ String (λ _ → Arg Term)) → List Name → List Name
    nmTel []                     acc = acc
    nmTel ((s , arg i t) ∷ tel)  acc = nmT t (nmTel tel acc)

    nmC : Clause → List Name → List Name
    nmC (clause tel ps t)      acc = nmTel tel (nmPs ps (nmT t acc))
    nmC (absurd-clause tel ps) acc = nmTel tel (nmPs ps acc)

    nmCls : List Clause → List Name → List Name
    nmCls []       acc = acc
    nmCls (c ∷ cs) acc = nmC c (nmCls cs acc)

------------------------------------------------------------------------
-- Is a (normalised) constructor type a path constructor?

private
  codomain : Term → Term
  codomain (pi a (abs s b)) = codomain b
  codomain t = t

  -- `_≡_` is Agda's BUILTIN PATH and is kept folded by the normaliser,
  -- so both heads are recognised (found by the scanner's own negative
  -- control on ∥_∥₁, 2026-09-27).
  isPathHead : Term → Bool
  isPathHead (def f _) =
    if primQNameEquality f (quote PathP) then true
    else primQNameEquality f (quote _≡_)
  isPathHead _ = false

  anyPathCon : List Name → TC Bool
  anyPathCon []       = return false
  anyPathCon (c ∷ cs) =
    withNormalisation true (getType c) >>= λ t →
    if isPathHead (codomain t) then return true else anyPathCon cs

------------------------------------------------------------------------
-- The scan.

data Kind : Set where
  kFun kData kHIT kRec kCon kAxiom kPrim : Kind

record Result : Set where
  constructor result
  field
    seen    : List Name           -- discovery order
    hits    : List Name
    datas   : List Name
    axioms  : List Name
    prims   : List Name
    kinds   : List (Σ Name (λ _ → Kind))
open Result public

private
  pushNew : List Name → NameSet → List Name → Σ NameSet (λ _ → List Name)
  pushNew []       s st = s , st
  pushNew (x ∷ xs) s st =
    if member x s then pushNew xs s st else pushNew xs (insert x s) (x ∷ st)

  -- one step: names referenced by the type and definition of n, and its kind
  step : Name → TC (Σ (List Name) (λ _ → Kind))
  step n =
    getType n >>= λ ty →
    getDefinition n >>= λ d → go ty d
    where
    go : Term → Definition → TC (Σ (List Name) (λ _ → Kind))
    go ty (function cs)       = return (nmT ty (nmCls cs []) , kFun)
    go ty (data-type pars cs) =
      anyPathCon cs >>= λ h → return (nmT ty cs , (if h then kHIT else kData))
    go ty (record-type c fs)  = return (nmT ty (c ∷ fields fs) , kRec)
      where
      fields : List (Arg Name) → List Name
      fields []             = []
      fields (arg i f ∷ xs) = f ∷ fields xs
    go ty (data-cons d q)     = return (nmT ty (d ∷ []) , kCon)
    go ty axiom               = return (nmT ty [] , kAxiom)
    go ty prim-fun            = return (nmT ty [] , kPrim)

  loop : Nat → NameSet → List Name → Result → TC Result
  loop zero    s st r = typeError (strErr "HITScan: fuel exhausted" ∷ [])
  loop (suc f) s []  r = return r
  loop (suc f) s (n ∷ st) r =
    step n >>= λ { (refs , k) →
    let sst = pushNew refs s st
        r' = record r
               { seen   = n ∷ seen r
               ; hits   = add k kHIT   n (hits r)
               ; datas  = add k kData  n (add k kHIT n (datas r))
               ; axioms = add k kAxiom n (axioms r)
               ; prims  = add k kPrim  n (prims r)
               ; kinds  = (n , k) ∷ kinds r }
    in loop f (fst sst) (snd sst) r' }
    where
    same : Kind → Kind → Bool
    same kFun kFun = true
    same kData kData = true
    same kHIT kHIT = true
    same kRec kRec = true
    same kCon kCon = true
    same kAxiom kAxiom = true
    same kPrim kPrim = true
    same _ _ = false
    add : Kind → Kind → Name → List Name → List Name
    add k k' n xs = if same k k' then n ∷ xs else xs

scan : Name → TC Result
scan n = loop 1000000 (insert n leaf) (n ∷ []) (result [] [] [] [] [] [])

------------------------------------------------------------------------
-- Macros.

private
  quoteNames : List Name → Term
  quoteNames []       = con (quote []) []
  quoteNames (x ∷ xs) =
    con (quote _∷_)
      (arg (arg-info visible (modality relevant quantity-ω)) (lit (name x)) ∷
       arg (arg-info visible (modality relevant quantity-ω)) (quoteNames xs) ∷ [])

macro
  hitsOf : Name → Term → TC ⊤
  hitsOf n hole = scan n >>= λ r → unify hole (quoteNames (reverse (hits r)))

  axiomsOf : Name → Term → TC ⊤
  axiomsOf n hole = scan n >>= λ r → unify hole (quoteNames (reverse (axioms r)))

  primsOf : Name → Term → TC ⊤
  primsOf n hole = scan n >>= λ r → unify hole (quoteNames (reverse (prims r)))

  datasOf : Name → Term → TC ⊤
  datasOf n hole = scan n >>= λ r → unify hole (quoteNames (reverse (datas r)))

  sizeOf : Name → Term → TC ⊤
  sizeOf n hole = scan n >>= λ r → unify hole (lit (nat (length (seen r))))

private
  kindStr : Kind → String
  kindStr kFun   = "function"
  kindStr kData  = "data"
  kindStr kHIT   = "HIT"
  kindStr kRec   = "record"
  kindStr kCon   = "constructor"
  kindStr kAxiom = "axiom"
  kindStr kPrim  = "primitive"

  printAll : List (Σ Name (λ _ → Kind)) → TC ⊤
  printAll []             = return tt
  printAll ((n , k) ∷ xs) =
    debugPrint "hitscan" 10 (strErr "  closure: " ∷ strErr (kindStr k) ∷ strErr " " ∷ nameErr n ∷ []) >>
    printAll xs

macro
  -- prints the whole closure (with -v hitscan:10) and returns tt
  reportClosure : Name → Term → TC ⊤
  reportClosure n hole =
    scan n >>= λ r →
    debugPrint "hitscan" 10 (strErr "HITScan closure of " ∷ nameErr n ∷ strErr " : " ∷
                             strErr (primShowNat (length (seen r))) ∷ strErr " names" ∷ []) >>
    printAll (reverse (kinds r)) >>
    unify hole (con (quote tt) [])
