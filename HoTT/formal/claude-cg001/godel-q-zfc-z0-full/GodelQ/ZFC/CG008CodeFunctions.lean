import GodelQ.ZFC.CG008D3AtG

/-!
# CG-008 · 关键发现：Foundation **有** V 内部的「码到码」函数与 Σ₁ 归纳

## 此前几轮的误判

`CG008BridgeAnatomy.lean` 说：「需要一个语法可计算的证明翻译——
而 Foundation 里没有——**算术侧没有，集合侧也没有**」。

**前半对，后半错。** 算术侧**有**：

| 文件 | 内容 |
|---|---|
| `Syntax/Formula/Functions.lean` | `shift`、`neg`、`subst`、`substs`、`bv`、`fomulaComplexity`——**全是 V 内部的「码到码」函数** |
| 同上:488 | `isUFormula_subst_ISigma1.sigma1_succ_induction`——**Σ₁ 归纳**（V 内部） |
| 同上:523 | `semiformula_subst_induction`——四元关系的归纳 |
| `Syntax/Term/Basic.lean` | `termBShift`、`termSubst` 等同类 |

**这些正是「语法可计算的码变换」。** 所以缺口的那个「证明翻译」在算术侧
**有可用的零件**——不是从零发明。

## 本探针要查实

1. 这些函数对**任意语言 `L`**（含 `ℒₛₑₜ`）定义（看 section 变量）；
2. 它们是 **V 内部**的（吃 `V`、吐 `V`，不是元层的语法）；
3. 缺口缺的到底是什么——**证明**的翻译（不是公式的翻译）。

**第 3 条是关键**：`subst`/`shift` 翻译的是**公式**；
缺口要的是把「一条 𝗜𝚺₁ 推导的码」变成「一条 𝗭𝗙𝗖 推导的码」——
**翻译的是推导**，而 Foundation 的 `derivation` 是 `Fixpoint`（不动点），
**没有对应的「推导变换函数」**。

**所以缺口的精确内容**：需要一个**推导层面的**码变换，
而 Foundation 只提供**公式层面**的。

## 治理

- Foundation 只读；本文件纯下游。
- 本文件不含任何未证标记，可进入收据。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008CodeFunctions

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full GodelQ.CG008HBL3
  GodelQ.CG008HBL3Test GodelQ.CG008Final GodelQ.CG008Probe15 GodelQ.CG008Probe16
  GodelQ.CG008Probe17 GodelQ.CG008Probe18 GodelQ.CG008Probe19 GodelQ.CG008Probe20
  GodelQ.CG008Delta1Wall GodelQ.CG008Probe21 GodelQ.CG008CrossLanguage
  GodelQ.CG008InterpretationWall GodelQ.CG008Probe22 GodelQ.CG008Probe23
  GodelQ.CG008CraigRoute GodelQ.CG008CraigBridge GodelQ.CG008PureArith
  GodelQ.CG008Probe24 GodelQ.CG008Probe25 GodelQ.CG008Correction
  GodelQ.CG008Rosser GodelQ.CG008InternalInduction GodelQ.CG008SingleD3
  GodelQ.CG008SingleD3Attack GodelQ.CG008BridgeAnatomy GodelQ.CG008SingleD3Theorem
  GodelQ.CG008ConRedo GodelQ.CG008MonoExt GodelQ.CG008RedoPrereq GodelQ.CG008RedoActual
  GodelQ.CG008AbstractRedo GodelQ.CG008Instantiate GodelQ.CG008Z0FromSingleD3
  GodelQ.CG008D3AtG

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **查实 1**：`subst` 是 **V 内部**的「码到码」函数——吃 `V` 吐 `V`。

对**任意** `L`（`[L.Encodable] [L.LORDefinable]`），所以 `ℒₛₑₜ` 也有。 -/
noncomputable example (n p : V) : V := Bootstrapping.subst ℒₛₑₜ n p

/-- **查实 2**：`shift`、`neg` 同类。 -/
noncomputable example (p : V) : V := Bootstrapping.shift ℒₛₑₜ p

noncomputable example (p : V) : V := Bootstrapping.neg ℒₛₑₜ p

/-- **查实 3**：`bv`（有界变量数）——**推导合法性判定要用到的量**。 -/
noncomputable example (p : V) : V := Bootstrapping.bv ℒₛₑₜ p

/-- **查实 4（缺口真正的形状）**：`derivation T` 是 `Fixpoint`（不动点），
而 Foundation 提供的是**公式层**的码变换。

**缺口要的是「推导层」的码变换**——即：给定 `d : V` 与 `Derivation 𝗜𝚺₁ d`，
造出 `d' : V` 使 `Derivation 𝗭𝗙𝗖 d'` 且 `d'` 的结论是 `d` 的结论的翻译。

**这不是 `subst`/`shift` 能直接给的**——它们变换公式，不变换推导。

**本探针把这一点固定下来**：缺口的精确内容是**推导变换函数**，
而它需要在 `Fixpoint` 层做（`derivation` 是不动点，
其归纳 `Fixpoint.induction` 是元层的）。 -/
example (d : V) : Prop :=
  Derivation 𝗜𝚺₁ d → ∃ d' : V, Derivation 𝗭𝗙𝗖 d'

end GodelQ.CG008CodeFunctions
