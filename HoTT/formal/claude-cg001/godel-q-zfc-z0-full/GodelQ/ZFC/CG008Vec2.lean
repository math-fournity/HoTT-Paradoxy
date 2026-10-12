import GodelQ.ZFC.CG008ShiftProof

/-!
# CG-008 · 二元向量的分量取值（**不依赖 `CG008IVE`**）

原先这两条在 `CG008Bv2.lean` 里，而 `CG008Bv2` 导入 `CG008IVE`——
于是任何想用 `bv_eqAtom_le` 的地方（`CG008BvBound`）都会经
`Bv2 → IVE` 绕回起点，形成循环。这两条本身只用向量算术，
**抽到这一层**即可解开。

教训（本会话第三次同类）：**先查导入图**，再动手。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008Vec2
open GodelQ.ZFCArith
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- 分量 0 与 1 的取值。 -/
lemma nth_vec₂_zero (t : V) : (^#0 ∷ t ∷ (0 : V)).[0] = (^#0 : V) := by
  rw [Arithmetic.nth_zero (V := V), Arithmetic.fstIdx_adjoin]

lemma nth_vec₂_one (t : V) : (^#0 ∷ t ∷ (0 : V)).[1] = t := by
  have h1 : (1 : V) = (0 : V) + 1 := by norm_num
  rw [h1, Arithmetic.nth_succ (V := V), Arithmetic.sndIdx_adjoin]
  rw [Arithmetic.nth_zero (V := V), Arithmetic.fstIdx_adjoin]

end GodelQ.CG008Vec2

#print axioms GodelQ.CG008Vec2.nth_vec₂_zero
#print axioms GodelQ.CG008Vec2.nth_vec₂_one
