import GodelQ.ZFC.ZFCSetSigma1

/-!
# CG-008 · 集合语言的内部演算辅助（ℒₛₑₜ 版的 `EquationalTheory`）

## 本文件要解决的问题

`CG008_HANDOFF_2026-10-11.md` §4.2 把「集合语言的内部化演算辅助
（`eq_refl` / `eq_symm` / `subst_eq` / `K_intro` / `ball_intro` / `bexs_intro` / `ball_replace` 等）
在 Foundation 里只为 `Term V ℒₒᵣ` 定义」列为 §4 路线「构建时最可能卡住的一步」。

**本文件用编译证明这个判断过强了。** 读 `EquationalTheory.lean:36-70` 可见，
`eq_refl` / `eq_symm` / `subst_eq` 的证明套路其实**只依赖三样东西**：

1. `complete T _ fun M _ _ ↦ …` —— 把「每个模型里为真」变成元层推导；
2. `internal_provable_of_outer_provable`（`D1.lean:32`）—— 元层推导 → V 内部可证性；
3. `TProof.specialize!`（`Typed.lean:462`）—— 全称句例化到项。

其中 2、3 **只要求 `T : Theory L` + `[T.Δ₁]`**，与 `L` 无关；
`K_intro` / `A_intro_left` / `A_intro_right` / `TProof.exs!` 同样对任意 `InternalTheory V L` 通用。
唯一 ℒₒᵣ 专属的只有两处：

- **`complete` 的来源**：算术版 `Bootstrapping.complete` 要求 `ArithmeticTheory`；
  集合语言换成 `SetTheory.complete`（`SetTheory/Basic/Misc.lean:269`，只要求 `[𝗘𝗤 _ ⪯ T]`）。
- **等式记号**：`≐`（`Semiterm.equals`）硬接线 `ℒₒᵣ`；集合语言写成
  `Semiformula.rel Language.Eq.eq ![t, u]`。

因此「自建集合语言内部演算」不是从零发明十情形归纳，而是**换掉 `complete` 的来源**。
本文件把这条替代路径固化成可复用的引理。

## 技术要点（编译实证）

`TProof.specialize!` 的结果形状是 `Semiformula.subst w (⌜σ⌝ : Semiformula V L n)`。
要让 `simpa` 把它化到 `setEq t u` 这样的具体形状，**必须给中间 `have` 显式的
typed 类型标注**（`∀¹ (setEq …) : Semiformula V ℒₛₑₜ k`），否则 Lean 会把 `⌜σ⌝`
elaborate 成 untyped 的 `FirstOrder.Semiformula`，`simpa` 就接不上。
这是本文件与 `EquationalTheory.lean` 唯一的写法差异。

## 治理

- Foundation 只读；本文件纯下游。
- 本文件不含任何未证标记，可进入收据。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.ZFCSetInternal

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full GodelQ.ZFCSetSigma1

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- 集合语言的等式原子（`≐` 的 ℒₛₑₜ 版）。 -/
noncomputable abbrev setEq {n : ℕ} (t u : Semiterm V ℒₛₑₜ n) : Semiformula V ℒₛₑₜ n :=
  .rel Language.Eq.eq ![t, u]

/-- 集合语言的「非等式」原子（`≉` 的 ℒₛₑₜ 版）。 -/
noncomputable abbrev setNe {n : ℕ} (t u : Semiterm V ℒₛₑₜ n) : Semiformula V ℒₛₑₜ n :=
  .nrel Language.Eq.eq ![t, u]

/-- 集合语言的成员关系原子。 -/
noncomputable abbrev setMem {n : ℕ} (t u : Semiterm V ℒₛₑₜ n) : Semiformula V ℒₛₑₜ n :=
  .rel Language.Mem.mem ![t, u]

/-! ## 1. 从「集合语言的 ZFC 定理」到「V 内部可证性」

这是全部辅助引理的共同第一步。 -/

/-- **桥梁**：集合语言的 𝗭𝗙𝗖 定理，其编码在 V 内部可证。
由 `internal_provable_of_outer_provable`（只要求 `[𝗭𝗙𝗖.Δ₁]`）给出。 -/
theorem set_outer_to_internal {σ : SetTheorySentence} (h : 𝗭𝗙𝗖 ⊢ σ) :
    𝗭𝗙𝗖.internalize V ⊢ ⌜σ⌝ :=
  internal_provable_of_outer_provable (T := 𝗭𝗙𝗖) (V := V) h

/-- **`SetTheory.complete` 的模型形式**：若一个集合句在 𝗭𝗙𝗖 的每个模型里为真，
它就是 𝗭𝗙𝗖 定理。 -/
theorem set_complete_of_models (σ : SetTheorySentence)
    (H : ∀ (M : Type) [SetStructure M] [Nonempty M] [M↓[ℒₛₑₜ] ⊧* 𝗭𝗙𝗖], M↓[ℒₛₑₜ] ⊧ σ) :
    𝗭𝗙𝗖 ⊢ σ :=
  SetTheory.complete.{0} 𝗭𝗙𝗖 σ H

/-! ## 2. 等式的内部演算（ℒₛₑₜ 版）

逐条对应 `EquationalTheory.lean` 的算术版，只把 `complete` 换成 `SetTheory.complete`、
把 `≐` 换成 `setEq`。 -/

/-- **自反**（算术版 `EquationalTheory.eq_refl`）。 -/
@[simp] theorem set_eq_refl (t : Term V ℒₛₑₜ) : 𝗭𝗙𝗖.internalize V ⊢ setEq t t := by
  have h : 𝗭𝗙𝗖 ⊢ (“∀ x, x = x” : SetTheorySentence) :=
    SetTheory.complete.{0} 𝗭𝗙𝗖 _ fun M _ _ _ ↦ by simp [models_iff]
  have h' : 𝗭𝗙𝗖.internalize V ⊢ (∀¹ (setEq (Semiterm.bvar 0) (Semiterm.bvar 0) :
      Semiformula V ℒₛₑₜ 1)) := by
    simpa using! internal_provable_of_outer_provable (T := 𝗭𝗙𝗖) (V := V) h
  simpa using TProof.specialize! h' t

/-- **对称**（算术版 `EquationalTheory.eq_symm`）。 -/
@[simp] theorem set_eq_symm (t u : Term V ℒₛₑₜ) :
    𝗭𝗙𝗖.internalize V ⊢ setEq t u 🡒 setEq u t := by
  have h : 𝗭𝗙𝗖 ⊢ (“∀ x y, x = y → y = x” : SetTheorySentence) :=
    SetTheory.complete.{0} 𝗭𝗙𝗖 _ fun M _ _ _ ↦ by simp [models_iff]
  have h' : 𝗭𝗙𝗖.internalize V ⊢ (∀¹ (∀¹ (setEq (Semiterm.bvar 1) (Semiterm.bvar 0) 🡒
      setEq (Semiterm.bvar 0) (Semiterm.bvar 1) : Semiformula V ℒₛₑₜ 2) :
      Semiformula V ℒₛₑₜ 1)) := by
    simpa using! internal_provable_of_outer_provable (T := 𝗭𝗙𝗖) (V := V) h
  simpa using TProof.specialize₂! h' u t

/-- **非等式对称**（算术版 `EquationalTheory.ne_symm`）。

**走法**：先证 `∼(setEq t u) 🡒 ∼(setEq u t)`（由 `set_eq_symm u t` 反证律），
再用 `setNe` 与 `∼setEq` 在 `val` 上相同（`Semiformula.neg_rel`）转换。
这样绕开了 `nrel` 编码与 typed quote 的直接对接。 -/
theorem set_neg_eq_symm (t u : Term V ℒₛₑₜ) :
    𝗭𝗙𝗖.internalize V ⊢ ∼(setEq t u) 🡒 ∼(setEq u t) := by
  have h : 𝗭𝗙𝗖.internalize V ⊢ setEq u t 🡒 setEq t u := set_eq_symm u t
  cl_prover [h]

/-- **非等式对称**（`setNe` 形式）。 -/
@[simp] theorem set_ne_symm (t u : Term V ℒₛₑₜ) :
    𝗭𝗙𝗖.internalize V ⊢ setNe t u 🡒 setNe u t := by
  have h := set_neg_eq_symm t u
  convert h using 2 <;> ext <;> simp [setNe, Bootstrapping.Semiformula.neg_rel]

/-- **传递**（算术版 `EquationalTheory.eq_uniform_trans`）。 -/
theorem set_eq_uniform_trans (t₁ t₂ t₃ : Term V ℒₛₑₜ) :
    𝗭𝗙𝗖.internalize V ⊢ setEq t₁ t₂ 🡒 setEq t₂ t₃ 🡒 setEq t₁ t₃ := by
  have h : 𝗭𝗙𝗖 ⊢ (“∀ x y z, x = y → y = z → x = z” : SetTheorySentence) :=
    SetTheory.complete.{0} 𝗭𝗙𝗖 _ fun M _ _ _ ↦ by simp [models_iff]
  have h' : 𝗭𝗙𝗖.internalize V ⊢ (∀¹ (∀¹ (∀¹ (setEq (Semiterm.bvar 2) (Semiterm.bvar 1) 🡒
      setEq (Semiterm.bvar 1) (Semiterm.bvar 0) 🡒
      setEq (Semiterm.bvar 2) (Semiterm.bvar 0) : Semiformula V ℒₛₑₜ 3) :
      Semiformula V ℒₛₑₜ 2) : Semiformula V ℒₛₑₜ 1)) := by
    simpa using! internal_provable_of_outer_provable (T := 𝗭𝗙𝗖) (V := V) h
  simpa using TProof.specialize₃! h' t₃ t₂ t₁

/-- **传递**（推论形式，算术版 `EquationalTheory.eq_trans`）。 -/
theorem set_eq_trans {t₁ t₂ t₃ : Term V ℒₛₑₜ} :
    𝗭𝗙𝗖.internalize V ⊢ setEq t₁ t₂ → 𝗭𝗙𝗖.internalize V ⊢ setEq t₂ t₃ →
    𝗭𝗙𝗖.internalize V ⊢ setEq t₁ t₃ := fun h₁ h₂ ↦
  set_eq_uniform_trans t₁ t₂ t₃ ⨀ h₁ ⨀ h₂

/-- **等号替换**（算术版 `EquationalTheory.subst_eq`）：等式两端可同时换等。 -/
theorem set_subst_eq (t₁ t₂ u₁ u₂ : Term V ℒₛₑₜ) :
    𝗭𝗙𝗖.internalize V ⊢ setEq t₁ t₂ 🡒 setEq u₁ u₂ 🡒 setEq t₁ u₁ 🡒 setEq t₂ u₂ := by
  have h : 𝗭𝗙𝗖 ⊢ (“∀ x₁ x₂ y₁ y₂, x₁ = x₂ → y₁ = y₂ → x₁ = y₁ → x₂ = y₂” : SetTheorySentence) :=
    SetTheory.complete.{0} 𝗭𝗙𝗖 _ fun M _ _ _ ↦ by simp [models_iff]
  have h' : 𝗭𝗙𝗖.internalize V ⊢
      (∀¹ (∀¹ (∀¹ (∀¹ (setEq (Semiterm.bvar 3) (Semiterm.bvar 2) 🡒
        setEq (Semiterm.bvar 1) (Semiterm.bvar 0) 🡒
        setEq (Semiterm.bvar 3) (Semiterm.bvar 1) 🡒
        setEq (Semiterm.bvar 2) (Semiterm.bvar 0) : Semiformula V ℒₛₑₜ 4) :
        Semiformula V ℒₛₑₜ 3) : Semiformula V ℒₛₑₜ 2) : Semiformula V ℒₛₑₜ 1)) := by
    simpa using! internal_provable_of_outer_provable (T := 𝗭𝗙𝗖) (V := V) h
  simpa using TProof.specialize₄! h' u₂ u₁ t₂ t₁

/-! ### 引号原子的求值辅助

`SetTheory.complete` 的语义义务里，`“#3 ∈ #1”` 这类**带编号变量的引号**
在 `Semiformula.Eval` 下不会自动化简。下面两条把引号结构展开到
`standardStructure` 的 `∈` / `=`，供后面的成员替换引理使用。 -/

section QuoteEval

variable {M : Type*} [SetStructure M] {n : ℕ}

/-- 引号原子的求值：`“#a ∈ #b”` 在 `v` 下等于 `v a ∈ v b`。
这一条把 `rewAux`/`Rew.emb` 的引号结构展开到 `standardStructure` 的 `∈`。 -/
@[simp] lemma eval_quote_mem (v : Fin n → M) (a b : Fin n) :
    (Semiformula.Eval v Empty.elim) (“#a ∈ #b” : Semiformula ℒₛₑₜ Empty n) ↔ v a ∈ v b := by
  simp [FirstOrder.Semiformula.eval_rel]

/-- 引号原子的求值（等式）。 -/
@[simp] lemma eval_quote_eq (v : Fin n → M) (a b : Fin n) :
    (Semiformula.Eval v Empty.elim) (“#a = #b” : Semiformula ℒₛₑₜ Empty n) ↔ v a = v b := by
  simp [FirstOrder.Semiformula.eval_rel]

end QuoteEval

/-- **成员关系的等号替换**（元层版本）：`x₁ = x₂ → y₁ = y₂ → x₁ ∈ y₁ → x₂ ∈ y₂`。

这是集合语言相对算术语言**新增**的一条（`ℒₒᵣ` 没有 `∈`）。
先在 𝗭𝗙𝗖 的外部层证明（走 `SetTheory.complete`），再内部化。 -/
theorem set_mem_subst_outer :
    𝗭𝗙𝗖 ⊢ (“∀ x₁ x₂ y₁ y₂, x₁ = x₂ → y₁ = y₂ → x₁ ∈ y₁ → x₂ ∈ y₂” : SetTheorySentence) := by
  apply SetTheory.complete.{0} 𝗭𝗙𝗖 _
  intro M _ _ _
  simp only [models_iff, FirstOrder.Semiformula.eval_all,
    LogicalConnective.HomClass.map_imply, LogicalConnective.Prop.arrow_eq]
  intro a b c d hab hcd hmem
  rw [eval_quote_eq] at hab hcd
  rw [eval_quote_mem] at hmem ⊢
  rw [hab, hcd] at hmem
  exact hmem

/-- **成员关系的等号替换**（内部化版本）。 -/
theorem set_subst_mem (t₁ t₂ u₁ u₂ : Term V ℒₛₑₜ) :
    𝗭𝗙𝗖.internalize V ⊢ setEq t₁ t₂ 🡒 setEq u₁ u₂ 🡒 setMem t₁ u₁ 🡒 setMem t₂ u₂ := by
  have h' : 𝗭𝗙𝗖.internalize V ⊢
      (∀¹ (∀¹ (∀¹ (∀¹ (setEq (Semiterm.bvar 3) (Semiterm.bvar 2) 🡒
        setEq (Semiterm.bvar 1) (Semiterm.bvar 0) 🡒
        setMem (Semiterm.bvar 3) (Semiterm.bvar 1) 🡒
        setMem (Semiterm.bvar 2) (Semiterm.bvar 0) : Semiformula V ℒₛₑₜ 4) :
        Semiformula V ℒₛₑₜ 3) : Semiformula V ℒₛₑₜ 2) : Semiformula V ℒₛₑₜ 1)) := by
    simpa using! internal_provable_of_outer_provable (T := 𝗭𝗙𝗖) (V := V) set_mem_subst_outer
  simpa using TProof.specialize₄! h' u₂ u₁ t₂ t₁

/-! ## 3. 命题连接词与量词（对 `L` 通用，直接可用）

这些来自 `Entailment.Minimal` 的 `InternalTheory V L` 实例，**无需自建**。 -/

theorem set_K_intro (φ ψ : Formula V ℒₛₑₜ)
    (hφ : 𝗭𝗙𝗖.internalize V ⊢ φ) (hψ : 𝗭𝗙𝗖.internalize V ⊢ ψ) :
    𝗭𝗙𝗖.internalize V ⊢ φ ⋏ ψ :=
  K_intro hφ hψ

theorem set_A_intro_left (φ ψ : Formula V ℒₛₑₜ) (hφ : 𝗭𝗙𝗖.internalize V ⊢ φ) :
    𝗭𝗙𝗖.internalize V ⊢ φ ⋎ ψ :=
  A_intro_left hφ

theorem set_A_intro_right (φ ψ : Formula V ℒₛₑₜ) (hψ : 𝗭𝗙𝗖.internalize V ⊢ ψ) :
    𝗭𝗙𝗖.internalize V ⊢ φ ⋎ ψ :=
  A_intro_right hψ

theorem set_exs_intro (φ : Semiformula V ℒₛₑₜ 1) (t : Term V ℒₛₑₜ)
    (h : 𝗭𝗙𝗖.internalize V ⊢ φ.subst ![t]) :
    𝗭𝗙𝗖.internalize V ⊢ ∃¹ φ :=
  TProof.exs! t h

end GodelQ.ZFCSetInternal
