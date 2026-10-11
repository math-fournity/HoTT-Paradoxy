import GodelQ.ZFC.Z0Full
import GodelQ.ZFC.Z0PA

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate

namespace GodelQ.ProbeD3Types

-- Core building blocks used by Z0Full.zfcTr_D3_standard's last line:
--   (Sh_provable_iff _).mp (WeakerThan.pbl (zfcTr.D1 ((Sh_provable_iff σ).mpr h)))
-- We need their EXACT types to (a) build the function F and (b) lift it to an implication theorem.

#check Z0Full.zfcTr.D1
#check Z0Full.zfcTr.D1 (σ := (α := ℕ))
#check WeakerThan.pbl
#check Sh_provable_iff
#check (@Sh_provable_iff)
#check FFL.Entailment.deduction
#check FFL.Entailment.Deduction.ofInsert
#check FFL.Entailment.Deduction.inv
#check FFL.Entailment.weakening
#check FFL.Entailment.axiom
#check FFL.Entailment.assume
#check FFL.Entailment.cut
#check FFL.Entailment.adjoin
#check FFL.Entailment.insert
#check FFL.Entailment.mono
#check FFL.Entailment.entails_of_provable
#check FFL.Entailment.prove_imp
#check FFL.Entailment.impI
#check FFL.Entailment.imp_intro
#check FFL.FirstOrder.Entailment.deduction
#check FFL.FirstOrder.Entailment.axiom
#check FFL.FirstOrder.Entailment.cut
#check FFL.FirstOrder.Entailment.assume

end GodelQ.ProbeD3Types
