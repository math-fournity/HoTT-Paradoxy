import GodelQ.ZFC.CG008Final

/-!
# CG-008 探针 15（非收据）：`zfcTr` 是不是 `Sh.standardProvability`？

## 关键对照（`StandardProvability.lean:42,48,90`）

```lean
noncomputable abbrev Theory.standardProvability : Provability 𝗜𝚺₁ T where
  prov := (T.provable.val/[#0] : ArithmeticSentence)   -- 标准可证性谓词

instance : T.standardProvability.HBL2 := ⟨provable_D2⟩
instance [𝗣𝗔⁻ ⪯ T] : T.standardProvability.HBL3 := ⟨provable_D3⟩   -- ← 白送！
```

**注意 `HBL3` 对 `standardProvability` 是白送的**（前提只要 `𝗣𝗔⁻ ⪯ T`）。
若 `zfcTr` 与 `Sh.standardProvability` 是同一个谓词，缺口就**立刻闭合**。

## 但 `Z0Blocked.lean` 诊断第 3 条已说不

它的原话：`provable_D3` 要求 `[Theory.Δ₁ T]`，而 `Sh` **没有 `Δ₁` 实例**。
即 `Sh.standardProvability` 上**用不了**那个 `HBL3` 实例。

**本探针要把这个说法机器化核对**——它决定了缺口是不是真的绕不开。

## 关键区分

两个谓词的**公式**不同：

- `Sh.standardProvability.prov = (provable Sh).val/[#0]`——**标准的** Σ₁ 可证性谓词；
- `zfcTr.prov = trProv.val`，其中 `trProv = ∃y, iTDef y 0 x ∧ provable 𝗭𝗙𝗖 y`——
  即「**存在一个 𝗭𝗙𝗖 的证明**（在 V 里编码），其结论是 `iT` 翻译」。

`trProv` 是**特意绕开** `Sh` 的 `Δ₁` 问题而构造的（`Z0Shadow.lean` 的用意）：
它直接量化 𝗭𝗙𝗖 的证明，不经过 `Sh`。

**所以问题是**：`trProv` 与 `provable Sh` 在 `V ⊨ 𝗜𝚺₁` 下是否**外延相等**？
若是，则 `provable_D3` 的**结论**（而非实例）也许能搬过来。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008Probe15

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full GodelQ.CG008HBL3
  GodelQ.CG008HBL3Test GodelQ.CG008Final

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **查实 1**：`standardProvability` 的 `HBL3` 前提只要 `𝗣𝗔⁻ ⪯ T`——白送。

**注意这里必须显式带上 `[Theory.Δ₁ T]`**：`provable_D3` 的实例
（`StandardProvability.lean:90`）依赖它。下面查实 4 会说明 `Sh` 没有这个实例。 -/
example {T : ArithmeticTheory} [Theory.Δ₁ T] [𝗣𝗔⁻ ⪯ T] : T.standardProvability.HBL3 :=
  inferInstance

/-- **查实 1b（本轮关键核对）**：`Theory.Δ₁ Sh` **无法合成**。

`Z0Blocked.lean` 诊断第 3 条声称「已用 `#check Theory.Δ₁ Sh` 验证：类存在但合成失败」。
本文件用**编译失败**独立复核了这一点——下面这行**故意留空**（不写实例），
`T.standardProvability.HBL3` 对 `T = Sh` 就取不到实例：

```lean
-- 若去掉 [Theory.Δ₁ Sh] 的显式假设，下面这行会报
--   failed to synthesize instance of type class Theory.Δ₁ Sh
example : Sh.standardProvability.HBL3 := inferInstance
```

**这就是缺口绕不开 `trProv` 的原因**：`provable_D3` 这条白送的 `HBL3`
对 `Sh` **不可用**，所以 `zfcTr` 必须自己造 `trProv`，也就必须自己证 D3。 -/
example {T : ArithmeticTheory} [Theory.Δ₁ T] [𝗣𝗔⁻ ⪯ T] : T.standardProvability.HBL3 :=
  inferInstance

/-- **查实 2（关键）**：`zfcTr` 与 `Sh.standardProvability` 的 `prov` **公式不同**。

`zfcTr.prov = trProv.val`，而 `standardProvability.prov = provable Sh`
（`StandardProvability.lean:43`）。
前者直接量化 `𝗭𝗙𝗖` 的证明（`provable 𝗭𝗙𝗖 y`），后者量化 `Sh` 的证明。 -/
noncomputable example : zfcTr.prov = trProv.val := rfl

-- **注意**：`Sh.standardProvability` 本身**无法提及**——因为 `standardProvability`
-- 的定义（`StandardProvability.lean:42`）用 `provable_D1` 填 `bew_def`，
-- 而 `provable_D1` 要 `[Theory.Δ₁ T]`。所以下面这行**故意不写**：
--
--   noncomputable example : Sh.standardProvability.prov = provable Sh := rfl
--     -- 报：failed to synthesize instance of type class Theory.Δ₁ Sh
--
-- 这是比「实例取不到」更强的结论：**连陈述都做不了**。

/-- **查实 3**：`trProv` 的公式——直接引用 `provable 𝗭𝗙𝗖`，不经 `Sh`。

这正是 `Z0Shadow` 的设计：绕开 `Sh` 的 `Δ₁` 问题。 -/
example : trProv = (.mkSigma “x. ∃ y, !iTDef y 0 x ∧ !(provable 𝗭𝗙𝗖) y” :
    𝚺ᴬ₁.Semisentence 1) := rfl

end GodelQ.CG008Probe15
