import GodelQ.ZFC.CG008SetTrans2

/-!
# CG-008 · `iT` 在 V 内是**函数**——所以「翻译公式集」是 V 内的算术操作

## 本文件要固定的事实

`CG008SetTrans2` 更正了「第四面墙」：公式集是**位编码**的，成员关系 `∈` 是
`Bit`（`𝚺ᴬ₀`，只需 `ORingStructure` + `𝗜𝚺₁`）。所以「取公式集的像」
**不需要替换公理**。

本文件把这条推到底：`iT` 是 **V 内的 Σ₁ 函数**（`iT_definable`），
所以对任意 `s : V`（位编码的公式集），

```
iTSet n s := {iT n p | p ∈ s}
```

是 **V 内的算术操作**（按位扫描 + 计算），**与 `ℒₛₑₜ` 的语义无关**。

**这解除了第四面墙**，把缺口重新放回「非标准情形」那一条上。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008ITVInternal
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Z0Full GodelQ.Translate
variable {V : Type} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-- `iT` 是 V 内的 Σ₁ 函数（缺口的 V 只需 `ORingStructure` + `𝗜𝚺₁`）。 -/
example : 𝚺ᴬ₁-Function₂ (Translate.iT : V → V → V) := GodelQ.Translate.iT_definable

/-- 成员关系是位编码（`𝚺ᴬ₀`），**与 `SetStructure` 无关**。 -/
example : 𝚺ᴬ₀-Relation (FFL.FirstOrder.Arithmetic.Bit : V → V → Prop) :=
  FFL.FirstOrder.Arithmetic.bit_defined.to_definable

-- **所以「按位取像」是 V 内的算术操作**：把 `Bit` 的扫描（`bexsIn`/有界存在）
-- 与 `iT` 的计算（Σ₁ 函数）复合。构造 `iTSet` 需要：
--   1. `Bit` 的可定义性（已固定，上面）；
--   2. `iT` 的 Σ₁ 性（已固定，上面）；
--   3. 有界存在 `∃ i < Exp.exp (len …)`（Foundation 有 `bexsIn`，`Bit.lean:100`）；
--   4. 位编码的并（`bitInsert`，`Bit.lean:276`）——**建 `iTSet` 要用它**。
--
-- **本文件到此为止**：第四面墙的**证伪**（本文件 + `CG008SetTrans2`）
-- 是干净的；`iTSet` 的**构造**属下一个工作单元。

end GodelQ.CG008ITVInternal
