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

证法：`IsSemiformula.case_iff`（8 支）+ `quote_*` 族（rfl）。
对 `m` 做 `Nat.strong_induction` 处理递归支（`and`/`or` 层数不变、
`all`/`exs` 层数 +1，但**码更小**，故用 `m` 的强归纳即可）。

⚠ 为什么层数写成 `↑m` 而非任意 `n : V`：
`quote_verum`/`quote_falsum` 的形状是 `{n : ℕ}`，而 `^⊤` 在任意 `n : V` 层都成立；
V 层没有 `V → ℕ` 转换，故 `n` 任意时 `⊤` 支取不出见证。

## 当前状态（2026-10-13）

**已证 2/8 支**：`⊤`、`⊥`（`exact ⟨⊤, by simp⟩`）。

**剩余 6 支**，两类困难：
* **`rel`/`nrel`**：需「项向量 `v` 的每个分量是引号」的**姊妹引理**
  （`IsSemitermVec → ∃ 引号向量`），同样需要结构递归；
* **`and`/`or`**：**同层**递归 ⇒ 对 `m` 的强归纳**不够**，
  须对**码本身**递归（`IsSemiformula` 的 `pi1_structural_induction`
  要求 `P` 是 Π₁ 关系，而我们的 `P` 含 `∃ φ : Semiproposition …`，不是 Π₁）；
* **`all`/`exs`**：层数 `↑m + 1` vs `↑(m+1)` 须对齐，另加 `m+1` 的归纳调用。

**结论**：这条引理**不是一行事**，需要真正的结构递归 + definability 工作。
但**它对语义路线不是必需的**——见下。

## ★ 更短的替代：不需要反向引理

语义路线真正需要的只是 `Provable 𝗭𝗙𝗖 φ` 对**具体的** φ。
`ExsBridge2` 的 φ 是 `imp (iT 0 (substs1 t p)) (^∃ (domZero ⋏ iT 1 p))`，
其中 `p` 在 `ExsBlockerQ` 里来自 `^∃ p ∈ s`（`s` 是公式集），
**但 `ExsBlockerQ` 可以改成对 `p` 的具体形状分情况**——
`ShCraigElimBranches` 的 `induction1` 支本来就是沿推导结构给的，
`p` 会以具体构造子形出现。这条要另开一轮核验。 -/
theorem isSemiformula_exists_quote {m : ℕ} {p : V}
    (hp : IsSemiformula ℒₛₑₜ (↑m : V) p) :
    ∃ φ : Semiproposition ℒₛₑₜ m, p = (⌜φ⌝ : V) := by
  induction m using Nat.strong_induction_on generalizing p with
  | _ m ih =>
    rcases IsSemiformula.case_iff.mp hp with
      ⟨k, R, v, hk, hv, rfl⟩ | ⟨k, R, v, hk, hv, rfl⟩ |
      rfl | rfl |
      ⟨p₁, p₂, h₁, h₂, rfl⟩ | ⟨p₁, p₂, h₁, h₂, rfl⟩ |
      ⟨p₁, h₁, rfl⟩ | ⟨p₁, h₁, rfl⟩
    · sorry
    · sorry
    · exact ⟨⊤, by simp⟩
    · exact ⟨⊥, by simp⟩
    · -- and：同层递归，用码本身的强归纳（下轮）
      sorry
    · sorry
    · -- all：`p₁` 层 `↑m + 1 = ↑(m+1)`，但 `↑(m+1)` 与 `↑m + 1` 须对齐
      sorry
    · sorry

#print axioms ProbeReverseQuote.isSemiformula_exists_quote

end ProbeReverseQuote