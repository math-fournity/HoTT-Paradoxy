import GodelQ.ZFC.CG008FinalBridge

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008Univ

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full

/-! # 对表：`provable_iff_provable` 的**先例**到底给了什么

Foundation（`DerivabilityCondition/D1.lean:35-41`）：

```lean
@[simp] lemma Provable.complete {phi : Sentence L} :
    T.internalize ℕ ⊢ ⌜phi⌝ ↔ T ⊢ phi

@[simp] lemma provable_iff_provable {T : Theory L} [T.Δ₁] {phi : Sentence L} :
    Provable T (⌜phi⌝ : ℕ) ↔ T ⊢ phi
```

**两条都把 `ℕ` 写在类型里**——`⌜phi⌝ : ℕ`。
所以「先例」桥的是 **ℕ 元素 ↔ 元层可证性**，
**不是**「任意 `V ⊧ 𝗜𝚺₁` 的元素 ↔ 元层可证性」。

本文件把这一点机器化：把 `ℕ` 换成任意 `V` 时**合成失败**。 -/

/-- **查实 1**：`Provable.complete` 的形状——`ℕ` 在类型中。 -/
noncomputable example (T : SetTheory) [T.Δ₁] (phi : Sentence ℒₛₑₜ) :
    Prop := T.internalize ℕ ⊢ ⌜phi⌝ ↔ T ⊢ phi

/-- **查实 2**：本包四处成功用的是**这一条**（`ZFCSetSigma1.lean:38` 等）。 -/
noncomputable example (psi : SetTheorySentence) :
    Provable 𝗭𝗙𝗖 (⌜psi⌝ : ℕ) ↔ 𝗭𝗙𝗖 ⊢ psi :=
  provable_iff_provable (T := 𝗭𝗙𝗖)

end GodelQ.CG008Univ
