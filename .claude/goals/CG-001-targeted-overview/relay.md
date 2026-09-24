# CG-001 relay 清单

> 状态：**CANDIDATE_NOT_CURRENT**。以下是本目标产生、需要研究 integrator（当前为 Codex Session C）或用户决定是否登记到共享 owner 的内容。本目标没有写入 STATE、MEMORY、方向追踪、全景视野、核心认知、`HoTT/CLAIM_EVIDENCE_MATRIX.md` 或任何 Session 目录。
>
> 登记前请独立核对：源码与 run 的哈希、`verification/` 下的校验输出，以及工作台 §4 的候选卡与判词。登记与否不影响本目标的完成判定。

## R1 共享矩阵行草稿（`HoTT/CLAIM_EVIDENCE_MATRIX.md`）

若登记，请由 integrator 按矩阵现行格式写入，并在 run 的 `RUN.json` 之外另建 index-row manifest（本目标不改 RUN.json）。草稿如下：

| proof ID | claims | 源码 | run | 状态草稿 |
|---|---|---|---|---|
| `MP-CG001-MOTION-MEASUREMENT-001` | `CG001-C-01`–`CG001-C-07` | `formal/claude-cg001/motion-measurement/MotionMeasurement.agda`（命题全文 `CLAIM.md`） | `verification/runs/20260924-CG001-MOTION-MEASUREMENT-01/`；Agda 2.8.0-3d04bac / cubical 0.9，`--safe --cubical --guardedness`，exit 0，stderr 0 B；目标内校验精确重放一致 | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEX_ONLY`（待登记） |
| `MP-CG001-MOTION-MEASUREMENT-NEG-001` | `CG001-C-03`（负控制） | `formal/claude-cg001/motion-measurement/WrongVaryingReading.agda` | `verification/runs/20260924-CG001-MOTION-MEASUREMENT-NEG-01/`；exit 42，`UnequalTerms 1 != 0 of type ℕ` | `KERNEL_REJECTED_AS_EXPECTED` |
| `MP-CG001-MEASUREMENT-LOG-001` | `CG001-C-08` | `formal/claude-cg001/measurement-log/MeasurementLog.agda`（命题全文 `CLAIM.md`） | `verification/runs/20260924-CG001-MEASUREMENT-LOG-02/`；exit 0，stderr 0 B；目标内精确重放一致。`…-01` 作废（目标内校验器附加标记命中注释，见 `verification/20260924-CG001-MEASUREMENT-LOG-01.NOTE.md`），不应登记 | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEX_ONLY`（待登记） |
| `MP-CG001-LEVEL-COMPARISON-001` | `CG001-C-09` | `formal/claude-cg001/level-comparison/LevelComparison.agda`（命题全文 `CLAIM.md`） | `verification/runs/20260924-CG001-LEVEL-COMPARISON-01/`；exit 0，stderr 0 B；目标内精确重放一致 | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEX_ONLY`（待登记） |

各 claim 的一句话与禁止外推见各包的 `CLAIM.md`（`HoTT/formal/claude-cg001/` 下的 motion-measurement、measurement-log、level-comparison）与本目录 `证据索引.md` §3。

## R2 方向与全景的候选条目（供 integrator 判断）

| 候选 | 建议去向 | 内容 | 证据 |
|---|---|---|---|
| A1 沿运动测量 | 方向追踪（新方向或挂在 DIR-U-A-REALITY-RELATIVE 下）；全景视野（新结果行） | 在“运动 = 恒等路径”这一 HoTT 读法下，任何取值于集合的仪表沿运动不变；现实中从冷镇到暖镇温度计会变。判词 QUALIFIED_HIT（有范围）。与 Astra C-251、C-264（去点）同一连通性事实，差量是新过程（沿运动测量）与一般定理 C-01(v)、依赖出路 C-06 | 工作台 §4.1；run `20260924-CG001-MOTION-MEASUREMENT-01` |
| C1 实数的测量记录 | 全景视野（结果行，与 W10 同族的差量） | Book HIIT 实数：真实的有限测量记录在 HoTT 中可得（有限选择）；无穷记录需要 AC_ω（关键否定方向为猜想；书 L937 “may not be”）。判词 REFUTED（有限任务）/ BOUNDARY（无穷记录）。观察：HoTT 基础部分给潜无穷、不给实无穷，与用户的有限测量前提同向 | 工作台 §4.2；run `20260924-CG001-MEASUREMENT-LOG-02` |
| I1 逐层一致推不出整体相同 | 全景视野（结果行） | 截断 Whitehead 与球面截面引理机器检查；有限 CW 复形只需有限层（AI 推导，猜想）；任意类型的 Whitehead 原则不可证（来源报告）是对非超完备模型的正确拒绝。判词 REFUTED（有限任务）/ BOUNDARY（无穷维理想比较） | 工作台 §4.3；run `20260924-CG001-LEVEL-COMPARISON-01` |

## R3 需要用户或 integrator 决定的问题

1. A1 的判词依赖一个解释立场：“Think in HoTT”指使用 HoTT 的合成读法（路径即运动）；按 GOAL (e)，“同成本”以保留合成经济 E 为基准。若审计认为 Book intro L85–91 的“purely homotopically”声明使这一读法不成立，A1 应降为 STRONG_CANDIDATE 或 BOUNDARY（已宣告范围）。
2. 是否把 `.claude/goals/CG-001-targeted-overview/tools/verify_cg001_run.py`（复用规范校验器、只替换索引检查）的做法吸收进项目治理，或改为由 integrator 登记后用规范校验器重验。
3. 目标内校验器比规范校验器多一条子串标记 `postulate`，会命中注释（run `20260924-CG001-MEASUREMENT-LOG-01` 因此作废）。若吸收这个校验器，建议改为只扫描非注释代码，或者保留现状、要求注释回避该词。本目标没有在失败后放宽它。
4. I1 的有限 CW 版本（k ≥ max(dim A, dim B − 1) 的 k-连通映射是等价）目前是 AI 推导的猜想，只有填胞腔一步机器检查。是否值得用 `Cubical.CW.*` 整体形式化，由 integrator 或用户决定。
