import GodelQ.ZFC.CG008Precise

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008Attack

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full GodelQ.CG008Precise GodelQ.ZFCSetInternal

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! # C 的攻击方案：要造它需要哪三样东西

## 目标（一句话）

```lean
theorem C (sigma : ArithmeticSentence) :
    Provable 𝗭𝗙𝗖 (⌜arithTrln.translate sigma⌝ : V) 🡒
      Provable 𝗭𝗙𝗖 (⌜arithTrln.translate (zfcTr sigma)⌝ : V)
```

## 为什么不能照搬算术版

算术版 `provable_internalize`（`D3.lean:175`）的证明链是：

```lean
sigma_one_complete (T := T) (σ := provabilityPred T σ)
  : V ⊧ provabilityPred T σ 🡒 Provable T ⌜provabilityPred T σ⌝
```

再往下是 `bold_sigma_one_complete`，它跑 `arithmetic_sigma₁_induction` 的**十情形**，
其中原子情形靠 `term_complete` + `toNumVec`：
把 V 的元素代换成**数字项** `𝕹 v`。

**`toNumVec` 是 ℒₒᵣ 专属**（`Arithmetic/Basic/Misc.lean` 的 `ORingStructure.numeral`）。
`ℒₜ` 无 numerals，所以这一整条链在集合侧**没有对偶**。

## 要造 C 需要的三样东西

### 第一样：`zfc_sigma1_internalize` 的集合侧归纳

Foundation **有骨架**：`lévy_sigma_succ_induction`
（`SetTheory/Definability/Definable.lean:66`），谓词吃层数，
与算术版 `arithmetic_sigma₁_induction` 同型。

**要补的**：把谓词实例化为 `fun n phi ↦ (V ⊧ phi 🡒 Provable 𝗭𝗙𝗖 ⌜phi⌝)`，
逐个给八个情形。其中**最难的两个仍是原子情形** `hEQ` / `hMem`。

### 第二样：原子情形的 `toNumVec` 对偶——** witness 代入**

算术版把 `t.valb w`（一个 ℕ）代成 `𝕹 (t.valb w)`。
集合侧的对偶：把 `t.val e`（一个 `V` 的元素）代成 **`t` 自己算出来**，
即 ZFC 内部要能证 `⌜t = t.val e⌝`——这是 **`set_subst_eq` 一类引理**
（`ZFCSetInternal.lean:144` 已有 `set_subst_eq`！）。

**关键差别**：算术版的 `𝕹 v` 是**常项**，所以 `toNumVec w ⤕ ⌜t⌝ = 𝕹 (t.valb w)`
是 `T.internalize V ⊢` 的一条等式公理。集合侧没有常项，
只能用**带自由变量的 `set_subst_eq`** 再全称闭包——
这正是本会话查实的**第一个障碍**（`⊢` 只对闭句有实例）。

### 第三样：把 `Provable 𝗭𝗙𝗖 x` 的 Σ₁ 性接进 `lévy` 层级

`Provable 𝗭𝗙𝗖 x := ∃ d, Proof 𝗭𝗙𝗖 d x`（`Proof/Basic.lean:541`），
而 `proof 𝗭𝗙𝗖` 是 `𝚫ᴬ₁.Semisentence 2`（同文件 `:552`）——
所以 `Provable 𝗭𝗙𝗖 ·` 本身是 **Σ₁ 的算术式**，但它谈论的是 **ℒₜ 推导**。

`lévy` 层级对 `Operator.Mem.mem` 与 `Language.Eq.eq` 封闭，
而 `provable 𝗭𝗙𝗖` 是一个**算术** Σ₁ 公式，与 ℒₜ 的两个谓词都不同。
**要补**：一条把 `provable 𝗭𝗙𝗖` 表达成 `lévy` 层级内公式的桥。

## 三样的共同瓶颈

**第二样是硬的**：它要求的正是 `set_subst_eq` 从闭项到带自由变量半项的推广，
而这一跳卡在**类型类实例缺失**（`Entailment (InternalTheory V ℒₜ) (Semiformula V ℒₜ n)` 不存在），
不是证明技巧问题。要么在 Foundation 层加实例，要么改用 `DerivationOf`/`TDerivation` 层。

## 治理

- Foundation 只读；本文件纯下游。
- 本文件只记方案与已核实的工具位置，不含未证标记。 -/

/-! ### 方案里用到的既有工具，逐个核实可引用 -/

/-- 工具 1：`set_subst_eq` 已在本包（`ZFCSetInternal.lean:144`，**闭项**版）。 -/
noncomputable example (t1 t2 u1 u2 : Term V ℒₛₑₜ)
    (h1 : 𝗭𝗙𝗖.internalize V ⊢ setEq t1 t2)
    (h2 : 𝗭𝗙𝗖.internalize V ⊢ setEq u1 u2) :
    𝗭𝗙𝗖.internalize V ⊢ setEq t1 u1 🡒 setEq t2 u2 :=
  set_subst_eq t1 t2 u1 u2 ⨀ h1 ⨀ h2

/-- 工具 2：`set_complete_of_models`（`ZFCSetInternal.lean:79`）——语义路线的入口。 -/
noncomputable example {sigma : SetTheorySentence}
    (H : ∀ (M : Type) [SetStructure M] [Nonempty M] [M↓[ℒₛₑₜ] ⊧* 𝗭𝗙𝗖], M↓[ℒₛₑₜ] ⊧ sigma) :
    𝗭𝗙𝗖 ⊢ sigma :=
  set_complete_of_models sigma H

end GodelQ.CG008Attack
