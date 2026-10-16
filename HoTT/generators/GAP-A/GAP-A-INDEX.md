# GAP-A 缺口闭合索引

> ⚠️ 本索引是**缺口闭合单元索引**，不是数学结论索引，也不是生成器族索引。
> 本单元 `registers_new_claim: false`，**不进入** `HoTT/CLAIM_EVIDENCE_MATRIX.md`。
> 唯一登记的否定性机械事实 = 「布尔律 `x ∧ ¬x = 0` 对 V2 三个结构性分离不是必需的」，
> 作用域 = `formal/V2DM3.agda` 定义的 DM3，不提升到所有 De Morgan 代数，不提升到区间 `I`。

## 索引行

| unit_id | task_family | 关联缺口 | grammar | search_run | verify_runs | 越界证明 | 判词 |
|---|---|---|---|---|---|---|---|
| `GAP-A-DM3` | TASK-FAMILY-GAP-A-INTERVAL-ORACLE-DE-MORGAN | 修订片 018 §3(A)：区间 I 的 oracle 不存在（点集模型携带布尔律而 I 不携带） | `V2-DM3-A-v1`（backend `v2-dm3`；DM3 = 三元非布尔 De Morgan 链 `0<a<1`，`~a=a`） | `SEARCH-GAP-A-DM3-001` | `VERIFY-GAP-A-DM3-WV-{0230,0041,0158,0001}` + `VERIFY-GAP-A-DM3-BLI-001` | `GAP-A-DM3-OUT-OF-ENVELOPE.json`（392/392 作用域内见证被 8 个既有文法全拒，族内拒因唯一；4 条 level-ingress 如实登记） | `DM3_DE_MORGAN_CONFIRMED_NON_BOOLEAN_LIFT`（`interval_i_confirmed=false`；`boolean_law_needed=false` kernel-confirmed） |

## 证据定位

- 冻结文法与代数声明：`GAP-A-DM3-GRAMMAR.json`
- 分母、枚举、remainder=0、归约、校准、非嵌入：`GAP-A-DM3-ENUMERATION.json`
- 越界机械证明（含 ingress 与作用域边界）：`GAP-A-DM3-OUT-OF-ENVELOPE.json`
- 验收报告（判词升级语义 + 强制披露 + 审计链）：`GAP-A-DM3-REPORT.md`
- 引擎内完整收据：`/Volumes/D/HoTT-machine-overview/machine-overview/runs/`
  （分支 `feat/machine-overview-m1`，commit `776e6b7`；RUN.json + kernel 四路五件套
  + 生成 Agda 源码 + source-manifest + witness-manifest）

## 与 GEN-001 的关系

- 本单元**不是** `GEN-001` 的一个验收单元：GEN-001 验收"有界生成器链贯通"，
  本单元闭合的是 GEN-001-V2-1 判词中**登记的缺口**（模型层 vs 结论证据）。
- 本单元把 V2-1 的 4 个 kernel 见证声明
  `POINT_SET_MIRROR_MODEL_KERNEL_CONFIRMED` 中的 availability / level / density
  三个机制升级为 `DM3_DE_MORGAN_CONFIRMED_NON_BOOLEAN_LIFT`（解释无关性 + 布尔律非必需）；
  **区间 I 分支仍开放**，V2-1 的 density 见证（`FACE_LATTICE_ORDER` 依赖类）
  仍**不得**作为关于区间 I 的结论证据。

## 禁止外推

- 不声称任何分离在真实区间 `I` 上成立（`I` 的相等不可判定；DM3 是模型，不是 `I`）。
- 不声称布尔律非必需这一事实对所有 De Morgan 代数成立（作用域 = DM3）。
- 不声称 D-04 / G-05 等前提的非现实判定成立（仍 `AI_ADJUDICATED_PENDING_EXTERNAL_AUDIT`）。
- 不声称引擎具备自主发现能力（任务族、文法、DM3 解释均由 AI 冻结供给，003 §5 角色纪律）。
- 不声称越界检查覆盖全部既有文法（12 个 symbolic-horn 文法为 schema 级
  `BACKEND_MISMATCH`，未跑机械检查；缺口 B 未闭合）。
