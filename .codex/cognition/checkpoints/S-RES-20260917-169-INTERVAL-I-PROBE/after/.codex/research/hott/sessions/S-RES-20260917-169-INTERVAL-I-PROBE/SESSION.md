# S-RES-20260917-169-INTERVAL-I-PROBE

身份：PREMISE-001 step-5 **缺口 A 的区间 I 分支收尾单元（表达界限设计探针）**——
168 裁决序列第 (1) 项「区间 I 设计探针」的执行；修订片 021（步骤产出的方案落盘）；
修订片 020（commit `221936a`）自我审计合同的**第二次执行**。
角色：AI 全自动执行（修订片 009/017）+ 强制审计层；外部 AI 追溯审计为终局复核。
**不邀请用户介入；本项目禁止启动任何 Sub Agent**（用户 2026-09-17 裁定，commit `679a016`）。

## 本单元产出

1. **三路设计探针**（引擎 `36d27e0`，`machine-overview/formal/`）：STATE revision 168
   指引把区间 I 分支设为设计探针问题（「先确定 I 上能写什么」），三路探针在 Cubical Agda
   2.8.0-3d04bac（sha256 `ac285c19…`）+ cubical v0.9 上跑完原生核，与
   `VERIFY-GAP-A-DM3-BLI-001` 完全一致的工具链身份（`environment.txt` 可核）：
   - **`IntervalIForms` = ACCEPT exit 0**：I 上**可写**的分离形态 = (a) I 上类型族 + `PathP`；
     (b) cofibration 条件层——`IsOne i1` / `endpointCases : (r:I) → Partial (r ∨ ~ r) Bool` /
     `endpointFamily` / `meetCases : (r s:I) → Partial (r ∧ s) Type₁` /
     `intervalFamily : I → SSet₂` / `pathOverConstant`。
   - **`IntervalIBoolDiscriminator` = REJECT exit 42**：
     `[SplitError.NotADatatype] Cannot split on argument of non-datatype I`（32.18-20）——
     `I → Bool` 端点观察器（DM3/点集 oracle 的形态，路线 c2）结构性不可写。
   - **`IntervalIEqualityAttempt` = REJECT exit 42**：`[UnequalSorts] IUniv != Type`（16.32-33）——
     `PathP (λ i → I) r s`（路线 c1，可判定等式的前提）连类型都成型不了。
2. **三个 run 目录**（引擎 `36d27e0`，`machine-overview/runs/`）：
   `PROBE-INTERVAL-I-{FORMS,BOOL-DISC,EQ-ATTEMPT}/`，各含 RUN.json（schema
   `machine-overview-probe-interval-i-run/v1`：schema_version / run_id / kind / started_at_utc /
   completed_at_utc / question / answer / status / expectation_met / registers_new_claim /
   design_source / kernels[argv, cwd, exit_code, stdout/stderr sha256, environment, artifacts] /
   toolchain_identity / git_state_engine / git_state_handoff / oracle_scope /
   key_adjudication_audit_trail）+ stdout.txt + stderr.txt + environment.txt + command.json +
   source-manifest.json。三路 `expectation_met=True`；stdout 2,400 / 2,644 / 568 bytes（重跑一致）；
   退出码 0 / 42 / 42。
3. **判词 `INTERVAL_I_SEPARATION_FORMS_FAMILY_AND_COFIBRATION_BOOL_OBSERVER_UNWRITABLE`**，
   `registers_new_claim:false`（F-011 语言片段探针），**不进 `HoTT/CLAIM_EVIDENCE_MATRIX.md`**。
   判词分级：「Bool 观察器不可写」= 关于工具链表达界限的**有界负结论**（作用域固定到
   Cubical Agda 2.8.0 + cubical v0.9；falsifier = 一个被核 ACCEPT 的非恒常 `I → Bool` 或一个
   被核 ACCEPT 的 I 上可判定相等）；「类型族/cofibration 可写」= **正面可写性证据**
   （falsifier = 核 REJECT 其中任一定义）。
4. **EXP-001 收尾**（168 裁决的方向 7 并入本单元）：HoTT 能否保真表达 DM3 分离语义 =
   **能，但承载层改变**——`Partial (φ)` 的「约束下分片定义」≠ `Bool` 的「全局可判定观察」。
   这不是「HoTT 无法表达相关现象」，而是「表达的层不同」。**方法学后果（对下一单元直接
   生效）**：现实对齐断裂的寻找**不应假设**「理论必须以某一固定形态（如可判定观察）携带某个
   语义」。
5. **缺口 A 的区间 I 分支以表达界限正面结论收尾**，而非以一个 I 上的 V2 值解释闭合；
   `interval_i_confirmed = false` 继续保持；V2-DM3 的 availability / level / density 见证
   **仍不得**作为关于区间 I 的结论证据。
6. **主 repo 交付物**：`HoTT/generators/PROBE-INTERVAL-I/`（REPORT 10,057 bytes + INDEX 3,056
   bytes），判词、三路收据定位、判词分级与未闭合项全部登记。
7. **修订片 021**：`Atria的方案/修订片/021 - 区间 I 设计探针：可写形态与表达界限（EXP-001
   收尾）.md`；索引 `Atria的方案/修订片.md` 已更新（last_shard→021、banner 20→21 个修订片、
   表内加 021 行）。`source=reflection`，定位为**步骤产出的方案落盘**（不是新提案）。
8. **第二份 020 合同审计集**（本 session 目录 `CORE_COGNITION_AUDIT.md` 索引 + 8 分片）：
   核心认知 46 条 = 对齐 10（+2 条按机制/发现分层）/ 深化 8（+1 条按方法/执行分层）/
   张力 5 / 未触及 9；扩展认知 8 片 32 个小节判断；**分片 008 裁决 = 延续 168 序列、不改道**
   （探针实测落在 168 预判的「不可写」分支内，反证条件未触发）。

## 本单元不是什么

- **不是数学结论**（F-011 / `MATH_PROOF_BEFORE_DELIVERY_V1`）：语言片段探针，
  `registers_new_claim:false`，不进 CLAIM_EVIDENCE_MATRIX。
- **不是发现**：零新数学命题、零新悖论候选；前提判定全部保持
  `AI_ADJUDICATED_PENDING_EXTERNAL_AUDIT`。**发现侧仍零产出。**
- **不是「HoTT 无法表达相关现象」**：是「表达的层不同」。
- **不判定任何前提的非现实性**（006 片三点保留全部适用）。
- **不声称**穷尽 I 上一切可写形态（第三形态问题登记为 unknown ingress）；
  不声称「Bool 观察器不可写」对其他工具链/未来版本成立（工具链相对性）；
  不声称引擎具备自主发现能力（探针模块由 AI 设计与冻结供给，003 片 §5 角色纪律）。

## 相对 168 的真实增量（诚实记账）

- **同形重复被打破**：167/168 产出同形的分母内负结论；169 产出链路以前没有的形态
  （表达界限的正面刻画），且是链路**第一次一个单元完全不跑分母**。
- **表达层可写性这一维被建立**：「HoTT 能否表达 X」现在有可复用测法（冻结形态候选 →
  原生核 → 收据 + 诊断名 + 行列号），且**必须区分「完全无法表达」与「只能以改变语义的
  形态表达」**。
- **母域第一次被升成被实际跑的问题**：区间 I 是「连续」这个母域在理论内的形式对应物；
  但升成的是**表达层**问题，不是**经济性断裂**问题（KC-000046 偏离从「零执行」收窄到
  「执行一半」）。
- **KC-000037–000039 的落差被确认为结构性**：三单元无回归，升级为 STATE 级结构性张力
  `T-OBVIOUSNESS-GAP-001`，作为 SUPPLY-010 第一优先级理由。
- **边际信息量低于 168**：闭合的是一个已登记的小缺口，不是一个新方向。
