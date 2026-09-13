# 核心认知逐编号回评：S-GOV-20260913-MACHINE-OVERVIEW-M1

> generation：`core-cognition-generation-4`；KC 总数：`36`；本单元在独立 worktree 分支上实现《HoTT 非现实性悖论机器统观完整方案》的 M0/M1 并跑通 L1 校准链路。本轮不产生新的数学结论：原生内核核验的对象是已有 C-73–C-75 机制的**校准实例**，只在 `machine-overview/runs/` 留探索收据，不进入 `HoTT/CLAIM_EVIDENCE_MATRIX.md`。

| KC | 来源/语义标签 | 与本轮关系 | 本轮评估 | 证据定位 | 未决 |
|---|---|---|---|---|---|
| `KC-000001` | `LocalGPT` / HoTT悖论研究三问 | `ALIGNED` | 找什么（TaskSpec 固定任务与完成标准）、怎么找（有类型枚举 + 反例/控制）、凭什么（profile 工具链与源码 pin + 原生内核）被拆成三个可检查对象。 | `machine-overview/tasks/MS-TASK-L1-RACE-COMPLETION-001.json`；`machine-overview/profiles/l1-partiality-v0.json`；KC-000001 | 只覆盖 L1 校准片段。 |
| `KC-000002` | `LocalGPT` / Theory Schema先行 | `ALIGNED` | profile 以行号声明被用到的 Delay/bind/race/deadline 符号，`inspect-profile` 逐符号核验；没有把这一个小片段冒充全书 Theory Schema。 | `machine-overview/profiles/l1-partiality-v0.json`；`machine-overview/runs/20260913-SEARCH-L1-001/RUN.json`；KC-000002 | 全 Schema 覆盖未做。 |
| `KC-000003` | `LocalGPT` / 合取前提与稠密过程 | `NOT_TOUCHED` | 稠密性/连续运动未进入本轮 fragment；profile 明确把 L3 结构模型列为 unsupported。 | `machine-overview/profiles/l1-partiality-v0.json`；KC-000003 | L3 仍待独立研究线。 |
| `KC-000004` | `LocalGPT` / 悖论作为反证与运动前提 | `NOT_TOUCHED` | 未处理运动前提与反证结构。 | KC-000004 | 不变。 |
| `KC-000005` | `LocalGPT` / 先找悖论后作最终归因 | `ALIGNED` | 搜索先产生候选与最小见证；归因留在 `review-correspondence` 且现实桥梁显式 `UNRESOLVED`，没有要求候选先交最终归因。 | `machine-overview/reports/MS-TASK-L1-RACE-COMPLETION-001-report.md`；KC-000005 | 不变。 |
| `KC-000006` | `LocalGPT` / 时间机制不能收窄为稠密性 | `ALIGNED` | 本轮只读「回合先后 / 完成时刻」这一侧（round index、deadline）；稠密性被单独列为 unsupported，两种考察面没有被合并。 | `machine-overview/profiles/l1-partiality-v0.json`；KC-000006 | 运动结构面未研究。 |
| `KC-000007` | `WebGPT` / LLM内在知识与模式匹配 | `ALIGNED` | 本轮搜索由确定性有类型枚举完成，未接入 LLM 提议路径；`verify --proof-file` 已提供候选外部证明的受检入口。 | `machine-overview/machine_overview/search.py`；`machine-overview/machine_overview/verify.py`；KC-000007 | LLM 提议路径未接入。 |
| `KC-000008` | `WebGPT` / 历史时间悖论作为HoTT启发 | `ALIGNED` | R041/C-73–C-75 只作为搜索后的外部基准（`calibration_match`）使用，搜索本身不读答案。 | `machine-overview/runs/20260913-SEARCH-L1-002/RUN.json`；KC-000008 | 不变。 |
| `KC-000009` | `WebGPT` / 定位HoTT理论设定的时间维度 | `ALIGNED` | `≈` 忽略 round index、而 bind/race/deadline 读取它——位置被固定到具体符号行与具体见证，不停留在「缺时间」形容。 | `machine-overview/profiles/l1-partiality-v0.json`；`machine-overview/runs/20260913-VERIFY-L1-COMPLETION-002/RUN.json`；KC-000009 | 仅模型层定位。 |
| `KC-000010` | `WebGPT` / 目标是现实相对非现实性而非内部矛盾 | `ALIGNED` | 校准判词停在表示/消费者层；没有把 kernel 通过写成 HoTT 内部矛盾或现实相对悖论成立。 | `machine-overview/reports/MS-TASK-L1-RACE-COMPLETION-001-report.md`；KC-000010 | 现实相对目标未主张。 |
| `KC-000011` | `WebGPT` / 理论推演排除时序与程序显式时序 | `DEEPENED` | 机器定位了一个具体位置：结果等价主动忽略完成先后，被声明的消费者（deadline / 业务 continuation）继续读取该先后；三族最小见证原生通过。 | `machine-overview/runs/20260913-VERIFY-L1-COMPLETION-002/RUN.json`；`machine-overview/runs/20260913-VERIFY-L1-DEADLINE-001/RUN.json`；KC-000011 | 只是已有 C-73–C-75 机制的校准实例。 |
| `KC-000012` | `WebGPT` / ASK计算合法性预分析 | `ALIGNED` | 输入域、完成标准、观察与禁止信息在 TaskSpec 中先固定；类型化上下文使非法组合（deadline 之后接 race）在枚举层直接排除并被单元测试覆盖。 | `machine-overview/tasks/MS-TASK-L1-RACE-COMPLETION-001.json`；`machine-overview/tests/test_machine_overview.py`；KC-000012 | 不变。 |
| `KC-000013` | `WebGPT` / ASK深化与理论工具性异化 | `ALIGNED` | TaskSpec 的 source_basis 指向 C11 第 #2/#5 行；correspondence checklist 逐项记录被悬置因子与补偿动作类别。 | `machine-overview/reviews/RV-MS-TASK-L1-RACE-COMPLETION-001-WV-0013.json`；KC-000013 | 账本语义仍为 PAPER_ONLY。 |
| `KC-000014` | `Gemini` / 双向目标的第二方向 | `NOT_TOUCHED` | 本轮未构造「现实无法完成而被当作已完成」的 B 方向任务；校准只演示完成先后被识别遗忘。 | `machine-overview/tasks/MS-TASK-L1-RACE-COMPLETION-001.json`；KC-000014 | B 方向任务未建。 |
| `KC-000015` | `Gemini` / 抽象即否定现实前提与Z铁律 | `NOT_TOUCHED` | 未研究 Z 铁律内容。 | KC-000015 | 不变。 |
| `KC-000016` | `Gemini` / Russell的构造过程与计算合法性 | `NOT_TOUCHED` | 未处理 Russell 型构造。 | KC-000016 | 不变。 |
| `KC-000017` | `Gemini` / 训练先验批判与Thinking in my math philosophy | `ALIGNED` | 系统不预装答案：顺序置换后见证集合相同、删除 deadline 操作后 deadline 族消失（文法敏感性），二者都写进收据。 | `machine-overview/runs/20260913-SEARCH-L1-002/RUN.json`；KC-000017 | 不变。 |
| `KC-000018` | `Gemini` / Z铁律的理论工具性与时间否定 | `NOT_TOUCHED` | 未裁决 Z 铁律。 | KC-000018 | 不变。 |
| `KC-000019` | `Gemini` / 合取真值与稠密空间中的完成困难 | `NOT_TOUCHED` | 未处理稠密空间完成困难。 | KC-000019 | 不变。 |
| `KC-000020` | `Gemini` / 悖论反证、运动量子化与HoTT时间怀疑 | `NOT_TOUCHED` | 未处理运动量子化物理判断。 | KC-000020 | 不变。 |
| `KC-000021` | `Gemini` / 机器证明与真实运行要求 | `DEEPENED` | 三族最小见证各自得到真实内核运行（verify 0 / controls 0 / 负控制按预期非零 / 重放字节一致）；两次模板缺陷导致的失败运行逐字节保留。 | `machine-overview/runs/20260913-VERIFY-L1-VALUE-002/RUN.json`；`machine-overview/runs/20260913-VERIFY-L1-COMPLETION-001/RUN.json`；KC-000021 | 不是新数学 claim。 |
| `KC-000022` | `Gemini` / 两类现实相对悖论 | `ALIGNED` | 任务与 profile 把两个方向登记为后续研究线；本轮只做校准，不宣称任一方向成立。 | `machine-overview/tasks/MS-TASK-L1-RACE-COMPLETION-001.json`；KC-000022 | 两类都未主张。 |
| `KC-000023` | `Gemini` / 时间时序处理应可直接定位 | `ALIGNED` | 每个见证给出精确 (pair, context, observation) 三元组；时间相关位置具体到 round index 与 deadline 界。 | `machine-overview/reports/MS-TASK-L1-RACE-COMPLETION-001-report.md`；KC-000023 | 不变。 |
| `KC-000024` | `Gemini` / 两类时序悖论与HoTT搜索问题 | `ALIGNED` | L1 校准覆盖第一类的表示/消费者侧；第二类（绕过 ASK 宣布完成）未建任务。 | `machine-overview/tasks/MS-TASK-L1-RACE-COMPLETION-001.json`；KC-000024 | 第二类未建。 |
| `KC-000025` | `Gemini` / 自指型悖论为何难找 | `NOT_TOUCHED` | 未处理自指构造。 | KC-000025 | 不变。 |
| `KC-000026` | `Gemini` / HoTT自身自指不可越过 | `NOT_TOUCHED` | 未构造 HoTT 自指实例。 | KC-000026 | 不变。 |
| `KC-000027` | `WebGPT` / HoTT对齐程序后继承程序自反界限 | `NOT_TOUCHED` | L5 自描述线未进入本轮。 | KC-000027 | 不变。 |
| `KC-000028` | `Codex` / HoTT自反真理验证的不可停机与自馈回环怀疑 | `NOT_TOUCHED` | 未研究自馈回环。 | KC-000028 | 不变。 |
| `KC-000029` | `Codex` / 理论经济收益作为自馈回环的高风险位置 | `ALIGNED` | TaskSpec 引用 C11 经济账本行；被悬置因子（round index）与补偿动作在 correspondence 中逐项登记。 | `machine-overview/tasks/MS-TASK-L1-RACE-COMPLETION-001.json`；KC-000029 | 账本自身仍 PAPER_ONLY。 |
| `KC-000030` | `Codex` / 历史理论经济认知完整性与HoTT经济学之问 | `ALIGNED` | 补偿动作按「恢复 / 预先保留 / 新增」三分登记（deadline 族记 `RECOVERY_FROM_ORIGINAL_REPRESENTATION`，业务 continuation 族记 `PRE_KEPT_BY_TASK_DECLARATION`）。 | `machine-overview/reviews/RV-MS-TASK-L1-RACE-COMPLETION-001-WV-0013.json`；KC-000030 | 逐行任务生成仍未完成。 |
| `KC-000031` | `Codex` / HoTT严格范型可能拒绝最小理想理论的构造方向 | `ALIGNED` | declared grammar 与 unsupported 清单分离，搜索只报告本片段耗尽，不写成 HoTT 覆盖结论。 | `machine-overview/grammars/l1-v1.json`；`machine-overview/profiles/l1-partiality-v0.json`；KC-000031 | 覆盖问题仍未决。 |
| `KC-000032` | `Codex` / 悖论反证理论与稠密性否定所引入的存在性 | `NOT_TOUCHED` | 未处理存在/不存在双视角的对象层构造。 | KC-000032 | 不变。 |
| `KC-000033` | `Codex` / Russell悖论对无时序不存在性前提的攻击 | `NOT_TOUCHED` | 未处理 Russell 形成模型。 | KC-000033 | 不变。 |
| `KC-000034` | `Codex` / 否定性存在与不存在的现实相对双视角 | `NOT_TOUCHED` | 未把双视角做成对象。 | KC-000034 | 不变。 |
| `KC-000035` | `Codex` / HoTT能否完整表达用户悖论研究理论 | `TENSION` | 本轮把「表达/覆盖」问题工程化为 declared bounds；这既没有回答该问题，也再次显示任何局部仪器都只能覆盖极小片段。张力保留，不用文档化冒充回答。 | `machine-overview/README.md`；KC-000035 | 表达/覆盖义务仍开放。 |
| `KC-000036` | `Codex` / HoTT研究哥德尔不完备性时的循环与自馈风险 | `NOT_TOUCHED` | 未研究 Gödel/自馈。 | KC-000036 | 不变。 |

## 四件套交叉与更新归属

- core_change: `NO`
- direction_change: `PROPOSED_ONLY`（机器统观系统目前只存在于本 worktree 分支；未写入主线的 `方向追踪.md`/STATE）
- panorama_change: `NO_NEW_MATHEMATICAL_RESULT`（三族校准实例已被 C-73–C-75 覆盖；探索收据不进入主张矩阵）
- essay_change: `NO`
- update_decision: `WORKTREE_LOCAL_DELIVERABLE`；主线 STATE/投影/checkpoint 的写入属于方案 M5 集成步骤，需另行授权
- cross_conflicts: 未发现四件套内部冲突；需要登记的外部关系是：本方案文档位于 repo 外且尚未登记为项目方向
- unresolved: M2–M5 未实现；cvc5/Alloy/egg 等后端未安装；`capture_agda_proof_run.py` 的 `.git` 必须为目录检查使 canonical 捕获无法直接在普通 worktree 运行；主线集成与 canonical checkpoint 未执行
