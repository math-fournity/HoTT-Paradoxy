-- CG-009: the meta-level target for hAB (path ①), stated precisely.
import GodelQ.ZFC.HAllProof

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate

namespace GodelQ.HABMeta2

-- Check the exact API for Rewriting.free at the typed level.
#check @Rewriting.free
#check @Rewriting.shift
-- The V-level free/subst route:
example (ψ : Semisentence ℒₒᵣ 1) : True := by trivial

end GodelQ.HABMeta2
