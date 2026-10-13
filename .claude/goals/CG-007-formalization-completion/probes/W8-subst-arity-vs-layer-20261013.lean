import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimSetupQ GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 4000000
namespace GodelQ.ProbeFL
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **正确形式的反驳（bvar 型）**：`v = ?[^#1, ^#0]`。

`subst ?[^&0]` 只有 1 格，`^rel` 元数 2 ⟹ `termSubstVec 2 ?[^&0] ?[^#1,^#0]`：
* 第 0 格 `^#1`：`1 ≥ len ?[^&0] = 1` ⟹ **越界补零** `0`；
* 第 1 格 `^#0`：`(qVec ?[^&0]).[0] = ^&0`。

故 = `?[0, ^&0]`。

**⚠ 但等一下**：`subst ?[^&0]` 只作用于**前 `n = 2` 格**吗？
`subst` 的向量长度是 1，而公式层数是 **1**（`v` 层 1）——所以 `subst`
只看**前 1 格**！`^rel 2 cEqN ?[^#1,^#0]` 的 `IsSemiformula` 层数是 1
（`v` 层 1），故 `subst ?[^&0]` 只用第 0 格。

**这才是关键**：`subst` 的向量长度由**公式层数**决定，不是由 `^rel` 的元数。
`^rel 2 R v` 的层数是 `v` 的层数（1），故 `subst ?[^&0]` 只看第 0 格——
**但 `termSubstVec` 却按元数 `k = 2` 作用在 `v` 上**（`substs_rel` 的定义）。

本引理把这个**作用范围的不一致**机器确认下来。 -/
lemma subst_arity_vs_layer :
    subst ℒₒᵣ (?[^&0] : V) (^rel 2 (↑cEqN) (?[^#1, ^#0] : V))
      = (^rel 2 (↑cEqN) (?[0, ^&0] : V) : V) := by
  have hR : (ℒₒᵣ).IsRel (2:V) (↑cEqN : V) := by rw [cEqN]; exact codeIn_rel_quote _
  have h1 : IsUTermVec ℒₒᵣ (1:V) ((^#0 : V) ∷ (0:V)) :=
    IsUTermVec.adjoin IsUTermVec.empty (IsUTerm.bvar (z := (0:V)))
  have hv : IsUTermVec ℒₒᵣ (2:V) (?[^#1, ^#0] : V) := by
    rw [show (?[^#1, ^#0] : V) = (^#1 : V) ∷ ((^#0 : V) ∷ (0:V)) from rfl]
    exact IsUTermVec.adjoin h1 (IsUTerm.bvar (z := (1:V)))
  rw [Bootstrapping.substs_rel (L := ℒₒᵣ) hR hv]
  congr 1
  rw [show (?[^#1, ^#0] : V) = (^#1 : V) ∷ ((^#0 : V) ∷ (0:V)) from rfl,
    show (?[0, ^&0] : V) = (0:V) ∷ ((^&0 : V) ∷ (0:V)) from rfl]
  rw [termSubstVec_cons₂ (IsUTerm.bvar (z := (1:V))) (IsUTerm.bvar (z := (0:V)))]
  rw [termSubst_bvar, termSubst_bvar]
  rw [show ((^&0 : V) ∷ (0:V)).[1] = (0:V) from by
    rw [show ((^&0 : V) ∷ (0:V)) = (^&0 : V) ∷ (0:V) from rfl]
    rw [nth_adjoin_one]
    rfl]
  rw [show ((^&0 : V) ∷ (0:V)).[0] = (^&0 : V) from nth_adjoin_zero _ _]

end GodelQ.ProbeFL
