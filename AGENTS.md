# 顶层综合 Repo 工作规范

本文件是 `/Volumes/D/HoTT_AI_HANDOFF_20260911` 顶层新 repo 的项目级治理入口。它补充全局 `~/.codex/AGENTS.md`，不替代全局规则；若两者冲突，遵循更具体且不扩大授权的项目事实。项目目标是把 LocalGPT、WebGPT、Gemini 的历史工作、用户原始问题、理解章节和可验证产物组织成可持续的 HoTT 悖论/现实相对研究工作区。

## Goal任务治理化、全Session认知与角色恢复

标识：`GOAL_TASK_LOCAL_GOVERNANCE_V1` / `HIGHEST_DIRECTIVE_ROLE_LOADING_V1`。全局`repo-cognitive-closure`
仍是第一语义动作；本项目所有Session，包括T0/T1治理和机械任务，随后必须完整读取
`.codex/skills/hott-local-session-governance/SKILL.md`、`.codex/cognition/TASK_ROUTING.md`与单体`最高指示.md`。
先确认当前用户/实际Goal及角色，再使用材料；读取最高指示不自动启动数学研究。

- 最高指示在首次进入、跨Session、压缩恢复、角色切换或正文版本改变时无条件全文重读；研究/理论审计
  每换语义单元或主要靶前提也重读，不受通用receipt豁免。普通后续turn核角色与freshness，触发失效才重建；
  不把每条shell命令当新理论单元。角色为研究生成、独立审计、来源解释、治理对齐、机械背景，动作按最高指示§0A。
- 第三轮原A/B任务使用Goal6/Goal6-audit及Goal5领域细则；用户新开续做C/D时，完整读既有
  `hott-machine-overview-execution`/`hott-machine-overview-audit` Skill的Goal7分支和单体
  `goal-7.md`/`goal-7-audit.md`。Goal7承担父范围充分性修复与同一第三轮的接续，不是第四轮。
  旧final-002和旧完成状态是历史输入；C必须先论证父范围到研究集合的充分性，再完成研究，不能只结案自选集。
- `.codex`是本项目canonical Skill树。宿主未显示Skill菜单时仍按以上路径读取；隐式匹配、metadata、索引、
  hash和旧“已加载”不能替代全文。角色路由只选择方法，不授予Goal创建、模型运行、Sub Agent或写权限；唯一例外是本文件「模式 P 动态 DAG 的任务限定授权」所规定的、用户 2026-10-02 明确授权的 P-DAG 节点。
- 跨Session/压缩后，在业务判断之前重新完整读取本角色Skill和单体闭包、最高指示，并按PROTOCOL恢复当前
  状态/原文/证据。公开说明角色/Goal、已读版本/EOF、原意与成功标准、未完成项及下一动作；不索取隐藏推理。
- A/B/C/D均只在用户明确启动/继续后执行；方案、最大编号、旧日志或Skill存在不使研究自动复活。
  C/D的新包准备不创建宿主任务或改研究STATE。B/D只读研究/current owners，写各自获准审计路径，
  不checkpoint或提交Git；具体身份、路径和权限按TASK_ROUTING及对应Goal，不跨角色继承。

任务适用性评估、全局泛化与验收见`dev-docs/Goal任务项目治理化与全局复用方案-20260923.md`；当前路由由
`TASK_ROUTING.md`拥有，实际研究状态仍由STATE拥有。上述全Session附加义务优先于下表T0/T1加载豁免；
四件套原有适用档位、固定顺序、source-first语义再对齐、证明门禁和checkpoint合同保持。

## 当前工作根与来源边界

- 当前工作根必须是本目录的顶层 Git repo。开始前确认 `git rev-parse --show-toplevel` 等于本目录；`AI对话录/` 和 `workspace/` 是磁盘上保留的嵌套历史 repo，已由顶层 `.gitignore` 排除，不是当前工作根。
- `核心认知.md` 当前身份（generation、KC 分母、来源数）必须从 `STATE.current_core` 与 manifest 动态取得，本文与任何治理正文不得内嵌具体代数/分母数字。它保留三份历史 primary 与后续 hash-pinned 一手用户悖论/元数学原文的 curation 线，并允许通过 incremental curation 纳入新 generation；转发 AI、supplemental、一般治理、附件和操作指令仍留在来源/Git，不进入 current core。每次工作开始必须从第一行连续读到 EOF；manifest 只提供哈希、定位和处置，不能代替原文。`方向追踪.md`、`全景视野.md` 也必须按固定顺序全文加载。
- `理解章节/` 是历史认知闭包及本次 transform 的主要工作成果；它是需要继续审计、修订和分层的当前知识候选，不自动凌驾于底层代码、原始来源和 Git。
- `sources/` 是来源快照和提取原件区。除非用户明确授权，不在其中改写历史来源；需要修复提取规则时改 `scripts/audit/`，重建派生文件，并保留旧 hash/差异。
- `/Volumes/D/ALL-Markdown/aistudio-docs/` 按用户要求已移走且不恢复。`sources/local-gpt/HoTT_is_GONE_COMPLETE.md` 是有 hash 的历史 AI 产物，不是已经证明覆盖原目录的事实；覆盖结论必须标为 `NOT_PROVEN`，不得将旧 validator 的缺源 PASS 当成认证。
- `private-audit/` 被忽略并按最小权限保存本机 Codex 原始 trajectory。它是只读审计输入，不进入公开提交；审计 LocalGPT 时必须使用 canonical `session_trajectory.py`，不能另写 inline trajectory parser，也不能从隐藏推理推断事实。

## 启动闭包（每个新 Session、压缩恢复、跨目录接手）

1. 先读本文件、`README.md`、`MEMORY.md`、`feature-list.md`、`rulings.md`，确认当前需求、当前状态、开放问题和来源边界。
2. 读 `.codex/skills/hott-local-session-governance/SKILL.md`、`.codex/cognition/LOAD_SET.json`、`.codex/cognition/PROTOCOL.md`、`.codex/skills/SKILL_ROLES.json` 和 `.codex/research/hott/STATE.json`；先区分 lifecycle 与 evidence status。
3. 按 `核心认知.md` → `方向追踪.md` → `全景视野.md` → `扩展认知.md` 固定顺序全文读取**四件套**，记录 generation/版本、SHA-256、字节、行数和实际 EOF；读取不是哈希检查，工具输出也不证明模型理解。任一 profile/task 都不得删减或重排四件套。第四件是 AI 阐释层（`essay-role:v1`），`核心认知.md` 仍是唯一用户原文权威。
4. 纯治理/审计用 `plan --profile governance`；数学研究用 `plan --profile research`。选定 stable record 后先 `query --record <ID>`，再 `plan --profile research --task <ID>` 水合对应 `理解章节/`、`HoTT/`、代码、测试、运行产物和 Git 证据。`depends_on` 只表示会传播 stale 的真实验证依赖；动机、先后、叙事、研究归属和接续关系必须使用不递归水合的 `research_parent`/`related_records`。每次 task plan 都要检查 `hydration_diagnostics`，query-first 巨型账本不得被间接提升为正文，除非本任务明确以其全文为决定性证据。
5. 需要历史轨迹时，先使用 `audit/` 的覆盖入口、`sources/SOURCE_MANIFEST.json` 和 canonical reader 的输出，再回到原始文件。不能因“没有看到”断言不存在。

任何四件套/启动必读文件缺失、发生截断、源 hash 改变、Git 状态与记录不一致或无法区分历史/当前事实时，降低结论或进入 `BLOCKED_FULL_SET_COGNITION`，不要开始数学研究或用摘要补洞。先移除四件套之外的非必要载荷，不能裁剪用户核心原文。

## 逐轮核心语义再对齐

标识：`CORE_SEMANTIC_REALIGNMENT_V1`。四件套在 Session 中存在、曾经完整读过或已有 load receipt，
只证明材料可用，不证明当前回答仍按其含义工作。凡本轮要解释、概括、评价、质疑、修正或据以选择
用户的悖论观、数学哲学、现实同一性、时间／时序、构造过程、ASK、理论经济、圆环或其它 core 概念，
都必须在作出实质判断和检索外部通常解释**之前**执行 source-first 再对齐：

1. 从 `核心认知.md` 读取本题直接相关的完整 KC 原文；从 `扩展认知.md` 的索引定位并完整读取相关
   阐释 shard／小节。若用户问的是跨主题总论、纠正 AI 对原意的理解、指出偏航，或无法先确定相关
   KC，完整重读核心认知与扩展认知；方向／成果／MEMORY／近期审计均不得代替它们。
2. 先形成四项对齐：用户主张是什么；本轮不得把它收窄成什么熟悉问题；它怎样改变当前任务／证据
   选择；哪些证明义务仍然开放。只有完成这一步，才可调用外部文献或标准解释评价精确主张。
3. 最终回答若重述或批评用户原意，必须给出可点击的 KC／阐释 locator，并把“忠实复述”和“证据
   评价”分开。若不能忠实复述，停止评价并继续读取；不得以训练知识、近期 AI 报告或标准术语补洞。
4. T0/T1 的轻量豁免不适用于上述语义触发。纯机械工作可以不重读四件套，但不得顺带产出 core
   语义判断。压缩 receipt、hash、逐 KC 状态或旧 `ALIGNED` 标签也不能替代本轮实际消费。

本合同不要求每个文件操作都重新读取全部四件套，也不建设语义 Hook 或自动真理判定器。它修补的是
Session 级“已加载”与 turn 级“真正用于当前判断”之间的缺口；具体执行与证据边界见 PROTOCOL。

## 研究与证据纪律

本 repo 保存的是研究过程和认知交接，不预设 HoTT 必然矛盾，也不把用户的 Z 铁律直接当作已证明的元定理。研究必须区分：

- 数学对象被定义；命题被推导；算法可执行；某一次运行完成；对所有输入有效完成；现实对应可实施。这些状态不能互相冒充。
- HoTT 的内部规则、一般计算/反射界限、某个公理或现实解释的新增义务。共享机制可以有 HoTT 实例，但不能写成 HoTT 独有。
- 用户提出的方向 A（现实可完成而理论化引入额外完成困难）与方向 B（现实不可完成却把理论对象当作已获得能力）是研究方向/候选构造，不是未经核验的缺陷结论。
- AI 自述、旧文档 PASS、有限玩具模拟、文件存在、Git 提交和单次测试各自只能证明其明确范围。重要主张必须有多样审计锚点：用户原文、AI 可见回答、tool call/result、代码/文档、运行结果、Git commit 和当前 hash。

## HoTT 悖论的系统化程序探索与完备性意识

标识：`HOTT_PARADOX_PROGRAMMATIC_COMPLETENESS_V1`。用户要求机器统观、系统化/完整/完备探索、用编程激发悖论、
寻找未知或给出大范围负结论时，必须先加载项目级
`.codex/research/hott/HOTT-PARADOX-PROGRAMMATIC-EXPLORATION-COMPLETENESS.md` 的完整 v2 index 和索引声明的全部 shards，
再结合当前 machine-overview 动态计划/证据选择本轮有界任务。该项目计划拥有候选空间、程序化方法、未知入口和
阶段验收；分支 worktree 只保存实现与候选证据，不建立第二份项目治理真值。它不替代四件套、STATE 或底层 proof/run。

每个系统化 TaskSpec/评价必须定位到搜索张量：

```text
TheoryConstruct × AbstractionChange × RealityOrTask × ConsumerOrContext
× ObservationLayer × CompletionProperty × Oracle × FrameworkOrModel
```

并固定 exact calculus、CandidateClass、generator、reducer、consumer、observation、completion、denominator、controls、
coverage level、unknown ingress、失效和停止条件。程序化激发至少从会改变结论的方法族做 omission scan：typed term/proof
enumeration、规则/前提 mutation 与 ablation、层级提升/擦除、consumer/context synthesis、组合/反馈/self-reference、
differential/metamorphic/property-based、symbolic/model search、termination/productivity/proof search 及版本化社区源码/论文挖掘。

有限 grammar 的完备性需要成员分母、remainder=0 与 coverage proof/独立重算；无限 code 需要 dovetailing/fairness；
从小 grammar 外推较大候选类需要 total、typed、task/consumer/observation/completion-preserving reduction。
`NO_HIT_WITHIN_SCOPE`、timeout、文件/测试/关键词数量、LLM 一致和目录全读都不能成为全局 HoTT 不存在或全理论完备。

不能提前命名的候选从新论文/版本/实现/consumer、新理论维度/激发算子/oracle、跨框架差分、反例和新的现实任务进入。
每个 bounded pass 结束必须执行遗漏审计并至少使用一个独立 taxonomy/source/framework/holdout 寻找 out-of-envelope；
unexpected result 要定位旧 envelope 漏项、修订分类、重评依赖结论并形成下一有界 successor，不能只增加案例。

每轮 Session 在逐 KC 回评之外，记录本轮覆盖 cells、未触达轴、enumeration/fairness、reducer 换题风险、oracle 假阳/假阴、
HoTT essentiality、现实对应、holdout/out-of-envelope、taxonomy 修订与下一停止条件。开放世界持续存在不阻止当前有界
pass 完成，也不授权永不停止任务、常驻审计 AI、语义 Hook 或第二份手工数据库。

## 数学结论交付前机器证明门禁

<!-- math-proof-delivery-gate:v1
proof_source_root: HoTT/formal
proof_run_root: HoTT/verification/runs
proof_index: HoTT/CLAIM_EVIDENCE_MATRIX.md
-->

标识：`MATH_PROOF_BEFORE_DELIVERY_V1`。本 repo 中，当前 AI 在最终答复、研究正文、方向/成果投影或当前状态中把一个数学命题作为已经成立的**数学结论**交付之前，必须完成与该精确命题相称的机器证明。数学结论包括但不限于定理、引理、等价、蕴含、不可能性、存在/不存在、全称性质、反例所否定的一般命题，以及被提升为已证事实的模型性质。

交付 Gate 按下列顺序执行：

1. 固定稳定 claim/proof ID、命题全文、量词、假设、公理、宇宙/类型论变体、依赖和禁止外推；自然语言结论必须能与形式命题逐项对照。
2. 将证明源码、项目文件和必要的锁定依赖信息保存到 `HoTT/formal/` 的合适 topic/claim 子目录；不得把聊天代码块、内存变量或 `/tmp` 中的唯一副本当作证明资产。
3. 使用能验证该命题真实语义的 proof assistant/kernel 实际运行。HoTT、univalence、cubical path、HIT、截断或高阶结构相关结论必须使用相应原生系统，或另有已机器证明的保真翻译；普通 Lean `Eq`、Python 枚举或有限测试不得冒充原生 HoTT 证明或无限/全称定理。
4. 把每次作为交付依据的运行保存到 `HoTT/verification/runs/<run-id>/`；至少包含 `RUN.json`、原始 `stdout.txt`、`stderr.txt`、`environment.txt` 和 `source-manifest.json`，记录工具/版本、命令、退出状态、源码与依赖哈希、时间、结论范围以及失败。临时构建缓存可以位于 `/tmp`，但最终证据不得只存在于 repo 外。
5. 在 `HoTT/CLAIM_EVIDENCE_MATRIX.md` 中建立或更新唯一索引行，连接 claim ID、proof ID、形式命题、源码、run receipt、证据等级和禁止外推；随后检查所有路径、哈希和实际 kernel 结果。
6. 只有 Gate 1–5 全部通过，才可使用 `MACHINE_PROVED` / `FORMAL_CHECKED_WITH_SCOPE` 或“已证明/数学结论”等交付措辞。Git 未获授权或尚未提交时，必须另标 `LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED`，不能声称跨 Session/机器可恢复。

无法完成机器证明时，不得把该命题作为数学结论交付。可以继续保存和讨论，但必须降格为 `QUESTION`、`CONJECTURE`、`HEURISTIC`、`PAPER_ONLY`、`COUNTEREXAMPLE_CANDIDATE` 或 `SOURCE_REPORTED_NOT_REPLAYED`，并明确缺少的证明义务。外部论文或历史 AI 声称的定理可以按来源身份转述，但在本 repo 重新运行前不能冒充“当前 AI 已机器证明”。有限穷举/模型检查只有在有限域、完备枚举和命题对应关系均固定时才证明该有限命题。

本门禁不要求把每个猜想都强行形式化，也不禁止在证明前探索；它要求的是：**未证明的内容不能被交付为已经成立的数学结论。** 详细合同见 `docs/quality/数学结论机器证明与证据留存规范.md`。

## 长治理文档分片与索引

标识：`GOVERNANCE_SHARD_INDEX_V2_PROJECT_V1`。命中 `governance-shard-index:v1/v2` 的 canonical 路径是**逻辑文档索引**，不是摘要：先读完整 shard table、`last_shard` 和顺序追加型的 `append_target`，再按任务读 owner shard；顺序追加型必须同时读 `append_target`。不得把索引、首片或末片冒充全文，也不得在索引末尾追加正文。

- 约 300 行是写作/换片软目标，不是上限、错误条件、发布 Gate 或清理配额；超行只在 validator 输出 `NOTICE`。
- 判定标准是“持续追加、妨碍定位、稳定入口与长历史混装、存在自然语义边界”，不是行数；高度内聚、通常必须全文读取，或属于来源快照、历史交付分卷、machine-managed 数据的文档保持单文件。
- 新逻辑文档必须用 v2：canonical 路径保留为索引，正文放同名 `NNN - 子主题.md` shard 目录；索引链接标题、文件名主题与 shard 第一个 H1 一致；新建 shard 必须与索引行、`last_shard`、`append_target` 在同一次提交或同一个 checkpoint 事务中更新。
- `.codex/tools/cognition_runtime.py` 3.6.1 在加载链上强制“索引 + 按 table 顺序全部分片”的全文覆盖；即使某个分片先因 active record 或直接 source 被单独选中，一旦其 canonical index 进入同一 plan，也必须把该分片恢复到索引后的 table 顺序。结构错误（缺片、未列片、标题/`last_shard`/`append_target` 不符）一律 fail closed；受 checkpoint 管理的逻辑文档分片同时进入 `HEAD.json.tracked`，只能与索引在同一原子事务中写入。
- 机械校验：`python3 -B scripts/audit/verify_governance_shards.py`；机械 PASS 只证明结构，不证明分片边界合理或内容完整。
- 每个索引前 15 行必须带首屏 banner（`> ⚠️ 逻辑文档索引：全文 = 本索引 + 下方 N 个分片；缺一片即未完成…`）；缺失或残缺会被同一校验器判为失败，避免"只打开索引就以为读完"。
- 完整项目合同见 `docs/quality/长治理文档分片与索引合同.md`；共享权威为 3.16.0 候选规范 `/Users/aurolafly/codex-worktrees/long-doc-sharding-3.16.0/docs/governance/长治理文档分片与索引规范.md`。
- 已分片：`README.md`、`MEMORY.md`、`理解章节/C1`–`C4`、`方向追踪.md`、`全景视野.md`、`扩展认知.md`（AI 阐释层）；当前分片数与方向／结果行数一律从各自索引和投影身份字段动态取得，不在本文件固化。大表按家族拆成行分片时，每片自带表头两行（唯一允许的重复内容），投影的身份字段（marker 块、`source_state_revision`、`projection_generation`、`semantic_status`）必须留在索引里。
- 保留单文件并登记触发条件：`核心认知.md`（四件套中唯一单文件；由 curation+manifest hash 管理，KC 平铺列表，改动须经 manager）、`HoTT/CLAIM_EVIDENCE_MATRIX.md`、`AGENTS.md`、已完成审计报告、来源快照与历史分卷。

## 写入、Git 与交接

- 新增或修改需求、当前状态、稳定设计、审计账本、验证结果、研究方向或研究成果投影时，按 `.codex` 的唯一 owner 路由写回；不要制造第二份当前真值。只有用户新的悖论/元数学原文或对此类工作意识的明确修正进入 core generation；一般治理裁定进入 rulings/Feature；候选/优先级/下一动作进入 `方向追踪.md` + STATE，结果/证据/失败/未知进入 `全景视野.md` + 底层 evidence owner。
- 当前人工纳入/排除与语义边界 owner 必须从 `STATE.current_core.curation` 动态取得，不在本文内嵌具体文件名；`scripts/audit/build_core_cognition.py` 是 core/manifest/transition 的 canonical manager。默认只检查，显式 `--write` 才生成；不手工润色生成物。新增用户悖论/元数学原文时建立 hash-pinned source、新 generation 和全量迁移收据，旧代由 Git/tag 与 curation lineage 保留，不在生成物末尾手工追加。
- 每个工作单元结束前，按修订片 020 产出**分片审计集** `.codex/research/hott/sessions/<session-id>/CORE_COGNITION_AUDIT.md`（索引）+ `CORE_COGNITION_AUDIT/` 分片：核心认知逐条五元组论证（含反证条件）、扩展认知逐段落论证、「已走过的路」航向复盘与「即将作出的选择」偏航分析。不能用“总体一致”替代逐编号遍历；旧的单文件审计是 archive evidence 与历史格式，不自动成为下轮输入。
- `.codex/tools/cognition_runtime.py` 的 `plan/read/check` 是只读加载器；checkpoint 默认 dry-run，只有用户已授予的写权限和显式 `--apply` 才能写入状态。每个 applied checkpoint 必须在同一事务中写入 `SESSION.md`、`RUNS.json` 和通过当前 generation 全量/顺序检查的 `CORE_COGNITION_AUDIT.md`，并产生 `.codex/cognition/checkpoints/<session-id>/transaction.json`、before/after 副本和 `result.json`。只有 canonical `result.json.status=CHECKPOINT_COMMITTED` 才能证明 checkpoint 已应用；Session 自写的 `POST-CHECKPOINT.json` 只能引用该收据，不能自我证明。历史缺收据只能登记缺口，禁止追溯伪造事务。
- Git 操作遵守全局基线规范：精确检查 dirty/index，保留既有嵌套 repo 与用户修改，精确 stage，提交后回读 HEAD、hash、验证结果。顶层 repo 的本次初始化与提交由用户本轮明确授权；不自动 push、发布、恢复已移走目录或删除历史。

## 模式 P 动态 DAG 的任务限定授权（用户 2026-10-02）

2026-09-17 的 blanket Sub Agent 禁令保留为历史规则，并继续约束本项目的一般工作；用户 2026-10-02 对**模式 P 的 P1/P2/P3 共同锻造、ZFC 定位与 HoTT 盲重放**作出任务限定的后续授权：Master 可以按证据依赖建立动态 DAG，启动不同刀具、来源核对、控制和 Battle 节点，并逐节点决定是否允许联网、只读 `dev`／`main`／其它分支或保持无泄漏盲态。

- 唯一执行入口是 `.codex/skills/hott-pattern-p-dynamic-dag-orchestration/SKILL.md` 与 `dev-docs/模式P动态DAG调度.md`。它们规定 TaskCard、NodeCard、访问等级、有界 Battle、Master 裁决、收据与停止；Skill 的存在不自动启动节点。
- 当前任务限定的 worker 请求固定为 `gpt-5.6-terra / max`，只读、无递归、无 Git/current-owner 写权。不得以原生 `spawn_agent` 的其它 profile/model/effort 作静默替代；默认一轮至多三名并行 worker，Battle 按依赖串行，新增节点必须有明确 gap/冲突触发。
- `BLIND_CARD` 不得读取项目已有答案、分支或网络；来源／控制／Battle 节点的可见材料和网络权限由 Master 在 NodeCard 中逐项列出。网络、`dev`、`main` 或其它分支的读取是证据权限，不是 worker 的一般权限。
- Battle 不是多数投票，也不索取隐藏思维。worker 只能交付公开的 MatchTrace、来源与反事实；Master 可以提出 claim，但该 claim 必须接受独立质询，最终以一手 source、同一任务控制和相称运行证据裁决。
- 只有 Master 写回本项目 current owners。App Server 仅在 exact model/effort 与 read-only sandbox、approval policy 得到实际资格化后使用；当前未资格化时使用已验证的 fresh CLI lane，或停止相应节点。发现旧的 native Sub Agent 句柄仍只关闭、登记，且不把它们当作 P-DAG 证据。
- 此 scoped exception 不授权一般 swarm、写入委派、推送、发布、凭据访问、外部系统 mutation 或把 DAG 输出升级为数学结论。研究发起人随后明确授权：P-DAG 的刀具规格、来源／Battle／timeout 收据和必要路由更新在完成精确 baseline、验证与 owner 回读后，应以**精确路径 Git commit**保留审计谱系；该授权不扩大到无关 dirty 路径、tag、push 或发布。其它任务仍适用原禁令和全局 `repo-subagent-governance` 合同。

## HoTT 创建动机反投影 ZFC 文献调查（用户 2026-10-03）

研究发起人已将“HoTT 作者为何在已有集合论基础下仍提出 HoTT”的文献调查，设为反投影 ZFC 候选来源的独立项目；唯一调用名是 `HOTT-MOTIVE-ZFC-SOP`。它由 `.codex/skills/hott-motive-zfc-literature/SKILL.md` 与 `dev-docs/HoTT创建动机反投影ZFC文献调查SOP.md` 共同拥有，路线种子是 `dev-docs/菲尔兹奖后续理论级目标路线图/009 - HoTT创建动机反投影ZFC候选路线.md`，项目档案根是 `audit/HOTT-MOTIVE-ZFC/README.md`。

- 仅在用户明确引用该 SOP、要求彻底调查／存档或继续该项目时启动。调用会授权 SOP 所定义的公开来源调查、R/Z/Q 卡和项目档案；它不因一个动机关键词自动启动，也不自动恢复其它 Goal。
- 每项必须经过 `R_i（HoTT 原典动机）→Z_i（精确集合论侧规则／代价／消费者）→Q_i（模式 P 与同一任务资格）`。作者动机不是 ZFC 不一致或缺陷的证据。
- `H0→Z0→Q0` 是专用传输门；ZFC 侧若在对象、formation、同一任务、未支付完成性、P2/P3形状或控制上不保真，判为 `ANTI_ANALOGY_CONTROL`，不得改写成 ZFC 无问题或调查失败。
- P-DAG、worker、模型运行、数学STATE、Power Set station切换、数学结论和新刀都需各自的现行授权与合同；该文献 SOP 不以“彻底调查”名义扩大权限。

## ZFC Q 可追溯语料落盘、MinerU 与文献地图（用户 2026-10-03）

研究发起人要求将“尽可能完成与 ZFC Q 有关文献的发现、全文落盘、MinerU 派生处理和可追溯地图”建立为独立项目；目标是为模式 P、Power Set、H0→Z0 与其它明显理论位置寻找可靠的 Q 线索，不是写博士论文或将书目数量变成结论。唯一调用名是 `ZFC-Q-CORPUS-MAP-SOP`，由 `.codex/skills/zfc-q-corpus-map/SKILL.md` 与 `dev-docs/ZFC-Q语料落盘与文献地图SOP.md` 共同拥有，项目档案根是 `audit/ZFC-Q-CORPUS-MAP/README.md`。

- 仅在用户明确引用该 SOP、要求继续该语料工程或要求其某个明确阶段时启动。调用授权其定义的公开元数据／全文发现、原件落盘、PDF 核验、MinerU 本地派生、地图与 Q lead routing；不自动授权 P-DAG、worker、数学STATE、Power Set station、新刀、数学证明、tag、push或发布。
- `全部文献`的操作含义是冻结并持续扩展的 corpus 内尽可能完整的 acquisition/map closure，不是声称全世界相关文献绝对穷尽。访问失败、付费墙、语言／版本限制和未处理引用必须保留为 remainder。
- DOI、作者、出版社、arXiv、正式会议／项目档案是作品身份和原文权威；浏览器下载页及用户提供的访问路线（包括 `sci-hub.jp`）只记录为 access provenance，不能单独证明版本、题录、原文内容或候选结论。每个获得的 PDF 必须按获取 SOP 核对 PDF 身份、题名、页码／文本层和哈希；MinerU 输出是派生阅读材料，不覆盖原件。
- `HOTT-MOTIVE-ZFC-SOP` 是总语料工程的一条已建立支线：其现有 run 作为 corpus seed／control，不重复复制也不因进入总语料自动升级为 Q。

## 任务路由（v5 分档）

治理强度与任务风险成正比。档位四变量：**主张风险 × 自治程度 × 视界长度 × 状态改写**；会话首条声明档位并记入 SESSION.md，越档即停（任务中途升级→立即升档过门，不允许"先交付后补证"）。

| 档 | 判据 | 启动加载义务 | 结束义务 | 硬门禁 |
|---|---|---|---|---|
| **T0 lite** | 只读/单会话/无主张/可重来 | 本文件 + `MEMORY/001` 队列片 + 任务文件（≈1.5 万 est tokens） | 无（对话内交代） | 来源边界；禁 Sub Agent；不 push |
| **T1 standard** | 写代码/文档；无数学主张 | 启动核（STATE 按 hot 字段消费：`current_core/active/latest_session/unresolved/revision`，命令 `python3 -c "import json;s=json.load(open('.codex/research/hott/STATE.json'));print(json.dumps({k:s[k] for k in ('current_core','active','latest_session','unresolved','revision')},ensure_ascii=False,indent=1))"`） | 轻量 SESSION.md（含 host/model/tier）+ 触及集 KC 复认 | + 写回归属表；validator |
| **T2 research** | 数学研究/系统化探索 | T1 核 + **四件套全文** + 业务 Skill + 三问 + FRONTIER/LESSONS/RESUME hot（≈12–18 万） | 分片审计集（触及集计量） | + 完备性回评（系统化任务另加载程序化完备性规划） |
| **T3 mutation** | checkpoint/数学结论/core 更新/投影写回 | T2 全量 + STATE 全文 | 全量 KC 审计 + 原子事务收据 | + F-011 机器证明门禁；`result.json` 唯一收据 |

领域附加条款（不随档位豁免）：HoTT 悖论研究每轮推进一个可检查构造/未知点，并在父级覆盖包络记录 cell、遗漏与 successor；方案执行走 `hott-paradox-search-sop`（七段循环 + 反思清单；方案优化必须 git 提交 `plan-revise(...)`，步骤提交携带反思结论，不提交不得继续下一步；当前步骤由 `goal-1.md` 索引、权威是 STATE）；历史审计/交接不自动启动新数学研究；修改本地治理框架须先重建 closure、按全局自维护 Gate 识别 C01–C10、验证并提交，不误改 dirty 的共享治理主库；来源快照与环境冲突时保留双方、记录 conflict/unknown，不得用新名/new hash 掩盖。压缩/跨会话重付按 `PROTOCOL` 收据制复认执行（全文重付仅在三触发器：core hash 变/升档/用户指令）。

本项目的成功标准不是文件数量，而是未来 AI 能在有限误判风险下知道“用户要什么、过去各 AI 实际做了什么、哪些产物可复现、哪些结论未证实、当前应从哪里继续，以及本轮是否沿着全部核心认知航向工作”。

## 积极思考

你的回复风格，有时候缺乏一种主动性。就是让我看不到足够充分的你的工作的价值，和后续的有价值的工作是什么？

其实有些事情你可以自己想出来，怎样继续做，就会让跟奇妙的事情被看到或者说发生。

所以我认为你应该对自己即将给用户汇报的工作结果进行更为积极和全面的思考，并且你的回复不应该是过于干脆俐落的，而是应该让内容更为饱满和平滑的。

## 简体中文优先

尽量使用简体中文回答用户的问题，但是必要的术语、词汇是可以使用英文的。
