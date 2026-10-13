import GodelQ.ZFC.ShCraigElimSetupQ
/-! ## `ExsBridge2` 原子情形的精确残差（2026-10-13）

`ExsBridge2` 的原子情形（`p = ^rel 2 cEqN ?[^#0,^#0]`、`t = ^&0`）：

```
Provable 𝗭𝗙𝗖 (imp (iT 0 (^rel 2 cEqN ?[^&0,^&0]))
                  (^∃ (domZero ⋏ iT 1 (^rel 2 cEqN ?[^#0,^#0]))))
```

注意 `iT 0 (^∃ p) = ^∃ (domZero ⋏ iT 1 p)`（`iT_exs`），
故目标就是 **`iT 0 (p[t]) → iT 0 (^∃ p)`**——
即「`iT` 把重言式 `p[t] → ∃x p(x)` 送到可证式」。

本探针把两侧展开到 `iTR` 层，让 Lean 打印残差，不写推测。 -/
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000

namespace GodelQ.ProbeExsB
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
namespace ProbeBridge2Atom

-- 两侧展开后的形状（`iT_rel` 两次）
example (hR : (ℒₒᵣ).IsRel (2:V) (↑cEqN : V)) :
    iT (0:V) (^rel 2 (↑cEqN) (?[^&0, ^&0] : V))
      = iTR (0:V) 2 (↑cEqN) (?[^&0, ^&0] : V) :=
  iT_rel (V := V) (n := (0:V)) (k := (2:V)) (R := (↑cEqN : V))
    (v := (?[^&0, ^&0] : V)) hR
    (by simpa using (IsUTermVec.adjoin (IsUTermVec.adjoin IsUTermVec.empty
      (IsUTerm.fvar (x := (0:V)))) (IsUTerm.fvar (x := (0:V)))))

-- `iT 0 (^∃ p) = ^∃ (domZero ⋏ iT 1 p)`（`iT_exs`，这是目标右端的来源）
example : iT (0:V) (^∃ (^rel 2 (↑cEqN) (?[^#0, ^#0] : V)))
      = (^∃ (domZero (V := V)) ^⋏ iT (0+1:V) (^rel 2 (↑cEqN) (?[^#0, ^#0] : V)) : V) :=
  iT_exs (V := V) (n := (0:V)) (p := (^rel 2 (↑cEqN) (?[^#0, ^#0] : V) : V))
    (IsUFormula.rel.mpr
      ⟨by rw [cEqN]; exact codeIn_rel_quote _,
       by simpa using (IsUTermVec.adjoin (IsUTermVec.adjoin IsUTermVec.empty
         (IsUTerm.bvar (z := (0:V)))) (IsUTerm.bvar (z := (0:V))))⟩)

end ProbeBridge2Atom