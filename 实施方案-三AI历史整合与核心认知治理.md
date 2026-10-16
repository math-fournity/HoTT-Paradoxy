# HoTT 三 AI 历史整合与核心认知治理实施方案

> 方案身份：EXECUTING_PLAN
>
> 建立时间：2026-09-12
>
> 目标 repo：/Volumes/D/HoTT_AI_HANDOFF_20260911
>
> 本文件是本次实施的执行依据，不是数学结论，也不是 AI 自述的完成证明。方案中的已知、目标、推断和待验证必须分开。

## 1. 目标与成功标准

本工程把三类历史工作和既有理解章节整合成一个以后唯一使用的本地研究 repo：

1. LocalGPT：/Volumes/D/ALL-Markdown 中第一波 HoTT 研究、来源整理、形式化尝试、治理和交接成果，并以 ~/.codex/sessions 中的 Codex trajectory 作为行为证据来源。
2. WebGPT：ChatGPT-HoTT - Main-20260911-1222.md 的网页工作记录，以及 workspace/ 中对应的研究、治理、代码、artifact、SESSION 和 Git 历史。
3. Gemini：Gemini 原始 JSON 中的用户问题、可见 AI 回答、代码、执行结果、inlineFile 和附件缺失状态。
4. 理解章节：对上述历史的已有 transform 层，保留历史版本并在证据闭合后形成当前理解入口。

最终成功标准：

- 顶层目录本身成为唯一明确的 Git repo 根。
- 现有 AI对话录/.git、workspace/.git 和 /Volumes/D/ALL-Markdown/.git 不被删除、重置或隐式覆盖。
- 三 AI 的来源身份、快照、HEAD、branch、tag、dirty 状态和历史关系可回溯。
- 三份用户提问提取文件原样保留并进入 source manifest。
- 完整 Codex 38 turn 的父线程/HoTT-2 主文件关系得到明确处理。
- 与 HoTT、悖论挖掘、抽象、时间、现实、计算合法性、研究方法和证据纪律相关的用户原文按时间顺序进入 核心认知.md。
- 每个核心认知单元都有连续编号、原文 hash、来源 locator 和作者身份。
- 用户原话、用户转发的 AI 内容、平台包装、附件引用和 AI 推导不混为一个身份。
- 每条输入用户消息都有纳入、辅助保留、重复、附件缺失或排除 disposition。
- LocalGPT、WebGPT、Gemini 的 visible response、工具调用、执行结果、代码、文档、artifact 和 Git 产出均有可回源证据。
- 重要 AI 主张可以回到句子/命题级原文、文件、代码、运行收据或 Git diff。
- 本地 .codex 治理要求每次开始前全文加载 核心认知.md。
- 每次工作结束按编号遍历所有核心认知，记录对齐、深化、纠偏、张力或偏航。
- 缺失源、截断、旧快照、未提交状态和工具失败必须阻塞或降级，不得伪称完成。
- 新 repo 可以在独立 clone 中恢复，最终 Git 状态干净。
- git commit、文件存在、测试通过、模型自述或摘要都不得自动升级为数学证明或 AI 理解证明。

## 2. 当前边界与决策

### 2.1 顶层 repo 决策

用户已明确要求直接把 /Volumes/D/HoTT_AI_HANDOFF_20260911 作为新 repo 根。本次不另建子目录，不把现有嵌套 repo 变成顶层 submodule。

顶层新 repo 的处理原则：

- 保留现有顶层 README、archive、history、manifests、onboarding 和 validation。
- 将 AI对话录 和 workspace 的文件内容复制为 sources/ 或理解章节/ 的整合快照。
- 不把 AI对话录/.git 和 workspace/.git 直接纳入顶层 Git 内容。
- 保存旧 repo 的 HEAD、refs、Git bundle、working-tree manifest 和 dirty diff。
- 新顶层 repo 成为未来工作的唯一活动工作根；旧 repo 是历史来源岛。

### 2.2 三个旧 repo 的当前身份

sources/SOURCE_MANIFEST.json 必须记录：

| 来源 | 当前状态 | 新 repo 处理 |
|---|---|---|
| AI对话录 | master，HEAD=c70b01c，27 commits；B1、读遍账本和 .DS_Store dirty | 保存当前树、HEAD、dirty diff 和历史 bundle；不自动改原 repo |
| workspace | main，HEAD=26fcecf，44 commits，当前 clean | 保存完整工作树快照、HEAD、tag 和历史 bundle |
| ALL-Markdown | codex/prime，HEAD=8470721，HEAD 历史 8 commits；staged rename、tracked 修改和大量 untracked | 保存 HEAD、index/worktree 状态、完整路径和 hash；不把 dirty 内容冒充已提交 |

### 2.3 aistudio-docs 边界

用户已经移走 /Volumes/D/ALL-Markdown/aistudio-docs/，本次不恢复、不重新读取、不列为当前必读源。

用户认为关键 HoTT 内容已经提取到 /Volumes/D/ALL-Markdown/HoTT_is_GONE_COMPLETE.md。该判断作为用户裁定和工作假设保存，但覆盖全部关键内容仍是待验证命题。

HoTT_is_GONE_COMPLETE.md 是历史 AI 产物，包含 HOTT is GONE、静态本体论、有限性/未知性/模糊性矛盾等强表述；后续工作对其中部分内容进行了收窄和分层。因此新 repo 中标记为：

~~~
source_role: HISTORICAL_AI_ARTIFACT
current_truth: NOT_AUTHORIZED_AS_MATHEMATICAL_PROOF
coverage_of_removed_aistudio_docs: NOT_PROVEN
~~~

旧 corpus manager 仍依赖被移走的 aistudio-docs，当前 validator 已出现缺源失败。新 repo 不继承旧 PASS；旧 validator 状态登记为 BLOCKED_SOURCE_REMOVED，新 repo 建立不依赖 removed source 的 core/source validator。

### 2.4 不变约束

- 原始对话录、用户原话、Gemini JSON、网页导出和 Codex trajectory 不改写。
- 核心认知.md 的原文区不被每次研究随意重写；用户新增认知以新 generation 加入。
- AI 解释、数学结论、代码实现、验证和运行观察分别记录。
- 不提交隐藏推理、secret、签名或不必要的完整私有系统上下文。
- 不删除失败、撤回、阻塞、截断、工具错误和未验证证据。
- 不自动 push、发布、发送外部消息或改动宿主配置。
- 不建立每句一个文件、每需求一个 checkpoint、常驻审计 AI 或第二套可变状态数据库。

## 3. 当前真值职责

| 内容 | 唯一 owner |
|---|---|
| 用户历史核心认知 occurrence | 核心认知.md + 核心认知.manifest.json |
| 用户明确裁定和当前边界 | rulings.md |
| 当前需求和验收 | feature-list.md |
| 当前研究队列和开放状态 | MEMORY.md + .codex/research/hott/STATE.json |
| 稳定 HoTT 研究结论 | HoTT/ 当前 owner 文档 |
| 历史 AI 工作史 | 理解章节/B0-B5 + audit ledgers |
| 工具、代码、artifact、运行状态 | sources、work、artifacts、verification 实物 |
| 单轮对核心认知的评估 | .codex/research/hott/sessions/<id>/CORE_COGNITION_AUDIT.md |
| 来源身份、版本和 hash | sources/SOURCE_MANIFEST.json |

README 只负责路由，MEMORY 只负责当前状态，rulings 只负责用户意图。任何一类当前事实不能在多个文件中各维护一份完整版本。

## 4. 目标目录布局

~~~
README.md
AGENTS.md
MEMORY.md
feature-list.md
rulings.md
核心认知.md
核心认知.manifest.json

理解章节/
sources/
  prompts/
  local-gpt/
  webgpt/
  gemini/
  understanding-transform/

audit/
  user-message-disposition.jsonl
  ai-response-ledger.jsonl
  tool-event-ledger.jsonl
  work-product-ledger.jsonl
  claim-evidence-ledger.jsonl
  source-coverage-report.md
  audit-summary.md

HoTT/
docs/
dev-docs/
scripts/
artifacts/
exchange/
archive/
history/
manifests/
onboarding/
validation/

.codex/
  AGENTS.md
  README.md
  skills/SKILL_ROLES.json
  skills/hott-local-session-governance/SKILL.md
  skills/hott-paradox-research/SKILL.md
  cognition/LOAD_SET.json
  cognition/PROTOCOL.md
  cognition/CORE_COGNITION.schema.json
  cognition/SOURCE_MANIFEST.schema.json
  cognition/HEAD.json
  research/hott/STATE.json
  research/hott/FRONTIER.md
  research/hott/LESSONS.md
  research/hott/RESUME.md
  research/hott/sessions/
  verification/
  tools/cognition_runtime.py
~~~

现有 nested repo 的 .git 不复制进顶层活动内容；旧历史使用 bundle、manifest 和整合前快照保留。

## 5. 核心认知.md 合同

### 5.1 输入文件

用户明确指定的三份输入原样保存：

~~~
Codex-HoTT-2-用户消息提取-20260911.md
ChatGPT-HoTT-Main-用户消息提取-20260911.md
Gemini-AI对话录-用户消息提取-20260911.md
~~~

当前这三份的已知计数是 Codex 主文件 10 条、WebGPT 56 条、Gemini 22 条。

为了满足完整 Codex 38 turn，还必须显式处理：

~~~
Codex-HoTT父线程-01a059c1-用户消息提取-20260911.md
Codex-并行会话-素数与归档-用户消息提取-20260911.md
~~~

父线程和主文件共有 41 条真实用户消息、38 个 turn。若只使用指定的 Codex 主文件，报告必须写成局部 Codex 输入，不能写成 38 turn 完整输入。

### 5.2 核心正文分层

核心认知.md 分为：

1. USER_OWNED_CORE：用户自己提出的 HoTT/悖论研究认知、判断、目标和研究航向。
2. USER_OWNED_GOVERNANCE：直接影响未来研究连续性的加载、交接、落盘和审计要求。
3. USER_RELAYED_CONTEXT：用户转发的 Gemini/GPT 内容，保存但不冒充用户立场。
4. ATTACHMENT_REFERENCE：附件引用或正文缺失的项目。
5. EXCLUDED_DISPOSITION：不进入核心正文但在完整 disposition 中登记理由的内容。

业务主题至少包括：

~~~
HOTT_OBJECT
HOTT_PARADOX
PARADOX_DISCOVERY
ABSTRACTION_AND_NEGATION
Z_LAW
TIME_AND_TEMPORALITY
BEING_AND_BECOMING
RUSSELL
ZENO
CIRCLE_PARADOX
BETTER_BEST
SHENCHENSH_MATRIX
IDENTITY_UNIVALENCE_TRANSPORT
TRUNCATION_QUOTIENT_REFLECTION
GUARDED_DIRECTED_VARIANTS
COMPUTATIONAL_LEGITIMACY
ASK
THEORY_SCHEMA
EVIDENCE_DISCIPLINE
RESEARCH_METHOD
SESSION_CONTINUITY
HANDOFF_GOVERNANCE
~~~

素数研究、纯平台连接消息和纯 UI 事务不进入核心正文，但必须在 disposition 中明确登记。

### 5.3 编号规则

核心 occurrence 使用连续 ID：

~~~
KC-000001
KC-000002
KC-000003
...
~~~

重复思想不删除；通过 repeats、refines、corrects、supersedes、anticipates 关联。

每个 KC 单元必须有：

~~~
source_message_id
platform
timestamp_original
timestamp_utc
source_file
source_locator
source_sha256
unit_sha256
author_class
themes
lifecycle
relations
~~~

排序键为：

~~~
timestamp_utc
→ source_platform_rank
→ source_message_ordinal
→ source_locator
→ unit_ordinal
~~~

保留原始时间文本和排序置信度；同一时间戳不得伪造因果顺序。

### 5.4 单元边界

一个核心认知单元是表达一个研究目标、判断、条件—结论组合、研究方法、证据要求、AI 纠偏、开放问题或交接要求的最小完整语义单位。

不采用机械的每个标点一句或整条消息一个单位：

- 公式和不可分的紧邻解释保持在一起；
- 一条消息中独立要求可拆分；
- 每个拆分单元保留原消息 locator；
- 原文区不润色，不把 AI 摘要写成用户原话；
- 只有 metadata 做主题、作者和关系标记。

## 6. 多样化审计锚点

### 6.1 用户消息处置

user-message-disposition.jsonl 必须覆盖：

- Codex parent/main 的 38 turn、41 条真实用户消息；
- WebGPT 56 条 Prompt；
- Gemini 22 条用户消息；
- Codex 并行/重复/附件消息；
- 每条消息是否进入核心；
- relay、attachment、duplicate、out-of-scope、missing 的原因。

### 6.2 AI response ledger

ai-response-ledger.jsonl 每条 visible AI response 一行，包含：

~~~
ai_id
response_id
platform
source_file
raw_locator
timestamp
content_sha256
visibility
full_text_available
material_claim_ids
artifact_ids
git_ids
error
truncation
disposition
~~~

必须将 LocalGPT 220 条 assistant message、WebGPT 55 条 Response 和 Gemini 24 条普通文本 response 分开登记。

### 6.3 Tool event ledger

tool-event-ledger.jsonl 记录 LocalGPT trajectory 中所有可见 tool call/result：

~~~
tool_event_id
session_id
turn_id
raw_locator
tool_name
visible_arguments
matching_result_id
result_status
path_mentions
side_effect_class
related_repo
related_commit
related_artifact
error_or_retry
truncation_status
~~~

只有 call 和 result 通过 ID 对齐，才可以说有可见结果；只有实际内容覆盖 source，才可以说 selected-read coverage。

### 6.4 Work product ledger

work-product-ledger.jsonl 记录代码、文档、artifact、SESSION、checkpoint 和 source snapshot：

~~~
artifact_id
path
source_ai
origin_response_ids
origin_tool_event_ids
repo
head_or_snapshot
file_sha256
status
~~~

status 使用 DOCUMENTED、IMPLEMENTED、EXECUTED、VERIFIED_WITH_SCOPE、RUNTIME_OBSERVED、HISTORICAL_ONLY、UNVERIFIED、MISSING、DIRTY_NOT_VERSION_CLOSED 等值。

### 6.5 Claim evidence ledger

claim-evidence-ledger.jsonl 将理解章节和当前文档中的重要句子/命题连接到证据：

~~~
claim_id
claim_text
claim_owner_document
claim_line
claim_type
source_locators
artifact_locators
git_locators
verification_run_ids
scope
conflicts
unknowns
verdict
~~~

代码存在不证明运行；测试通过只覆盖其断言、样本、环境和版本；AI 自述不替代 evidence。

## 7. 三 AI 审计方法

### 7.1 LocalGPT

使用 canonical session_trajectory.py：

~~~
catalog → tree → scan/tail/search → inspect → context → coverage
~~~

不写 inline parser，不从 encrypted/private reasoning 推断隐藏行动。

分别保留 parent 和 HoTT-2 main 的：

- session、branch、fork、parent identity；
- turn、user、assistant、tool、result、error、usage、compaction 计数；
- 220 条 visible assistant message；
- 1,143 次 tool call 和对应 result；
- 失败、重试、中断和截断；
- ALL-Markdown、workspace、AI对话录的路径、Git 和 artifact 联系。

阶段抽样只能是摘要，不能代替逐项 event ledger。

### 7.2 WebGPT

完整登记：

~~~
56 Prompt
55 Response
111 UI message sections
~~~

每个 Response 连接到：

~~~
W section
→ visible answer
→ workspace R/revision
→ SESSION/artifact/code
→ Git commit 或 dirty snapshot
→ 理解章节和 claim-evidence
~~~

保留连续 Prompt、重复 Gemini 问题和最后连续两条 Response。

### 7.3 Gemini

完整登记：

~~~
24 ordinary text responses
21 thought records，按隐私边界登记
17 executableCode
17 codeExecutionResult
2 inlineFile
1 Drive document reference without body
~~~

两个 inlineFile 不得分类为 empty；必须解码、hash、登记代码摘要和作用。Drive 文档正文缺失时标记 ATTACHMENT_BODY_UNAVAILABLE。

Gemini 的项目状态自述必须回到 ALL-Markdown/workspace 实物和 Git；玩具求值器、预期输出和沙箱文件不能升级为 HoTT 内核证明或项目文件写入。

## 8. 顶层 .codex 定制治理

### 8.1 两个 Skill

参考 WebGPT 的双 Skill 结构，但改为顶层 repo 相对路径：

~~~
.codex/skills/hott-local-session-governance/SKILL.md
.codex/skills/hott-paradox-research/SKILL.md
~~~

治理 Skill 负责 repo root、权限、核心认知全文加载、动态状态、session/checkpoint/recovery、逐 ID audit、stale base、缺件和截断。

业务 Skill 负责用户数学哲学内部重建、标准 HoTT 比较、候选构造、反解释、研究前沿和证据边界。

### 8.2 LOAD_SET

固定必读至少包括：

~~~
核心认知.md
核心认知.manifest.json
AGENTS.md
README.md
MEMORY.md
feature-list.md
rulings.md
理解章节/README.md
理解章节/B5-成果总账.md
理解章节/A0-总目标.md
理解章节/A11-开放问题与悬空接头.md
.codex/skills/SKILL_ROLES.json
.codex/cognition/PROTOCOL.md
.codex/research/hott/STATE.json
.codex/research/hott/FRONTIER.md
.codex/research/hott/LESSONS.md
.codex/research/hott/RESUME.md
~~~

动态集合由 STATE 中 open、active、pending、blocked、in_progress、review_required 记录及其完整依赖展开。

### 8.3 每次开始

1. 确认当前 repo root。
2. 读取根 AGENTS 和本地治理 Skill。
3. 读取 LOAD_SET 和 STATE。
4. 从核心认知.md 第 1 行连续读取到实际 EOF。
5. 记录 generation、SHA、总行数、总字节数和实际 ranges。
6. 读取当前状态、前沿、开放记录和直接依赖。
7. 记录本轮目标、权限、理论配置和高代价误判。
8. 任一步失败都进入 BLOCKED_FULL_CORE_COGNITION，不开始研究。

工具可以证明输出范围，不能证明模型真正理解。容量不足必须明确降级。

### 8.4 每次结束

每个实质研究、审计、代码、设计或文档工作单元保存：

~~~
.codex/research/hott/sessions/<SESSION_ID>/
├── SESSION.md
├── CORE_COGNITION_AUDIT.md
├── RUNS.json
└── evidence/
~~~

CORE_COGNITION_AUDIT.md 必须按 KC-000001 到最后一个 ID 逐项出现，每项至少有：

~~~
relation
alignment
deepening
correction
deviation
assessment
evidence_ids
~~~

单元状态使用 ALIGNED、DEEPENED、CORRECTED、TENSION_IDENTIFIED、DEVIATED_RECOVERED、NOT_RELEVANT、BLOCKED。

即使不相关，也要写“已检查，未改变”。缺 ID、重复 ID、空 assessment、无 evidence 引用的 audit 必须失败。

Session 级还要记录 ON_COURSE、ON_COURSE_WITH_REFINEMENT、ON_COURSE_BUT_BLOCKED、OFF_COURSE_RECOVERED 或 OFF_COURSE_UNRESOLVED，并分别评估用户认知忠实性、研究深化、数学证据、准备工作和研究漂移。

核心认知原文不在每次工作中重写；用户新增认识创建新的 generation。

## 9. 实施 Waves

### Wave 0：基线和边界

- 运行顶层已有 README 的 baseline；
- 记录三个旧 repo 的 root、HEAD、branch、tag、status、common-dir；
- 记录 nested repo 和顶层文件；
- 记录 aistudio-docs 已移走；
- 记录 HoTT_is_GONE_COMPLETE.md 的 hash、行数和历史身份；
- 记录当前 missing source、旧 validator failure 和 dirty ownership。

验收：有 source identity draft，旧材料可回退，未改动旧 repo。

### Wave 1：顶层 Git 与方案基线

- 写入本方案；
- 初始化顶层 Git；
- 提交顶层现有 README 的原始基线和本方案；
- 创建顶层 .gitignore；
- 明确 nested .git、私有 trajectory、临时输出和系统缓存边界；
- 创建 root governance skeleton，不覆盖现有 README。

验收：顶层有第一份可恢复 commit；原 README 可以从该 commit 恢复。

### Wave 2：来源快照

- 复制三份指定用户提问文件；
- 补充 Codex parent/main visible trajectory 证据；
- 复制 ChatGPT export 和 workspace 内容；
- 复制 Gemini JSON；
- 复制 AI对话录/理解章节当前工作树；
- 保存所有 repo HEAD、dirty diff、tracked/untracked manifest 和 file hash；
- 保存 HoTT_is_GONE_COMPLETE.md 及相关 GONE 历史文件；
- 对 removed aistudio-docs 只登记 source gap，不伪造恢复。

验收：所有源文件有 source ID，所有排除、重复、缺失有理由。

### Wave 3：核心认知 Walking Skeleton

- 以三份指定提问文件为主输入；
- 补齐 Codex parent 的业务相关用户消息；
- 生成消息和单元候选；
- 执行业务相关性裁定；
- 按时间确定性排序；
- 生成 KC ID、manifest 和 disposition；
- 进行 exact text/hash/locator round-trip。

验收：未来 AI 能从一份核心认知.md 看到完整、原文保真、按时间排序的业务核心。

### Wave 4：三 AI evidence ledger

- 用 canonical trajectory reader 建立 LocalGPT event ledger；
- 完整登记 visible response 和 tool call/result；
- 完整登记 WebGPT 55 Response；
- 完整登记 Gemini text、thought、code、result、inlineFile 和附件缺失；
- 建立 work-product、Git 和 claim-evidence ledger；
- 修正理解章节旧计数、旧读态和 Gemini inlineFile 错误；
- 旧理解章节保留历史身份，修正版成为 current owner。

验收：必要事件类全部可访问或明确 unavailable；重要主张有相称 evidence。

### Wave 5：本地 .codex 治理

- 创建根 AGENTS 和 .codex/AGENTS；
- 创建双 Skill、SKILL_ROLES、LOAD_SET 和 PROTOCOL；
- 适配 WebGPT 的单一 cognition runtime；
- 加入 core full-load receipt；
- 加入逐 ID core audit receipt；
- 加入缺件、截断、stale snapshot、中断、恢复和权限测试；
- 建立 STATE、FRONTIER、LESSONS、RESUME；
- 更新 README、Feature、MEMORY、rulings 和 docs 路由。

验收：顶层新 repo 可按本地治理启动和恢复；fresh Session 的真实理解仍是独立验收。

### Wave 6：验证和 Git 交接

- 运行 core extraction round-trip；
- 运行 source/hash/locator validator；
- 运行 response/tool/result/artifact coverage validator；
- 运行 preflight 和 all-ID post-audit validator；
- 旧 corpus validator 如实保留 BLOCKED_SOURCE_REMOVED；
- 运行当前不依赖 removed source 的 validator；
- 在独立 clone 中恢复；
- 回读 final HEAD、status、tree、tag 和 receipts。

## 10. Git 提交序列

推荐顶层提交：

~~~
I0  preserve top-level handoff baseline and this plan
I1  source identity, snapshots, manifests and historical provenance
I2  core cognition and user disposition
I3  three-AI response/tool/artifact/claim ledgers
I4  local .codex governance and runtime checks
I5  current routing, conflict cleanup and verification receipts
~~~

每次只 stage 精确路径，不混入 nested repo 的其他并行变更。

原 AI对话录 和 /Volumes/D/ALL-Markdown 是否另行 clean commit，要以各自 path manifest 和用户授权单独决定；新顶层 repo 的 clean commit 不自动证明旧 repo clean。

正式 tag 只有在最终验收通过后建立；如果 source gap、validator failure、core audit 未完成或 fresh Session 未执行，只建立 partial/candidate 版本或不打正式完成 tag。

## 11. 回滚与恢复

- 初始化前保留原文件；
- 编辑已有文件前运行 check_file_baseline.sh；
- 不删除 nested .git；
- 不恢复或改动 removed aistudio-docs；
- 每个 source/core/evidence generation 有 hash；
- 新 generation 不覆盖旧 generation；
- 生成器失败保留失败输出，不用空文件替代；
- checkpoint 先 dry-run 再 apply；
- recovery 需要确认旧 writer 已停止；
- 旧 repo dirty diff 只作为 provenance 保存；
- clean clone 从顶层 commit 恢复，不依赖 nested .git。

## 12. 最终验收矩阵

| 面 | 必须证据 | 通过状态 |
|---|---|---|
| 顶层 Git | clean status、HEAD、fsck、独立 clone | PASS |
| 来源身份 | manifest、hash、HEAD/tag/status、缺件列表 | PASS_WITH_SCOPE |
| 用户提问 | Codex 38/41、Web 56、Gemini 22 的逐条 disposition | PASS |
| 核心认知 | KC 连续、原文 hash、时间排序、source locator、无未解释候选 | PASS |
| LocalGPT | tree、visible response/tool/result ledger、parent/main/fork | PASS_WITH_SCOPE 或 unavailable |
| WebGPT | 55 Response 与 workspace artifact/Git 关联 | PASS_WITH_SCOPE |
| Gemini | 24 text、21 thought、17 code、17 result、2 inlineFile、附件缺失 | PASS_WITH_SCOPE |
| removed source | 用户排除、旧 validator failure、替代 source coverage 不冒充等价 | PASS_WITH_SCOPE |
| 本地治理 | root route、双 Skill、LOAD_SET、pre/post core audit、recovery tests | PASS_WITH_SCOPE |
| fresh Session | 实际全文加载、未知问题接手、旧错误回避、逐 ID 回顾 | NOT_RUN 直到真正执行 |
| 数学真值 | 独立 HoTT/Agda/Lean/专家审查 | 不由本工程自动升级 |

## 13. 不得使用的完成表述

在证据闭合前，不得写：

~~~
已经完整理解全部 AI 工作
所有历史内容均已覆盖
核心认知已经被 AI 完全理解
HoTT 的强结论已经被证明
HoTT is GONE 已经得到数学认证
旧 aistudio-docs 已经被等价完整替代
36/36 PASS 所以整个交接完成
~~~

准确表述应是：

~~~
在已声明 source boundary 内，提取和来源定位通过；
当前 core generation 的用户业务原文已按编号保全；
AI 工作史已按事件/回复/产物层完成有界证据登记；
removed source 造成的旧 validator 缺口仍然开放；
fresh Session 的模型理解验收与数学真值认证是独立事项。
~~~

## 14. 本次执行起点

方案写入后严格执行：

~~~
方案落盘
→ 顶层 Git 初始化
→ 原始顶层 README 基线 commit
→ source manifest
→ 核心认知 Walking Skeleton
→ 三 AI history ledger
→ .codex 本地治理
→ validators and recovery
→ final commits and clean-clone acceptance
~~~

本方案不授权 push、外部发布、删除旧 repo、恢复 aistudio-docs、提交 hidden trajectory 或伪造数学/理解认证。
