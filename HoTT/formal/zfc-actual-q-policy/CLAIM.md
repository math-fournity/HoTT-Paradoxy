# Q／P／A／B／ZFC-1：条件性逻辑核、受控过程模型与 HoTT 反射反例

> **身份：** `CURRENT_PROJECT_FORMAL_PACKAGE / CONDITIONAL_POLICY_CONSEQUENCE_PLUS_CONTROLLED_ZENO_MODEL_PLUS_NATIVE_HOTT_COUNTEREXAMPLE / NOT_A_FORMALIZATION_OF_BARE_ZFC`。
>
> **用户原论述：** [2026-10-04 Q／P／A／B／ZFC-1 原文](../../../sources/prompts/Codex-ZFC-Q-P-A-B-ZFC1-用户原文-20261004.md)。
>
> **交付运行：** `MP-ZFC-ACTUAL-Q-POLICY-002` / [`20261004-MP-ZFC-ACTUAL-Q-POLICY-002-06`](../../verification/runs/20261004-MP-ZFC-ACTUAL-Q-POLICY-002-06/RUN.json)、`MP-ZFC-OBSERVATION-LANGUAGE-BOUNDARY-001` / [`20261004-MP-ZFC-OBSERVATION-LANGUAGE-BOUNDARY-001-01`](../../verification/runs/20261004-MP-ZFC-OBSERVATION-LANGUAGE-BOUNDARY-001-01/RUN.json)、`MP-ZFC-COMPLETION-POLICY-UNIFORMITY-001` / [`20261004-MP-ZFC-COMPLETION-POLICY-UNIFORMITY-001-01`](../../verification/runs/20261004-MP-ZFC-COMPLETION-POLICY-UNIFORMITY-001-01/RUN.json)、`MP-ZFC-UNPAID-COMPLETION-PROMOTION-001` / [`20261004-MP-ZFC-UNPAID-COMPLETION-PROMOTION-001-01`](../../verification/runs/20261004-MP-ZFC-UNPAID-COMPLETION-PROMOTION-001-01/RUN.json)、`MP-ZFC-MEMBERSHIP-LANGUAGE-INVARIANCE-001` / [`20261004-MP-ZFC-MEMBERSHIP-LANGUAGE-INVARIANCE-001-01`](../../verification/runs/20261004-MP-ZFC-MEMBERSHIP-LANGUAGE-INVARIANCE-001-01/RUN.json) 与 `MP-ZFC-ACTUAL-Q-HOTT-COUNTEREXAMPLE-001` / [`20261004-MP-ZFC-ACTUAL-Q-HOTT-COUNTEREXAMPLE-001-01`](../../verification/runs/20261004-MP-ZFC-ACTUAL-Q-HOTT-COUNTEREXAMPLE-001-01/RUN.json) 都已通过精确重放；本页仍须与 `README.md`、`REVISIONS.md`、跨 kernel 对应表共同解释，不能把条件 theorem 缩写成“ZFC 不一致”。

## 1. 用户论证被怎样忠实地拆成可检验对象

| 用户符号／主张 | 精确形式对象 | 已机器检查的范围 | 仍未支付的现实或来源义务 |
|---|---|---|---|
| `Q`：对时间／过程完成的理论观察力 | `CompletionObservable task := ∃ classify, classify (observe state) ↔ originDone state`。`QMissing` 是其否定。 | 一个明确的观察函数无法区分原完成与原未完成状态时，内核证明 `QMissing`。 | 这不是“bare ZFC 没有时间”或“ZFC 不能编码过程”；它是某个固定任务观察接口的相对性质。 |
| `Q` 的成员语言边界 | `MembershipTheory α := MembershipModel α → Prop` 不接收 `originDone`；`CompletionExpansion` 才加入这个谓词。 | 若一个成员模型满足任意此类 base theory，它可有同一 membership、却在任一指定状态对 `originDone` 相反的两个扩张。 | 这不是 ZFC 模型存在或不一致定理，也不证明实际圆环 Done 不可在 ZFC 中定义；它严格说明：未被定义／桥接的外部 Done 不能由成员语言本身替你决定。 |
| `Q` 的统一判词 | `QUniform assessment := equal full QProfile → equal completion judgment`；`O3O5Adequate` 要求 original-resolution 的 required bridge 已支付。 | 相同完整 profile + `originalResolved`／`bridgeRequired` 的异判，内核推出 `¬ QUniform`；无 bridge 的 original-resolution 推出 `¬ O3O5Adequate`。 | 这是条件性元政策 theorem；实际 Zeno、圆环和 HoTT Q 是否有同一完整 profile、相反判词，仍由来源和同一任务映射支付。 |
| `P` 的未付款反模型 | `BaseSubtheoryModel` 保留 `member/input/step/observe/formalDone`；`ProcessExpansion` 才加 `originDone`。 | 只要有一个 `formalDone` witness，就存在所有 base/subtheory 字段不变而 `originDone` 为假的 expansion；因此 base/subtheory 不能语义蕴含 `CompletionPromotion`。 | 这是泛化模型论反例，不是实际 ZFC 模型、物理过程或 Standard Solution 的来源判词。 |
| ZFC 的成员语言边界 | `MembershipFormula` 含 `=`、`∈`、`⊥`、`→`、`∀`，没有 `originDone` atom。 | 每个此类公式及其 theory 在相同 membership 的不同 Done expansion 中真值不变；同一 theory 可以有相反 Done 的扩张。 | 没有编码完整 ZFC schema；它证明语言不含 Done 时的语法—语义不变性，不证明 ZFC 无法定义具体 Done。 |
| `A`：Zeno 侧的数学完成 | `∃ state, formalDone state`。 | 受控模型有一个 `limit` formal-completion witness。 | 实际 Standard Solution 是否对用户的圆环／芝诺原任务建立了这个 `A`，由来源卡决定。 |
| 弱 `P`：数学共同体把模型结果称作“解决” | `WeakResolutionLabel`，它只能从 `formalDone` 产生 `CompletionJudgment`，不产生 `originDone`。 | 受控模型可无矛盾地把 `limit` 标为 `revisedResolved`。 | 标签是哪个真实来源、它是否声称原任务已完成。 |
| 强 `P`：所谓“数学幻觉”实际把模型完成当原过程完成 | `MathematicalIllusionP`：在其适用站点，`formalDone state → originDone state`；`PolicyScopeWitness` 是“为何政策从 Zeno 侧扩展到 HoTT 侧”的**形式占位**。 | 强 P、scope witness 与 B 同时存在时，Lean 导出 `False`。 | IEP/SEP/Norton 现在支持 Zeno-side local completion policy；它们仍不支付到用户圆环／HoTT 的范围。Lean 不能证明某文献作者承担这个范围，须由来源卡另行支付。 |
| `B`：HoTT 侧不想要的反例 | Lean 中是 `∃ state, formalDone state ∧ ¬ originDone state`；Cubical Agda 中由固定 `CompletionReflectsOriginalHalting` 的否定提供对应形状。 | Cubical Agda 内核证明：截断 Q 的 stage-one completion 不能推出原 universe Q 的有限 halt。 | 这个 Agda 命题尚未被证明等同于 Lean `B` 的实际 Zeno／HoTT 共用任务签名。 |
| `ZFC-1 = ZFC + P` | `ZFCMinusOne ZFCBase policy := ZFCBase ∧ policy.applies zeno`，即**使用模型**的显式加项。 | `ZFCOneUse` 可推出其含有的 `ZFCMinusOne`。 | 它不是 ZFC 对象语言、不是 ZFC 的保守扩张、也不是 ZFC 一致性模型。 |
| `ZFC + A = ZFC + P` | `ZFCWith ZFCBase A ↔ ZFCMinusOne ZFCBase policy`。 | 只有另给 `A ↔ AdmittedZenoP policy` 时才成立。 | “数学界承认 A 等价于接受 P”不能由叙事或 kernel 自动推出。 |

这张表保留用户原论证的因果结构，同时阻止三个偷换：把 `SOURCE_UNOBSERVED` 当成否定、把“revised resolved”当成原过程完成、把一个跨理论类比当成实际任务等价。

## 2. `MP-ZFC-ACTUAL-Q-POLICY-002` / `C-359`：Lean 4 的条件性逻辑核

[ActualQPolicy.lean](ActualQPolicy.lean) 是当前 Lean 源。它不导入 Mathlib，所有列出的定理均使用 Lean 4 core 检查；源末尾的 `#print axioms` 对每条交付定理报告“does not depend on any axioms”。当前交付收据是 `20261004-MP-ZFC-ACTUAL-Q-POLICY-002-06`：Lean 4.34.1 二进制及源文件哈希均冻结，随后重放得到完全相同的 exit/stdout/stderr。

### 2.1 机器命题

1. `observation_collision_implies_QMissing`：两个状态同一 `observe` 值而原 `originDone` 相反，足以推出该观察缺少 Q。
2. `task_equiv_transports_QMissing` 与 `same_actual_Q_transports_QMissing`：保持 `State`、`input`、`step`、`observe`、`formalDone` 和 `originDone` 的 `TaskEquiv` 是一条严格的 Q gap 运输控制。
3. `q_gap_does_not_logically_force_P`：`QMissing` **不能仅靠逻辑**生成强 P。`Q` 缺失“允许 P”必须是来源可审计的政策前提，写在 `ZFCOneUse.gapAdmitsZenoP` 中。
4. `zfcOneUse_is_ZFCMinusOne`：一个明确给出 base、Q gap、政策和 admission 的 `ZFCOneUse` 确实包含 `ZFCBase ∧ AdmittedZenoP`。
5. `zfc_plus_A_iff_ZFCMinusOne`：用户的 `ZFC + A = ZFC + P` 只有在显示的 `A ↔ admitted P` 前提下成为 theorem。
6. `zfc1_promotes_A`：在这个强政策的使用模型内，Zeno 的 `formalDone` 被提升为 `originDone`。
7. `source_scoped_P_with_B_is_inconsistent`：若 `ZFCOneUse` 中的 P 有 `PolicyScopeWitness`，且 HoTT 侧有 B，则导出 `False`。该 witness 在 Lean 内只是一个范围蕴含；要称它为“来源归属”，还必须有独立来源卡。
8. `zfc1_same_actual_Q_P_with_B_is_inconsistent`：严格 `SameActualQ` 是第 7 条的一个充分实例。
9. `zfc1_yields_A_and_conflicts_with_B`：若再有 A，内核同时给出 Zeno 侧被提升的 `originDone` 与 `False`。
10. `zfcOneUse_and_same_actual_Q_do_not_logically_force_B`：反向控制构造一个有 Q gap、已承认强 P 且有真正 `SameActualQ` 的空 formal-completion use-model，但其中 B 不成立。因此“ZFC-1 导致 B”不是纯逻辑后果；B 必须由固定 HoTT theorem 和实际任务映射另行支付。

第 7 条是对用户“欲得 A 的 P 一旦同样用于 B 就交出不想要的结果”的最强**条件性**形式化；第 8 条说明严格状态等价是其一条充分路径；第 10 条反过来证明 B 不能被该使用模型自动制造。`False` 所在的语境是证明项显式包含的 `ZFCOneUse + PolicyScopeWitness + B`，不是 `ZFC ⊢ False`。

### 2.2 `TaskEquiv` 是严格控制，来源范围是实际义务

早期草稿把同一 Q 写成来源字段 `QFingerprint` 的相等。这会允许两个同样写着 `SOURCE_UNOBSERVED` 的任务被误当成同一任务。现行源改为：

```text
SameActualQ
  := Nonempty (TaskEquiv zenoTask hottTask)

TaskEquiv preserves
  State, input, step, observe, formalDone, originDone.
```

`QEvidence` 中的 O1–O5、bridge/payment 状态仍保留，但只能说明来源证据的状态，不能代替语义等价。`TaskEquiv` 因而是最严格的反类比控制；跨领域来源不必提供状态双射，却必须提供足以实例化 `PolicyScopeWitness` 的理由，即解释为什么同一个强 P 有权从 Zeno 侧扩张到 HoTT 侧。Lean 的结构字段不包含书目、作者或解释责任；“来源归属”是来源审计对该字段的外部资格要求。当前来源分母的判词见 [P 的来源范围审计](../../../audit/20261004-ZFC-ACTUAL-Q-POLICY-SCOPE-SOURCE-DENOMINATOR.md)。

### 2.3 `MP-ZFC-OBSERVATION-LANGUAGE-BOUNDARY-001` / `C-362`：成员语言不自动决定原过程完成

[ZFCObservationLanguage.lean](ZFCObservationLanguage.lean) 机器化的是用户所说“元理论没有在这个维度上作出判断”的一个**最小、可反驳版本**。它不把 ZFC 简化成“不能谈时间”，而是先固定一个准确的语言边界：

```text
MembershipTheory α
  = MembershipModel α → Prop

CompletionExpansion α
  = 同一个 membership model + 外加的 originDone : α → Prop
```

`base_model_admits_opposite_originDone_expansions` 证明：若 `base` 是某个 membership-only theory 的模型，且给定状态 `state`，则存在两个对该 theory 同样成立、membership 完全一致的 expansion；一个令 `originDone state` 成立，另一个令它不成立。这个 theorem 的前提是**已有 base model**，所以它不构造 ZFC 模型，也不触及 ZFC 一致性。

同一文件还给出反向正控制。`CompletionSpecification` 可以从 membership model 定义一个指定的完成谓词；`CompletionBridge` 说明 expansion 的 `originDone` 恰等于这个 specification。`shared_completion_bridge_determines_originDone` 与 `shared_bridge_rejects_opposite_completion_readings` 证明：一旦同一 bridge 被支付，两个扩张不再能对完成状态异判。

这一步把 Q 的含义收紧为：**一个基础性语言／验收层若没有把原过程 Done 纳入自己的定义或桥接合同，它本身不选择这个 Done；若补入定义或 bridge，它能够选择。** 因而它支持的是“未付 bridge 的观察边界”，不是“ZFC 无法表示时间、序列或计算”。

### 2.4 `MP-ZFC-COMPLETION-POLICY-UNIFORMITY-001` / `C-363`：同一完整 Q 的异判不是统一政策

[ZFCCompletionPolicyUniformity.lean](ZFCCompletionPolicyUniformity.lean) 形式化用户最后提出的政策层逻辑。它将完整 `QProfile` 拆为 O1 表示、O2 形式完成、O3 区分两种完成、O4 同一任务 bridge、O5 元审查，以及 `requiresBridge`、`bridgePaid` 和 `originalTaskPreserved`。

其关键定理为：

```text
profile(Zeno) = profile(HoTT)
∧ judgment(Zeno) = originalResolved
∧ judgment(HoTT) = bridgeRequired
⟹ ¬ QUniform
```

另一个定理表明，若一个需要 bridge 的案例被称作 `originalResolved` 而 bridge 未支付，则它违反该模型中的 `O3O5Adequate`。反控制 `coarse_shared_Q_can_have_different_judgments` 同时证明：只共享“都需要 bridge”并不构成矛盾；一侧若真实支付 bridge、保留任务，异判可以合理。

这正好避免两种相反的误读：不能只因 Zeno 和 HoTT 都谈“完成”就宣布 ZFC 异判；也不能因为它们表面不同就忽略用户所要求的同一完整 Q 检验。当前来源状态仍是：Zeno 侧有局部 policy，圆环／HoTT 的共同 profile、policy scope 和相反 judgment 都未支付。因此 C-363 是**收尾判词的条件形式**，不是实际 ZFC 冲突已经证明。

### 2.5 `MP-ZFC-UNPAID-COMPLETION-PROMOTION-001` / `C-364`：未付 P 的保字段反模型

[ZFCUnpaidCompletionPromotion.lean](ZFCUnpaidCompletionPromotion.lean) 将 C-362 的语言边界提升到用户真正要的 `P`：base/subtheory interface 同时公开 `member`、`input`、`step`、`observe` 与 `formalDone`，但不公开 `originDone`。它定义：

```text
CompletionPromotion
  := ∀ state, formalDone(state) → originDone(state)

CompletionPromotionExtension
  := Models(base/subtheory) ∧ CompletionPromotion
```

若 base/subtheory 有某个 `formalDone` witness，`unpaid_formal_completion_has_countermodel` 构造一个保留**全部**已公开 base/subtheory 字段、仍满足同一 theory、却令该 witness 的 `originDone` 为假的 expansion；它同时否定 `CompletionPromotion`。随后的 `base_subtheory_does_not_semantically_entail_unpaid_promotion` 给出等价的全称表述：该 theory 不能仅从这些公开信息语义蕴含 P。

正控制也在同一文件中：`CompletionBridge` 加上 `FormalCompletionAdequacy` 会推出 `CompletionPromotion`。因此这个结果不说“所有 mathematical completion 都是假象”；它精确说：**没有把原过程 contract 写进 bridge 的 completion promotion 不是 base/subtheory 的后果，而是 `ZFC-1` 式额外加项。**

### 2.6 `MP-ZFC-MEMBERSHIP-LANGUAGE-INVARIANCE-001` / `C-365`：成员公式对外加 Done 的语法—语义不变性

[ZFCMembershipLanguageBoundary.lean](ZFCMembershipLanguageBoundary.lean) 进一步避免“只是接口类型不带字段”的质疑。它显式实现一段最小一阶成员语言：

```text
MembershipFormula ::= x = y | x ∈ y | ⊥ | φ → ψ | ∀ φ
```

`evalBase_invariant_under_originDone` 对每一个公式归纳证明：只要 membership relation 不变，外加 `originDone` predicate 怎样变化都不会改变公式真值。`satisfies_membership_theory_invariant_under_originDone` 将它提升到任意此类 formula theory；`membership_theory_has_opposite_originDone_expansions` 构造同一 theory 的两份相反 Done expansion。

这并未宣称“ZFC 的完整 axiom scheme 已在 Lean 中编码”。相反，它给出一个更精确的条件桥：**任何未来把 ZFC 公理编码为仅用 `=`、`∈` 的 formula theory，都会落在这条不变性定理的范围内；若要决定原过程 Done，必须加入定义、predicate 或 bridge。**

## 3. 受控 Zeno 过程模型：它证明什么，刻意不证明什么

`ActualQPolicy.lean` 还给出一个无公理的 `ZenoToyState` 控制：

```text
stage n       有限编号阶段
limit         数学模型的 formal-completion 状态
endpoint      指定原过程 endpoint 状态
```

- `zenoToyRun_is_stage` 和 `zenoToy_no_finite_stage_is_origin_done`：每个自然数编号的运行仍是 `stage n`，不是 `endpoint`。
- `zenoToy_has_formal_completion`：`limit` 满足 `formalDone`，所以 A 的形式存在。
- `zenoToy_QMissing`：`limit` 与 `endpoint` 被映到同一观察值，但原完成谓词相反。
- `zenoToy_weak_label_is_revised`：弱标签可称 `limit` 为 `revisedResolved`，而没有输送原完成。
- `zenoToy_no_unconditional_completion_bridge` 与 `zenoToy_no_admitted_strong_P`：若强 P 在此任务非真空地适用，它会在 `limit` 把 `originDone` 断言成一个没有构造子的命题，因而被内核否定。
- `endpointControl_observes_origin_completion` 和 `endpointControl_completion_bridge`：另一受控端点模型确实有可判别 endpoint 与已支付 bridge。这是正控制，防止从“有限阶段无最后项”错误推出“一切连续端点模型都不可能到达”。

这个模型只是把“模型完成、原过程完成和观测能力”分离成可运行的最小接口。它**不是**实数、极限、真实连续时间、Achilles、圆环，亦非物理运动模型。

## 4. `MP-ZFC-ACTUAL-Q-HOTT-COUNTEREXAMPLE-001` / `C-360`：Cubical Agda 的 B 控制

[HoTTCounterexample.agda](HoTTCounterexample.agda) 复用 C-358 的固定 Cubical Agda Q：

```agda
MathematicalIllusionP = CompletionReflectsOriginalHalting

coarseCompletion :
  runFor 0 (question TU judgeTU) ≡ just 1

originalCompletionFails :
  ¬ Questioning.Halts (Type ℓ-zero) judgeU

hottCounterexampleToMathematicalIllusionP :
  ¬ MathematicalIllusionP
```

这里的“强 P”是很窄的固定蕴含：**截断后的 stage-one completion 蕴含原 universe Q 有某个有限 halt witness**。`hottCounterexampleExpanded` 直接把该蕴含与两个现有 witness 合成为空类型。 [WrongHoTTCounterexample.agda](WrongHoTTCounterexample.agda) 是反向控制：伪造原 Q 的 fuel-0 halt 在 `20261004-MP-ZFC-ACTUAL-Q-HOTT-COUNTEREXAMPLE-NEG-001-01` 中准确地被 `nothing != just 1` 拒绝。

## 5. 跨 kernel 与来源边界

- [CROSS-KERNEL-MAPPING.md](CROSS-KERNEL-MAPPING.md) 说明 Lean 中的抽象 B 与 Cubical Agda 中的实际定理怎样相连，以及为什么这仍不是单一 kernel 的跨系统定理。
- [SOURCE-BOUNDARY.md](SOURCE-BOUNDARY.md) 固定当前可用的 Zeno／ZFC／Standard Solution 文本能支持什么、不能支持什么。
- [P 的来源范围审计](../../../audit/20261004-ZFC-ACTUAL-Q-POLICY-SCOPE-SOURCE-DENOMINATOR.md) 固定 `PolicyScopeWitness` 所需的来源分母及其当前缺口。
- [REVISIONS.md](REVISIONS.md) 保存这次包的预备失败、修复和哪些运行才能成为交付依据。

## 6. `MP-ZFC-ACTUAL-Q-ZENO-LIMIT-CONTROL-001` / `C-361`：实分析 A 控制

[ZenoLimitControl.lean](ZenoLimitControl.lean) 在 Lean 4.34.0 与固定 Mathlib 依赖中使用

\[
s_n = 1 - \left(\frac12\right)^n
\]

证明：

```text
FormalA                      := Tendsto s_n (𝓝 1)
StrictSequentialDone         := ∃ n : ℕ, s_n = 1
¬ (FormalA → StrictSequentialDone)
```

它还证明闭实时间区间 `Set.Icc 0 1` 的 terminal parameter 确实可取到 1。因而 C-361 同时防两种错误：把“极限”偷换成某个有限自然数编号阶段已完成，或者反过来由有限阶段无末项推出连续时间端点不可能到达。

Lean 的 `#print axioms` 对此包报告 `propext`、`Classical.choice`、`Quot.sound`；它们作为 Mathlib 经典实分析信任边界被明确保留。当前主收据为 [`20261004-MP-ZFC-ACTUAL-Q-ZENO-LIMIT-CONTROL-001-04`](../../verification/runs/20261004-MP-ZFC-ACTUAL-Q-ZENO-LIMIT-CONTROL-001-04/RUN.json)，其命令内固定了 `LEAN_PATH` 并可由通用 verifier 重放。`StrictSequentialDone` 是本包刻意设定的严格控制，**不**被归因给 Standard Solution 或数学共同体。

## 7. 禁止外推

本包没有证明以下任何一项：

1. `ZFC ⊢ False`、ZFC 不一致、或 Power Set 公理导致矛盾；
2. ZFC 不能表示时间、自然数步骤、序列、递归或计算；
3. 数学共同体实际采用了 `ZFCOneUse`、强 P 或 `A ↔ P`；
4. IEP、SEP、Norton、Bathfield 或其他来源已经对用户圆环的 `OriginDone` 作出原任务完成判词；
5. 固定 Zeno／圆环过程与固定 Cubical Agda HoTT Q 已由严格 `TaskEquiv` 连结，或有来源可支付的 `PolicyScopeWitness`；
6. 连续端点、实分析、极限理论或集合论基础本身错误；
7. “反现实”“数学真理性”或“与魔鬼交易”这类哲学结论是 proof assistant 内核可判的命题。
8. 任何实际 ZFC 模型的存在、ZFC 的一致性，或用户圆环 `OriginDone` 不能由集合论定义。
9. IEP／SEP／Norton 的 Zeno-side policy 和 fixed HoTT Q 已具有相同 `QProfile`，或已经形成 `originalResolved`／`bridgeRequired` 的实际异判。
10. `BaseSubtheoryModel` 是 ZFC、实分析、芝诺物理过程或用户圆环的完整语义模型。
11. 最小 `MembershipFormula` 已经是完整 ZFC schema 的编码或 ZFC 的一致性证明。

相反，本包给未来实际实例化一条清晰可推翻路线：若来源明确把 `Done_formal` 改写为不同的 `Done_revised`，或不能支付其 P 跨案例适用的 `PolicyScopeWitness`，则当前 `False` theorem 不能用于实际来源判词；严格 `TaskEquiv` 的失败只会阻断严格路径，不能单独否定一份可能存在的范围论证。只有强 P、可审的范围支付、实际 B 映射和版本固定来源都齐备，才可以把条件后果推进为 `ACTUAL_Q_POLICY_CONFLICT_WITH_SOURCE_BOUNDARY`。
