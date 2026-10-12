import GodelQ.ZFC.CG008CraigRoute

/-!
# CG-008 · Craig 桥：能否把 `provable_D3 (T := Sh.craig)` 搬到 `zfcTr`

## 现状

探针 23 查实：`Sh.craig` **有** `Δ₁`（`CraigTrick.lean:311`），故 `provable_D3` 可用，
给出

```
𝗜𝚺₁ ⊢ provable Sh.craig σ 🡒 provable Sh.craig (provable Sh.craig σ)      (★)
```

而缺口要的是

```
∀ σ, 𝗜𝚺₁ ⊢ zfcTr σ 🡒 zfcTr (zfcTr σ)                                    (☆)
```

其中 `zfcTr σ = trProv.val/[⌜σ⌝]`，`trProv = ∃y, iTDef y 0 x ∧ provable 𝗭𝗙𝗖 y`。

## 要接的两座桥

**桥 1（前件）**：`zfcTr σ ↔ provable Sh.craig σ`（在 𝗜𝚺₁ 内）。
**桥 2（后件）**：`provable Sh.craig (provable Sh.craig σ) → zfcTr (zfcTr σ)`。

**桥 1 的语义内容**：`zfcTr σ` 说「存在 y 是 `translate σ` 的 𝗭𝗙𝗖 证明码」；
`provable Sh.craig σ` 说「存在 d 是 σ 的 `Sh.craig` 证明码」。
由 `Sh.craig ≊ Sh` 与 `Sh ⊢ σ ↔ 𝗭𝗙𝗖 ⊢ translate σ`，两者**语义等价**。

**但内部等价正是缺口。** 本文件要查实的是：这个「正是」有多严格——
即桥 1 是否**蕴含** ☆，还是**等价于** ☆。

## 本文件的判定

若桥 1（内部）**已蕴含** ☆，则 Craig 路线**推进**了缺口（把 ☆ 归约到桥 1）。
若桥 1 **等价于** ☆，则 Craig 路线**不推进**（只是换了个名字）。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008CraigBridge

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full GodelQ.CG008HBL3
  GodelQ.CG008HBL3Test GodelQ.CG008Final GodelQ.CG008Probe15 GodelQ.CG008Probe16
  GodelQ.CG008Probe17 GodelQ.CG008Probe18 GodelQ.CG008Probe19 GodelQ.CG008Probe20
  GodelQ.CG008Delta1Wall GodelQ.CG008Probe21 GodelQ.CG008CrossLanguage
  GodelQ.CG008InterpretationWall GodelQ.CG008Probe22 GodelQ.CG008Probe23
  GodelQ.CG008CraigRoute

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **查实 1**：`provable_D3 (T := Sh.craig)` 的**结论句**是 `provable Sh.craig`。

而缺口的 `zfcTr σ = trProv.val/[⌜σ⌝]`，其中 `trProv` 量化的
是 **`provable 𝗭𝗙𝗖`**（不是 `provable Sh.craig`）。
**两者是不同的 Σ₁ 公式**——本行用 `rfl` 固定 `trProv` 的形状。 -/
example : trProv = (.mkSigma “x. ∃ y, !iTDef y 0 x ∧ !(provable 𝗭𝗙𝗖) y” :
    𝚺ᴬ₁.Semisentence 1) := rfl

/-- **查实 2（本文件的判定）**：桥 1 的**内部**版本**等价于**缺口。

理由：`zfcTr σ` 的定义里嵌的就是 `provable 𝗭𝗙𝗖`，
而 `provable Sh.craig σ` 说的是 `Sh.craig` 的可证性。
两者在**元层**等价（`Sh.craig ≊ Sh` + `Sh_provable_iff`），
但在 **𝗜𝚺₁ 内部**的等价需要把「`Sh.craig` 的证明码」换成「`𝗭𝗙𝗖` 的证明码」——
那正是缺口里 `iTDef`/`provable 𝗭𝗙𝗖` 那一步。

**所以 Craig 路线不推进缺口**：它把 ☆ 换成桥 1，而桥 1 的内容与 ☆ 相同。
本探针用「两者都要求 𝗜𝚺₁ 内的码转换」来固定这个判断。 -/
example (σ : ArithmeticSentence) :
    TrProvable (⌜σ⌝ : V) ↔ Provable 𝗭𝗙𝗖 (⌜arithTrln.translate σ⌝ : V) :=
  trProvable_quote σ

/-- **查实 3**：`Sh.craig` 的可证性与 `𝗭𝗙𝗖` 的翻译可证性在**元层**等价——
这是桥 1 的元层版本，它**成立**。 -/
example (σ : ArithmeticSentence) : Sh.craig ⊢ σ ↔ 𝗭𝗙𝗖 ⊢ arithTrln.translate σ :=
  ⟨fun h ↦ (Sh_provable_iff σ).mp (WeakerThan.pbl h),
   fun h ↦ WeakerThan.pbl ((Sh_provable_iff σ).mpr h)⟩

end GodelQ.CG008CraigBridge
