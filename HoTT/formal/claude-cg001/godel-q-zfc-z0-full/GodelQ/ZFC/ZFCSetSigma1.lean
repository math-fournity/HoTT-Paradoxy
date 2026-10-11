import GodelQ.ZFC.Z0Full

/-!
# CG-008 · Phase 0（下游扩展，纯 `HoTT/formal/`，不改 Foundation）

本文件是 ZFC 集合论 Σ₁ 完全性（Z0 唯一实质缺口 `zfcTr_D3_internalize` 的闭合主线）的
**Phase 0 基础设施锚点**。

## 本阶段已机器证明的内容

* `zfcProvable_iff_arith`：把集合论可证性 `Provable 𝗭𝗙𝗖 (⌜ψ⌝)` 与其算术 Σ₁ 半句
  `(provable 𝗭𝗙𝗖).val/[⌜ψ⌝]` 等价起来——确认「ZFC 证明了集合句 ψ 的编码」这一陈述
  本身是一个**算术 Σ₁** 陈述（因为 `provable 𝗭𝗙𝗖 : 𝚺ᴬ₁.Semisentence 1` 对任意理论通用，
  见 `Foundation/.../Proof/Basic.lean:556`，本包 `Z0Full.lean:41` 已成功使用）。
* `zfcProvable_arith_sigma1`：显式给出该陈述的 `ℬ[<, ℒₒᵣ].Hierarchy 𝚺 1` 层级证据。

这两步锁定了 CG-008 的「Σ₁」半边：缺口 `zfcTr_D3_internalize` 两端
`Provable 𝗭𝗙𝗖 (⌜translate τ⌝)` / `Provable 𝗭𝗙𝗖 (⌜translate (zfcTr τ)⌝)` 都是算术 Σ₁ 陈述。
尚缺的「完全性」半边（真 → 可证，内部化）即 `set_sigma_one_complete`，需把
`D3.lean` 的算术机器平移到 Lévy 层级，关键依赖 `SetTheory/Basic/Hierarchy.lean` 的
`setTheory_sigma₁_induction'` 与集合论项求值完全性（仿 `D3.lean:45` 的本地 `term_complete`）。
见 `CG008_PROJECT.md` §3 / §5。

本文件不含任何未证标记，可进入收据。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.ZFCSetSigma1

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full

/-- ZFC 对集合句 ψ 的可证性（元层 `𝗭𝗙𝗖 ⊢ ψ`）与编码层 `Provable 𝗭𝗙𝗖 (⌜ψ⌝ : ℕ)`
逐字对应；直接由 Foundation 的通用 `provable_iff_provable`（需 `[𝗭𝗙𝗖.Δ₁]`，
已由 `ZFCDelta1.lean` 证得）给出。 -/
theorem zfcProvable_iff_provable {ψ : SetTheorySentence} :
    Provable 𝗭𝗙𝗖 (⌜ψ⌝ : ℕ) ↔ 𝗭𝗙𝗖 ⊢ ψ :=
  provable_iff_provable (T := 𝗭𝗙𝗖)

/-- 因此 `Provable 𝗭𝗙𝗖 (⌜ψ⌝)` 是一个算术 Σ₁ 陈述。 -/
theorem zfcProvable_arith_sigma1 {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁] {ψ : SetTheorySentence} :
    ℬ[<, ℒₒᵣ].Hierarchy 𝚺 1 ((provable 𝗭𝗙𝗖).val/[⌜ψ⌝] : ArithmeticSentence) :=
  (provable 𝗭𝗙𝗖).sigma_prop.rew (ω := _)

end GodelQ.ZFCSetSigma1
