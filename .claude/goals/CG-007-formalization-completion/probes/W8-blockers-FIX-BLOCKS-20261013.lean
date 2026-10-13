import GodelQ.ZFC.ShCraigElimSetupQ
/-! ## 修复后的 blocker 阻断了「过强」论证（2026-10-13）

`ShCraigElimSetupQ.lean` 已把 `Derivation Sh.craig dd` 补回两条 blocker。
本探针核验：修复后，`p = ⊤` 的论证**不再成立**——
它现在还需要 `Derivation Sh.craig (axm (insert ⊤ s) ⊤)`，
而这要求 `⊤ ∈ Sh.craig.Δ₁Class`（`axm` 构造子的条件），并非免费。

下面把「修复后还差什么」机器摆明。 -/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
open GodelQ.ShCraigElimSetupQ
set_option maxHeartbeats 800000

namespace ProbeFixBlocks
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- 修复后的 blocker 签名（机器核验：确实多了 Derivation 假设）
#check @GodelQ.ShCraigElimSetupQ.ExsBlockerQ
#check @GodelQ.ShCraigElimSetupQ.AllBlockerQ

-- ★ 关键：修复后，p = ⊤ 的实例还需要这一条
--    `Derivation Sh.craig (axm (insert ⊤ s) ⊤)`，由 `Derivation.axm` 需要
--    `⊤ ∈ Sh.craig.Δ₁Class`。把它作为显式假设写出来，看论证是否还能走通。
example (s : V) (hs : IsFormulaSet (L := ℒₒᵣ) s) (hps : (^∃ (^⊤ : V) : V) ∈ s)
    (hder : Derivation (V := V) (L := ℒₒᵣ) Sh.craig
      (axm (insert (^⊤ : V) s) (^⊤ : V)))
    (hB : GodelQ.ShCraigElimSetupQ.ExsBlockerQ (V := V)) :
    Derivable (V := V) (L := ℒₛₑₜ) 𝗭𝗙𝗖 (translateSeq (V := V) s) := by
  have htop : substs1 ℒₒᵣ (^&(0:V) : V) (^⊤ : V) = ^⊤ := by
    simp [substs1, Bootstrapping.substs_verum]
  have hQ : GodelQ.ShCraigElimSetup.Q (V := V) (axm (insert (^⊤ : V) s) (^⊤ : V)) := by
    unfold GodelQ.ShCraigElimSetup.Q
    rw [fstIdx_axm, translateSeq_insert, iT_verum]
    exact Derivable.verum (s := insert (^⊤ : V) (translateSeq s))
      (fun q hq => by
        rcases mem_bitInsert_iff.mp hq with rfl | hq
        · exact IsSemiformula.verum (L := ℒₛₑₜ) (n := (0:V))
        · exact GodelQ.ShCraigElimBranches.isFormulaSet_translateSeq hs q hq)
      (by simp)
  have h := hB (s := s) (p := (^⊤ : V)) (t := (^&(0:V) : V))
    (dd := axm (insert (^⊤ : V) s) (^⊤ : V)) hs hps
    (IsSemiterm.fvar (L := ℒₒᵣ) (V := V) (n := (0:V)) 0)
    (by rw [fstIdx_axm, htop]) hder hQ
  unfold GodelQ.ShCraigElimSetup.Q at h
  rw [fstIdx_exsIntro] at h
  exact h

end ProbeFixBlocks