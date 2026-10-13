import GodelQ.ZFC.CG008OfNat

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008CLocal

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Z0Full

/-! # C 的定位：一条可编译的最小命题

## 命题 `C_loc`（精确陈述，不需反证）

```lean
theorem C_loc :
    (∀ (V : Type) [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁],
       ∀ sigma : ArithmeticSentence,
         Provable 𝗭𝗙𝗖 (⌜arithTrln.translate sigma⌝ : V) 🡒
           Provable 𝗭𝗙𝗖 (⌜arithTrln.translate (zfcTr sigma)⌝ : V))
      ↔
    (∀ (V : Type) [SetStructure V] [Nonempty V] [V↓[ℒₛₑₜ] ⊧* 𝗭𝗙𝗖],
       ∀ sigma : ArithmeticSentence,
         Provable 𝗭𝗙𝗖 (⌜arithTrln.translate sigma⌝ : V) 🡒
           Provable 𝗭𝗙𝗖 (⌜arithTrln.translate (zfcTr sigma)⌝ : V))
```

**这不是定理**——它把 C 的两侧写成「同一断言在两种模型类下」。
本文件把它作为**定位记录**钉住：

* 右侧**可期**：在 `V └§ 𝗭` 下 `ofNat : ℕ → V` 可用，
  「V 的元素 ↦ 常项」的代入有了载体，算术版 `term_complete` 的集合对偶**有希望照搬**；
* 左侧**是 C 本身**：只要 `V └§ 𝗜𝚺칠`，`ofNat` 拿不到。

## 判断（给舰队的 practical / impractical）

**PARTIAL-PRACTICAL（分两半）**：

* **右侧 practical**：`V └§ 𝗭` 下 `ofNat` + `omega` 的闭包性质
  （`add_mem_omega`/`mul_mem_omega`，本包 `ArithInterp.lean` 已用）
  给出集合侧 toNumVec 所需的全部零件。**这一半是可写的工作。**
* **左侧 impractical（我的判断）**：Z0 的结论形状是「任意 `V └§ 𝗜𝚺칠`」，
  所以**不能**把 `V └§ 𝗭` 补进前提——那会改变结论的适用范围。
  **要弥合 `𝗜𝚺칠` 与 `𝗭` 之差，需要的是「在 `𝗜𝚺칠` 模型内部重建 omega 的闭包」，
  而那件事的数学内容 = C 本身。**

**所以这不是「补一个 Foundation 层」能了事的，也不是「一座不可逾越的墙」**——
它的准确形状是：**一条前提差，且该前提差不能靠加强前提消掉。**

## 治理

- Foundation 只读；本文件纯下游。
- 本文件**不含未证标记**，只记定位与判断。
- **不声称 C 不可能**；只声称「在当前 Foundation API 下，左侧缺一个层」。 -/

/-- 记 1：右侧成立所需的前提（`V └§ 𝗭`）在 Foundation 里自洽——`ofNat` 可用。 -/
noncomputable example (V : Type) [SetStructure V] [Nonempty V]
    [V↓[ℒₛₑₜ] ⊧* 𝗭𝗙𝗖] : ℕ → V := ofNat

end GodelQ.CG008CLocal
