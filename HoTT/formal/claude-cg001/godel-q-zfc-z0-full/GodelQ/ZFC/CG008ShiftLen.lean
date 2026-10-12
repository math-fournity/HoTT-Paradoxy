import GodelQ.ZFC.CG008Conj

/-!
# CG-008 · `shiftVec` 的三条事实（对任意 `n : V`）

**未证**，但本轮把结构查清了，下一步的全部内容如下。

## 要证什么

```lean
theorem shiftVec_facts (b : V) : ∀ n : V,
    IsUTermVec ℒₛₑₜ n (shiftVec b n)
      ∧ len (shiftVec b n) = n
      ∧ termBShiftVec ℒₛₑₜ n (shiftVec b n) = shiftVec (b + 1) n
```

## 为什么必须**同时**归纳

- ①`IsUTermVec` 的定义本身带 `len`（`Term/Basic.lean:174`）⇒ ①要②；
- ③ 的 `termBShiftVec_cons`（`Term/Functions.lean:393`）要 `IsUTermVec` ⇒ ③要①；
- `len_termBShiftVec`（`Term/Functions.lean:383`）要 `IsUTermVec` ⇒ ②要①。

分开证会成环，所以一次归纳给出三元组。

## 已验的机器事实

| 事项 | 状态 |
|---|---|
| 归纳原理 `ISigma1.sigma1_succ_induction`（`Schemata.lean:706`）可用 | ✅ |
| 其前提 `[V↓[ℒₒᵣ] ⊧* 𝗜𝚺⁺₁]` 由 `inferInstance` 从 `𝗜𝚺₁` 得到 | ✅ |
| 其 `definability` 闸门要 `maxHeartbeats ≥ 1600000` | ✅ |
| `shiftVec b (n+1) = ^#b ∷ termBShiftVec n (shiftVec b n)`（`shiftVec_succ`） | ✅ |
| `shiftVec b 0 = 0`（`shiftVec_zero`） | ✅ |

## 递推步的写法要点（本轮实测）

- 三条**分别写 `have`**，最后 `refine ⟨?_, ?_, ?_⟩`；
- **不要在整条合取上 `rw`**——那会让 `isDefEq` 去判两个 `Fixpoint` 项是否相等，
  3200000 心跳仍超时。本轮的失败正是踩了这一点。
- ③ 用 `termBShiftVec_cons hb ih.1`，其中 `hb : IsUTerm ℒₛₑₜ ^#b`
  （`IsUTerm.bvar`），`ih.1 : IsUTermVec ℒₛₑₜ n (shiftVec b n)`；
  再用 `termBShift_bvar` 与 `shiftVec_succ` 收尾。

## 一旦这条过了

`CG008Conj.conjunct_snd_isUFormula` 由 `IsUTermVec.isSemitermVec` **直接**给出——
**结果层由 `listMax (termBVVec …)` 算出**，不需要任何算术界，
从而绕开「`V` 的 `LT` 是裸的」那条障碍；进而 `ve2_isUFormula`
与 `iVE_isUFormula` 的最后一支一并闭合。
-/

open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open FFL.Entailment
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding

namespace GodelQ.CG008ShiftLen
open GodelQ.ZFCArith GodelQ.Translate
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- 两条已验的递归等式（本文件顶部记录的一部分）
example (b : V) : Translate.shiftVec b 0 = 0 := by simp

example (b n : V) :
    Translate.shiftVec b (n + 1)
      = ^#b ∷ Bootstrapping.termBShiftVec ℒₛₑₜ n (Translate.shiftVec b n) := by
  simp

-- 归纳原理与其前提（已验）
example : V↓[ℒₒᵣ] ⊧* 𝗜𝚺⁺₁ := inferInstance

end GodelQ.CG008ShiftLen
