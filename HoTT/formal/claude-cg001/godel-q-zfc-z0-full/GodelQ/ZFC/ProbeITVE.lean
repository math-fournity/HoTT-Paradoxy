import GodelQ.ZFC.ShCraigElimBranches

/-!
# DEVELOPMENT_PROBE / NOT_A_RECEIPT / NOT_A_CLAIM

身份：开发探针。判定项层相容律 `iVE n (termShift ℒₒᵣ t) = shift ℒₛₑₜ (iVE n t)`。

**注意语言**：`t` 是 `ℒₒᵣ` 的项码，但 `eqAtom` 产生的是 `ℒₛₑₜ` 的公式码——
`iVE` 的作用是把 `ℒₒᵣ` 项**翻译**成 `ℒₛₑₜ` 公式（`^#z ↦ (#0 = #(z+1))`）。
所以 `shift ℒₛₑₜ` 作用在 `ℒₛₑₜ` 公式上，其 bvar 语义与 `ℒₒᵣ` 侧的 `termShift` 不同。

本轮先判定的地基：`shift ℒₛₑₜ (eqAtom t) = eqAtom t`（`eqAtom` 只含 bvar，
而 `termShift` 不动 bvar，故 `eqAtom` 是 `shift`-不变的）。
**不是**收据源，**不是**数学主张。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate
open GodelQ.SeqTranslate

namespace GodelQ.ProbeITVE

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **地基**：`eqAtom t` 是 `shift ℒₛₑₜ`-不变的。

`eqAtom t = ^rel 2 cEqN ?[^#0, t]`；`shift` 对 rel 支作用 `termShiftVec`，
把向量逐元素 `termShift ℒₛₑₜ`。若 `t` 本身是 bvar 或已含 `ℒₛₑₜ` 侧的自由变量，
需分情况。这里先判定**最简情形**：`t` 是 bvar。 -/
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

end GodelQ.ProbeITVE
