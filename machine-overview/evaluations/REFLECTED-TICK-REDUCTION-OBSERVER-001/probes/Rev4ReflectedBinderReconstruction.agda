{-# OPTIONS --cubical --guarded #-}
module Rev4ReflectedBinderReconstruction where

open import Agda.Builtin.Cubical.Path
open import Agda.Builtin.List
open import Agda.Builtin.Nat
open import Agda.Builtin.Reflection
open import Agda.Builtin.Unit
open import Clocked.Primitives

infixl 1 _>>=_
_>>=_ : ∀ {a b} {A : Set a} {B : Set b} → TC A → (A → TC B) → TC B
_>>=_ = bindTC

vInfo : ArgInfo
vInfo = arg-info visible (modality relevant quantity-ω)

vArg : ∀ {A : Set} → A → Arg A
vArg x = arg vInfo x

ordinaryConst : ∀ {k} → ▸ k \ α → Nat
ordinaryConst α = zero

forcingConst : ∀ {k} → (@ftick α : FTick k) → Nat
forcingConst α = zero

clone : Name → Name → TC ⊤
clone source target =
  getType source >>= λ ty →
  declareDef (vArg target) ty >>= λ _ →
  getDefinition source >>= λ where
    (function clauses) → defineFun target clauses
    _ → typeError (strErr "expected a function definition" ∷ [])

unquoteDecl ordinaryConstClone = clone (quote ordinaryConst) ordinaryConstClone
unquoteDecl forcingConstClone = clone (quote forcingConst) forcingConstClone

ordinary-clone-computes : ∀ {k} → ▸ k \ α → ordinaryConstClone α ≡ zero
ordinary-clone-computes α = λ _ → zero

forcing-clone-computes : forcingConstClone {k = k0} ◇ ≡ zero
forcing-clone-computes = λ _ → zero

