import GodelQ.ZFC.CG008Probe7

/-!
# CG-008 · 原始层（`Derivable`）作为绕过自由变量障碍的通道

## 为什么这条路可能行

`CG008MemCase.lean` 定下障碍：算术版 `bold_sigma_one_complete`（`D3.lean:82`）的 `P`
用 `toNumVec w ⤔ ⌜φ⌝` 把自由变量的值**命名成数字项**，落回闭句层；
`ℒₛₑₜ` 无常项与函数符号，这一步无对偶。

但读 `Syntax/Proof/Basic.lean:935` 发现一条此前未用的通道：

```lean
lemma internal_provable_iff_internal_derivable {φ : V} :
    Provable T φ ↔ Derivable T (insert φ ∅ : V)
```

`Derivable`（`Basic.lean:537`）作用在**编码的序列** `s : V` 上，不是 typed `Formula`。
它的规则 API（`Basic.lean:786-937`）只要求 `T.Δ₁Class`。探针 6 已查实这些规则
对 `𝗭𝗙𝗖` 全部可用。

**关键**：`Derivable` 层没有「自由变量」这个概念——它只有编码。
所以 Σ₁ 完全性若在这个层做，「把自由变量的值命名成项」的障碍**可能根本不存在**。

## 本文件做什么

把两个层之间的**桥**固定下来：typed 层（`ZFCSetInternal.lean` 的 13 条引理的结论形状）
与编码层（`Derivable`）**等价**。这是「下沉」的合法性依据。

**性能注记**（编译实证，见 `CG008Probe7.lean`）：两座桥**单独**都很快；
把它们**串起来**（`mp` 套 `mp`）会让 elaboration 在 `whnf` 上超时。
下面的写法把两座桥拆成独立的 `have`，让 Lean 逐段确定类型。

## 治理

- Foundation 只读；本文件纯下游。
- 本文件不含任何未证标记，可进入收据。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008Raw

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full GodelQ.ZFCSetSigma1
  GodelQ.ZFCSetInternal GodelQ.CG008Reduce GodelQ.CG008SetAll

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **typed 层的内部可证性 ⇒ 编码层的 `Derivable`**。

两个层之间的桥：`ZFCSetInternal.lean` 的 13 条引理结论都是
`𝗭𝗙𝗖.internalize V ⊢ φ`（typed 层，`φ : Formula V ℒₛₑₜ`），
而 `Derivable` 要的是编码。分两步走，每步都标注中间类型。 -/
theorem internal_derivable_of_tprovable {φ : Formula V ℒₛₑₜ}
    (h : 𝗭𝗙𝗖.internalize V ⊢ φ) : Derivable 𝗭𝗙𝗖 (insert φ.val ∅ : V) := by
  have h₁ : Provable 𝗭𝗙𝗖 φ.val := (tprovable_iff_provable (T := 𝗭𝗙𝗖) (V := V)).mp h
  exact internal_provable_iff_internal_derivable.mp h₁

/-- **反向**：编码层的 `Derivable` ⇒ typed 层的内部可证性。
两个方向都是通用引理，所以这两层**等价**——这就是「下沉」的合法性。 -/
theorem tprovable_of_internal_derivable {φ : Formula V ℒₛₑₜ}
    (h : Derivable 𝗭𝗙𝗖 (insert φ.val ∅ : V)) : 𝗭𝗙𝗖.internalize V ⊢ φ := by
  have h₁ : Provable 𝗭𝗙𝗖 φ.val := internal_provable_iff_internal_derivable.mpr h
  exact (tprovable_iff_provable (T := 𝗭𝗙𝗖) (V := V)).mpr h₁

end GodelQ.CG008Raw
