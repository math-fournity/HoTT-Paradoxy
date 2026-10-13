import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimSetupQ GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 4000000
namespace GodelQ.ProbeFL
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **`hExs` 的关键判定**：`iT 0 (subst ?[t] p)` **依赖 `t`**。

取 `p = ^rel 2 cEqN ?[^#0,^#0]`（层 1），两个不同的项：

* `t = ^&0`：`subst ?[^&0] p` = `^rel 2 cEqN ?[^&0,^&0]`
  ⟹ `iT 0 (…) = iTR 0 2 cEqN ?[^&0,^&0]`（向量 `?[^&0,^&0]`）；
* `t = ^#1`：`subst ?[^#1] p` = `^rel 2 cEqN ?[^#1,^#0]`
  ⟹ `iT 0 (…) = iTR 0 2 cEqN ?[^#1,^#0]`（向量 `?[^#1,^#0]`）。

**两者的向量不同**（`?[^&0,^&0]` vs `?[^#1,^#0]`），故 `iT 0 (subst ?[t] p)` **依赖 `t`**。

**推论**：`hExs` 的 `Derivable.exs` 里我们能自由选 `t'`，
但 `ih` 给的 `iT 0 (substs1 ℒₒᵣ t p)` **依赖推导里那个具体的 `t`**——
故 `t'` 必须依赖 `t`，**需要一个项层的翻译 `iTe`（`ℒₒᵣ` 项码 → `ℒₛₑₜ` 项码）**。

**而 `iT` 没有项层**：它的 `exs` 支给 `domZero ^⋏ iT (n+1) p`，
**没有项的位置**（`∃x∈ω` 被编码成「`domZero` 且 `p`」，存在量化被消掉了）。

**本探针把「依赖 `t`」这一条机器确认**（两个不同的向量）。 -/
example :
    subst ℒₒᵣ (?[^&0] : V) (^rel 2 (↑cEqN) (?[^#0, ^#0] : V))
      = (^rel 2 (↑cEqN) (?[^&0, ^&0] : V) : V) := by
  have hR : (ℒₒᵣ).IsRel (2:V) (↑cEqN : V) := by rw [cEqN]; exact codeIn_rel_quote _
  have hv : IsUTermVec ℒₒᵣ (2:V) (?[^#0, ^#0] : V) := by
    simpa using isUTermVec_two_bvars (V := V) (L := ℒₒᵣ)
  rw [Bootstrapping.substs_rel (L := ℒₒᵣ) hR hv]
  congr 1
  rw [show (?[^#0, ^#0] : V) = (^#0 : V) ∷ ((^#0 : V) ∷ (0:V)) from rfl]
  rw [termSubstVec_cons₂ (IsUTerm.bvar (z := (0:V))) (IsUTerm.bvar (z := (0:V)))]
  rw [termSubst_bvar, termSubst_bvar]
  rw [show (?[^&0] : V).[0] = (^&0 : V) from by
    rw [show (?[^&0] : V) = ((^&0 : V) ∷ (0:V)) from rfl]
    rw [nth_adjoin_zero]]
  rw [show (?[^&0, ^&0] : V) = (^&0 : V) ∷ ((^&0 : V) ∷ (0:V)) from rfl]

end GodelQ.ProbeFL
