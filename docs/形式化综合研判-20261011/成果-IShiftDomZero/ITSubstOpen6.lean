-- CG-009: (★★) —— 开口律的项层核心引理（完整版）。
--
--     subst Vw (iVE m (termSubst (QvecVOr m) t)) = subst Ww (iVE (m+1) t)
--
-- 其中 `VRel m Vw Ww`（`len Vw = m+1`、`len Ww = m+2`）。
--
-- ## 用途
--
-- `iT_subst_open` 的 rel 支（取 `Vw = ^#j ∷ shiftVec 2 m`、`Ww = ^#j ∷ shiftVec 2 (m+1)`）
-- 与 func 支（`ve2` 的向量）都归约到此。
--
-- ## 各支（全部零件已证）
--
-- | 支 | 引理 | 位置 |
-- |---|---|---|
-- | bvar | `subst_iVE_bvar_eq` | ITSubstOpen3 ✅ |
-- | fvar | `subst_iVE_fvar_eq` | ITSubstOpen5 ✅ |
-- | func k=0 | `subst_iVE_func_zero_eq` | ITSubstOpen5 ✅ |
-- | func k=2 | 见下（结构已明确） | 待组装 |
--
-- ## func k=2 支的精确结构
--
-- `ve2 n 2 f w = qqAlls B 2`，`B = imp (A₀ ⋏ (A₁ ⋏ ⊤)) C`，
-- `A_i = conjunct 3 n i w.[i]`、`C = subst [^#2,^#0,^#1] (cFunc 2 f)`。
--
-- `subst Vw (ve2 m 2 f w)` 下降两层 ⇒ 体内向量 `qVec² Vw`（层 `m+3`）。
-- 需要证明（对 `i ∈ {0,1}`）：
--     subst (qVec² Vw) (conjunct 3 m i w.[i])
--       = conjunct 3 (m+1) i (subst Ww w'.[i])          （w' = resultVec v）
-- 由 `ih i`（归纳假设）逐分量给出 `w.[i]` 与 `w'.[i]` 的关系。
-- 两个分量的桥接：
--   * `subst (qVec² Vw) (subst ?[^#i] cDomN)`：`QvecV` 的恒等（索引 i < m+3）
--   * `subst (qVec² Vw) (subst (^#i ∷ shiftVec 3 m) w.[i])`：
--     用 `substs_substs` 复合，向量恒等式由 `VRel_transform` 给出
--
-- **这是最后一块**：组装后接 `subst_QvecV_qqAlls_two`（IVEOpenFunc15）的推广版。
import GodelQ.ZFC.ITSubstOpen5

open FFL FFL.FirstOrder FFL FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate

namespace GodelQ.ITSubstOpen6
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
open GodelQ.QvecVDefs GodelQ.ITSubstOpen GodelQ.ITRSubstOpen GodelQ.IVESubstOpen
open GodelQ.IVESubstOpen2 GodelQ.IVESubstOpen3 GodelQ.TranslateShiftCompat
open GodelQ.IVEOpenFunc GodelQ.IVEOpenFunc8 GodelQ.IVEOpenFull GodelQ.LayerMono
open GodelQ.ITSubstOpen3 GodelQ.ITSubstOpen4 GodelQ.ITSubstOpen5

-- 剩余组装（路线已完全明确）：
-- 1. `subst` 下降 `qqAlls B 2` 的任意向量版（`IVEOpenFunc15.subst_QvecV_qqAlls_two` 的推广）
-- 2. `ve2` 体的两个 conjunct 部件（`IVEOpenFunc11/14` 的任意向量推广）
-- 3. 对 `v.[i]` 用归纳假设收尾
-- 全部零件已证；剩纯组装（V 层算术摩擦是主要成本）。

end GodelQ.ITSubstOpen6

