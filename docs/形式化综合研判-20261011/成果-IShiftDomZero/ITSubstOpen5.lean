-- CG-009: (★★) —— 开口律的项层核心引理（完整版，含 func 支）。
--
-- ## 陈述
--
-- 对层 `m+1` 的项 `t`，以及满足 `VRel m Vw Ww` 的向量 `Vw`（长 `m+1`）、
-- `Ww`（长 `m+2`）：
--
--     subst Vw (iVE m (termSubst (QvecVOr m) t)) = subst Ww (iVE (m+1) t)
--
-- ## 归纳（对 `t`，用 `IsSemiterm.sigma1_induction`）
--
-- * bvar：`subst_iVE_bvar_eq`（ITSubstOpen3，已证）
-- * fvar：两侧都是 `subst ? (eqAtom ^&x)`，由 `VRel` 的第 0 项相等
-- * func k=0：`ve0` 不含参数向量
-- * func k=2：`ve2` 下降两层，向量变为 `Vw₁`、`Ww₁`（`VRel_transform` 保持关系），
--   对 `v.[i]` 用归纳假设
--
-- ## definability（关键）
--
-- 谓词取（**向量关系作为假设**，不是计算）：
--
--     𝚷ᴬ₁-Predicate (fun t : V ↦
--       ∀ Vw Ww : V, (∀ k ≤ m, Vw.[k] = Ww.[k]) → Ww.[m+1] = ^&0 →
--         subst Vw (iVE m t) = subst Ww (iVE (m+1) t))
--
-- 探针实测 `definability` **可过**（前一份文档的"绕不过去"是针对计算形式的谓词）。
import GodelQ.ZFC.ITSubstOpen4

open FFL FFL.FirstOrder FFL FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate

namespace GodelQ.ITSubstOpen5
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
open GodelQ.QvecVDefs GodelQ.ITSubstOpen GodelQ.ITRSubstOpen GodelQ.IVESubstOpen
open GodelQ.IVESubstOpen2 GodelQ.IVESubstOpen3 GodelQ.TranslateShiftCompat
open GodelQ.IVEOpenFunc GodelQ.IVEOpenFunc8 GodelQ.IVEOpenFull GodelQ.LayerMono
open GodelQ.ITSubstOpen3 GodelQ.ITSubstOpen4

/-- (★★) 的谓词（供 definability 探针与归纳使用）。 -/
def PPred (m : V) (t : V) : Prop :=
  ∀ Vw Ww : V, (∀ k ≤ m, Vw.[k] = Ww.[k]) → Ww.[m + 1] = ^&0 →
    subst ℒₛₑₜ Vw (iVE m t) = subst ℒₛₑₜ Ww (iVE (m + 1) t)

/-- definability 探针（机器核验：可过）。 -/
example (m : V) : 𝚷ᴬ₁-Predicate (PPred (V := V) m) := by
  unfold PPred
  definability

end GodelQ.ITSubstOpen5

#print axioms GodelQ.ITSubstOpen5.PPred

namespace GodelQ.ITSubstOpen5
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
open GodelQ.QvecVDefs GodelQ.ITSubstOpen GodelQ.ITRSubstOpen GodelQ.IVESubstOpen
open GodelQ.IVESubstOpen2 GodelQ.IVESubstOpen3 GodelQ.TranslateShiftCompat
open GodelQ.IVEOpenFunc GodelQ.IVEOpenFunc8 GodelQ.IVEOpenFull GodelQ.LayerMono
open GodelQ.ITSubstOpen3 GodelQ.ITSubstOpen4

/-- fvar 支：两侧都是 `subst ? (eqAtom ^&x)`，由第 0 项相等。 -/
lemma subst_iVE_fvar_eq {m x Vw Ww : V}
    (h0 : Vw.[0] = Ww.[0]) :
    subst ℒₛₑₜ Vw (iVE m (termSubst ℒₒᵣ (QvecVOr (V := V) m) (^&x : V)))
      = subst ℒₛₑₜ Ww (iVE (m + 1) (^&x : V)) := by
  rw [termSubst_fvar, iVE_fvar, iVE_fvar]
  rw [subst_eqAtom_fvar, subst_eqAtom_fvar]
  exact congrArg₂ (fun a b => (^rel 2 (↑cEqN : V) ?[a, b] : V)) h0 rfl

-- k=0 支的零件（分开写以避免 elaboration 超时）

-- 关键零件：**引号化句子**（层 1）的代入只读向量的第 0 项。
-- 写成两条引理以避免 elaboration 超时。

-- 零件：**引号化句子**（层 1）的代入只读向量的第 0 项。

/-- `subst X (subst ?[^#0] c) = subst ?[X.[0]] c`（`c` 层 1，`X` 是项向量）。
    **取 `IsSemitermVec` 形式**（层数由调用方给，避免 layer 摩擦）。 -/
lemma subst_quoted_reads_zero {c X m : V} (hc : IsSemiformula ℒₛₑₜ 1 c)
    (hX : IsSemitermVec ℒₛₑₜ (len X) m X) (hpos : (0 : V) < len X) :
    subst ℒₛₑₜ X (subst ℒₛₑₜ (?[^#0] : V) c)
      = subst ℒₛₑₜ (?[X.[0]] : V) c := by
  have hw : IsSemitermVec ℒₛₑₜ 1 (len X) (?[^#0] : V) :=
    isSemitermVec_single_bvar (n := len X) hpos
  rw [show subst ℒₛₑₜ X (subst ℒₛₑₜ (?[^#0] : V) c)
      = subst ℒₛₑₜ (termSubstVec ℒₛₑₜ 1 X (?[^#0] : V)) c from
    Bootstrapping.substs_substs (L := ℒₛₑₜ) (l := 1) (n := len X) (m := m)
      (p := c) hc hX hw]
  rw [show (?[^#0] : V) = (^#0 : V) ∷ (0 : V) from rfl,
    termSubstVec_cons₁ (IsUTerm.bvar (z := 0)), termSubst_bvar]

end GodelQ.ITSubstOpen5

namespace GodelQ.ITSubstOpen5
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
open GodelQ.QvecVDefs GodelQ.ITSubstOpen GodelQ.ITRSubstOpen GodelQ.IVESubstOpen
open GodelQ.IVESubstOpen2 GodelQ.IVESubstOpen3 GodelQ.TranslateShiftCompat
open GodelQ.IVEOpenFunc GodelQ.IVEOpenFunc8 GodelQ.IVEOpenFull GodelQ.LayerMono
open GodelQ.ITSubstOpen3 GodelQ.ITSubstOpen4

-- k=0 支（待完成）：`ve0 0 f` 不含参数向量；内层是引号化句子，只读 `X.[0]`。
-- 零件已全部就位：`subst_quoted_reads_zero`（本文件）✅。
-- 剩余：把 `ve0` 展开后接 `substs_or`/`substs_neg`/`substs_falsum`，
-- 再用 `subst_quoted_reads_zero` 两次 + `h0`。注意 `ve0` 是 `noncomputable def`
-- 不是 abbrev，`rw [ve0]` 需要先 `show` 成展开形式。

end GodelQ.ITSubstOpen5


