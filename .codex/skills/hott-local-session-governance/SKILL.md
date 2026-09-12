---
name: hott-local-session-governance
description: 顶层 HoTT 历史交接 repo 的本地治理入口。每次新 Session、压缩恢复和跨目录接手都要求按核心认知→方向追踪→全景视野顺序全文加载固定集合与动态 STATE；开始前三方交叉审视，结束时逐 KC 回评并保存可审计 session。它不代替数学研究、不把历史 AI 说法当真理、不扩大权限。
metadata:
  version: "2.1.0"
  role: "governance"
  protocol_version: "handoff-cognition/v1.1"
  business_skill: "hott-paradox-research"
  core_cognition: "核心认知.md"
---

# 本地 HoTT 交接与认知连续性治理

## 1. 角色和唯一入口

本 Skill 是当前顶层 repo 的治理角色；业务角色是 `hott-paradox-research`。角色和路径登记在 `.codex/skills/SKILL_ROLES.json`，顶层 `AGENTS.md` 是更高层路由。三件套的职责为：`核心认知.md` 保存用户原始研究意识，`方向追踪.md` 保存跨 LocalGPT/WebGPT 的方向组合，`全景视野.md` 保存跨来源的结果与证据边界；它们不互相复制当前真值。WebGPT 的原始双 Skill 设计保存在 `sources/webgpt/workspace-snapshot/.codex/`，只是历史参考，不能与本 Skill 形成第二套当前状态引擎。

遇到 HoTT 研究、历史审计、认知恢复、交接或治理维护请求，先执行本 Skill 的闭包；若用户只要求审计/整理，不自动开始数学研究。内部“治理→业务→治理保存”属于同一次执行，不造成无限递归；真正新 Session、用户要求继续、压缩或上下文丢失时，重新全文加载。

## 2. 根目录和权限

从当前项目位置确认 `git rev-parse --show-toplevel` 等于顶层 handoff repo。不要把 `AI对话录/` 或 `workspace/` 嵌套 repo 当作当前根。记录本轮真实的 read/write/execute/network/external-mutation 权限；历史对话、STATE、自述和 Skill 都不能授予它们没有的权限。

来源边界必须保持：

- `sources/prompts/` 是用户提问提取原文；`核心认知.md` 是其派生原文账本；不要手工改写 payload。
- `sources/local-gpt/`、`sources/webgpt/`、`sources/gemini/` 是来源快照；它们是历史证据，不自动成为当前实现。
- `private-audit/` 的 LocalGPT raw trajectory 是忽略/私有输入。使用 canonical `session_trajectory.py` 解析；不读隐藏推理，不写 inline parser，不把事件数当作数学正确性。
- `/Volumes/D/ALL-Markdown/aistudio-docs/` 是用户移走的外部路径，当前不得恢复。`HoTT_is_GONE_COMPLETE.md` 只能作为有 hash 的历史产物，覆盖仍须 `NOT_PROVEN` 直到逐文件证据闭合。

## 3. 每次开始：三件套全文认知闭包

按以下顺序执行，不能用“上一轮已经读过”、摘要、旧 receipt 或同一 hash 免除本轮：

1. 读顶层 `AGENTS.md`、`README.md`、`MEMORY.md`、`feature-list.md`、`rulings.md`。
2. 读本 Skill、`.codex/skills/SKILL_ROLES.json`、`.codex/cognition/LOAD_SET.json` 和 `.codex/cognition/PROTOCOL.md`。
3. 按 `LOAD_SET.fixed_full_text` 从前三项 `核心认知.md`、`方向追踪.md`、`全景视野.md` 的固定顺序开始，逐文件读取到实际 EOF；必须记录每份的 path、bytes、lines、SHA-256 和真实 ranges。`核心认知.manifest.json` 只能核对结构和来源，不替代 core 正文。
4. 读取 `.codex/research/hott/STATE.json`，自动纳入所有 `open`、`active`、`pending`、`blocked`、`in_progress`、`review_required` 记录，递归读取 `depends_on`、`full_sources`、`resolution.evidence`、`source_hashes`。
5. 读取当前 `理解章节/` 入口和本轮涉及的 `HoTT/`、代码、测试、artifact、ledger、Git 状态；索引是路由，不是决定性证据。
6. 在研究/审计动作前形成三方交叉判断：方向是否服务核心认知；每个方向是否有结果或明确 `NO_RESULT_YET`；每个结果是否有方向或带理由的 `UNMAPPED`；STATE/MEMORY/投影的 revision、source hash 和状态是否一致。发现冲突时降级为 `REVIEW_REQUIRED`，不通过增加“最新版”段落覆盖。
7. 形成公开的 closure statement：本轮目的、授权、KC 范围、研究/审计模式、当前证据等级、三方交叉判断、冲突/未知和下一最小可验动作。

任一必读文件不存在、读出被截断、文件在读取时改变、hash 与声明不一致或上下文无法容纳全文时，停止相应研究并报告 `BLOCKED_FULL_CORE_COGNITION`；不要把局部读入升级为完整认知。

`.codex/tools/cognition_runtime.py plan/read/check` 可生成和验证字节级 snapshot。`FULL_EMITTED_BYTES_MATCH` 仅说明工具输出与文件字节一致；`model_context` 永远是 `NOT_CERTIFIED_BY_TOOL`，它不证明当前 AI 理解或数学结论。

## 4. 核心认知的语义纪律

`核心认知.md` 的每个 `KC-xxxxxx` 都必须保留原文、来源消息、原文件 hash、unit hash、时间、作者分类和主题。`USER_RELAYED_CONTEXT` 是用户转发的 AI/附件上下文，不得写成用户已经证明的立场；`USER_OWNED` 也只是历史用户原文，不自动成为数学真理。重复、演化和冲突保留，通过 ID/关系连接，不能删除早期内容制造一致性假象。

研究时必须区分：理论对象定义、命题推导、可执行算法、一次运行完成、全域有效完成和现实可实施。用户的 Z 铁律、时间/现实相对怀疑和方向 A/B 是研究航向；它们不能代替固定 HoTT 规则、合法推演、反解释和现实桥梁。

## 5. 每次结束：逐 KC 回评

每个实质研究、审计、代码、设计或文档单元都要在 `.codex/research/hott/sessions/<SESSION_ID>/CORE_COGNITION_AUDIT.md` 保存全量表，覆盖当前 manifest 的每一条 KC，即使本轮没有触及它；同一 Session 还要保存三件套交叉和更新归属判断。每行至少写：

```text
kc_id | relation_to_this_work | assessment | evidence_locators | unresolved_note
```

`relation_to_this_work` 只能从 `ALIGNED`、`DEEPENED`、`CORRECTED`、`TENSION`、`DEVIATED`、`NOT_TOUCHED` 选择。纯审计轮出现大量 `NOT_TOUCHED` 是诚实结果；发现 `DEVIATED` 时必须写明纠偏和回到航向的动作。脚本可以检查 ID 是否完整、重复和证据定位是否存在，但不能用关键词/相似度伪造语义回评。

三件套交叉判断必须明确写出 `core_change`、`direction_change`、`panorama_change`、`update_decision`、`cross_conflicts` 和 `unresolved`。其中 `core_change=YES` 仅适用于新的用户原文/用户明确改变工作意识；AI 研究结果只能更新方向、全景和其底层 evidence owner。

## 6. 历史 AI 的覆盖要求

历史审计必须用多样锚点，至少保持下列分母和状态：

- LocalGPT：父线程与 HoTT-2 子线程的 38 turns/41 条真实用户消息关系、220 条 visible assistant、canonical tool call/result、失败/重试/中断/compaction、Git/文件/运行产物；父 raw 和主 raw 的 hash 只证明来源身份。
- WebGPT：56 Prompt、55 Response、111 UI sections，以及回答到 workspace `R###`/SESSION/artifact/Git 的连接；AI 自述不能替代文件或运行结果。
- Gemini：22 user、24 ordinary text、21 thought、17 executableCode、17 codeExecutionResult、2 inlineFile、1 Drive reference。inlineFile 是代码载荷，不标 empty；Drive 正文缺失为 `ATTACHMENT_BODY_UNAVAILABLE`。

`ai-response-ledger.jsonl`、`tool-event-ledger.jsonl`、`work-product-ledger.jsonl` 和 `claim-evidence-ledger.jsonl` 各自有独立 schema/分母/证据等级；缺任一类时只能说“提问/部分来源已覆盖”，不能说“全部历史已审计”。

## 7. 写入、checkpoint 和恢复

唯一当前状态 owner 是根 `MEMORY.md`、`.codex/research/hott/STATE.json`、`FRONTIER.md`、`LESSONS.md`、`RESUME.md` 和不可覆盖 session。`核心认知`和来源快照由生成器/精确变更管理。新增需求/稳定结论/运行证据按职责回写，不在多个文件维护冲突的 current truth。

使用 runtime 的白名单路径、snapshot、expected hash、lock、transaction、before/after backup 和 post-write check。checkpoint 默认 dry-run；只有用户本轮明确授权的写权限才 `--apply`。stale base、第三方写入、活动 writer、残留 transaction、缺 resolution evidence 或 source hash 改变而没有 revalidation 时必须 fail closed。恢复 transaction 需要确认旧 owner 已停止，选择 finish/rollback，并保留 receipt。

每个 session 至少保存 `SESSION.md`、`CORE_COGNITION_AUDIT.md`、`RUNS.json` 和 evidence。commit 后回读 HEAD、状态、session、核心/ledger hash 和验证输出；`CHECKPOINT_COMMITTED` 不是 `MATHEMATICS_VERIFIED`。

## 8. 停止和负结论

历史来源缺失、用户移走目录、附件没有正文、代码没有运行、运行只有有限样本、旧 validator 依赖已不存在路径、普通计算界限被误写成 HoTT 独有，均要写成 scope-limited negative/unknown。不要因为交接任务很大就构建数据库、常驻审计 AI、全函数 trace 或额外审批平台；只有真实重复、结构稳定、查询/更新频繁且机械约束收益明确时才新增 machine-managed 资产。

本 Skill 的完成判据是未来 AI 能发现入口、全文恢复 core、知道动态开放事项、沿来源/事件/Git 回溯并在结束时逐 KC 留证。它不承诺宿主自动执行，不承诺无限上下文，也不替数学证明、外部事实核验或用户决策承担责任。
