import GodelQ.ZFC.ShCraigElimSetupQ
/-! ## ⚠ `ExsBlockerQ` 可能**过强**：`p = ⊤` 支的论证（2026-10-13）

`ExsBlockerQ` 只要求 `Q dd`（不要求 `dd` 是 `Sh.craig` 的真推导）。
若 `p = ⊤`，则 `substs1 t ⊤ = ⊤`，于是 `fstIdx dd = insert ⊤ s`，
而**任何含 `⊤` 的 sequent 都可导**（`Derivable.verum`）——
故 `Q dd` 是**无条件成立**的假设，不带信息。

那样 `ExsBlockerQ` 就会要求：对任意公式集 `s`（只要 `^∃ ⊤ ∈ s`），
`Derivable (translateSeq s)` ——**这不可能是真的**。

本探针机器核验这条论证链的每一步（不声称已证伪整个 blocker，
证伪需要模型；这里核验的是「假设无条件成立」这一步）。 -/
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000

namespace GodelQ.ProbeExsB
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

namespace GodelQ.ProbeTopRefute

-- 步 1：`substs1 t ⊤ = ⊤`（`ℒₒᵣ` 侧）—— 作为具名引理供步 5 使用
lemma substs1_top (t : V) : substs1 ℒₒᵣ t (^⊤ : V) = ^⊤ := by
  simp [substs1, Bootstrapping.substs_verum]

-- 步 2：`iT 0 ⊤ = ⊤`
example : iT (0:V) (^⊤ : V) = ^⊤ := iT_verum (V := V) 0

-- 步 3：含 `⊤` 的 sequent 无条件可导（`Derivable.verum`）
example (S : V) (hS : IsFormulaSet (L := ℒₛₑₜ) S) :
    Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖 (insert (^⊤ : V) S) :=
  Derivable.verum (s := insert (^⊤ : V) S)
    (fun q hq => by
      rcases mem_bitInsert_iff.mp hq with rfl | hq
      · exact IsSemiformula.verum (L := ℒₛₑₜ) (n := (0:V))
      · exact hS q hq)
    (by simp)

-- 步 4：把 1+2 拼起来——`Q dd` 在 `fstIdx dd = insert ⊤ s` 时无条件成立
example (s : V) (hs : IsFormulaSet (L := ℒₒᵣ) s) :
    Q (V := V) (axm (insert (^⊤ : V) s) (^⊤ : V)) := by
  unfold Q
  rw [fstIdx_axm, translateSeq_insert, iT_verum]
  exact Derivable.verum (s := insert (^⊤ : V) (translateSeq s))
    (fun q hq => by
      rcases mem_bitInsert_iff.mp hq with rfl | hq
      · exact IsSemiformula.verum (L := ℒₛₑₜ) (n := (0:V))
      · exact ShCraigElimBranches.isFormulaSet_translateSeq hs q hq)
    (by simp)

-- 步 5：★ 关键 —— `ExsBlockerQ` 的两条**非平凡**假设对任意 `s` 同时可满足
-- （`IsFormulaSet s` 与 `^∃ ⊤ ∈ s` 之外的两条：`fstIdx dd = insert (substs1 t p) s` 与 `Q dd`）
example (s X t : V) (hs : IsFormulaSet (L := ℒₒᵣ) s) :
    -- ① fstIdx 条件
    fstIdx (axm (insert (^⊤ : V) s) X) = insert (substs1 ℒₒᵣ t (^⊤ : V)) s
    -- ② `Q dd` 条件
    ∧ Q (V := V) (axm (insert (^⊤ : V) s) X) := by
  refine ⟨?_, ?_⟩
  · rw [fstIdx_axm, substs1_top]
  · unfold Q
    rw [fstIdx_axm, translateSeq_insert, iT_verum]
    exact Derivable.verum (s := insert (^⊤ : V) (translateSeq s))
      (fun q hq => by
        rcases mem_bitInsert_iff.mp hq with rfl | hq
        · exact IsSemiformula.verum (L := ℒₛₑₜ) (n := (0:V))
        · exact ShCraigElimBranches.isFormulaSet_translateSeq hs q hq)
      (by simp)

end GodelQ.ProbeTopRefute