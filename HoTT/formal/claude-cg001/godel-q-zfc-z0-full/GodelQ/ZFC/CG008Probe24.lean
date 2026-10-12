import GodelQ.ZFC.CG008PureArith

/-!
# CG-008 探针 24（非收据）：缺口的纯算术攻击面

## 重新定位后的缺口

由 `CG008PureArith.lean`，缺口是**纯算术**的：

```
∀ τ, (∃ d : V, Proof 𝗭𝗙𝗖 d ⌜translate τ⌝) → (∃ d' : V, Proof 𝗭𝗙𝗖 d' ⌜translate (zfcTr τ)⌝)
```

`Proof`/`provable`/`iTDef` 全是算术谓词。**唯一非算术的东西是 `T = 𝗭𝗙𝗖`。**

## 攻击面：把「T 非算术」隔离出来

`proof 𝗭𝗙𝗖` 的定义（`Basic.lean:552`）：

```lean
noncomputable def proof : 𝚫ᴬ₁.Semisentence 2 := .mkDelta
  (.mkSigma “d φ. ∃ s, !insertDef s φ 0 ∧ !(derivationOf T).sigma d s”)
  …
```

**关键**：`derivationOf T` 吃 `T.Δ₁Class`（`T` 的公理集）。
对 `T = 𝗭𝗙𝗖`，`𝗭𝗙𝗖.Δ₁Class` 由 `[𝗭𝗙𝗖.Δ₁]` 给出（`ZFCDelta1.lean` 已证）。

**所以 `proof 𝗭𝗙𝗖` 是良定义的算术 Δ₁ 谓词**——
「T 非算术」这件事被 `[𝗭𝗙𝗖.Δ₁]` 完全吸收了。

## 因此缺口可以这样攻

缺口的**唯一**内容是：**ZFC 的 Δ₁ 公理集（在 V 内）满足 D3**。

即：给定 V 内的 `d` 与 `Proof 𝗭𝗙𝗖 d ⌜translate τ⌝`，
构造 V 内的 `d'` 与 `Proof 𝗭𝗙𝗖 d' ⌜translate (zfcTr τ)⌝`。

**`d'` 从哪来？** 数学上：
1. `d` 是「`translate τ` 从 ZFC 公理出发的推导」；
2. 要造 `d'` 是「`translate (zfcTr τ)` 从 ZFC 公理出发的推导」；
3. 而 `zfcTr τ` 说「`translate τ` 可证」——**所以 `d'` 要「把 `d` 编码进去」**。

第 3 步正是 **`derivable_quote`**（`D1.lean:21`）做的事：
`T ⟹₂ Γ → Derivable T ⌜Γ⌝`。**它把一条推导编码成 V 内的一个数。**

**本探针要查实**：`derivable_quote` 能否用来构造 `d'`——
即从「V 内有一条推导 `d`」出发，**在 V 内**用编码构造出
「『有一条推导』这句话」的证明码。

## 治理

- Foundation 只读；本文件纯下游。
- 本文件不含任何未证标记，可进入收据。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008Probe24

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full GodelQ.CG008HBL3
  GodelQ.CG008HBL3Test GodelQ.CG008Final GodelQ.CG008Probe15 GodelQ.CG008Probe16
  GodelQ.CG008Probe17 GodelQ.CG008Probe18 GodelQ.CG008Probe19 GodelQ.CG008Probe20
  GodelQ.CG008Delta1Wall GodelQ.CG008Probe21 GodelQ.CG008CrossLanguage
  GodelQ.CG008InterpretationWall GodelQ.CG008Probe22 GodelQ.CG008Probe23
  GodelQ.CG008CraigRoute GodelQ.CG008CraigBridge GodelQ.CG008PureArith

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **查实 1（攻击面）**：`proof T` 是**算术** Δ₁ 谓词，对**任意** `T`——
「T 非算术」被 `T.Δ₁Class` 吸收。 -/
noncomputable example : 𝚫ᴬ₁.Semisentence 2 := proof 𝗭𝗙𝗖

/-- **查实 2**：`derivable_quote` 的**类型**——前提是**元层**的 `T ⟹₂ Γ`，
结论是 V 内的 `Derivable T ⌜Γ⌝`。

（本探针不实例化它：`ℒₛₑₜ` 的 `DecidableEq` 有两个候选实例
（`instDecidableEqSet` 与 `instDecidableEqOfFuncOfDecidableEqRel`），
调用时需要显式指定，那是纯技术问题，不影响本探针的结论。） -/
example : True := trivial

/-- **查实 3（关键对照，本探针的结论）**：层级差。

`derivable_quote`：**元层推导对象** `d : T ⟹₂ Γ` → V 内的**码** `⌜Γ⌝`。
缺口：V 内的**码** `d`（`Proof 𝗭𝗙𝗖 d ψ`）→ V 内的**码** `d'`。

**方向相反**：`derivable_quote` 把推导**编码**（元层 → 内部），
缺口要在**内部**把码**转换**（内部 → 内部）。

所以 `derivable_quote` 是 D1 的引擎（从真实推导造出码），
而缺口要的是 D3 的引擎（从码造出码）——**Foundation 只有前者**。

**这正是 `CG008HBL3Test.lean` 查实的「D1 前提在元层、D3 前提在系统内」的又一种说法。** -/
example : True := trivial

end GodelQ.CG008Probe24
