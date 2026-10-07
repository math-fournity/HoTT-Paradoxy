import GodelQ.OmegaQuestion
import GodelQ.ProvabilityLogic

/-!
# CG-005 · 资格检查：CG001-C-84 至 C-94 的精确命题

每条命题在这里重述为一个带名字的定理，类型逐字给出，证明直接引用包内定理；
`CLAIM.md` 引用的就是这些类型。最后打印每条命题依赖的内核公理。
-/

open GodelQ Filter Topology

/-- C-84：完成恰是某一有限阶段完成；阶段观察单调且可计算。 -/
theorem qual_C84 :
    (∀ e : Process, Done e ↔ ∃ k, DoneBy e k) ∧
    (∀ (e : Process) (k₁ k₂ : ℕ), k₁ ≤ k₂ → DoneBy e k₁ → DoneBy e k₂) ∧
    ComputablePred (fun p : Process × ℕ => DoneBy p.1 p.2) :=
  ⟨done_iff_exists_stage, fun _ _ _ h h₁ => doneBy_mono h h₁, doneBy_computable⟩

/-- C-85：Kleene–罗素对角点与对角逃逸。 -/
theorem qual_C85 :
    (∀ accepts : Process → Prop, REPred accepts → ∃ d : Process, (Done d ↔ accepts d)) ∧
    (∀ O : NeverObserver, ∃ d : Process, ¬ Done d ∧ ¬ O.accepts d ∧ (Done d ↔ O.accepts d)) :=
  ⟨diagonal_fixed_point, diagonal_escape⟩

/-- C-86：可枚举、可靠、完备不可兼得；“永不完成”不可枚举（两条独立路线）。 -/
theorem qual_C86 :
    (¬ ∃ O : NeverObserver, ∀ e, ¬ Done e → O.accepts e) ∧
    (∀ accepts : Process → Prop, (∀ e, accepts e → ¬ Done e) → (∀ e, ¬ Done e → accepts e) →
      ¬ REPred accepts) ∧
    ¬ REPred (fun e : Process => ¬ Done e) :=
  ⟨no_complete_never_observer, complete_observer_not_re, never_done_not_re⟩

/-- C-87：补丁塔的一步——严格更大的可靠观察者仍有漏点。 -/
theorem qual_C87 :
    ∀ O : NeverObserver, ∃ O' : NeverObserver, (∀ e, O.accepts e → O'.accepts e) ∧
      (∃ d, O'.accepts d ∧ ¬ O.accepts d) ∧ (∃ d', ¬ Done d' ∧ ¬ O'.accepts d') :=
  tower_step

/-- C-88：Π1 可靠；每一次完成、每一个有限时刻都看得见。 -/
theorem qual_C88 :
    ∀ T : EffectiveTheory,
      (∀ e, T.provesNever e → ¬ Done e) ∧ (∀ e, Done e → T.provesHalts e) ∧
      (∀ e, ¬ Done e → ∀ k, T.provesNotYet e k) :=
  fun T => ⟨T.never_sound, T.observes_every_completion, T.observes_every_instant⟩

/-- C-89：哥德尔第一不完备定理的过程形式（ω 形式）。 -/
theorem qual_C89 :
    ∀ T : EffectiveTheory,
      (∃ d : Process, ¬ Done d ∧ ¬ T.provesNever d ∧ (∀ k, T.provesNotYet d k) ∧
        (Done d ↔ T.provesNever d)) ∧ ¬ T.CompleteForNever :=
  fun T => ⟨T.godel_I_process_form, T.not_completeForNever⟩

/-- C-90：魔鬼交易——ω 完成规则 P 与“有效 + 一致 + Σ1/Δ0 完全”不可兼得。 -/
theorem qual_C90 :
    (∀ T : EffectiveTheory, ¬ T.OmegaClosed) ∧
    (∀ T : OmegaTheory, ¬ REPred T.provesNever) ∧
    (∀ (provesHalts provesNever : Process → Prop) (provesNotYet : Process → ℕ → Prop),
      REPred provesNever → (∀ e, Done e → provesHalts e) →
      (∀ e k, ¬ DoneBy e k → provesNotYet e k) →
      (∀ e, (∀ k, provesNotYet e k) → provesNever e) →
      ∃ e, provesHalts e ∧ provesNever e) :=
  ⟨fun T => T.devils_bargain, fun T => T.not_effective, effective_omega_inconsistent⟩

/-- C-91：哥德尔–芝诺跑者（含圆环读法与平凡芝诺控制）。 -/
theorem qual_C91 :
    (∀ O : ArrivalObserver, ∃ d : Process, Arrives d ∧ ¬ O.accepts d ∧ (∀ n, position d n < 1) ∧
      (∃ L, Tendsto (position d) atTop (𝓝 L)) ∧ (Arrives d ↔ ¬ O.accepts d)) ∧
    (∀ d : Process, Arrives d ↔ ¬ Done d) ∧
    (∀ d : Process, Restores d ↔ Arrives d) ∧
    (position (Nat.Partrec.Code.rfind' Nat.Partrec.Code.succ) = (fun n => 1 - (1 / 2 : ℝ) ^ n) ∧
      Arrives (Nat.Partrec.Code.rfind' Nat.Partrec.Code.succ) ∧
      toyTheory.provesNever (Nat.Partrec.Code.rfind' Nat.Partrec.Code.succ)) :=
  ⟨goedel_zeno_runner, arrives_iff, restores_iff_arrives, zeno_control_concrete⟩

/-- C-92：Löb、哥德尔第二不完备、自用 P 的崩塌、ZFC-1 严格更强；前提可被一致模型满足。 -/
theorem qual_C92 :
    (∀ (T : HBLTheory) (φ : T.S), T.Pr (T.imp (T.box φ) φ) → T.Pr φ) ∧
    (∀ T : HBLTheory, T.Pr T.con → T.Pr T.bot) ∧
    (∀ T : HBLTheory, ¬ T.Pr T.bot → ¬ T.Pr T.con) ∧
    (∀ (T : HBLTheory) (E : HBLExtension T), ¬ T.Pr T.bot → ∃ s, E.Pr' s ∧ ¬ T.Pr s) ∧
    (¬ trivialBoxModel.Pr trivialBoxModel.bot ∧ ¬ trivialBoxModel.Pr trivialBoxModel.con) :=
  ⟨fun T => T.loeb, fun T => T.goedel_II, fun T => T.goedel_II_consistent, extension_strict,
    ⟨trivialBoxModel_consistent, trivialBoxModel_con_unprovable⟩⟩

/-- C-93：同一个 ω 追问——P_fin 在芝诺与 H0 上被否定；可观察性的分界。 -/
theorem qual_C93 :
    (∀ q : OmegaQuestion, q.Never → ∀ FormalDone : Prop, FormalDone → ¬ (FormalDone → q.Done)) ∧
    (zenoQ.Never ∧ Tendsto (fun n => (1 : ℝ) - (1 / 2 : ℝ) ^ n) atTop (𝓝 1)) ∧
    (∀ settled : ℕ → Prop, (∀ n, ¬ settled n) → ∀ UniverseGiven : Prop, UniverseGiven →
      ¬ (UniverseGiven → (h0Q settled).Done)) ∧
    (∀ d : Process, (processQ d).Never ↔ Arrives d) ∧
    (∀ (T : EffectiveTheory) (e₀ : Process), T.provesNever e₀ →
      ((processQ e₀).Never ∧ T.provesNever e₀) ∧
      ∃ d, (processQ d).Never ∧ ¬ T.provesNever d ∧ ∀ k, T.provesNotYet d k) :=
  ⟨OmegaQuestion.P_fin_refuted, ⟨zenoQ_never, zenoQ_formal⟩, h0_P_fin_refuted,
    processQ_never_iff_arrives, observability_split⟩

/-- C-94：ZFC + A = ZFC + P 及其二难——A_general ⟺ Q 完备，P ⟹ A_general，
有效理论没有 A_general，具有 A_general 的理论要么不可枚举、要么不一致。 -/
theorem qual_C94 :
    (∀ T : RunnerTheory, T.AGeneral ↔ T.toEffectiveTheory.CompleteForNever) ∧
    (∀ T : RunnerTheory, T.toEffectiveTheory.OmegaClosed → T.AGeneral) ∧
    (∀ T : RunnerTheory, ¬ T.AGeneral) ∧
    (∀ (provesHalts provesNever provesArrives : Process → Prop) (provesNotYet : Process → ℕ → Prop),
      (∀ d, provesArrives d ↔ provesNever d) → (∀ e, Done e → provesHalts e) →
      (∀ e k, ¬ DoneBy e k → provesNotYet e k) → (∀ d, Arrives d → provesArrives d) →
      ¬ REPred provesNever ∨ ∃ e, provesHalts e ∧ provesNever e) :=
  ⟨fun T => T.aGeneral_iff_complete, fun T => T.omegaClosed_imp_aGeneral, fun T => T.not_aGeneral,
    zfc1_dichotomy⟩

#print axioms qual_C84
#print axioms qual_C85
#print axioms qual_C86
#print axioms qual_C87
#print axioms qual_C88
#print axioms qual_C89
#print axioms qual_C90
#print axioms qual_C91
#print axioms qual_C92
#print axioms qual_C93
#print axioms qual_C94
