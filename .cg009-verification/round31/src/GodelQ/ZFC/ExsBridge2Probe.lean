-- CG-009: ExsBridge2 的**决定性探针**：t 含自由变量时，蕴含是否假？
--
-- 背景（Master 转述 + 我核源码）：
-- * `IsTerm ℒₒᵣ t := IsSemiterm ℒₒᵣ 0 t` 的 `bv : termBV L t ≤ 0` **只约束 bvar**；
-- * Foundation `IsSemiterm.fvar (n x)` **无条件**成立 ⟹ `IsTerm ℒₒᵣ (^&x)` 成立；
-- * Foundation 的 `exsIntro` blueprint 也只要求 `isSemiterm 0 t`，**没加** FVFree。
--   故 `ExsBlockerQ` 的 `IsTerm ℒₒᵣ t` 是对 Foundation 规则的忠实照抄。
--
-- 本探针检验：取 t = ^&0（含自由变量），命题
--     Provable (imp (iT 0 (substs1 t p)) (^∃ (domZero ^⋏ iT 1 p)))
-- 在语义上是否成立。若 t 的值不在 ω 中，右边的 ∃ 可为假，而左边可真 ⟹ **蕴含假**。
import GodelQ.ZFC.ExsBridge2

open FFL FFL.FirstOrder FFL FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate

namespace GodelQ.ExsBridge2Probe

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! ## 事实 1：`IsTerm` 不排除自由变量（Foundation `IsSemiterm.fvar` 无条件） -/

example (x : V) : IsTerm ℒₒᵣ (^&x : V) := IsSemiterm.fvar 0 x

/-! ## 事实 2：`substs1 t p = subst ℒₒᵣ ?[t] p`（Foundation `Functions.lean:797`） -/

example (x : V) (p : V) : substs1 ℒₒᵣ (^&x : V) p = subst ℒₒᵣ ((^&x : V) ∷ (0 : V)) p := rfl

/-! ## 事实 3：`iT` 把自由变量 x 送到 `eqAtom ^&x`（`iVE_fvar`）

即 `iVE n (^&x) = eqAtom ^&x`——这解释了为什么 t 含 fvar 时，
`iT 0 (substs1 t p)` 里会出现"t 的值 = #0"这个等式，
而它的真假取决于 fvar 的值；若该值不在 ω，则存在见证不在 ω 中。

本文件只固定事实；结论由 `ExsBridge2` 的桥是否可证来判定。
-/

example (x : V) : iVE (0 : V) (^&x : V) = eqAtom (^&x : V) := iVE_fvar 0 x

end GodelQ.ExsBridge2Probe
