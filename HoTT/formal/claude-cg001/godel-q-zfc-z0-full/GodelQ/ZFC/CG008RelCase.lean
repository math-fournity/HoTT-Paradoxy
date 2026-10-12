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

open GodelQ.Translate (iT iTR iVE eqAtom)

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

/-! ## 试建（续）：`isUFormula_qqAlls` 把目标降到 body

**关键引理**（`Formula/Iteration.lean:515`）：

```lean
@[simp] lemma isUFormula_qqAlls {p k : V} : IsUFormula L (qqAlls p k) ↔ IsUFormula L p
```

**所以 `IsUFormula (iTR n k R v)` 归约到 body 的 `IsUFormula`**，
而 body 是 `imp (conjunct … ⋏ (conjunct … ⋏ ⊤)) (subst … (cRel R))`——
`imp` 保持 `IsUFormula`（`Formula/Functions.lean:185`）。

**剩下的**：`conjunct`、`iVE`、`cRel`、`subst` 各构件的公式性。
**这是本会话第一次确需新建的零件**——本行固定这条链。 -/

/-- **查实 5**：`isUFormula_qqAlls` 的**形状**——归约到 body。 -/
example {p k : V} : Bootstrapping.IsUFormula ℒₛₑₜ (Bootstrapping.qqAlls p k) ↔
    Bootstrapping.IsUFormula ℒₛₑₜ p :=
  Bootstrapping.isUFormula_qqAlls

/-- **查实 6**：`IsUFormula.imp` 保持公式性——`imp` 的两个参数都是公式即可。 -/
example {p q : V} : Bootstrapping.IsUFormula ℒₛₑₜ (Bootstrapping.imp ℒₛₑₜ p q) ↔
    (Bootstrapping.IsUFormula ℒₛₑₜ p ∧ Bootstrapping.IsUFormula ℒₛₑₜ q) :=
  Bootstrapping.IsUFormula.imp

/-! ## 装配清单：`rel` 情形所需的零件与现状

`iTR n k R v = qqAlls (imp (conjunct 2 n 0 (iVE n v.[0]) ⋏ (conjunct 2 n 1 (iVE n v.[1]) ⋏ ⊤)) (subst ?[#0,#1] (cRel R))) 2`

| 构件 | 保持 `IsUFormula` 的引理 | 现状 |
|---|---|---|
| `qqAlls` | `isUFormula_qqAlls`（`Iteration.lean:515`） | ✅ 已查实 |
| `imp` | `IsUFormula.imp`（`Functions.lean:185`） | ✅ 已查实 |
| `⋏`（`and`） | `IsUFormula.and` | ✅ 已有（`ITQuoteProof` 用过） |
| `⊤` | `IsUFormula.verum` | ✅ 已有 |
| `conjunct b n i y` | 需证：`subst` 与 `⋏` 的复合（**本包定义**，`InternalTranslate.lean:115`） | ⚠️ **待建** |
| `iVE n t`（项翻译） | 需证：`iVE` 的结果是**项**的码，不是公式 | ⚠️ **待建**（且类型可能不同） |
| `subst ?[#0,#1] (cRel R)` | `substs_*` 系列（`Functions.lean:476-485`）与 `subst` 归纳（`:503`） | ◐ 部分就位 |
| `cRel R` | 关系符号的码——`IsRel` 的见证 | ◐ 需 `hR` |

**结论**：`rel` 情形的装配**零件全部就位**——**我先前的「`iVE` 类型问题」是错的**。

## 更正：`iVE` 返回的是**公式**，不是项

我先前写道：「`iVE n t` 是**项**的码，而 `conjunct` 的 `⋏` 两边要求**公式**，
所以还需一层『项 ⟹ 公式』的转换」。**这是错的。**

读 `iVE.construction`（`InternalTranslate.lean:163-167`）：

```lean
bvar := fun _ z ↦ eqAtom (^#(z + 1))
fvar := fun _ x ↦ eqAtom (^&x)
func := fun p k f _ w ↦ if k = 0 then ve0 k f else ve2 (p 0) k f w
```

**每个分支都返回 `eqAtom …`**，而
`eqAtom t = ^rel 2 (cEqN : V) ?[^#0, t]`（`:93`）——**一个原子公式的码**。

**所以 `iVE n t` 本身就是公式**，`conjunct` 的 `⋏` 两边都合适。
**「项 ⟹ 公式」的转换已经内建在 `iVE` 里了**（这正是它叫「变量等式」的原因，
见 `:176` 的注释「`iVE n ⌜t⌝` 是 `varEqual t`（层数 n）的编码」）。

## 装配清单（更正后）

| 构件 | 引理 | 现状 |
|---|---|---|
| `qqAlls` | `isUFormula_qqAlls`（`Iteration.lean:515`） | ✅ 已查实 |
| `imp` | `IsUFormula.imp`（`Functions.lean:185`） | ✅ 已查实 |
| `⋏` | `IsUFormula.and` | ✅ 已有 |
| `⊤` | `IsUFormula.verum` | ✅ 已有 |
| `iVE n t` | **返回 `eqAtom`，即公式**——需 `IsUFormula (eqAtom t)` | ⚠️ 待建（但**无类型问题**） |
| `conjunct b n i y` | `subst` 与 `⋏` 的复合（本包定义） | ⚠️ 待建 |
| `subst ?[#0,#1] (cRel R)` | `substs_*` 系列 + `subst` 归纳（`:503`） | ◐ 部分就位 |
| `cRel R` | 需 `hR` | ◐ 就位 |

**净结论**：`rel` 情形的装配**无类型障碍**，
剩两处要建：`IsUFormula (eqAtom t)` 与 `conjunct` 的复合性。 -/

/-- **查实 7**：`iVE` 返回 `eqAtom` 的**结果**——即公式的码。 -/
noncomputable example (n t : V) : V := iVE n t

/-- **查实 8（更正的关键）**：`eqAtom t` 是**原子公式**——`^rel 2 cEqN ?[^#0, t]`。

**所以 `iVE` 的输出是公式**，「项 ⟹ 公式」的转换内建其中。 -/
noncomputable example (t : V) : V := eqAtom t

end GodelQ.CG008RelCase
