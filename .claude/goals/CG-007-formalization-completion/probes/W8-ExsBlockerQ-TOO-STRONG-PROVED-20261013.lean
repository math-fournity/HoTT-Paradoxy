import GodelQ.ZFC.ShCraigElimSetupQ
/-! ## ⚠ `ExsBlockerQ` **过强**（机器证明，2026-10-13）

**结论**：`ExsBlockerQ` 蕴含一条它不该蕴含的命题——

```
ExsBlockerQ → ∀ s, IsFormulaSet ℒₒᵣ s → ^∃ ⊤ ∈ s → Derivable 𝗭𝗙𝗖 (translateSeq s)
```

**为什么**：`ExsBlockerQ` 只保留 `Q dd`（= `Derivable (translateSeq (fstIdx dd))`），
**丢掉了 `Derivation Sh.craig dd`**。在 `p = ⊤` 的实例里
`substs1 t ⊤ = ⊤`，于是 `Q dd` 退化成「sequent 里有 `⊤`」，
对**任意** `s` 都无条件成立——`Q dd` 不再携带关于 `s` 的信息。

而 `induction1` 的 `hExs` 支**手里有** `hd : DerivationOf Sh.craig dd (...)`,
`hd.2 : Derivation Sh.craig dd` 会强制 `dd` 有真实结构。
**blocker 把这条信息丢了**，所以它比 `hExs` 支真正的义务更强。

**这是 blocker 的表述缺陷，不是数学难点**——修法：把 `Q dd` 换成
`Derivation Sh.craig dd ∧ Q dd`（即保留 `hd.2`），或直接在
`induction1` 支内联，不经过这个 `def`。 -/
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000

namespace GodelQ.ProbeExsB
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

namespace ProbeTooStrong

lemma substs1_top (t : V) : substs1 ℒₒᵣ t (^⊤ : V) = ^⊤ := by
  simp [substs1, Bootstrapping.substs_verum]

/-- **主定理**：`ExsBlockerQ` 过强。 -/
theorem exsBlockerQ_too_strong (hB : ShCraigElimSetupQ.ExsBlockerQ (V := V))
    (s : V) (hs : IsFormulaSet (L := ℒₒᵣ) s) (hps : (^∃ (^⊤ : V) : V) ∈ s) :
    Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖 (translateSeq (V := V) s) := by
  -- 用 `p = ⊤`、`t = ^&0`、`dd = axm (insert ⊤ s) ⊤` 实例化 blocker
  have h := hB (s := s) (p := (^⊤ : V)) (t := (^&0 : V))
    (dd := axm (insert (^⊤ : V) s) (^⊤ : V)) hs hps
    (IsSemiterm.fvar (L := ℒₒᵣ) (V := V) (n := (0:V)) 0)
    (by rw [fstIdx_axm, substs1_top])
    (by
      unfold ShCraigElimSetup.Q
      rw [fstIdx_axm, translateSeq_insert, iT_verum]
      exact Derivable.verum (s := insert (^⊤ : V) (translateSeq s))
        (fun q hq => by
          rcases mem_bitInsert_iff.mp hq with rfl | hq
          · exact IsSemiformula.verum (L := ℒₛₑₜ) (n := (0:V))
          · exact ShCraigElimBranches.isFormulaSet_translateSeq hs q hq)
        (by simp))
  unfold ShCraigElimSetup.Q at h
  rw [fstIdx_exsIntro] at h
  exact h

end ProbeTooStrong

#print axioms ProbeTooStrong.exsBlockerQ_too_strong