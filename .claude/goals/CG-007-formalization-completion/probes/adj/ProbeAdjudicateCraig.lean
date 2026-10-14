import GodelQ.ZFC.ShCraigElimSetup

/-!
裁决探针（**不是收据**）：`Sh.craig` 的 Δ₁Class 成员，V 层特征式到底是哪个 `reWitness`。

对比两端：
  A（004-Step 的说法）：`Theory.IsCraigAxiom (T := Sh)` 成立，`(IsCraigAxiom.defined (T := Sh)).iff`
     是现成定理，`Δ₁Class` 就是 `{ φ | V ⊧/![φ] T.Δ₁ch.val }`，所以成员就是 `Sh.IsCraigAxiom`。
  B（我 2026-10-13 的说法）：成员 = `Theory.IsCraigAxiom (T := Sh.craig)`，reWitness 是 `(Sh.craig).reWitness`。

关键在 `Δ₁ch`：`Sh.craig` 的 Δ₁ 实例来自 Foundation `CraigTrick.lean:311`，
   `ch := T.craigCh` 且 `T := Sh`，
而 `craigCh`（`CraigTrick.lean:210`）的 body 写的是 `!(T.reWitness.val) s p`，即 `Sh.reWitness`。

所以 A 与 B 如果都对，则 `Sh.IsCraigAxiom = (Sh.craig).IsCraigAxiom`，即两个 reWitness 描述的集合相同。
本探针逐条核。
-/
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup

namespace GodelQ.ProbeAdjudicateCraig

variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- (1) 两者的定义性展开：`(Sh.craig).IsCraigAxiom p` 与 `Sh.IsCraigAxiom p`
example (p : V) :
    Theory.IsCraigAxiom (V := V) (T := Sh.craig) p =
      (∃ s p' : V, p = p' ^⋏ qqVerums s ∧ (Semiformula.Evalb ![s, p']) ↑(Sh.craig).reWitness.val) := by
  rfl

example (p : V) :
    Theory.IsCraigAxiom (V := V) (T := Sh) p =
      (∃ s p' : V, p = p' ^⋏ qqVerums s ∧ (Semiformula.Evalb ![s, p']) ↑Sh.reWitness.val) := by
  rfl

-- (2) Δ₁Class 的定义（`Theory.Δ₁Class`）
example (p : V) : (p ∈ (Sh.craig).Δ₁Class) = (V ⊧/![p] (Sh.craig).Δ₁ch.val) := by
  rfl

-- (3) 关键：`Sh.craig` 的 Δ₁ch 是 `Sh.craigCh`，而 craigCh 的 body 引用 `Sh.reWitness`
example : (Sh.craig).Δ₁ch = Sh.craigCh := rfl

-- (4) Foundation 的现成定理：两者可互化
example (p : V) (h : p ∈ (Sh.craig).Δ₁Class) : Theory.IsCraigAxiom (V := V) Sh p :=
  ((Theory.IsCraigAxiom.defined (V := V) (T := Sh)).iff).mp h

example (p : V) (h : Theory.IsCraigAxiom (V := V) Sh p) : p ∈ (Sh.craig).Δ₁Class :=
  ((Theory.IsCraigAxiom.defined (V := V) (T := Sh)).iff).mpr h

end GodelQ.ProbeAdjudicateCraig
