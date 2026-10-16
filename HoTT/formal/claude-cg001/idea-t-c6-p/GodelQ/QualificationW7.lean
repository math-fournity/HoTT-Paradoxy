import GodelQ.IdeaT
import GodelQ.PTwoSides

/-!
# CG-007 · W7：命题对照（CG001-C-114、C-115、C-116）

每条命题的类型逐字写在这里，证明只引用前面文件中的定理。文件末尾的依赖检查机器核对：标为“不经对角点”的定理
不依赖本项目的对角构造（Kleene 不动点及其推论），它们落到停机不可枚举上；正控制核对检查器看得见对角依赖。
-/

namespace GodelQ.W7Qual

open Filter Topology GodelQ.Zeno GodelQ.IdeaT GodelQ.C6 GodelQ.PTwoSides
open FFL FFL.FirstOrder FFL.FirstOrder.Arithmetic FFL.FirstOrder.SetTheory
open scoped FFL.FirstOrder.Arithmetic
open GodelQ.ZFCNum GodelQ.ZFCEff

/-- **CG001-C-114（想法 T 的一般形式：观察力不完备的两种形式与脚手架；AI 的形式化提案）**：
(1) 形式一（维度缺失）：接口压平了维度上的差别，则经该接口的可靠、完备观察者不存在（不论可不可计算）；
(2) 形式二（维度在、观察力不完备）：维度不可枚举，则每个可靠、可枚举的观察者漏掉的点不可枚举、无穷，
    它可以被严格加细，加细之后仍有漏点；
(3) 脚手架：存在经接口的可靠、完备、可枚举的观察者 ⟺ 维度在接口的纤维上恒定，并且维度可枚举；
(4) 两种形式不同：停机维度经恒等接口纤维恒定，完备可枚举的观察者仍不存在；
(5) 𝗭𝗙𝗖 上的形式二：𝗭𝗙𝗖 证明的“永不停机”漏掉的过程不可枚举、无穷；
(6) 芝诺的极限接口上的形式一：只交出极限值的接口上，判“在某个有限阶段取到”的可靠、完备观察者不存在。 -/
theorem qual_C114 :
    (∀ (X Y : Type) (π : X → Y) (D : X → Prop), (∃ x₁ x₂, π x₁ = π x₂ ∧ D x₁ ∧ ¬ D x₂) →
      ¬ ∃ A : Y → Prop, Sound π A D ∧ Complete π A D) ∧
    (∀ (X : Type) [Primcodable X] (D : X → Prop), ¬ REPred D →
      ∀ A : X → Prop, REPred A → (∀ x, A x → D x) →
        ¬ REPred (· ∈ {x | D x ∧ ¬ A x}) ∧ {x | D x ∧ ¬ A x}.Infinite ∧
        ∃ A' : X → Prop, REPred A' ∧ (∀ x, A' x → D x) ∧ (∀ x, A x → A' x) ∧
          (∃ x, A' x ∧ ¬ A x) ∧ {x | D x ∧ ¬ A' x}.Nonempty) ∧
    (∀ (X Y : Type) [Primcodable X] (π : X → Y) (D : X → Prop),
      (∃ A : Y → Prop, Sound π A D ∧ Complete π A D ∧ REPred (fun x => A (π x))) ↔
        (FiberConstant π D ∧ REPred D)) ∧
    (FiberConstant (id : Process → Process) (fun e => ¬ Done e) ∧
      ¬ ∃ A : Process → Prop, Sound id A (fun e => ¬ Done e) ∧ Complete id A (fun e => ¬ Done e) ∧
        REPred (fun x => A (id x))) ∧
    (¬ REPred (· ∈ {x | ¬ Done x ∧ ¬ 𝗭𝗙𝗖 ⊢ neverS ΦH (Encodable.encode x)}) ∧
      {x | ¬ Done x ∧ ¬ 𝗭𝗙𝗖 ⊢ neverS ΦH (Encodable.encode x)}.Infinite) ∧
    (¬ ∃ A : ℝ → Prop,
      Sound (fun s : ℕ → ℝ => Filter.limUnder Filter.atTop s) A
        (fun s => AttainsAt s (Filter.limUnder Filter.atTop s)) ∧
      Complete (fun s : ℕ → ℝ => Filter.limUnder Filter.atTop s) A
        (fun s => AttainsAt s (Filter.limUnder Filter.atTop s))) :=
  ⟨fun _ _ π D h => form_one_dimension_missing π D h,
   fun _ _ D hD A hA hs => form_two_observation_incomplete D hD A hA hs,
   fun _ _ _ π D => scaffold π D,
   two_forms_differ, zfc_form_two, zeno_form_one⟩

/-- **CG001-C-115（C6：元理论对标准解的审查力；定义是 AI 提案，责任的来源是研究发起人 KC-000065）**：
(1) 标准解在跑者 d 上不充分（极限说到了、原过程没到）恰是 d 永不停机；
(2) 有效的审查（证明“不充分”可枚举、所证不错）都不完备；
(3) 正控制：去掉有效性，照真值裁决的审查可靠且完备；
(4) 𝗭𝗙𝗖：有一个跑者，标准解对它确实不充分，𝗭𝗙𝗖 却既证明不了它停机（充分），也证明不了它永不停机（不充分）；
(5) 不论用哪个 ℒₛₑₜ 公式 Φ 写“标准解在 d 上出错”，只要 𝗭𝗙𝗖 不错证它，标准解出错而 𝗭𝗙𝗖 证明不了的跑者
    有无穷多个，并且列不全。 -/
theorem qual_C115 :
    (∀ d : Process, ¬ Adequate d ↔ ¬ Done d) ∧
    (∀ R : Review, ¬ R.Complete) ∧
    (∃ pa pi : Process → Prop, (∀ d, pa d → Adequate d) ∧ (∀ d, pi d → ¬ Adequate d) ∧
      ∀ d, pa d ∨ pi d) ∧
    (∃ d : Process, ¬ Adequate d ∧ ¬ 𝗭𝗙𝗖 ⊢ haltsS ΦH (Encodable.encode d) ∧
      ¬ 𝗭𝗙𝗖 ⊢ neverS ΦH (Encodable.encode d)) ∧
    (∀ Φ : SetTheorySemisentence 1,
      (∀ d : Process, 𝗭𝗙𝗖 ⊢ neverS Φ (Encodable.encode d) → ¬ Adequate d) →
      {d : Process | ¬ Adequate d ∧ 𝗭𝗙𝗖 ⊬ neverS Φ (Encodable.encode d)}.Infinite ∧
      ¬ REPred (· ∈ {d : Process | ¬ Adequate d ∧ 𝗭𝗙𝗖 ⊬ neverS Φ (Encodable.encode d)})) := by
  refine ⟨inadequate_iff, no_complete_review, truth_review_complete, ?_,
    fun Φ h => zfc_cannot_criticize Φ h⟩
  obtain ⟨d, h1, h2, h3⟩ := zfc_review_gap
  exact ⟨d, h1, h2, h3⟩

/-- **CG001-C-116（P 的两侧：语义的 P₁ 与证明论的 ω 完成规则）**：
(1) 反现实：有一个“形式完成而原过程没完成”的实例，就不存在既统一接受形式完成、又宣称原完成的接受集；
(2) 不可计算：统一接受形式完成、又只接受形式完成，形式完成不可枚举时接受集不可枚举；
(3) ℝ 的每一点上语义 P₁ 都不成立；格点上它成立（正控制）；P₀：稠密跑者极限意义到达 1，却没在有限阶段到 1；
(4) 跑者族：(1)(2) 的实例；对不要求有效性的跑者理论，A（P₁ 作为接受规则）恰是 ω 完成规则 P，也恰是无桥完成代换；
    有效理论没有 A；真值理论有 A 与 P，却不可枚举。 -/
theorem qual_C116 :
    (∀ (X : Type) (F O : X → Prop), (∃ x, F x ∧ ¬ O x) →
      ¬ ∃ Acc : X → Prop, P1Rule Acc F ∧ OriginSound Acc O) ∧
    (∀ (X : Type) [Primcodable X] (Acc F : X → Prop), P1Rule Acc F → FormalSound Acc F →
      ¬ REPred F → ¬ REPred Acc) ∧
    ((∀ x : ℝ, ¬ SemanticP1 (fun s : ℕ → ℝ => ArrivesAt s x) (fun s => AttainsAt s x)) ∧
      (∀ (m : ℕ) (L : ℝ), SemanticP1 (fun s : {s : ℕ → ℝ // ∀ n, s n ∈ grid m} => ArrivesAt s.1 L)
        (fun s => AttainsAt s.1 L)) ∧
      (ArrivesAt densePos 1 ∧ ¬ AttainsAt densePos 1)) ∧
    ((¬ ∃ Acc : Process → Prop, P1Rule Acc Arrives ∧ OriginSound Acc ReachesEnd) ∧
      (∀ Acc : Process → Prop, P1Rule Acc Arrives → FormalSound Acc Arrives → ¬ REPred Acc) ∧
      (∀ T : LooseRunnerTheory, (T.A ↔ T.P) ∧ (T.CompletionSubstitution ↔ T.P)) ∧
      (∀ T : RunnerTheory, ¬ P1Rule T.provesArrives Arrives) ∧
      (truthRunner.A ∧ truthRunner.P ∧ ¬ REPred truthRunner.provesArrives)) :=
  ⟨fun _ F O h => semantic_side_refuted F O h,
   fun _ _ Acc F hr hs hF => computational_side Acc F hr hs hF,
   ⟨semanticP1_false_real, semanticP1_grid, p0_dense_runner⟩,
   two_sides⟩

end GodelQ.W7Qual

/-! ## 依赖检查：标为“不经对角点”的定理不依赖本项目的对角构造 -/

open Lean Elab Command in
run_cmd do
  let env ← getEnv
  let diagonal : List Name :=
    [``GodelQ.diagonal_fixed_point, ``GodelQ.diagonal_escape, ``GodelQ.no_complete_never_observer,
     ``GodelQ.complete_observer_not_re, ``GodelQ.tower_step, ``GodelQ.EffectiveTheory.godel_I_process_form,
     ``GodelQ.EffectiveTheory.not_completeForNever, ``GodelQ.EffectiveTheory.devils_bargain,
     ``GodelQ.ZFCEff.godel_I_process_form_zfc, ``GodelQ.ZFCSound.godel_I_process_form_zfc_full]
  let avoid : List Name :=
    [``GodelQ.IdeaT.form_one_dimension_missing, ``GodelQ.IdeaT.form_two_observation_incomplete,
     ``GodelQ.IdeaT.scaffold, ``GodelQ.IdeaT.two_forms_differ, ``GodelQ.IdeaT.halting_form_two,
     ``GodelQ.IdeaT.zfc_form_two, ``GodelQ.IdeaT.zeno_form_one,
     ``GodelQ.C6.no_complete_review, ``GodelQ.C6.zfc_review_gap, ``GodelQ.C6.zfc_review_incomplete,
     ``GodelQ.C6.zfc_cannot_criticize,
     ``GodelQ.PTwoSides.semantic_side_refuted, ``GodelQ.PTwoSides.computational_side,
     ``GodelQ.PTwoSides.real_p1_refuted, ``GodelQ.PTwoSides.runner_p1_refuted,
     ``GodelQ.PTwoSides.runner_p1_not_computable, ``GodelQ.PTwoSides.LooseRunnerTheory.A_iff_P,
     ``GodelQ.PTwoSides.effective_no_A_turing, ``GodelQ.PTwoSides.truth_has_A_and_P,
     ``GodelQ.W7Qual.qual_C114, ``GodelQ.W7Qual.qual_C115]
  let viaHalting : List Name :=
    [``GodelQ.IdeaT.two_forms_differ, ``GodelQ.IdeaT.zfc_form_two, ``GodelQ.C6.no_complete_review,
     ``GodelQ.C6.zfc_review_gap, ``GodelQ.C6.zfc_cannot_criticize,
     ``GodelQ.PTwoSides.runner_p1_not_computable, ``GodelQ.PTwoSides.effective_no_A_turing]
  for r in avoid do
    if GodelQ.reaches env r diagonal then
      throwError m!"{r} depends on a GodelQ diagonal declaration"
  for r in viaHalting do
    unless GodelQ.reaches env r [``ComputablePred.halting_problem_not_re] do
      throwError m!"{r} does not go through the halting theorem"
  -- 正控制：经 C-94 的 `not_aGeneral` 的那条证明确实到达对角点；C-116 的合取式因此也到达。
  unless GodelQ.reaches env ``GodelQ.PTwoSides.effective_no_A [``GodelQ.diagonal_fixed_point] do
    throwError "checker failed its positive control"
  unless GodelQ.reaches env ``GodelQ.W7Qual.qual_C116 [``GodelQ.diagonal_fixed_point] do
    throwError "expected qual_C116 to include the diagonal route (effective_no_A)"
  logInfo m!"W7 dependency check: {avoid.length} theorems avoid all {diagonal.length} GodelQ diagonal declarations; {viaHalting.length} of them go through ComputablePred.halting_problem_not_re; positive controls passed (effective_no_A and qual_C116 reach diagonal_fixed_point)."

#print axioms GodelQ.W7Qual.qual_C114
#print axioms GodelQ.W7Qual.qual_C115
#print axioms GodelQ.W7Qual.qual_C116
