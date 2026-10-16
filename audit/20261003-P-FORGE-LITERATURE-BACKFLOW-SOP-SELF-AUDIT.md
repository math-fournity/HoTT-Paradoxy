# P-FORGE 路线级文献回流审计 SOP：首次设计自审

> **身份：** SOP_DESIGN_SELF_AUDIT / GOVERNANCE_ALIGNMENT / NOT_B0_TO_B5_EXECUTION / NOT_A_ZFC_Q_OR_MATHEMATICAL_RESULT。
>
> **审计对象：** P-FORGE-LITERATURE-BACKFLOW-AUDIT-SOP 的首次设计、入口和 writeback；不审计候选文献的数学内容，不替代实际文献回流。

## 1. 审计范围与输入

本次审计针对研究发起人的要求：将新一轮“路线级文献回流审计”完整记录、命名、标准化、checklist 化，并审计这份方案是否真的服务于“锻刀与发现 ZFC Q 是同一个共同收敛过程”。

直接输入是：

1. 核心认知 KC-000056--KC-000062：基础理论靶、罗素计算--存在--自指模式 P、明显核心承诺和一遍匹配启发式；
2. P-FORGE 原子审计 A3：130 个历史单位、Q-0 UNFORMED 和 ZFC_Q_NOT_LOCATED 的受限结论；
3. 候选 ref codex/hott-motive-zfc-literature 的可读 archive：其 R_i → Z_i → Q_i 研究、Power Set-subset/RepFun 路线控制和 H0→Z0 反类比；
4. 当前 dev 与候选 worktree 的 Git 身份核对：候选是 CANDIDATE_NOT_CURRENT，旧 integration handoff 已滞后，候选 worktree 有未提交路径；
5. 新 SOP 的索引与三片正文。

本自审不把候选 archive 的来源主张升格为 dev 当前事实。它也不宣称 B0、B1、B2、B3、B4 或 B5 已经被执行。

## 2. 标准 checklist 的自审结果

| ID | 审计问题 | 证据 | 结果 |
|---|---|---|---|
| SA-01 | 是否有稳定、可在 /goal 引用的名称？ | SOP 索引标题与第 5 节 | PASS |
| SA-02 | 是否把锻刀与发现 Q 编译到操作字段，而非停在宣言？ | RB-D12/RB-D13、I0--I4、CL-4 | PASS |
| SA-03 | 是否阻断 R_i→Z_i→Q_i 的直接跳跃？ | 索引第 2 节、001 §3.1、002 判词字典 | PASS |
| SA-04 | 是否阻断 H0→Z0→Q0 的类比偷换？ | T0--T5、TRANSPORT_ANTI_ANALOGY、CL-2 | PASS |
| SA-05 | 是否把历史 AS_RUN 与文献回流 delta 分开？ | 002 §4--§5、CL-4 | PASS |
| SA-06 | 是否要求 formation route、actual consumer 和 T/u/F/C/I/O/Done？ | RB-D04、RB-D06--D10、RouteBackflowCard | PASS |
| SA-07 | 是否将 payment、route mismatch、task switch 和 source-layer control 保留为正当负校准？ | 002 §2--§3、CL-3 | PASS |
| SA-08 | 是否对候选 worktree/current owner 建立了 fail-closed 权限边界？ | 001 §2、002 B3 硬规则、003 CL-1 | PASS |
| SA-09 | 是否把影响缩小到 I0--I4 的选择性重审，避免重新跑 130 卡？ | 002 §4--§5、003 B0--B5 | PASS |
| SA-10 | 是否阻止 CANDIDATE_Q_ELIGIBLE 被误写为 ZFC Q 或数学结论？ | 002 §2、§6，003 CL-4 | PASS |
| SA-11 | 是否为 evidence freeze、路线卡、控制、写回、停止和重开提供可执行检查表？ | 003 CL-0--CL-5、完成/停止/重开段 | PASS |
| SA-12 | 是否避免新增第二套研究数据库、自动 worker、自动集成或无边界文献扫描？ | 索引 §3，003 自审问题 8 | PASS |
| SA-13 | 是否已建立本 SOP 的 discoverability 与 current-queue 路由？ | dev-docs/README、audit/README、F-043/F-044、MEMORY、rulings 的本次 writeback；全仓分片验证 PASS | PASS |
| SA-14 | 是否将计划完成和回流执行完成明确分开？ | 索引状态、003 §3--§5 | PASS |
| SA-15 | 是否包含冻结、路线卡、传输、支付、影响、停止和 /goal 启动所需的最小标记？ | 27 个 SOP coverage markers、3 个分片的只读断言 | PASS |

## 3. 发现的风险与处置

| 风险 | 影响 | 本 SOP 的处置 |
|---|---|---|
| 候选 ref 的旧交接单已滞后，且 worktree dirty | 不能把 archive 摘要当作 stable input | B0 必须重新冻结 candidate ref、target、base、selected commits 与 dirty disposition |
| 文献中存在 HoTT 动机并不等于 ZFC 有同一问题 | 容易把 R_i 直接称作 Q_i | R/Z/Q 三层和 RB-D03--D15 强制分离 |
| H0 的 HoTT 过程具有独有规则和解释桥 | 容易用“都是 universe/totality”制造错误对应 | T0--T5 任一失败即 TRANSPORT_ANTI_ANALOGY 或 TASK_SWITCH |
| 旧的 130 卡是历史 AS_RUN，不是可被新资料覆写的草稿 | 容易把新文献倒灌进旧运行 | I2/I3 只能写 SOURCE_BACKFLOW_DELTA，AS_RUN 保持 |
| 文献数量本身可导致无限准备工作 | 可能把锻刀与 Q 重新脱钩 | B1 需要最小缺口；B2/B3 只有改变 RB 维度才推进；无影响即停止 |
| 当前 user core 已保存 H0/Z0 与 P 的方向，但新 SOP 是方法合同 | 不能把本 SOP 本身误当用户一手理论主张 | 用户原话仍由核心认知/rulings/source owners 持有 |

## 4. 本次判词

~~~
PLAN_DESIGN_SELF_AUDIT = PASS_WITH_REPOSITORY_VALIDATION
SOP_STATUS             = PLAN_READY
EXECUTION_STATUS       = BACKFLOW_INPUT_NOT_FROZEN
LITERATURE_BACKFLOW    = NOT_EXECUTED
CANDIDATE_INTEGRATION  = NOT_STARTED
ZFC_Q                  = NOT_LOCATED
~~~

通过的是方案本身：它把文献回流转成可逐路线证伪的 P/Q 共同锻造程序，并保护了历史审计、来源层与任务同一性。它没有通过、也没有尝试通过的是实际 B0--B5 回流；那需要研究发起人随后启动 SOP，并从 B0 的证据冻结开始。

## 5. 已执行验证与修复

本工作单元已运行：

~~~
python3 -B scripts/audit/verify_governance_shards.py
python3 -B scripts/audit/verify_pattern_p_tool_history_sources.py --root .
git diff --check
~~~

结果：

| 检查 | 结果 | 范围 |
|---|---|---|
| `python3 -B scripts/audit/verify_governance_shards.py` | PASS；2030 个扫描索引、210 个 canonical indexes、15 个不阻塞的软行数提示 | 新 SOP 的 v2 index/三片以及全仓分片结构和 reader banner |
| `python3 -B scripts/audit/verify_pattern_p_tool_history_sources.py --root .` | PASS；18 个 Pattern-P origin sources | P-FORGE 来源历史治理约束 |
| `git diff --check` | PASS | 本轮精确路径无空白符错误 |
| 只读 SOP coverage assertion | PASS；27 个必需标记、3 个分片 | 新 SOP 的稳定名、RB-D01--RB-D16、T0--T5、B0--B5、判词、AS_RUN/SOURCE_BACKFLOW_DELTA 与 /goal 启动词 |

验证曾暴露一个与新 SOP 内容无关、但会阻塞全仓分片检查的既有 P-FORGE 结构错误：N34 的 v2 文件名包含 `P/Q`，被解释为嵌套路径；两份既有 sequential index 的 reader banner 也没有验证器规定的“缺一片即未完成”文字。本轮已将文件名规范为 `P-Q`，同步 index link、H1、last/append target 和两条 banner。这个修复已由精确 Git commit `b55fb158` 保存。它只恢复 Markdown/index 结构与既有 A3 已完成状态的一致性；没有改变 N34 的历史事实、P/Q 判词或任何数学结论。

上述检查只验证本 repo 的结构、链接/来源治理和空白符；它们不验证候选文学术正确性，也不执行 B0--B5。
