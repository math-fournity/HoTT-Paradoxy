import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimSetupQ GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 4000000
namespace GodelQ.ProbeFL
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **判定 `hExs` 的边界：`iT 0 (subst ?[t] p)` 的顶层形状。**

取 `p = ^rel 2 cEqN ?[^#0,^#0]`（层 1）、`t = ^#0`：

`subst ?[^#0] p = ^rel 2 cEqN ?[^#0,^#0]`（`#0 ↦ ^#0` 是恒等）

`iT 0 (^rel 2 cEqN ?[^#0,^#0]) = iTR 0 2 cEqN ?[^#0,^#0]`
= `qqAlls (imp (conjunct 2 0 0 (iVE 0 ^#0) ⋏ …) (subst ?[^#0,^#1] (cRel cEqN))) 2`

**注意 `t` 在结果里完全消失了**——`subst ?[^#0]` 把 `#0` 换成 `^#0`，
而 `iT` 只看到结果 `^rel 2 cEqN ?[^#0,^#0]`。

**关键**：`substs1 ℒₒᵣ t p` 的 `t` 被**代入掉了**，
所以 `iT 0 (substs1 ℒₒᵣ t p)` **不含 `t` 的独立信息**——
它只含 `t` 被代入后的结果。

**这对 `hExs` 是好消息**：`Derivable.exs` 里我们能自由选 `t'`，
只要能让 `substs1 ℒₛₑₜ t' (iT 1 p)` 与 `iT 0 (substs1 ℒₒᵣ t p)` 对上即可。
**不一定需要项层翻译 `iTe`**——§12.24 的判断过强。

本探针把「`t` 被代入掉」这一条机器确认（`subst ?[^#0] p = p` 于这个 `p`）。 -/
lemma subst_bvar0_self :
    subst ℒₒᵣ (?[^#0] : V) (^rel 2 (↑cEqN) (?[^#0, ^#0] : V))
      = (^rel 2 (↑cEqN) (?[^#0, ^#0] : V) : V) := by
  have hR : (ℒₒᵣ).IsRel (2:V) (↑cEqN : V) := by rw [cEqN]; exact codeIn_rel_quote _
  have hv : IsUTermVec ℒₒᵣ (2:V) (?[^#0, ^#0] : V) := by
    simpa using isUTermVec_two_bvars (V := V) (L := ℒₒᵣ)
  rw [Bootstrapping.substs_rel (L := ℒₒᵣ) hR hv]
  congr 1
  rw [show (?[^#0, ^#0] : V) = (^#0 : V) ∷ ((^#0 : V) ∷ (0:V)) from rfl]
  rw [termSubstVec_cons₂ (IsUTerm.bvar (z := (0:V))) (IsUTerm.bvar (z := (0:V)))]
  rw [termSubst_bvar]
  simp only [nth_adjoin_zero]

end GodelQ.ProbeFL
