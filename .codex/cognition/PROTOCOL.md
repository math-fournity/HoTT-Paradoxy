# 顶层综合 repo 认知与交接协议

版本：`handoff-cognition/v3.0`（v5 分档版，2026-09-18；v2.6 及以前见 Git 历史）。本协议是本 repo 的当前执行合同；它参考并重写适配了 WebGPT 快照中的双 Skill 治理，但不把快照中的旧 root、旧 host 状态或旧 PASS 当成当前事实。**v3 变更**：档位判定第 0 步与分档深度、STATE 按档消费（hot 字段 vs 全文）、压缩收据制复认、审计触及集计量、ROI 遥测字段、invariant 章成为唯一不变量定义处（吸收原 `.codex/AGENTS.md` 复述清单）。

## 1. 目标和边界

本协议要保证未来 AI 在开始研究前知道四件事：用户要研究什么、过去三个 AI 实际说过/做过什么、哪些产物能由文件/Git/运行证据支持、哪些结论仍是历史或未知。它不保证宿主一定自动加载文件，不认证模型理解，不把认知闭包变成数学证明，也不授予创建其他 AI、网络访问、发布、push 或修改外部 repo 的权限。

当前 top-level repo 的 source-of-truth 分层如下：

| 层 | 当前 owner | 可信含义 |
|---|---|---|
| 用户方向/裁定 | `rulings.md`、`核心认知.md` | rulings 拥有治理裁定；current core 拥有三份历史 primary 与以后 hash-pinned 一手输入中的用户直接悖论/元数学原文；不是数学真理 |
| 方向组合/统筹 | `方向追踪.md` | 跨 LocalGPT/WebGPT 的候选、优先级、依赖和下一动作；不是机器记录真值 |
| 成果全景/决策支持 | `全景视野.md` | 跨来源的结果、正反例、失败、未知和证据边界；不是数学主张矩阵 |
| 当前需求/状态 | `feature-list.md`、`MEMORY.md`、`STATE.json` | 可修订当前真值 |
| 历史认知 | `理解章节/`、`sources/` | 需要按 provenance 和证据等级使用 |
| 实际代码/产物 | `HoTT/`、`artifacts/`、`.codex/.../sessions/` | 文件存在/执行/验证分别记载 |
| 对话/事件证据 | `audit/*-ledger.jsonl`、`private-audit/` | 可见内容与工具事件；不含隐藏推理认证 |
| 版本历史 | 顶层 Git、嵌套 Git 快照、manifest | 历史理由/状态，不能取代当前要求 |

## 2. 每次开始的硬步骤（v3：第 0 步定档，步骤深度按档）

0. **档位判定（新增）**：按根 AGENTS 任务路由表判 T0–T3，会话首条声明档位并记入 SESSION.md（`tier` 字段）；越档即停。档内义务以 LOAD_SET `tiers` 扩展键为准。
1. 确认当前 root 是本目录，读取顶层 `AGENTS.md`、`README.md`、`MEMORY.md`、`feature-list.md`、`rulings.md`（T0 可只读 AGENTS + MEMORY/001 + 任务文件）。
2. 完整读取本地治理 SOP、角色表、此协议、`LOAD_SET.json`；**STATE 按档消费**——T0/T1 只读 hot 字段（`current_core/active/latest_session/unresolved/revision`，见根 AGENTS 路由表内命令）；T2/T3 读全文。纯治理无需自动加载业务 SOP；研究档才全文加载它。
3. 无条件按 `always_full_documents` 把四件套逐文件读到真实 EOF（**T0 豁免、T1 视任务涉及面、T2/T3 的首次进入或全文重载触发无条件**）；manifest、摘要、关键词命中、KC 子集和旧 Session 收据不能替代，governance/research 档也不能删减或重排。命中 `governance-shard-index:v2` 时，"逐文件读到真实 EOF" 等于**索引 + 按 table 顺序的全部分片**；缺任一片、未列片、标题或 `last_shard`/`append_target` 不符即未完成全文加载，降至 `BLOCKED_FULL_SET_COGNITION` 或重启加载。
4. governance profile 加载四件套、启动核和最新短 Session；research profile 再加载业务 SOP、三问、FRONTIER/LESSONS/RESUME 的 hot 部分（历史全文在各自 `*-log/`，query_first）。STATE 全文让所有 record 可见，但 loader 只按 `lifecycle_status` 决定任务资格，不因 `evidence_status=REVIEW_REQUIRED` 自动展开历史 Session。
5. 需要某一 candidate/result/issue/历史记录的底层证据时，先 `query --record <ID>` 查看身份和边界，再用 `plan --profile research --task <ID>` 显式递归展开 `depends_on`、`full_sources`、`resolution.evidence` 和 `source_hashes`（T0/T1 默认不做任务水合）。`depends_on` 只表示会传播 stale 的验证依赖；`research_parent`/`related_records` 只做谱系与叙事导航，不递归水合。显式水合后的正文必须全文读，不能用 query 输出替代；同时必须检查 plan 的 `hydration_diagnostics`。
6. 在进入实际研究/审计动作前完成三方交叉检查（T1 查 latest+active 一致性；T2/T3 全三方）：当前方向是否服务 core；每个方向是否有结果或明确 `NO_RESULT_YET`；每个结果是否有方向或有理由的 `UNMAPPED`；STATE/MEMORY/投影的 revision/hash 是否一致。不能以补写“最新版”覆盖冲突。
7. 记录 load snapshot：profile/tier、每个文件的 layer/selection reason、SHA-256、bytes、lines、实际范围、Git HEAD 和 dirty。加载变化或截断时重启；四件套无法全文保有则 `BLOCKED_FULL_SET_COGNITION`，优先移出四件套之外的载荷而非裁剪 core。
8. 形成本轮 closure statement：目标、范围、授权、档位与 hydration、当前完整 KC 范围、理论配置、证据缺口、四件套交叉结果、风险最高的误判和最小可验动作。

**压缩/跨会话重付（v3 收据制，替代全额重付）**：压缩后重付 = 档内启动核 + **持有收据复认**（逐文档核对 sha256 未变 + 逐 KC 一行复认 + 抽查 N 段原文，复认记录入 SESSION.md）；全文重付仅在三触发器：`core_sha256` 变化 / 档位升级 / 用户指令。本条为对 rulings §9/§11 的合同级修订，授权见 rulings §25。

工具报告 `FULL_EMITTED_BYTES_MATCH` 只表示读出字节与文件 hash 匹配，字段 `model_context` 必须保持 `NOT_CERTIFIED_BY_TOOL`。模型不能保留全文时必须公开降级，不能把“读过摘要”写成全文闭包。

## 3. 执行不变量（v3 的唯一正文）

本章吸收旧 `.codex/AGENTS.md` 的复述式不变量。根 `AGENTS.md` 负责宪法和分档路由，
`LOAD_SET.json` 负责机读层归属，本章负责它们在会话中如何共同生效；其它文档只可指向本章，
不得另写一份会独立漂移的当前规则。

1. **授权、根与来源边界**：当前顶层 Git root 是唯一写入根；`AI对话录/` 与 `workspace/` 是历史嵌套 repo。`sources/`、`核心认知.md` 和 `private-audit/` 的边界按根 `AGENTS.md` 执行；本协议不授予网络、外部 mutation、push、发布或 Sub Agent 权限。
2. **动态身份与任务资格**：core generation、KC 分母、curation、最新会话和当前 revision 只能从 `STATE.current_core`、`STATE.latest_session` 与 STATE 记录取得。`lifecycle_status` 决定任务资格，`evidence_status` 只表达证据状态；历史、关闭、替代和待审记录不因被读取而自动复活。
3. **四件套与档位**：全文固定顺序为 `核心认知.md` → `方向追踪.md` → `全景视野.md` → `扩展认知.md`；分片文档的全文是索引加 table 顺序全部分片。T2/T3 无条件完成四件套；T0 豁免，T1 仅在任务涉及面需要时加载。缺文件、截断、读取期间变化、hash 不一致或分片结构错误时停止为 `BLOCKED_FULL_SET_COGNITION`，不用摘要补洞。
4. **压缩重付**：压缩/跨会话默认执行档内启动核与收据复认（逐文档 hash、逐 KC 立场、原文抽查）；只有 `core_sha256_changed`、档位升级或用户明确要求时重做全文加载。收据制只证明持有/复认范围，不证明模型理解。
5. **关系和水合**：`depends_on` 只表达会传播 stale 的验证依赖；谱系、动机和叙事使用 `research_parent`/`related_records`，不得借此递归水合。需要底层证据时先 `query --record`，再显式 task plan；query-first 原件只有在本任务要求其全文时才提升。
6. **写入与证明边界**：math conclusion 的 source/kernel run/index 仍由根 `MATH_PROOF_BEFORE_DELIVERY_V1` 独立控制。checkpoint 只保存已授权的状态事务：默认 dry-run，`--apply` 要求当前授权、完整 session bundle、原子 before/after 与唯一 `result.json.status=CHECKPOINT_COMMITTED`；checkpoint 不能代替数学证明。
7. **审计与可证边界**：每个实质单元以分片审计集保留 KC 覆盖、关系、证据定位、反证条件、四件套交叉判断和下一选择。机械检查能验证字节、结构、hash 与覆盖，不能认证模型理解、数学真理或未来宿主行为。

## 4. 核心认知账本的使用

当前人工 owner、generation、curation、manifest 与 transition 全部从 `STATE.current_core` 动态取得。`scripts/audit/build_core_cognition.py` 默认 check、显式 `--write` 生成 `核心认知.md`、manifest 和 transition。当前每个 `KC-xxxxxx` 都是 `USER_OWNED_DIRECT` 精确原文，完整 hash/locator/themes 在 manifest，core 只留紧凑来源行。

工作中引用 KC 时必须保留当前精确 ID。转发 AI、附件、supplemental、一般治理对话和纯文件操作指令只能从 source/history 引用并标明身份，不得进入 core 或冒充用户已采纳。重复中的语义演化保留；无新增认识的跨平台复读可在 disposition 中显式去重。旧 generation-2/913 KC 由 `governance-v2.1.0` 与 913/913 transition 保存；generation-3/27 KC 由 `governance-v3.0.0` 与 generation-4 transition 全量保留。

## 4A. 四件套交叉审视与更新归属

`核心认知.md`、`方向追踪.md`、`全景视野.md` 是三个不同职责的当前输入，不是三份相互同步的摘要：

| 新事实 | 应更新 | 不应更新 |
|---|---|---|
| 用户提出新的研究意识、约束、方向或明确修正 | 先保存用户原文输入，再更新 core generation；按需求同步 `rulings.md` | 不把 AI 结果写成用户原文 |
| 新候选、优先级、依赖、状态或下一判别动作 | `方向追踪.md` 与 STATE 对应记录 | 不改写 core |
| 新推导、代码、测试、运行、失败、未知或证据范围 | `全景视野.md`、原 result/artifact/ledger/Git owner | 不因结果漂亮而改写 core |
| 结果稳定成为当前数学/技术知识 | 原 `HoTT/` 或稳定 topic owner | 不让全景成为第二份证明正文 |
| core 与方向冲突 | 方向标 `MISALIGNED`/`REVIEW_REQUIRED`，回到原文和证据 | 不修改 core 求表面一致 |
| 长文（AI 阐释层）需要修订 | 原位修改长文的分片；若涉及用户原文，先核对与 core 逐字一致 | 不改 core、不把 AI 展开写成用户原文或数学结论 |
| 方向与结果冲突 | 保留冲突，降低状态并核直接证据 | 不追加“最新版”覆盖块 |

四件套的当前 projection 只应保留稳定 ID、范围、关系和证据入口（其中核心问题意识长文是 AI 阐释层，不是用户原文权威）；原始响应、工具事件、代码、Git 和
运行产物仍由 `audit/`、`sources/`、`HoTT/`、`artifacts/` 和 Git 拥有。当前 `方向追踪.md` 和 `全景视野.md`
已经有 22,226 行 source register 的可发现性收据，但仍必须显式显示 `PENDING_DIRECT_SENTENCE_ADJUDICATION`、
数学复核和模型理解未认证；“全量登记”不能替代语义/数学结论。

## 4B. 分片逻辑文档（shard index）的读取与写入

合同 owner 是 `docs/quality/长治理文档分片与索引合同.md`；共享权威是 3.16.0 候选规范。要点：

1. **读取**：先读 canonical 索引的完整 table、`last_shard`、`append_target`，再按任务读 owner shard；顺序追加型还要读 `append_target`。索引只路由，不是摘要；不得把索引、首片或末片冒充逻辑文档全文。
2. **写入**：`topical` 文档原位修改 owner shard；`sequential` 文档追加到 `append_target`；新建 shard 必须与索引行、`last_shard`、`append_target` 在同一 commit 或同一个 checkpoint 事务中更新。
3. **加载器强制**：`.codex/tools/cognition_runtime.py` 3.6.1 在 `plan` 中把索引展开为索引 + 按 table 顺序的全部分片；某个分片若先由 active record 或直接 source 进入选择集，识别到 canonical index 后也必须重排回索引后的 table 顺序，同时保留原选择来源。逐片给出 hash/bytes/lines 与 `logical_id`/`logical_role`/`full_load`；`check` 必须覆盖每一片（否则 `COVERAGE_INCOMPLETE`）；结构错误一律 fail closed。`MUTABLE` 逻辑文档的分片同时进入 `HEAD.json.tracked`。
4. **300 行是软目标**，不是上限、Gate 或清理配额；超行只产生 `NOTICE`。判定分片看追加方式、导航成本与自然语义边界，不看行数。
5. **机械校验**：`python3 -B scripts/audit/verify_governance_shards.py`（pin 的 3.16.0 候选副本 + sha256 漂移检测）。机械 PASS 不证明边界合理或内容完整；迁移必须另做标题/内容对账与 consumer 扫描。
6. **表格式投影的行分片**（`方向追踪.md`、`全景视野.md`）：大表按家族拆成行分片，每片自带表头两行（唯一允许的重复内容，必须逐行对账）；身份与状态字段（marker 块、`source_state_revision`、`projection_generation`、`semantic_status`）留在索引；`verify_three_way_cognition.py` 按逻辑文本解析 `DIR-*`/`OUT-*` 行并拒绝 0/0 空壳 PASS；编辑投影必须用 `scripts/audit/projection_edit.py` 的模式，把索引与全部分片放进同一 payload。

## 5. 每次结束的逐编号回评（v3：触及集三段式计量 + ROI 遥测）

每个实质工作单元必须在 `.codex/research/hott/sessions/<SESSION_ID>/CORE_COGNITION_AUDIT.md` 保存分片审计集，覆盖 manifest 中全部 KC，分三段：

1. **触及集/张力延续集/裁决延续集**：逐条五元组 `kc_id | relation_to_this_work | assessment | evidence_locators | unresolved_note`（relation 词表与反证条件要求见治理 SOP 的审计格式章节）；
2. **其余 KC**：一行一条 `NOT_TOUCHED` + 下次触及条件（免五元组展开，仍是逐条可审计立场）；
3. **扩展认知**：按片触及计量（被本单元实际消费/检验的片逐段回评，其余片一行登记）。

当本轮是纯治理/审计而未触及数学方向时，大量 `NOT_TOUCHED` 是诚实结果，不是失败。SESSION.md 必填元数据（v3）：`host`（codex-cli/zcode-desktop/…）、`model`、`tier`（T0–T3）、`load_receipt`（档内文件 sha256 清单或 plan snapshot）、**`element_usage` ROI 遥测表**（框架元件 × 实际用到/未用但会拦住什么/未用且无影响，≤30 行）。逐编号回评不能被脚本自动生成的相似度或关键词匹配冒充。

**当前 writer 兼容边界**：runtime 3.6.1 的 checkpoint writer 仅授权新 session 目录第一层文件，
会拒绝在同一新事务写入嵌套 `CORE_COGNITION_AUDIT/` 分片。分片审计集仍是 current 设计合同；
在该 writer 获得经授权的路径/事务升级前，checkpoint 可使用完整单文件 46-KC legacy audit 作为
兼容 bundle，并必须登记 `G-V5-SESSION-AUDIT-SHARD-WRITE-GAP-001`。不得把这一兼容路径写成
分片已原子化，亦不得绕过 runtime 手工伪造 transaction/result。

## 6. 历史 AI 审计合同

- LocalGPT 的父线程、HoTT-2 main、visible assistant、canonical trajectory tool event、Git、`/Volumes/D/ALL-Markdown` 快照和 dirty 状态要分开记录。canonical `session_trajectory.py` 是轨迹解析入口；不解析隐藏推理、不把响应数量等同于工作正确性。
- WebGPT 的 56 Prompt、55 Response、111 UI sections 要逐项登记，并连接其 workspace snapshot 的 `R###`、SESSION、artifact、代码和 Git 状态。只存在于导出回答中的说法标 `AI_VISIBLE_UNVERIFIED`，文件/Git/运行另行定级。
- Gemini 的 22 user、24 ordinary text response、21 thought、17 executableCode、17 codeExecutionResult、2 inlineFile 和 1 Drive document reference 必须有计数与 locator。inlineFile 是真实代码 payload，不得称为 empty；Drive 正文缺失标 `ATTACHMENT_BODY_UNAVAILABLE`。thought 内容按隐私/可见性边界登记，不当作公开答案或隐藏推理认证。
- `work-product-ledger` 记录所有重要文档、代码、artifact、checkpoint 和 source snapshot 的状态；`claim-evidence-ledger` 把理解章节/当前文档的主张连回具体句子、文件、事件和 Git。文件存在只能是 `DOCUMENTED`，运行结果和验证范围单独填写。

## 7. 写入与 checkpoint

<!-- math-proof-delivery-gate:v1 -->

任何准备交付为已成立事实的数学结论，在写入稳定 owner、全景或最终答复前，都必须执行根 AGENTS 的 `MATH_PROOF_BEFORE_DELIVERY_V1`。精确形式命题和证明源码由 `HoTT/formal/` 持有；实际 proof assistant/kernel 运行由 `HoTT/verification/runs/<run-id>/` 持有，至少保存 `RUN.json`、`stdout.txt`、`stderr.txt`、`environment.txt`、`source-manifest.json`；唯一快速索引由 `HoTT/CLAIM_EVIDENCE_MATRIX.md` 持有。

checkpoint 只能保存状态，不能替代数学证明。代码存在、Python/Node 测试、有限样本、外部论文、历史 aggregate receipt、AI 自述和普通 Lean `Eq` 均不能自动升级成 HoTT 特定机器证明。缺任一 proof/source/run/index 或语义忠实性条件时，状态必须是 `QUESTION/CONJECTURE/HEURISTIC/PAPER_ONLY/COUNTEREXAMPLE_CANDIDATE/SOURCE_REPORTED_NOT_REPLAYED`，不得写“已证明/数学结论”。`/tmp` 可用于可删除缓存，不能承载唯一证明或收据。

当前可变状态包括根 `MEMORY.md`、投影与长文 `方向追踪.md`/`全景视野.md`/核心问题意识长文、`.codex/research/hott/FRONTIER.md`、`LESSONS.md`、`RESUME.md`、`STATE.json`，以及对应 session/candidate 路径。STATE v2 必须分别记录 `lifecycle_status` 与 `evidence_status`；历史 Session 的待复核主张由独立 issue/result 持有。core 语义决策属于 HUMAN_EDITED curation，core/manifest/transition 属 MACHINE_MANAGED；修改须走 manager 并建立新 generation。

`.codex/tools/cognition_runtime.py plan/read/check` 使用 source hash、乐观 snapshot、路径白名单、事务 journal、before/after backup 和锁。`checkpoint` 默认 dry-run；只有当前用户明确授权的写操作再使用 `--apply`。`STATE.revision`、`HEAD.json`、latest session、旧 record identity 和 resolution evidence 必须一致；新增或改变非空 `depends_on` 还必须声明 `dependency_semantics=verification_staleness`。每个 applied checkpoint 在同一事务中必须包含 `SESSION.md`、`RUNS.json` 与当前 core generation 全量、顺序、逐行有 assessment/evidence 的 `CORE_COGNITION_AUDIT.md`。运行器生成的 `transaction.json`、before/after 副本和 `result.json` 是 checkpoint 应用证据；`POST-CHECKPOINT.json` 只能从真实 result 派生，不能自写 `checkpoint_applied=true` 取得证明资格。遇 stale base、活动 writer、未完成 transaction、第三方写入、缺 Session evidence 或冲突，fail closed；恢复必须确认旧 owner 已停止，选择 finish/rollback 并保存 receipt。历史缺收据保留为 `CHECKPOINT_RECEIPT_MISSING`，禁止追溯伪造。

每个 session 目录至少保存 `SESSION.md`、`CORE_COGNITION_AUDIT.md`、`RUNS.json` 和 evidence；session 历史不可覆盖。提交后回读新 HEAD、状态、session、生成物 hash 和验证输出，只有如此才可称 `CHECKPOINT_COMMITTED`；Git commit 本身不等于数学验证。

## 8. 失败、未知与停止条件

以下情况必须保留为负结论或未知：来源被用户移走、原始附件正文缺失、AI 只宣称未落盘、旧 validator 依赖不存在路径、代码没有实际运行、运行只覆盖有限样本、普通逻辑界限被写成 HoTT 独有、理论定义被写成可执行算法、以及无法证明完整覆盖。任务可在证据足够时结束，不为了“看起来完整”引入数据库、常驻审计 AI、每函数 trace 或无必要的审批平台。

本 repo 的交接完成判据是：入口可发现、source boundaries 明确、原文可重放、账本可核验、关键冲突和未知显式存在、future AI 有启动/结束路径。数学结论另按 HoTT 规则、证明工具和现实解释分别验收。
