# 外部 AI 工作吸收：验证事件与时标边界（独立核验与项目内重放）

> 会话：`S-GOV-20260913-098-EXTERNAL-WORK-IMPORT`
> 来源：另一 AI 会话 `01a099e9-66ee-7270-8bf9-04f7f1c81e62`（由用户交接）；交接说明与原件见
> `audit/imports/verification-event-20260913-01a099e9/`
> 结果：本 repo 内形成唯一 owner 源码 + 项目 canonical run + 8 条矩阵 claim；负向校准与失败史全部保留

## 1. 交接说明要求与实际处置对照

| 交接说明要求 | 实际处置 |
|---|---|
| 先保全原件，不改字节 | `original-package/`（170 文件 / 1,171,988 B / 整树 `56376a96…`）、`relocated-replay/`（192 文件 / 整树 `f05422f9…`）、两份外部文档均按原字节入 repo；`IMPORT.json` 记录来源与哈希 |
| 独立只读核验（§9 脚本） | 逐项复现：整树哈希、9 个外部 run 的 stdout/stderr/源码快照/依赖哈希、`attempt-003` 与 `positive-final-001` 输出逐字节相同、`negative-002` exit 42 且 `expectation_met=true`（诊断 `[UnequalTerms]` / `afterP != initial`） |
| 主源码成为当前 owner | `HoTT/formal/verification-event/VerificationEvent.agda`（`04f18440…`，与原件逐字节相同）+ `TOOLCHAIN.json` + `AGDA_LIBRARIES` |
| 负向源隔离 | `HoTT/formal/verification-event/negative/BadCast.agda`（`1e84149…`），不纳入正向构建 |
| 项目内新 run（真实执行） | `capture_agda_proof_run.py` → `HoTT/verification/runs/20260913-MP-VERIFICATION-EVENT-001-01/`：exit 0、stderr 0、`KERNEL_ACCEPTED_WITH_SCOPE`、`INDEXED_IN_CLAIM_EVIDENCE_MATRIX`、`EXACT_INDEX_SNAPSHOT_MATCH`；`verify_formal_proof_run.py --rerun` → `EXACT_EXIT_STDOUT_STDERR_MATCH` |
| 负向控制"核对到指定错误" | 项目探针 `project-negative-probe/`（冻结命令 + 原始 stdout/stderr/exit）：exit 42、`BadCast.agda:10`、`afterP != initial`；外部 `negative-002` 保留为首选外部负向收据 |
| 唯一数学索引 | `HoTT/CLAIM_EVIDENCE_MATRIX.md` 新增包行 `MP-VERIFICATION-EVENT-001` 与 `C-149`–`C-156`；本地 ID 对照 `EVT-01`–`EVT-08` 写在行内 |
| 版本维度 | `HoTT/verification/PROOF_VERSION_CLOSURE.json` 的 **追加式** `later_packages` 登记本包（历史 17 包冻结收据不改写），verifier 增加"tracked + run INDEXED + exit 0"检查 |

## 2. 判词与范围

> 固定有限验证事件模型内，保留时标的历史核查可完成；把固定过去改成当前的转换不成立，完全阶段擦除不保留相关真值判断。
> 原生 Cubical Agda 核查通过。**该最小候选未构成 HoTT 自身非现实性实例。**

模型：`Stage = initial/afterP/afterHistory`；`Step = issueP/recordHistory`；`Claim = atom/historical/current`；`Registered` 三项明示登记；`P = Unit`；
`K(s,c) = Trunc (Registered s c)`（源码定义的原生高阶归纳命题截断）；`Historical` 固定引用 `initial`。证明只用 Agda 内建 Cubical 原语，未调用 univalence、未导入 `Cubical.*`（Cubical 库仅由共享 capture 命令载入）。

claim 对照：`EVT-01→C-149`（事件链）、`EVT-02→C-150`（有限登记健全）、`EVT-03→C-151`（Current 分布与判定器）、`EVT-04→C-152`（后来可核查固定过去）、`EVT-05→C-153`（过去→当前改写不存在 + BadCast 校准）、`EVT-06→C-154`（完全阶段擦除不保真）、`EVT-07→C-155`（保阶段正控制）、`EVT-08→C-156`（显式 factivity/合取消去参数下的 Moore/Fitch 条件核）。

## 3. 必须与结果同时保留的失败/负结论

1. **候选未达目标**：这条"让尚未验证进入待验证内容"的最短路线在该最小版本下没有成为所需的 HoTT BUG；失败位置是 `BadCast.agda:10` 的 `afterP != initial`（`[UnequalTerms]`）。
2. **环境失败史**：外部包 9 个 run 中 `attempt-001`、`smoke-001`、`smoke-002` 为 exit 154 的隔离运行数据启动失败（复制本机既有内建接口缓存后恢复，`smoke-003` exit 0）；失败的源码快照与缓存备份保留。**不把启动异常宣称为 HoTT 理论错误或已完整诊断的 Agda 缺陷。**
3. **异目录重放是同宿主**：`handoff-positive-001` / `handoff-negative-001` 只证明"不依赖作者原目录"，不是跨机器/跨操作系统结论；路径改变使 stdout 绝对文件名不同，不声称字节相同。
4. **schema 不冒充**：外部 run 使用 `isolated-agda-run/v1`；项目收据使用 `formal-proof-run/v1`，由本轮真实运行产生，未改写外部收据。

## 4. 已存在的四个早期文档 Session

`S-AUD-20260913-KC15-01a099e9`、`S-REV-20260913-WORKLINE-01a099e9`、`S-DOC-20260913-CORE-ESSAY-01a099e9`、`S-DOC-20260913-TIME-ORDER-01a099e9` 已在 repo（commit `4022206`）中，本轮**只登记历史身份**：

- 它们没有 canonical checkpoint 收据，因此保持 `LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED`/历史身份，**不倒填**本轮事务日期；
- 综合文章与 core 的关系不变：文章是用户原意的 AI 阐释，不进入 `核心认知.md`，36 段原文的 owner 仍是 core + manifest。

## 5. 残余未知

- 候选文档中更一般的证书规格仍未实现（保持 PAPER_ONLY 历史提案身份）；
- 本包不证明"HoTT 的所有时间/时序问题"；用户已澄清时序≠时间/运动结构，本实验属时序线；
- fresh model behavior `NOT_RUN`（结构与内核层已验证，模型行为需真实 Session 观察）；
- 外部原件中的绝对路径与缓存属于历史现场，不为了"好看"改写。
