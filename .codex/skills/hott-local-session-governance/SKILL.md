---
name: hott-local-session-governance
description: HoTT项目各档共用的认知与任务角色治理。新Session、跨Session、压缩恢复、角色切换以及治理/机械任务均先用它加载最高指示并确定消费角色；另负责BLOCKED、KC审计和来源边界。第三轮执行/审计路由到专用Skill，不自动启动研究。
metadata:
  version: "4.4.0"
  role: "governance"
  protocol_version: "handoff-cognition/v3.2"
  business_skill: "hott-paradox-research"
  core_cognition: "核心认知.md"
---

# 本地 HoTT 交接治理差异层

本 Skill 不是第二份启动流程或 checkpoint 合同。先按根 `AGENTS.md` 判定档位，再读
`.codex/cognition/LOAD_SET.json`、`.codex/cognition/PROTOCOL.md` 与角色表；纯治理不因此自动开始数学研究。
目录名 `.codex` 是历史路径，不限定宿主。能够读取 repo 文件并执行 `python3` 的宿主共享同一真值树、
runtime 和中立收据；宿主差异只写入 session 的 `host/model/tier/load_receipt` 元数据。

## 全Session输入、任务选择与恢复

先完整执行全局repo-cognitive-closure，再读root AGENTS和`TASK_ROUTING.md`。所有项目Session均全文读
单体`最高指示.md`；按当前用户/实际Goal选RESEARCH_GENERATION、INDEPENDENT_AUDIT、SOURCE_EXPLANATION、GOVERNANCE_ALIGNMENT
或MECHANICAL_CONTEXT，并回答其§0A对应理解题。角色只改变消费/行动，不改变读取范围或扩大权限。

匹配原第三轮A/B时分别读执行/审计Skill与Goal6/Goal6-audit及其领域细则；匹配续做C/D时复用同两Skill的
Goal7分支，完整读root`goal-7.md`/`goal-7-audit.md`。C补父范围充分性与研究义务，D审C固定新交付；
旧A closed/旧seal不授予新完成资格。路径按repo根及`.codex/skills/`解析；即使host未显示Skill也实际读取。
按实际用户/Goal/角色选择，不能因编号最新切换。新包只准备时，不注册C研究状态、不启动任务。

新Session、跨Session、压缩、角色/版本变化后，先重新全文读共同入口、当前角色Skill、单体闭包和最高指示，
然后回当前owner/证据恢复阶段、未证项、已失败动作和下一步。研究每换理论单元/主要靶前提另全文重读最高指示；
普通后续turn做有效性检查，不每条命令重复。四件套按原档位和source-first触发，不能以本入口替代它们。

公开恢复说明含任务/角色/实际读取版本与EOF、原意/验收、未完项和下一动作；不输出隐藏推理。缺件/截断先补，
源冲突停相关决定；旧Goal、最大编号或近期日志不能获得活动资格。Task路由只管入口，STATE仍管研究current事实。

本Skill被T0/T1调用也不自动触发数学研究或T3写回。B的自身审计记录可以在明确获准路径保存，但不能推进
STATE/投影、修A成果或Git提交。用户仅让准备A/B材料时不创建/启动任何其他AI。

## 视觉证据的压缩恢复

标识：`VISUAL_EVIDENCE_WRITEBACK_V1`。当 PDF 页图、截图、图表、白板或任何图像观察将承担来源、运行、数学、审计或项目状态判断时，图像被显示给当前会话不构成可恢复证据。实际检查完一个任务定义的最小视觉单元后，必须在打开下一视觉单元前，把它的输入身份、定位、观察、证据等级、边界和下一游标写入该任务**已有**的 evidence owner。

压缩、新Session、交接、工具中断或无法确定是否已写入时，先读取该 owner；只有其中已落盘的视觉行／卡可被消费。已渲染、曾在对话中查看、或只存在于 assistant 叙述中的图像观察，一律按`RENDERED_UNAUDITED`／未审阅处理，并从原图或原件重新检查。不得用压缩摘要、语言模型记忆、旧 assistant 文本或“看起来像已读”的页图名称补写结论。

该规则不要求建立统一截图数据库、每页新文件或每次视觉操作提交 Git。它要求复用任务已有的来源笔记、运行收据、视觉审计或其他 evidence owner；视觉单元的大小由任务风险和观察粒度决定。写入、运行和一次恢复演练只能证明其明确范围，不能认证所有未来模型、所有图像任务或每次压缩都自动遵循本规则。

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

## Turn级核心语义再对齐

`CORE_SEMANTIC_REALIGNMENT_V1`补充的是Session加载后的认知消费。用户询问或纠正其悖论观、数学哲学、
现实同一性、时间／时序、构造过程、ASK、理论经济等core含义时，先读取相关完整KC与扩展认知owner shard；
跨主题总论、AI误解／偏航复盘或无法确定KC时完整重读这两个逻辑文档。近期报告、MEMORY、方向／全景、
load receipt与hash不得替代。

回答前明确：用户主张、禁止收窄、对当前任务的作用、仍待证明的义务；随后才可用外部通常解释作评价。
纯机械T0/T1工作可以不触发，但不能附带core语义判断。实际read与final locator是一次行为证据；本Skill、
validator或一次成功不认证所有未来turn。完整触发与失败处置以PROTOCOL §2A为准。
