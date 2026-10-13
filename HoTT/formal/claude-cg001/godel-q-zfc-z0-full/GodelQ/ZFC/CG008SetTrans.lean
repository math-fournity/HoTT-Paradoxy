import GodelQ.ZFC.CG008ITCommute

/-!
# CG-008 · 为什么「翻译公式集」这条路走不通（第四面墙）

## 想法

九支搬运（`CG008TransformShape`）里，`Derivable T s` 的 `s` 是一个**公式集**，
所以搬运似乎要先把 `s` 翻译成 `iTSet n s := {iT n p | p ∈ s}`。
本文件核对这个像**能不能在 V 内取出来**。

## 结论：不能，而且原因是结构性的

取替换像需要**替换公理模式**。Foundation 的版本：

```lean
lemma replacement_rel_existsUnique (X : V) (R : V → V → Prop)
    (h : ∀ x, ∃! y, R x y) (hR : ℒₛₑₜ-relation R) :
    ∃! Y : V, ∀ y : V, y ∈ Y ↔ ∃ x ∈ X, R x y
```

**它的上下文是 `[SetStructure V] [Nonempty V] [V↓[ℒₛₑₜ] ⊧* 𝗭𝗙]`**——
V 必须是 **ZFC 的模型**（`SetStructure` + ZF 语义）。

而缺口的 V 只有 **`[ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]`**——
**算术**模型，`ℒₛₑₜ` 的语义**根本不在上下文里**。
（`CG008Probe3.lean` 已机器化过：这里若强行要 `SetStructure V`，
`infer_instance` 会**静默合成到比特编码实例**，给出语义错误的引理。）

**所以 `iTSet` 取不出来**——不是「难」，是**类型上不成立**。

## 这解释了为什么缺口如此顽固

缺口的 V 是「V 内部有一个 𝗭𝗙𝗖 推导码」的 V，
**不是**「V 满足 ZF」的 V。这两者不同：
- `Provable 𝗭𝗙𝗖 d φ` 展开是 `Proof 𝗭𝗙𝗖 d φ`——一个**算术**谓词
  （`derivation 𝗭𝗙𝗖` 是 `Δ₁` 不动点，只需 `𝗭𝗙𝗖.Δ₁`）；
- 而 ZF 的语义（替换、分离、ω 的最小性）**不在**这个上下文里。

**这就是缺口的真正困难**：要证的是**算术谓词** `Provable 𝗭𝗙𝗖` 的性质，
但**唯一已知的证法**（把 𝗜𝚺₁ 的推导翻成 𝗭𝗙𝗖 的）需要 **ZF 的语义**，
而那个语义在 V 的假设里**不存在**。

## 与既有记录的关系

- `CG008InterpretationWall.lean`：「解释在元层有，系统内没有」；
- `CG008CrossLanguage.lean`：「`HBL3` 只在同语言时可陈述」；
- **本文件**：第三面——**取像要替换，而替换要 ZF 语义，缺口上下文没有**。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008SetTrans
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Z0Full GodelQ.Translate
variable {V : Type} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- 机器化的要点：`iT` 是 Σ₁ 函数——替换能用的前提在本上下文里成立。

所以障碍不在 `iT` 的可定义性，而在替换公理本身。 -/
example : 𝚺ᴬ₁-Function₂ (Translate.iT : V → V → V) := GodelQ.Translate.iT_definable

end GodelQ.CG008SetTrans
