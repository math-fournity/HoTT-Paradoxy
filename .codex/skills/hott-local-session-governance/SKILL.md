---
name: hott-local-session-governance
description: 顶层 HoTT 交接 repo 的治理差异层。用于新 Session、压缩恢复、交接、治理维护与审计：补充 BLOCKED_FULL_SET_COGNITION 停止协议、分片 KC 审计集格式及三类历史 AI 覆盖分母。完整启动、档位、写入与 checkpoint 规则由根 AGENTS、LOAD_SET 和 PROTOCOL 唯一拥有。
metadata:
  version: "4.0.0"
  role: "governance"
  protocol_version: "handoff-cognition/v3.0"
  business_skill: "hott-paradox-research"
  core_cognition: "核心认知.md"
---

# 本地 HoTT 交接治理差异层

本 Skill 不是第二份启动流程或 checkpoint 合同。先按根 `AGENTS.md` 判定档位，再读
`.codex/cognition/LOAD_SET.json`、`.codex/cognition/PROTOCOL.md` 与角色表；纯治理不因此自动开始数学研究。
目录名 `.codex` 是历史路径，不限定宿主。能够读取 repo 文件并执行 `python3` 的宿主共享同一真值树、
runtime 和中立收据；宿主差异只写入 session 的 `host/model/tier/load_receipt` 元数据。

## BLOCKED_FULL_SET_COGNITION

当本档位要求的启动文件或四件套任一逻辑全文缺失、读取被截断、读取中变更、hash 与已声明身份不符，
或 v2 index 的 table、`last_shard`、`append_target`、标题/路径不一致时，停止为
`BLOCKED_FULL_SET_COGNITION`。不得以摘要、manifest、关键词、旧 receipt、KC 子集或单一 shard 替代。

处置顺序是：记录缺口和实际已读范围；停止相应研究或 mutation；移除四件套之外的非必要载荷；在足够容量
的宿主重建加载；只有用户明确缩小任务时才按新档位重判。工具的 bytes/hash 或 `FULL_EMITTED_BYTES_MATCH`
只证明文件输出身份，不能证明模型理解、数学命题或现实对应。来源快照、`private-audit/`、用户移走的路径和
历史 AI 自述仍按根 AGENTS 的来源边界处理，不因 BLOCKED 而恢复、改写或补造它们。

## 分片核心认知审计集

每个实质研究、审计、设计或代码单元在
`.codex/research/hott/sessions/<SESSION_ID>/` 保存 `CORE_COGNITION_AUDIT.md` 索引及同名分片目录。
索引含 session、当前 core identity、四件套交叉字段、分片表、计数、冲突/未知和裁决；v2 index + table
全部分片才是完整审计。checkpoint 时 `SESSION.md`、`RUNS.json` 与审计索引/分片必须满足 runtime 的原子 bundle
检查，唯一应用收据仍是 checkpoint `result.json.status=CHECKPOINT_COMMITTED`。

核心认知逐条立场必须可证伪。触及、张力延续或裁决延续项写五元组：
`relation | 该条要求的工作姿态 | 已走过的路实际做了什么（含证据定位） | 为什么是该 relation | 下一选择 + 反证条件`。
其余 KC 仍逐条登记 `NOT_TOUCHED` 与下次触及条件；运行时要求较厚的结构条目时补足其证据与论证字段。
合法 relation 仅为 `ALIGNED`、`DEEPENED`、`CORRECTED`、`TENSION`、`DEVIATED`、`NOT_TOUCHED`。`NOT_TOUCHED`
不是空白；`TENSION`/`DEVIATED` 必须给纠偏和回航动作。任何 relation 都要说明什么新证据会改变判断。

扩展认知按 `##` 小节或声明的触及片回评：工作姿态、已走过的路及其证据、偏航诊断、下一选择。审计还必须
分开「已走过的路」与「即将作出的选择」：后者列全部候选、各自支持/可能违背的 KC 或扩展认知、裁决、反证条件
和回退路径。若审计改变 `next_minimal_verification`，先通过授权 checkpoint 更新 STATE，再执行新方向。

## 历史 AI 覆盖分母

历史审计至少分开以下分母及证据层：LocalGPT 的父线程与 HoTT-2 关系、38 turns/41 条真实用户消息、
220 条可见 assistant、canonical tool call/result、失败/重试/中断/compaction 与 Git/产物；WebGPT 的
56 Prompt、55 Response、111 UI sections 及其到 workspace `R###`/SESSION/artifact/Git 的连接；Gemini 的
22 user、24 ordinary text、21 thought、17 executableCode、17 codeExecutionResult、2 inlineFile、1 Drive reference。
inlineFile 是代码载荷；缺失 Drive 正文标 `ATTACHMENT_BODY_UNAVAILABLE`。ledger 各自拥有 schema/分母/证据等级；
来源 hash、AI 自述或文件存在不能单独升级为数学结论或完整历史审计。

完整启动、tier、压缩重付、关系水合、分片写入、数学证明门禁、checkpoint、恢复与停止条件见
`.codex/cognition/PROTOCOL.md`；当前任务、权限、来源边界与 Git 行为见根 `AGENTS.md`。业务研究方法仍在
`hott-paradox-research`，方案步骤仍在 `hott-paradox-search-sop`；本差异层不扩大它们的授权。
