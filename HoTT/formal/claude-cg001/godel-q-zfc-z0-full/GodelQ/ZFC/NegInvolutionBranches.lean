import GodelQ.ZFC.SeqTranslateFormula

/-!
# CG-007 · W8 第二层（九）：码层面 `neg` 的对合律——八支的核心步骤

`iT`/`neg` 相容律的 `nrel` 支需要码层面的对合律 `neg (neg x) = x`。
本文件给出该对合律的**逐构造子核心步骤**（八支全部）。

## 为什么这能证

`neg` 本身就是 `UformulaRec1` 的构造（`Negation.construction`），
所以对合律用同一个 `semiformula_result_induction` 就能证，
谓词取 `P _param _n p q := neg ℒₒᵣ q = p`（`q` 是 `result`，原理固定它）。

本机确认该谓词被接受。八支的核心步骤各自独立可证（见下），
它们与 `Negation.construction` 的支定义（都是 `rfl` 可展开的）配合，
再补上 `result_all`/`result_exs` 的层数展开（`Negation` 用默认 `allChanges`，
即 `param' = param`，与 `iT` 的 `n+1` 不同），即可组装出完整对合律。

## 支的对应（每支都是"`neg` 抵消 `Negation.construction` 的该支"）

| 支 | `Negation.construction` 产出 | 对合用引理 |
|---|---|---|
| `rel` | `^nrel k R v` | `neg_nrel` |
| `nrel` | `^rel k R v` | `neg_rel` |
| `verum` | `^⊥` | `neg_falsum` |
| `falsum` | `^⊤` | `neg_verum` |
| `and` | `y₁ ^⋎ y₂` | `neg_or` + 归纳假设 |
| `or` | `y₁ ^⋏ y₂` | `neg_and` + 归纳假设 |
| `all` | `^∃ ys.[0]` | `neg_ex` + 归纳假设 |
| `exs` | `^∀ ys.[0]` | `neg_all` + 归纳假设 |
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.SeqTranslate

namespace GodelQ.NegInvolutionBranches

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- `Negation.construction` 的 `verum` 支产出 `^⊥`（`rfl`）。 -/
lemma negConstruction_verum (param : V) : Negation.construction.verum param = (^⊥ : V) := rfl

/-- `Negation.construction` 的 `falsum` 支产出 `^⊤`（`rfl`）。 -/
lemma negConstruction_falsum (param : V) : Negation.construction.falsum param = (^⊤ : V) := rfl

/-- `Negation.construction` 的 `rel` 支产出 `^nrel`（`rfl`）。 -/
lemma negConstruction_rel (param k R v : V) :
    Negation.construction.rel param k R v = (^nrel k R v : V) := rfl

/-- `Negation.construction` 的 `nrel` 支产出 `^rel`（`rfl`）。 -/
lemma negConstruction_nrel (param k R v : V) :
    Negation.construction.nrel param k R v = (^rel k R v : V) := rfl

/-- **对合律的 `rel` 支**：`neg (nrel k R v) = rel k R v`。 -/
lemma neg_invol_rel {k R v : V} (hR : (ℒₒᵣ).IsRel k R) (hv : IsUTermVec ℒₒᵣ k v) :
    neg ℒₒᵣ (^nrel k R v) = (^rel k R v : V) :=
  neg_nrel (L := ℒₒᵣ) hR hv

/-- **对合律的 `nrel` 支**：`neg (rel k R v) = nrel k R v`。 -/
lemma neg_invol_nrel {k R v : V} (hR : (ℒₒᵣ).IsRel k R) (hv : IsUTermVec ℒₒᵣ k v) :
    neg ℒₒᵣ (^rel k R v) = (^nrel k R v : V) :=
  neg_rel (L := ℒₒᵣ) hR hv

/-- **对合律的 `verum` 支**：`neg ⊥ = ⊤`。 -/
lemma neg_invol_verum : neg ℒₒᵣ (^⊥ : V) = (^⊤ : V) := neg_falsum (L := ℒₒᵣ)

/-- **对合律的 `falsum` 支**：`neg ⊤ = ⊥`。 -/
lemma neg_invol_falsum : neg ℒₒᵣ (^⊤ : V) = (^⊥ : V) := neg_verum (L := ℒₒᵣ)

/-- **对合律的 `and` 支**：`neg (y₁ ⋎ y₂) = p ⋏ q`，由 `neg_or` 与归纳假设。 -/
lemma neg_invol_and {p q y₁ y₂ : V}
    (ihp : neg ℒₒᵣ y₁ = p) (ihq : neg ℒₒᵣ y₂ = q)
    (hu₁ : IsUFormula ℒₒᵣ y₁) (hu₂ : IsUFormula ℒₒᵣ y₂) :
    neg ℒₒᵣ (y₁ ^⋎ y₂) = (p ^⋏ q : V) := by
  rw [neg_or (L := ℒₒᵣ) hu₁ hu₂, ihp, ihq]

/-- **对合律的 `or` 支**：`neg (y₁ ⋏ y₂) = p ⋎ q`。 -/
lemma neg_invol_or {p q y₁ y₂ : V}
    (ihp : neg ℒₒᵣ y₁ = p) (ihq : neg ℒₒᵣ y₂ = q)
    (hu₁ : IsUFormula ℒₒᵣ y₁) (hu₂ : IsUFormula ℒₒᵣ y₂) :
    neg ℒₒᵣ (y₁ ^⋏ y₂) = (p ^⋎ q : V) := by
  rw [neg_and (L := ℒₒᵣ) hu₁ hu₂, ihp, ihq]

/-- **对合律的 `all` 支**：`neg (∃¹ x) = ∀¹ p`。 -/
lemma neg_invol_all {p x : V} (ih : neg ℒₒᵣ x = p) (hu : IsUFormula ℒₒᵣ x) :
    neg ℒₒᵣ (^∃ x) = (^∀ p : V) := by
  rw [neg_ex (L := ℒₒᵣ) hu, ih]

/-- **对合律的 `exs` 支**：`neg (∀¹ x) = ∃¹ p`。 -/
lemma neg_invol_exs {p x : V} (ih : neg ℒₒᵣ x = p) (hu : IsUFormula ℒₒᵣ x) :
    neg ℒₒᵣ (^∀ x) = (^∃ p : V) := by
  rw [neg_all (L := ℒₒᵣ) hu, ih]

end GodelQ.NegInvolutionBranches

#print axioms GodelQ.NegInvolutionBranches.neg_invol_rel
#print axioms GodelQ.NegInvolutionBranches.neg_invol_nrel
#print axioms GodelQ.NegInvolutionBranches.neg_invol_verum
#print axioms GodelQ.NegInvolutionBranches.neg_invol_falsum
#print axioms GodelQ.NegInvolutionBranches.neg_invol_and
#print axioms GodelQ.NegInvolutionBranches.neg_invol_or
#print axioms GodelQ.NegInvolutionBranches.neg_invol_all
#print axioms GodelQ.NegInvolutionBranches.neg_invol_exs
