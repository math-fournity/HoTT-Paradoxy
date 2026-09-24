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

各 claim 的一句话与禁止外推见 `HoTT/formal/claude-cg001/motion-measurement/CLAIM.md` 与本目录 `证据索引.md` §3。

## R2 方向与全景的候选条目（供 integrator 判断）

| 候选 | 建议去向 | 内容 | 证据 |
|---|---|---|---|
| A1 沿运动测量 | 方向追踪（新方向或挂在 DIR-U-A-REALITY-RELATIVE 下）；全景视野（新结果行） | 在“运动 = 恒等路径”这一 HoTT 读法下，任何取值于集合的仪表沿运动不变；现实中从冷镇到暖镇温度计会变。判词 QUALIFIED_HIT（有范围）。与 Astra C-251、C-264（去点）同一连通性事实，差量是新过程（沿运动测量）与一般定理 C-01(v)、依赖出路 C-06 | 工作台 §4.1；run `20260924-CG001-MOTION-MEASUREMENT-01` |

## R3 需要用户或 integrator 决定的问题

1. A1 的判词依赖一个解释立场：“Think in HoTT”指使用 HoTT 的合成读法（路径即运动）；按 GOAL (e)，“同成本”以保留合成经济 E 为基准。若审计认为 Book intro L85–91 的“purely homotopically”声明使这一读法不成立，A1 应降为 STRONG_CANDIDATE 或 BOUNDARY（已宣告范围）。
2. 是否把 `.claude/goals/CG-001-targeted-overview/tools/verify_cg001_run.py`（复用规范校验器、只替换索引检查）的做法吸收进项目治理，或改为由 integrator 登记后用规范校验器重验。
