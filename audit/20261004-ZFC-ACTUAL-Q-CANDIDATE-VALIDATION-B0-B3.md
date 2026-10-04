# ZFC 实际 Q 候选分支的冻结验证与路线级回流（B0–B3）

> **身份：** `CANDIDATE_BRANCH_INDEPENDENT_VALIDATION / P_FORGE_LITERATURE_BACKFLOW_B0_B3 / CANDIDATE_NOT_CURRENT`。
>
> **对象：** `refs/heads/codex/zfc-q-policy-formalization` 的精确 Git 对象
> `ea6c338f777f51dfaaa2a44122c72f2dfaa997cb`，而非其 live worktree 的未提交文件。
>
> **问题：** 该候选包是否实质改变“ZFC 的完成桥观察边界”这一收束性研究判断，还是只增加一组平行的形式化材料？
>
> **结论先行：** 它给当前收束增加了两项可复核的形式支撑：一阶 `=`／`∈` 语言对外加 `originDone` 的不变性，以及“强完成提升政策 + 明示范围 witness + HoTT 侧 B”才导出矛盾的条件性政策核。它没有填补实际 Zeno、圆环与 HoTT 的同一任务／来源范围桥。因此它把候选终局语言**收紧**为“未付 completion bridge 的观察边界”，没有把 `Q-1` 提升为 `ZFC_Q_LOCATED`。

## 1. TaskDescriptor 与研究身份

| 字段 | 本轮冻结内容 |
|---|---|
| 父结果 | P1/P2/P3 的共同锻造与 ZFC 的 Q 发现是一个收敛过程；此前分支已把它收束为 `COMPLETION_OBSERVATION_AUDIT_REQUIRED`。 |
| 当前目标 | 独立复核一个候选分支的形式命题、保存运行和来源边界，判断它能否改变当前 Q 的精确表述或下一判别行动。 |
| 成功标准 | 对精确 commit 建立 `LiteratureEvidenceEnvelope`；逐条区分 candidate code、kernel result、来源解释与实际 ZFC 结论；给出 B1/B2/B3 路线判词、falsifier 和可消费的下一步。 |
| 非范围 | 不集成该分支；不修改 canonical `dev`、`STATE.json`、`MEMORY`、Feature、rulings 或 claim matrix；不把候选 theorem 写成 bare ZFC 矛盾。 |
| profile | `RESEARCH_PROFILE_GOVERNED`：候选 worktree、已有收束包、来源卡和跨 kernel proof 会共同改变终局措辞的证据边界。 |
| P/Q 共同锻造作用 | `Q_NARROW`：将“ZFC 的时间观察”收紧为“若原过程 Done 未被定义或 bridge 支付，则成员语言／形式完成不能自动判定它”。 |

## 2. B0：LiteratureEvidenceEnvelope

| 字段 | 冻结值 |
|---|---|
| `envelope_id` | `LEB-20261004-ZFC-ACTUAL-Q-POLICY-VERIFY-001` |
| `authority_status` | `FROZEN_CANDIDATE_ONLY` |
| `candidate_ref / exact_source_commit` | `codex/zfc-q-policy-formalization` / `ea6c338f777f51dfaaa2a44122c72f2dfaa997cb` |
| `candidate_base` | `e10771d96940f43ebfb7747898bb1ce6ecb29b17`（本轮 `git merge-base refs/heads/dev ea6c338f`） |
| `observed_dev_target` | `81140216b519f418a5064ca21258c8ffa0afa7f8`；该 target 是独立且 dirty 的 canonical worktree，未在本轮写入。 |
| `source_worktree` | `/Users/aurolafly/.codex/worktrees/a329/HoTT_AI_HANDOFF_20260911`。预检发现其有未提交文件，故全部排除。 |
| `verification_worktree` | 新建 detached `/Users/aurolafly/.codex/worktrees/zfc-q-policy-verify-20261004`，HEAD 固定为 `ea6c338f`，开始和结束均无本轮产生的 Git diff。 |
| `selected_commits` | `35448f86`、`d17abfb9`、`d6dd60f1`、`6ac8bd21`、`56bc84c1`、`589985cb`、`00427fc7`、`5a1b2f0e`、`ea6c338f`；只消费其中的实际 Q policy package 与其保存的 receipts。 |
| `explicitly_excluded` | candidate live worktree 的所有 dirty/untracked path；canonical `dev` 的所有 dirty/index 状态；未列入本报告的该分支其它历史成果。 |
| `selected_paths` | `HoTT/formal/zfc-actual-q-policy/`、C-359–C-365 的 seven proof receipts、`HoTT/CLAIM_EVIDENCE_MATRIX.md`、`HoTT/verification/PROOF_VERSION_CLOSURE.json`、`audit/20261004-ZFC-ACTUAL-Q-RESEARCH-CLOSURE.md`、`SOURCE-BOUNDARY.md` 与 candidate integration handoff。 |
| `freeze evidence` | exact Git object inspection、source-manifest hashes、clean detached checkout、selected `verify_proof_version_closure.py` run。 |
| `reopen_if` | exact candidate commit、candidate source manifests、current `dev` target 或用户的 Q/Done 定义发生改变。 |

这满足 B0 的关键要求：候选工作树的存在没有被当作证据；本轮只使用可由 `git show` 和 clean detached worktree 重建的字节。

## 3. B1：路线库存

| route_id | 候选来源断言 | 拟议 ZFC-side 位置 | 最小缺口 | 预期影响 |
|---|---|---|---|---|
| `RB-FORMULA-DONE-001` | C-365：只含 `=`、`∈`、`⊥`、`→`、`∀` 的最小成员语言及其 theory，对外加 `originDone` 变化不变。 | ZFC 的对象语言形式可作为未来受检 language fragment；不是完整 ZFC 公理模式。 | 必须给出完整 ZFC schema 的保真编码，或一个实际定义的 `originDone`／completion bridge。 | 细化未来 source admission：不能从“使用成员语言／集合论”直接推出原过程 Done 已被判定。 |
| `RB-POLICY-SCOPE-001` | C-359/C-363/C-364：`ZFCOneUse + PolicyScopeWitness + B` 才导出 `False`；同一完整 QProfile 的异判才破坏拟议 uniform policy；未付 bridge 有保字段反模型。 | ZFC 被实际用作基础语境时的 use-level completion policy，不是 ZFC 对象语言。 | 实际 Zeno→圆环／HoTT 的 source-owned `PolicyScopeWitness`，或完整同一 `QProfile` 与相反 judgment。 | 细化终局语言和跨案例来源要求；不能直接升格为实际 ZFC 冲突。 |
| `RB-CONTROL-TRIAD-001` | C-360/C-361：fixed HoTT coarse completion 不反射原 finite halt；几何级数极限不等于有限阶段 endpoint，同时存在闭连续时间 endpoint。 | 不是 ZFC candidate site，而是对两端过强读法的形式控制。 | 一个保留同一任务的 actual source bridge。 | 阻止“极限必然等于有限步骤到达”与“没有最后离散阶段就没有连续端点”两种错误外推。 |

## 4. B2：RouteBackflowCards

### 4.1 `RB-FORMULA-DONE-001`

| 维度 | 处置 |
|---|---|
| RB-D01 | `LEB-20261004-ZFC-ACTUAL-Q-POLICY-VERIFY-001 / FROZEN_CANDIDATE_ONLY`。 |
| RB-D02 | candidate `ZFCMembershipLanguageBoundary.lean`，C-365；精确 commit 与 saved run 见 §6。 |
| RB-D03 | 最小一阶 equality/membership language；它是对未来 ZFC encoding 所在语言的片段分析，非 bare ZFC model。 |
| RB-D04 | 路线仅是 formula-language route；不得把它偷换为 Power Set、RepFun、完整 schema、模型或实际数学实践路线。 |
| RB-D05 | H0→Z0 的 T0–T5 没有通过：T0 是 Lean meta-language；T1–T5 没有 actual Zeno/circle/HoTT task transport。`TRANSPORT_ANTI_ANALOGY`。 |
| RB-D06 | 形式 `T/u/F/C/I/O/Done` 为 carrier、membership relation、formula evaluation、theory satisfaction、external `originDone`；不等于用户圆环或 Zeno 的过程合同。 |
| RB-D07 | 没有 source-defined active consumer；只是 syntax/semantics boundary。 |
| RB-D08 | 没有 same-object reentry；P2 不适用。 |
| RB-D09 | 没有 source-defined lifecycle / `NeedBuild → OperatorUse → BuildDone`；P3 不适用。 |
| RB-D10 | 负控制：将 explicit `originDone` specification/bridge 加入后，opposite expansion 被阻断。实际 payment 仍待来源定义。 |
| RB-D11 | `Lean 4 core` formal language layer；不是 ZFC axiom schema、proof assistant runtime 或 physical process。 |
| RB-D12 | 只影响 future source admission 和现有 completion-observation terminal wording；不改历史 AS_RUN。 |
| RB-D13 | `Target-Q` = 未付 completion bridge；`Candidate-Q` 不新增；`Control-Q` = paid bridge；状态维持 `Q-1_SEED`，但候选空间被收紧。 |
| RB-D14 | positive control = specified bridge；negative control = `True`/`False` Done expansions；falsifier = actual source supplies a membership-defined process Done / full bridge. |
| RB-D15 | `NEW_SOURCE_INGRESS / FORMULA_FRAGMENT_ONLY / SOURCE_LAYER_CONTROL`。 |
| RB-D16 | future canonical integrator 可选择性吸收为 I1 source-admission refinement；停止于 full ZFC encoding 或 actual bridge source 出现。 |

### 4.2 `RB-POLICY-SCOPE-001`

| 维度 | 处置 |
|---|---|
| RB-D01 | 同一 frozen envelope。 |
| RB-D02 | candidate `ActualQPolicy.lean`（C-359）、`ZFCCompletionPolicyUniformity.lean`（C-363）与 `ZFCUnpaidCompletionPromotion.lean`（C-364）。 |
| RB-D03 | use-level policy calculus：`ZFCOneUse` 明确是 base proposition + Q gap + admitted policy 的模型，不是 ZFC syntax。 |
| RB-D04 | `PolicyScopeWitness` 路线与 strict `TaskEquiv` 路线被分开；不得以 metadata equality、同名 Done 或两边都谈 completion 代替。 |
| RB-D05 | H0→Z0 未 transport：candidate 自身将 cross-kernel mapping 标为未支付；T0 到 T5 仍无 actual evidence。 |
| RB-D06 | Lean task signature 可表达 state/input/step/observe/formalDone/originDone；实际 Zeno、圆环、HoTT 的这些字段未同卡填实。 |
| RB-D07 | source consumer 仍缺；candidate 只展示 `ZFCOneUse` 的显式前提。 |
| RB-D08 | no P2 reentry claim。 |
| RB-D09 | no P3 source lifecycle claim。 |
| RB-D10 | `PolicyScopeWitness`、full `TaskEquiv`、paid bridge/formal adequacy 都是正控制；它们是前提，不可由 Q gap 自动获得。 |
| RB-D11 | Lean conditional policy layer + separately checked Cubical Agda control；不跨层归为 bare ZFC。 |
| RB-D12 | 使既有 `P_TO_B_SOURCE_UNPROVED` 边界更加明确，未反驳或替换任何 fixed parent card。 |
| RB-D13 | `Target-Q` = 统一 completion-observation policy；`Candidate-Q` = none newly eligible；`Control-Q` = explicit scope/payment; Q remains `Q-1_SEED`。 |
| RB-D14 | positive control = paid bridge / payment-difference profile；negative control = C-360 and C-361; falsifier = actual source-owned scope or explicit rejection. |
| RB-D15 | `NEW_SOURCE_INGRESS / CONDITIONAL_POLICY_CONSEQUENCE / EVIDENCE_INSUFFICIENT_FOR_ACTUAL_CONFLICT`。 |
| RB-D16 | canonical integrator should compare candidate C-359 with the current contributor policy calculus before accepting any source-level wording; stop unless actual scope evidence arrives. |

## 5. B3：影响分流与 P/Q 自审

| 路线 | B2 主判词 | B3 impact | 说明 |
|---|---|---|---|
| `RB-FORMULA-DONE-001` | `NEW_SOURCE_INGRESS` | `I1` | 这项形式证明提高未来 ZFC source card 对“原过程 Done 是否已经被定义”的要求；candidate-only 身份禁止 current-owner 写回。 |
| `RB-POLICY-SCOPE-001` | `NEW_SOURCE_INGRESS` | `I1` | 它把实际冲突所需的 `PolicyScopeWitness`、full QProfile 与 B 映射明确写成不可省略的前提。 |
| `RB-CONTROL-TRIAD-001` | `SOURCE_LAYER_CONTROL` | `I0` | 它只增强正反控制，不生成新的 active Q。 |

### P/Q 共同锻造判词

```text
Q state before: Q-1_SEED / COMPLETION_OBSERVATION_AUDIT_REQUIRED
effect:         Q_NARROW
Q state after:  Q-1_SEED / COMPLETION_BRIDGE_OBSERVATION_BOUNDARY_CANDIDATE
new blade:      NO (P1/P3-C and existing completion-observation calculus contain the pattern)
tool-only drift: NO
```

它不是 `TOOL_ONLY_DRIFT`：C-365 防止我们把“ZFC 没有时间”误报为结论；C-359/C-363/C-364 防止我们把局部 Zeno resolution、HoTT B 和用户的规范张力误拼成 ZFC 的对象层 `False`。两者都直接收紧了同一 Q 的可检验空间。

## 6. 独立可复现验证

### 6.1 固结证据

在 clean detached worktree 中执行：

```text
python3 -B scripts/audit/verify_proof_version_closure.py \
  --proof-id MP-ZFC-ACTUAL-Q-POLICY-002 \
  --proof-id MP-ZFC-ACTUAL-Q-HOTT-COUNTEREXAMPLE-001 \
  --proof-id MP-ZFC-ACTUAL-Q-ZENO-LIMIT-CONTROL-001 \
  --proof-id MP-ZFC-OBSERVATION-LANGUAGE-BOUNDARY-001 \
  --proof-id MP-ZFC-COMPLETION-POLICY-UNIFORMITY-001 \
  --proof-id MP-ZFC-UNPAID-COMPLETION-PROMOTION-001 \
  --proof-id MP-ZFC-MEMBERSHIP-LANGUAGE-INVARIANCE-001
```

结果为 `SELECTED_PACKAGES_VERSION_CLOSED`，selected claims 为 C-359 至 C-365。该 verifier 只证明 Git/source/receipt/index closure；它不替 kernel 重做数学检查。

### 6.2 新鲜 kernel 重放

| 范围 | 结果 | 关键观察 |
|---|---|---|
| `ActualQPolicy.lean` | Lean 4.34.1 exit 0 | 33 个打印 theorem 均 `does not depend on any axioms`；强 P、scope 和 B 都是显式前提。 |
| `ZFCObservationLanguage.lean` | Lean 4.34.1 exit 0 | 6 个 theorem 无额外公理；base model 与 completion expansion 的区分为定义性语义。 |
| `ZFCCompletionPolicyUniformity.lean` | Lean 4.34.1 exit 0 | 7 个 theorem 无额外公理；same full profile 与 coarse profile 的控制同时存在。 |
| `ZFCUnpaidCompletionPromotion.lean` | Lean 4.34.1 exit 0 | 6 个 theorem 无额外公理；`originDone := False` expansion 是显式反模型。 |
| `ZFCMembershipLanguageBoundary.lean` | Lean 4.34.1 exit 0 | 4 个 theorem 无额外公理；对 formula 的结构归纳确实保留 `originDone` 在语言外。 |
| `ZenoLimitControl.lean` | Lean 4.34.0 + pinned Mathlib exit 0 | 五条定理均报告 `propext`、`Classical.choice`、`Quot.sound`，已按该实分析控制的声明信任边界保留。 |
| `HoTTCounterexample.agda` | Cubical Agda 2.8.0 / cubical-0.9 exit 0 | fixed truncation stage-one completion 与 original universe finite-halt failure 的组合通过核验。 |
| `WrongHoTTCounterexample.agda` | Cubical Agda exit 42（预期拒绝） | 在 `nothing != just 1` 处被拒绝，说明伪造的 fuel-0 halt 没有被接受。 |

所有 direct replay 只在 detached checkout 执行；它们不修改候选 source、canonical `dev` 或当前 contributor 的 canonical owners。

### 6.3 一手来源的当日复核

为避免把 candidate source card 的转述当作当前网页事实，本轮于 2026-10-04 重新读取三个一手公开页面：

| 来源 | 当日可核事实 | 对本路线的作用 |
|---|---|---|
| IEP, *Zeno’s Paradoxes*, [Standard Solution](https://iep.utm.edu/zenos-paradoxes/) | 将 Standard Solution 说成使用 calculus/real analysis；明说“没有 final step”是被拒绝的假设；又把 ZF(C) 作为 real analysis foundation 的 majority view，并称其间接解决 Zeno。 | 确证 ZFC-supported Standard Solution 的 R1 resolution、R2 completion-condition change 和基础语境；没有圆环或 HoTT 的同一任务 bridge。 |
| SEP, [*Supertasks*](https://plato.stanford.edu/entries/spacetime-supertasks/) | 对 Zeno walk 明确区分“执行 final action”与“完成 every step”；在 supertask 中两种 complete 不等价，并将后者局限于该任务的解释。 | 直接支持 `SOURCE_TASK_CONTRACT_SPLIT`，反对把两个 Done 自动视为同一谓词。 |
| Norton, [*Zeno’s Paradoxes of Motion*](https://sites.pitt.edu/~jdnorton/teaching/paradox/chapters/Zeno/Zeno.html) | 显式将 completion 从“包括最后 action”改写为“做完所有 actions”，并给每个 action 一个时刻。 | 给 R2 一条透明的 source-defined transformation；它的适用对象仍是 runner/action task。 |

这次复核强化而没有推翻已有来源判断：**当前标准来源把 completion 的语义选择公开写出来。** 因而它们是
本地 Zeno policy 的来源，而不是一条无边界、不可见的共同 P；它们没有给出用户圆环 `OriginDone` 或 fixed
HoTT question 的 `PolicyScopeWitness`。

## 7. 独立代码审读与最终判词

候选代码没有把结论藏进 kernel：

1. C-359 明确把 `ZFCOneUse`、`gapAdmitsZenoP`、`PolicyScopeWitness` 与 HoTT-side B 写成条件；源码还证明 `QMissing` 不会以纯逻辑强制 P，且 use-model 本身不强制 B。
2. C-363 明确要求**完整** `QProfile` 相同；它同时提供“bridge payment 不同则可以合理异判”的反控制。
3. C-365 只处理一个刻意最小的语言；它不能证明完整 ZFC schema 没有定义过程 predicate，也不能证明实际 `originDone` 无法在 ZFC 中表达。
4. C-360/C-361 不是 Zeno–HoTT 同一任务 theorem：一个是 fixed Cubical HoTT completion reflection control，另一个是有限阶段与连续端点的实分析控制。

因此本轮的最强可用结论是：

> **ZFC 问题查找的形式层已经进入收尾：我们已能严格表述并机器检验“未经定义或 bridge 支付的 formal completion 不自动决定 origin completion”，也已机器检验一旦把跨任务的强政策范围、完整同 Q 与 HoTT B 额外加入便会发生何种条件性冲突。实际 ZFC 的最终问题仍取决于来源是否真正承担该跨任务政策。**

这不是退回到“没有发现”。它将最后仍可能推翻或完成研究的事件缩成两类：

1. 一手来源真正支付或拒绝 `PolicyScopeWitness`／same-task completion bridge；
2. 对用户圆环 `OriginDone` 的进一步固定，使同一任务测试可以通过或被明确拒绝。

## 8. 自审与后续

| 检查 | 判词 |
|---|---|
| 理论层级 | `ALIGNED`：不把 Lean meta-policy 或最小 formula language 冒充 bare ZFC。 |
| 圆环／芝诺原问 | `ALIGNED_WITH_OPEN_BRIDGE`：C-361 的连续端点正控制保留，未把没有有限阶段误写成没有连续到达。 |
| 一手来源 | `ALIGNED`：IEP/SEP/Norton 当日复核确认 R1/R2 与 contract split；未将页面的 local runner policy 扩写为跨案例政策。 |
| HoTT 使用 | `ALIGNED_WITH_SCOPE`：C-360 是 main HoTT 发现的原生控制，不是 Zeno 的同一过程。 |
| P/Q 共同锻造 | `Q_NARROW`：提高 source/bridge 的准入精度，未凭新文件宣称 Q 会合。 |
| 新刀 | `OLD_TOOL_FIELD_GAP = NO`：没有发现 P1/P2/P3 无法容纳的独立判断职责。 |
| current truth | `CANDIDATE_NOT_CURRENT`：不修改 dirty canonical `dev`；若需要接受，必须走干净 integration worktree。 |

**下一最小判别行动：** 不再增加 generic limit、ZFC 或 HoTT 文献。只检验一份版本固定的来源是否主张同一个强 completion policy 跨越其 Zeno runner 合同、用户圆环 `OriginDone` 与 fixed HoTT completion contract；来源明确拒绝该范围时，当前路线应正式闭合为 `ACTUAL_Q_UNIFICATION_REJECTED_WITH_SCOPE`。
