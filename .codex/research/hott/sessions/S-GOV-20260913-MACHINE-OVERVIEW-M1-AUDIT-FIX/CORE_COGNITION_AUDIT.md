# 核心认知逐编号回评：S-GOV-20260913-MACHINE-OVERVIEW-M1-AUDIT-FIX

> generation：`core-cognition-generation-4`；KC 总数：`36`；本单元独立复现并修复外部 M1 审计的 F1–F7，重跑三族校准与全部回归；不产生新的数学结论，探索收据仍只留在 `machine-overview/runs/`。

| KC | 来源/语义标签 | 与本轮关系 | 本轮评估 | 证据定位 | 未决 |
|---|---|---|---|---|---|
| `KC-000001` | `LocalGPT` / HoTT悖论研究三问 | `ALIGNED` | 找什么（TaskSpec 冻结）、怎么找（文法内完整枚举）、凭什么（绑定到 case revision 的搜索/见证/目标 + 原生内核）现在在每次消费入口重新核验，而不是只声明一次。 | `machine-overview/AUDIT-RESPONSE-20260913.md`；`machine-overview/machine_overview/case.py`；KC-000001 | 只覆盖 L1 校准片段。 |
| `KC-000002` | `LocalGPT` / Theory Schema先行 | `CORRECTED` | 审计 F1 证明「符号仍在固定行号」不能代替源码字节身份；资格判定现在把源码哈希 FAIL 计入失败，并把 support 模块纳入 profile v1。 | `machine-overview/machine_overview/profile.py`；`machine-overview/profiles/l1-partiality-v1.json`；KC-000002 | 全 Schema 覆盖仍未做。 |
| `KC-000003` | `LocalGPT` / 合取前提与稠密过程 | `NOT_TOUCHED` | 稠密性/运动结构仍不在本 fragment。 | KC-000003 | L3 待独立研究线。 |
| `KC-000004` | `LocalGPT` / 悖论作为反证与运动前提 | `NOT_TOUCHED` | 未处理运动前提。 | KC-000004 | 不变。 |
| `KC-000005` | `LocalGPT` / 先找悖论后作最终归因 | `ALIGNED` | 修复后仍是先产生候选，再以结构驱动的方式写对应说明；现实桥梁保持 `UNRESOLVED`。 | `machine-overview/reviews/RV-*-r3-*-WV-0002-*.json`；KC-000005 | 不变。 |
| `KC-000006` | `LocalGPT` / 时间机制不能收窄为稠密性 | `ALIGNED` | 时序/完成面与结构面继续分开；profile 仍显式把 L3 列为 unsupported。 | `machine-overview/profiles/l1-partiality-v1.json`；KC-000006 | 运动结构未研究。 |
| `KC-000007` | `WebGPT` / LLM内在知识与模式匹配 | `ALIGNED` | 搜索仍由确定性有类型枚举完成；LLM 提议路径未接入。 | `machine-overview/machine_overview/search.py`；KC-000007 | LLM 模块未运行。 |
| `KC-000008` | `WebGPT` / 历史时间悖论作为HoTT启发 | `ALIGNED` | R041/C-73–C-74 仍只用于搜索后的基准比对（`calibration_match=PRESENT`）。 | `machine-overview/runs/20260913-SEARCH-L1-003/RUN.json`；KC-000008 | 不变。 |
| `KC-000009` | `WebGPT` / 定位HoTT理论设定的时间维度 | `ALIGNED` | 位置仍被固定到 `ret n a` 的 round index 与具体消费者；F4 修复后机制描述与实际 AST 一致。 | `machine-overview/machine_overview/correspondence.py`；KC-000009 | 仅模型层定位。 |
| `KC-000010` | `WebGPT` / 目标是现实相对非现实性而非内部矛盾 | `ALIGNED` | 修复没有把工具缺陷或内核通过升格成理论结论；判词仍停在表示/消费者层。 | `machine-overview/AUDIT-RESPONSE-20260913.md`；KC-000010 | 现实相对目标未主张。 |
| `KC-000011` | `WebGPT` / 理论推演排除时序与程序显式时序 | `DEEPENED` | F2 给出一个新的一般教训：内核接受的是「交给它的公式」，公式是否属于当前任务与版本必须由协调器单独绑定；这正是时序/身份在工具层的责任，而非公式自身的性质。 | `machine-overview/machine_overview/verify.py`；KC-000011 | 仍只是已有 C-73–C-75 机制的校准实例。 |
| `KC-000012` | `WebGPT` / ASK计算合法性预分析 | `CORRECTED` | ASK 的「先问合法性」在工具层落实为：每次消费前重新哈希冻结输入并核对见证归属；只在创建时声明不够（F1/F2）。 | `machine-overview/machine_overview/case.py`；`machine-overview/tests/test_audit_regressions.py`；KC-000012 | 不变。 |
| `KC-000013` | `WebGPT` / ASK深化与理论工具性异化 | `ALIGNED` | 补偿类别与机制说明现在从 AST/观察生成；deadline 行明确写作「读取构造子已携带的 n」，不再暗示从商恢复。 | `machine-overview/machine_overview/correspondence.py`；KC-000013 | 账本语义仍为 PAPER_ONLY。 |
| `KC-000014` | `Gemini` / 双向目标的第二方向 | `NOT_TOUCHED` | 未构造 B 方向任务。 | KC-000014 | B 方向未建。 |
| `KC-000015` | `Gemini` / 抽象即否定现实前提与Z铁律 | `NOT_TOUCHED` | 未裁决 Z 铁律。 | KC-000015 | 不变。 |
| `KC-000016` | `Gemini` / Russell的构造过程与计算合法性 | `ALIGNED` | F7 的修复把「正确的类型拒绝」与「基础设施失败」「意外诊断」分开：负控制必须出现 Falsify 模块的类型错误，否则不记成功。 | `machine-overview/machine_overview/verify.py`；KC-000016 | 未做真实内核崩溃实验。 |
| `KC-000017` | `Gemini` / 训练先验批判与Thinking in my math philosophy | `ALIGNED` | 失败不被删除：审计前的 7 个旧 run 加 `LEGACY.json` 保留并可校验；中断尝试 rollover 保存；修复过程本身留档。 | `machine-overview/runs/*/LEGACY.json`；`machine-overview/AUDIT-RESPONSE-20260913.md`；KC-000017 | 不变。 |
| `KC-000018` | `Gemini` / Z铁律的理论工具性与时间否定 | `ALIGNED` | 「身份/来源」在后续责任中被重新检查：输入哈希、见证 AST、目标冻结、运行收据形成闭环。 | `machine-overview/machine_overview/verify.py`；KC-000018 | 不外推为普遍规律。 |
| `KC-000019` | `Gemini` / 合取真值与稠密空间中的完成困难 | `NOT_TOUCHED` | 未处理稠密空间完成困难。 | KC-000019 | 不变。 |
| `KC-000020` | `Gemini` / 悖论反证、运动量子化与HoTT时间怀疑 | `NOT_TOUCHED` | 未处理物理判断。 | KC-000020 | 不变。 |
| `KC-000021` | `Gemini` / 机器证明与真实运行要求 | `DEEPENED` | 三族 post-fix 原生运行 + 正负控制 + 重放；新增内部超时/进程组终止、artifact 哈希校验与重放分级（区分冷/暖缓存日志差异与命题被拒）。 | `machine-overview/runs/20260913-VERIFY-L1-POSTFIX-*/RUN.json`；KC-000021 | 非新增 F-011 claim。 |
| `KC-000022` | `Gemini` / 两类现实相对悖论 | `ALIGNED` | 修复只涉及工具正确性；两方向仍都未主张成立。 | KC-000022 | 两类都未主张。 |
| `KC-000023` | `Gemini` / 时间时序处理应可直接定位 | `ALIGNED` | 七组缺陷都定位到具体文件/行为/复现；修复后每个见证仍给出精确 (pair, context, observation) 与 AST 哈希。 | `machine-overview/AUDIT-RESPONSE-20260913.md`；KC-000023 | 不变。 |
| `KC-000024` | `Gemini` / 两类时序悖论与HoTT搜索问题 | `CORRECTED` | F6 修复把「预算耗尽」与「范围穷尽」分开：`complete_within_declared_grammar` 必须同时满足无预算停止、无捕获截断与全遍历。 | `machine-overview/machine_overview/search.py`；KC-000024 | 有界运行不证明普遍结论。 |
| `KC-000025` | `Gemini` / 自指型悖论为何难找 | `NOT_TOUCHED` | 未处理自指。 | KC-000025 | 不变。 |
| `KC-000026` | `Gemini` / HoTT自身自指不可越过 | `NOT_TOUCHED` | 未构造自指实例。 | KC-000026 | 不变。 |
| `KC-000027` | `WebGPT` / HoTT对齐程序后继承程序自反界限 | `ALIGNED` | 校准器明确承担两类独立检查：内核命题有效性与命题对任务的忠实性；两者不可互相代替。 | `machine-overview/AUDIT-RESPONSE-20260913.md`；KC-000027 | 仍非 HoTT 独有发现。 |
| `KC-000028` | `Codex` / HoTT自反真理验证的不可停机与自馈回环怀疑 | `NOT_TOUCHED` | 未研究自馈回环。 | KC-000028 | 不变。 |
| `KC-000029` | `Codex` / 理论经济收益作为自馈回环的高风险位置 | `DEEPENED` | 审计证明自动化的经济收益依赖不可省略的义务（输入重核、身份绑定、证据重算）；省略这些义务就等于把「已验证」变成了不可信的默认值。 | `machine-overview/machine_overview/case.py`；KC-000029 | 账本仍 PAPER_ONLY。 |
| `KC-000030` | `Codex` / 历史理论经济认知完整性与HoTT经济学之问 | `ALIGNED` | 补偿动作三类仍逐例登记；F4 后类别的判定来自实际 ops（deadline=读取已声明表示；business continuation=任务预先保留；纯 race=消费者读取完成顺序）。 | `machine-overview/reviews/RV-*-r3-*.json`；KC-000030 | 逐行任务生成仍未完成。 |
| `KC-000031` | `Codex` / HoTT严格范型可能拒绝最小理想理论的构造方向 | `ALIGNED` | 声明范围现在是硬约束：缩减必须留在文法内，越界直接 `REDUCTION_LEFT_DECLARED_GRAMMAR`；完整性字段不再把截断说成穷尽。 | `machine-overview/machine_overview/search.py`；KC-000031 | 覆盖问题仍未决。 |
| `KC-000032` | `Codex` / 悖论反证理论与稠密性否定所引入的存在性 | `NOT_TOUCHED` | 未处理存在/不存在双视角构造。 | KC-000032 | 不变。 |
| `KC-000033` | `Codex` / Russell悖论对无时序不存在性前提的攻击 | `NOT_TOUCHED` | 未处理 Russell 形成模型。 | KC-000033 | 不变。 |
| `KC-000034` | `Codex` / 否定性存在与不存在的现实相对双视角 | `ALIGNED` | F4 要求在解释中写清「恢复」的层次：从 `ret n a` 读取 n 属于读取已声明表示，不是从结果商恢复；未核清的补偿类别返回 `UNRESOLVED`。 | `machine-overview/machine_overview/correspondence.py`；KC-000034 | 补偿三分仍未系统化到全部候选。 |
| `KC-000035` | `Codex` / HoTT能否完整表达用户悖论研究理论 | `CORRECTED` | 审计再次证明「AST 有表达式」不等于「研究问题被忠实表达」：新增文法成员资格、绑定检查与结构驱动对应审查，未核清时降为 `REVIEW_REQUIRED`。 | `machine-overview/machine_overview/correspondence.py`；KC-000035 | 表达/覆盖义务仍开放。 |
| `KC-000036` | `Codex` / HoTT研究哥德尔不完备性时的循环与自馈风险 | `NOT_TOUCHED` | 未研究 Gödel/自馈。 | KC-000036 | 不变。 |

## 四件套交叉与更新归属

- core_change: `NO`
- direction_change: `NO`（本轮只修工具正确性，不改变研究方向）
- panorama_change: `NO_NEW_MATHEMATICAL_RESULT`（三族仍为 C-73–C-75 的校准实例）
- essay_change: `NO`
- update_decision: `WORKTREE_LOCAL_FIX`；主线 STATE/投影/checkpoint 仍属 M5 集成，需另行授权
- cross_conflicts: 审计 `REQUEST_CHANGES` 与 v1 交付措辞的冲突已通过修复解决：旧收据 + `LEGACY.json` 保留、新收据带完整绑定；无被隐藏的失败
- unresolved: M2–M5；canonical capture 的 worktree 兼容；两个依赖忽略资产的 verifier；缓存状态未在 profile 中声明；OS 级候选隔离未实现
