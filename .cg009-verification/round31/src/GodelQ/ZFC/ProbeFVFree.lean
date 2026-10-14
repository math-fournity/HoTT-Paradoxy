-- Probe: IsTermFVFree is the ready-made "closed term" predicate (per Master's intel).
import GodelQ.ZFC.ITSubstOpen9
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory Bootstrapping
open scoped FFL.FirstOrder.Arithmetic FFL.FirstOrder.Bounding
open FFL.FirstOrder.Language
open GodelQ.ZFCArith GodelQ.Translate

namespace GodelQ.ProbeFVFree
variable {V : Type*} [ORingStructure V] [V↓[ℒₒᵣ] ⊧* 𝗜𝚺₁]

-- Q1: IsTermFVFree rejects fvars at ANY layer (incl. 0)
example (x : V) : ¬ IsTermFVFree ℒₒᵣ (0:V) (^&x : V) := by simp

-- Q2: layer-0 bvars are impossible, so bvar branch is vacuous but harmless
example (n x : V) : IsTermFVFree ℒₒᵣ n ^#x ↔ x < n := by simp

-- Q3: IsTermFVFree implies IsSemiterm (it's a conjunction member)
example (n t : V) (h : IsTermFVFree ℒₒᵣ n t) : IsSemiterm ℒₒᵣ n t := h.1

-- Q4: **候选 (C) 的真实代价 —— 零**（Master 情报核实）。
-- `IsTermFVFree L n t := IsSemiterm L n t ∧ termShift L t = t`（Functions.lean:696）
-- 两条 simp 引理 Foundation 已给：`.bvar`（x < n）、`.fvar`（fvar 直接假）。
-- `IsTermFVFree.fvar` 已声明为 simp：`¬ IsTermFVFree L n ^&x`（Functions.lean:703）
example (n x : V) : ¬ IsTermFVFree ℒₒᵣ n ^&x := by simp

-- Q5: 层 0 下 bvar 不可能 ⟹ IsTermFVFree 层 0 只剩 fvar/func 两支
example (t : V) (h : IsTermFVFree ℒₒᵣ (0:V) t) : IsSemiterm ℒₒᵣ (0:V) t := h.1

end GodelQ.ProbeFVFree
