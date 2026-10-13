import GodelQ.ZFC.CG008GapSharp

/-!
# CG-008 · 窄命题为什么仍不是免费的：循环性检查（机器化）

## 窄命题

```
narrow : ∀ σ, ℒₒᵣ 的 Σ₁ 句 σ → Provable 𝗜𝚺₁ (⌜σ⌝ : V) → Provable 𝗭𝗙𝗖 (⌜translate σ⌝ : V)
```

## 本轮要机器化的两点

**要点 A（形式化的方向）**：`narrow` 的**结论**是 V 内部的
`Provable 𝗭𝗙𝗖 ⌜translate σ⌝`。展开后是一个存在量化：V 内有一个元素 `d`
使 `Proof 𝗭𝗙𝗖 d ⌜translate σ⌝`。**`d` 必须是 V 内的具体项**。

**要点 B（为什么现有工具给不出 `d`）**：
- `internalize_provability`（`D1.lean:27`）的前提是**元层**的 `T ⊢ φ`；
  `narrow` 的前提是 **V 内部**的 `Provable 𝗜𝚺₁ ⌜σ⌝`（一个 V 内元素 `d'`）。
  **两者层不同**，不能互推。
- `paInterp.interpret_theory`（`PAModel.lean:246`）也是**元层**的：
  对每个 `φ ∈ 𝗜𝚺₁` 给一个元层证明对象，走 `SetTheory.complete`。
- 若把 `narrow` 用在 `σ := zfcTr τ`（这正是 `CG008GapSharp` 的用法），
  它的前提 `Provable 𝗜𝚺₁ ⌜zfcTr τ⌝` 说的是「V 内有一条 𝗜𝚺₁ 推导，
  结论是 `zfcTr τ`」——而 `zfcTr τ` 本身的**内容**就是
  「V 内有一条 𝗭𝗙𝗖 推导，结论是 `translate τ`」。
  **所以 `narrow` 在这一点上要求 V 把「自己内部有一条 𝗜𝚺₁ 推导」
  变成「自己内部有一条 𝗭𝗙𝗖 推导」**——这是一次**反射**，
  其一般形式（对所有 σ）**蕴含** 𝗜𝚺₁ 的 Σ₁ 可靠性，
  而后者在 𝗜𝚺₁ 内**不可证**（否则 𝗜𝚺₁ ⊢ Con(𝗜𝚺₁)，与 G2 矛盾）。

**结论**：`narrow` **不能**作为一个「更弱的、可以单独攻下的」目标——
它与缺口同强。本文件把这一点固定成一条**精确的蕴含**（不是证明）。

## 治理

- Foundation 只读；本文件纯下游。
- 本文件不含任何未证标记，可进入收据。
- **本文件记录的是循环性分析，不是窄命题的证明。**
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008Circularity
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Z0Full GodelQ.Translate
variable {V : Type} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **窄命题的形状**（本文件的分析对象）。 -/
def Narrow : Prop :=
  ∀ {σ : ArithmeticSentence}, ℬ[<, ℒₒᵣ].Hierarchy 𝚺 1 σ →
    Provable 𝗜𝚺₁ (⌜σ⌝ : V) → Provable 𝗭𝗙𝗖 (⌜arithTrln.translate σ⌝ : V)

/-- **要点 A 的形式化**：窄命题的结论就是 `zfcTr` 在 V 内成立。

这不是新定理——是 `models_zfcTr_iff` 的直接读法，
但把它写出来能看清「结论里有一个 V 内的见证 `d`」。 -/
theorem narrow_conclusion_is_zfcTr {σ : ArithmeticSentence}
    (h : Provable 𝗭𝗙𝗖 (⌜arithTrln.translate σ⌝ : V)) :
    V↓[ℒₒᵣ] ⊧ zfcTr σ :=
  (models_zfcTr_iff V σ).mpr h

/-- **要点 B 的形式化（关键）**：窄命题对 `σ := zfcTr τ` 的实例，
其前提恰好是 `d3_hypothesis_gives_ISigma1_proof` 的**结论**，
而其后件正是缺口对 `τ` 的结论。

**所以窄命题 ⟹ 缺口**（`CG008GapSharp` 已证），
且**反过来**：若缺口成立，则对任意满足前提的 σ，
`Provable 𝗜𝚺₁ ⌜σ⌝` 不能（在 𝗜𝚺₁ 内）推出 `V ⊨ zfcTr σ`
——否则缺口本身就不需要 `hD3G` 了。

下面把「窄命题 ⟹ 缺口」**原样**再固定一次，
以标明本文件与 `CG008GapSharp` 用的是同一条归约。 -/
theorem gap_of_narrow (h : Narrow (V := V)) :
    ∀ (τ : ArithmeticSentence),
      Provable 𝗭𝗙𝗖 (⌜arithTrln.translate τ⌝ : V) →
      Provable 𝗭𝗙𝗖 (⌜arithTrln.translate (zfcTr τ)⌝ : V) :=
  GodelQ.CG008GapSharp.gap_of_internalized_interpretation (V := V) h

/-- **循环性的精确陈述**：把 `narrow` 用在 `σ := zfcTr τ` 上，
它要求的是「V 内一条 𝗜𝚺₁ 推导 ⟹ V 内一条 𝗭𝗙𝗖 推导」。

**注意**：这条**不是**新定理，而是 `Narrow` 的定义在该点的展开——
本文件用 `rfl` 级别的重述来标明：窄命题的**每一处**应用都是这个形状，
所以「先把窄命题证出来」并不比重述缺口容易。 -/
theorem narrow_at_zfcTr (h : Narrow (V := V)) (τ : ArithmeticSentence)
    (hσ : ℬ[<, ℒₒᵣ].Hierarchy 𝚺 1 (zfcTr τ))
    (hI : Provable 𝗜𝚺₁ (⌜zfcTr τ⌝ : V)) :
    Provable 𝗭𝗙𝗖 (⌜arithTrln.translate (zfcTr τ)⌝ : V) :=
  h hσ hI

end GodelQ.CG008Circularity

#print axioms GodelQ.CG008Circularity.gap_of_narrow
#print axioms GodelQ.CG008Circularity.narrow_at_zfcTr
