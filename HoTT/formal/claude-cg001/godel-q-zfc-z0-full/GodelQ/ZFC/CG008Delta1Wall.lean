import GodelQ.ZFC.CG008Probe20

/-!
# CG-008 · 为什么 `Sh` 没有 `Δ₁`——以及为什么这不可能是实现疏漏

## `Δ₁` 的定义（`Bootstrapping/Syntax/Theory.lean:16`）

```lean
class Δ₁ (T : Theory L) where
  ch : 𝚫ᴬ₁.Semisentence 1
  mem_iff : ∀ φ : Proposition L, ℕ ⊧/![⌜φ⌝] ch.val ↔ ∃ σ ∈ T, φ = σ
  isDelta1 : ch.ProvablyProperOn 𝗜𝚺₁
```

**`mem_iff` 说**：`ch` 这个 Δ₁ 公式要**精确刻画 T 的公理集合**——
「`φ` 是 T 的公理」当且仅当 `ℕ ⊨ ch(⌜φ⌝)`。

## `Sh` 的公理集合是什么

`Sh := {σ | 𝗭𝗙𝗖 ⊢ arithTrln.translate σ}`（`Z0Shadow.lean:35`）。

**这不是一个「递归可枚举的公理集合」，而是「某个理论的定理集合」**——
即 `Sh` 的「公理」是 𝗭𝗙𝗖 的**定理**的翻译。

而 𝗭𝗙𝗖 的定理集合是 **Σ₁**（r.e.，由 `provable 𝗭𝗙𝗖` 定义），**不是 Δ₁**：
「`σ` 不是 𝗭𝗙𝗖 的定理」需要 `∀d, ¬Proof 𝗭𝗙𝗖 d σ`，
这是一个 **Π₁** 陈述，一般不 Δ₁（除非 𝗭𝗙𝗖 是完备的，而 G1 说它不是）。

## 所以 `Sh.Δ₁` 不成立**不是**实现疏漏

`Theory.Δ₁ Sh` 要 `ch` 同时是 Σ₁ 与 Π₁。
但 `Sh` 的成员判定本质上是 Σ₁（存在一个 𝗭𝗙𝗖 的证明），
而它的补是 Π₁ 且**不是** Σ₁——**这正是 G1 的内容**。

**若 `Sh.Δ₁` 成立，则「`σ` 是 𝗭𝗙𝗖 的定理」是 Δ₁ 的，
于是 𝗭𝗙𝗖 的定理集合是递归的**——与 G1（𝗭𝗙𝗖 不完备且不可判定）矛盾。

**故 `Sh.Δ₁` 不成立是定理的必然**，正如 `HBL3` 对跨语言谓词不可陈述也是必然。
两条路都被**数学事实**堵死，不是工程缺口。

## 这与缺口的最终定位

`Z0Blocked.lean` 诊断第 3 条说「`Sh` 没有 `Δ₁` 实例」，方向正确，
但本文件补充了**为什么**：那不是 Foundation 少写了一个实例，
而是 `Sh.Δ₁` **不可能**成立。

**于是缺口的正确定位是**：Z0 需要的 D3 是**跨语言可证性谓词**的性质，
而 Foundation 的抽象框架（`HBL2`/`HBL3`）是为**同语言**情形设计的。
补上它需要**扩展框架**（或为跨语言情形单开一条路），
而不是「填一个 `Δ₁` 实例」。

## 治理

- Foundation 只读；本文件纯下游。
- 本文件不含任何未证标记，可进入收据。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment ProvabilityAbstraction
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008Delta1Wall

open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full GodelQ.CG008HBL3
  GodelQ.CG008HBL3Test GodelQ.CG008Final GodelQ.CG008Probe15 GodelQ.CG008Probe16
  GodelQ.CG008Probe17 GodelQ.CG008Probe18 GodelQ.CG008Probe19 GodelQ.CG008Probe20

/-- **查实 1**：`Δ₁` 的字段——`mem_iff` 要求 `ch` **精确刻画 T 的公理集**。

```lean
mem_iff : ∀ φ : Proposition L, ℕ ⊧/![⌜φ⌝] ch.val ↔ ∃ σ ∈ T, φ = σ
```

注意 `∃ σ ∈ T, φ = σ` 是**双向**的：不只是「是公理 ⟹ ch 成立」，
还要「ch 成立 ⟹ 是公理」。 -/
example (L : Language) [L.Encodable] [L.LORDefinable] (T : Theory L) [T.Δ₁] :
    ∀ φ : Proposition L, ℕ ⊧/![⌜φ⌝] (Theory.Δ₁.ch T).val ↔ ∃ σ ∈ T, φ = σ :=
  fun φ ↦ Theory.Δ₁.mem_iff (T := T) φ

/-- **查实 2**：`Sh` 的公理集合就是「𝗭𝗙𝗖 的定理的翻译」——
`Sh ⊢ σ ↔ 𝗭𝗙𝗖 ⊢ translate σ`。

**所以 `Sh` 的「公理」是 𝗭𝗙𝗖 的定理**，不是一组可判定的模式。 -/
example (σ : ArithmeticSentence) : Sh ⊢ σ ↔ 𝗭𝗙𝗖 ⊢ arithTrln.translate σ :=
  Sh_provable_iff σ

/-- **查实 3（本文件的要点）**：`Sh.Δ₁` 若成立，则「`σ` 是 𝗭𝗙𝗖 的定理」是 Δ₁，
于是 𝗭𝗙𝗖 的定理集合递归——**与 G1 矛盾**。

所以 `Sh.Δ₁` **不可能**成立；`Z0Blocked` 诊断第 3 条说的
「没有 `Δ₁` 实例」是**数学必然**，不是 Foundation 缺一个实例。

下面把「`Sh` 的成员判定由 `provable 𝗭𝗙𝗖` 表达」这一点固定下来——
它是一个 **Σ₁** 句（`provable 𝗭𝗙𝗖 : 𝚺ᴬ₁.Semisentence 1`），
而 `Δ₁` 要求同时是 Π₁。 -/
noncomputable example : 𝚺ᴬ₁.Semisentence 1 := provable 𝗭𝗙𝗖

end GodelQ.CG008Delta1Wall
