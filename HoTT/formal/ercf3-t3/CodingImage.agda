module CodingImage where

open import Agda.Builtin.Nat
open import Agda.Builtin.Equality
open import Agda.Builtin.Bool using (Bool; true; false)
open import Agda.Builtin.List using (List; []; _∷_)
open import ObjectSyntax
open import DiagonalCore
open import DecodingFence using (Empty)
import BitCoding as BC
import StreamingParser as SP
import FormulaCoding as FC
open BC using (_≤_)
open SP using (_++_)

_≢_ : {A : Set} → A → A → Set
x ≢ y = x ≡ y → Empty

-- T3 audit pulse (bounded): the *replacement* justification for the default
-- branches of the repaired decoders.
--
-- The independent audit (finding F1) showed that the default-branch story in
-- the C-168 narrative was attached to the wrong function: `codeAtom` is
-- surjective (C-184/C-185).  The repaired coders `codeT'`/`codeF'` really do
-- miss `1`, but that fact was never proved here; this module proves it:
--
--   C-186  `(t : Tm) → codeT' t ≢ suc zero`
--   C-187  `(φ : Fml) → codeF' φ ≢ suc zero`
--
-- Why `1` is missed: `codeBits` of a non-empty list always starts with a digit
-- `pack b c` whose argument `c` is itself a code-sentinel value `≥ 1`, and
-- `pack b c ≥ 2` whenever `c ≥ 1`.  So the repaired coders are **not
-- surjective**, which is what makes a default branch *reachable* -- and
-- therefore necessary for a total decoder -- whereas the old narrative's
-- justification (non-surjectivity of `codeAtom`) was simply false.

suc≠zero' : {k : Nat} → suc k ≢ zero
suc≠zero' ()

suc-inj' : {m n : Nat} → suc m ≡ suc n → m ≡ n
suc-inj' refl = refl

twice≠one : (c : Nat) → BC.twice c ≢ suc zero
twice≠one zero ()
twice≠one (suc c) p = suc≠zero' (suc-inj' p)

-- `pack b c` is never `1` as soon as the remaining bundle is non-empty.
pack≠one : (b : Bool) (c : Nat) → suc zero ≤ c → BC.pack b c ≢ suc zero
pack≠one false c h = twice≠one c
pack≠one true (suc c) h p = suc≠zero' (suc-inj' p)

code-sentinel : (bs : List Bool) → suc zero ≤ BC.codeBits bs
code-sentinel bs = BC.≤-trans (BC.s≤s BC.z≤n) (BC.codeBits-dominates bs)

-- C-186
codeT'-misses-one : (t : Tm) → SP.codeT' t ≢ suc zero
codeT'-misses-one (var n) = pack≠one false (BC.codeBits (false ∷ SP.unary n)) (code-sentinel (false ∷ SP.unary n))
codeT'-misses-one (num n) = pack≠one false (BC.codeBits (true ∷ SP.unary n)) (code-sentinel (true ∷ SP.unary n))
codeT'-misses-one (t +t u) =
  pack≠one true (BC.codeBits (SP.bits t ++ SP.bits u)) (code-sentinel (SP.bits t ++ SP.bits u))

-- C-187
codeF'-misses-one : (φ : Fml) → FC.codeF' φ ≢ suc zero
codeF'-misses-one (_=f_ t u) =
  pack≠one false (BC.codeBits (false ∷ (SP.bits t ++ SP.bits u)))
                 (code-sentinel (false ∷ (SP.bits t ++ SP.bits u)))
codeF'-misses-one bot = pack≠one false (BC.codeBits (true ∷ [])) (code-sentinel (true ∷ []))
codeF'-misses-one (φ =>f ψ) =
  pack≠one true (BC.codeBits (false ∷ (FC.bitsF φ ++ FC.bitsF ψ)))
                (code-sentinel (false ∷ (FC.bitsF φ ++ FC.bitsF ψ)))
codeF'-misses-one (all n φ) =
  pack≠one true (BC.codeBits (true ∷ (SP.unary n ++ FC.bitsF φ)))
                (code-sentinel (true ∷ (SP.unary n ++ FC.bitsF φ)))
