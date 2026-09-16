# 顶层综合 Repo 工作规范

本文件是 `/Volumes/D/HoTT_AI_HANDOFF_20260911` 顶层新 repo 的项目级治理入口。它补充全局 `~/.codex/AGENTS.md`，不替代全局规则；若两者冲突，遵循更具体且不扩大授权的项目事实。项目目标是把 LocalGPT、WebGPT、Gemini 的历史工作、用户原始问题、理解章节和可验证产物组织成可持续的 HoTT 悖论/现实相对研究工作区。

## 当前工作根与来源边界

- 当前工作根必须是本目录的顶层 Git repo。开始前确认 `git rev-parse --show-toplevel` 等于本目录；`AI对话录/` 和 `workspace/` 是磁盘上保留的嵌套历史 repo，已由顶层 `.gitignore` 排除，不是当前工作根。
- `核心认知.md` 当前身份必须从 `STATE.current_core` 与 manifest 动态取得；本轮为 `core-cognition-generation-4`/36 个 `KC-*`。它保留三份历史 primary 的既有 27 个用户原文单元，并允许以后把 hash-pinned 的一手用户悖论/元数学原文通过 incremental curation 纳入新 generation；转发 AI、supplemental、一般治理、附件和操作指令仍留在来源/Git，不进入 current core。每次工作开始必须从第一行连续读到 EOF；manifest 只提供哈希、定位和处置，不能代替原文。`方向追踪.md`、`全景视野.md` 也必须按固定顺序全文加载。
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
- 已分片：`README.md`、`MEMORY.md`、`理解章节/C1`–`C4`、`方向追踪.md`（5 片 / 28 条方向行）、`全景视野.md`（8 片 / 90 条结果行）、`扩展认知.md`（8 片，AI 阐释层）。大表按家族拆成行分片时，每片自带表头两行（唯一允许的重复内容），投影的身份字段（marker 块、`source_state_revision`、`projection_generation`、`semantic_status`）必须留在索引里。
- 保留单文件并登记触发条件：`核心认知.md`（三件套中唯一单文件；由 curation+manifest hash 管理，KC 平铺列表，改动须经 manager）、`HoTT/CLAIM_EVIDENCE_MATRIX.md`、`AGENTS.md`、已完成审计报告、来源快照与历史分卷。

## 写入、Git 与交接

- 新增或修改需求、当前状态、稳定设计、审计账本、验证结果、研究方向或研究成果投影时，按 `.codex` 的唯一 owner 路由写回；不要制造第二份当前真值。只有用户新的悖论/元数学原文或对此类工作意识的明确修正进入 core generation；一般治理裁定进入 rulings/Feature；候选/优先级/下一动作进入 `方向追踪.md` + STATE，结果/证据/失败/未知进入 `全景视野.md` + 底层 evidence owner。
- 当前人工纳入/排除与语义边界 owner 必须从 `STATE.current_core.curation` 取得（本轮为 `scripts/audit/core-cognition-curation-v4.json`）；`scripts/audit/build_core_cognition.py` 是 core/manifest/transition 的 canonical manager。默认只检查，显式 `--write` 才生成；不手工润色生成物。新增用户悖论/元数学原文时建立 hash-pinned source、新 generation 和全量迁移收据，旧代由 Git/tag 与 curation lineage 保留，不在生成物末尾手工追加。
- 每个工作单元结束前，生成 `.codex/research/hott/sessions/<session-id>/CORE_COGNITION_AUDIT.md`，逐一列出当前 generation 的全部 `KC-*`：对齐、深化、纠偏、张力、偏航或不适用，并附本轮证据定位。不能用“总体一致”替代逐编号遍历；旧审计是 archive evidence，不自动成为下轮输入。
- `.codex/tools/cognition_runtime.py` 的 `plan/read/check` 是只读加载器；checkpoint 默认 dry-run，只有用户已授予的写权限和显式 `--apply` 才能写入状态。每个 applied checkpoint 必须在同一事务中写入 `SESSION.md`、`RUNS.json` 和通过当前 generation 全量/顺序检查的 `CORE_COGNITION_AUDIT.md`，并产生 `.codex/cognition/checkpoints/<session-id>/transaction.json`、before/after 副本和 `result.json`。只有 canonical `result.json.status=CHECKPOINT_COMMITTED` 才能证明 checkpoint 已应用；Session 自写的 `POST-CHECKPOINT.json` 只能引用该收据，不能自我证明。历史缺收据只能登记缺口，禁止追溯伪造事务。
- Git 操作遵守全局基线规范：精确检查 dirty/index，保留既有嵌套 repo 与用户修改，精确 stage，提交后回读 HEAD、hash、验证结果。顶层 repo 的本次初始化与提交由用户本轮明确授权；不自动 push、发布、恢复已移走目录或删除历史。

## 任务路由

- 只做历史审计/交接：读治理 Skill 和审计脚本，不自动启动新数学研究。
- 继续 HoTT 悖论研究：先完成本文件与本地治理 Skill 的闭包，再加载业务 Skill `hott-paradox-research`；系统化/机器统观任务还必须加载项目级程序探索完备性规划。每轮推进一个可检查构造/未知点，同时在父级覆盖包络中记录其 cell、遗漏与 successor。
- 执行"用现实对齐找出 HoTT 非现实前提"的方案步骤、或走完一步后做反思：先完成本文件与本地治理 Skill 的闭包，再加载执行 Skill `hott-paradox-search-sop`（七段执行循环 + 反思清单 + 方案演化 git 纪律）；当前步骤由 `goal-1.md` 索引、权威是 STATE。每次方案优化必须 git 提交（`plan-revise(...)`），每个步骤提交必须携带反思结论；不提交不得继续下一步。
- 修改本地治理框架：先重新建立 closure，再按全局治理自维护 Gate 识别 C01–C10，修改 owner、schema、脚本和运行入口，执行验证并提交；项目专属变化不误改 dirty 的共享治理主库，不把 WebGPT 历史副本当作当前 host 配置。
- 发现来源快照与实际环境冲突：保留双方、记录 conflict/unknown 和适用范围；不得用新文件名或新 hash 掩盖冲突。

本项目的成功标准不是文件数量，而是未来 AI 能在有限误判风险下知道“用户要什么、过去各 AI 实际做了什么、哪些产物可复现、哪些结论未证实、当前应从哪里继续，以及本轮是否沿着全部核心认知航向工作”。
