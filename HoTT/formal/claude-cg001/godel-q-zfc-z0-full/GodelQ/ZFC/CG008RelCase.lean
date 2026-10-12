import GodelQ.ZFC.CG008LvlInduction

/-!
# CG-008 探针（非收据）：`rel`/`hnrel` 两情形要什么

## `iT_rel` 给出的

```lean
lemma iT_rel {n k R v : V} (hR : (ℒₒᵣ).IsRel k R) (hv : IsUTermVec ℒₒᵣ k v) :
    iT n (^rel k R v) = ?     -- 见 InternalTranslate.lean:538
```

**目标**：`IsUFormula ℒₛₑₜ (iT n (^rel k R v))`。

由 `iT_rel`，右边是 `iTR n k R v`——其定义（`:196`）：
`qqAlls (imp (conjunct 2 n 0 (iVE n v₀) ⋏ (conjunct 2 n 1 (iVE n v₁) ⋏ ⊤)) (subst ... (cRel R))) 2`

**即**：`∀∀ (… 🡒 R'(#0,#1))`——**一个集合语言的公式**。

**所以 `IsUFormula` 应当成立**，只要各构件都是公式：
`qqAlls`（量词）、`imp`、`conjunct`、`iVE`（项翻译）、`cRel`、`subst`。

## 本探针

查实各构件的 `IsUFormula` 引理是否就位。 -/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping
open FFL.Entailment
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008RelCase

open GodelQ.Translate (iT iTR)

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **查实 1**：`iTR` 是集合语言公式的码——`qqAlls` 构造的。 -/
noncomputable example (n k R v : V) : V := iTR n k R v

/-- **查实 2（要的引理）**：`iTR n k R v` 满足 `IsUFormula`。

**这是 `rel` 情形所需**——本行固定其形状。

**已查（按本轮教训先查 Foundation 与本包）**：
`InternalTranslate.lean` 里**没有** `IsUFormula (iT …)` 形式的引理；
`iT_rel`/`iT_nrel`/`iT_and`/`iT_or`/`iT_all`/`iT_exs`（`:538-570`）都是**等式**，
不是 `IsUFormula` 判定。

**所以 `rel` 情形要新建一条引理**：
「`iTR n k R v` 是集合语言公式」——
由 `iTR` 的定义（`:196`，`qqAlls` 构造）与各构件的公式性拼出。
**这是本会话第一次遇到确实需要新建的零件**（前两次都发现 Foundation 已有）。 -/
example (n k R v : V) : Prop := Bootstrapping.IsUFormula ℒₛₑₜ (iTR n k R v)

/-! ## 试建：`iTR` 的 `IsUFormula` 引理

**由 `iTR` 的定义**（`InternalTranslate.lean:196`）：

```
iTR n _k R v = qqAlls (imp (conjunct 2 n 0 (iVE n v.[0]) ⋏ (conjunct 2 n 1 (iVE n v.[1]) ⋏ ⊤))
    (subst ?[#0,#1] (cRel R))) 2
```

**要证 `IsUFormula`**，需各构件的公式性。**先查哪些构件的引理已有。** -/

/-- **查实 3**：`cRel R` 是**关系符号的码**——`IsRel` 的见证。 -/
example (R : V) : Prop := (ℒₛₑₜ).IsRel 2 R

/-- **查实 4（要建的）**：`iTR n k R v` 是集合语言公式。

**注意 `IsUFormula` 是 `Fixpoint` 定义**（`Formula/Basic.lean:284`），
所以「是公式」的证明通常走 `IsUFormula.xxx.mpr` 构造器。

**本行只固定目标**——实际构造需要逐层拼 `qqAlls`/`imp`/`conjunct` 的公式性，
那是下一步的具体工作。 -/
example (n k R v : V) : Prop := Bootstrapping.IsUFormula ℒₛₑₜ (iTR n k R v)

end GodelQ.CG008RelCase
