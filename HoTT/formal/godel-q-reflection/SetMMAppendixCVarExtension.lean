/-
  M-level, source-bound positive control for G2.

  The generated input fixes the actual variable vocabulary and $f assignments
  of set.mm@160ebb… .  This file proves only the Appendix-C precondition that
  an embedding of that finite vocabulary can be extended by a countably
  infinite fresh family at every source variable type.

  It does not parse all frames into mAx, construct a set.mm-internal mFS
  witness, translate verified proof traces into mPPSt/mThm, define an adequate
  Prv, construct a diagonal sentence, or relate proof acceptance to
  OriginDone.
-/

import SetMMAppendixCGenerated

namespace SetMMAppendixCVarExtension

open SetMMAppendixCGenerated

/-- A source variable remains distinguishable from every newly supplied
    variable in the Appendix-C infinite extension. -/
inductive ExtendedVar where
  | raw : RawVar → ExtendedVar
  | fresh : RawType → Nat → ExtendedVar
deriving DecidableEq, Repr

def variableType : ExtendedVar → RawType
  | .raw rawVariable => rawVarType rawVariable
  | .fresh typecode _ => typecode

def rawEmbedding : RawVar → ExtendedVar := ExtendedVar.raw

def freshFamily (typecode : RawType) : Nat → ExtendedVar :=
  fun index => .fresh typecode index

def HasCountablyInfiniteTypedExtension : Prop :=
  ∀ typecode : RawType,
    ∃ family : Nat → ExtendedVar,
      Function.Injective family ∧
      ∀ index : Nat, variableType (family index) = typecode

theorem rawEmbedding_preserves_source_type (rawVariable : RawVar) :
    variableType (rawEmbedding rawVariable) = rawVarType rawVariable := rfl

theorem rawEmbedding_injective : Function.Injective rawEmbedding := by
  intro left right equality
  cases equality
  rfl

theorem freshFamily_injective (typecode : RawType) :
    Function.Injective (freshFamily typecode) := by
  intro left right equality
  cases equality
  rfl

theorem freshFamily_has_requested_type (typecode : RawType) (index : Nat) :
    variableType (freshFamily typecode index) = typecode := rfl

theorem raw_ne_fresh (rawVariable : RawVar) (typecode : RawType) (index : Nat) :
    rawEmbedding rawVariable ≠ freshFamily typecode index := by
  intro equality
  cases equality

theorem sourceType_has_countably_infinite_extension :
    HasCountablyInfiniteTypedExtension := by
  intro typecode
  refine ⟨freshFamily typecode, freshFamily_injective typecode, ?_⟩
  intro index
  exact freshFamily_has_requested_type typecode index

#print axioms rawEmbedding_preserves_source_type
#print axioms rawEmbedding_injective
#print axioms freshFamily_injective
#print axioms raw_ne_fresh
#print axioms sourceType_has_countably_infinite_extension

end SetMMAppendixCVarExtension
