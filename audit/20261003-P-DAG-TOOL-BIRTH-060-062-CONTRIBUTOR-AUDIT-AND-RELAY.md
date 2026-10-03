# P-DAG H060–H062：派生刀具来源门的独立审计与贡献分支交接

> **身份：** `CANDIDATE_NOT_CURRENT / CONTRIBUTOR_AUDIT / METHOD_CLARIFICATION_CANDIDATE / NOT_A_ZFC_OR_POWERSET_RESULT`。
>
> **分支边界：** 本文写于 `codex/p-dag-tool-birth-audit`，其起点为
> `19a16de82cd4023ed4fd892d00b9dbdf1436fcf9`；审计时观察到 canonical `dev` 为
> `c1be72b05e970e9aaf8db3d3a36d4ea987c2da73`。本分支没有修改 `MEMORY`、`STATE`、
> `feature-list`、`rulings` 或 `dev-docs/模式P三把刀/012` 等 current owner。

## 1. 这次审计回答的精确问题

H054–H059 已正确把“忒修斯式 history → snapshot → identity”保持为
`NOT_ENOUGH_EVIDENCE`：没有一个真实同层 consumer 需要在同一 Done 中区分
continuation 与 reconstruction。

这里新审的不是 ZFC 或 Power Set，而是一个方法边界：现行 Tool-Birth 合同是否已经清楚地
禁止把这种**合成控制中出现的、尚待来源验证的条件接口**称为
`DERIVED_TOOL_CANDIDATE`？

结论分两层：

```text
Trace–Snapshot–Identity / Power Set: NOT_ENOUGH_EVIDENCE（不变）
Tool-Birth contract wording: source-realization clarification candidate（新增）
P4 / new numbered tool / ZFC Q / mathematical claim: NONE
```

它不是把一个“没有找到”误写为新刀。相反，它把 synthetic clue、真实 consumer 与工具升级门分开。

## 2. 直接合同证据与 Master 判词

在 canonical `dev@c1be72b0` 的
[`新刀具出生与花纹宇宙合同`](<../dev-docs/模式P三把刀/012 - 新刀具出生与花纹宇宙合同.md>) 中：

- §2 把 `theory variant / object / input / process / observation / Done` 列入
  Tool-BirthCard，并把 `source / worker plan` 表述为“哪些 source、节点**可验证**该判断”；
- §3 的 `DERIVED_TOOL_CANDIDATE` 只要求组合的基本判断可以还原到旧刀；
- §4 的新编号门也只要求“一个来源或运行**计划**”。

这些条目是必要的，但文字本身没有要求：在给理论花纹使用
`DERIVED_TOOL_CANDIDATE` 或 `UNCONTAINED_PATTERN_CANDIDATE` 前，必须已有一个固定、
实际、来源定义的同一任务 consumer，且它的 I/O/Done 真会随所称差异而改变。计划如何将来验证，
与已存在的 source realization 不是同一件事。

**Master textual verdict：** 应将这一点补成 Tool-Birth 的显式 promotion guard。这个 verdict
只针对合同歧义；它不等于 H054 的花纹已经通过该门。

## 3. H054–H059 为何仍停在 `NOT_ENOUGH_EVIDENCE`

| 证据 | 已经显示的事实 | 对本次问题的作用 |
|---|---|---|
| H054 | 合成 replacement/reassembly 端点可有相同当前 subset 而不同 lineage。 | 只给 pattern clue。 |
| H055 | endpoint 保留 `(subset, immutable lineage)` 后，假定 identity task 可以区分。 | 说明表示层修复可能存在，不能证明某理论做不到。 |
| H056 | Metamath extensionality / power-set 卡没有 provenance、identity consumer 或 Done。 | bare Power Set source 没有同一任务。 |
| H058 | Mathlib NFA 把 concrete path 压到 endpoint set；language acceptance 的 Done 只要求存在接受终点。 | 真实负控制：历史丢失可对实际任务完全正确。 |
| H059 | sealed arbiter 仍返回 `NOT_ENOUGH_EVIDENCE`。 | 不允许把条件接口升级为 tool。 |

因此，提议的 guard 不会阻塞 H054 作为一遍匹配的可证伪线索；它只阻止该线索在没有实际
consumer 前越级为派生刀具。

## 4. 新节点、运行边界与 trajectory receipt

| 节点 | 身份 / 结论 | 运行与行为边界 | raw wire SHA-256 / public terminal |
|---|---|---|---|
| H060 | `INPUT_CONTRACT_FAILURE / NO_AGENT_OUTPUT`：prompt 少 `BEGIN FROZEN SOURCE CARD`。 | 模型采样前退出；无 wire、工具、文件或审批。 | 不适用。 |
| H061 | `source-realized same-task` guard 应显式加入；当前 Theseus 卡仍 `NOT_ENOUGH_EVIDENCE`。 | `gpt-5.6-terra / max`；read-only、禁网、`approval=never`；prompt gate PASS；0 command/file/approval。 | `ba693905d38039c354a3f2594c46e8c4a5ba1cd81bbe2f90819a9e771665937c` / `:804`。 |
| H062 | 合同原文不明确要求 actual source realization；需最小文字澄清；没有实际理论花纹通过。 | 同一 exact execution envelope；prompt gate PASS；0 command/file/approval。 | `48ecbdcd27debed5455916367919a86e58ae02aaadef0ac30bc097fe131a0c70` / `:579`。 |

对 H061/H062 均已用 shared `session_trajectory.py` 运行
`catalog → tree → assistant terminal → coverage`。两个 raw wire 都有一条 terminal turn；coverage 均报告
`tool_calls=0`、`tool_results=0`。其 L1/L2/L3 是 `NOT_TESTED`／`NOT_OBSERVED`，L4/L5 分别仍须语义审查和
接受证据；本文不从 reasoning 项或 final 文字反推出隐藏思维。

H062 末行选择了 `BATTLE_INCONCLUSIVE`，因为它没有也不应裁定任何实际理论花纹；但它对**文本问题**的
公开 ledger 与 H061 一致：`source / worker plan` 是 prospective validation，不能代替一个 actual
source-defined same-task consumer。Master 的“需要澄清”只以合同原文和这一公开、可反驳的理由为依据，
不以两个 agent 的一致性为依据。

## 5. 与原初锻刀理念的逐项自审

| 原初要求 | 本单元的对照 | 判词 |
|---|---|---|
| `Claude-罗素原则P1至P3`：理论论域元素的存在性追问必须属于理论面对的问题。 | promotion guard 要求固定理论卡与实际 consumer，避免把合成故事换成理论 X 的 Q。 | `ALIGNED`。 |
| `GLM-算符先行于存在性落定`：对象在合法性未落定前被同一理论算符使用，才形成张力。 | guard 要求同一 source 的 C/I/O/Done，避免把对象、过程与消费者拼自不同故事。 | `ALIGNED`。 |
| `Codex-模式P与一遍匹配`：P 写对后，AI 应一遍匹配出线索，不必遍历理论细节。 | guard 位于**候选升级后**，不限制 H054 的 deidentified clue；它要求随后 source validation。 | `ALIGNED`。 |
| 2026-10-02 用户直接要求：三刀的惯性可能限制花纹宇宙，新刀出生与系统自审必须进 Git。 | H054–H062 逐刀做 containment / controls；H060 的失败与 H061 的最小重放均保留为精确 Git 谱系。 | `ALIGNED`。 |

对偏差的分类是：

```text
H060: RUNNER_OR_EVIDENCE_FAILURE / INPUT_CONTRACT_FAILURE
H061: functional replay after one frozen marker correction
contract wording: IDEA_SPEC_INCOMPLETE candidate at the promotion boundary
actual Theseus pattern: NOT_ENOUGH_EVIDENCE, not OLD_TOOL_FIELD_GAP
```

这里的 `IDEA_SPEC_INCOMPLETE` 是**候选的合同层判词**：用户原意已经区分“AI 先看到线索”与“打理论 X 的
问题”，而现行 Tool-Birth 文本没有把这两个阶段的来源门写明。它不表示用户原初理念被反证，也不表示
P1/P2/P3 需要增加第四把刀。

## 6. 最小候选修订：不新增状态、不新增刀

建议 canonical integrator 在 `模式P三把刀/012` 的 §3 之后审阅并选择性加入以下文字：

```text
### Source-realization gate

对一个理论 X 的花纹，在使用 `DERIVED_TOOL_CANDIDATE` 或
`UNCONTAINED_PATTERN_CANDIDATE` 前，Tool-BirthCard 必须引用一个固定、实际、
来源定义的同一任务：写明 T、对象、consumer，以及该 consumer 的输入、操作、观察和 Done。
所称 distinction 必须改变该同一 consumer 的 observation 或 Done；只给合成／假设接口、
将字段拼自不同任务、或只给未来的 source/worker plan 时，花纹状态只能是
`NOT_ENOUGH_EVIDENCE`。它可以保留为 conditional interface sketch，但不是已成立的派生候选。

本门不限制 P-DISCOVERY 的一遍匹配线索，也不阻止 `OLD_TOOL_FIELD_GAP` 用于运行器、prompt
或既有字段的局部修复；它只约束理论花纹向派生／未容纳候选的升级。
```

这比新建 `PRE_SOURCE_INTERFACE_SKETCH` 枚举更小：现有的 `NOT_ENOUGH_EVIDENCE` 已能忠实表示它，
而新状态会无必要扩大合同和回归矩阵。

## 7. 当前 source denominator 已失效，禁止把本报告写成“全历史已对齐”

canonical `dev@c1be72b0` 新增的
`scripts/audit/verify_pattern_p_tool_history_sources.py` 期待 `dev-notes/0109` 的旧快照：

```text
expected: 1719 lines / 141651 bytes /
          fdb556b5173f9138880ad94c8e0b1a4d47fb90f73aeeca48f05bb1f9a5e8769c
actual:   1849 lines / 150776 bytes /
          fd0c995bd31195514ef469583a1dc9b2e6624e043b451b1ecbe84c9a08247c55
```

该文件目前是 original worktree 中的 untracked conversation archive。其新增区块从第 1722 行开始，
包括研究发起人的直接“持续锻刀、花纹宇宙、Git 谱系、全历史自审、忒修斯/Power Set”要求；本分支
已把该 7 行直接消息保存为[候选来源快照](<20261003-P-DAG-TOOL-BIRTH-ORIGIN-DELTA-SOURCE-CANDIDATE.md>)，
但它仍不是 canonical curation。验证器
**正确地**返回 `FAIL`；此前历史回答中的“18 项 PASS”已过时，不能用于本单元的 full-origin 对齐声明。

本报告没有试图覆盖、提交或手改该 original worktree 的 untracked archive。它仅登记：

```text
STALE_SOURCE_REAUDIT_REQUIRED
full-origin alignment: BLOCKED_PENDING_CANONICAL_SOURCE_REFRESH
H061/H062 local method evidence: still usable within their frozen source scope
```

## 8. Canonical integration checklist

1. 由 canonical integrator 先保存／curate 第 1722 行起的 user-direct turn，给它稳定来源身份、hash 与
   `IN_SCOPE` / `PRECURSOR` 处置；更新 full-history audit 的分母和 source verifier，直至实际 PASS。
2. 重新读取该刷新后的 full audit，确认“source-realization gate”仍忠实于用户的 P、一遍匹配和新刀要求。
3. 如接受 §6 的文字，原位更新 `dev-docs/模式P三把刀/012`、相应动态 DAG self-audit owner 和回归样本；
   不要在 contributor 分支把候选描述改为 current truth。
4. 用三项回归检查候选门：H054 synthetic sketch 必须保留 `NOT_ENOUGH_EVIDENCE`；H058 的真实 NFA consumer
   必须因 path identity 不影响其 Done 而仍不通过；一个未来真实同层 identity consumer 才可进入
   `DERIVED_TOOL_CANDIDATE` 的 containment 审查。
5. 在 expected target HEAD 上复核、精确 stage、运行 shard/source/diff 检查并提交；之后才更新
   MEMORY/STATE/Feature 等 canonical projections。

## 9. 贡献分支收据

本分支的精确可复查提交：

```text
e15364a9  research: freeze derived tool source gate critic
43bd4b90  fix: replay derived gate critic with source marker
59b51568  research: freeze derived tool source gate arbitration
<next commit> audit: relay derived tool source gate clarification
```

它们只新增独占 `audit/20261003-P-DAG-TOOL-BIRTH-060*`、`061*`、`062*` 路径及本文。
它们不能自行把 current `dev` 的方法合同或研究状态推进；交接时必须在 canonical target 的最新 HEAD 上
重新核对同名路径和 source denominator。
