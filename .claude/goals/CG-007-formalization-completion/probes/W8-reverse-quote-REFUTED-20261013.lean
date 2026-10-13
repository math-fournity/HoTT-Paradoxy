import GodelQ.ZFC.ShCraigElimSetupQ
/-! ## ⚠ 反向引理**在非标准模型里为假**——我这条支作废（2026-10-13）

001-Step 提出的反例论证（Master 逐条核验后采纳），我复核**成立**：

1. `IsUFormula : V → Prop := (FormalizedFormula.construction L).Fixpoint ![]`
   ——**是 Fixpoint**，非标准模型里含**非标准元素**；
2. `IsSemiformula` 是 Σ₁ 可定义谓词，非标准 V 里存在「非标准长度」的合式公式码；
3. 这些码**不对应任何元层 `φ : Semiproposition`**（元层公式是**有限**语法对象）；
4. ⟹ **反向引理 `IsSemiformula → ∃ φ, p = ⌜φ⌝` 在非标准模型里是假的**。

**旁证（决定性）**：Foundation 的 `IsSemiformula.sound`（`Coding.lean:478`）
**载体是 `ℕ`**——不是「V 层版待建」，而是**V 层版不存在**。
ℕ 层版的存在恰恰说明：标准模型里对，非标准模型里错。

**我的错误链**（第九次同类）：
* 我搜到 `IsSemiformula.sound` 后判断「V 层版应当可证，只是要搬证明」；
* 实际证据（载体是 ℕ）指向的是**相反**的结论；
* 我把它读成了「搬一下就行」，而不是「ℕ 限定是**本质的**」。

**教训**：看到「载体被限定在 ℕ」时，先问**为什么**限定——
若限定是本质的（非标准模型反例），那就不是「待推广」而是「不可推广」。 -/
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000

namespace GodelQ.ProbeExsB
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
namespace ProbeReverseRefuted

-- 记录关键事实：IsUFormula 是 Fixpoint（非标准元素可入）
#check @IsUFormula
#check @IsSemiformula

-- 反向引理在 ℕ 层存在（标准模型）
#check @IsSemiformula.sound

end ProbeReverseRefuted