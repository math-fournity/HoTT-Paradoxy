import GodelQ.ZFC.ShCraigElimBranches

/-!
# DEVELOPMENT_PROBE / NOT_A_RECEIPT / NOT_A_CLAIM

身份：开发探针。推进 `iVE` 与 `shift` 的相容律
`iVE n (termShift ℒₒᵣ t) = shift ℒₛₑₜ (iVE n t)`。

**语言**：`iVE` 把 `ℒₒᵣ` 项翻译成 `ℒₛₑₜ` 公式；`termShift` 在 `ℒₒᵣ` 侧
（`^#z ↦ ^#z`、`^&x ↦ ^&(x+1)`），`shift` 在 `ℒₛₑₜ` 侧。

两支的需求：
- bvar：`eqAtom ^#(z+1) = shift (eqAtom ^#(z+1))` —— 已证（`shift_eqAtom_bvar`）。
- fvar：`eqAtom ^&(x+1) = shift (eqAtom ^&x)` —— 待证。
**不是**收据源，**不是**数学主张。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.SeqTranslate

namespace GodelQ.ProbeITVE

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- 地基：`eqAtom ^#z` 是 `shift ℒₛₑₜ`-不变的。 -/
lemma shift_eqAtom_bvar (z : V) :
    shift ℒₛₑₜ (eqAtom (^#z : V)) = eqAtom (^#z : V) := by
  have h0 : IsUTerm ℒₛₑₜ (^#0 : V) := IsUTerm.bvar
  have hz : IsUTerm ℒₛₑₜ (^#z : V) := IsUTerm.bvar
  have hv : IsUTermVec ℒₛₑₜ 2 (?[^#0, ^#z] : V) := by
    rw [show (?[^#0, ^#z] : V) = (^#0 : V) ∷ (^#z ∷ 0) from rfl]
    exact IsUTermVec.adjoin (IsUTermVec.adjoin IsUTermVec.empty hz) h0
  rw [eqAtom, shift_rel (L := ℒₛₑₜ) (hR := by rw [cEqN]; exact codeIn_rel_quote _) (hv := hv)]
  congr 1
  rw [termShiftVec_cons₂ (L := ℒₛₑₜ) (ht₁ := h0) (ht₂ := hz)]
  simp [termShift_bvar]

/-- fvar 支：`shift ℒₛₑₜ (eqAtom ^&x) = eqAtom ^&(x+1)`。

`eqAtom ^&x = ^rel 2 cEqN ?[^#0, ^&x]`；`shift` 后向量逐元素 `termShift ℒₛₑₜ`，
`^#0` 不动、`^&x ↦ ^&(x+1)`，正是 `eqAtom ^&(x+1)` 的向量。 -/
lemma shift_eqAtom_fvar (x : V) :
    shift ℒₛₑₜ (eqAtom (^&x : V)) = eqAtom (^&(x + 1) : V) := by
  have h0 : IsUTerm ℒₛₑₜ (^#0 : V) := IsUTerm.bvar
  have hx : IsUTerm ℒₛₑₜ (^&x : V) := IsUTerm.fvar x
  have hx' : IsUTerm ℒₛₑₜ (^&(x + 1) : V) := IsUTerm.fvar (x + 1)
  have hv : IsUTermVec ℒₛₑₜ 2 (?[^#0, ^&x] : V) := by
    rw [show (?[^#0, ^&x] : V) = (^#0 : V) ∷ (^&x ∷ 0) from rfl]
    exact IsUTermVec.adjoin (IsUTermVec.adjoin IsUTermVec.empty hx) h0
  rw [eqAtom, shift_rel (L := ℒₛₑₜ) (hR := by rw [cEqN]; exact codeIn_rel_quote _) (hv := hv)]
  rw [eqAtom]
  congr 1
  rw [termShiftVec_cons₂ (L := ℒₛₑₜ) (ht₁ := h0) (ht₂ := hx)]
  simp [termShift_bvar, termShift_fvar]

end GodelQ.ProbeITVE
