import GodelQ.ZFC.ShCraigElimSetupQ
/-! ## ★ 反向引理：IsSemiformula → 是引号（2026-10-13）

语义路线的最后一件：把 V 层的公式码识别成 Semiproposition 的引号。
Foundation 只有正向（quote_isSemiformula），反向不存在。

但 IsSemiformula.case_iff 给出 8 支析取，每支都是构造子形，
而 quote_* 族都是 rfl —— 故反向引理应当可证。

本探针证它（用 IsSemiformula.induction，不用 case_iff）。 -/
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000

namespace GodelQ.ProbeExsB
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
namespace ProbeReverseQuote

/-- 反向引理（**层数取 ℕ 版本**）：层 `↑m` 的公式码是某 `Semiproposition L m` 的引号。

证法：`IsSemiformula.sigma1_structural_induction`（**只需 Σ₁**，
而我们的谓词含 `∃ φ`，正是 Σ₁ 形——Π₁ 版会卡住，Σ₁ 版不会）。 -/
theorem isSemiformula_exists_quote {m : ℕ} {p : V}
    (hp : IsSemiformula ℒₛₑₜ (↑m : V) p) :
    ∃ φ : Semiproposition ℒₛₑₜ m, p = (⌜φ⌝ : V) := by
  -- 谓词 `P n q := ∃ (m : ℕ), n = ↑m ∧ ∃ φ : Semiproposition ℒₛₑₜ m, q = ⌜φ⌝`
  -- 它含两层 `∃`，是 Σ₁ 形，故可用 `sigma1_structural_induction`
  suffices h : ∀ (n : V) (q : V), IsSemiformula ℒₛₑₜ n q →
      ∃ (k : ℕ) (φ : Semiproposition ℒₛₑₜ k), n = (↑k : V) ∧ q = (⌜φ⌝ : V) from
    (by
      obtain ⟨k, φ, hk, hq⟩ := h (↑m) p hp
      have : k = m := by exact_mod_cast hk.symm
      subst this
      exact ⟨φ, hq⟩)
  apply IsSemiformula.sigma1_structural_induction (L := ℒₛₑₜ)
    (P := fun n q ↦ ∃ (k : ℕ) (φ : Semiproposition ℒₛₑₜ k), n = (↑k : V) ∧ q = (⌜φ⌝ : V))
  · definability
  · -- rel
    intro n k r v hk hv; sorry
  · intro n k r v hk hv; sorry
  · intro n; exact ⟨0, ⊤, by simp, by simp⟩
  · intro n; exact ⟨0, ⊥, by simp, by simp⟩
  · intro n p₁ p₂ h₁ h₂ ih₁ ih₂; sorry
  · intro n p₁ p₂ h₁ h₂ ih₁ ih₂; sorry
  · intro n p₁ h₁ ih; sorry
  · intro n p₁ h₁ ih; sorry

#print axioms ProbeReverseQuote.isSemiformula_exists_quote

end ProbeReverseQuote