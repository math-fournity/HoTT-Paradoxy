# 顶层综合 repo 认知与交接协议

版本：`handoff-cognition/v1.1`。本协议是本 repo 的当前执行合同；它参考并重写适配了 WebGPT 快照中的双 Skill 治理，但不把快照中的旧 root、旧 host 状态或旧 PASS 当成当前事实。

## 1. 目标和边界

本协议要保证未来 AI 在开始研究前知道四件事：用户要研究什么、过去三个 AI 实际说过/做过什么、哪些产物能由文件/Git/运行证据支持、哪些结论仍是历史或未知。它不保证宿主一定自动加载文件，不认证模型理解，不把认知闭包变成数学证明，也不授予创建其他 AI、网络访问、发布、push 或修改外部 repo 的权限。

当前 top-level repo 的 source-of-truth 分层如下：

| 层 | 当前 owner | 可信含义 |
|---|---|---|
| 用户方向/裁定 | `rulings.md`、`核心认知.md` | 用户原文和当前裁定；不是数学真理 |
| 方向组合/统筹 | `方向追踪.md` | 跨 LocalGPT/WebGPT 的候选、优先级、依赖和下一动作；不是机器记录真值 |
| 成果全景/决策支持 | `全景视野.md` | 跨来源的结果、正反例、失败、未知和证据边界；不是数学主张矩阵 |
| 当前需求/状态 | `feature-list.md`、`MEMORY.md`、`STATE.json` | 可修订当前真值 |
| 历史认知 | `理解章节/`、`sources/` | 需要按 provenance 和证据等级使用 |
| 实际代码/产物 | `HoTT/`、`artifacts/`、`.codex/.../sessions/` | 文件存在/执行/验证分别记载 |
| 对话/事件证据 | `audit/*-ledger.jsonl`、`private-audit/` | 可见内容与工具事件；不含隐藏推理认证 |
| 版本历史 | 顶层 Git、嵌套 Git 快照、manifest | 历史理由/状态，不能取代当前要求 |

## 2. 每次开始的硬步骤

每个新 Session、上下文压缩恢复、跨 repo 接手、用户改变范围或 source hash 变化后，必须：

1. 确认当前 root 是本目录，读取顶层 `AGENTS.md`、`README.md`、`MEMORY.md`、`feature-list.md`、`rulings.md`。
2. 完整读取本地治理 Skill、业务 Skill、角色表、此协议、`LOAD_SET.json` 和 `STATE.json`。
3. 按 `LOAD_SET.fixed_full_text` 的顺序逐文件读到真实 EOF；前三文件必须严格是 `核心认知.md`、`方向追踪.md`、`全景视野.md`，第四文件才是三问。核心账本不能用 manifest、摘要、关键词命中或旧 Session 收据替代。
4. 读取 STATE 自动纳入所有 `open`、`active`、`pending`、`blocked`、`in_progress`、`review_required` 记录，递归展开 `depends_on`、`full_sources`、`resolution.evidence` 和 `source_hashes`。不能只读手工 active 列表而让开放记录隐身。
5. 在进入实际研究/审计动作前完成三方交叉检查：当前方向是否服务 core；每个方向是否有结果或明确 `NO_RESULT_YET`；每个结果是否有方向或有理由的 `UNMAPPED`；STATE/MEMORY/投影的 revision/hash 是否一致。不能以补写“最新版”覆盖冲突。
6. 记录 load snapshot：每个文件相对路径、SHA-256、bytes、lines、实际读入范围、总 bytes/lines、Git HEAD 和 dirty 状态。加载途中发生变化或截断，重新开始或降级为 `BLOCKED_FULL_CORE_COGNITION`。
7. 形成本轮 closure statement：目标、范围、授权（read/write/execute/network/external mutation）、涉及的 KC 范围、理论配置、证据缺口、三件套交叉结果、风险最高的误判和本轮最小可验动作。

工具报告 `FULL_EMITTED_BYTES_MATCH` 只表示读出字节与文件 hash 匹配，字段 `model_context` 必须保持 `NOT_CERTIFIED_BY_TOOL`。模型不能保留全文时必须公开降级，不能把“读过摘要”写成全文闭包。

## 3. 核心认知账本的使用

`核心认知.md` 的原文正文由 `scripts/audit/build_core_cognition.py` 生成，`核心认知.manifest.json` 是其机器清单。每个 `KC-xxxxxx` 具有原文 payload hash、source message、platform、timestamp、author class、themes、lifecycle 和关系。元数据是索引，不是对用户语义的自动裁决。

工作中引用 KC 时必须保留精确 ID；若引用历史用户转发的 AI 内容，注明 `USER_RELAYED_CONTEXT`，不冒充用户已采纳。重复、修订、矛盾和时序邻接都保留；不得因为后来的 AI 说法而删除早期用户原文。

## 3A. 三件套交叉审视与更新归属

`核心认知.md`、`方向追踪.md`、`全景视野.md` 是三个不同职责的当前输入，不是三份相互同步的摘要：

| 新事实 | 应更新 | 不应更新 |
|---|---|---|
| 用户提出新的研究意识、约束、方向或明确修正 | 先保存用户原文输入，再更新 core generation；按需求同步 `rulings.md` | 不把 AI 结果写成用户原文 |
| 新候选、优先级、依赖、状态或下一判别动作 | `方向追踪.md` 与 STATE 对应记录 | 不改写 core |
| 新推导、代码、测试、运行、失败、未知或证据范围 | `全景视野.md`、原 result/artifact/ledger/Git owner | 不因结果漂亮而改写 core |
| 结果稳定成为当前数学/技术知识 | 原 `HoTT/` 或稳定 topic owner | 不让全景成为第二份证明正文 |
| core 与方向冲突 | 方向标 `MISALIGNED`/`REVIEW_REQUIRED`，回到原文和证据 | 不修改 core 求表面一致 |
| 方向与结果冲突 | 保留冲突，降低状态并核直接证据 | 不追加“最新版”覆盖块 |

三件套的当前 projection 只应保留稳定 ID、范围、关系和证据入口；原始响应、工具事件、代码、Git 和
运行产物仍由 `audit/`、`sources/`、`HoTT/`、`artifacts/` 和 Git 拥有。当前 `方向追踪.md` 和 `全景视野.md`
已经有 22,226 行 source register 的可发现性收据，但仍必须显式显示 `PENDING_DIRECT_SENTENCE_ADJUDICATION`、
数学复核和模型理解未认证；“全量登记”不能替代语义/数学结论。

## 4. 每次结束的逐编号回评

每个实质工作单元必须在 `.codex/research/hott/sessions/<SESSION_ID>/CORE_COGNITION_AUDIT.md` 保存逐编号表，覆盖 manifest 中全部 KC，不能只覆盖本轮使用过的几个。每行至少包含：

```text
kc_id | relation_to_this_work | assessment | evidence_locators | unresolved_note
```

`relation_to_this_work` 使用 `ALIGNED`、`DEEPENED`、`CORRECTED`、`TENSION`、`DEVIATED`、`NOT_TOUCHED`；`assessment` 必须说明事实依据，不能只写“符合”。当本轮是纯治理/审计而未触及数学方向时，大量 `NOT_TOUCHED` 是诚实结果，不是失败；若发现偏离，必须在 session 记录、MEMORY 和必要的 ruling/design owner 中写明纠偏。

逐编号回评不能被脚本自动生成的相似度或关键词匹配冒充。脚本可以检查 ID 完整、hash、证据定位格式；语义评估由当前 AI 写公开、可审计的文本。

## 5. 历史 AI 审计合同

- LocalGPT 的父线程、HoTT-2 main、visible assistant、canonical trajectory tool event、Git、`/Volumes/D/ALL-Markdown` 快照和 dirty 状态要分开记录。canonical `session_trajectory.py` 是轨迹解析入口；不解析隐藏推理、不把响应数量等同于工作正确性。
- WebGPT 的 56 Prompt、55 Response、111 UI sections 要逐项登记，并连接其 workspace snapshot 的 `R###`、SESSION、artifact、代码和 Git 状态。只存在于导出回答中的说法标 `AI_VISIBLE_UNVERIFIED`，文件/Git/运行另行定级。
- Gemini 的 22 user、24 ordinary text response、21 thought、17 executableCode、17 codeExecutionResult、2 inlineFile 和 1 Drive document reference 必须有计数与 locator。inlineFile 是真实代码 payload，不得称为 empty；Drive 正文缺失标 `ATTACHMENT_BODY_UNAVAILABLE`。thought 内容按隐私/可见性边界登记，不当作公开答案或隐藏推理认证。
- `work-product-ledger` 记录所有重要文档、代码、artifact、checkpoint 和 source snapshot 的状态；`claim-evidence-ledger` 把理解章节/当前文档的主张连回具体句子、文件、事件和 Git。文件存在只能是 `DOCUMENTED`，运行结果和验证范围单独填写。

## 6. 写入与 checkpoint

当前可变状态包括根 `MEMORY.md`、三件套投影 `方向追踪.md`/`全景视野.md`、`.codex/research/hott/FRONTIER.md`、`LESSONS.md`、`RESUME.md`、`STATE.json`，以及对应 session/candidate 路径。核心原文、来源快照和历史 ledger 默认 machine-managed 或 append-only；修改它们须走生成器/精确审核并记录新 generation。三件套投影若由人工综合，应保留 `asset_class`、source revision、projection generation 和未完成语义范围。

`.codex/tools/cognition_runtime.py plan/read/check` 使用 source hash、乐观 snapshot、路径白名单、事务 journal、before/after backup 和锁。`checkpoint` 默认 dry-run；只有当前用户明确授权的写操作再使用 `--apply`。`STATE.revision`、`HEAD.json`、latest session、旧 record identity 和 resolution evidence 必须一致。遇 stale base、活动 writer、未完成 transaction、第三方写入或冲突，fail closed；恢复必须确认旧 owner 已停止，选择 finish/rollback 并保存 receipt。

每个 session 目录至少保存 `SESSION.md`、`CORE_COGNITION_AUDIT.md`、`RUNS.json` 和 evidence；session 历史不可覆盖。提交后回读新 HEAD、状态、session、生成物 hash 和验证输出，只有如此才可称 `CHECKPOINT_COMMITTED`；Git commit 本身不等于数学验证。

## 7. 失败、未知与停止条件

以下情况必须保留为负结论或未知：来源被用户移走、原始附件正文缺失、AI 只宣称未落盘、旧 validator 依赖不存在路径、代码没有实际运行、运行只覆盖有限样本、普通逻辑界限被写成 HoTT 独有、理论定义被写成可执行算法、以及无法证明完整覆盖。任务可在证据足够时结束，不为了“看起来完整”引入数据库、常驻审计 AI、每函数 trace 或无必要的审批平台。

本 repo 的交接完成判据是：入口可发现、source boundaries 明确、原文可重放、账本可核验、关键冲突和未知显式存在、future AI 有启动/结束路径。数学结论另按 HoTT 规则、证明工具和现实解释分别验收。
