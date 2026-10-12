import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 4000000
namespace GodelQ.ProbeArith

/-! ## 决定性二分：`semiformula_result_induction` 的 `key` 类型里
**不能出现 `param + 1`**（2026-10-12，机器验证）

`iT_shift` 的 `key` 类型是

```lean
iT param (shift ℒₒᵣ p) = shift ℒₛₑₜ (iT.construction.result ℒₒᵣ param p)
```

—— `param` **原样**出现，`(by definability)` 通过。

`iT_free` 的正确形状需要 `result ... (param + 1) p`（`iT` 的 `all` 支把层数 +1）。
把它写进 `key` 的类型，`(by definability)` **失败**：

```lean
iT param (free ℒₒᵣ p)
  = imp ℒₛₑₜ (subst ℒₛₑₜ ?[^&0] domZero) (free ℒₛₑₜ (iT.construction.result ℒₒᵣ (param+1) p))
                                                            ~~~ ^^^^
```

**二分结果**（全部用同一台机器、同一探针，只改 RHS）：

| RHS（`key` 类型） | `definability` |
|---|---|
| `shift L (result L param p)`        | ✅ |
| `free L (result L param p)`         | ✅ |
| `imp (subst ?[^&0] domZero) (result L param p)` | ✅ |
| `imp (subst ?[^&0] domZero) (free (result L param p))` | ✅ |
| `free L (result L (param+1) p)`     | ❌ |
| `free L (result L (n+1) p)`         | ❌ |

**结论**：失败的**唯一**原因是 `param + 1`（算术），
与 `free`/`imp`/`subst` **全部无关**——把算术表达式写进 `key` 的类型，
`DefinableRel₄` 的实例合成就过不去。

**绕法（下一步待试）**：把层数位移从 `key` 的类型里**拿掉**，
改成在 `P` 里只写 `result L param q`（`param` 原样），
然后在 `all`/`exs` 两支**内部**用 `result_all`/`result_exs` 的层数展开
把 `+1` 补回来。这正是 `ShCraigElimNegLaw` 用 `Negation` 时说的
「`param' = param`」与 `iT` 的 `param' = param + 1` 不同的原因。
-/

-- 正对照（已知可过）
theorem ctrl_shift {n : V} : ∀ p, IsSemiformula ℒₒᵣ n p →
    iT n (shift ℒₒᵣ p) = shift ℒₛₑₜ (iT n p) := by
  have key : ∀ {param n p : V}, IsSemiformula ℒₒᵣ n p → param = n →
      iT param (shift ℒₒᵣ p) = shift ℒₛₑₜ (iT.construction.result ℒₒᵣ param p) :=
    UformulaRec1.Construction.semiformula_result_induction
      (V := V) (c := iT.construction) (L := ℒₒᵣ)
      (P := fun param n p q => param = n → iT param (shift ℒₒᵣ p) = shift ℒₛₑₜ q)
      (by definability)
      (by intro n param k R v hR hv h; subst h; sorry)
      (by intro n param k R v hR hv h; subst h; sorry)
      (by intro n param h; subst h; sorry)
      (by intro n param h; subst h; sorry)
      (by intro n param p q hp hq ihp ihq h; subst h; sorry)
      (by intro n param p q hp hq ihp ihq h; subst h; sorry)
      (by intro n param p hp ih h; subst h; sorry)
      (by intro n param p hp ih h; subst h; sorry)
  intro p hp
  exact key hp rfl

-- 失败对照：`param + 1`
theorem bad_plus_one {n : V} : ∀ p, IsSemiformula ℒₒᵣ n p →
    iT n (free ℒₒᵣ p)
      = imp ℒₛₑₜ (subst ℒₛₑₜ ?[^&0] domZero) (free ℒₛₑₜ (iT (n + 1) p)) := by
  have key : ∀ {param n p : V}, IsSemiformula ℒₒᵣ n p → param = n →
      iT param (free ℒₒᵣ p)
        = imp ℒₛₑₜ (subst ℒₛₑₜ ?[^&0] domZero) (free ℒₛₑₜ (iT.construction.result ℒₒᵣ (param+1) p)) :=
    UformulaRec1.Construction.semiformula_result_induction
      (V := V) (c := iT.construction) (L := ℒₒᵣ)
      (P := fun param n p q => param = n →
        iT param (free ℒₒᵣ p)
          = imp ℒₛₑₜ (subst ℒₛₑₜ ?[^&0] domZero) (free ℒₛₑₜ (iT.construction.result ℒₒᵣ (param+1) q)))
      (by definability)
      sorry

end GodelQ.ProbeArith
