import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimSetupQ GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 4000000
namespace GodelQ.ProbeFL
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **`iT_substs1` 的一般形状（层数 = 向量长度）**：

```
iT (n-1) (subst w p) = subst w (iT n p)      （p 层 n、w 长 n 层 n）
```

`iT_substs1` 是 `n = 1`、`w = ?[^&0]` 的特例。

**`all` 支的关键**：`p = ^∀ X`（层 `n`）⟹ `X` 层 `n+1`；
归纳假设在 `X` 上以 `qVec w`（长 `n+1`、层 `n+1`）实例化，
而 `qVec w` 恰好是 `subst` 推过 `∀` 时用的向量——**同步**。 -/
theorem iT_substs1_gen : ∀ {n p : V}, IsSemiformula ℒₒᵣ n p →
    ∀ w, IsSemitermVec ℒₒᵣ n n w →
    iT (n - 1) (subst ℒₒᵣ w p) = subst ℒₛₑₜ w (iT n p) := by
  intro n p hp
  apply IsSemiformula.pi1_structural_induction (L := ℒₒᵣ) ?_ ?_ ?_ ?_ ?_ ?_ ?_ ?_ ?_ hp
  · definability
  · intro n k R v hR hv w hw; sorry
  · intro n k R v hR hv w hw; sorry
  · intro n w hw
    rw [Bootstrapping.substs_verum (L := ℒₒᵣ), iT_verum (n := n - 1),
      iT_verum (n := n), Bootstrapping.substs_verum (L := ℒₛₑₜ)]
  · intro n w hw
    rw [Bootstrapping.substs_falsum (L := ℒₒᵣ), iT_falsum (n := n - 1),
      iT_falsum (n := n), Bootstrapping.substs_falsum (L := ℒₛₑₜ)]
  · intro n p q hp hq ihp ihq w hw
    rw [Bootstrapping.substs_and (L := ℒₒᵣ) hp.isUFormula hq.isUFormula]
    rw [iT_and (V := V) (n := n - 1)
        (IsSemiformula.subst (L := ℒₒᵣ) (n := n) (m := n) hp hw).isUFormula
        (IsSemiformula.subst (L := ℒₒᵣ) (n := n) (m := n) hq hw).isUFormula]
    rw [iT_and (V := V) (n := n) hp.isUFormula hq.isUFormula]
    rw [Bootstrapping.substs_and (L := ℒₛₑₜ)
        (isSemiformula_iT (n := n) p hp).isUFormula
        (isSemiformula_iT (n := n) q hq).isUFormula]
    rw [ihp w hw, ihq w hw]
  · intro n p q hp hq ihp ihq w hw
    rw [Bootstrapping.substs_or (L := ℒₒᵣ) hp.isUFormula hq.isUFormula]
    rw [iT_or (V := V) (n := n - 1)
        (IsSemiformula.subst (L := ℒₒᵣ) (n := n) (m := n) hp hw).isUFormula
        (IsSemiformula.subst (L := ℒₒᵣ) (n := n) (m := n) hq hw).isUFormula]
    rw [iT_or (V := V) (n := n) hp.isUFormula hq.isUFormula]
    rw [Bootstrapping.substs_or (L := ℒₛₑₜ)
        (isSemiformula_iT (n := n) p hp).isUFormula
        (isSemiformula_iT (n := n) q hq).isUFormula]
    rw [ihp w hw, ihq w hw]
  · intro n p hp ih w hw
    -- `^∀ p`（层 n）⟹ `p` 层 n+1
    rw [Bootstrapping.substs_all (L := ℒₒᵣ) hp.isUFormula]
    rw [show iT (n - 1) (^∀ (subst ℒₒᵣ (qVec ℒₒᵣ w) p))
          = (^∀ (imp ℒₛₑₜ domZero (iT ((n - 1) + 1) (subst ℒₒᵣ (qVec ℒₒᵣ w) p))) : V)
        from iT_all (n := n - 1)
          (IsSemiformula.subst (L := ℒₒᵣ) (n := n + 1) (m := n + 1) hp hw.qVec).isUFormula]
    rw [iT_all (n := n) hp.isUFormula]
    rw [Bootstrapping.substs_all (L := ℒₛₑₜ)
        (IsUFormula.imp.mpr ⟨isUFormula_domZero2,
          (isSemiformula_iT (n := n + 1) p hp).isUFormula⟩)]
    -- 两侧都是 `^∀ (subst (qVec w) (imp domZero …))`
    congr 1
    rw [show (imp ℒₛₑₜ (domZero (V := V)) (iT (n + 1) p) : V)
          = (neg ℒₛₑₜ (domZero (V := V)) ^⋎ iT (n + 1) p : V) from rfl]
    rw [show (imp ℒₛₑₜ (domZero (V := V))
            (iT (n - 1 + 1) (subst ℒₒᵣ (qVec ℒₒᵣ w) p)) : V)
          = (neg ℒₛₑₜ (domZero (V := V))
              ^⋎ iT (n - 1 + 1) (subst ℒₒᵣ (qVec ℒₒᵣ w) p) : V) from rfl]
    rw [Bootstrapping.substs_or (L := ℒₛₑₜ)
        (IsUFormula.neg isUFormula_domZero2)
        ((isSemiformula_iT (n := n + 1) p hp).isUFormula)]
    congr 1
    · -- 第一分量：`neg domZero` vs `subst (qVec w) (neg domZero)`
      congr 1
      -- `subst_qVec_domZero'` 要 `IsSemitermVec ℒₛₑₜ (len w') 1 w'`；
      -- 这里 `w' = qVec ℒₒᵣ w`（层 n+1 的项向量），需其层 1 版
      exact (subst_qVec_domZero' (V := V) (w := qVec ℒₒᵣ w) ?_).symm
    · -- 第二分量：归纳假设在 `p`（层 n+1）与 `qVec w`（长 n+1）上
      sorry
  · intro n p hp ih w hw; sorry

end GodelQ.ProbeFL
