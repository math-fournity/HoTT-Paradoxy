import GodelQ.ZFC.ShCraigElimSetupQ
/-! ## `ExsBridge` 展开：它在数学上是什么（2026-10-13）

`ExsBridge` 要证（对任意 `p` 层 1、`t` 项、`T'` 项）：

```
Provable 𝗭𝗙𝗖 ( neg (iT 0 (substs1 ℒᵣ t p))
                ⋎ substs1 ℒₛₑₜ T' (domZero ⋏ iT 1 p) )
```

即「`iT 0 (p[t]) → (t' ∈ ω ∧ iT 1 p)`」在 𝗭𝗙𝗖 中可证。

`replace_of_imp` 只要求这条**蕴含**可证（不需要等式），
这是它与被 §2.7 判死的「等式路线」的根本区别。

本探针把两侧的**原子情形**（`p = ^rel 2 cEqN ?[v0,v1]`）展开到能算的粒度，
看 `iT 0 (substs1 t p)` 与 `substs1 T' (domZero ⋏ iT 1 p)` 差在哪里。 -/
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000

namespace GodelQ.ProbeExsB
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

namespace GodelQ.ProbeBridgeShape

-- 形状核对：`iT_exs` 给的实例公式（`T'` 要代进去的那个）
#check @GodelQ.Translate.iT_exs
#check @Bootstrapping.substs_and
#check @Bootstrapping.substs_verum

-- `substs1 T' (domZero ⋏ X) = substs1 T' domZero ⋏ substs1 T' X`
example {X T' : V} (hd : IsUFormula ℒₛₑₜ (domZero (V := V)))
    (hX : IsUFormula ℒₛₑₜ X) :
    substs1 ℒₛₑₜ T' ((domZero (V := V)) ^⋏ X)
      = substs1 ℒₛₑₜ T' (domZero (V := V)) ^⋏ substs1 ℒₛₑₜ T' X := by
  simp only [substs1, Bootstrapping.substs_and hd hX]

end GodelQ.ProbeBridgeShape