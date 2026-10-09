import GodelQ.EffectiveTheory
import Mathlib.Analysis.SpecificLimits.Basic
import Mathlib.Topology.Order.MonotoneConvergence

/-!
# CG-005 · 哥德尔–芝诺跑者

芝诺的跑者每一步走完剩下路程的一半。这里的跑者多了一条规矩：它在第 `n` 步前查看一个过程
`d` 是否已在 `n` 步之内停机；若已停机，跑者就此站住，否则继续减半。

* `position_lt_one`：任何有限时刻，跑者都还没到终点；
* `limit_exists`：位置序列单调有界，极限一定存在（“完成的整体”总是有的）；
* `arrives_iff`：跑者跑到终点（极限为 1）恰好当 `d` 永不停机；
* `restores_iff_arrives`：同一构造的圆环读法——两端的间隙收拢为零，恰好当跑者到达；
* `goedel_zeno_runner`（C-91）：对任一可枚举且可靠的“到达”接受者，都有一个跑者确实到达，
  该接受者却确认不了；并且“跑者到达”恰好当“接受者不确认它到达”——哥德尔句化身为芝诺跑者；
* `zeno_control`：当 `d` 是一个确定永不停机的过程时，跑者就是经典芝诺序列 `1 - (1/2)^n`，
  其到达可被确认（平凡芝诺这一个具体实例确实被极限理论解决）；
* `RunnerTheory`：理论证明“跑者到达 ⟺ d 永不停机”时，A_general（理论确认每一个到达的芝诺式
  跑者）恰好等价于 Q 完备；有效、一致、Σ1/Δ0 完全的理论没有 A_general；
* `zfc1_dichotomy`：满足 A_general 的 Σ1/Δ0 完全理论，要么不可枚举，要么不一致。
-/

namespace GodelQ

open Filter Topology Nat.Partrec

/-- 剩余路程：从 1 开始，每一步在过程 `d` 尚未停机时减半，停机后不再变化。 -/
noncomputable def remaining (d : Process) : ℕ → ℝ
  | 0 => 1
  | n + 1 => if DoneBy d n then remaining d n else remaining d n / 2

/-- 跑者的位置。 -/
noncomputable def position (d : Process) (n : ℕ) : ℝ := 1 - remaining d n

/-- 到达：位置序列趋于终点 1。 -/
def Arrives (d : Process) : Prop := Tendsto (position d) atTop (𝓝 1)

/-- 圆环读法：两端之间的间隙收拢为 0（复原）。 -/
def Restores (d : Process) : Prop := Tendsto (remaining d) atTop (𝓝 0)

theorem remaining_pos (d : Process) : ∀ n, 0 < remaining d n
  | 0 => by simp [remaining]
  | n + 1 => by
      have ih := remaining_pos d n
      simp only [remaining]
      split_ifs
      · exact ih
      · exact half_pos ih

theorem remaining_succ_le (d : Process) (n : ℕ) : remaining d (n + 1) ≤ remaining d n := by
  have ih := remaining_pos d n
  simp only [remaining]
  split_ifs
  · exact le_rfl
  · linarith

theorem remaining_antitone (d : Process) : Antitone (remaining d) :=
  antitone_nat_of_succ_le (remaining_succ_le d)

theorem remaining_le_one (d : Process) (n : ℕ) : remaining d n ≤ 1 := by
  have := remaining_antitone d (Nat.zero_le n)
  simpa [remaining] using this

/-- 任何有限时刻，跑者都还没到终点。 -/
theorem position_lt_one (d : Process) (n : ℕ) : position d n < 1 := by
  unfold position; linarith [remaining_pos d n]

theorem position_monotone (d : Process) : Monotone (position d) := fun a b h => by
  unfold position; linarith [remaining_antitone d h]

/-- “完成的整体”总是有的：位置序列的极限存在。 -/
theorem limit_exists (d : Process) : ∃ L, Tendsto (position d) atTop (𝓝 L) :=
  ⟨_, tendsto_atTop_ciSup (position_monotone d)
    ⟨1, by rintro _ ⟨n, rfl⟩; exact (position_lt_one d n).le⟩⟩

theorem remaining_of_never (d : Process) (h : ¬ Done d) : ∀ n, remaining d n = (1 / 2 : ℝ) ^ n
  | 0 => by simp [remaining]
  | n + 1 => by
      have hn : ¬ DoneBy d n := fun hk => h ((done_iff_exists_stage d).mpr ⟨n, hk⟩)
      simp only [remaining, hn, ↓reduceIte, remaining_of_never d h n, pow_succ]
      ring

theorem remaining_frozen (d : Process) (k : ℕ) (hk : DoneBy d k) :
    ∀ n, remaining d (k + n) = remaining d k
  | 0 => rfl
  | n + 1 => by
      have hkn : DoneBy d (k + n) := doneBy_mono (Nat.le_add_right k n) hk
      show remaining d (k + n + 1) = remaining d k
      simp only [remaining, hkn, ↓reduceIte]
      exact remaining_frozen d k hk n

/-- 跑者到达，恰好当过程 `d` 永不停机。 -/
theorem arrives_iff (d : Process) : Arrives d ↔ ¬ Done d := by
  constructor
  · intro harr hd
    obtain ⟨k, hk⟩ := (done_iff_exists_stage d).mp hd
    have hconst : ∀ᶠ n in atTop, (1 - remaining d k) = position d n := by
      filter_upwards [eventually_ge_atTop k] with n hn
      obtain ⟨m, rfl⟩ := Nat.exists_eq_add_of_le hn
      simp [position, remaining_frozen d k hk m]
    have hlim : Tendsto (position d) atTop (𝓝 (1 - remaining d k)) :=
      tendsto_const_nhds.congr' hconst
    have := tendsto_nhds_unique harr hlim
    linarith [remaining_pos d k]
  · intro h
    have hr : remaining d = fun n => (1 / 2 : ℝ) ^ n := funext (remaining_of_never d h)
    have hpow := tendsto_pow_atTop_nhds_zero_of_lt_one (r := (1 / 2 : ℝ)) (by norm_num) (by norm_num)
    have : Tendsto (fun n => (1 : ℝ) - (1 / 2 : ℝ) ^ n) atTop (𝓝 (1 - 0)) :=
      tendsto_const_nhds.sub hpow
    unfold Arrives position
    rw [hr]
    simpa using this

/-- 圆环读法与芝诺读法是同一回事：间隙收拢恰好当跑者到达。 -/
theorem restores_iff_arrives (d : Process) : Restores d ↔ Arrives d := by
  unfold Restores Arrives position
  constructor
  · intro h
    have := (tendsto_const_nhds (x := (1 : ℝ))).sub h
    simpa using this
  · intro h
    have := (tendsto_const_nhds (x := (1 : ℝ))).sub h
    have hfun : (fun n => (1 : ℝ) - (1 - remaining d n)) = remaining d := by
      funext n; ring
    rw [hfun] at this
    simpa using this

/-- 一个“到达”接受者：可枚举，且只确认确实到达的跑者。 -/
structure ArrivalObserver where
  accepts : Process → Prop
  re : REPred accepts
  sound : ∀ d, accepts d → Arrives d

/-- 到达接受者就是永不完成观察者。 -/
def ArrivalObserver.toNever (O : ArrivalObserver) : NeverObserver :=
  ⟨O.accepts, O.re, fun d h => (arrives_iff d).mp (O.sound d h)⟩

/-- C-91：哥德尔–芝诺跑者。 -/
theorem goedel_zeno_runner (O : ArrivalObserver) :
    ∃ d : Process, Arrives d ∧ ¬ O.accepts d ∧ (∀ n, position d n < 1) ∧
      (∃ L, Tendsto (position d) atTop (𝓝 L)) ∧ (Arrives d ↔ ¬ O.accepts d) := by
  obtain ⟨d, hnd, hna, hiff⟩ := diagonal_escape O.toNever
  refine ⟨d, (arrives_iff d).mpr hnd, hna, position_lt_one d, limit_exists d, ?_⟩
  rw [arrives_iff]
  exact not_congr hiff

/-- 平凡芝诺控制：对确定永不停机的过程，跑者就是经典芝诺序列，且到达。 -/
theorem zeno_control (d : Process) (h : ¬ Done d) :
    position d = (fun n => 1 - (1 / 2 : ℝ) ^ n) ∧ Arrives d := by
  refine ⟨?_, (arrives_iff d).mpr h⟩
  funext n
  simp [position, remaining_of_never d h n]

/-- 平凡芝诺控制（具体）：`rfind' succ` 驱动的跑者就是经典芝诺序列，并且具体理论
`toyTheory` 确认它永不停机——这一个芝诺跑者的到达是看得见的。 -/
theorem zeno_control_concrete :
    position (Code.rfind' Code.succ) = (fun n => 1 - (1 / 2 : ℝ) ^ n) ∧
      Arrives (Code.rfind' Code.succ) ∧ toyTheory.provesNever (Code.rfind' Code.succ) :=
  ⟨(zeno_control _ rfind_succ_never).1, (zeno_control _ rfind_succ_never).2, rfl⟩

/-- 带“到达”陈述的有效理论：理论证明“跑者到达 ⟺ d 永不停机”（它形式化了上面的分析）。 -/
structure RunnerTheory extends EffectiveTheory where
  provesArrives : Process → Prop
  arrives_iff_never : ∀ d, provesArrives d ↔ provesNever d

namespace RunnerTheory

variable (T : RunnerTheory)

/-- A_general：理论确认每一个确实到达的芝诺式跑者的到达——
“极限理论解决芝诺式问题”作为一般方法的主张。 -/
def AGeneral : Prop := ∀ d, Arrives d → T.provesArrives d

/-- A_general 恰好等价于 Q 完备（理论看得见每一个“永不完成”）。 -/
theorem aGeneral_iff_complete : T.AGeneral ↔ T.toEffectiveTheory.CompleteForNever := by
  constructor
  · intro hA e he
    exact (T.arrives_iff_never e).mp (hA e ((arrives_iff e).mpr he))
  · intro hC d hd
    exact (T.arrives_iff_never d).mpr (hC d ((arrives_iff d).mp hd))

/-- ω 完成规则 P 给出 A_general。 -/
theorem omegaClosed_imp_aGeneral (hP : T.toEffectiveTheory.OmegaClosed) : T.AGeneral :=
  (T.aGeneral_iff_complete).mpr (T.toEffectiveTheory.omegaClosed_imp_complete hP)

/-- 有效、一致、Σ1/Δ0 完全的理论没有 A_general。 -/
theorem not_aGeneral : ¬ T.AGeneral := fun hA =>
  T.toEffectiveTheory.not_completeForNever ((T.aGeneral_iff_complete).mp hA)

/-- 理论自己的“到达”确认是一个到达接受者。 -/
def arrivalObserver : ArrivalObserver where
  accepts := T.provesArrives
  re := T.re_never.of_eq (fun d => (T.arrives_iff_never d).symm)
  sound d h := (arrives_iff d).mpr (T.toEffectiveTheory.never_sound d ((T.arrives_iff_never d).mp h))

/-- 理论内的哥德尔–芝诺跑者：跑者确实到达；理论在每一刻都确认它尚未停下、确认它还没到；
理论却确认不了它到达。 -/
theorem goedel_zeno_in_theory :
    ∃ d : Process, Arrives d ∧ ¬ T.provesArrives d ∧ (∀ n, T.provesNotYet d n) ∧
      (∀ n, position d n < 1) ∧ (∃ L, Tendsto (position d) atTop (𝓝 L)) := by
  obtain ⟨d, harr, hna, hlt, hlim, _⟩ := goedel_zeno_runner T.arrivalObserver
  exact ⟨d, harr, hna, T.toEffectiveTheory.observes_every_instant d ((arrives_iff d).mp harr),
    hlt, hlim⟩

end RunnerTheory

/-- ZFC-1 二难：一个理论若证明“跑者到达 ⟺ d 永不停机”、Σ1/Δ0 完全，并且具有 A_general
（ZFC + A），那么它要么不可枚举（P 不可计算），要么不一致（P 导致矛盾）。 -/
theorem zfc1_dichotomy
    (provesHalts provesNever provesArrives : Process → Prop) (provesNotYet : Process → ℕ → Prop)
    (hlink : ∀ d, provesArrives d ↔ provesNever d)
    (hs1 : ∀ e, Done e → provesHalts e)
    (hd0 : ∀ e k, ¬ DoneBy e k → provesNotYet e k)
    (hA : ∀ d, Arrives d → provesArrives d) :
    ¬ REPred provesNever ∨ ∃ e, provesHalts e ∧ provesNever e := by
  by_cases hre : REPred provesNever
  · right
    by_contra hcon
    push Not at hcon
    let T : RunnerTheory :=
      { provesHalts := provesHalts, provesNever := provesNever, provesNotYet := provesNotYet,
        re_never := hre, sigma1_complete := hs1, delta0_complete := hd0,
        consistent := fun e a b => hcon e a b, provesArrives := provesArrives,
        arrives_iff_never := hlink }
    exact T.not_aGeneral hA
  · left; exact hre

end GodelQ

#print axioms GodelQ.position_lt_one
#print axioms GodelQ.limit_exists
#print axioms GodelQ.arrives_iff
#print axioms GodelQ.restores_iff_arrives
#print axioms GodelQ.goedel_zeno_runner
#print axioms GodelQ.zeno_control
#print axioms GodelQ.zeno_control_concrete
#print axioms GodelQ.RunnerTheory.aGeneral_iff_complete
#print axioms GodelQ.RunnerTheory.omegaClosed_imp_aGeneral
#print axioms GodelQ.RunnerTheory.not_aGeneral
#print axioms GodelQ.RunnerTheory.goedel_zeno_in_theory
#print axioms GodelQ.zfc1_dichotomy
