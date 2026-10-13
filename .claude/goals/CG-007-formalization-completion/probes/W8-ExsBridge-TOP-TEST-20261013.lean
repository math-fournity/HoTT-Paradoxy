import GodelQ.ZFC.ShCraigElimSetupQ
/-! ## `ExsBridge` 的 `p = ⊤` 测试（2026-10-13）

按 [[cg007-blocker-defs-too-strong]] 的纪律，对每条新义务先做退化测试。
`ExsBridge` 要 `Provable 𝗭𝗙𝗖 (neg (iT 0 (substs1 t p)) ⋎ substs1 T' (domZero ⋏ iT 1 p))`。

取 `p = ⊤`：`substs1 t ⊤ = ⊤`、`iT 0 ⊤ = ⊤`、`iT 1 ⊤ = ⊤`，于是义务退化成

```
Provable 𝗭𝗙𝗖 (neg ⊤ ⋎ substs1 T' (domZero ⋏ ⊤))
```

`neg ⊤ = ⊥`，而 `⊥ ⋎ X = X`（`imp` 的展开），故等价于
`Provable 𝗭𝗙𝗖 (substs1 T' (domZero ⋏ ⊤))`。

**这与 blocker 那次不同**：它不是「假设无条件成立」，而是**结论变成一个具体的可证性**
——`T' ∈ ω ∧ ⊤` 的翻译可证。这个未必为假（若 `T'` 是具体数字闭项，它就真）。

本探针把退化后的形状算清楚，供判断 `ExsBridge` 是否合理。 -/
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000

namespace GodelQ.ProbeExsB
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

namespace GodelQ.ProbeBridgeTop

-- `p = ⊤` 时 `substs1 t ⊤ = ⊤`（ℒₒᵣ 侧）
example (t : V) : substs1 ℒₒᵣ t (^⊤ : V) = ^⊤ := by
  simp [substs1, Bootstrapping.substs_verum]

-- `iT 0 ⊤ = ⊤`、`iT 1 ⊤ = ⊤`
example : iT (0:V) (^⊤ : V) = ^⊤ := iT_verum (V := V) 0
example : iT (1:V) (^⊤ : V) = ^⊤ := iT_verum (V := V) 1

-- 退化后的形状：`neg ⊤ ⋎ substs1 T' (domZero ⋏ ⊤)`
example {T' : V} :
    substs1 ℒₛₑₜ T' ((domZero (V := V)) ^⋏ (^⊤ : V))
      = substs1 ℒₛₑₜ T' (domZero (V := V)) ^⋏ ^⊤ := by
  rw [substs1, Bootstrapping.substs_and
    (isSemiformula_domZero (V := V) (n := (0:V))).isUFormula
    (IsUFormula.verum (L := ℒₛₑₜ))]
  simp [substs1]

end GodelQ.ProbeBridgeTop