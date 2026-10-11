import GodelQ.ZFC.SeqTranslate

/-! 探针 L6d：三条新引理（临时文件，不进收据） -/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.Translate GodelQ.ZFCArith

namespace ProbeL6d

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- 第 3 条：cRel 的公式性（层级 = 元数 2）
lemma isSemiformula_cRel (R : V) : IsSemiformula ℒₛₑₜ 2 (cRel R) := by
  simp [cRel, cRelN]

-- 定义域公式的编码
lemma isSemiformula_cDomN : IsSemiformula ℒₛₑₜ 1 (↑cDomN : V) := by
  simp [cDomN]

-- 函数定义公式的编码（0 元 / 2 元）
lemma isSemiformula_cFunc (k f : V) : IsSemiformula ℒₛₑₜ (if k = 0 then 1 else 3) (cFunc k f) := by
  simp only [cFunc, cFuncN]
  split <;> split <;> simp

end ProbeL6d
