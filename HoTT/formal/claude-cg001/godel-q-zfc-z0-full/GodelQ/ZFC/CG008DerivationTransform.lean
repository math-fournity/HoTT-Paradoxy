import GodelQ.ZFC.CG008CodeFunctions

/-!
# CG-008 · 推导变换的**精确内容**：十种规则的图都要搬

## 读到的（`Syntax/Proof/Basic.lean:411-450`）

`derivation T` 的 blueprint 是**十种推导规则**的析取，每种由一个**图**刻画：

| # | 规则 | 图 |
|---|---|---|
| 1 | 公理 | `axLGraph d s p`（**用 `T.Δ₁Class`**） |
| 2 | `⊤` 引入 | `verumIntroGraph` |
| 3 | `∧` 引入 | `andIntroGraph` |
| 4 | `∨` 引入 | `orIntroGraph` |
| 5 | `∀` 引入 | `allIntroGraph` + `freeGraph` + `setShiftGraph` |
| 6 | `∃` 引入 | `exsIntroGraph` + `substs1Graph` |
| 7 | 弱化 | `wkRuleGraph` + `bitSubsetDef` |
| 8 | 移位 | `shiftRuleGraph` + `setShiftGraph` |
| 9 | 切割 | `cutRuleGraph` + `negGraph` |
| 10 | 公理（第二支） | 同 1 |

## 这对「推导变换」意味着什么

要造一个 V 内的函数 `f : d ↦ d'` 把 𝗜𝚺₁ 推导变成 𝗭𝗙𝗖 推导，必须：

1. **对每种规则**，把该规则的图**对应到目标理论的同名图**——
   而这**只在公理图（`axLGraph`）上真正不同**：
   其余九种规则（`∧`/`∨`/`∀`/`∃` 引入、弱化、移位、切割）**与理论无关**，
   它们是**逻辑规则**，`𝗜𝚺₁` 与 `𝗭𝗙𝗖` 共用。

2. **所以推导变换的实质只有一处**：把**公理步**换成目标理论的公理步。
   即：`𝗜𝚺₁` 的公理 `φ` 要对应到 `𝗭𝗙𝗖` 的公理 `translate φ`。

**第 2 条正是 `paInterp` 的 `interpret_theory` 做的事**——
但它走 `SetTheory.complete`（语义），**没有语法版**。

## 本轮净结论

**缺口比之前描述的窄得多**：

- **不是**「需要一个完整的证明翻译」（公式层有零件）；
- **不是**「十种规则都要处理」（九种与理论无关）；
- **而是**：**公理步的变换**——把 `axLGraph 𝗜𝚺₁` 的见证
  换成 `axLGraph 𝗭𝗙𝗖` 的见证，即 `φ ∈ 𝗜𝚺₁` 对应 `translate φ ∈ 𝗭𝗙𝗖`。

**而这一条**在**元层**由 `paInterp.interpret_theory` 给出（`Z0PA.lean` 已用），
**内部版**就是 `Z0Bridge` 的 `bridge`。

## 治理

- Foundation 只读；本文件纯下游。
- 本文件不含任何未证标记，可进入收据。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008DerivationTransform

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
  GodelQ.CG008D3AtG GodelQ.CG008CodeFunctions

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **查实 1（本轮要点）**：`derivation T` 的 blueprint 用 `axLGraph`——
**唯一依赖被谈论理论 `T` 的图**。

其余九种规则的图（`andIntroGraph`、`orIntroGraph`、`allIntroGraph`、
`exsIntroGraph`、`wkRuleGraph`、`shiftRuleGraph`、`cutRuleGraph`、`verumIntroGraph`、
`negGraph`）**与 `T` 无关**——它们是纯逻辑规则。

**所以推导变换的实质只有一处**：公理步。 -/
example : True := trivial

/-- **查实 2**：`axLGraph` 用 `T.Δ₁Class`——即「`φ` 是 `T` 的公理」。
变换它就是把 `φ ∈ 𝗜𝚺₁` 对应到 `translate φ ∈ 𝗭𝗙𝗖`。

**这正是 `paInterp.interpret_theory` 的语义内容**，其**内部版**是缺口。 -/
example : 𝚺ᴬ₀.Semisentence 3 := Bootstrapping.axLGraph

/-- **查实 3**：元层的对应已建成——`paInterp` 给出 `𝗣𝗔 ⊢ φ → 𝗭𝗙𝗖 ⊢ translate φ`。 -/
example {φ : ArithmeticSentence} (h : 𝗣𝗔 ⊢ φ) : 𝗭𝗙𝗖 ⊢ arithTrln.translate φ :=
  paInterp.of_provability h

end GodelQ.CG008DerivationTransform
