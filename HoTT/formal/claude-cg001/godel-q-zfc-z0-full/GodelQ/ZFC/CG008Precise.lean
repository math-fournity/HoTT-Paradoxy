import GodelQ.ZFC.CG008N2V

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008Precise

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full GodelQ.CG008N2V

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! # 精确缺口：一条最小技术命题

## 命题 `the_gap`

```lean
theorem the_gap (sigma : ArithmeticSentence) :
    V↓[ℒₒᵣ] ⊧ zfcTr sigma → Provable 𝗭𝗙𝗖 (iT 0 ⌜sigma⌝)
```

**两边都可陈述**，且都在本包既有定义里（`models_trProv_iff` 给左端语义，
`TrProvable` 给右端）。

## 三段拆解（本轮机器核实的位置）

| 段 | 内容 | API |
|---|---|---|
| A | `V ⊧ zfcTr sigma ↔ Provable 𝗭𝗙𝗖 ⌜translate sigma⌝` | `models_trProv_iff` |
| B | `⌜translate sigma⌝ = iT 0 ⌜sigma⌝` | `iT_quote` |
| **C** | `Provable 𝗭𝗙𝗖 ⌜translate sigma⌝ → Provable 𝗭𝗙𝗖 ⌜translate (zfcTr sigma)⌝` | **缺** |

A、B 已通（`CG008Bridge1` 已用 A+B）。

**C 就是 ZFC 内部的 Σ₁ 完备性**：
`zfcTr sigma` 是 Σ₁ 算术句，要把它在 ℒₜ 里的翻译也变成 ZFC 可证。

## Foundation 已给 / 缺什么

**已给**（`CG008N2V` 核实）：
`natCastEmbedding : ℕ ↪ₛ[ℒₒᵣ] V` + `IsInitial` 实例——
Σ₁ 沿此嵌入的绝对性对 **ℒₒᵣ** 句成立。

**缺**：同一件事对 **ℒₜ 推导码**的版本。
具体说，Foundation 没有

```lean
-- 想要的（Foundation 目前没有）
theorem zfc_sigma1_internalize (sigma : ArithmeticSentence) :
    Provable 𝗭𝗙𝗖 (⌜arithTrln.translate sigma⌝ : V) →
      Provable 𝗭𝗙𝗖 (⌜arithTrln.translate (zfcTr sigma)⌝ : V)
```

算术版的对应物**有**：`provable_internalize`
（`D3.lean:175`，`T : ArithmeticTheory` + `[T.Δ₁]` + `[𝗣𝗔⁻ ⪯ T]`），
但它不能取 `T := 𝗭𝗙𝗖`——`𝗭𝗙𝗖 : SetTheory = Theory ℒₜ` 不是 `ArithmeticTheory`。

**治理**：本文件只记命题与 API 位置，不含未证标记。 -/

/-- **查实 1**：A 段——左端的语义桥（`models_trProv_iff`）。 -/
example (V : Type) [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
    (sigma : ArithmeticSentence) :
    V↓[ℒₒᵣ] ⊧ zfcTr sigma ↔ Provable 𝗭𝗙𝗖 (⌜arithTrln.translate sigma⌝ : V) :=
  models_trProv_iff V sigma

end GodelQ.CG008Precise
