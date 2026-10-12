import GodelQ.ZFC.CG008RelCase

/-!
# CG-008 · 建 `IsUFormula (eqAtom t)`——`rel` 情形的第一块

## 目标

```lean
IsUFormula ℒₛₑₜ (eqAtom t)
```

其中 `eqAtom t = ^rel 2 (cEqN : V) ?[^#0, t]`（`InternalTranslate.lean:93`）。

## 由 Foundation 的判定（`Formula/Basic.lean:322`）

```lean
@[simp] lemma rel : IsUFormula L (^rel k r v) ↔ L.IsRel k r ∧ IsUTermVec L k v
```

**所以要证两件事**：
1. `(ℒₛₑₜ).IsRel 2 (cEqN : V)`——等号是元数 2 的关系；
2. `IsUTermVec ℒₛₑₜ 2 ?[^#0, t]`——那两个参数是项向量。

## 治理

- Foundation 只读；本文件纯下游。
- 若成功则无未证标记、可进收据。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic Bootstrapping
open FFL.Entailment
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008EqAtom

open GodelQ.Translate (iT iTR iVE eqAtom cEqN)

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **查实 1**：`cEqN` 是等号在 `ℒₛₑₜ` 下的**编码**——`Encodable.encode Eq.eq`（`:83`）。 -/
noncomputable example : ℕ := cEqN

/-- **查实 2（要证的第一件）**：`(ℒₛₑₜ).IsRel 2 (cEqN : V)`。

**待查**：`IsRel` 说的是「`k` 与 `R` 使得 `R` 是元数 `k` 的关系符号的码」。
`cEqN` 是 `Eq.eq` 的编码，所以应当成立——
**需 `Language.IsRel` 的相应引理**（`SetLanguage.lean` 或 Foundation）。 -/
example : Prop := (ℒₛₑₜ).IsRel 2 (cEqN : V)

/-! ## 试证：`IsUFormula (eqAtom t)`

**先看 `iT_quote` 的 `rel` 情形怎么拿到 `IsUFormula`**——
它用的是 `Sentence.quote_isUFormula`（对**元层**句子的报价），
所以那条路对**内部码**不适用。

**本行直接由 `eqAtom` 的定义与 `IsUFormula.rel` 试。** -/

/-- **试证**：`eqAtom t` 是公式。

**注意**：`?[^#0, t]` 是 `SemitermVec`（两个项），
所以第二件要证 `IsUTermVec ℒₛₑₜ 2 ?[^#0, t]`。
**而 `t` 是 V 内任意的数**——它未必是项的码！

**这就是新障碍**：`eqAtom t` 对**任意** `t : V` 未必是公式；
只有当 `t` 是项的码时才成立。
**所以 `IsUFormula (eqAtom t)` 不是无条件定理**，
需要 `IsUTerm ℒₛₑₜ n t` 之类的前提。

**这与 `iVE` 的情形吻合**：`iVE n t` 的输入 `t` 是**算术项的码**，
其 `IsUTerm` 性由归纳假设（`TermRec` 的归纳）保证。 -/
example (t : V) : Prop := Bootstrapping.IsUTerm ℒₛₑₜ t → Bootstrapping.IsUFormula ℒₛₑₜ (eqAtom t)

end GodelQ.CG008EqAtom
