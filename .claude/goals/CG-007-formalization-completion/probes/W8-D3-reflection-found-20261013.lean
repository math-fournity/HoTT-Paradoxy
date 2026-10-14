import GodelQ.ZFC.ShCraigElimSetupQ
/-! ## ★ D3 第四步的工具**已存在于 Foundation**：Σ₀ 反射原理（2026-10-13）

第四步要：`Evalb ![s,p'] ↑Sh.reWitness.val` ⟹ `Provable 𝗭𝗙𝗖 (…)`。

`reWitness` 是 **Σ₀** 句子（`𝚺ᴬ₀.Semisentence 2`，`CraigTrick.lean:103`），
故需要的正是 **Σ₀ 反射原理**。Foundation 在 `Absoluteness.lean` 有：

```
lemma models_iff_provable_of_Sigma0_param [V↓[ℒₒᵣ] ⊧* T] {n : ℕ}
    {σ : ArithmeticSemisentence n}
    (hσ : ℬ[<, ℒₒᵣ].Hierarchy 𝚺 0 σ) {e : Fin n → ℕ} :
    V ⊧/(Nat.cast ∘ e) σ ↔ T ⊢ (σ ⇜ fun x ↦ numeral (e x))
```

## ⚠ 两个前提（本探针确认，可能是新的障碍）

1. **`[T.SoundOnHierarchy 𝚺 1]`** —— 需要理论对 Σ₁ 层**可靠**。
   对 `T := 𝗭𝗙𝗖`，这正是本项目要证的东西的**一部分**；
   若本包没建这个 instance，这条引理用不了。

2. **`e : Fin n → ℕ`** —— 参数是 **ℕ 值**（标准数字），不是任意 V 元素。
   这是「载体」的又一实例：`reWitness` 的 `s`、`p'` 若非标准码，用不了。

**故第四步 = Σ₀ 反射 + 标准性**，而标准性正是 002-Step 报的
「标准码支已付清，障碍在非标准码」。**这与舰队的既有判断一致。**

## 附带发现：`ISigma1.exists_matrix_provable`

```
ISigma1.exists_matrix_provable :
  ℬ[<, ℒₒᵣ].Hierarchy 𝚺 1 φ → ∃ θ, 𝗜𝚺₁ ⊢ ∀¹* (φ 🡘 ∃¹ θ.val)
```

这正是 `reWitness` 的定义来源（`CraigTrick.lean:104` 用了它的 `.choose.val`）。
它本身是 **`∃ θ` + `𝗜𝚺₁ ⊢`** 的形式——**元层的**，不是 V 层可用的。

本探针核验这条工具的形状与可用性。 -/
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000

namespace GodelQ.ProbeExsB
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
namespace ProbeD3Reflection

#check @models_iff_provable_of_Sigma0_param
#check @sigma_one_completeness_iff_param
#check @ISigma1.exists_matrix_provable

end ProbeD3Reflection