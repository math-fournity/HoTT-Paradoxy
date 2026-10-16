/-!
`MP-ZFC-MEMBERSHIP-LANGUAGE-INVARIANCE-001` makes the language claim behind
Q explicit at the level of a first-order membership language.

The formulas below have equality, membership, falsity, conjunction,
disjunction, implication, universal quantification and existential
quantification.  They deliberately have no `originDone` predicate.
The kernel proves that every such formula, and hence every theory formed only
from such formulas, is invariant under changing an external origin-completion
predicate while keeping the membership relation fixed.

This is not a formalization of the full ZFC axiom scheme.  Rather, it is a
syntax/semantics theorem for the language in which a future ZFC encoding would
live.  It does not say that ZFC cannot define a particular process predicate;
it says that no predicate absent from the language/definitions can be supplied
automatically by satisfaction of membership-language formulas alone.
-/

namespace ZFCMembershipLanguageBoundary

universe u

structure MembershipStructure (α : Type u) where
  member : α → α → Prop

structure CompletionExpansion (α : Type u) extends MembershipStructure α where
  originDone : α → Prop

def expand
    (membership : MembershipStructure α)
    (originDone : α → Prop) : CompletionExpansion α where
  member := membership.member
  originDone := originDone

/-- A de Bruijn-style first-order membership language with the standard
    connectives used when expressing set-theoretic axiom schemes. -/
inductive MembershipFormula where
  | equal (left right : Nat)
  | member (left right : Nat)
  | falsum
  | and (left right : MembershipFormula)
  | or (left right : MembershipFormula)
  | implies (left right : MembershipFormula)
  | all (body : MembershipFormula)
  | existsF (body : MembershipFormula)

def extendValuation
    (valuation : Nat → α)
    (value : α) : Nat → α
  | 0 => value
  | Nat.succ index => valuation index

def evalBase
    (model : MembershipStructure α)
    (valuation : Nat → α) : MembershipFormula → Prop
  | .equal left right => valuation left = valuation right
  | .member left right => model.member (valuation left) (valuation right)
  | .falsum => False
  | .and left right => evalBase model valuation left ∧ evalBase model valuation right
  | .or left right => evalBase model valuation left ∨ evalBase model valuation right
  | .implies left right => evalBase model valuation left → evalBase model valuation right
  | .all body => ∀ value, evalBase model (extendValuation valuation value) body
  | .existsF body => ∃ value, evalBase model (extendValuation valuation value) body

/-- An external atom that is intentionally unavailable in `MembershipFormula`.
    It is used only to state the differing-completion control. -/
def evalOriginDone
    (expansion : CompletionExpansion α)
    (valuation : Nat → α)
    (index : Nat) : Prop :=
  expansion.originDone (valuation index)

/-- Every membership-language formula is invariant under an external Done
    change whenever membership itself is preserved. -/
theorem evalBase_invariant_under_originDone
    (left right : CompletionExpansion α)
    (sameMembership : ∀ x y, left.member x y ↔ right.member x y)
    (valuation : Nat → α)
    (formula : MembershipFormula) :
    evalBase left.toMembershipStructure valuation formula ↔
      evalBase right.toMembershipStructure valuation formula := by
  induction formula generalizing valuation with
  | equal leftIndex rightIndex => rfl
  | member leftIndex rightIndex =>
      exact sameMembership (valuation leftIndex) (valuation rightIndex)
  | falsum => rfl
  | and leftFormula rightFormula leftIH rightIH =>
      constructor
      · intro leftPair
        exact ⟨(leftIH valuation).mp leftPair.1, (rightIH valuation).mp leftPair.2⟩
      · intro rightPair
        exact ⟨(leftIH valuation).mpr rightPair.1, (rightIH valuation).mpr rightPair.2⟩
  | or leftFormula rightFormula leftIH rightIH =>
      constructor
      · intro leftChoice
        cases leftChoice with
        | inl leftProof => exact Or.inl ((leftIH valuation).mp leftProof)
        | inr rightProof => exact Or.inr ((rightIH valuation).mp rightProof)
      · intro rightChoice
        cases rightChoice with
        | inl leftProof => exact Or.inl ((leftIH valuation).mpr leftProof)
        | inr rightProof => exact Or.inr ((rightIH valuation).mpr rightProof)
  | implies leftFormula rightFormula leftIH rightIH =>
      constructor
      · intro leftImp rightPremise
        have leftPremise : evalBase left.toMembershipStructure valuation leftFormula :=
          (leftIH valuation).mpr rightPremise
        have leftResult := leftImp leftPremise
        exact (rightIH valuation).mp leftResult
      · intro rightImp leftPremise
        have rightPremise : evalBase right.toMembershipStructure valuation leftFormula :=
          (leftIH valuation).mp leftPremise
        have rightResult := rightImp rightPremise
        exact (rightIH valuation).mpr rightResult
  | all body bodyIH =>
      constructor
      · intro leftAll value
        exact (bodyIH (extendValuation valuation value)).mp (leftAll value)
      · intro rightAll value
        exact (bodyIH (extendValuation valuation value)).mpr (rightAll value)
  | existsF body bodyIH =>
      constructor
      · intro leftExists
        rcases leftExists with ⟨value, leftProof⟩
        exact ⟨value, (bodyIH (extendValuation valuation value)).mp leftProof⟩
      · intro rightExists
        rcases rightExists with ⟨value, rightProof⟩
        exact ⟨value, (bodyIH (extendValuation valuation value)).mpr rightProof⟩

abbrev MembershipTheory : Type := MembershipFormula → Prop

def Satisfies
    (model : MembershipStructure α)
    (theory : MembershipTheory) : Prop :=
  ∀ formula, theory formula → ∀ valuation, evalBase model valuation formula

/-- A theory whose formulas are all in the membership language is invariant
    under external completion expansions with the same membership relation. -/
theorem satisfies_membership_theory_invariant_under_originDone
    (left right : CompletionExpansion α)
    (sameMembership : ∀ x y, left.member x y ↔ right.member x y)
    (theory : MembershipTheory) :
    Satisfies left.toMembershipStructure theory ↔
      Satisfies right.toMembershipStructure theory := by
  constructor
  · intro leftSatisfies formula inTheory valuation
    exact (evalBase_invariant_under_originDone left right sameMembership valuation formula).mp
      (leftSatisfies formula inTheory valuation)
  · intro rightSatisfies formula inTheory valuation
    exact (evalBase_invariant_under_originDone left right sameMembership valuation formula).mpr
      (rightSatisfies formula inTheory valuation)

/-- A satisfying membership-language model can be expanded in two ways that
    preserve every base formula while disagreeing on a selected external Done
    atom.  This is conditional on the supplied base model; it constructs no
    model of ZFC. -/
theorem membership_theory_has_opposite_originDone_expansions
    (theory : MembershipTheory)
    (base : MembershipStructure α)
    (baseSatisfies : Satisfies base theory)
    (state : α) :
    ∃ positive negative : CompletionExpansion α,
      Satisfies positive.toMembershipStructure theory ∧
      Satisfies negative.toMembershipStructure theory ∧
      (∀ x y, positive.member x y ↔ negative.member x y) ∧
      positive.originDone state ∧
      ¬ negative.originDone state := by
  refine ⟨expand base (fun _ => True), expand base (fun _ => False), ?_, ?_, ?_, ?_, ?_⟩
  · simpa [expand] using baseSatisfies
  · simpa [expand] using baseSatisfies
  · intro x y
    rfl
  · exact True.intro
  · intro h
    exact h

/-- The external atom really can change across the two expansions, whereas no
    membership formula can observe that change. -/
theorem external_originDone_control
    (base : MembershipStructure α)
    (state : α) :
    evalOriginDone (expand base (fun _ => True)) (fun _ => state) 0 ∧
    ¬ evalOriginDone (expand base (fun _ => False)) (fun _ => state) 0 := by
  constructor
  · exact True.intro
  · intro h
    exact h

#print axioms evalBase_invariant_under_originDone
#print axioms satisfies_membership_theory_invariant_under_originDone
#print axioms membership_theory_has_opposite_originDone_expansions
#print axioms external_originDone_control

end ZFCMembershipLanguageBoundary
