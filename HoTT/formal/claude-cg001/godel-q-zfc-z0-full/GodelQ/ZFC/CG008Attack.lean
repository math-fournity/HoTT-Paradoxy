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


/-! ### 舰队对表补入（012-Flash 情报，本会话已独立核验路径）

**两个方向，一易一难**（012-Flash 探路，我核验了引理路径与签名）：

**方向 1（易，已证于其探针）**：`p x → (codeOfREPred p).Evalb (M := V) ![(x:V)]`。
走 `codeOfREPred_spec`（`NAT` 层）再抬到任意 `V ⊨ ` + IS1 + u`，用 Foundation 的
`sigmaOne_upward_absolute`（`Arithmetic/Definability/Absoluteness.lean:78`，
**本会话核实存在，签名 `phi.Evalb v → phi.Evalb (M := V) (Nat.cast ∘ v)`**）。

**方向 2（难，且不能走同一条路）**：`V ⊧ Evalb → p x`。
**是数学事实而非工程难度**：V 可非标准，`Evalb` 的见证可能非标准；
`codeOfPartrec'_spec`（`R0/Representation.lean:271`）**`NAT`-only**；
模型层 `code`/`code_uniq`（281–341）**只给唯一性**。

**对 C 的方案的意义**：C 要的正是**方向 2 形状**的东西
（从 V 手里的见证反推标准事实）。012-Flash 的建议：
* 优先**绕开 `codeOfREPred`**，改用 `reWitness`/`reCh` 的 Σ₁ 定义——
  **`reWitness_spec` 本身就是 V 层**的现成件
  （`CraigTrick.lean:106`，签名 `V ⊧/e T.reCh.val ↔ ∃ w, V ⊧/(w :> e) T.reWitness.val`，
  **本会话核实存在且确为 V 层**）；
* 若坚持走 `codeOfREPred`，只剩 `codeAux` 的模型层归纳，代价高得多。

**另一条提醒（012-Flash）**：`Sh.reCh.val` 与 `trProv` **内容相同、不是同一公式**，
无论走哪条都要补一条「语义相同」的桥。 -/

/-! ### 核验：方向 1 的抬升工具确实存在 -/

/-- **查实**：`sigmaOne_upward_absolute`——Σ₁ 沿 `natCastEmbedding` 上升。 -/
noncomputable example {k : ℕ} (phi : 𝚺ᴬ₁.Semisentence k)
    (v : Fin k → ℕ) (h : phi.val.Evalb v) :
    phi.val.Evalb (M := V) (Nat.cast ∘ v) :=
  sigmaOne_upward_absolute (V := V) phi v h

/-- **查实**：`reWitness_spec` 是 **V 层**的（不是 ℕ 层）。 -/
noncomputable example (e : Fin 1 → V) :
    V↓[ℒₒᵣ] ⊧/e Sh.reCh.val ↔ ∃ w, V↓[ℒₒᵣ] ⊧/(w :> e) Sh.reWitness.val :=
  Theory.reWitness_spec Sh V e

end GodelQ.CG008Attack
