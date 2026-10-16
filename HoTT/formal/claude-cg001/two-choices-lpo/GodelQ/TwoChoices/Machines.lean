import GodelQ.ProcessObservation
import GodelQ.TwoChoices.Core

/-!
# A 断言存在的结果，机器交不出；经典逻辑对“停”与“不停”一视同仁（CG001-C-420、C-421）

研究发起人（2026-10-14，原话节选）：
- “一种表述是不可停机的，另外一种表述是可停机的，这两种表述在ZFC那里，在是否可停机这个观察角度
  上，不存在辨别力。”
- “ZFC-1这个反现实的逻辑，不仅仅在现实中是无法完成A的……”

本文件在经典的 Lean（与 ZFC 一样有排中律）里证明：

* C-420：每个停机搜索的开关序列（`haltBits e`）都单调，在经典逻辑里都有落定的一步；可是没有
  任何机器能统一交出这一步（`no_computable_settling_point`），也没有机器能交出终值本身
  （`no_computable_final_value`）。A 断言其存在的结果，没有哪个计算过程交得出来。
* C-421：排中律给“会停”和“永不停”同样的待遇，每一个都有现成的真假（`bivalence_halting`）；
  集合的存在也不过问可计算性，会停的程序和偶数一样组成集合（`sets_exist_alike`）；可是同一个理论
  证得出二者的差别：偶数可判定，停机不可判定（`computability_differs`）。在经典逻辑里 LPO 是
  定理（`lpo_classical`），它来自排中律，依赖 `Classical.choice`。

本文件是经典的：这里的定理依赖 `Classical.choice`，`QualificationTC.lean` 把这一点也作为对照写进
公理审计（审计不是空的）。
-/

namespace GodelQ.TwoChoices

open GodelQ Nat.Partrec Nat.Partrec.Code

/-- 停机搜索的开关序列：第 `k` 步回答“到这一步停了吗”。 -/
def haltBits (e : Process) : ℕ → Bool := fun k => decide (DoneBy e k)

theorem haltBits_mono (e : Process) : MonoBits (haltBits e) := by
  intro m n hmn hm
  exact decide_eq_true (doneBy_mono hmn (of_decide_eq_true hm))

/-- 在任何落定的步上，开关的值就是“停了没有”的真假。 -/
theorem done_iff_settled (e : Process) {N : ℕ} (hN : SettlesAt (haltBits e) N) :
    Done e ↔ haltBits e N = true := by
  constructor
  · intro hd
    obtain ⟨k, hk⟩ := (done_iff_exists_stage e).mp hd
    have h1 : haltBits e (N + k) = true :=
      decide_eq_true (doneBy_mono (Nat.le_add_left k N) hk)
    rw [hN (N + k) (Nat.le_add_right N k)] at h1
    exact h1
  · intro h
    exact (done_iff_exists_stage e).mpr ⟨N, of_decide_eq_true h⟩

theorem haltBits_computable : Computable (fun p : Process × ℕ => haltBits p.1 p.2) :=
  doneBy_computable.decide

/-- 在经典逻辑里 LPO 是定理：它来自排中律。 -/
theorem lpo_classical : LPO := by
  intro q
  rcases Classical.em (∃ k, q k = true) with h | h
  · exact Or.inr h
  · refine Or.inl (fun k => ?_)
    cases hk : q k with
    | false => rfl
    | true => exact absurd ⟨k, hk⟩ h

/-- C-420 (1)：在经典逻辑里，每个停机搜索都有落定的一步。 -/
theorem haltBits_settles_classically (e : Process) : ∃ N, SettlesAt (haltBits e) N :=
  limBit_of_lpo lpo_classical (haltBits e) (haltBits_mono e)

/-- C-420 (2)：没有机器能统一交出“在哪一步落定”。 -/
theorem no_computable_settling_point :
    ¬ ∃ F : Process → ℕ, Computable F ∧ ∀ e, SettlesAt (haltBits e) (F e) := by
  rintro ⟨F, hF, hset⟩
  apply ComputablePred.halting_problem 0
  refine ComputablePred.computable_iff.mpr ⟨fun e => haltBits e (F e), ?_, ?_⟩
  · exact haltBits_computable.comp (Computable.pair Computable.id hF)
  · funext e
    exact propext (done_iff_settled e (hset e))

/-- C-420 (3)：也没有机器能交出终值本身。 -/
theorem no_computable_final_value :
    ¬ ∃ f : Process → Bool, Computable f ∧
      ∀ e, ∃ N, SettlesAt (haltBits e) N ∧ haltBits e N = f e := by
  rintro ⟨f, hf, hfin⟩
  apply ComputablePred.halting_problem 0
  refine ComputablePred.computable_iff.mpr ⟨f, hf, ?_⟩
  funext e
  obtain ⟨N, hN, hv⟩ := hfin e
  rw [← hv]
  exact propext (done_iff_settled e hN)

/-- C-421 (1)：排中律对“会停”与“永不停”一视同仁，每一个都有现成的真假。 -/
theorem bivalence_halting (e : Process) : Done e ∨ ¬ Done e := Classical.em _

/-- C-421 (2)：集合的存在不过问可计算性：会停的程序组成一个集合，偶数也组成一个集合。 -/
theorem sets_exist_alike :
    (∃ S : Set Process, ∀ e, e ∈ S ↔ Done e) ∧ (∃ S : Set ℕ, ∀ n, n ∈ S ↔ n % 2 = 0) :=
  ⟨⟨{e | Done e}, fun _ => Iff.rfl⟩, ⟨{n | n % 2 = 0}, fun _ => Iff.rfl⟩⟩

/-- C-421 (3)：同一个理论证得出二者的差别：偶数可判定，停机不可判定。 -/
theorem computability_differs :
    ComputablePred (fun n : ℕ => n % 2 = 0) ∧ ¬ ComputablePred Done :=
  ⟨PrimrecPred.computablePred
      (Primrec.eq.comp (Primrec.nat_mod.comp Primrec.id (Primrec.const 2)) (Primrec.const 0)),
    ComputablePred.halting_problem 0⟩

end GodelQ.TwoChoices

#print axioms GodelQ.TwoChoices.haltBits_mono
#print axioms GodelQ.TwoChoices.done_iff_settled
#print axioms GodelQ.TwoChoices.lpo_classical
#print axioms GodelQ.TwoChoices.haltBits_settles_classically
#print axioms GodelQ.TwoChoices.no_computable_settling_point
#print axioms GodelQ.TwoChoices.no_computable_final_value
#print axioms GodelQ.TwoChoices.bivalence_halting
#print axioms GodelQ.TwoChoices.sets_exist_alike
#print axioms GodelQ.TwoChoices.computability_differs
