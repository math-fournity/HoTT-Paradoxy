import GodelQ.ZFC.ShCraigElimSetupQ
/-! ## `ExsBridge2` 的**语义路线**（2026-10-13）

`ExsBridge2` 要 `Provable 𝗭𝗙𝗖 φ`（`φ := imp (iT 0 (substs1 t p)) (^∃ (domZero ⋏ iT 1 p))`）。

关键工具（Foundation 现成）：
* `SetTheory.complete`：只需在每个 𝗭𝗙𝗖 模型里成立；
* `DirectTranslation.translate_iff`：`M ⊧ π.translate σ ↔ (π.Model M) ⊧ σ`。

**四条入口全部可用（本探针 exit 0）**：
1. `SetTheory.complete : (∀ M, M ⊧ φ) → T ⊢ φ`；
2. `DirectTranslation.Model.translate_iff : M ⊧ π.translate σ ↔ (π.Model M) ⊧ σ`；
3. `DirectTranslation.Model.evalb_singleton_translate_iff`（层 1 版）；
4. `iT_quote : iT ↑n ⌜φ⌝ = ⌜arithTrln.translate φ⌝`（`iT` 与 `translate` 的桥）。

**战略意义**：`ExsBridge2` 的数学内容是「`p[t] → ∃x∈ω p(x)`」——
这在算术里是**一阶逻辑重言式**（t 的值就是见证）。
故它不需要 `iT_substs1` 那样的语法等式桥，走语义路线更直接。

本探针核验语义路线的入口件是否可用。 -/
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000

namespace GodelQ.ProbeExsB
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
namespace ProbeBridge2Semantic

-- 入口 1：`SetTheory.complete`
#check @SetTheory.complete

-- 入口 2：翻译的语义桥
#check @DirectTranslation.Model.eval_translate_iff
#check @DirectTranslation.Model.evalb_singleton_translate_iff

-- 入口 3：句子的语义桥（`translate_iff` 在 Model 命名空间下）
#check @DirectTranslation.Model.translate_iff

-- 入口 4：`iT` 与 `translate` 的关系（包内）
#check @iT_quote
#check @arithTrln

end ProbeBridge2Semantic