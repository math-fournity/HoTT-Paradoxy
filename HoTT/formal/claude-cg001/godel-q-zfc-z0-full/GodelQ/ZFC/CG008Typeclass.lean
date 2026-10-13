import GodelQ.ZFC.CG008Attack

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008Typeclass

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full GodelQ.ZFCSetInternal

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! # 攻硬门槛：那个**缺失的类型类实例**

## 问题（精确化）

`setTheory_sigma₁_induction'` 的 `hEQ`/`hMem` 要求
`∀ n t₁ t₂, 𝗭𝗙𝗖.internalize V ⊢ (.rel Language.Eq.eq ![t₁, t₂])`，
其中 `t₁ t₂ : Semiterm V ℒₛₑₜ n`——**n 个自由变量**。

而 `⊢` 的实例（`Syntax/Proof/Typed.lean:140`）是
`Entailment (InternalTheory V L) (Formula V L)`，
`Formula V L := Semiformula L V 0`——**只到 n = 0**。

**所以缺的不是「n > 0 的实例」这种可自然推广的东西，
而是 `ξ` 也不同**（归纳侧 `ξ` 是任意类型，内部侧 `ξ = V`）。

## 两条路

**路 A（加实例）**：给 `Semiformula V L n` 直接补一个 `Entailment` 实例。
但 `⊢!ᵈᵉʳ` 的定义是 `DerivationOf T val Γ.val`（`Typed.lean:129`），
而 `Γ : Sequent V L` 是**公式集**——自由变量本应由 sequent 承载，
所以「带自由变量的公式」在 Foundation 的推导层**根本没有对应物**；
`⊢` 只对闭句有意义是**设计**，不是遗漏。**路 A 与 Foundation 的设计冲突。**

**路 B（降到 `TDerivation` 层）**：`Sequent V L` 带公式集，
`TProof.specialize!` / `TProof.all!` 可把闭句证明泛化
（`ZFCSetInternal.lean` 的 `set_eq_refl` 等正是这么造的：
先 `complete` 得元层闭句定理，再 `internal_provable_of_outer_provable` + `TProof.specialize!`）。
**`ZFCSetInternal.lean` 已给出路 B 的可用范例。**

## 判定（待机器化）

路 A 撞设计；路 B 有范例。**所以「实例缺失」更像是「我用了错的层」，
而非「Foundation 缺 API」。** 下一步：照 `ZFCSetInternal` 的范例，
把 `set_eq_refl` 从闭项推广到带自由变量的半项。

**治理**：本文件只记查实，不含未证标记。 -/

/-- **查实 1**：闭项版自反性（路 B 的起点，`ZFCSetInternal.lean:90`）。 -/
noncomputable example (t : Term V ℒₛₑₜ) : 𝗭𝗙𝗖.internalize V ⊢ setEq t t :=
  set_eq_refl t

/-- **查实 2**：`⊢` 只认闭句——`n > 0` 时**类型类合成失败**（预期）。

下面这行**编不过**，保留为注释形式的事实记录：

```lean
-- example {n : ℕ} (t : Semiterm V ℒₛₑₜ n) :
--     𝗭𝗙𝗖.internalize V ⊢ setEq t t := set_eq_refl t
-- 错误：failed to synthesize
--   Entailment (InternalTheory V ℒₛₑₜ) (Bootstrapping.Semiformula V ℒₛₑₜ n)
``` -/
noncomputable example (t : Term V ℒₛₑₜ) : 𝗭𝗙𝗖.internalize V ⊢ setEq t t :=
  set_eq_refl t


/-! ## 补记：`substNumerals` 也证伪了「路 A 可行」

`FixedPoint.lean:30`：`substNumerals (phi : V) (v : Fin k → V) : V :=
subst ℒₒᵣ (matrixToVec (fun i ↦ numeral (v i))) phi`。

**它用的正是 `numeral ℒₒᵣ`**——又一次只有 ℒₒᵣ 有。
而它的引理 `substNumerals_app_quote`（`:33`）只给 `v : Fin k → ℕ` 的形状：

```lean
(substNumerals ⌜σ⌝ (v ·) : V) = ⌜((Rew.subst (fun i ↦ ↑(v i))) ▹ σ : ArithmeticSentence)⌝
```

**注意 `ArithmeticSentence`、`↑(v i)`（ℕ→V 的铸造）**——
这条引理说的是「把标准自然数代进**算术**句」，与集合侧无关。

**所以：`substNumerals` 是 Foundation 给出的「参数代入」标准工具，**
**它也只在 ℒₒᵣ 上有。** 这与「`ℒₜ` 无 numerals」是同一事实的第三处印证。

**净结论**：`ξ = V` 的半公式 + 赋值代入，在 Foundation 里
**没有**「`V ⊧/e φ ⟹ Provable 𝗭𝗙𝗖 (φ 代入 e 的码)」这条桥。
造它 = 造 C。**（无未证标记，本文件到此。）** -/

end GodelQ.CG008Typeclass
