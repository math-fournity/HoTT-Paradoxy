import GodelQ.ZFC.CG008RouteB

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008N1

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full GodelQ.ZFCSetInternal

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! # `hEQ` 义务的最终定位：Foundation 的 `TProof` **整层都是闭句级**

## 三个负面观察（都机器核过源码）

**观察 1**：`∀¹ (setEq #0 t)` 对任意 `t : Semiterm V ℒₜ 1` **不是定理**
（取 `t := #1` 读作 `∀ x y, x = y`）。**所以 `set_eq_refl` 那条路不能这样改。**

**观察 2**：`TProof` 命名空间里的每个定义（`Typed.lean:325-470`）
都只谈 `φ : Formula V L = Semiformula V L 0`——**闭句**。
`specialize` / `specialize₂!` / `specialize₃!` 收的 `t : Term V L` 也是**闭项**。

**所以要把 `set_eq_symm` 一类引理从闭项推广到 `Semiterm V ℒₜ n`，
Foundation 的 `TProof` 层**没有对应 API**——不是缺一条引理，是缺一个层的搬运。**

## hEQ 的真实义务（正题）

实例化 `setTheory_sigma₁_induction` 的 `P := fun n phi psi ↦ (V ⊧ phi → Provable 𝗭𝗙𝗣 ⌜phi⌝)` 后，
`hEQ` 情形是：

```
    V ⊧ (.rel Eq.eq ![t₁, t₂]) → Provable 𝗭𝗙𝗢 ⌜(.rel Eq.eq ![t₁, t₂])⌝
```

前提为**真**。要造的是「从 `V ⊧ t₁ = t₂` 生出 ZFC 推导」——
即算术版 `term_complete` 的集合对偶，而那个对偶靠 `toNumVec`（数字项），
`ℒₜ` 无数字项。

## 净结论

**三条独立证据都指向同一处**：`toNumVec`、`natCastEmbedding` 的 numeral 用法、
`substNumerals`——Foundation 的「赋值/见证代入」工具**全部 ℒₒᵣ 专属**。
**所以 C 的硬门槛 = 给 ℒₜ 造一个 `toNumVec` 的对偶**，
而它在 Foundation 里不存在，且 `TProof` 层没有承载它的类型。

**治理**：本文件只记查实，不含未证标记。 -/

/-- 查实：`Term V ℒₜ = Semiterm V ℒₜ 0`（`Typed.lean:51`）。 -/
noncomputable example : (Bootstrapping.Term V ℒₛₑₜ) = (Bootstrapping.Semiterm V ℒₛₑₜ 0) := rfl

end GodelQ.CG008N1
