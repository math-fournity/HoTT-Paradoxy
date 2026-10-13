import GodelQ.ZFC.ShCraigElimSetupQ
/-! ## 更正：`ExsBridge` 是**假的**；正确的桥是「p[t] → ∃x∈ω p(x)」（2026-10-13）

上一轮我报「`ExsBlockerQ` 归约到唯一一条 `ExsBridge`」，那条归约**形式上正确**，
但 `ExsBridge` 本身**语义为假**：

它 `∀ T'` 量化。取 `T' = ^&0`，结论需要
`Provable 𝗭𝗙𝗖 (^&0 ∈ ω ∧ …)`（因为 `substs1 T' domZero` 就是「T' ∈ ω」）。
而 `Provable φ`（φ 带自由变量）在 LK 里等价于 `⊢ ∀x φ`，
故需要 `⊢ ∀x (x ∈ ω)`——**假**。取 `p = #0 = #0`、`t = ^&0` 即得具体反例。
**故那条归约是空洞的（前提不可满足），不是有效进展。**

**正确的桥**：不要求单个见证项，而要求

```
Provable 𝗭𝗙𝗖 (iT 0 (substs1 ℒᵣ t p) → ^∃ (domZero ⋏ iT 1 p))
```

即「p[t] → ∃x(x ∈ ω ∧ p(x))」——**语义为真**（t 的值就是那个 x）。
它与 sequent 里的 ∃ 公式**同一形状**，故不需任何见证项。

**归约**（本文件机器核验）：
1. `ih` 给 `Derivable (insert A (translateSeq s))`，`A := iT 0 (substs1 t p)`；
2. 桥给 `¬A ⋎ ∃` 可证，`split_or` 拆成 `{¬A, ∃}`，`wk` 得 `Derivable (insert (¬A) S)`
   （`∃ ∈ S` 是关键）；
3. `cut A` 收尾。 -/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000

namespace GodelQ.ProbeExsB
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
namespace ProbeExsBridge2
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **正确的桥**：`p[t] → ∃x (x ∈ ω ∧ p(x))`。 -/
def ExsBridge2 : Prop :=
  ∀ {p t : V}, IsUFormula ℒₒᵣ p → IsTerm ℒₒᵣ t →
    Provable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖
      (imp ℒₛₑₜ (iT (0:V) (substs1 ℒₒᵣ t p))
        ((^∃ (domZero (V := V)) ^⋏ iT (0+1:V) p) : V))

/-- **`ExsBlockerQ` 由正确的桥推出**（证明完整）。 -/
theorem exsBlockerQ_of_bridge2 (hBr : ExsBridge2 (V := V)) :
    ShCraigElimSetupQ.ExsBlockerQ (V := V) := by
  intro s p t dd hs hps ht hfd hder ih
  unfold ShCraigElimSetup.Q at ih ⊢
  rw [fstIdx_exsIntro]
  rw [hfd, translateSeq_insert] at ih
  have hpex : IsSemiformula ℒₒᵣ (1:V) p := by
    have h0 : IsFormula ℒₒᵣ (^∃ p) := hs (^∃ p) hps
    simpa using (IsSemiformula.exs (L := ℒₒᵣ) (n := (0:V)) (p := p)).mp h0
  have hp : IsUFormula ℒₒᵣ p := hpex.isUFormula
  have hS : IsFormulaSet (L := ℒₛₑₜ) (translateSeq s) :=
    GodelQ.ShCraigElimBranches.isFormulaSet_translateSeq hs
  have hmem : ((^∃ (domZero (V := V)) ^⋏ iT (0+1:V) p) : V) ∈ translateSeq s :=
    mem_translateSeq_iff.mpr ⟨(^∃ p : V), hps, (iT_exs (V := V) (n := (0:V)) hp).symm⟩
  have hA : IsFormula ℒₛₑₜ (iT (0:V) (substs1 ℒₒᵣ t p)) :=
    isSemiformula_iT (n := (0:V)) (substs1 ℒₒᵣ t p)
      (IsSemiformula.substs1 (L := ℒₒᵣ) (n := (0:V)) ht hpex)
  have hE : IsFormula ℒₛₑₜ ((^∃ (domZero (V := V)) ^⋏ iT (0+1:V) p) : V) :=
    (IsSemiformula.exs (L := ℒₛₑₜ) (n := (0:V))
      (p := ((domZero (V := V)) ^⋏ iT (0+1:V) p))).mpr
      (IsSemiformula.and.mpr
        ⟨isSemiformula_domZero (V := V) (n := (0:V)),
         isSemiformula_iT (n := (0+1:V)) p (by simpa using hpex)⟩)
  have hW : Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖
      (insert (imp ℒₛₑₜ (iT (0:V) (substs1 ℒₒᵣ t p))
        ((^∃ (domZero (V := V)) ^⋏ iT (0+1:V) p) : V)) ∅) :=
    internal_provable_iff_internal_derivable.mp (hBr hp ht)
  have hsplit : Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖
      (insert (neg ℒₛₑₜ (iT (0:V) (substs1 ℒₒᵣ t p)))
        (insert ((^∃ (domZero (V := V)) ^⋏ iT (0+1:V) p) : V) ∅)) :=
    ShCraigElimSetupQ.split_or hA.neg hE hW
  have hnegA : Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖
      (insert (neg ℒₛₑₜ (iT (0:V) (substs1 ℒₒᵣ t p))) (translateSeq s)) := by
    refine Derivable.wk
      (s := insert (neg ℒₛₑₜ (iT (0:V) (substs1 ℒₒᵣ t p))) (translateSeq s))
      (s' := insert (neg ℒₛₑₜ (iT (0:V) (substs1 ℒₒᵣ t p)))
        (insert ((^∃ (domZero (V := V)) ^⋏ iT (0+1:V) p) : V) ∅)) ?_ ?_ hsplit
    · intro y hy
      rcases mem_bitInsert_iff.mp hy with rfl | hy
      · exact hA.neg
      · exact hS y hy
    · intro y hy
      rcases mem_bitInsert_iff.mp hy with rfl | hy
      · exact mem_bitInsert_iff.mpr (Or.inl rfl)
      · rcases mem_bitInsert_iff.mp hy with rfl | hy
        · exact mem_bitInsert_iff.mpr (Or.inr hmem)
        · exact absurd hy (Arithmetic.not_mem_empty y)
  exact Derivable.cut (iT (0:V) (substs1 ℒₒᵣ t p)) ih hnegA

end ProbeExsBridge2

#print axioms ProbeExsBridge2.exsBlockerQ_of_bridge2
