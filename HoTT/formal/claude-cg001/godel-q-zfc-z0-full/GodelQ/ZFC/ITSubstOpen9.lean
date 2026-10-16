-- CG-009: `iT_subst_open` —— 公式层的完整开口律（∀m，含 0）。
--
--     iT m (subst ℒₒᵣ (QvecVOr m) q) = subst ℒₛₑₜ (QvecV m) (iT (m+1) q)     (q : 层 m+1)
--
-- ## 归纳谓词（关键设计）
--
--     P param n p r := n = param + 1 →
--         subst (QvecV param) r = iT param (subst (QvecVOr param) p)
--
-- * `param` 就是 `iT` 的层参数，**无减法**（Σ1 形 + 无 `tsub` 摩擦）；
-- * 守卫 `n = param + 1` 是 `subst` 的类型要求（公式层 = 向量长度 + 1 的源层）；
-- * 结论取 `param = m`、`n = m+1`，得定理的**反向**，`.symm` 收尾。
--
-- ## 递归支的守卫
--
-- `semiformula_result_induction` 的 hall 支给 IH 在 `(allChanges param i) = param + 1`
-- 处，层 `n + 1` —— 守卫 `n + 1 = (param + 1) + 1` 由 `hn : n = param + 1` 立得。
import GodelQ.ZFC.ITSubstOpen8
import GodelQ.ZFC.SubstDomZero

open FFL FFL.FirstOrder FFL FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.SeqTranslate

namespace GodelQ.ITSubstOpen9
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
open GodelQ.QvecVDefs GodelQ.ITSubstOpen GodelQ.ITRSubstOpen GodelQ.IVESubstOpen
open GodelQ.IVESubstOpen2 GodelQ.IVESubstOpen3 GodelQ.TranslateShiftCompat
open GodelQ.IVEOpenFunc GodelQ.IVEOpenFunc8 GodelQ.IVEOpenFull GodelQ.LayerMono
open GodelQ.ITSubstOpen2 GodelQ.ITSubstOpen3 GodelQ.ITSubstOpen4
open GodelQ.ITSubstOpen5 GodelQ.ITSubstOpen6 GodelQ.ITSubstOpen7 GodelQ.ITSubstOpen8

/-- `subst (QvecV (m+1)) domZero = domZero`（**宇宙多态**本地版；
    `SubstDomZero` 的那条固定在 `Type`，本文件在 `Type*`）。 -/
lemma subst_QvecV_domZero' (m : V) :
    subst ℒₛₑₜ (QvecV (V := V) (m + 1)) (domZero (V := V)) = domZero (V := V) := by
  rw [domZero]
  have hQ : IsSemitermVec ℒₛₑₜ (m + 1 + 1) (m + 1 + 1) (QvecV (V := V) (m + 1)) :=
    isSemitermVec_QvecV (m + 1)
  have hw : IsSemitermVec ℒₛₑₜ 1 (m + 1 + 1) (?[^#0] : V) :=
    isSemitermVec_single_bvar (n := m + 1 + 1) (by simp)
  rw [Bootstrapping.substs_substs (L := ℒₛₑₜ) (l := 1) isSemiformula_cDomN hQ hw]
  rw [show (?[^#0] : V) = (^#0 : V) ∷ (0 : V) from rfl,
    termSubstVec_cons₁ (IsUTerm.bvar (z := 0)), termSubst_bvar]
  rw [show ((QvecV (V := V) (m + 1)).[0]) = ^#0 from
    GodelQ.ITRSubstOpen.nth_QvecV_lt (m + 1) 0 (by simp)]

/-- 归纳谓词（**Π1 形**：`∀ m'` 守卫式）。
    取 `n = m'+1` 即定理（`m'` 是 iT 的层参数）。 -/
def QPred (n p : V) : Prop :=
  ∀ m', m' + 1 = n →
    iT m' (subst ℒₒᵣ (QvecVOr (V := V) m') p) = subst ℒₛₑₜ (QvecV (V := V) m') (iT (m' + 1) p)

/-- **开口律（公式层，∀m）**。 -/
theorem iT_subst_open : ∀ (m : V) (q : V), IsSemiformula ℒₒᵣ (m + 1) q →
    iT m (subst ℒₒᵣ (QvecVOr (V := V) m) q) = subst ℒₛₑₜ (QvecV (V := V) m) (iT (m + 1) q) := by
  have key : ∀ {n p : V}, IsSemiformula ℒₒᵣ n p → QPred (V := V) n p := by
    intro n p hp
    apply IsSemiformula.pi1_structural_induction (L := ℒₒᵣ) (P := QPred (V := V))
      ?_ ?_ ?_ ?_ ?_ ?_ ?_ ?_ ?_ hp
    · -- definability
      unfold QPred
      definability
    · -- rel
      intro n k R v hR hv
      unfold QPred
      intro m' hm'
      have hk2 : k = 2 := by
        rcases Arithmetic.isRel_iff_LOR.mp hR with h' | h' <;> exact h'.1
      subst hk2
      have hv' : IsSemitermVec ℒₒᵣ 2 (m' + 1) v := by rw [hm']; exact hv
      show iT m' (subst ℒₒᵣ (QvecVOr (V := V) m') (^rel 2 R v))
        = subst ℒₛₑₜ (QvecV (V := V) m') (iT (m' + 1) (^rel 2 R v))
      rw [substs_rel (L := ℒₒᵣ) hR hv.isUTermVec]
      rw [iT_rel hR (IsSemitermVec.termSubstVec (L := ℒₒᵣ) (k := 2)
        (isSemitermVec_QvecVOr_low (m := m')) hv').isUTerm]
      conv_rhs => rw [iT_rel hR hv.isUTermVec]
      exact iTR_subst_open (m := m') hR hv'
    · -- nrel
      intro n k R v hR hv
      unfold QPred
      intro m' hm'
      have hk2 : k = 2 := by
        rcases Arithmetic.isRel_iff_LOR.mp hR with h' | h' <;> exact h'.1
      subst hk2
      have hv' : IsSemitermVec ℒₒᵣ 2 (m' + 1) v := by rw [hm']; exact hv
      show iT m' (subst ℒₒᵣ (QvecVOr (V := V) m') (^nrel 2 R v))
        = subst ℒₛₑₜ (QvecV (V := V) m') (iT (m' + 1) (^nrel 2 R v))
      rw [substs_nrel (L := ℒₒᵣ) hR hv.isUTermVec]
      rw [iT_nrel hR ((IsSemitermVec.termSubstVec (L := ℒₒᵣ) (k := 2) (isSemitermVec_QvecVOr_low (m := m')) hv')).isUTerm]
      rw [iT_nrel hR hv.isUTermVec]
      rw [Bootstrapping.substs_neg (L := ℒₛₑₜ) (n := m' + 1)
        (isSemiformula_iTR (n := m' + 1) hR hv') (isSemitermVec_QvecV (V := V) m')]
      exact congrArg (neg ℒₛₑₜ) (iTR_subst_open hR hv')
    · -- verum
      intro n
      unfold QPred
      intro m' hm'
      show iT m' (subst ℒₒᵣ (QvecVOr (V := V) m') (^⊤ : V))
        = subst ℒₛₑₜ (QvecV (V := V) m') (iT (m' + 1) (^⊤ : V))
      rw [Bootstrapping.substs_verum (L := ℒₒᵣ), iT_verum, iT_verum,
        Bootstrapping.substs_verum (L := ℒₛₑₜ)]
    · -- falsum
      intro n
      unfold QPred
      intro m' hm'
      show iT m' (subst ℒₒᵣ (QvecVOr (V := V) m') (^⊥ : V))
        = subst ℒₛₑₜ (QvecV (V := V) m') (iT (m' + 1) (^⊥ : V))
      rw [Bootstrapping.substs_falsum (L := ℒₒᵣ), iT_falsum, iT_falsum,
        Bootstrapping.substs_falsum (L := ℒₛₑₜ)]
    · -- and
      intro n p q hp hq ihp ihq
      unfold QPred at ihp ihq ⊢
      intro m' hm'
      have hp' : IsSemiformula ℒₒᵣ (m' + 1) p := by rw [hm']; exact hp
      have hq' : IsSemiformula ℒₒᵣ (m' + 1) q := by rw [hm']; exact hq
      show iT m' (subst ℒₒᵣ (QvecVOr (V := V) m') (p ^⋏ q))
        = subst ℒₛₑₜ (QvecV (V := V) m') (iT (m' + 1) (p ^⋏ q))
      rw [Bootstrapping.substs_and (L := ℒₒᵣ) hp'.isUFormula hq'.isUFormula]
      conv_rhs => rw [iT_and hp'.isUFormula hq'.isUFormula]
      rw [iT_and (IsSemiformula.subst (L := ℒₒᵣ) hp' (isSemitermVec_QvecVOr_low (m := m'))).isUFormula
        (IsSemiformula.subst (L := ℒₒᵣ) hq' (isSemitermVec_QvecVOr_low (m := m'))).isUFormula]
      rw [Bootstrapping.substs_and (L := ℒₛₑₜ)
        (isSemiformula_iT p hp').isUFormula (isSemiformula_iT q hq').isUFormula]
      exact congrArg₂ (· ^⋏ ·) (ihp m' hm') (ihq m' hm')
    · -- or
      intro n p q hp hq ihp ihq
      unfold QPred at ihp ihq ⊢
      intro m' hm'
      have hp' : IsSemiformula ℒₒᵣ (m' + 1) p := by rw [hm']; exact hp
      have hq' : IsSemiformula ℒₒᵣ (m' + 1) q := by rw [hm']; exact hq
      show iT m' (subst ℒₒᵣ (QvecVOr (V := V) m') (p ^⋎ q))
        = subst ℒₛₑₜ (QvecV (V := V) m') (iT (m' + 1) (p ^⋎ q))
      rw [Bootstrapping.substs_or (L := ℒₒᵣ) hp'.isUFormula hq'.isUFormula]
      conv_rhs => rw [iT_or hp'.isUFormula hq'.isUFormula]
      rw [iT_or (IsSemiformula.subst (L := ℒₒᵣ) hp' (isSemitermVec_QvecVOr_low (m := m'))).isUFormula
        (IsSemiformula.subst (L := ℒₒᵣ) hq' (isSemitermVec_QvecVOr_low (m := m'))).isUFormula]
      rw [Bootstrapping.substs_or (L := ℒₛₑₜ)
        (isSemiformula_iT p hp').isUFormula (isSemiformula_iT q hq').isUFormula]
      exact congrArg₂ (· ^⋎ ·) (ihp m' hm') (ihq m' hm')
    · -- all
      intro n p hp ih
      unfold QPred at ih ⊢
      intro m' hm'
      have hp' : IsSemiformula ℒₒᵣ ((m' + 1) + 1) p := by rw [hm']; exact hp
      show iT m' (subst ℒₒᵣ (QvecVOr (V := V) m') (^∀ p))
        = subst ℒₛₑₜ (QvecV (V := V) m') (iT (m' + 1) (^∀ p))
      conv_rhs => rw [iT_all hp'.isUFormula]
      rw [Bootstrapping.substs_all (L := ℒₒᵣ) hp'.isUFormula]
      rw [show qVec ℒₒᵣ (QvecVOr (V := V) m') = QvecVOr (V := V) (m' + 1) from
        (QvecVOr_succ m').symm]
      rw [iT_all (IsSemiformula.subst (L := ℒₒᵣ) hp'
        (isSemitermVec_QvecVOr_low (m := m' + 1))).isUFormula]
      conv_rhs => rw [imp]
      rw [Bootstrapping.substs_all (L := ℒₛₑₜ)
        (IsUFormula.or.mpr ⟨(isSemiformula_domZero (n := m' + 1)).isUFormula.neg,
          (isSemiformula_iT p hp').isUFormula⟩)]
      rw [show qVec ℒₛₑₜ (QvecV (V := V) m') = QvecV (V := V) (m' + 1) from
        (QvecV_succ m').symm]
      rw [Bootstrapping.substs_or (L := ℒₛₑₜ)
          (isSemiformula_domZero (n := m' + 1)).isUFormula.neg
          (isSemiformula_iT p hp').isUFormula,
        Bootstrapping.substs_neg (L := ℒₛₑₜ) (n := (m' + 1) + 1)
          (isSemiformula_domZero (n := m' + 1))
          (isSemitermVec_QvecV (V := V) (m' + 1))]
      rw [subst_QvecV_domZero' (V := V) m']
      exact congrArg (fun x => ^∀ (neg ℒₛₑₜ (domZero (V := V)) ^⋎ x))
        (ih (m' + 1) (by rw [hm']))
    · -- exs
      intro n p hp ih
      unfold QPred at ih ⊢
      intro m' hm'
      have hp' : IsSemiformula ℒₒᵣ ((m' + 1) + 1) p := by rw [hm']; exact hp
      show iT m' (subst ℒₒᵣ (QvecVOr (V := V) m') (^∃ p))
        = subst ℒₛₑₜ (QvecV (V := V) m') (iT (m' + 1) (^∃ p))
      conv_rhs => rw [iT_exs hp'.isUFormula]
      rw [Bootstrapping.substs_ex (L := ℒₒᵣ) hp'.isUFormula]
      rw [show qVec ℒₒᵣ (QvecVOr (V := V) m') = QvecVOr (V := V) (m' + 1) from
        (QvecVOr_succ m').symm]
      rw [iT_exs (IsSemiformula.subst (L := ℒₒᵣ) hp'
        (isSemitermVec_QvecVOr_low (m := m' + 1))).isUFormula]
      rw [Bootstrapping.substs_ex (L := ℒₛₑₜ)
        (IsUFormula.and.mpr ⟨(isSemiformula_domZero (n := m' + 1)).isUFormula,
          (isSemiformula_iT p hp').isUFormula⟩)]
      rw [show qVec ℒₛₑₜ (QvecV (V := V) m') = QvecV (V := V) (m' + 1) from
        (QvecV_succ m').symm]
      rw [Bootstrapping.substs_and (L := ℒₛₑₜ)
        (isSemiformula_domZero (n := m')).isUFormula
        (isSemiformula_iT p hp').isUFormula]
      rw [subst_QvecV_domZero' (V := V) m']
      exact congrArg (fun x => ^∃ (domZero (V := V) ^⋏ x))
        (ih (m' + 1) (by rw [hm']))
  -- 主结论
  intro m q hq
  have h := key hq
  unfold QPred at h
  exact h m rfl

end GodelQ.ITSubstOpen9

#print axioms GodelQ.ITSubstOpen9.iT_subst_open
