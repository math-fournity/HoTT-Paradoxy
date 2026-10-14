import GodelQ.ZFC.CG008TargetShape
import Foundation.FirstOrder.Arithmetic.Bootstrapping.DerivabilityCondition.D3

/-!
# CG-008 · 一处自我更正：C 的门槛**不是**「更强的模型前提」

## 被更正的记录

我在 2026-10-13 的 `CG008CLocal.lean` 与记忆 `c-is-tanumvec-dual-hole` 里写下：

> 算术侧 `ORingStructure.numeral` 只要 `[ORingStructure α]`；
> 集合侧同一动作（「V 的元素 ↦ 常项」）要 `V ⊧ 𝗭`，严格强于 C 的前提。
> ⟹ C 有一个**前提差**，且不能靠加强前提消掉。

**该记录过强。本文件机器更正它。**

## 更正的核心事实（机器核对，见下方 theorem）

Foundation 算术侧 Σ₁ 完备性（`D3.lean`）的「把值命名成项」这一步，
载体是 `𝕹`，而

```lean
noncomputable def typedNumeral (m : V) : Semiterm V ℒₒᵣ n := ⟨numeral m, by simp⟩
```

（`Syntax/Term/Typed.lean:358`）——**载体参数 `m : V` 是一个 V 的元素**。
`term_complete`（`D3.lean:46`）的结论右端：

```lean
T.internalize V ⊢ (toNumVec w ⤕ ⌜t⌝) ≐ 𝕹 (Semiterm.valb w t)
```

其中 `Semiterm.valb w t : V`。**在非标准 V 上它就是非标准元素**，
而前提只有 `[ORingStructure V] [V ⊧* 𝗜𝚺₁]`——**没有 `V ⊧ 𝗭`**。

（注意区分：`ORingStructure.numeral : ℕ → α`（`Arithmetic/Basic/Misc.lean:26`）
递归在**标准** ℕ 上；但 `typedNumeral` 把**整个 V 元素**塞进去当载体。
我此前只看了 `numeral`，没看套在外面的 `typedNumeral`——**这就是错的来源**。）

## 更正后，C 的困难是什么

不是「模型的谓词强度」，而是：**集合侧缺一个等价的 carrier**——
即把 V 的元素塞进 `ℒₛₑₜ` 常项位置的机制。

- 这不等于 `ofNat : ℕ → V`（那个是反方向：ℕ → V，且要 `V ⊧ 𝗭`）；
- 它也不等于「更强的前提」——**前提强度是够的**；
- 它等于：`ℒₜ` 侧缺常项（已确认 `IsEmpty (ℒₜ).Func 0`），
  所以「为任意 V 元素造一个闭项」这件算术侧免费的事，集合侧没有对应物。

**这仍然是真困难，但性质不同**：从「前提差（不可弥合）」改为
「缺一个构造机制（库级工作）」——这与 Master 编排文档 §9.15 的 D3 闸门裁决
方向一致（正确工具是 `bold_sigma_one_complete`，它正是在 `T.internalize V ⊢` 层工作）。

## 治理

- Foundation 只读；本文件纯下游。
- 本文件不含任何未证标记，可进收据。
- **不声称 C 已证**；`Z0Blocked.lean:65` 的未证标记仍在。
- 本文件只做**一次自我更正**：把「前提差」降格为「缺构造机制」。 -/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008ThresholdCorrection

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Z0Full GodelQ.Translate

/-- **更正的核心机器事实**：算术侧 Σ₁ 完备性的「换常项」载体取**任意 V 元素**
（含非标准的），前提只有 `ORingStructure V` + `V ⊧* 𝗜𝚺₁`。

这条 type-checks 即证伪「该步需要 `V ⊧ 𝗭`」的记录。
`Semiterm.valb w t : V` 是非标准 V 上的非标准元素时，
`typedNumeral (Semiterm.valb w t)` 依然有意义。 -/
theorem arithmetic_carrier_accepts_nonstandard :
    ∀ {V : Type} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
      (T : ArithmeticTheory) [Theory.Δ₁ T] [𝗣𝗔⁻ ⪯ T] {n : ℕ}
      (t : ClosedSemiterm ℒₒᵣ n) (w : Fin n → V),
      Theory.internalize V T ⊢
        Semiterm.subst (Arithmetic.toNumVec w) ⌜t⌝ ≐
          Arithmetic.typedNumeral (Semiterm.valb w t) := by
  intro V _ _ T _ _ n t w
  exact Arithmetic.term_complete T t w

/-- **`typedNumeral` 的载体参数类型是 `V`**（不是 `ℕ`）：`typedNumeral` 可施加于
任意 `m : V`。本行把一个 V 元素直接塞进 carrier 并编译通过。 -/
example {V : Type} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁] {n : ℕ} :
    (fun m : V => Arithmetic.typedNumeral (V := V) (n := n) m) 0 =
      Arithmetic.typedNumeral (V := V) (n := n) 0 := rfl

end GodelQ.CG008ThresholdCorrection

#print axioms GodelQ.CG008ThresholdCorrection.arithmetic_carrier_accepts_nonstandard
