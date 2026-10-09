import GodelQ.ProcessObservation

/-!
# CG-005 · 理论层：有效理论对过程完成的观察力（Q）

把一个有效公理化的理论 `T`（例如 bare ZFC）只透过它关于过程的三类陈述来看：

* `provesHalts e`   ：`T ⊢ ⌜e 停机⌝`
* `provesNever e`   ：`T ⊢ ⌜e 永不停机⌝`
* `provesNotYet e k`：`T ⊢ ⌜e 在 k 步之内尚未停机⌝`

并且只假设四条标准的元性质（对 bare ZFC 都是教科书事实，最后一条是一致性这一通常前提）：

* (R)   `re_never`        ：`T` 证明的“永不停机”句构成可枚举集合（`T` 有效公理化）；
* (Σ1C) `sigma1_complete` ：确实停机的过程，`T` 都证明它停机；
* (Δ0C) `delta0_complete` ：在第 k 步确实尚未停机，`T` 都证明这一点；
* (Con) `consistent`      ：`T` 不同时证明“e 停机”与“e 永不停机”。

由此证明：

* `never_sound`（C-88）：一致 + Σ1 完全 ⟹ `T` 说“永不停机”时不会说错；
* `godel_I_process_form`（C-89）：存在过程 `d`，它确实永不停机，`T` 在每一刻都确认“尚未停机”，
  却证明不了“永不停机”；并且 `d` 停机恰好当 `T` 证明它永不停机——哥德尔句的过程形式；
* `devils_bargain`（C-90）：`T` 不封闭于 ω 完成规则 P（“每一刻都尚未停机，所以永不停机”）；
  更一般地，Σ1C、Δ0C 加上 P，要么不可枚举（`OmegaTheory.not_effective`），
  要么不一致（`effective_omega_inconsistent`）；
* 必要性与非空：不要一致性时 P 可由有效理论满足；不要有效性时有一致的 P 理论（停机事实本身）；
  四条前提可同时被一个具体理论满足。
-/

namespace GodelQ

open Nat.Partrec Nat.Partrec.Code

/-- 透过关于过程的陈述来看的有效理论，附四条标准元性质。 -/
structure EffectiveTheory where
  provesHalts : Process → Prop
  provesNever : Process → Prop
  provesNotYet : Process → ℕ → Prop
  re_never : REPred provesNever
  sigma1_complete : ∀ e, Done e → provesHalts e
  delta0_complete : ∀ e k, ¬ DoneBy e k → provesNotYet e k
  consistent : ∀ e, provesHalts e → provesNever e → False

namespace EffectiveTheory

variable (T : EffectiveTheory)

/-- C-88：`T` 说“永不停机”时不会说错（Π1 可靠），由一致性与 Σ1 完全性推出。 -/
theorem never_sound : ∀ e, T.provesNever e → ¬ Done e :=
  fun e hn hd => T.consistent e (T.sigma1_complete e hd) hn

/-- `T` 作为一个永不完成观察者。 -/
def observer : NeverObserver := ⟨T.provesNever, T.re_never, T.never_sound⟩

/-- Q 不是没有：每一次真实的完成，`T` 都看得见。 -/
theorem observes_every_completion : ∀ e, Done e → T.provesHalts e := T.sigma1_complete

/-- Q 不是没有：对永不完成的过程，每一个有限时刻，`T` 都确认“尚未完成”。 -/
theorem observes_every_instant (e : Process) (h : ¬ Done e) (k : ℕ) : T.provesNotYet e k :=
  T.delta0_complete e k (fun hk => h ((done_iff_exists_stage e).mpr ⟨k, hk⟩))

/-- C-89：哥德尔第一不完备定理的过程形式（含 ω 形式）。 -/
theorem godel_I_process_form :
    ∃ d : Process, ¬ Done d ∧ ¬ T.provesNever d ∧ (∀ k, T.provesNotYet d k) ∧
      (Done d ↔ T.provesNever d) := by
  obtain ⟨d, hnd, hna, hiff⟩ := diagonal_escape T.observer
  exact ⟨d, hnd, hna, T.observes_every_instant d hnd, hiff⟩

/-- Q 完备：`T` 看得见每一个“永不完成”。 -/
def CompleteForNever : Prop := ∀ e, ¬ Done e → T.provesNever e

/-- Q 不完备：没有有效、一致、Σ1 完全的理论看得见每一个“永不完成”。 -/
theorem not_completeForNever : ¬ T.CompleteForNever := by
  intro h
  obtain ⟨d, hnd, hna, _⟩ := T.godel_I_process_form
  exact hna (h d hnd)

/-- ω 完成规则 P：只要每一个有限时刻都确认“尚未完成”，就接受“永不完成”——
以“完成的整体”宣布无穷过程的结局。 -/
def OmegaClosed : Prop := ∀ e, (∀ k, T.provesNotYet e k) → T.provesNever e

/-- P 会给出完备的 Q。 -/
theorem omegaClosed_imp_complete (hP : T.OmegaClosed) : T.CompleteForNever :=
  fun e h => hP e (T.observes_every_instant e h)

/-- C-90：魔鬼交易（有效形式）。有效、一致、Σ1/Δ0 完全的理论不封闭于 P。 -/
theorem devils_bargain : ¬ T.OmegaClosed := fun hP =>
  T.not_completeForNever (T.omegaClosed_imp_complete hP)

end EffectiveTheory

/-- 不要求有效性、但封闭于 P 的理论。 -/
structure OmegaTheory where
  provesHalts : Process → Prop
  provesNever : Process → Prop
  provesNotYet : Process → ℕ → Prop
  sigma1_complete : ∀ e, Done e → provesHalts e
  delta0_complete : ∀ e k, ¬ DoneBy e k → provesNotYet e k
  consistent : ∀ e, provesHalts e → provesNever e → False
  omega : ∀ e, (∀ k, provesNotYet e k) → provesNever e

namespace OmegaTheory

variable (T : OmegaTheory)

/-- 封闭于 P 的一致理论恰好接受全部永不完成者。 -/
theorem decides_never : ∀ e, T.provesNever e ↔ ¬ Done e := by
  intro e
  constructor
  · exact fun hn hd => T.consistent e (T.sigma1_complete e hd) hn
  · intro h
    exact T.omega e (fun k => T.delta0_complete e k
      (fun hk => h ((done_iff_exists_stage e).mpr ⟨k, hk⟩)))

/-- C-90（不可计算形式）：一致 + Σ1C + Δ0C + P ⟹ 永不完成句集不可枚举——P 不可计算。 -/
theorem not_effective : ¬ REPred T.provesNever := fun hre =>
  complete_observer_not_re T.provesNever (fun e h => (T.decides_never e).mp h)
    (fun e h => (T.decides_never e).mpr h) hre

end OmegaTheory

/-- C-90（矛盾形式）：有效 + Σ1C + Δ0C + P，而不预设一致性 ⟹ 理论不一致：
存在 `e`，理论既证明它停机又证明它永不停机。 -/
theorem effective_omega_inconsistent
    (provesHalts provesNever : Process → Prop) (provesNotYet : Process → ℕ → Prop)
    (hre : REPred provesNever)
    (hs1 : ∀ e, Done e → provesHalts e)
    (hd0 : ∀ e k, ¬ DoneBy e k → provesNotYet e k)
    (hP : ∀ e, (∀ k, provesNotYet e k) → provesNever e) :
    ∃ e, provesHalts e ∧ provesNever e := by
  by_contra hcon
  push Not at hcon
  exact EffectiveTheory.devils_bargain
    ⟨provesHalts, provesNever, provesNotYet, hre, hs1, hd0, fun e a b => hcon e a b⟩ hP

/-! ## 必要性与非空（控制） -/

/-- 一个确定永不停机的具体过程：`rfind' succ` 寻找后继函数的零点，永远找不到。 -/
theorem rfind_succ_never : ¬ Done (Code.rfind' Code.succ) := by
  intro h
  unfold Done at h
  simp [Code.eval] at h
  exact absurd (Nat.rfind_spec (Part.get_mem h)) (by simp)

/-- 控制 1（非空）：四条前提可以同时被一个具体的有效理论满足——它只知道一条
“永不停机”事实（`rfind' succ`）。 -/
def toyTheory : EffectiveTheory where
  provesHalts e := Done e
  provesNever e := e = Code.rfind' Code.succ
  provesNotYet e k := ¬ DoneBy e k
  re_never := ComputablePred.to_re (PrimrecPred.computablePred
      (Primrec.eq.comp Primrec.id (Primrec.const (Code.rfind' Code.succ))))
  sigma1_complete _ h := h
  delta0_complete _ _ h := h
  consistent e h1 h2 := by subst h2; exact rfind_succ_never h1

/-- 控制 2（P 可一致，但不可计算）：“停机事实本身”构成一致、Σ1C、Δ0C、封闭于 P 的理论。 -/
def truthTheory : OmegaTheory where
  provesHalts e := Done e
  provesNever e := ¬ Done e
  provesNotYet e k := ¬ DoneBy e k
  sigma1_complete _ h := h
  delta0_complete _ _ h := h
  consistent _ h1 h2 := h2 h1
  omega e h := fun hd => by
    obtain ⟨k, hk⟩ := (done_iff_exists_stage e).mp hd
    exact h k hk

/-- 控制 3（一致性必要）：不要一致性时，P 可以被一个有效理论满足——那个什么都证明的理论。 -/
theorem consistency_needed :
    ∃ (provesHalts provesNever : Process → Prop) (provesNotYet : Process → ℕ → Prop),
      REPred provesNever ∧ (∀ e, Done e → provesHalts e) ∧
      (∀ e k, ¬ DoneBy e k → provesNotYet e k) ∧
      (∀ e, (∀ k, provesNotYet e k) → provesNever e) := by
  refine ⟨fun _ => True, fun _ => True, fun _ _ => True, ?_, fun _ _ => trivial,
    fun _ _ _ => trivial, fun _ _ => trivial⟩
  exact ComputablePred.to_re (Computable.computablePred ((Computable.const true).of_eq fun _ => by simp))

/-- 控制 4（可靠性必要）：没有可靠性时，对角逃逸不成立——接受一切的可枚举集合不漏掉任何过程。 -/
theorem soundness_needed :
    ¬ ∀ (accepts : Process → Prop), REPred accepts → ∃ d, ¬ Done d ∧ ¬ accepts d := by
  intro h
  obtain ⟨d, _, hna⟩ := h (fun _ => True)
    (ComputablePred.to_re (Computable.computablePred ((Computable.const true).of_eq fun _ => by simp)))
  exact hna trivial

end GodelQ

#print axioms GodelQ.EffectiveTheory.never_sound
#print axioms GodelQ.EffectiveTheory.godel_I_process_form
#print axioms GodelQ.EffectiveTheory.not_completeForNever
#print axioms GodelQ.EffectiveTheory.devils_bargain
#print axioms GodelQ.OmegaTheory.decides_never
#print axioms GodelQ.OmegaTheory.not_effective
#print axioms GodelQ.effective_omega_inconsistent
#print axioms GodelQ.rfind_succ_never
#print axioms GodelQ.toyTheory
#print axioms GodelQ.truthTheory
#print axioms GodelQ.consistency_needed
#print axioms GodelQ.soundness_needed
