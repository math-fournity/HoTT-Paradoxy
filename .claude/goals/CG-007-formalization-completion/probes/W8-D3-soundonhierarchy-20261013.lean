import GodelQ.ZFC.ShCraigElimSetupQ

/-! ## D3 第四步的**闸门核验**：`𝗭𝗙𝗖.SoundOnHierarchy 𝚺 1` 是否可用（2026-10-14）

`models_iff_provable_of_Sigma0_param` 需要 `[T.SoundOnHierarchy 𝚺 1]`。
若该 instance 不成立/不存在，**第四步整条不可用**（与工作多少无关）。

**危险**：`T.SoundOnHierarchy 𝚺 1` 说「`T` 证的每条 Σ₁ 句都为真」——
这对**可靠的**理论成立，但**本项目要证的正是 𝗭𝗙𝗖 的一致性**，
若把 `SoundOnHierarchy` 当免费假设用，有**循环论证**的风险。

**本探针机器确认了循环性（exit 0）**——见下面的 theorem。 -/
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000

namespace GodelQ.ProbeExsB
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
namespace ProbeD3Gate

/-- 本探针的发现：**`T.SoundOnHierarchy 𝚺 1` 蕴含 `T` 一致**。
（`FirstOrder/Arithmetic/Basic/Hierarchy.lean:189`）

```
instance (T : ArithmeticTheory) [T.SoundOnHierarchy 𝚺 1] : Entailment.Consistent T :=
  T.consistent_of_sound (ℬ[<, ℒₒᵣ].Hierarchy 𝚺 1) (by simp)
```

故 `models_iff_provable_of_Sigma0_param` 对 `T := 𝗭𝗙𝗖` 的实例化
**逻辑上依赖 𝗭𝗙𝗖 的一致性**。

⚠ 本项目要证的正是 `𝗭𝗙𝗖 ⊬ 𝗭𝗙𝗖.consistent`。若 D3 的证明引用这个 instance，
**就是循环论证**（用「𝗭𝗙𝗖 一致」证「𝗭𝗙𝗖 一致」的反命题）。 -/
theorem sound_on_hierarchy_implies_consistent
    (T : ArithmeticTheory) [T.SoundOnHierarchy 𝚺 1] : Entailment.Consistent T := inferInstance

end ProbeD3Gate

#print axioms ProbeD3Gate.sound_on_hierarchy_implies_consistent