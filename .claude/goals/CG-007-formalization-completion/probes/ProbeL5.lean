import GodelQ.ZFC.SeqTranslate

/-! 探针 L5：三条新引理（临时文件，不进收据） -/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.Translate GodelQ.ZFCArith

namespace ProbeL5

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- A. "⌜φ⌝ 是公式" 的现成引理
#check @FFL.FirstOrder.Arithmetic.Bootstrapping.Sentence.quote_isSemiformula
#check @FFL.FirstOrder.Arithmetic.Bootstrapping.Sentence.quote_isUFormula
#check @FFL.FirstOrder.Arithmetic.Bootstrapping.Semiformula.quote_isSemiformula
#check @FFL.FirstOrder.Arithmetic.Bootstrapping.Sentence.quote_eq_encode_nat
#check @FFL.FirstOrder.Arithmetic.Bootstrapping.IsSemiformula.substs
#check @FFL.FirstOrder.Arithmetic.Bootstrapping.IsSemiformula.qqAlls

-- B. 第 3 条：cRel 的公式性
example (n R : V) : IsSemiformula ℒₛₑₜ n (cRel R) := by
  unfold cRel
  split
  · exact ?_
  · exact ?_

end ProbeL5
