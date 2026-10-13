import GodelQ.ZFC.ShCraigElimSetupQ
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000

namespace GodelQ.ProbeExsFinal
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

/-! ### 义务 ③ 与 `conjunct_rename` 对接

`conjunct_rename` 是**层数 1→0 对齐器**：
左边 `subst qVec² W` + `conjunct 2 1 …` 是 `iT 1` 侧过 `substs_qqAlls_two` 后的形，
右边 `conjunct 2 0 …` 是 `iT 0` 侧的形。**层数位移被它吸收。**

注：`conjunct_rename` 的 `i` 是**隐式**，`hi : i < 2` 里的 `2` 是裸字面量，
所以照抄成显式 `(j : V) (hj : j < 2)` 会把 i 逼到 universe 0——直接 `rw` 用它更稳。 -/

example :
    subst ℒₛₑₜ ((?[^#0, ^#1, ^&0] : V))
        (conjunct (V := V) (2:V) (1:V) (0:V) (iVE (V := V) (1:V) (^#(0:V) : V)))
      = conjunct (V := V) (2:V) (0:V) (0:V) (iVE (V := V) (0:V) (^&(0:V) : V)) := by
  rw [conjunct_rename (V := V) (by norm_num)]

end GodelQ.ProbeExsFinal
