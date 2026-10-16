import GodelQ.ZFC.SeqTranslate

/-! 探针 L3：iT 的公式保持性（临时文件，不进收据） -/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.Translate

namespace ProbeL3

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- A. 构造子的输出形状
#check @GodelQ.Translate.iT.construction
#check @GodelQ.Translate.iT.blueprint
#check @FFL.FirstOrder.Arithmetic.Bootstrapping.UformulaRec1.Construction.semiformula_result_induction
#check @FFL.FirstOrder.Arithmetic.Bootstrapping.IsSemiformula.and
#check @FFL.FirstOrder.Arithmetic.Bootstrapping.IsSemiformula.or
#check @FFL.FirstOrder.Arithmetic.Bootstrapping.IsSemiformula.all
#check @FFL.FirstOrder.Arithmetic.Bootstrapping.IsSemiformula.exs
#check @FFL.FirstOrder.Arithmetic.Bootstrapping.IsSemiformula.verum
#check @FFL.FirstOrder.Arithmetic.Bootstrapping.IsSemiformula.falsum

-- B. iTR 的公式性（rel 支的子目标）
#check @GodelQ.Translate.iTR
#check @GodelQ.Translate.iTR_quote
#check @GodelQ.Translate.qqAlls
#check @GodelQ.Translate.conjunct
#check @GodelQ.Translate.imp
#check @FFL.FirstOrder.Arithmetic.Bootstrapping.IsSemiformula.imp
#check @FFL.FirstOrder.Arithmetic.Bootstrapping.IsSemiformula.neg

-- C. 尝试：公式保持性（先用 sorry 占位看语句是否成型）
example {n p : V} (hp : IsSemiformula ℒₒᵣ n p) : IsSemiformula ℒₛₑₜ n (iT n p) := by
  sorry

end ProbeL3
