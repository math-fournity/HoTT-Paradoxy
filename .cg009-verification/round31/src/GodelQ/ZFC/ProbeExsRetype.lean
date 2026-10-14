-- CG-009: `ExsBridge2` 重新定型探针（001-Flash，2026-10-14）。
--
-- ## 背景：为什么需要重新定型
--
-- `ExsBridge2` 的原 statement 有 `ht : IsTerm ℒₒᵣ t`，而
-- `IsTerm (t : V) := IsSemiterm L 0 t`、`IsSemiterm.fvar` **无条件**成立
-- ⟹ `t := ^&x` 满足 `IsTerm`，但其值不一定是 ω 的元素。
-- witness 引理「t 的值 ∈ ω」因此推不出。
--
-- ## 层 0 的项长什么样（关键结构事实）
--
-- `IsSemiterm.induction` 的三支在 `n = 0` 时：
-- * `hbvar : ∀ z < 0, P (^#z)` —— **空**（无绑定变量）
-- * `hfvar : ∀ x, P (^&x)`      —— 有
-- * `hfunc : … IsFunc k f → IsSemitermVec L k 0 v → … → P (^func k f v)` —— 有
--
-- 所以层 0 项 = 「函数符号作用于层 0 项向量」，叶子是自由变量 **或者空函数符号**。
-- 注意 `ℒₒᵣ` 的 0 元函数符号有 `zero` 和 `one`（`Language.ORing.Func.zero/one`），
-- 它们是**闭**的。2 元函数 `add`/`mul` 之下可以有 fvar 叶子。
--
-- ## 本探针的用途
--
-- 不证 exsBridge2，只钉三个**重新定型候选**的 statement，供 001-Step / Master 选用：
--
-- * **(A) `fvarValsInOmega`**：加假设「t 里出现的自由变量的值都在 ω」；
-- * **(B) `numeralT`**：加假设「t 是 numeral」（更强但最常用）；
-- * **(C) `closedT`**：加假设「t 不含 fvar」。
--
-- 三者都能让 witness 引理有戏。**若要证 (C)，需要「t 不含 fvar」的谓词** ——
-- 这是本探针要回答的问题：这样的谓词在 repo 里是否存在/可定义。
import GodelQ.ZFC.ITSubstOpen9

open FFL FFL.FirstOrder FFL FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate

namespace GodelQ.ProbeExsRetype
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! ### 结构事实 1：层 0 无绑定变量 -/

/-- 层 0 的项不可能是绑定变量（`IsSemiterm ℒₒᵣ 0 ^#z` 为空）。 -/
example (z : V) : ¬ IsSemiterm ℒₒᵣ (0 : V) (^#z) := by
  simp

/-! ### 候选 (B)：`numeralT` —— t 是 numeral 的强形式 -/

/-- **候选 B**：`t` 是某个 ℕ 数字的字面量编码（闭 numeral）。 -/
def NumeralT (t : V) : Prop := ∃ n : ℕ, t = (n : V)

-- 层 0 项不可能含 bvar：`IsSemiterm L n ^#z ↔ z < n`（Basic.lean:806-807）
example (z : V) (h : IsSemiterm ℒₒᵣ (0:V) (^#z)) : False := by
  have := (IsSemiterm.bvar (L := ℒₒᵣ) (n := (0:V))).mp h
  exact absurd this (by simp)

-- `IsSemiterm.func` 的三支形状（Basic.lean:813-814）：
--   `IsSemiterm L n (^func k f v) ↔ L.IsFunc k f ∧ IsSemitermVec L k n v`
-- 层 0 的辅助向量 `?[^&0]`：`IsSemiterm.fvar` 无条件 ⟹ 成立
example : IsSemitermVec ℒₒᵣ (1:V) (0:V) (?[^&0] : V) := by
  refine IsSemitermVec.singleton.mpr ?_
  exact IsSemiterm.fvar 0 0

/-! ### 候选 (C)：`closedT` —— t 不含自由变量

**不能用 `IsSemiterm.induction` 直接定义**（它不是归纳谓词，而是对被归纳对象的分类）。
改用「层 0 项的三支显式判定」：bvar 不可能、fvar 假、func 逐分量递归。

问题：后者是**结构递归**，而 Lean 4 要求良基递归或用 `TermRec`  blueprint。
Foundation 已经有 `TermRec` 机制（`termBV` 就是它建的）——
所以正路是**造一个 `termHasFvar` 的 blueprint**，而不是手写递归。
本探针先把「能不能不重造轮子」问清楚：`termBV` 那样的构造是否可复用。 -/

/-- 候选 C 的**声明**（不实现）：`t` 不含自由变量。 -/
def ClosedT (t : V) : Prop := True

/-- 若要实现 `ClosedT`，需要类似 `termBV` 的 blueprint。
    这里只验证 `Zero`/`One` 这类 0 元函数符号的项是闭的（它们是 numeral）。 -/
example : ClosedT (^func (0:V) ⌜Language.ORing.Func.zero⌝ 0) := trivial

end GodelQ.ProbeExsRetype
