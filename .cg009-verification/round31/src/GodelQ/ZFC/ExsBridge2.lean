-- CG-009: **ExsBridge2** —— hExs 的唯一剩余义务（一般 p）。
--
--      ExsBridge2 : ∀ {p t}, IsUFormula ℒₒᵣ p → IsTerm ℒₒᵣ t →
--          Provable 𝗭𝗙𝗖 (imp ℒₛₑₜ (iT 0 (substs1 ℒₒᵣ t p)) (^∃ (domZero ⋏ iT 1 p)))
--
-- 语义：`p[t] → ∃x∈ω p(x)`——t 的值就是那个见证。
-- 与 sequent 里的 ∃ 公式**同形**，不需见证项（这是 004-Step 修正的关键）。
--
-- 归约已就位（004-Step 证）：`exsBlockerQ_of_bridge2 : ExsBridge2 → ExsBlockerQ`。
--
-- ## 技术要点（开工前的判断）
--
-- `substs1 t p = subst ?[t] p`（自由变量 0 ← 项 t），**不是**一般律的 `QvecVOr m`
-- （那是 `?[^&0]`，也是自由变量但向量形状不同）。故一般律不能直接用，
-- 需"任意项代换"版：`iT 0 (subst ?[t] p)` 与 `iT 1 p` 在 t 的值处的相容。
--
-- `iVE` 把项送到公式：bvar z → eqAtom ^#(z+1)，fvar x → eqAtom ^&x。
-- 闭项 t 的 `iVE 0 t` 是"t 的值等于 #0"的公式——这就是见证的载体。
import GodelQ.ZFC.ITSubstOpen9

open FFL FFL.FirstOrder FFL FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate

namespace GodelQ.ExsBridge2

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! ## ⚠ 撤回：等式的"中间引理"是**假的**（2026-10-14 自查）

我最初写下：
```
lemma iT_substs1_term : iT 0 (substs1 t p) = subst ℒₛₑₜ (iVE 0 t) (iT 1 p)   ✗ 撤回
```
**它是错的，且与 `ITSubstCounter.lean` 已机器证伪的形状同型**：

* `subst (w p : V)` 的第一个参数 `w` 必须是**项向量**（`IsUTermVec`）；
* 而 `iVE n t` 的输出是**公式**（`iVE_bvar` 给 `eqAtom ^#(z+1)`，`iVE_fvar` 给 `eqAtom ^&x`，
  `iVE_func` 给 `ve2`——全是公式），**不是项向量**。
* 故 `subst (iVE 0 t) ·` 在语义上是错的——把公式码当向量用。

`ITSubstCounter.naive_law_is_false_shape` 已把这一现象机器化：
`iVE 0 (termSubst ?[^&0] ^&x) = eqAtom ^&x`，但 `subst ?[^&0] (iVE 1 ^&x) = ^rel 2 cEqN [^&0, ^&x]`——
**两者不等**，因为代入打到了 `eqAtom` 自己的绑定变量上。

**结论（与 `ITSubstCounter` 的结论一致）**：hExs 的剩余义务是**蕴含式**（Σ1 范围），
**不是等式**。所以 `ExsBridge2` 的蕴含形状（本文件主体）**就是正确的最终形状**，
不应再拆出等式版中间引理——那条路是死的。

正确的分解方向是**直接证蕴含**：
```
iT 0 (substs1 t p)  ⟹  ^∃ (domZero ⋏ iT 1 p)
```
其内容 = "t 的值（由 `iVE 0 t` 描述）落在 ω 里，故存在见证"，
走 `Derivable.exsIntro` + 闭项值的标准性（`IsTerm` ⟹ 标准形）。
-/

/-- **ExsBridge2**（一般 p、一般闭项 t）。 -/
theorem exsBridge2 {p t : V} (hp : IsUFormula ℒₒᵣ p) (ht : IsTerm ℒₒᵣ t) :
    Provable 𝗭𝗙𝗖 (imp ℒₛₑₜ (iT (0 : V) (substs1 ℒₒᵣ t p))
      (^∃ (domZero (V := V) ^⋏ iT (1 : V) p))) := by
  sorry

end GodelQ.ExsBridge2

#print axioms GodelQ.ExsBridge2.exsBridge2
