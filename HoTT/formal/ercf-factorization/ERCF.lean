/-
MP-ERCF-001: task-relative factorization controls for the ERCF research line.

Scope: ordinary dependent type theory / Lean equality.  These theorems are
general representation results.  They do not use univalence, cubical Path,
HITs, truncation, or any HoTT-specific rule, and therefore do not constitute a
HoTT paradox.
-/

set_option autoImplicit false

universe uR uA uY uI uS

namespace ERCF

def FactorsThrough {R : Type uR} {A : Type uA} {Y : Type uY}
    (abstract : R → A) (observe : R → Y) : Prop :=
  ∃ decode : A → Y, ∀ x : R, observe x = decode (abstract x)

def FiberConstant {R : Type uR} {A : Type uA} {Y : Type uY}
    (abstract : R → A) (observe : R → Y) : Prop :=
  ∀ x y : R, abstract x = abstract y → observe x = observe y

def ParadoxWitness {R : Type uR} {A : Type uA} {Y : Type uY}
    (abstract : R → A) (observe : R → Y) : Prop :=
  ∃ x y : R, abstract x = abstract y ∧ observe x ≠ observe y

def HasSection {R : Type uR} {A : Type uA} (abstract : R → A) : Prop :=
  ∃ choose : A → R, ∀ a : A, abstract (choose a) = a

def Injective {R : Type uR} {A : Type uA} (abstract : R → A) : Prop :=
  ∀ ⦃x y : R⦄, abstract x = abstract y → x = y

theorem factorsThrough_implies_fiberConstant
    {R : Type uR} {A : Type uA} {Y : Type uY}
    {abstract : R → A} {observe : R → Y}
    (h : FactorsThrough abstract observe) :
    FiberConstant abstract observe := by
  rcases h with ⟨decode, hdecode⟩
  intro x y hxy
  calc
    observe x = decode (abstract x) := hdecode x
    _ = decode (abstract y) := congrArg decode hxy
    _ = observe y := (hdecode y).symm

theorem paradoxWitness_implies_not_factorsThrough
    {R : Type uR} {A : Type uA} {Y : Type uY}
    {abstract : R → A} {observe : R → Y}
    (witness : ParadoxWitness abstract observe) :
    ¬ FactorsThrough abstract observe := by
  intro hfactor
  rcases witness with ⟨x, y, habstract, hobserve⟩
  exact hobserve ((factorsThrough_implies_fiberConstant hfactor) x y habstract)

theorem abstractDerivedObservation_factors
    {R : Type uR} {A : Type uA} {Y : Type uY}
    (abstract : R → A) (decode : A → Y) :
    FactorsThrough abstract (fun x => decode (abstract x)) := by
  exact ⟨decode, fun _ => rfl⟩

theorem fiberConstant_and_section_implies_factorsThrough
    {R : Type uR} {A : Type uA} {Y : Type uY}
    {abstract : R → A} {observe : R → Y}
    (hconstant : FiberConstant abstract observe)
    (hsection : HasSection abstract) :
    FactorsThrough abstract observe := by
  rcases hsection with ⟨choose, hchoose⟩
  refine ⟨fun a => observe (choose a), ?_⟩
  intro x
  exact (hconstant (choose (abstract x)) x (hchoose (abstract x))).symm

def forgetSecond {A : Type uA} {S : Type uS} : A × S → A :=
  fun pair => pair.1

def observeSecond {A : Type uA} {S : Type uS} : A × S → S :=
  fun pair => pair.2

theorem e0_has_paradoxWitness
    {A : Type uA} {S : Type uS}
    (a₀ : A) (s₀ s₁ : S) (different : s₀ ≠ s₁) :
    ParadoxWitness (@forgetSecond A S) (@observeSecond A S) := by
  exact ⟨(a₀, s₀), (a₀, s₁), rfl, different⟩

theorem e0_secondObservation_does_not_factor
    {A : Type uA} {S : Type uS}
    (a₀ : A) (s₀ s₁ : S) (different : s₀ ≠ s₁) :
    ¬ FactorsThrough (@forgetSecond A S) (@observeSecond A S) := by
  exact paradoxWitness_implies_not_factorsThrough
    (e0_has_paradoxWitness a₀ s₀ s₁ different)

theorem e0_firstObservation_factors
    {A : Type uA} {S : Type uS} :
    FactorsThrough (@forgetSecond A S) (@forgetSecond A S) := by
  exact ⟨fun a => a, fun _ => rfl⟩

theorem subsingletonCodomain_has_no_paradoxWitness
    {R : Type uR} {A : Type uA} {Y : Type uY}
    [Subsingleton Y]
    (abstract : R → A) (observe : R → Y) :
    ¬ ParadoxWitness abstract observe := by
  intro witness
  rcases witness with ⟨x, y, _, different⟩
  exact different (Subsingleton.elim (observe x) (observe y))

theorem unitObservation_factors
    {R : Type uR} {A : Type uA}
    (abstract : R → A) (observe : R → Unit) :
    FactorsThrough abstract observe := by
  exact ⟨fun _ => (), fun x => Subsingleton.elim (observe x) ()⟩

def NonInjective {R : Type uR} {A : Type uA} (abstract : R → A) : Prop :=
  ∃ x y : R, x ≠ y ∧ abstract x = abstract y

def SeparatesCollapsedPairs
    {R : Type uR} {A : Type uA} {Y : Type uY} {I : Type uI}
    (abstract : R → A) (observations : I → R → Y) : Prop :=
  ∀ x y : R, abstract x = abstract y → x ≠ y →
    ∃ index : I, observations index x ≠ observations index y

theorem separatingFamily_detects_nonfactorization
    {R : Type uR} {A : Type uA} {Y : Type uY} {I : Type uI}
    {abstract : R → A} {observations : I → R → Y}
    (hnoninjective : NonInjective abstract)
    (hseparates : SeparatesCollapsedPairs abstract observations) :
    ∃ index : I, ¬ FactorsThrough abstract (observations index) := by
  rcases hnoninjective with ⟨x, y, different, collapsed⟩
  rcases hseparates x y collapsed different with ⟨index, distinguished⟩
  exact ⟨index, paradoxWitness_implies_not_factorsThrough
    ⟨x, y, collapsed, distinguished⟩⟩

theorem identityObservation_factors_implies_injective
    {R : Type uR} {A : Type uA}
    {abstract : R → A}
    (h : FactorsThrough abstract (fun x : R => x)) :
    Injective abstract := by
  rcases h with ⟨decode, hdecode⟩
  intro x y hxy
  calc
    x = decode (abstract x) := hdecode x
    _ = decode (abstract y) := congrArg decode hxy
    _ = y := (hdecode y).symm

#check factorsThrough_implies_fiberConstant
#check paradoxWitness_implies_not_factorsThrough
#check abstractDerivedObservation_factors
#check fiberConstant_and_section_implies_factorsThrough
#check e0_has_paradoxWitness
#check e0_secondObservation_does_not_factor
#check e0_firstObservation_factors
#check subsingletonCodomain_has_no_paradoxWitness
#check unitObservation_factors
#check separatingFamily_detects_nonfactorization
#check identityObservation_factors_implies_injective

end ERCF
