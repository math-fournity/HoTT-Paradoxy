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

/-! ## 装配：`IsUFormula (eqAtom t)` 的两块

**第一块**：`(ℒₛₑₜ).IsRel 2 (cEqN : V)`。
**第二块**：`IsUTermVec ℒₛₑₜ 2 ?[^#0, t]`——
由 `IsUTermVec` 的判定（`Term/Basic.lean:222`）：

```lean
IsUTermVec L 2 (?[t₁, t₂] : V) ↔ IsUTerm L t₁ ∧ IsUTerm L t₂
```

**所以第二块归约到 `IsUTerm ℒₛₑₜ ^#0 ∧ IsUTerm ℒₛₑₜ t`**——
前半是**有界变量**（`^#0` 总是项），后半是**前提**。 -/

-- **查实 3**：`IsUTermVec` 对二元向量的判定（`Term/Basic.lean:222`）：
--
--   `IsUTermVec L 2 (?[t₁, t₂] : V) ↔ IsUTerm L t₁ ∧ IsUTerm L t₂`
--
-- **归约到两个分量的 `IsUTerm`**。（`?[…]` 是 `SemitermVec` 的记号，
-- 需 `open scoped` 相应记号；本行以注释记录其类型。）

/-- **查实 4（要证的目标形状）**：`eqAtom t` 是公式，**前提是 `t` 是项**。

**两块**：`IsRel 2 cEqN`（`cEqN` 是 `Eq.eq` 的编码，应当可由 `Language.IsRel` 的
引理给出）与 `IsUTermVec 2 ?[^#0, t]`（由查实 3 与 `^#0` 的项性给出）。 -/
example (t : V) : Prop := Bootstrapping.IsUTerm ℒₛₑₜ t →
    Bootstrapping.IsUFormula ℒₛₑₜ (eqAtom t)

/-! ## 两块都到位：`codeIn_rel_quote` 是 `@[simp]`

`Language.lean:109`：

```lean
@[simp] lemma codeIn_rel_quote {k : ℕ} (r : L.Rel k) : L.IsRel (V := V) k ⌜r⌝
```

**`cEqN = Encodable.encode (Eq.eq : (ℒₛₑₜ).Rel 2)`**（`InternalTranslate.lean:83`），
即 `cEqN = ⌜Eq.eq⌝`——**所以 `IsRel 2 cEqN` 由 `codeIn_rel_quote` 直接给出**。

**这就是第一块。** 加上第二块（`IsUTermVec` 归约到 `IsUTerm ^#0 ∧ IsUTerm t`），
`eqAtom` 的公式性**两块都就位**。 -/

/-- **查实 5（第一块）**：`cEqN` 是 `Eq.eq` 的**编码**。 -/
example : cEqN = Encodable.encode (Language.Eq.eq : (ℒₛₑₜ).Rel 2) := rfl

/-- **查实 6（第一块）**：`(ℒₛₑₜ).IsRel 2 (cEqN : V)`。

由 `isRel_quote_quote`（`Language.lean:100`）：
`L.IsRel k x ↔ ∃ R : L.Rel k, Encodable.encode R = x`——
取 `R := Eq.eq`、`x := cEqN` 即得。 -/
example : (ℒₛₑₜ).IsRel 2 (cEqN : V) :=
  (Bootstrapping.isRel_quote_quote (V := V) (L := ℒₛₑₜ) (k := 2) (x := cEqN)).mpr
    ⟨Language.Eq.eq, rfl⟩

/-! ## 装配：`IsUFormula (eqAtom t)` -/

set_option maxHeartbeats 400000 in
/-- **主结果**：`eqAtom t` 是公式，**前提是 `t` 是项**。

由 `IsUFormula.rel`（`Formula/Basic.lean:322`）：
`IsUFormula L (^rel k r v) ↔ L.IsRel k r ∧ IsUTermVec L k v`。

- `L.IsRel 2 cEqN` ✅（`isRel_quote_quote`，上文已证）；
- `IsUTermVec ℒₛₑₜ 2 ?[^#0, t]`——由 `IsUTermVec.mkSeq₂_iff` 归约到
  `IsUTerm ℒₛₑₜ ^#0 ∧ IsUTerm ℒₛₑₜ t`，前半是**有界变量**（总是项），
  后半是**前提**。 -/
theorem eqAtom_isUFormula (t : V) (ht : Bootstrapping.IsUTerm ℒₛₑₜ t) :
    Bootstrapping.IsUFormula ℒₛₑₜ (eqAtom t) := by
  rw [eqAtom]
  rw [Bootstrapping.IsUFormula.rel]
  refine ⟨?_, ?_⟩
  · exact (Bootstrapping.isRel_quote_quote (V := V) (L := ℒₛₑₜ) (k := 2) (x := cEqN)).mpr
      ⟨Language.Eq.eq, rfl⟩
  · -- `?[^#0, t]` 的两个分量：有界变量与前提
    exact Bootstrapping.IsUTermVec.mkSeq₂_iff.mpr
      ⟨Bootstrapping.IsUTerm.bvar (L := ℒₛₑₜ) (z := 0), ht⟩

-- 公理洁净检查
#print axioms GodelQ.CG008EqAtom.eqAtom_isUFormula

end GodelQ.CG008EqAtom
