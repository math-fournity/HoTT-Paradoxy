import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000

namespace GodelQ.ProbeExsFinal
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! ### Foundation 的 IsUTerm 是裸 Fixpoint，namespace 里只有 IsUTermVec 的引理

IsUTerm L x := (construction L).Fixpoint ![]  (Basic.lean:151)
namespace IsUTerm 里只有 defined/definable/definable' 三个实例，
**没有任何构造子或代入保持引理**。

所以 `IsUTerm` 的归纳原理若是 Fixpoint 提供的，名字要探。 -/

#check @IsUTerm
#check @TermRec
#check @Language.TermRec

end GodelQ.ProbeExsFinal