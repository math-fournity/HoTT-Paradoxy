import GodelQ.ZFC.ShCraigElimSetupQ
/-! ## `IsTerm` 与 `IsTermFVFree` 的关系（2026-10-14）

**问题**：「闭项的值在 ω」需要「t 不含 fvar」，而 `IsTerm t` 给不出这条
（`IsSemiterm.fvar` 对 `x` 无条件）。

`IsTermFVFree`（`Functions.lean:696`）的定义是
`IsSemiterm L n t ∧ termShift L t = t`——**用 shift 不动来刻画无 fvar**。

## 核验结果（exit 0，公理三条）

**`¬ IsTermFVFree ℒₒᵣ 0 ^&0` —— 机器证出**：

```lean
example : ¬ IsTermFVFree ℒₒᵣ (0:V) (^&(0:V) : V) := by
  rw [IsTermFVFree]
  intro h
  rw [termShift_fvar] at h
  simp at h
```

机制：`IsTermFVFree n t := IsSemiterm L n t ∧ termShift L t = t`，
而 `termShift ^&0 = ^&1 ≠ ^&0`。

## ★ 决定性后果

**`IsTerm ^&0` 成立，但 `IsTermFVFree 0 ^&0` 为假。**
⟹ **不存在** `IsTerm t → IsTermFVFree 0 t`（`^&0` 就是反例）。

**故「闭项的值在 ω」这条引理的前提不能只用 `IsTerm`**——
它需要更强的「t 不含 fvar」，而那是**额外的义务**。

**且不能收窄 `ExsBlockerQ` 的 statement**（Master 已提醒：
Foundation 的 `exsIntro`/`ex_m` 也只要求 `IsTerm`，收窄会让归致在 fvar 上失效）。

**⟹ hExs 的桥无论怎么走，都要正面处理 fvar。** -/
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open GodelQ.ZFCArith GodelQ.ZFCZ0 GodelQ.Translate GodelQ.Z0Full
open GodelQ.SeqTranslate GodelQ.ShCraigElimSetup GodelQ.ShCraigElimBranches GodelQ.TranslateShiftCompat
set_option maxHeartbeats 800000

namespace GodelQ.ProbeExsB
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]
namespace ProbeIsTermFVFree
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- ① `IsTermFVFree` 的定义
#check @IsTermFVFree

-- ② `termShift` 对 fvar 加一（机制：故 fvar 项 shift 后会变）
#check @termShift_fvar

-- ③ `IsTerm ^&0` 成立（已知）
example : IsTerm ℒₒᵣ (^&(0:V) : V) := IsSemiterm.fvar (L := ℒₒᵣ) (V := V) (n := (0:V)) 0

-- ④ ★ 决定性：`IsTermFVFree 0 ^&0` 应为**假**（termShift ^&0 = ^&1 ≠ ^&0）
--    若它确实假，则「闭项值在 ω」的前提**不能只用 IsTerm**
example : ¬ IsTermFVFree ℒₒᵣ (0:V) (^&(0:V) : V) := by
  rw [IsTermFVFree]
  intro h
  rw [termShift_fvar] at h
  simp at h

end ProbeIsTermFVFree