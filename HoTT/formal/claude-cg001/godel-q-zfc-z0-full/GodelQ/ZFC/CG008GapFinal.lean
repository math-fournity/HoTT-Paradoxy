import GodelQ.ZFC.CG008ITParts

/-!
# CG-008 · 缺口的**最终精确定位**（2026-10-13 第十一轮）

## 结论一句话

缺口 = **ZFC 内部的 Σ₁ 完备性**：
`V 🧡 TrProvable(x) → Provable 𝗭𝗙𝗖 (iT 0 x)`。
Foundation **有算术版**（`D3.lean:162` `sigma_one_provable_of_models`，前提 `[T.Δ₁] [𝗣𝗔⁻ ⪯ T]`），
**没有集合论版**。

## 怎么走到这一步的

`hD3G : 𝗜𝚺₁ ⊢ zfcTr σ → zfcTr (zfcTr σ)` 由 Foundation 的
`instance [∀ σ, 𝔅.FormalizedCompleteOn (𝔅 σ)] : 𝔅.HBL3 := ⟨by simp⟩`
（`ProvabilityAbstraction/Basic.lean:93`）归约到：
`∀ σ, [zfcTr.FormalizedCompleteOn (zfcTr σ)]`，即 `∀ σ, 𝗜𝚺₁ ⊢ zfcTr σ → zfcTr (zfcTr σ)`。
**前提没变弱，问题没消失**（与 2026-10-12 第四轮的结论一致）。

展开 `zfcTr σ = trProv.val/[⌜σ⌝]`（`Z0Full.lean:60,65`），其中
`trProv = "x. ∃ y, !iTDef y 0 x ∧ !(provable 𝗭𝗙𝗖) y"`（`Z0Full.lean:40`）：

```
zfcTr σ       = ∃ y, iT 0 ⌜σ⌝ = y ∧ provable 𝗭𝗙꜀ y
zfcTr (zfcTr σ) = ∃ y, iT 0 ⌜(zfcTr σ)⌝ = y ∧ provable 𝗭𝗙꜀ y
```

所以 `hD3G` 的语义内容（在任意 V 中）是：

```
(∃ y, iT 0 ⌜σ⌝ = y ∧ Provable 𝗭𝗙꜀ y)  →   (∃ y, iT 0 ⌜(zfcTr σ)⌝ = y ∧ Provable 𝗭𝗙꜀ y)
```

**前件取见证 `y = iT 0 ⌜σ⌝ = ⌜translate σ⌝`**（用现已证通的 `iT_quote`）。
所以后件需要的是：**`Provable 𝗭𝗙꜀ ⌜translate (zfcTr σ)⌝`**。

而 `translate (zfcTr σ)` 是一个 **Σ₁ 句的翻译**（`zfcTr σ` 是 Σ₁，`iT` 保 Σ₁——
这一点现在由 `CG008ITParts.iT_isUFormula` 与 Foundation 的 `iT` 定义保障）。
**于是缺口就是：ZFC 证明真的 Σ₁ 算术句的翻译。**

## 与算术版的逐条对照

| | 算术版（Foundation `D3.lean:162`） | 需要的集合论版 |
|---|---|---|
| 陈述 | `V 🧡 σ → Provable T ⌜σ⌝`（σ 是 **Σ₁ 算术句**） | `V 🧡 TrProvable x → Provable 𝗭𝗙꜀ (iT 0 x)` |
| 前提 | `[T.Δ₁]`、`[𝗣𝗔⁻ ⪯ T]` | 需要什么？**未查清** |
| 证明走 | `bold_sigma_one_complete` + `toNumVec` 代入 | 不能用 `toNumVec`（`ℒₜ` 无常项） |

**`toNumVec` 这一行是关键**：算术版把 V 的元素代换成**数字项** `𝕹 v`，
靠的是 `ℒₒᵣ` 有数字项；`ℒₜ` **没有**，所以这条证明**无法照搬**——
这正是 2026-10-12 第四轮「P1 的 hMem/hNMem 是对的」那条判断的根据。

## 为什么不能改用语义论证

自然的替代是 `SetTheory.complete`（`SetTheory/Basic/Misc.lean:269`）：
要证 `𝗭𝗙꜀ ⊢ φ`，只需证「每个 `M 🧡 𝗭𝗙꜀` 满足 φ」。
**但 V 本身可能就是那个非标准的 `M ⊧ 𝗭𝗙꜀`**，而对它要建
「`M ⊧ TrProvable x` `→` `M ⊧ ∃d, 是 x 的翻译的推导`」——
这就是**在 V 内把元层推导对象变成 V 的元素**，即原先的 `bridge`。
**换了外衣，没换内容。**

## 治理

- Foundation 只读；本文件纯下游。
- 本文件不含未证标记。
- **记录的是定位，不是证明。**
-/

namespace GodelQ.CG008GapFinal

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **查实 1**：Foundation 的 `HBL3` 实例**只吃 `FormalizedCompleteOn`**，
所以归约确如上述、前提不弱化。 -/
example {𝔅 : ProvabilityAbstraction.Provability 𝗜𝚺₁ Sh} [∀ σ, 𝔅.FormalizedCompleteOn (𝔅 σ)] :
    𝔅.HBL3 := inferInstance

/-- **查实 2**：算术版 Σ₁ 完备性**存在**且前提是 `[T.Δ₁]`、`[𝗣𝗔⁻ ⪯ T]`。 -/
example (T : ArithmeticTheory) [Theory.Δ₁ T] [𝗣𝗔⁻ ⪯ T] {σ : ArithmeticSentence}
    (_hσ : ℬ[<, ℒₒᵣ].Hierarchy 𝚺 1 σ) :
    V↓[ℒₒᵣ] ⊧ σ → Provable T (⌜σ⌝ : V) :=
  Bootstrapping.Arithmetic.sigma_one_complete (T := T) _hσ

/-- **查实 3**：`SetTheory.complete` 是语义路线，需要「每个 M 满足 φ」——
而 V 本身可以是那个 M。 -/
example {φ : SetTheorySentence}
    (H : ∀ (M : Type*) [SetStructure M] [Nonempty M] [M↓[ℒₛₑₜ] ⊧* 𝗭𝗙𝗖], M↓[ℒₛₑₜ] ⊧ φ) :
    𝗭𝗙𝗖 ⊢ φ :=
  SetTheory.complete 𝗭𝗙𝗖 φ H

end GodelQ.CG008GapFinal