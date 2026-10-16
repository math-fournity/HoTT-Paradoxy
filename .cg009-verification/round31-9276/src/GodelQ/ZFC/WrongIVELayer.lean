import GodelQ.ZFC.SeqTranslateFormula

/-!
# 负控制：`iVE` 的 bvar 规则错写时被内核拒绝

`isSemiformula_iVE` 依赖 `iVE_bvar : iVE n (^#z) = eqAtom (^#(z + 1))`。
本文件故意把结论写成"层数不加一"（`iVE 0 ^#0 = eqAtom ^#0`），
内核应当拒绝：`iVE 0 ^#0 = eqAtom ^#1`，而 `^#1 ≠ ^#0`。
本文件**不是**任何运行的编译源；它的用途只是证明正规则不是空转。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.SeqTranslate

open GodelQ.Translate GodelQ.ZFCArith

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- 错误的化简（应为 `eqAtom ^#(0+1)`）：内核必须拒绝。 -/
example : iVE (0 : V) (^#0) = eqAtom (^#0) := by
  rw [iVE_bvar]

end GodelQ.SeqTranslate
