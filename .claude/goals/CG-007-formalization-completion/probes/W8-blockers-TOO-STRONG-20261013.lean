import GodelQ.ZFC.ShCraigElimSetupQ
/-! ## ⚠ `ExsBlockerQ` 与 `AllBlockerQ` **都过强**（机器证明，2026-10-13）

**共同缺陷**：两个 blocker 的假设里只有 `Q dd`，**丢掉了 `Derivation Sh.craig dd`**。
而 `induction1` 的对应支手里是 `hd : DerivationOf Sh.craig dd (...)`，
`hd.2 : Derivation Sh.craig dd` 会强制 `dd` 有真实结构。

**后果**：取 `p = ⊤`。则 `substs1 t ⊤ = ⊤`、`free ⊤ = ⊤`，
`Q dd` 退化成「sequent 里有 `⊤`」，对**任意** `s` 无条件成立——
不再携带关于 `s` 的信息。于是两个 blocker 各自蕴含：

```
ExsBlockerQ → ∀ s, IsFormulaSet s → ^∃ ⊤ ∈ s → Derivable (translateSeq s)
AllBlockerQ → ∀ s, IsFormulaSet s → ^∀ ⊤ ∈ s → Derivable (translateSeq s)
```

**这是 blocker 的表述缺陷，不是数学难点**。
修法：假设里保留 `hd.2`，即写成 `Derivation Sh.craig dd ∧ Q dd`；
或直接在 `induction1` 支内联，不经过 `def`。 -/
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000

namespace GodelQ.ProbeExsB
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

namespace ProbeBlockersTooStrong

lemma substs1_top (t : V) : substs1 ℒₒᵣ t (^⊤ : V) = ^⊤ := by
  simp [substs1, Bootstrapping.substs_verum]

lemma free_top : free ℒₒᵣ (^⊤ : V) = ^⊤ := by
  simp [free, substs1, Bootstrapping.shift_verum, Bootstrapping.substs_verum]

/-- `Q` 在 `fstIdx dd = insert ⊤ S` 时无条件成立。 -/
lemma Q_of_fstIdx_eq_insert_top {dd S : V}
    (hS : IsFormulaSet (L := ℒₒᵣ) S) (h : fstIdx dd = insert (^⊤ : V) S) :
    ShCraigElimSetup.Q (V := V) dd := by
  unfold ShCraigElimSetup.Q
  rw [h, translateSeq_insert, iT_verum]
  exact Derivable.verum (s := insert (^⊤ : V) (translateSeq S))
    (fun q hq => by
      rcases mem_bitInsert_iff.mp hq with rfl | hq
      · exact IsSemiformula.verum (L := ℒₛₑₜ) (n := (0:V))
      · exact ShCraigElimBranches.isFormulaSet_translateSeq hS q hq)
    (by simp)

/-- **`ExsBlockerQ` 过强**。 -/
theorem exsBlockerQ_too_strong (hB : ShCraigElimSetupQ.ExsBlockerQ (V := V))
    (s : V) (hs : IsFormulaSet (L := ℒₒᵣ) s) (hps : (^∃ (^⊤ : V) : V) ∈ s) :
    Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖 (translateSeq (V := V) s) := by
  have h := hB (s := s) (p := (^⊤ : V)) (t := (^&0 : V))
    (dd := axm (insert (^⊤ : V) s) (^⊤ : V)) hs hps
    (IsSemiterm.fvar (L := ℒₒᵣ) (V := V) (n := (0:V)) 0)
    (by rw [fstIdx_axm, substs1_top])
    (Q_of_fstIdx_eq_insert_top hs (by rw [fstIdx_axm]))
  unfold ShCraigElimSetup.Q at h
  rw [fstIdx_exsIntro] at h
  exact h

/-- **`AllBlockerQ` 过强**（同一论证，用 `free ⊤ = ⊤`）。 -/
theorem allBlockerQ_too_strong (hB : ShCraigElimSetupQ.AllBlockerQ (V := V))
    (s : V) (hs : IsFormulaSet (L := ℒₒᵣ) s) (hps : (^∀ (^⊤ : V) : V) ∈ s) :
    Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖 (translateSeq (V := V) s) := by
  have h := hB (s := s) (p := (^⊤ : V))
    (dd := axm (insert (^⊤ : V) (setShift (L := ℒₒᵣ) s)) (^⊤ : V)) hs hps
    (by rw [fstIdx_axm, free_top])
    (Q_of_fstIdx_eq_insert_top hs.setShift (by rw [fstIdx_axm]))
  unfold ShCraigElimSetup.Q at h
  rw [fstIdx_allIntro] at h
  exact h

end ProbeBlockersTooStrong

#print axioms ProbeBlockersTooStrong.exsBlockerQ_too_strong
#print axioms ProbeBlockersTooStrong.allBlockerQ_too_strong