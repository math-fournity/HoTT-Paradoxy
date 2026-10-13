import GodelQ.ZFC.ShCraigElimSetupQ
/-! ## `RootBlockerQ` 是否也有「丢 `Derivation`」缺陷？（2026-10-13）

`AllBlockerQ`/`ExsBlockerQ` 已证过强并修复（补回 `Derivation Sh.craig dd`）。
`RootBlockerQ` 是**不同形状**：它没有子推导 `dd`——

```
RootBlockerQ : ∀ {s p}, IsFormulaSet s → p ∈ s → p ∈ Sh.craig.Δ₁Class → Q (axm s p)
```

所以「丢 `hd.2`」的机制**不适用**（`axm` 支在 `induction1` 里也没有子推导）。
但值得核验另一件事：`p ∈ Sh.craig.Δ₁Class` 是否**被用到**——
若某条路根本不用它，那它就是过弱（这里反而是好事），
若它必须用，则 `RootBlockerQ` 就是 D3 本身，形状正确。

本探针只做形状核对，不声称结论。 -/
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000

namespace GodelQ.ProbeExsB
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

namespace ProbeRootCheck

-- `RootBlockerQ` 的签名
#check @GodelQ.ShCraigElimSetupQ.RootBlockerQ
#check @GodelQ.ShCraigElimSetupQ.RootBlocker

-- 对照：`axm` 构造子要求 `p ∈ T.Δ₁Class`（这是 RootBlockerQ 第三条假设的用途）
#check @Bootstrapping.Derivation.axm

-- `axm` 支在 `induction1` 里没有子推导 ⇒ 不存在「丢 hd.2」问题
example (s p : V) (hs : IsFormulaSet (L := ℒₒᵣ) s) (hps : p ∈ s)
    (hpT : p ∈ (Theory.craig Sh).Δ₁Class) :
    Derivation (V := V) (L := ℒₒᵣ) (Theory.craig Sh) (axm s p) :=
  Derivation.axm hs hps hpT

end ProbeRootCheck