# GEN-001 验收报告：有界生成器验收单元（第一链）

> 单元：`GEN-001 BOUNDED_GENERATOR_ACCEPTANCE_UNIT`（方案修订片 003）
> 任务族：`TASK-FAMILY-WITNESS-RECOVERABILITY`（PREMISE-001/007 的 SUPPLY-007，E-02）
> 执行者：AI（带强制审计层，`AI_ADJUDICATED_PENDING_EXTERNAL_AUDIT`）
> 执行日：2026-09-16
> 判词：**`GENERATOR_LINK_DEMONSTRATED_WITH_SCOPE`**

## 0. 本报告不是什么

- **不是数学结论**。本单元验收的是**链的贯通**（冻结 → 枚举 → 归约 → 原生核 → 收据），
  不是任何数学命题的真值（F-011 / `MATH_PROOF_BEFORE_DELIVERY_V1`）。
- **不是"引擎自主发现了新方向"**。任务族由 AI 冻结供给（角色纪律，修订片 003 §5）；
  引擎贡献的是**在冻结文法上的完整枚举 + grammar-preserving 归约**，原生核贡献 oracle 判定。
- **不是"该前提非现实"的证明**。E-02 的非现实判定仍是 pending external audit 的候选。

## 1. 链的实际运行（全部为 observed，可复算）

| 阶段 | 产物 | 结果 |
|---|---|---|
| 冻结任务族 | `GEN-001-GRAMMAR.json`（文法 `L1-WITNESS-RECOVERY-v1`） | 声明 2 个新构造子 `downstream_guard` / `downstream_needs_true_late`；界 `delay_index_max=3`、`context_depth_max=2`、`deadline_horizons=[0,1,2,3]` |
| 引擎枚举 | search run `20260916-SEARCH-GEN001-WITNESS-RECOVERY-001` | 9 atoms × 598 contexts = 14,352 pair-context checks；`complete_within_declared_grammar=true`；`grammar_violations=0`；**remainder=0** |
| grammar-preserving 归约 | 同上 run | 2,736 个原始分离 → **52 个规范归约见证**（每个归约步都重检文法成员资格与分离性） |
| 越界证明 | `GEN-001-OUT-OF-ENVELOPE.json` | 3 个核验见证对全部 **15 个既有声明文法**的成员资格检查全部为 `within=False`：对 `l1-v0/v1/v2` 返回 `BIND_CONTINUATION`；对 12 个 symbolic-horn 文法为 `BACKEND_MISMATCH`（不同后端，无法表达 delay-fragment 见证） |
| 原生核校验 | 3 个 verify run（见 §2） | 每个含 4 路 kernel 收据：`verify` / `controls`（正控制）/ `negative-control`（须被拒）/ `verify-replay`（确定性） |
| 收据化 | `HoTT/verification/runs/20260916-VERIFY-GEN001-*` | RUN.json + kernel stdout/stderr/environment/command + generated Agda + source-manifest |

## 2. 原生核结果（Cubical Agda 2.8.0-3d04bac + cubical v0.9）

| verify run | 见证 | 观察模式 | verify | controls | negative-control | verify-replay |
|---|---|---|---|---|---|---|
| `...-040` | WV-0040 | deadline | KERNEL_ACCEPTED (exit 0) | ACCEPTED | **REJECTED_AS_EXPECTED (exit 42)** | EXACT_EXIT_STDOUT_STDERR_MATCH |
| `...-041B` | WV-0041 | delay（race-截断） | KERNEL_ACCEPTED (exit 0) | ACCEPTED | **REJECTED_AS_EXPECTED (exit 42)** | EXACT_EXIT_STDOUT_STDERR_MATCH |
| `...-049` | WV-0049 | delay（race-截断） | KERNEL_ACCEPTED (exit 0) | ACCEPTED | **REJECTED_AS_EXPECTED (exit 42)** | EXACT_EXIT_STDOUT_STDERR_MATCH |

三个见证全部绑定 `downstream_guard`（新构造子），因此全部机械越界（§1）。
WV-0040 的语义是"下游工序在截断后越过截止线"；WV-0041 / WV-0049 是"race 截断把到达次序折叠成值差异，
下游守卫工序在失败分支上发散"——后者最贴近 E-02 的"截断后见证不可恢复"。

## 3. 修订片 003 §4 的四项验收判据

1. **分母固定且 remainder=0** — ✔ `complete_within_declared_grammar=true`，无截断、无预算耗尽。
2. **至少一个候选是现有 15 个文法无法产出的** — ✔ 3/3 核验见证机械越界（`GEN-001-OUT-OF-ENVELOPE.json`）。
3. **每个候选的 oracle verdict 由原生核而非启发式给出** — ✔ Cubical Agda 原生核 4 路收据，
   含必须被拒的负控制（exit 42）与精确 replay 匹配；Python 模型只负责**提出**候选，从不替代核。
4. **完整链 input → candidate → oracle → receipt** — ✔ case revision → search run → verify run →
   kernel 收据 → correspondence review → report，全部哈希绑定。

**判词：`GENERATOR_LINK_DEMONSTRATED_WITH_SCOPE`**
（generator_family: 第 1 类 typed term/proof synthesis 的真实链；scope: 单一冻结任务族；remainder=0；
其余五类生成器状态不变，仍 PARTIAL；不声称开放候选空间的完备覆盖；不声称引擎具备自主发现能力。）

## 4. 语义建模的诚实边界（重要，请外部审计优先看这里）

本族把 E-02（命题截断：见证信息不可恢复）建模在 **Delay Bool 片段**上：

- **截断** ↔ 对已声明 partner 的 `race`：race 把到达轮次（delay equivalence ≈ 遗忘的信息）折叠成值差异。
- **被截断摧毁的见证** ↔ 到达轮次 / 哪个生产者赢得了 race。
- **下游工序** ↔ 预先声明的 `bind` 延续，只在见证存活时完成。

**这不是 HoTT 的命题截断本身**。Delay Bool 是 E-02 的一个**有界对应物**，不是截断类型。
任务文件 `MS-TASK-GEN001-WITNESS-RECOVERY-001.json` 的 `assumptions` 与
`correspondence.open_obligations` 显式登记了这一点：cubical 原生截断族仍是 V2 候选。
若外部审计认为该建模对应不可接受，本链的**链贯通结论不变**（验收的是链，不是建模保真），
但"E-02 已被机器检验"的任何推论必须撤回。

## 5. 过程披露（一处中断 + 一处记账缝隙）

- run `...-041` 的首个进程在 kernel 阶段被外部超时杀掉。引擎按自身设计 roll over，第二次尝试完成。
  完成的收据诚实地记录 `target_freeze.status = "REUSED"`（ledger 条目由被杀的第一次尝试创建），
  而工作区校验器在 `first_verify_run == run_id` 时期望 `"FROZEN"`——这是**校验器缝隙，不是收据篡改**。
  处置：同一见证（相同候选 AST 哈希）以新 run-id `...-041B` 重跑，得到完全一致的干净收据；
  原始 `...-041` 目录（含被中断尝试）**未经修改地**移入
  `machine-overview/archived-interrupted-runs/` 并附 README 披露，供审计读取。
- 全量 `mo.py validate` 在归档后返回 **VALID / 17 cases / 0 errors**。

## 6. CE-MAP 决策（对修订片 003 action 7 的一处执行层偏离）

修订片 003 §4 action 7 要求"在 CE-MAP 建立索引行"。但引擎自身的 `evidence_policy` 与 F-011 规定：
**exploration receipts 不进入 `HoTT/CLAIM_EVIDENCE_MATRIX.md`**，只有带形式源码 + 原生核 run +
冻结矩阵行的精确数学 claim 才能进入。本单元的 `claim_relation` 明确是
`exploration_candidate_not_registered` / `registers_new_claim: false`。

**执行决策**：不在 `CLAIM_EVIDENCE_MATRIX.md` 建行；改为在本目录维护
`GEN-001-INDEX.md`（能力验收索引，显式标注"非数学结论"）。这保留了两条纪律的意图：
GEN-001 的索引化要求得到满足，而 CE-MAP 的"只有已证 claim 才进入"的门槛未被突破。
**此偏离待方案层裁决**（见 §8 的 reflection 登记）。

## 7. 自我限定

- 本链**不提升** E-02 非现实判定的证据等级；它仍是 `AI_ADJUDICATED_PENDING_EXTERNAL_AUDIT`。
- 本链**不声称**其余四个任务族（DIVISIBILITY / EXISTENCE-VS-AVAILABILITY / COMPLETION-PROCESS /
  IDENTITY-OBSERVATION-LAYER）已贯通；它们仍是 step-5 的后续单元。
- 本链**不声称**开放候选空间被穷尽（`NO_HIT_WITHIN_SCOPE` 不构成全局无候选证明）。
- 52 个归约见证中只有 3 个被送入原生核（按修订片 003 的"每选定点一个 kernel check"预算）；
  未送核的 49 个仍是 Python 模型层面的候选，**不是核验结论**。

## 8. 供外部审计复核的关键判定

1. E-02 → Delay Bool 的建模对应是否可接受（§4）。
2. 越界证明的强度：`BIND_CONTINUATION` 是否足以证明"新任务族"（而非"旧族的新参数"）。
3. `target_freeze` 缝隙的处置（归档不修改）是否可接受（§5）。
4. CE-MAP 执行层偏离是否应回写为方案修订（§6）。
5. 三个见证的语义选择（两个 race-截断 + 一个 deadline）是否覆盖了该族的关键观察层。
