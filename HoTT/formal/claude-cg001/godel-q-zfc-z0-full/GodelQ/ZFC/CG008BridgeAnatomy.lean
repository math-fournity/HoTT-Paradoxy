import GodelQ.ZFC.CG008SingleD3Attack

/-!
# CG-008 · 那条内部桥的解剖：为什么所有路线都回到它

## 所有路线都归约到同一条桥

| 路线 | 归约到 |
|---|---|
| 整族 `HBL3`（`CG008HBL3`） | `∀ σ, zfcTr.FormalizedCompleteOn (zfcTr σ)` |
| 单句 `D3`（`CG008SingleD3`） | `𝗜𝚺₁ ⊢ zfcTr 𝐆 🡒 zfcTr (zfcTr 𝐆)` |
| 单句的**攻击**（`CG008SingleD3Attack`） | **内部桥** `𝗜𝚺₁ ⊢ provabilityPred 𝗜𝚺₁ ψ 🡒 zfcTr ψ` |
| `Z0Bridge` 的 `bridge` | 同一条内部桥 |

**同一条桥**：**在 𝗜𝚺₁ 内部**，把「`𝗜𝚺₁` 证明了 ψ」变成「`𝗭𝗙𝗖` 证明了 `translate ψ`」。

## 为什么现有的 `paInterp` 给不出它

`paInterp : 𝗭𝗙𝗖 ⊳ 𝗣𝗔`（`PAModel.lean:246`）的构造：

```lean
interpret_theory φ hφ := by
  apply SetTheory.complete.{0}
  intro M _ _ _
  exact DirectTranslation.Model.translate_iff.mpr
    (models_theory_iff.mp (models_PA (M := M)) φ hφ)
```

**它走 `SetTheory.complete`——完备性定理，语义论证。**
所以它给出的是**元层**的 `𝗭𝗙𝗖 ⊢ translate φ`，
**不产生 V 内部的证明编码**。

这与 `of_provability`（`LK/Interpretation.lean:443`）是同一件事，
`CG008InterpretationWall.lean` 已记录。

## 桥的精确内容

```
要证：𝗜𝚺₁ ⊢ provabilityPred 𝗜𝚺₁ ψ 🡒 zfcTr ψ
```

展开两边：
- 左：`∃ d : V, Proof 𝗜𝚺₁ d ⌜ψ⌝`（V 内有一条 𝗜𝚺₁ 的推导）；
- 右：`∃ d' : V, Proof 𝗭𝗙𝗖 d' ⌜translate ψ⌝`（V 内有一条 𝗭𝗙𝗖 的推导）。

**要做的**：**在 V 内**把 `d`（一条 𝗜𝚺₁ 推导的码）
变成一个 `d'`（同一条推理在 𝗭𝗙𝗖 里的推导的码）。

**这是「证明翻译」——把一个推导的编码系统地重写成另一个。**
数学上，`paInterp` 的语义内容足以保证**存在性**（元层），
但**在 V 内构造出 `d'`** 需要把 `interpret_theory` 的每一步
（现在是语义的）改成**语法可计算**的。

## 这与 P1 的障碍是同一件事的两种说法

- P1（`CG008MemCase.lean`）：`ℒₛₑₜ` 无常项，`toNumVec` 无对偶；
- 本文件：`paInterp` 的 `interpret_theory` 走完备性，无语法版。

**两者都指向**：**需要一个语法可计算的证明翻译**（从 𝗜𝚺₁ 的推导到 𝗭𝗙𝗖 的推导），
而这个东西 Foundation 里没有——**不在算术侧，也不在集合侧**。

## 治理

- Foundation 只读；本文件纯下游。
- 本文件不含任何未证标记，可进入收据。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008BridgeAnatomy

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full GodelQ.CG008HBL3
  GodelQ.CG008HBL3Test GodelQ.CG008Final GodelQ.CG008Probe15 GodelQ.CG008Probe16
  GodelQ.CG008Probe17 GodelQ.CG008Probe18 GodelQ.CG008Probe19 GodelQ.CG008Probe20
  GodelQ.CG008Delta1Wall GodelQ.CG008Probe21 GodelQ.CG008CrossLanguage
  GodelQ.CG008InterpretationWall GodelQ.CG008Probe22 GodelQ.CG008Probe23
  GodelQ.CG008CraigRoute GodelQ.CG008CraigBridge GodelQ.CG008PureArith
  GodelQ.CG008Probe24 GodelQ.CG008Probe25 GodelQ.CG008Correction
  GodelQ.CG008Rosser GodelQ.CG008InternalInduction GodelQ.CG008SingleD3
  GodelQ.CG008SingleD3Attack

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **查实 1**：`paInterp` 是 `𝗭𝗙𝗖 ⊳ 𝗣𝗔`——一个**直接解释**。 -/
noncomputable example : 𝗭𝗙𝗖 ⊳ 𝗣𝗔 := paInterp

/-- **查实 2**：`paInterp.of_provability` 给的是**元层**结论——
`𝗣𝗔 ⊢ φ → 𝗭𝗙𝗖 ⊢ translate φ`。**不产生 V 内部的编码。** -/
example {φ : ArithmeticSentence} (h : 𝗣𝗔 ⊢ φ) : 𝗭𝗙𝗖 ⊢ arithTrln.translate φ :=
  paInterp.of_provability h

/-- **查实 3（桥的精确内容）**：`Proof` 的两边——左是 𝗜𝚺₁ 的推导，右是 𝗭𝗙𝗖 的推导。

**桥要做的**：在 V 内把左边那个 `d` 变成右边那个 `d'`。
这是**语法可计算的证明翻译**，而 `paInterp` 的 `interpret_theory` 是**语义的**。 -/
example (ψ : ArithmeticSentence) : Prop :=
  (∃ d : V, Proof 𝗜𝚺₁ d (⌜ψ⌝ : V)) → (∃ d' : V, Proof 𝗭𝗙𝗖 d' (⌜arithTrln.translate ψ⌝ : V))

end GodelQ.CG008BridgeAnatomy
