import GodelQ.C6Review
import GodelQ.Zeno.Runners

/-!
# CG-007 · W7（三）：P 的两侧——语义的 P₁ 与证明论的 ω 完成规则

研究发起人【原话】（十三条 [6]，KC-000068）：“而ZFC-1中的P之所以是所谓的“数学幻觉”，本质上是反现实的，是不可计算的”；
“设ZFC-1=ZFC+A，则ZFC-1=ZFC+P”。

GPT 各线给 P 的语义定义：dev-04 #4，P = 无桥完成代换；dev-08 #91，P₀ 是“改写完成之后仍称为解决”，P₁ 才是强跳跃
Done_formal → Done_origin。CG-005 的证明论 P 是 ω 完成规则 `OmegaClosed`（C-90）。此前二者的关系只是解释
（Targets Ⅲ-2、G-3）。本文件把它们形式地接起来。

**抽象层**：一族任务；形式完成 F（标准解的判词）；原完成 O（原过程完成）；接受集 Acc（宣布“已完成”的那些）。
* `P1Rule Acc F`：P₁ 作为接受规则——凡形式完成，都接受为已完成。
* `OriginSound Acc O`：接受即宣布原完成（强跳跃所声称的）；`FormalSound Acc F`：接受只在形式完成时发生。
* `semantic_side_refuted`（反现实）：只要有一个“形式完成而原过程没完成”的实例，统一接受形式完成就不能同时宣称原完成。
* `computational_side`（不可计算）：统一接受形式完成、又只接受形式完成，则接受集就是 F；F 不可枚举时，接受集不可枚举。

两侧落在两个不同的特征上：反现实来自“跳跃”（把形式完成说成原完成），一个稠密实例就够；不可计算来自“统一”
（对整族任务一律接受），与是否宣称原完成无关。

**实例**：
* 实数轴：F = 极限意义到达 x，O = 有限阶段取到 x。语义 P₁ 恰在孤立点成立（`semanticP1_iff_isolated`），所以在 ℝ 的
  每一点都不成立；量子化格点上成立（正控制）。
* 跑者族（C-91）：F = `Arrives`，O = 有限阶段到 1（`ReachesEnd`）。F 恰是永不停机，不可枚举。
* 理论：`LooseRunnerTheory`（不要求有效性）。
  - `A_iff_P`：在 Δ0 完全、且“尚未完成”句可靠时，A（把 P₁ 当接受规则）与 ω 完成规则 P 等价——这是
    “ZFC+A = ZFC+P”作为闭包条件的形式；
  - `completionSubstitution_iff_omegaClosed`：跑者形式的“无桥完成代换”（每一有限阶段都确认尚未完成，就接受极限完成）
    恰是 ω 完成规则；
  - 有效理论两样都没有：一条经魔鬼交易（C-90），一条经 `computational_side`（只用停机不可枚举，不用对角点）；
  - 真值理论两样都有，但不可枚举（P 可一致，不可计算）。
-/

namespace GodelQ.PTwoSides

open Filter Topology GodelQ.Zeno GodelQ.C6

section abstract

variable {X : Type*}

/-- P₁ 作为接受规则：凡形式完成，都接受为已完成。 -/
def P1Rule (Acc F : X → Prop) : Prop := ∀ x, F x → Acc x

/-- 接受即宣布原完成。 -/
def OriginSound (Acc O : X → Prop) : Prop := ∀ x, Acc x → O x

/-- 接受只在形式完成时发生。 -/
def FormalSound (Acc F : X → Prop) : Prop := ∀ x, Acc x → F x

/-- 语义的 P₁：形式完成蕴含原完成。 -/
def SemanticP1 (F O : X → Prop) : Prop := ∀ x, F x → O x

theorem semantic_side (Acc F O : X → Prop) (hr : P1Rule Acc F) (ho : OriginSound Acc O) :
    SemanticP1 F O := fun x h => ho x (hr x h)

/-- **反现实**：有一个形式完成而原过程没完成的实例，就不存在既统一接受形式完成、又宣称原完成的接受集。 -/
theorem semantic_side_refuted (F O : X → Prop) (hx : ∃ x, F x ∧ ¬ O x) :
    ¬ ∃ Acc : X → Prop, P1Rule Acc F ∧ OriginSound Acc O := by
  rintro ⟨Acc, hr, ho⟩
  obtain ⟨x, hF, hO⟩ := hx
  exact hO (semantic_side Acc F O hr ho x hF)

/-- P₀ 控制：公开换题（接受形式完成，并只当作形式完成）总是一致的——接受集取 F 本身。 -/
theorem p0_consistent (F : X → Prop) : ∃ Acc : X → Prop, P1Rule Acc F ∧ FormalSound Acc F :=
  ⟨F, fun _ h => h, fun _ h => h⟩

end abstract

section effective

variable {X : Type} [Primcodable X]

/-- **不可计算**：统一接受形式完成、又只接受形式完成，则接受集就是 F；F 不可枚举时接受集不可枚举。 -/
theorem computational_side (Acc F : X → Prop) (hr : P1Rule Acc F) (hs : FormalSound Acc F)
    (hF : ¬ REPred F) : ¬ REPred Acc := fun hA => hF (hA.of_eq fun x => ⟨hs x, hr x⟩)

end effective

/-! ## 实例一：实数轴（稠密）与格点（量子化） -/

/-- 终点 x 处的语义 P₁ 恰在 x 孤立时成立（W2 的归因定理）。 -/
theorem semanticP1_iff_isolated {Y : Type*} [TopologicalSpace Y] [FirstCountableTopology Y] (x : Y) :
    SemanticP1 (fun s : ℕ → Y => ArrivesAt s x) (fun s => AttainsAt s x) ↔ Isolated x :=
  attains_iff_isolated x

/-- ℝ 的每一点上语义 P₁ 都不成立。 -/
theorem semanticP1_false_real (x : ℝ) :
    ¬ SemanticP1 (fun s : ℕ → ℝ => ArrivesAt s x) (fun s => AttainsAt s x) := fun h =>
  real_not_isolated x ((semanticP1_iff_isolated x).mp h)

/-- ℝ 上反现实：芝诺式过程 `zenoSeq x` 极限意义到达 x，却在每个有限阶段都没到。 -/
theorem real_p1_refuted (x : ℝ) :
    ¬ ∃ Acc : (ℕ → ℝ) → Prop, P1Rule Acc (fun s => ArrivesAt s x) ∧ OriginSound Acc (fun s => AttainsAt s x) :=
  semantic_side_refuted _ _ ⟨zenoSeq x, zenoSeq_arrives x, fun ⟨n, hn⟩ => zenoSeq_ne x n hn⟩

/-- 正控制：格点（粒度 2⁻ᵐ）上取值的过程，语义 P₁ 成立。 -/
theorem semanticP1_grid (m : ℕ) (L : ℝ) :
    SemanticP1 (fun s : {s : ℕ → ℝ // ∀ n, s n ∈ grid m} => ArrivesAt s.1 L) (fun s => AttainsAt s.1 L) :=
  fun s h => grid_attains s.2 h

/-- P₀ 在稠密跑者上：改写后的完成（极限意义到达 1）成立，原完成（有限阶段到 1）不成立。 -/
theorem p0_dense_runner : ArrivesAt densePos 1 ∧ ¬ AttainsAt densePos 1 :=
  ⟨densePos_arrives, densePos_not_attains⟩

/-! ## 实例二：跑者族（C-91） -/

/-- 跑者的形式完成（极限意义到达）恰是永不停机，不可枚举。 -/
theorem arrives_not_re : ¬ REPred Arrives := fun h =>
  never_done_not_re (h.of_eq fun d => arrives_iff d)

/-- 跑者族上反现实：`rfind' succ` 的跑者到达，却永远到不了 1。 -/
theorem runner_p1_refuted : ¬ ∃ Acc : Process → Prop, P1Rule Acc Arrives ∧ OriginSound Acc ReachesEnd :=
  semantic_side_refuted _ _ ⟨Nat.Partrec.Code.rfind' Nat.Partrec.Code.succ,
    (arrives_iff _).mpr rfind_succ_never, not_reachesEnd _⟩

/-- 跑者族上不可计算：统一接受到达、又只接受到达的接受集不可枚举。 -/
theorem runner_p1_not_computable (Acc : Process → Prop) (hr : P1Rule Acc Arrives)
    (hs : FormalSound Acc Arrives) : ¬ REPred Acc :=
  computational_side Acc Arrives hr hs arrives_not_re

/-- 跑者族上宣称原完成的接受集必须是空的（`ReachesEnd` 从不成立）。 -/
theorem originSound_runner_iff (Acc : Process → Prop) : OriginSound Acc ReachesEnd ↔ ∀ d, ¬ Acc d :=
  ⟨fun h d hd => not_reachesEnd d (h d hd), fun h d hd => absurd hd (h d)⟩

/-! ## 实例三：理论——A、ω 完成规则 P 与无桥完成代换 -/

/-- 不要求有效性的跑者理论：例如 𝗭𝗙𝗖 + A 或 𝗭𝗙𝗖 + P 的抽象形状。 -/
structure LooseRunnerTheory where
  provesNever : Process → Prop
  provesNotYet : Process → ℕ → Prop
  provesArrives : Process → Prop
  delta0_complete : ∀ e k, ¬ DoneBy e k → provesNotYet e k
  notYet_sound : ∀ e k, provesNotYet e k → ¬ DoneBy e k
  arrives_iff_never : ∀ d, provesArrives d ↔ provesNever d

namespace LooseRunnerTheory

variable (T : LooseRunnerTheory)

/-- A：把 P₁ 当接受规则（凡跑者到达，理论都确认它到达）。 -/
def A : Prop := P1Rule T.provesArrives Arrives

/-- ω 完成规则 P。 -/
def P : Prop := ∀ e, (∀ k, T.provesNotYet e k) → T.provesNever e

/-- 跑者形式的无桥完成代换：每一有限阶段都确认尚未完成，就接受极限完成（到达）。 -/
def CompletionSubstitution : Prop := ∀ d, (∀ k, T.provesNotYet d k) → T.provesArrives d

theorem completionSubstitution_iff_P : T.CompletionSubstitution ↔ T.P :=
  ⟨fun h e he => (T.arrives_iff_never e).mp (h e he), fun h d hd => (T.arrives_iff_never d).mpr (h d hd)⟩

/-- 理论确认每一阶段“尚未完成”，当且仅当过程确实永不完成。 -/
theorem allNotYet_iff (e : Process) : (∀ k, T.provesNotYet e k) ↔ ¬ Done e := by
  rw [done_iff_exists_stage]
  constructor
  · rintro h ⟨k, hk⟩
    exact T.notYet_sound e k (h k) hk
  · intro h k
    exact T.delta0_complete e k fun hk => h ⟨k, hk⟩

/-- **𝗭𝗙𝗖+A = 𝗭𝗙𝗖+P（闭包条件形式）**：A 与 ω 完成规则 P 等价。 -/
theorem A_iff_P : T.A ↔ T.P := by
  constructor
  · intro hA e he
    exact (T.arrives_iff_never e).mp (hA e ((arrives_iff e).mpr ((T.allNotYet_iff e).mp he)))
  · intro hP d hd
    exact (T.arrives_iff_never d).mpr (hP d ((T.allNotYet_iff d).mpr ((arrives_iff d).mp hd)))

/-- 有 A 的理论，只要它的“到达”确认不错，就不可枚举（不可计算）。 -/
theorem A_not_re (hA : T.A) (hs : FormalSound T.provesArrives Arrives) : ¬ REPred T.provesArrives :=
  runner_p1_not_computable T.provesArrives hA hs

end LooseRunnerTheory

/-- 有效理论没有 A（经魔鬼交易 C-90，即 C-94 的 `not_aGeneral`）。 -/
theorem effective_no_A (T : RunnerTheory) : ¬ P1Rule T.provesArrives Arrives := T.not_aGeneral

/-- 有效理论没有 A（第二条证明：只用跑者到达不可枚举，不用对角点）。 -/
theorem effective_no_A_turing (T : RunnerTheory) : ¬ P1Rule T.provesArrives Arrives := fun hA =>
  runner_p1_not_computable T.provesArrives hA T.arrivalObserver.sound T.arrivalObserver.re

/-- 有效理论没有跑者形式的无桥完成代换（魔鬼交易）。 -/
theorem effective_no_completionSubstitution (T : RunnerTheory) :
    ¬ ∀ d, (∀ k, T.provesNotYet d k) → T.provesArrives d := fun h =>
  T.toEffectiveTheory.devils_bargain fun e he => (T.arrives_iff_never e).mp (h e he)

/-- 真值理论（`truthTheory`，C-90 控制 2）作为不要求有效性的跑者理论。 -/
def truthRunner : LooseRunnerTheory where
  provesNever e := ¬ Done e
  provesNotYet e k := ¬ DoneBy e k
  provesArrives d := Arrives d
  delta0_complete _ _ h := h
  notYet_sound _ _ h := h
  arrives_iff_never d := arrives_iff d

/-- 正控制：真值理论有 A 与 P，“到达”确认不错，却不可枚举——P 可一致，不可计算。 -/
theorem truth_has_A_and_P :
    truthRunner.A ∧ truthRunner.P ∧ FormalSound truthRunner.provesArrives Arrives ∧
      ¬ REPred truthRunner.provesArrives := by
  have hA : truthRunner.A := fun _ h => h
  have hs : FormalSound truthRunner.provesArrives Arrives := fun _ h => h
  exact ⟨hA, (truthRunner.A_iff_P).mp hA, hs, truthRunner.A_not_re hA hs⟩

/-- 真值理论再宣称“到达即原完成”，就错了（反现实）。 -/
theorem truth_not_originSound : ¬ OriginSound truthRunner.provesArrives ReachesEnd := fun h =>
  runner_p1_refuted ⟨truthRunner.provesArrives, fun _ h => h, h⟩

/-! ## 两侧合一 -/

/-- **P 的两侧**：在跑者族上，
(1) 语义一侧：把 P₁ 当接受规则并宣称原完成，与原过程矛盾（反现实）；
(2) 计算一侧：把 P₁ 当接受规则并只接受形式完成，接受集不可枚举（不可计算）；
(3) 二者的证明论形式：对不要求有效性的跑者理论，A 恰是 ω 完成规则 P，也恰是无桥完成代换；
(4) 有效理论两样都没有；真值理论两样都有，但不可枚举。 -/
theorem two_sides :
    (¬ ∃ Acc : Process → Prop, P1Rule Acc Arrives ∧ OriginSound Acc ReachesEnd) ∧
    (∀ Acc : Process → Prop, P1Rule Acc Arrives → FormalSound Acc Arrives → ¬ REPred Acc) ∧
    (∀ T : LooseRunnerTheory, (T.A ↔ T.P) ∧ (T.CompletionSubstitution ↔ T.P)) ∧
    (∀ T : RunnerTheory, ¬ P1Rule T.provesArrives Arrives) ∧
    (truthRunner.A ∧ truthRunner.P ∧ ¬ REPred truthRunner.provesArrives) :=
  ⟨runner_p1_refuted, runner_p1_not_computable,
    fun T => ⟨T.A_iff_P, T.completionSubstitution_iff_P⟩, effective_no_A,
    ⟨truth_has_A_and_P.1, truth_has_A_and_P.2.1, truth_has_A_and_P.2.2.2⟩⟩

end GodelQ.PTwoSides

#print axioms GodelQ.PTwoSides.semantic_side_refuted
#print axioms GodelQ.PTwoSides.computational_side
#print axioms GodelQ.PTwoSides.p0_consistent
#print axioms GodelQ.PTwoSides.semanticP1_iff_isolated
#print axioms GodelQ.PTwoSides.semanticP1_false_real
#print axioms GodelQ.PTwoSides.real_p1_refuted
#print axioms GodelQ.PTwoSides.semanticP1_grid
#print axioms GodelQ.PTwoSides.p0_dense_runner
#print axioms GodelQ.PTwoSides.arrives_not_re
#print axioms GodelQ.PTwoSides.runner_p1_refuted
#print axioms GodelQ.PTwoSides.runner_p1_not_computable
#print axioms GodelQ.PTwoSides.originSound_runner_iff
#print axioms GodelQ.PTwoSides.LooseRunnerTheory.A_iff_P
#print axioms GodelQ.PTwoSides.LooseRunnerTheory.completionSubstitution_iff_P
#print axioms GodelQ.PTwoSides.LooseRunnerTheory.A_not_re
#print axioms GodelQ.PTwoSides.effective_no_A
#print axioms GodelQ.PTwoSides.effective_no_A_turing
#print axioms GodelQ.PTwoSides.effective_no_completionSubstitution
#print axioms GodelQ.PTwoSides.truth_has_A_and_P
#print axioms GodelQ.PTwoSides.truth_not_originSound
#print axioms GodelQ.PTwoSides.two_sides
