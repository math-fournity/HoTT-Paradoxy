import GodelQ.ZFC.Z0Full
import GodelQ.ZFC.Z0PA
import Foundation.FirstOrder.LK.Interpretation

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.Z0Full
open LogicalConnective

/-!
# CG-007 · W8 第 1 层：`arithTrln.translate` 与逼辑运算的语法交换律

本文件只含无未证标记的七条引理（CG001-C-388）。
`emb` 相关的工作（CG001-C-389）在 `Z0Layer1Emb.lean`，它带未证标记。
-/

namespace GodelQ.Z0Layer1

variable {n : ℕ} {k : ℕ}

theorem map_and (φ ψ : Semiformula ℒₒᵣ Empty n) :
    arithTrln.translate (Semiformula.and φ ψ) =
      Semiformula.and (arithTrln.translate φ) (arithTrln.translate ψ) :=
  LogicalConnective.HomClass.map_and _ _ _

theorem map_or (φ ψ : Semiformula ℒₒᵣ Empty n) :
    arithTrln.translate (Semiformula.or φ ψ) =
      Semiformula.or (arithTrln.translate φ) (arithTrln.translate ψ) :=
  LogicalConnective.HomClass.map_or _ _ _

theorem map_neg (φ : Semiformula ℒₒᵣ Empty n) :
    arithTrln.translate (Semiformula.neg φ) = Semiformula.neg (arithTrln.translate φ) :=
  LogicalConnective.HomClass.map_neg _ _

theorem map_all (φ : Semiformula ℒₒᵣ Empty (n + 1)) :
    arithTrln.translate (Semiformula.all φ) = arithTrln.fal (arithTrln.translate φ) :=
  rfl

theorem map_exs (φ : Semiformula ℒₒᵣ Empty (n + 1)) :
    arithTrln.translate (Semiformula.exs φ) = arithTrln.exs (arithTrln.translate φ) :=
  rfl

theorem map_rel (R : Language.ORing.Rel k) (v : Fin k → Semiterm ℒₒᵣ Empty n) :
    arithTrln.translate (Semiformula.rel R v) = arithTrln.translateRel R v :=
  rfl

theorem map_nrel (R : Language.ORing.Rel k) (v : Fin k → Semiterm ℒₒᵣ Empty n) :
    arithTrln.translate (Semiformula.nrel R v) = ∼arithTrln.translateRel R v :=
  rfl

end GodelQ.Z0Layer1

#print axioms GodelQ.Z0Layer1.map_and
#print axioms GodelQ.Z0Layer1.map_or
#print axioms GodelQ.Z0Layer1.map_neg
#print axioms GodelQ.Z0Layer1.map_all
#print axioms GodelQ.Z0Layer1.map_exs
#print axioms GodelQ.Z0Layer1.map_rel
#print axioms GodelQ.Z0Layer1.map_nrel
