---
name: hott-session-governance
description: ALL-Markdown/HoTT 的跨 Session 治理入口。自动路由每次完整认知恢复、历史研究来源与证据分层、动态依赖、当前工作记忆、里程碑 checkpoint 和结束回读；用于新会话、继续、压缩恢复与治理审计，不代替 HoTT 数学业务，不扩大权限。
metadata:
  version: "1.0.0"
  role: "governance"
  protocol_version: "1.3.0"
  business_skill: "hott-paradox-research"
---

# HoTT 跨 Session 认知与交接治理

## 1. 名称、入口、职责

本 Skill 的独立名称为 **hott-session-governance**。业务 Skill 为 **hott-paradox-research**。根 AGENTS 是总入口，`.codex/skills/SKILL_ROLES.json` 是角色/路径登记。没有第三份研究目标、第二份主张矩阵或第二套状态引擎。

收到 HoTT/研究继续/治理相关请求，新 Session 或压缩后：先完整读根 AGENTS、两类 Skill 和角色表，执行本协议，再根据本轮任务选择业务工作或治理工作。用户无需分别命名两个 Skill；调用业务即包含治理生命周期。仅审计/维护治理不自动执行数学研究。

同一次进入中的“治理→业务→治理保存”是一条调用链，不因为内部委派而反复重入、无限重读。真正新 Session、用户再次要求继续而进入 Skill、压缩或上下文丢失，每次都重置并重新全文加载。旧收据/相同哈希不得免读。

## 2. 先明确实际目录和当前权限

从当前 Skill 的项目相对位置解析根，不使用历史 `/Volumes/D/...` 或固定旧 sandbox 根。恢复包不是原主机实时环境。记录本轮 read/write/execute/network/external-mutation 权限；Chat、Work、模型、其他AI、Git/发布不能由历史 MEMORY 授权。

无 Git 时记录 UNKNOWN，用原包、改前字节和哈希保全，不创造伪提交。遇只读挂载，不提权；可在当前明确授权下另建可写工作副本，必须说明真正路径及原目录没有被改。

## 3. 每次完整恢复

按 `.codex/cognition/LOAD_SET.json` 与当次 `.codex/research/hott/STATE.json` 生成集合。先完整读取第五闭包，其次完整读取已对齐三问；全部正文及历史原文附件从首行到实际末行，不固定旧行数、不用摘要/关键词片段/变量读入/仅哈希代替。

其后完整读根 README/MEMORY、指定来源、研究 owner/矩阵、Schema 入口、本协议、两类 Skills 与角色表、STATE、FRONTIER/LESSONS/RESUME、最近 Session、活动/待复核/未解决记录及递归依赖的完整正文。

加载引擎每次根据 records 的开放状态自动加入记录，不只依赖手工 active/review_due/unresolved 列表。任何实际用于本轮的旧结果还须登记为依赖；已关闭且无关的历史可不注入，但不得删除原文。源缺失不能伪称完整恢复。

分页绑定同一 snapshot。加载过程中若源/STATE/HEAD变化、发生截断或压缩，就重新计划并从头全文读。正文真的进入模型上下文才算加载；coverage 工具只核文件范围。受权工作完成加载后可以产生新文件和 checkpoint；它们是本轮输出，不意味着每写一文件就无限重启。外部输入改变或新工作依赖未加载材料时，先重新恢复相应有效输入；新入口或压缩仍强制全套重读。

## 4. 必须恢复“做过什么”，不能只有理念

从完整研究记录回答：原任务/理论配置是什么；实际构造与推演是什么；哪些反解释成功；哪里失败、为什么；证明/计算/现实桥梁/原创性/外审各到哪里；下一动作是什么、为什么。

MEMORY 的概述只能导航，不能代替当前依赖的研究正文。只有会话说法却缺原报告时，保存可见公开文本或明确标记的恢复记录，另记 source_gap，不能编造原实验、源代码、旧 hash 或 PASS。登记记录的字节完整性不提升其数学可信度。

R001 当前具体入口是 `.codex/research/hott/imports/R001/`。其原实验与完整原研究包未随当前附件到位；恢复档案可以提供历史认识，但使用其结论作新证明前仍需回源或独立重建留证。缺件只限制相应认证，不关闭全部研究。

## 5. 语义接续核对与开放思考

全文后明确本轮目标、与九类方向的关系、实际配置、既有状态、最近失败和下一自主动作；不要求用户重新确认普通选题。这不是替代全文的摘要，也不是隐藏思维链。

共同问题、证据责任和授权要连续；方法与结论可修订。业务 Skill 的操作库不是智能许可清单。新构造、反模型和不同路线可直接尝试，治理不能要求预设 HoTT 必错/必对、每轮必须突破或消耗完资源。

## 6. 里程碑与结束自动交接

在当前获准写/执行时，每个实质里程碑和结束前：保存新的不可覆盖 Session 记录；同一 checkpoint 提交根 MEMORY、FRONTIER、LESSONS、RESUME、STATE；正文提供本轮公开请求、输入版本、实际动作、结果/失败、proof_delta、依赖影响、未知和下一动作。

STATE 必须登记新研究正文与证据，不只在最终回复贴链接。R001 式来源缺口必须有独立记录；所有重要开放事项须登记，不能只有 MEMORY 一行。

commit 后回读新 HEAD/STATE 和修改正文；新调用的 plan 必须包含本次 Session、最新 MEMORY 与本次依赖。只有成功且实测可重载才称 CHECKPOINT_COMMITTED。无权限/中断/失败标 CHECKPOINT_NOT_SAVED，并交付可恢复文本，不宣称已持久化。

## 7. 一致性、关闭与变更

旧 snapshot 被拒绝；不能最后写者覆盖。未完成事务拒绝混合加载，恢复须确认旧写者已停止，禁止擅自抢锁。变更相关 source_hashes 时附实质复核说明；下游受影响记录待复核，不用换 hash 消除数学问题。

从 open/active/pending/blocked/in_progress/review_required 移出时，必须有 resolution.reason 和非空 resolution.evidence 路径。工具检查字段和证据文件存在，不认证理由正确。不能仅移出 unresolved 列表或写 CLOSED 隐藏未解决历史；原路径/record ID保留。

会话中的证据质量应原样传承：会话报告、重新整理的档案、原始代码输出、独立复现/专家意见分别登记，重复引用不增加真实性。旧结论→新证据→修订→受影响依赖可追溯。

## 8. 执行工具和验收范围

唯一引擎继续使用 `.codex/skills/hott-paradox-research/scripts/cognition_runtime.py`（兼容路径）；plan/read/check只读，checkpoint默认dry-run，显式apply且本轮授权才写。协议细节见 [PROTOCOL](../../cognition/PROTOCOL.md)。

代码测试模拟的是文件调用者，不是不同 AI。新进程能读到新状态只证明文件路由与持久化，不证明 AI 必然理解。宿主是否自动读取根 AGENTS 需实际环境支持，不能通过一份文档保证。容量不足不得偷换摘要；不承诺无限上下文或后台连续工作。

外部 repo-cognitive-closure 若已提供则按真实正文使用；没有则明确未调用，以本地实际来源和协议完成可执行范围，不假装安装或启动其它治理系统。
