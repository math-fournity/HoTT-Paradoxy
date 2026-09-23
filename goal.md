# HoTT 现实相对研究 Goal：原四弹 redo 与四分支后续计划

> 状态：`PHASE_1_COMPLETE_WITH_SCOPE / THEORY_INSPECTION_IN_PROGRESS / P42_CONSTRUCTION_COMPLETE / P43_NEXT / GOAL_ACTIVE`；具体当前动作和revision以STATE为准。
> Goal schema：`four-stage-redo-goal/v2`
> 唯一 current objective owner：本文件  
> 工作根：`/Volumes/D/HoTT_AI_HANDOFF_20260911`  
> Git 工作面：顶层 repo 的 `main`  
> 状态 owner：`.codex/research/hott/STATE.json`  
> App Goal：第一阶段见第 1 节；第二阶段按第 2 节的四分支总体计划推进，ABX 是其中实际消费者分支。其余旧机器统观内容仍是历史/候选，不自动构成工作队列。
> 说明：文件存在、计划完成或局部证明均不证明数学结论；2026-09-21 的原 X/数学现实同一性澄清已按第 1.1 节完成有界核对。四分支计划不追溯性改变第一阶段判词。

## 1. 当前目标：原四弹 redo

对“四弹一体”原方案进行忠实、可复核的 redo，并只按证据给出判词：整体成立、整体未成立、仅局部成立，或在精确义务上开放。若发现真实的 HoTT—现实任务失配见证，再以它为对象开展独立的新研究；不得预设“击落 HoTT”必然已经发生或必然能够由原四弹推出。

本目标的第一阶段是“原四弹 redo”，第二阶段是“新候选研究”。二者严格分开：第一阶段的未成立、撤回或范围结论本身就是完成结果；第二阶段不能因为仍有未知问题、仍想取得更强结论、仍可做更多形式化或仍可改善材料，而自动延长第一阶段。

### 硬元约束

除非用户明确改写本目标，每次开始新的工作单元前，必须先给出“判词改变凭据”：它要改变的既有精确判词或六义务编号；新输入、反例、实际消费者、证明义务或证据失效；最小可验证行动及正、负结果如何改变判词；停止/回归条件；以及现有源码、运行、报告或控制为何不足。缺少任一项，不启动该单元，不新增报告、包、重放、分类、全库扫描或证明支线。

仍有未知、可能存在更一般定理、某方向“还有数学价值”、再跑一次未变输入、增加消费者/审阅包/索引，或希望公开/发表/取得更强结论，均不足以继续 redo。它们最多是第二阶段候选。

### 第一阶段完成判据与当前结果

redo 的完成判据是：原四弹的每一层、层间桥梁、所需理论承诺、最强保任务恢复和证据范围均已逐项判定到相称强度；随后交付说明局部定理、整体结论和能改变结论的缺失事实的范围报告。

此前完成的范围交付包括：第三十五轮逐层对账、九个既有证明包的资格核验、固定自然消费者源码合同及 revision 209 checkpoint。其当时判词为 `ORIGINAL_FOUR_STAGE_TARGET_NOT_ESTABLISHED / ASSUMPTIONS_AND_TASKS_RECONCILED_WITH_SCOPE`：原四弹整体“击落”结论未建立，精确局部结果保留。这不是 HoTT 全局无问题定理，也不是“已击落 HoTT”。

## 1.1 已完成的受限勘误：原 X 与第三弹任务忠实性

用户随后澄清：原 A、B、X 共同观察的主过程是“圆 `C` 去掉指定点 `p`、呈现为去点圆 `M`／开区间 `N`、再尝试把两端闭合并复原”的过程；`Spec_A`／`Spec_B` 的 `√2` 读出／有理精确根差异只是后来的算术校准，不能替换该主过程。这个输入可能改变 G01 的 X/过程固定、G04 的同任务桥，以及上段范围判词的理由，故按硬元约束作一次受限重开。

本勘误的固定凭据与停止边界如下：

| 项目 | 固定内容 |
|---|---|
| 可能改变的判词 | G01 的主 X，G04 的同任务桥，以及第一阶段范围判词的理由；不直接改变 HoTT 内部一致性结论 |
| 新输入 | 用户对原 `C → M/N → 闭合/复原` 过程和 `√2` 校准角色的明确澄清；可见原问答必须逐字归档 |
| 最小验证 | 核对用户原文、022/023/025、当前策略、第三十五轮报告与已有 HoTT/消费者实物，写出 X、静态 A、过程性 B、Input、允许操作、Observation、Done 及 `RealitySame` 的关系 |
| 必需理论侧事实 | 找到具体 HoTT 规则、定理、库接口或实际消费者 H，确实把静态 A 当作足以履行过程性 B 的同一任务处理；`RealitySame(A,B,X)` 本身不等于 H，也不推出 `TaskEq` 或规格等价 |
| 负结果 | 若没有 H，保留“原整体结论未建立”，以修正后的理由重新关闭第一阶段；`√2` 结果继续只是校准 |
| 正结果 | 若发现 H，只为该具体 H 建立新的、带精确命题和机器证明门禁的原生任务；不把旧 M3 算术分离直接升格 |
| 停止条件 | 完成上述映射与固定来源审计后停止；不扩展到新消费者、全库搜索、重复 kernel 运行或第二阶段 |

`RealitySame(A,B,X)` 可以作为语义/建模规格的显式外部前提或参数；它也可以由一个专门的 `Denotes`／来源定理支持。它不应被排除在证明规格之外，但其内容只能是共同指称：还必须另有同一 Input、操作、观察与 Done 的任务合同 C，以及实际理论承诺。在 ABX 的符号中，该理论侧事实写作 `K`，以避免与用户原文的 `H_top(M,N)`（通常同胚判据）混淆。没有 C 与 K 时，不能把 `M3` 的规格不等价写成原圆环过程的反例。

该有界审计已完成。固定来源中的实际 univalence/同胚运输控制保留了来源、闭图和 Done，并显式拒绝把裸 `N` 当作充分输出；同一对象对的连续曲线与环境 `Success` 也在源码中作为不同操作合同处理。`√2` 文件将请求和 Done 分开，固定 Coq locator 消费者没有圆环闭合词汇或任务桥。因此结果为 `NO_ACTUAL_H_COMMITMENT_FOUND_WITHIN_FIXED_SCOPE`，并非全局不存在定理。第一阶段以修正后的理由重新关闭：原整体“击落”结论仍未建立，`√2` M3 继续只是校准。直接证据见 `audit/astra-task-fidelity-corrigendum-20260921/H-COMMITMENT-AUDIT.md` 与其 manifest/verification。

### 第二阶段重开条件

除第 1.1 节已经授权的受限勘误外，只有输入、源码、依赖或运行失效；发现会推翻当前判词的具体反例或实际理论承诺；现有证据无法回答一个固定六义务；或用户明确开启新研究/新交付时，才重开。新的“击落 HoTT”探索必须另立候选任务，固定同一 X、操作、信息、观察、Done、理论承诺、反解释与停止条件，且不得回溯性地把 redo 重标为未完成。

每个自然单元结束时，若没有改变判词，也没有产生新的合格判词改变凭据，则保存必要证据、交付当前结论并停止该分支。最终回答必须区分机器证明、来源支持的解释、开放问题和阶段完成状态。

## 2. 当前第二阶段：四分支研究组合

用户要求把上一轮关于 `R_min`、`K_theory`、`K_app` 和 `K_engine` 的四分支回答完整落盘，并根据令牌经济、可判别性和反漂移要求决定先后。详细 owner 是 [HoTT后续研究总体方案.md](HoTT后续研究总体方案.md)：P1 是共同的 `R_min` 规格资格化，P2 是规则/定理级桥，P3 是 ABX 实际消费者，P4 是被触发才做的实现忠实性审计。

P1–P39已形成有范围的规格、规则、消费者、几何与反射结果，历史路径和判词见工作树。用户在机器统观回顾后明确要求把**HoTT理论的充分检视放在第一位**：当前P40改为 `P40-THEORY-INSPECTION-FIRST-001`，先覆盖规则、派生构造、可选公理、语义模型和相关变体，核抽象选择及关键交互，再排序靶前提并设计过程。此前G-04/D-01/Book§11.2三选一不再是当前第一步。详见总体方案第006片；它复用已有Schema、PREMISE与证明控制，不重建统观平台。一般`X_T`回到原圆环`X₀`仍须保任务桥。

四分支都保留为后续可能性，但不是四个同时运行的工作队列。每个单元必须给出判词改变凭据、一个新分母、精确任务、正反控制和停止条件；若没有新增事实，必须结束而不以文档、关键词或重复运行代替进展。

## 3. 历史机器统观目标与其余第二阶段候选

下列原 2026-09-14 机器统观目标、文献队列与完成门，保留为 Git 可回查的历史背景和潜在第二阶段材料。除 ABX 外，它们不自动定义当前 `/goal`，也不能因自身开放而重新启动工作。

### 3.1 历史最终目标与禁止误报

在唯一当前工作根的 main 中持续、自主推进“HoTT 非现实性悖论的系统化机器统观”，直至取得至少一个严格合格的现实相对悖论见证，并闭合机器证明、HoTT 必要性、现实同任务对应、学术定位、统观覆盖证书和可复现证据。

不得把下列结果误报为 Goal 完成：计划或治理框架完成；一次超时；固定循环；一般不可判定性；一般 Gödel 不完备性；外部 proof-search 发散；普通表示边界；synthetic implication；理论正确拒绝错误输入；HoTT 中可表达的普通计算问题；尚未找到反例的 bounded negative。

### 3.2 历史 Session 恢复与单工作面

每次新 Session、压缩恢复或范围变化，先从 main 完整加载：

- 项目及目录 `AGENTS.md`、`repo-cognitive-closure`；
- `hott-local-session-governance` 与 `hott-paradox-research`；
- 四件套全文；
- `STATE`、`MEMORY`、`FRONTIER`、`RESUME`；
- `.codex/research/hott/HOTT-PARADOX-PROGRAMMATIC-EXPLORATION-COMPLETENESS.md` 的索引和全部分片；
- 本文件与 active record `A-HOTT-MACHINE-OVERVIEW-GOAL-002`、历史兼容记录 `A-HOTT-MACHINE-OVERVIEW-GOAL-001`、`A-HOTT-PROGRAMMATIC-COMPLETENESS-001`、`A-COMPUTABILITY-LITERATURE-COVERAGE-AUDIT-001`、`A-LIT-CLASSICS-001`、单工作面决定。

外部 `/Volumes/D/HoTT-machine-overview` 只作只读候选来源。所有决定性计划、状态、源码、run、来源身份、失败、反证和 checkpoint 必须进入 main 的正确 owner。不得让未来 Session 依赖外部 worktree 中未导入的 current truth。

### 3.3 历史已验证基线：从这里继续，不重复开工

### 3.1 文献

- `LIT-DENOMINATOR-001` v1 已冻结并验证。
- Rosser 1936、Kleene 1938 与 Post 1944 primary 已补齐并审读；Post 从 BAMS 50(5) 整期抽取印刷页 284–316，33 页来源／页界固定。
- `LIT-HOTT-COMPUTABILITY-001` 已推进到六片：除 Parametric CT、Oracle、2LTT、groupoid-syntax 与 C-227–C-232 外，C-233–C-243 已重放 LOPS ordinary-internal-classifier no-go/crisp recovery 和 ITT regular/degenerate/transport 对照；全面文献/citation 覆盖仍未完成。
- revision 131 所称“19 个 FULL_TEXT_TO_READ”是历史初始队列，不是永久 current 计数；剩余量以 current LIT records 为准。

### 3.2 R1/R2 本地计算基础

- C-188–C-190：R1 固定停机／循环校准。
- C-191–C-194：有限 `ProgramCode`、总 decoder、bounded evaluator 与 controls。
- C-195–C-198：自然数编码、合法像往返／覆盖、数值 bounded evaluator。
- C-199–C-202：program/input/fuel 公平有限调度与 observation preservation。
- C-203–C-207：stage-indexed partial answer、正答案持续、`CodeHalts ↔ SemiReturns`、公平正见证枚举。

这些结果是一般计算性基础，不能完成本 Goal。

### 3.3 R2 universality／undecidability 当前前沿

- C-208：Coq Library of Undecidability Proofs `coq-8.15@c486697` 已在 Coq 8.15.2 从 777 文件干净树重放 `MM2_HALTING_undec`；`Print Assumptions` 为 `Closed under the global context`。
- C-208 的精确含义必须保留为上游 synthetic implication：`decidable MM2_HALTING → enumerable (complement SBTM_HALT)`。它不是纯构造元理论中的无条件 `¬ decidable MM2_HALTING`。
- C-209–C-213：Cubical Agda 已证明本地 label-1 MM2 函数式模型编译到 `ProgramCode` 时查表、finality、单步、任意有限运行和截断停机存在性双向保持，并有分支 controls。
- C-214–C-218：Coq 同核 `MM2ProgramCodeBridge.v` 已从 777 文件干净上游树完成 F-011 capture/index/freeze/exact replay；机器证明 `MM2_HALTING ⪯ PC_HALTING`、`PC_HALTING_undec`，且 `Print Assumptions` 为 `Closed under the global context`。该结论仍是 synthetic implication。
- `R2-CROSS-KERNEL-001`：`R2-TASKSPEC.json` 已固定四模型 correspondence；28 个源码 anchors、3 个 formal packages、282 个独立 controls 全部 PASS，判词为 `DUAL_KERNEL_SCOPED_CORRESPONDENCE_WITH_SAME_KERNEL_COQ_REDUCTION`；不主张跨 kernel definitional equality。
- C-219–C-222：`coq-synthetic-computability@b9523cb` 的 109 文件树与 20 文件目标闭包已固定；Coq 8.13.2 重放 `EPF_SCT_halting`、`K_nat_bool_undec`、`K_nat_undec`，三个 `Print Assumptions` 均为 `Closed under the global context`。精确强度是显式 `EPF_bool + SCT` 前提下的 internal `~ decidable`，不是 ambient HoTT 无条件结论。
- 上述新资产尚未 Git 提交，统一为 `LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED`。

### 3.4 `G-HOTT-SYNTAX` 当前前沿

- C-223–C-226：`akaposi/cohtt@5babc385` 的 91 文件作者树已固定；20 个 `TT` 模块在 Agda 2.8.0/Cubical v0.9 两阶段 source replay 通过。
- exact slice 含 `Con/Sub/Ty/Tm`、substitution/context extension、`U/El`、Π/β/η、二阶 coherence；α-normalisation 证明 `isSetTy`，并有 groupoid/set syntax 的 `isoCon/isoSub/isoTy/isoTm`。
- 该 slice 缺 Nat、一般 identity/Path、对象层 univalence/HIT、raw proof checker/enumerator 与 arithmetic interpretation，因此不是完整 R4 calculus。
- 2LTT primary 明说 §2.1 suggested syntax 不是 complete raw specification；basic conservativity 与 strengthenings 必须分开。
- C-227–C-232：边界保持的两层代数接口已机器证明 context-uniform FORM/INTRO/dependent-ELIM for `R` + outer UIP 会推出 inner UIP，并排除非平凡 inner loop；原生 `S¹.loop ≠ refl` 与删去 strict 两层桥的 identity-replacement 均有控制。它重构的是已发表 Theorem 2.20，不证明 basic HoTT/2LTT 矛盾。
- C-233–C-238：LOPS 官方 Agda-flat 全包 exact replay；ordinary internal weak fibration classifier 把 fiberwise 提升为 familywise 并坍缩 interval，crisp/tiny 版本构造 classifier，local argument 被 modal checker 拒绝。
- C-239–C-243：Boulier–Tabareau Coq 源 exact replay；regular open-family replacement 导出 `False`，actual QIT 只给 `DFib`，`RFib` 需要 `DFib + Trans`，更强路径消去另受 `emptyctx` 限制。
- C-244–C-249：`uds-psl/coq-synthetic-incompleteness@cd7d849` 已从 repo-contained 807-file archive 在 Coq 8.15.2 fresh build并 exact replay；机器重放 universal classifier divergence、abstract essential incompleteness、`EPFμ → CTQ` 与 Robinson Q 条件独立句。universality、strong separation、Peirce、CTQ、Q containment、enumerability、consistency均显式；对象理论是一阶算术，不是 exact HoTT calculus。
- R3→R4 十二义务矩阵：H-SYNTAX/H-SUBSTITUTION 仅 scoped present；H-NAT/H-ID-PATH/H-UNIVALENCE-HIT 在当前 groupoid syntax absent-by-definition；其余七项 open。R4 readiness=`NOT_READY`。

### 3.4 历史第一 successor

上一轮三条薄切、2LTT replacement 数学核、natural-consumer 消融、CE-MAP v1 与 R3 source replay 都已形成真实链。CE-MAP 已把 revision 149 的 478 个具名输入全部登记；C-244–C-249 已关闭一个 exact R3 基准，但没有把一般一阶不完备性偷换成 HoTT 结论。当前按判别力推进：

1. `R4-HOTT-NAT-EFFECTIVITY-001`：R3 已闭合；现在比较 cubicaltt/redtt/cooltt/cctt，选择同时具 Nat/Path/conversion 的 exact target，并以闭合证明输入规范把 holes/undefined/未解目标与无终止性证明的递归明确列为域外构造；先推进 H-NAT/H-ID-PATH/H-CONVERSION/H-EFFECTIVITY；
2. `CLASSIFIER-REALITY-BRIDGE-001`：继续检查是否有真实 consumer 需要 local/open classifier 且拒绝 crisp、transport 或 pointwise-fibrant 支付；不得把扩大后的 local task冒充与 global task相同；
3. 保持三个并行返回口：Oracle Modalities 的 Agda 2.6.4.3/Cubical v0.7 重放与 modal→ambient consumer；R2 ambient 无条件 no-decider／ProgramCode 对应；物理时间/时空连续性与现实同任务桥梁。

`NATURAL-CONSUMER-002` 已找到真实调用链，但 crisp、degenerate+transport 和 pointwise-fibrant 限制能够完成来源中声明的真实任务；故固定为 `DEFENSE_WORKS_WITH_EXPLICIT_PAYMENT`，不是 Goal 终点。CE-MAP 已将该同型 no-go 归约为一个带 anti-preservation 的 pattern class。现在优先选择未被防线覆盖的 Gödel/R4 cell；不以已完成 R3 机器证明保护候选。

### 3.5 历史文献覆盖剩余义务

文献与代码交替推进。以 2026-09-14 为具名截止日，继续 current LIT owner 中尚未闭合的：

- Post 的 Friedberg–Muchnik／2024 CIC forward chain，及 Rice–Shapiro、Tarski、Hilbert–Bernays、Löb、Lawvere、Rogers／Myhill、Chaitin；
- Kleene normal form、s-m-n、recursion theorem；
- termination、partiality、dominance、guarded／clocked recursion；
- 2024–2026 Oracle Modalities 的旧工具链/论文对账、Post hierarchy、synthetic computability、cubical cofibration complexity、ordinal decidability、groupoid-syntax citation chain、Extension Types、Agda Gödel、MetaRocq、Lean Foundation。

每项记录版本／hash、精确 theorem 与 assumptions、阅读范围、TaskSpec 映射、反解释、遗漏和 replay 状态；完成 backward／forward citation chaining 与独立 holdout。只声明具名截止日与渠道分母内的覆盖，不把搜索未命中写成不存在。

### 3.6 历史 CE-MAP 与机器统观完备性

`CE-MAP-001` v1 已完成具名 revision-149 分母登记，把 cases、evaluations、formal packages、claims、STATE records 和文献路由映射到八轴张量：

`TheoryConstruct × AbstractionChange × RealityOrTask × ConsumerOrContext × ObservationLayer × CompletionProperty × Oracle × FrameworkOrModel`。

当前 478/478 canonical items、69 个显式 `UNCLASSIFIED`，产物由 `scripts/audit/build_ce_map.py` 查询和验证。下一轮继续推进六类生成器：typed synthesis、rule mutation/ablation、consumer synthesis、self-reference/universal computation、metamorphic/differential、source/AI-guided。

- 有限 grammar：给 coverage proof 与 remainder=0；
- 无限 code：给公平 dovetailing／no-starvation；
- 类级外推：给保持 task、consumer、observation、completion 的 total typed reduction；
- 始终保留 OP-14 反解释、coverage shadow、out-of-envelope 和 unknown ingress。

### 3.7 历史计算阶梯

- R0：有限观察窗未完成，只作观察。
- R1：固定程序发散；不算最终悖论。
- R2：闭合程序码、decoder、bounded evaluator、公平枚举、正半判定、universality/reduction；当前另闭合显式 EPF_bool/SCT 前提下的 internal no-decider，ambient 无条件结论仍开放。
- R3：一般 formal-system/Robinson-Q 条件基准 C-244–C-249 已 exact replay；当前 target HoTT 的 proof code/classifier、`Universal θ`、算术解释、strong separation/representability、s-m-n／自应用、fixed point 与 independent sentence 仍属于 R4 bridge义务。
- R4／`G-HOTT-SYNTAX-001`：首个 Π/U/El/groupoid-coherence exact slice 已重放；继续补 syntax、judgment、conversion、proof checking/enumerability、Nat、dependent substitution、Path/univalence/HIT 与 inner/outer metatheory，取得 exact HoTT incompleteness 或精确边界。
- R5：只有 trusted HoTT rules 推出 `⊥` 才能使用；其它结果不得称 HoTT 内部矛盾。

### 3.8 历史方向 A、方向 B 与时间／时序

方向 A：理论引入连续性、稠密性、无限细分、商化、同一化、时序坍缩或额外相干义务，使现实可完成任务在理论中无法完成。

方向 B：理论绕过 ASK，把 mere existence、Path、外部解释、部分分类、有限近似或可证明性提升为 chosen witness、当前归约、内部自知、总求解、精确完成或实际交付。

“时间”保留对时空、运动、连续／非连续及稠密性的结构问题；“时序”保留对先后、依赖、当前可用、构造和验证落定顺序的问题。Gödel、Kleene、Lawvere、Löb 必须服务方向 A/B，不能取代现实相对问题。

### 3.9 历史“机器证明不能停机”的候选资格

只有下列链条贯通时，它才成为最终候选：

1. 明确对象程序、证明搜索、反射或自验证过程；
2. 以不变量、共归纳、不可分离性或经证明的保真归约机器证明不完成；
3. 定位具体 HoTT 抽象／资格变化，并以消融证明其必要性；
4. 找到预先冻结的自然 consumer；
5. 与现实侧保持同一任务、输入、观察和完成标准；
6. 证明方向 A 或 B 的不相容；
7. 通过正控制和最强竞争解释。

若只得到一般计算边界或 HoTT 中可表达的普通停机问题，登记为 R0–R3 或 `GENERIC_MECHANISM_WITH_HOTT_INSTANCE` 并继续。

### 3.10 历史 bounded unit 的完成要求

每个有界工作单元必须保存真实 `input → candidate → oracle → evidence` 链，记录失败、反例、换题风险、未触达轴和下一 successor。遇到防线就更新候选并换构造／consumer，不重复堆叠小循环。

数学结论必须在 main 的 `HoTT/formal/`、`HoTT/verification/runs/`、`HoTT/CLAIM_EVIDENCE_MATRIX.md` 完成 F-011，并通过 STATE、projection、MEMORY、session、36-KC audit 和 canonical checkpoint 保存连续性。

### 3.11 历史机器统观 Goal 的完成门

只有同时满足以下条件，才标记 Goal `complete`：

1. 至少一个候选贯通“exact HoTT 规则／表示 → 抽象或资格变化 → natural consumer → 机器证明的不完成／不相容 → HoTT 必要性 → 现实同任务对应 → 方向 A 或 B”；
2. 通过最强反解释与独立或跨框架复核；
3. 学术覆盖达到具名截止日与渠道分母；
4. 机器统观对声明的 CandidateClass 给出有界覆盖、无限公平或保真归约证书；
5. 最终报告可从 main 的来源、proof、run、失败和 checkpoint 重建全部重要主张。

未找到合格见证时，不得因工作量、局部 no-go 或“可能不存在”完成 Goal；保留未知并继续下一项有判别力的 bounded successor，除非用户明确修改目标。
