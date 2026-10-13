import GodelQ.ZFC.CG008RouteB

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008OfNat

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Z0Full GodelQ.ZFCSetInternal

/-! # 更正与再定位：`ofNat` 存在，但要 `V └§ Z`

## 事实（机器核实）

`SetTheory/Z/Z.lean:427`：

```lean
noncomputable def ofNat : ℕ → V
  |     0 => └┐
  | n + 1 => succ (ofNat n)

noncomputable scoped instance (n) : OfNat V n := └ñofNat n└╗
noncomputable scoped instance : NatCast V := └ñofNat└╗
```

**这些定义在 `SetTheory.Z` 段（`V └§ Z`）里**。
本文件的 `V` 只要 `[V └§ 𝗜𝚺칠]`，所以 `ofNat` **拿不到**。

## 我先前说法的更正

我说过「`L_set` 无 numerals」——**太粗**。准确的是：

* `ORingStructure V` 的 `numeral : ℕ → V` 是 **L_or 结构自带**的
  （`Arithmetic/Basic/Misc.lean`），**只要 𝗜𝚺칠** 就能用，`toNumVec` 用的正是它；
* `SetStructure V` 的 `ofNat` **存在**，但**要 `V └§ Z`**，比 C 的前提强。

**所以差别在「前提强度」，不在「有没有」。**

## 净结论（比上一轮更准）

C 的硬门槛不是「`L_set` 没有 numerals」这种不可能性，
而是：**算术版 `term_complete` 靠的是「只要 𝗜𝚺칠 就能把 V 的元素换成常项」，
集合侧同一个替换要 `V └§ Z`。**

这两者的差，正是 `𝗣𝗔⁻ ⪯ 𝗭` 这种「模型更强才有」的东西。

**治理**：本文件只记查实，不含未证标记。 -/

/-- **查实 1**：`[V └§ Z]` 时 `ofNat : ℕ → V` 可用。 -/
noncomputable example (V : Type) [SetStructure V] [Nonempty V] [V↓[ℒₛₑₜ] ⊧* 𝗭𝗙𝗖] :
    ℕ → V := ofNat

/-- **查实 2（本轮要点）**：只有 `[V └§ 𝗜𝚺칠]` 时 `ofNat` **拿不到**。

下面这行**编不过**，保留为注释形式的事实记录：

```lean
-- noncomputable example (V : Type) [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺칠] :
--     ℕ → V := ofNat
-- 错误：failed to synthesize instance of type class
--   V↓[ℒₛₑₜ] ⊧* 𝗭
``` -/
noncomputable example : True := trivial

end GodelQ.CG008OfNat
