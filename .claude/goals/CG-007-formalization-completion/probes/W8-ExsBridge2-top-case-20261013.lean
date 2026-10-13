import GodelQ.ZFC.ShCraigElimSetupQ
/-! ## `ExsBridge2` 的 `p = ⊤` 情形：走语义路线（2026-10-13）

`p = ⊤` 时 `ExsBridge2` 退化为 `Provable 𝗭𝗙𝗖 (⊤ → ^∃ (domZero ⋏ ⊤))`，
即 `Provable 𝗭𝗙𝗖 (^∃ (domZero ⋏ ⊤))`——「ω 非空」。

**关键**：`^∃ (domZero ⋏ ⊤)` 是**闭句**（无自由变量），
故可直接用 `SetTheory.complete` + 模型论证。

**这一步不需要反向引理**——因为 `p = ⊤` 是**具体的**，
`^∃ (domZero ⋏ ⊤)` 就是 `⌜∃¹(domZero ⋏ ⊤)⌝`（`quote_*` 是 rfl）。

本探针核验这条路。 -/
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000

namespace GodelQ.ProbeExsB
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
namespace ProbeBridge2Top

-- 目标句的形状：`^∃ (domZero ⋏ ⊤)`
-- `domZero ⋏ ⊤` 是层 1 公式（`domZero` 层 1、`⊤` 任意层）
example : IsSemiformula ℒₛₑₜ (1:V) ((domZero (V := V)) ^⋏ (^⊤ : V)) :=
  IsSemiformula.and.mpr
    ⟨by simpa using isSemiformula_domZero (V := V) (n := (0:V)), by simp⟩

-- `^∃ (domZero ⋏ ⊤)` 是闭句（层 0）
example : IsSemiformula ℒₛₑₜ (0:V) ((^∃ ((domZero (V := V)) ^⋏ (^⊤ : V))) : V) :=
  (IsSemiformula.exs (L := ℒₛₑₜ) (n := (0:V)) (p := _)).mpr (by
    simpa using (IsSemiformula.and.mpr
      ⟨by simpa using isSemiformula_domZero (V := V) (n := (0:V)), by simp⟩ :
      IsSemiformula ℒₛₑₜ ((0:V) + 1) ((domZero (V := V)) ^⋏ (^⊤ : V))))

-- ω 非空（`zero_mem_ω`，Foundation 现成）
#check @SetTheory.zero_mem_ω
#check @SetTheory.ω

end ProbeBridge2Top