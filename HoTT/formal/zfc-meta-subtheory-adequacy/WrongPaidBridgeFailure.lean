/-!
Expected rejection control for MP-ZFC-META-SUBTHEORY-ADEQUACY-001.

The control case has a paid bridge.  It deliberately tries to prove the
failure predicate anyway.  Lean must reject the `¬ True` obligation; a source
gap cannot be manufactured by merely choosing the failure label.
-/

namespace WrongZFCMetaSubtheoryAdequacy

structure ApplicationCase where
  applicationClaim : Prop
  claimsOriginalResolution : Prop
  requiresBridge : Prop
  bridgePaid : Prop
  explicitTaskSwitch : Prop

def ApplicationAdequacyFailure (case_ : ApplicationCase) : Prop :=
  case_.applicationClaim ∧
  case_.claimsOriginalResolution ∧
  case_.requiresBridge ∧
  ¬ case_.bridgePaid ∧
  ¬ case_.explicitTaskSwitch

def bridgePaidControl : ApplicationCase where
  applicationClaim := True
  claimsOriginalResolution := True
  requiresBridge := True
  bridgePaid := True
  explicitTaskSwitch := False

theorem wrong_paid_bridge_failure :
    ApplicationAdequacyFailure bridgePaidControl := by
  trivial

end WrongZFCMetaSubtheoryAdequacy
