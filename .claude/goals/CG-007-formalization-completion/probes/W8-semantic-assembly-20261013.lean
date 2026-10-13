import GodelQ.ZFC.ShCraigElimSetupQ
/-! ## 语义路线组装：卡点定位（2026-10-13）

三件零件已找到：
1. `tprovable_tquote_iff_provable_quote_sentence`：`Provable T ⌜σ⌝ ↔ T.internalize V ⊢ ⌜σ⌝`（多态）；
2. `SetTheory.complete`：`(∀ M, M ⊧ φ) → T ⊢ φ`（多态）；
3. `translate_iff`：`M ⊧ π.translate σ ↔ (π.Model M) ⊧ σ`（多态）。

**组装时的卡点**：目标 `ExsBridge2` 要的是
`Provable 𝗭𝗙𝗖 (imp (iT 0 (substs1 t p)) (^∃ (domZero ⋏ iT 1 p)))`，
即一个**具体的 V 层码**，而不是 `⌜σ⌝` 形。

零件 1 要求码是**引号形**。故须先说明
  `imp (iT 0 (substs1 t p)) (^∃ (domZero ⋏ iT 1 p)) = ⌜某 Sentence⌝`。

`iT_quote` 只对 `⌜φ⌝` 形（φ 是 Semisentence）给等式，方向相反。
**这是本路线的真正卡点**——不是宇宙问题（那已解决），而是**码的形状识别**。

本探针把卡点精确定位。 -/
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000

namespace GodelQ.ProbeExsB
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
namespace ProbeSemanticAssembly

-- 零件 1 的形状（要求 ⌜σ⌝）
#check @tprovable_tquote_iff_provable_quote_sentence

-- 目标码的形状：iT 0 (...) 与 ^∃ (...) 都是 V 层构造
-- `^∃ q` 是 `IsUFormula.exs` 形，不是引号
#check @Semiformula.exs

-- iT_quote 的方向：⌜φ⌝ → 码
#check @iT_quote

end ProbeSemanticAssembly