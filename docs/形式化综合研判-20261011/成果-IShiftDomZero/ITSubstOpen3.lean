-- CG-009: (★★) —— 开口律的项层核心引理。
--
-- 设 `Vw`、`Ww` 是项向量，满足前缀相等 + 末项 `Ww.[m+1] = ^&0`。
-- 则对层 `m+1` 的项 `t`：`subst Vw (iVE m (termSubst (QvecVOr m) t)) = subst Ww (iVE (m+1) t)`。
--
-- 用途：`iT_subst_open` 的 rel 支（`conjunct 2 m j` 的向量是 `^#j ∷ shiftVec 2 m`
-- 与其 `++ [^&0]`）与 func 支（`ve2` 的向量）都归约到这一形状。
import GodelQ.ZFC.ITSubstOpen2

open FFL FFL.FirstOrder FFL FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate

namespace GodelQ.ITSubstOpen3
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
open GodelQ.QvecVDefs GodelQ.ITSubstOpen GodelQ.ITRSubstOpen GodelQ.IVESubstOpen
open GodelQ.IVESubstOpen2 GodelQ.IVESubstOpen3 GodelQ.TranslateShiftCompat
open GodelQ.IVEOpenFunc GodelQ.IVEOpenFunc8 GodelQ.IVEOpenFull GodelQ.LayerMono

/-! ## 零件：任意向量下的 `eqAtom` 代入 -/

/-- `subst v (eqAtom (^#z)) = ^rel 2 cEqN ?[v.[0], v.[z]]`。 -/
lemma subst_eqAtom_bvar (v : V) (z : V) :
    subst ℒₛₑₜ v (eqAtom (^#z : V)) = ^rel 2 (↑cEqN : V) ?[v.[0], v.[z]] := by
  show subst ℒₛₑₜ v (^rel 2 (↑cEqN : V) ((^#0 : V) ∷ (^#z : V) ∷ (0 : V)))
    = ^rel 2 (↑cEqN : V) ?[v.[0], v.[z]]
  rw [substs_rel (L := ℒₛₑₜ) (by rw [cEqN]; exact codeIn_rel_quote _)
    (isUTermVec_eqAtom_vec (^#z) (IsUTerm.bvar (z := z)))]
  congr 1
  rw [termSubstVec_cons₂ (IsUTerm.bvar (z := 0)) (IsUTerm.bvar (z := z))]
  congr 1
  · rw [termSubst_bvar]
  · rw [termSubst_bvar]

/-- `subst v (eqAtom (^&x)) = ^rel 2 cEqN ?[v.[0], ^&x]`（fvar 不动）。 -/
lemma subst_eqAtom_fvar (v : V) (x : V) :
    subst ℒₛₑₜ v (eqAtom (^&x : V)) = ^rel 2 (↑cEqN : V) ?[v.[0], ^&x] := by
  show subst ℒₛₑₜ v (^rel 2 (↑cEqN : V) ((^#0 : V) ∷ (^&x : V) ∷ (0 : V)))
    = ^rel 2 (↑cEqN : V) ?[v.[0], ^&x]
  rw [substs_rel (L := ℒₛₑₜ) (by rw [cEqN]; exact codeIn_rel_quote _)
    (isUTermVec_eqAtom_vec (^&x) (IsUTerm.fvar x))]
  congr 1
  rw [termSubstVec_cons₂ (IsUTerm.bvar (z := 0)) (IsUTerm.fvar x)]
  congr 1
  · rw [termSubst_bvar]
  · rw [termSubst_fvar]

/-- **bvar 支**：`z ≤ m`。
    `z < m`：两侧读 `Vw.[z+1] = Ww.[z+1]`；
    `z = m`：左侧是 fvar `^&0`，右侧读 `Ww.[m+1] = ^&0`。 -/
lemma subst_iVE_bvar_eq {m z Vw Ww : V} (hz : z < m + 1)
    (h0 : Vw.[0] = Ww.[0])
    (hz1 : z < m → Vw.[z + 1] = Ww.[z + 1])
    (hlast : Ww.[m + 1] = ^&0) :
    subst ℒₛₑₜ Vw (iVE m (termSubst ℒₒᵣ (QvecVOr (V := V) m) (^#z : V)))
      = subst ℒₛₑₜ Ww (iVE (m + 1) (^#z : V)) := by
  rcases lt_or_ge z m with hlt | hge
  · rw [termSubst_bvar, nth_QvecVOr_lt m z hlt, iVE_bvar, iVE_bvar]
    rw [subst_eqAtom_bvar, subst_eqAtom_bvar]
    exact congrArg₂ (fun a b => (^rel 2 (↑cEqN : V) ?[a, b] : V)) h0 (hz1 hlt)
  · have hzm : z = m := by
      have hzle : z ≤ m := lt_succ_iff_le.mp hz
      exact le_antisymm hzle hge
    rw [hzm, termSubst_bvar, nth_QvecVOr_last m, iVE_fvar, iVE_bvar]
    rw [subst_eqAtom_fvar, subst_eqAtom_bvar]
    exact congrArg₂ (fun a b => (^rel 2 (↑cEqN : V) ?[a, b] : V)) h0 hlast.symm

end GodelQ.ITSubstOpen3

#print axioms GodelQ.ITSubstOpen3.subst_eqAtom_bvar
#print axioms GodelQ.ITSubstOpen3.subst_eqAtom_fvar
#print axioms GodelQ.ITSubstOpen3.subst_iVE_bvar_eq

namespace GodelQ.ITSubstOpen3
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
open GodelQ.QvecVDefs GodelQ.ITSubstOpen GodelQ.ITRSubstOpen GodelQ.IVESubstOpen
open GodelQ.IVESubstOpen2 GodelQ.IVESubstOpen3 GodelQ.TranslateShiftCompat
open GodelQ.IVEOpenFunc GodelQ.IVEOpenFunc8 GodelQ.IVEOpenFull GodelQ.LayerMono

