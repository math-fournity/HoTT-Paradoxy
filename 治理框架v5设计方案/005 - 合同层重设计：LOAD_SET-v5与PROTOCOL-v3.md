# 合同层重设计：LOAD_SET v5 与 PROTOCOL v3

（对应《机制报告》003：PROTOCOL / LOAD_SET / SKILL_ROLES / 治理 Skill 的调查结论）

## 1. LOAD_SET.json → v5（tiered schema）

**原来存在什么问题**：v4 只有 governance/research 两档且都含全量启动核——
层机制本身精良（query_first 是框架最成功的减容战役，F-012：-97%），但最大的
账本 STATE 被填进了 always_full_boot（机制报告 007："机制只建了一半"）；
没有"轻任务"层，强度无梯度。

**打算如何调整**（schema 骨架）：

```json
{ "schema_version": "cognition-load-set/v5",
  "policy": "TIERED_CLOSURE_WITH_RECEIPT_REATTESTATION",
  "tiers": {
    "T0-lite":     { "boot": ["AGENTS.md","MEMORY.md","MEMORY/001*.md"],
                     "four_set": false, "state": "hot_only",
                     "end_obligation": "none" },
    "T1-standard": { "boot": ["<瘦身启动核>"], "four_set": false,
                     "state": "hot_plus_active", "end_obligation": "session_lite" },
    "T2-research": { "boot": ["<瘦身启动核>"], "four_set": true,
                     "extra": [".codex/skills/hott-paradox-research/SKILL.md","三问","FRONTIER-hot","LESSONS-index","RESUME-hot"],
                     "end_obligation": "audit_sharded_touched" },
    "T3-mutation": { "same_as": "T2", "gates": ["math_proof","atomic_checkpoint","full_kc_audit"] }
  },
  "state_hot_fields": ["active","latest_session","current_core","unresolved","revision"],
  "compaction": { "mode": "receipt_reattestation",
                  "full_reload_triggers": ["core_sha256_changed","tier_escalation","user_order"] },
  "query_first": ["<原清单 + STATE-archive>"], "task_expand": ["<原清单>"] }
```

（瘦身启动核 = 现核去掉 STATE 全文换成 hot 快照、MEMORY/003 换队列+上限片、
README 压成单片导航；详见分片 006/008。）

**为什么调整后更好**：档位成为数据而非散文，runtime `--tier` 展开与 fail-closed
语义原样复用（v4 已验证的机制不动，只换数据）；"轻任务合法化"有了机读载体；
压缩策略从唯一全额重付变为收据制+三触发器——重付成本从 49.7 万降到 ≈6 千
（启动核瘦身后）+ 复认 ≈2–3K。

## 2. PROTOCOL.md → v3（分档步骤）

**原来存在什么问题**：八步硬步骤对所有任务一视同仁——步骤本身正确
（闭包→交叉→动作的时序防伪设计有效），但把它套在 T0 任务上是纯开销；
且 §2 要求"完整读取 STATE.json"，与 STATE 体量形成物理冲突（机制报告 007：
这是被绕过的直接诱因之一）。

**打算如何调整**：步骤改为**分档参数化**——同一条流程骨架（闭包→资格→交叉→
动作→回评→写回），每步标注 T0–T3 的执行深度（如"交叉审视：T0 免、T1 查
latest+active 一致性、T2/T3 全三方"）；"STATE 完整读取"改为"按档读 hot 快照/
hot+active/全量（仅 T3 迁移时）"。新增第 0 步：**档位判定与声明**（判据表 +
会话首条声明 + 越档即停）。invariant 章成为唯一不变量定义处（吸收 .codex/AGENTS
的复述职能，见分片 004）。

**为什么调整后更好**：保留时序防伪（这是机制报告 009 认定的有效原理），砍掉
与任务风险不成比例的深度——正是消融实验显示"可以低成本替代"的那部分；
"完整读取 STATE"义务与 STATE 体量的冲突从根上解除（义务还在，对象变成 hot
快照 ≤3K）。

## 3. SKILL_ROLES.json（原位，内容微增）

**原来存在什么问题**：无实质问题（机制报告 003：240 tokens 买掉一整类路由
故障，性价比最高）——只有叙事上的宿主联想（路径在 `.codex/` 下）。

**调整**：文件**原位不动**（`.codex/skills/SKILL_ROLES.json`；2026-09-18 修订：
默认方案不迁移树，更名随之取消——路径绑定由分片 003 的叙事层声明解除），
内容加一字段 `"host_binding": "none"`，其余不动。**为什么**：好部件不值得动；
"宿主中立"的实质在声明与路由，不在文件名——零行为变化买到同样的单套性。

## 4. 治理 SOP（原 hott-local-session-governance SKILL，19KB/≈5,833 tokens）

**原来存在什么问题**：约 60% 与 PROTOCOL/AGENTS 互相复述（三份文档讲同一套
八步/审计/checkpoint）；自身内嵌 generation-4/36（又一处漂移）；19KB 的
"讲如何省上下文的文档"本身是启动核第 4 大件。

**打算如何调整**：瘦身到 ≤6KB 的**差异层**——只保留三块别处没有的内容：
(a) BLOCKED 停止协议的完整分支表；(b) 审计集格式细则（五元组/relation 词表/
反证条件——020 合同的正文）；(c) 历史 AI 覆盖分母（LocalGPT/WebGPT/Gemini
计数）。八步流程、checkpoint 规则、分片合同全部改为对 PROTOCOL/合同文档的
单行引用。frontmatter 保留（Codex 发现兼容），正文宿主中立化。

**为什么调整后更好**：三份复述变一份权威+两份指针，同步面 O(N)→O(1)；
启动核再减 ≈4K tokens；反证条件化审计等真正独创的内容反而更突出（不再淹在
复述里）。依据同机制报告 003 的自指观察——"讲省上下文的文档不该是最贵的文档之一"。
