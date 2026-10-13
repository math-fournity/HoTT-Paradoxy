import GodelQ.ZFC.CG008SetTrans

/-!
# CG-008 · **更正**：公式集是**位编码**的，不是 ZF 集合——第四面墙不成立

## 我上一轮的结论错了

`CG008SetTrans.lean` 记：「取公式集的像要替换公理，而替换要 `[SetStructure V] [V↓[ℒₛₑₜ] ⊧* 𝗭𝗙]`，
缺口的 V 没有，所以 `iTSet` 取不出来」。**这个结论过强。**

## 机器查实（本轮）

`Derivable T s` 里的 `p ∈ s` **不是 ZF 的成员关系**，而是
**算术引导层自己的位编码成员关系**（`Exponential/Bit.lean:25`）：

```lean
def Bit (i a : V) : Prop := LenBit (Exp.exp i) a
instance : Membership V V := ⟨fun a i ↦ Bit i a⟩
```

它的可定义性是 **`𝚺ᴬ₀`**（`bit_defined`，`Bit.lean:31`）：
```lean
def bitDef : 𝚺ᴬ₀.Semisentence 2 := .mkSigma “x y. ∃ z <⁺ y, !expDef z x ∧ !lenbitDef z y”
```
——**只需要 `ORingStructure` + `𝗜𝚺₁`**，与 `ℒₛₑₜ` 的语义**无关**。

`IsFormulaSet`（`Proof/Basic.lean:23`）用的 `∈'`（`∀ p ∈' s, …`）
展开成 `ballIn`，其底层就是这个位编码。

## 所以

「取公式集的像」**不需要替换公理**——位编码是 V 自己的编码方案，
`iT` 是 V 内的 Σ₁ 函数，所以像可以在 V 内用**算术**手段构造
（如按位扫描/向量操作），**不碰 ZF 语义**。

**第四面墙不成立**；`CG008SetTrans.lean` 的那一节应降格为
「一个被证伪的猜想」。缺口的困难回到三面墙（解释墙、跨语言墙、语言墙）
加上「非标准情形」这一条。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008SetTrans2
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Z0Full GodelQ.Translate
variable {V : Type} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- **机器查实**：`Derivable` 里的成员关系是**位编码**，其可定义性是 `𝚺ᴬ₀`。

这条只需 `ORingStructure` + `𝗜𝚺₁`——**没有 `SetStructure`，没有 `⊧ 𝗭𝗙`**。
所以「取公式集的像要替换公理」是**错的**。 -/
example : 𝚺ᴬ₀-Relation (FFL.FirstOrder.Arithmetic.Bit : V → V → Prop) :=
  FFL.FirstOrder.Arithmetic.bit_defined.to_definable

end GodelQ.CG008SetTrans2
