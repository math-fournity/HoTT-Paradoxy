import GodelQ.ZFC.CG008Probe17

/-!
# CG-008 探针 18（非收据）：`𝗭𝗙𝗖.standardProvability` 能否成立

## 探针 17 的发现

`Provability` 是**多语言**的：`Provability (T₀ : Theory L₀) (T : Theory L)`，
只要求 `[L.ReferenceableBy L₀]`。而 `ℒₒᵣ` 对**任意** `[Encodable α]` 有
`GödelNumber ℒₒᵣ α`（`Arithmetic/Basic/Misc.lean:114`），
所以 `Semiterm.Operator.GödelNumber ℒₒᵣ (Sentence ℒₛₑₜ)` 成立
⇒ **`Provability 𝗜𝚺₁ 𝗭𝗙𝗖` 可陈述**（探针 17 查实）。

## 本探针要查实的

`StandardProvability.lean:42` 的 `standardProvability` 声明是

```lean
variable {L : Language} [L.Encodable] [L.LORDefinable] {T : Theory L} [T.Δ₁]
noncomputable abbrev Theory.standardProvability : Provability 𝗜𝚺₁ T where
  prov := provable T
  bew_def := provable_D1
```

**若 `[ℒₛₑₜ.Encodable]`、`[ℒₛₑₜ.LORDefinable]`、`[𝗭𝗙𝗖.Δ₁]` 三者都能合成**，
则 `𝗭𝗙𝗖.standardProvability : Provability 𝗜𝚺₁ 𝗭𝗙𝗖` 成立，
而 `provable_D3` 的实例（`StandardProvability.lean:90`，前提 `[𝗣𝗔⁻ ⪯ T]`）
也许能给出 **`𝗭𝗙𝗖.standardProvability.HBL3`**——那就**直接闭合缺口**。

**关键未知**：`[ℒₛₑₜ.LORDefinable]`。`LORDefinable` 说语言 L 在 ℒₒᵣ 里可定义；
对 `ℒₛₑₜ`，这需要集合成员关系是算术可定义的——正是 `arithTrln` 那套的工作。

## 本探针逐条查实这三个前提
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008Probe18

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full GodelQ.CG008HBL3
  GodelQ.CG008HBL3Test GodelQ.CG008Final GodelQ.CG008Probe15 GodelQ.CG008Probe16
  GodelQ.CG008Probe17

/-- **查实 1**：`ℒₛₑₜ` 的编码实例成立（`SetTheory/Basic/Misc.lean:64`）。

注意 `Encodable` 是**逐元数**的（`(k : ℕ) → Encodable (L.Func k)`），
不是语言上的单个类。 -/
example : (k : ℕ) → Encodable ((ℒₛₑₜ).Func k) := fun _ ↦ inferInstance

example : (k : ℕ) → Encodable ((ℒₛₑₜ).Rel k) := fun _ ↦ inferInstance

/-- **查实 2**：`[𝗭𝗙𝗖.Δ₁]` 成立（`ZFCDelta1.lean`）。 -/
noncomputable example : 𝗭𝗙𝗖.Δ₁ := inferInstance

/-- **查实 3（关键未知）**：`[ℒₛₑₜ.LORDefinable]` 成立吗？

`LORDefinable`（`Arithmetic/Bootstrapping/Syntax/Language.lean:22`）要求：
语言的函数与关系符号的编码集合是**算术 Σ₀ 可定义**的
（`func : 𝚺ᴬ₀.Semisentence 2`、`rel : 𝚺ᴬ₀.Semisentence 2`）。

对 `ℒₛₑₜ`：只有 `Mem` 一个二元关系、没有函数符号，
所以 `rel` 要刻画「`(k, c)` 使得 `c` 是 `Mem` 在元数 `k` 下的码」。

**这条若成立，`𝗭𝗙𝗖.standardProvability : Provability 𝗜𝚺₁ 𝗭𝗙𝗖` 就成立**，
而 `provable_D3` 的实例（前提 `[𝗣𝗔⁻ ⪯ T]`）也许能给出
`𝗭𝗙𝗖.standardProvability.HBL3`——那就**直接闭合缺口**。

**但注意 `provable_D3` 的结论是 `𝗜𝚺₁ ⊢ □σ 🡒 □□σ`，其中 `□ = provabilityPred T`，
`σ : Sentence L`**。对 `T = 𝗭𝗙𝗖`，`σ` 是**集合句**，
而 `□□σ = □(□σ)` 里 `□σ` 是**算术句**，不是集合句——
**类型不匹配**。所以 `provable_D3` 对 `L = ℒₛₑₜ` **用不了**。

这正是缺口的深层原因：`HBL3.D3` 要求 `𝔅 (𝔅 σ)` 里的 `𝔅 σ` 仍是 `L` 的句子，
而可证性谓词把 `L` 句变成了 `L₀` 句。**只有当 `L = L₀` 时才自洽**，
而缺口恰恰是跨语言的（集合句 ↔ 算术句）。

本探针把这一点固定下来。 -/
example : FFL.FirstOrder.Language.LORDefinable ℒₛₑₜ := inferInstance

end GodelQ.CG008Probe18
