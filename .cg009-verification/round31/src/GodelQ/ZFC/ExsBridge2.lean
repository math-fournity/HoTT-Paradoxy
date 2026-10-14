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

/-- **中间引理（项代换的 iT 相容）**：闭项代换与翻译交换。

`substs1 t p = subst ?[t] p`（自由变量 0 ← t），而 `iT` 把自由变量 x 送到 `eqAtom ^&x`。
闭项 t 的 `iVE 0 t` 是"t 的值 = #0"——见证的载体。

这条是 ExsBridge2 的**实质内容**（`ShCraigElimBranches` 的备忘表里记为
"`iT` 与 `substs1` 的相容 | 不存在"）。 -/
lemma iT_substs1 (p t : V) (hp : IsUFormula ℒₒᵣ p) (ht : IsTerm ℒₒᵣ t) :
    iT (0 : V) (substs1 ℒₒᵣ t p)
      = subst ℒₛₑₜ (iVE (0 : V) t) (iT (1 : V) p) := by
  sorry

/-- **ExsBridge2**（一般 p、一般闭项 t）。 -/
theorem exsBridge2 {p t : V} (hp : IsUFormula ℒₒᵣ p) (ht : IsTerm ℒₒᵣ t) :
    Provable 𝗭𝗙𝗖 (imp ℒₛₑₜ (iT (0 : V) (substs1 ℒₒᵣ t p))
      (^∃ (domZero (V := V) ^⋏ iT (1 : V) p))) := by
  sorry

end GodelQ.ExsBridge2

#print axioms GodelQ.ExsBridge2.exsBridge2
