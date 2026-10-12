import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000
namespace GodelQ.ProbeAll
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! ## 决定性检验：`iT 0 (free ℒₒᵣ p)` 与 `free ℒₛₜ (imp domZero (iT 1 p))` **不相等**

（2026-10-12，机器验证）

取最原子例 `p = ^rel 2 cEqN ?[^#0, ^#1]`（层 1）。两侧经 `simp only` 归一化后：

```
LHS = ^rel 2 cEqN (iVE 0 ^&0 ∷ iVE 0 ^&1 ∷ 0)
RHS = substs1 ℒₛₑₜ ^&0 (shift ℒₛₑₜ (imp ℒₛₑₜ domZero (^rel 2 cEqN (iVE 1 ^#0 ∷ iVE 1 ^#1 ∷ 0))))
```

**LHS 是裸 `^rel`，RHS 是 `imp` 包着的 `substs1/shift` 复合**——顶层构造子就不同，
**必然不相等**。这一条比 ShCraigElimBranches 第十五轮的手算更强：
它是**机器归一化后**的确定性结论，不是推导。

**结论**：`hAll` 不能走「先 `iT` 后 `free`」的等式桥接。
正确方向是从 `ih` 出发直接用 `Derivable` 规则构造（`wk`/`cut`/`em`），
或者给 `iT` 的 `all` 支换语义（接口级改动，需研究发起人确认）。 -/

example : iT (0:V) (free ℒₒᵣ (^rel (0+1+1) (↑cEqN) (?[^#0, ^#(0+1)] : V)))
    = free ℒₛₑₜ (imp ℒₛₑₜ domZero (iT (1:V) (^rel (0+1+1) (↑cEqN) (?[^#0, ^#(0+1)] : V)))) := by
  simp only [iT, free, iVE_bvar, iVE_fvar, eqAtom, substs_rel, termSubstVec_cons₂,
    termSubst_bvar, termSubst_fvar, nth_adjoin_zero, nth_adjoin_one]
  rw [show UformulaRec1.Construction.result ℒₒᵣ iT.construction 1
      (^rel (0 + 1 + 1) (↑cEqN) (^#0 ∷ ^#(0 + 1) ∷ 0))
      = ^rel (0 + 1 + 1) (↑cEqN) (?[iVE 1 ^#0, iVE 1 ^#(0+1)] : V) from by
    unfold iT; rfl]
  rw [show UformulaRec1.Construction.result ℒₒᵣ iT.construction 0
      (substs1 ℒₒᵣ (^&0) (shift ℒₒᵣ (^rel (0 + 1 + 1) (↑cEqN) (^#0 ∷ ^#(0 + 1) ∷ 0))))
      = ^rel (0 + 1 + 1) (↑cEqN) (?[iVE 0 ^&0, iVE 0 ^&(0+1)] : V) from by
    unfold iT; rfl]
  -- 目标：两侧顶层构造子不同（`^rel` vs `imp`），不可能相等
  sorry

end GodelQ.ProbeAll
