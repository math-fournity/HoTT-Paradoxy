{-# OPTIONS --safe --cubical #-}

-- A source-corresponding, deliberately small cubical syntax fragment.
--
-- This is not the full syntax or metatheory of cctt, redtt, Cubical Agda, or
-- HoTT.  It retains only Nat, Path/refl, explicit certificates, and a
-- structurally recursive certificate checker.  The point is to make the
-- proof-code interface itself explicit before attempting a Gödel coding.

module CCTTmini where

open import Agda.Builtin.Nat using (Nat; zero; suc)
open import Agda.Builtin.Equality using (_≡_; refl)
open import Agda.Builtin.Bool using (Bool; true; false)
open import Agda.Builtin.List using (List; []; _∷_)
open import Agda.Builtin.Maybe using (Maybe; nothing; just)

mutual
  data Ty : Set where
    natTy  : Ty
    pathTy : Ty → Tm → Tm → Ty

  data Tm : Set where
    var   : Nat → Tm
    zeroT : Tm
    sucT  : Tm → Tm
    reflT : Tm → Tm

Ctx : Set
Ctx = List Ty

data Var : Nat → Ctx → Ty → Set where
  here  : {Γ : Ctx} {A : Ty} → Var zero (A ∷ Γ) A
  there : {n : Nat} {Γ : Ctx} {A B : Ty} → Var n Γ A → Var (suc n) (B ∷ Γ) A

data LookupResult (n : Nat) (Γ : Ctx) : Set where
  found : (A : Ty) → Var n Γ A → LookupResult n Γ

lookup : (n : Nat) → (Γ : Ctx) → Maybe (LookupResult n Γ)
lookup zero    []      = nothing
lookup zero    (A ∷ Γ) = just (found A here)
lookup (suc n) []      = nothing
lookup (suc n) (B ∷ Γ) with lookup n Γ
... | nothing          = nothing
... | just (found A p) = just (found A (there p))

-- A raw certificate is finite syntax with no hole, import, metavariable, or
-- recursion constructor.  The checker below decides this restricted fragment.
data RawCert : Set where
  varC  : Nat → RawCert
  zeroC : RawCert
  sucC  : RawCert → RawCert
  reflC : RawCert → RawCert

erase : RawCert → Tm
erase (varC n) = var n
erase zeroC    = zeroT
erase (sucC c) = sucT (erase c)
erase (reflC c) = reflT (erase c)

data Deriv (Γ : Ctx) : Tm → Ty → Set where
  dvar  : {n : Nat} {A : Ty} → Var n Γ A → Deriv Γ (var n) A
  dzero : Deriv Γ zeroT natTy
  dsuc  : {t : Tm} → Deriv Γ t natTy → Deriv Γ (sucT t) natTy
  drefl : {t : Tm} {A : Ty} → Deriv Γ t A → Deriv Γ (reflT t) (pathTy A t t)

data Checked (Γ : Ctx) (c : RawCert) : Set where
  checked : (A : Ty) → Deriv Γ (erase c) A → Checked Γ c

-- Total by structural recursion on the finite RawCert input.
check : (Γ : Ctx) → (c : RawCert) → Maybe (Checked Γ c)
check Γ (varC n) with lookup n Γ
... | nothing          = nothing
... | just (found A p) = just (checked A (dvar p))
check Γ zeroC = just (checked natTy dzero)
check Γ (sucC c) with check Γ c
... | nothing                       = nothing
... | just (checked natTy d)        = just (checked natTy (dsuc d))
... | just (checked (pathTy A t u) d) = nothing
check Γ (reflC c) with check Γ c
... | nothing            = nothing
... | just (checked A d) = just (checked (pathTy A (erase c) (erase c)) (drefl d))

accepts : Ctx → RawCert → Bool
accepts Γ c with check Γ c
... | nothing = false
... | just _  = true

-- The directly inspectable positive and negative controls frozen by GZ-008.
Γ₁ : Ctx
Γ₁ = natTy ∷ []

oneC : RawCert
oneC = sucC (varC zero)

positiveC : RawCert
positiveC = reflC oneC

positiveAccepted : accepts Γ₁ positiveC ≡ true
positiveAccepted = refl

positiveWitness : Checked Γ₁ positiveC
positiveWitness = checked
  (pathTy natTy (sucT (var zero)) (sucT (var zero)))
  (drefl (dsuc (dvar here)))

illScopedRejected : accepts [] (varC zero) ≡ false
illScopedRejected = refl

wrongSucRejected : accepts [] (sucC (reflC zeroC)) ≡ false
wrongSucRejected = refl

-- A total checker result cannot manufacture a typing derivation: every
-- accepted result carries the relevant Deriv explicitly.  SomeDeriv makes the
-- existential type visible without relying on a library sigma type.
data SomeDeriv (Γ : Ctx) (t : Tm) : Set where
  hasType : (A : Ty) → Deriv Γ t A → SomeDeriv Γ t

checkedSound : {Γ : Ctx} {c : RawCert} → Checked Γ c → SomeDeriv Γ (erase c)
checkedSound (checked A d) = hasType A d

checkSound : {Γ : Ctx} {c : RawCert}
  → (accepted : Checked Γ c)
  → check Γ c ≡ just accepted
  → SomeDeriv Γ (erase c)
checkSound accepted _ = checkedSound accepted
