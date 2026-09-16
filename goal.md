# HoTT 非现实性悖论系统化机器统观 Goal

> 状态：`ACTIVE`  
> Goal schema：`hott-machine-overview-goal/v2`  
> 唯一 current objective owner：本文件  
> 工作根：`/Volumes/D/HoTT_AI_HANDOFF_20260911`  
> Git 工作面：顶层 repo 的 `main`  
> 截止日口径：2026-09-14  
> 方法 owner：`.codex/research/hott/HOTT-PARADOX-PROGRAMMATIC-EXPLORATION-COMPLETENESS.md`  
> 状态 owner：`.codex/research/hott/STATE.json`  
> App Goal：`完成 goal.md 制定的内容，过程中持续更新需要更新的治理框架要求维护的文档，确保未来的你能够跨越多个压缩边界，始终保持认知连贯。注意你的工作措辞，不要引发安全警报！`  
> 说明：本文件定义完整目标；文件存在、计划完成或局部证明均不证明 Goal 已完成。

## 1. 最终目标与禁止误报

在唯一当前工作根的 main 中持续、自主推进“HoTT 非现实性悖论的系统化机器统观”，直至取得至少一个严格合格的现实相对悖论见证，并闭合机器证明、HoTT 必要性、现实同任务对应、学术定位、统观覆盖证书和可复现证据。

不得把下列结果误报为 Goal 完成：计划或治理框架完成；一次超时；固定循环；一般不可判定性；一般 Gödel 不完备性；外部 proof-search 发散；普通表示边界；synthetic implication；理论正确拒绝错误输入；HoTT 中可表达的普通计算问题；尚未找到反例的 bounded negative。

## 2. Session 恢复与单工作面

每次新 Session、压缩恢复或范围变化，先从 main 完整加载：

- 项目及目录 `AGENTS.md`、`repo-cognitive-closure`；
- `hott-local-session-governance` 与 `hott-paradox-research`；
- 四件套全文；
- `STATE`、`MEMORY`、`FRONTIER`、`RESUME`；
- `.codex/research/hott/HOTT-PARADOX-PROGRAMMATIC-EXPLORATION-COMPLETENESS.md` 的索引和全部分片；
- 本文件与 active record `A-HOTT-MACHINE-OVERVIEW-GOAL-002`、历史兼容记录 `A-HOTT-MACHINE-OVERVIEW-GOAL-001`、`A-HOTT-PROGRAMMATIC-COMPLETENESS-001`、`A-COMPUTABILITY-LITERATURE-COVERAGE-AUDIT-001`、`A-LIT-CLASSICS-001`、单工作面决定。

外部 `/Volumes/D/HoTT-machine-overview` 只作只读候选来源。所有决定性计划、状态、源码、run、来源身份、失败、反证和 checkpoint 必须进入 main 的正确 owner。不得让未来 Session 依赖外部 worktree 中未导入的 current truth。

## 3. 当前已验证基线：从这里继续，不重复开工

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

## 4. 当前第一 successor

上一轮三条薄切、2LTT replacement 数学核、natural-consumer 消融、CE-MAP v1 与 R3 source replay 都已形成真实链。CE-MAP 已把 revision 149 的 478 个具名输入全部登记；C-244–C-249 已关闭一个 exact R3 基准，但没有把一般一阶不完备性偷换成 HoTT 结论。当前按判别力推进：

1. `R4-HOTT-NAT-EFFECTIVITY-001`：R3 已闭合；现在比较 cubicaltt/redtt/cooltt/cctt，选择同时具 Nat/Path/conversion 的 exact target，并以闭合证明输入规范把 holes/undefined/未解目标与无终止性证明的递归明确列为域外构造；先推进 H-NAT/H-ID-PATH/H-CONVERSION/H-EFFECTIVITY；
2. `CLASSIFIER-REALITY-BRIDGE-001`：继续检查是否有真实 consumer 需要 local/open classifier 且拒绝 crisp、transport 或 pointwise-fibrant 支付；不得把扩大后的 local task冒充与 global task相同；
3. 保持三个并行返回口：Oracle Modalities 的 Agda 2.6.4.3/Cubical v0.7 重放与 modal→ambient consumer；R2 ambient 无条件 no-decider／ProgramCode 对应；物理时间/时空连续性与现实同任务桥梁。

`NATURAL-CONSUMER-002` 已找到真实调用链，但 crisp、degenerate+transport 和 pointwise-fibrant 限制能够完成来源中声明的真实任务；故固定为 `DEFENSE_WORKS_WITH_EXPLICIT_PAYMENT`，不是 Goal 终点。CE-MAP 已将该同型 no-go 归约为一个带 anti-preservation 的 pattern class。现在优先选择未被防线覆盖的 Gödel/R4 cell；不以已完成 R3 机器证明保护候选。

## 5. 文献覆盖剩余义务

文献与代码交替推进。以 2026-09-14 为具名截止日，继续 current LIT owner 中尚未闭合的：

- Post 的 Friedberg–Muchnik／2024 CIC forward chain，及 Rice–Shapiro、Tarski、Hilbert–Bernays、Löb、Lawvere、Rogers／Myhill、Chaitin；
- Kleene normal form、s-m-n、recursion theorem；
- termination、partiality、dominance、guarded／clocked recursion；
- 2024–2026 Oracle Modalities 的旧工具链/论文对账、Post hierarchy、synthetic computability、cubical cofibration complexity、ordinal decidability、groupoid-syntax citation chain、Extension Types、Agda Gödel、MetaRocq、Lean Foundation。

每项记录版本／hash、精确 theorem 与 assumptions、阅读范围、TaskSpec 映射、反解释、遗漏和 replay 状态；完成 backward／forward citation chaining 与独立 holdout。只声明具名截止日与渠道分母内的覆盖，不把搜索未命中写成不存在。

## 6. CE-MAP 与机器统观完备性

`CE-MAP-001` v1 已完成具名 revision-149 分母登记，把 cases、evaluations、formal packages、claims、STATE records 和文献路由映射到八轴张量：

`TheoryConstruct × AbstractionChange × RealityOrTask × ConsumerOrContext × ObservationLayer × CompletionProperty × Oracle × FrameworkOrModel`。

当前 478/478 canonical items、69 个显式 `UNCLASSIFIED`，产物由 `scripts/audit/build_ce_map.py` 查询和验证。下一轮继续推进六类生成器：typed synthesis、rule mutation/ablation、consumer synthesis、self-reference/universal computation、metamorphic/differential、source/AI-guided。

- 有限 grammar：给 coverage proof 与 remainder=0；
- 无限 code：给公平 dovetailing／no-starvation；
- 类级外推：给保持 task、consumer、observation、completion 的 total typed reduction；
- 始终保留 OP-14 反解释、coverage shadow、out-of-envelope 和 unknown ingress。

## 7. 计算阶梯

- R0：有限观察窗未完成，只作观察。
- R1：固定程序发散；不算最终悖论。
- R2：闭合程序码、decoder、bounded evaluator、公平枚举、正半判定、universality/reduction；当前另闭合显式 EPF_bool/SCT 前提下的 internal no-decider，ambient 无条件结论仍开放。
- R3：一般 formal-system/Robinson-Q 条件基准 C-244–C-249 已 exact replay；当前 target HoTT 的 proof code/classifier、`Universal θ`、算术解释、strong separation/representability、s-m-n／自应用、fixed point 与 independent sentence 仍属于 R4 bridge义务。
- R4／`G-HOTT-SYNTAX-001`：首个 Π/U/El/groupoid-coherence exact slice 已重放；继续补 syntax、judgment、conversion、proof checking/enumerability、Nat、dependent substitution、Path/univalence/HIT 与 inner/outer metatheory，取得 exact HoTT incompleteness 或精确边界。
- R5：只有 trusted HoTT rules 推出 `⊥` 才能使用；其它结果不得称 HoTT 内部矛盾。

## 8. 始终并列的方向 A、方向 B 与时间／时序

方向 A：理论引入连续性、稠密性、无限细分、商化、同一化、时序坍缩或额外相干义务，使现实可完成任务在理论中无法完成。

方向 B：理论绕过 ASK，把 mere existence、Path、外部解释、部分分类、有限近似或可证明性提升为 chosen witness、当前归约、内部自知、总求解、精确完成或实际交付。

“时间”保留对时空、运动、连续／非连续及稠密性的结构问题；“时序”保留对先后、依赖、当前可用、构造和验证落定顺序的问题。Gödel、Kleene、Lawvere、Löb 必须服务方向 A/B，不能取代现实相对问题。

## 9. “机器证明不能停机”的最终候选资格

只有下列链条贯通时，它才成为最终候选：

1. 明确对象程序、证明搜索、反射或自验证过程；
2. 以不变量、共归纳、不可分离性或经证明的保真归约机器证明不完成；
3. 定位具体 HoTT 抽象／资格变化，并以消融证明其必要性；
4. 找到预先冻结的自然 consumer；
5. 与现实侧保持同一任务、输入、观察和完成标准；
6. 证明方向 A 或 B 的不相容；
7. 通过正控制和最强竞争解释。

若只得到一般计算边界或 HoTT 中可表达的普通停机问题，登记为 R0–R3 或 `GENERIC_MECHANISM_WITH_HOTT_INSTANCE` 并继续。

## 10. 每个 bounded unit 的完成要求

每个有界工作单元必须保存真实 `input → candidate → oracle → evidence` 链，记录失败、反例、换题风险、未触达轴和下一 successor。遇到防线就更新候选并换构造／consumer，不重复堆叠小循环。

数学结论必须在 main 的 `HoTT/formal/`、`HoTT/verification/runs/`、`HoTT/CLAIM_EVIDENCE_MATRIX.md` 完成 F-011，并通过 STATE、projection、MEMORY、session、36-KC audit 和 canonical checkpoint 保存连续性。

## 11. 唯一 Goal 完成门

只有同时满足以下条件，才标记 Goal `complete`：

1. 至少一个候选贯通“exact HoTT 规则／表示 → 抽象或资格变化 → natural consumer → 机器证明的不完成／不相容 → HoTT 必要性 → 现实同任务对应 → 方向 A 或 B”；
2. 通过最强反解释与独立或跨框架复核；
3. 学术覆盖达到具名截止日与渠道分母；
4. 机器统观对声明的 CandidateClass 给出有界覆盖、无限公平或保真归约证书；
5. 最终报告可从 main 的来源、proof、run、失败和 checkpoint 重建全部重要主张。

未找到合格见证时，不得因工作量、局部 no-go 或“可能不存在”完成 Goal；保留未知并继续下一项有判别力的 bounded successor，除非用户明确修改目标。
