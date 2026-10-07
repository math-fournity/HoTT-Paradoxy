import GodelQ.GodelZenoRunner

/-!
# CG-005 · 同一个 ω 追问：芝诺、H0、Z0 与哥德尔–芝诺跑者

一个 ω 追问是在每个有限阶段 `n` 提出的同一个问题“到了吗／落定了吗／找到了吗”。
它的“完成”是某一阶段答“是”；它的“永不完成”是每一阶段都答“否”。

四个实例：

* `zenoQ`：经典芝诺——第 `n` 步是否已到终点（位置 `1 - (1/2)^n = 1`？）；
* `processQ d`：过程 `d` 是否已在 `n` 步内停机。哥德尔–芝诺跑者的“站住”、以及 Z0（理论对
  自身矛盾的证明搜索）都是这一形式的实例；
* `h0Q settled`：HoTT 宇宙上的逐层追问（第 `n` 问：宇宙是否在第 `n+1` 层落定）。其“每一问
  都答否”是 Cubical Agda 中的定理（CG001-C-78；`question (Type ℓ-zero) judge ≡ never`），
  不在 Lean 内重证；这里以参数 `settled` 与假设 `never` 接入，跨内核的对应写在 CLAIM 中。

本文件证明：

* `P_fin_refuted`：对任何永不完成的 ω 追问，“有一个形式上完成的整体 ⟹ 某个有限阶段完成”
  （完成的有限读法 P_fin）都不成立——芝诺（极限为 1）、H0（宇宙一次给出）、Z0（全部证明的
  集合存在）同遭否定；
* `zenoQ_never` 与 `zenoQ_formal`：经典芝诺永不在有限阶段到达，而极限恰为 1；
* `observability_split`：对任一有效理论 `T`，同一图式里既有 `T` 看得见其“永不完成”的实例，
  也有 `T` 看不见的实例（对角过程）——区别不在图式，而在过程是否把 `T` 自己的接受接口当作输入。
-/

namespace GodelQ

open Filter Topology Nat.Partrec

/-- ω 追问：每个有限阶段同一个问题。 -/
structure OmegaQuestion where
  done : ℕ → Prop

namespace OmegaQuestion

def Done (q : OmegaQuestion) : Prop := ∃ n, q.done n

def Never (q : OmegaQuestion) : Prop := ∀ n, ¬ q.done n

theorem never_iff (q : OmegaQuestion) : q.Never ↔ ¬ q.Done := by
  unfold Never Done
  constructor
  · rintro h ⟨n, hn⟩; exact h n hn
  · intro h n hn; exact h ⟨n, hn⟩

/-- 完成的有限读法 P_fin 在任何永不完成的 ω 追问上都被否定：形式上完成的整体存在，
并不给出某一有限阶段的完成。 -/
theorem P_fin_refuted (q : OmegaQuestion) (hN : q.Never) (FormalDone : Prop) (hF : FormalDone) :
    ¬ (FormalDone → q.Done) := fun hP =>
  (q.never_iff.mp hN) (hP hF)

end OmegaQuestion

/-- 经典芝诺：第 `n` 步是否已到终点。 -/
noncomputable def zenoQ : OmegaQuestion := ⟨fun n => (1 : ℝ) - (1 / 2 : ℝ) ^ n = 1⟩

theorem zenoQ_never : zenoQ.Never := by
  intro n h
  have hpos : (0 : ℝ) < (1 / 2 : ℝ) ^ n := by positivity
  change (1 : ℝ) - (1 / 2 : ℝ) ^ n = 1 at h
  linarith

theorem zenoQ_formal : Tendsto (fun n => (1 : ℝ) - (1 / 2 : ℝ) ^ n) atTop (𝓝 1) := by
  have hpow := tendsto_pow_atTop_nhds_zero_of_lt_one (r := (1 / 2 : ℝ)) (by norm_num) (by norm_num)
  simpa using (tendsto_const_nhds (x := (1 : ℝ))).sub hpow

/-- 芝诺：极限为 1，而 P_fin 被否定。 -/
theorem zeno_P_fin_refuted :
    ¬ (Tendsto (fun n => (1 : ℝ) - (1 / 2 : ℝ) ^ n) atTop (𝓝 1) → zenoQ.Done) :=
  zenoQ.P_fin_refuted zenoQ_never _ zenoQ_formal

/-- 过程的停机追问。 -/
def processQ (d : Process) : OmegaQuestion := ⟨DoneBy d⟩

theorem processQ_done_iff (d : Process) : (processQ d).Done ↔ Done d :=
  (done_iff_exists_stage d).symm

/-- 哥德尔–芝诺跑者：它的站住追问永不完成，恰好当它到达。 -/
theorem processQ_never_iff_arrives (d : Process) : (processQ d).Never ↔ Arrives d := by
  rw [OmegaQuestion.never_iff, processQ_done_iff, arrives_iff]

/-- H0：HoTT 宇宙上的逐层追问，以参数接入。 -/
def h0Q (settled : ℕ → Prop) : OmegaQuestion := ⟨settled⟩

/-- H0：宇宙“一次给出”（形式上完成的整体）不给出某一层的落定——在 C-78 的
“每一问都答否”之下，P_fin 被否定。 -/
theorem h0_P_fin_refuted (settled : ℕ → Prop) (never : ∀ n, ¬ settled n)
    (UniverseGiven : Prop) (hU : UniverseGiven) : ¬ (UniverseGiven → (h0Q settled).Done) :=
  (h0Q settled).P_fin_refuted never UniverseGiven hU

/-- 可观察性的分界：对任一有效理论 `T`，若 `T` 已确认某个 `e₀` 永不停机，则同一图式中
`processQ e₀` 是 `T` 看得见其永不完成的实例；同时存在 `T` 看不见其永不完成的实例。 -/
theorem observability_split (T : EffectiveTheory) (e₀ : Process) (h₀ : T.provesNever e₀) :
    ((processQ e₀).Never ∧ T.provesNever e₀) ∧
      ∃ d, (processQ d).Never ∧ ¬ T.provesNever d ∧ ∀ k, T.provesNotYet d k := by
  refine ⟨⟨?_, h₀⟩, ?_⟩
  · exact (OmegaQuestion.never_iff _).mpr (by rw [processQ_done_iff]; exact T.never_sound e₀ h₀)
  · obtain ⟨d, hnd, hna, hall, _⟩ := T.godel_I_process_form
    exact ⟨d, (OmegaQuestion.never_iff _).mpr (by rw [processQ_done_iff]; exact hnd), hna, hall⟩

/-- 具体分界：`toyTheory` 看得见经典芝诺跑者的永不站住，却看不见某个对角跑者的。 -/
theorem toy_observability_split :
    ((processQ (Code.rfind' Code.succ)).Never ∧ toyTheory.provesNever (Code.rfind' Code.succ)) ∧
      ∃ d, (processQ d).Never ∧ ¬ toyTheory.provesNever d ∧ ∀ k, toyTheory.provesNotYet d k :=
  observability_split toyTheory _ rfl

end GodelQ

#print axioms GodelQ.OmegaQuestion.P_fin_refuted
#print axioms GodelQ.zenoQ_never
#print axioms GodelQ.zenoQ_formal
#print axioms GodelQ.zeno_P_fin_refuted
#print axioms GodelQ.processQ_never_iff_arrives
#print axioms GodelQ.h0_P_fin_refuted
#print axioms GodelQ.observability_split
#print axioms GodelQ.toy_observability_split
