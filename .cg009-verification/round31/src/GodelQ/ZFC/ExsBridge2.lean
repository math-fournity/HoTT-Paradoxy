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

/-- **中间引理（项代换的 iT 相容）**：`substs1` 与 `iT` 交换。

`substs1 L t u = subst L ?[t] u` —— 把**绑定变量 0**（bvar）换成项 `t`。
与一般律的 `QvecVOr m = ?[^&0]`（把 bvar 0 换成**自由**变量 `^&0`）是**不同的代入向量**，
故一般律不覆盖它——这正是缺口所在。

按 `iT_free_eq` 的先例，右侧应把 `t` 经 `iVE 0` 送到公式（`iVE 0 t` 描述"t 的值 = #0"），
再代入 `iT 1 p`。

**命名说明**（Master 提醒）：本名与 003 线旧文件 `ITSubsts1.lean` 的 `iT_substs1` **同名不同命题**
（旧的是 `?[^&0]` 自由变量版）。本文件用 `iT_substs1_term` 以区别。 -/
lemma iT_substs1_term (p t : V) (hp : IsUFormula ℒₒᵣ p) (ht : IsTerm ℒₒᵣ t) :
    iT (0 : V) (substs1 ℒₒᵣ t p)
      = subst ℒₛₑₜ (iVE (0 : V) t) (iT (1 : V) p) := by
  have hs1 : substs1 ℒₒᵣ t p = subst ℒₒᵣ (?[t] : V) p := rfl
  rw [hs1]
  trace_state
  sorry

/-- **ExsBridge2**（一般 p、一般闭项 t）。 -/
theorem exsBridge2 {p t : V} (hp : IsUFormula ℒₒᵣ p) (ht : IsTerm ℒₒᵣ t) :
    Provable 𝗭𝗙𝗖 (imp ℒₛₑₜ (iT (0 : V) (substs1 ℒₒᵣ t p))
      (^∃ (domZero (V := V) ^⋏ iT (1 : V) p))) := by
  sorry

end GodelQ.ExsBridge2

#print axioms GodelQ.ExsBridge2.exsBridge2
