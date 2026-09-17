# GEN-001-V2-1 验收报告：V2 L2-cofibration 首族链（第二阶段）

> 单元：`GEN-001 BOUNDED_GENERATOR_ACCEPTANCE_UNIT`（方案修订片 003）× V2 片段（修订片 015 §5 阶段 2）
> 任务族：`TASK-FAMILY-V2-EXISTENCE-VERSUS-AVAILABILITY`（SUPPLY-009 / V2-A；PREMISE-G-05 并入 PREMISE-D-04）
> 执行者：AI 全自动（修订片 017；`AI_ADJUDICATED_PENDING_EXTERNAL_AUDIT`）
> 执行日：2026-09-17
> 判词：**`GENERATOR_LINK_DEMONSTRATED_WITH_SCOPE`**（四项判据全部带收据，见 §3）

## 0. 本报告不是什么

- **不是数学结论**（F-011 / `MATH_PROOF_BEFORE_DELIVERY_V1`）。本单元验收的是**链的贯通**：
  冻结 → 枚举 → 归约 → 越界检查 → 原生核 → 收据。
- **不是"引擎自主发现了新方向"**。任务族与文法由 AI 冻结供给（角色纪律，003 §5）；
  引擎贡献的是在冻结文法上的完整枚举 + grammar-preserving 归约；原生核贡献 oracle 判定。
- **不是"该前提非现实"的证明**。G-05/D-04 的非现实判定仍是 pending external audit 的候选。
- **不是关于真实区间 I 的结论**（本报告最重要的诚实边界，见 §5）。

## 1. 链的实际运行（全部 observed，可复算）

| 阶段 | 产物 | 结果 |
|---|---|---|
| 冻结任务族 | `GEN-001-V2-1-GRAMMAR.json`（文法 `L2-COFIBRATION-A-v1`，backend `v2-l2-cofibration`） | 命中门槛 **G-b**（存在 ≠ 可用，双坐标；delay 片段无法承载：在 delay 中 `ret(n,b)` 的存在性即即时可用性，两个坐标不可分别观察）；新结构 op = `supply`/`fill`/`fill_of`/`tower`/`between`；3 个新 continuation verdict；界 `delay_index_max=2`、`declared_faces=[0,3,5,15]`、`tower_levels=[0,1]`、`context_depth_max=3`、`deadline_horizons=[0,1]` |
| 引擎枚举 | search run `SEARCH-GEN001-V2-1-001` | 3,059 contexts × 1,104 等价对 = **3,377,136 pair-context checks**；`complete_within_declared_grammar=true`；`grammar_violations=0`；**remainder=0**（预算未耗尽） |
| grammar-preserving 归约 | 同上 run | **212,864** 个原始分离 → **51,904** 个规范归约见证（每个归约步重检文法成员资格与分离性） |
| 越界证明（作用域化） | `GEN-001-V2-1-OUT-OF-ENVELOPE.json` | **50,624 / 50,624** 作用域内见证被全部 7 个既有 delay 文法拒绝，且**理由唯一**（buckets：`CONTEXT_DEPTH` 44,928 / `UNKNOWN_OP:supply` 3,776 / `BIND_CONTINUATION` 1,536 / `UNKNOWN_OP:between` 192 / `UNKNOWN_OP:tower` 192） |
| 原生核校验 | 4 个 verify run（§2） | 每个含 4 路 kernel 收据：`verify` / `controls` / `negative-control`（须被拒）/ `verify-replay`（确定性） |
| 收据化 | 引擎 `runs/SEARCH-GEN001-V2-1-001/`、`runs/VERIFY-GEN-001-V2-1-WV-*/`（分支 `feat/machine-overview-m1`，commit `3a6ccd0`） | RUN.json + kernel stdout/stderr/environment/command + 生成 Agda + source-manifest + witness-manifest（sha256 见 §6） |

**输入层 L1 不可见性（机械可复算，本族最强的新颖性证据）**：51,904 / 51,904 个归约见证的
**输入对**在 delay 轴上全部 `delayEquiv = true`——即 L1 delay 片段在输入层完全无法区分这些对；
分离完全由 V2 文法（结构 op / 新 continuation verdict / 新观察层）产生。
（注：输入层不可见 ≠ L1 无法用自带 context 复现分离；纯 race/deadline 见证共 1,280 条
可被 L1 复现，已登记为 ingress，见 §4 Q1。）

## 2. 原生核结果（Cubical Agda 2.8.0 + cubical v0.9，mirror `formal/V2Cofibration.agda`）

| verify run | 见证 | 新机制 | 绑定 continuation | verify | controls | negative-control | verify-replay |
|---|---|---|---|---|---|---|---|
| `VERIFY-GEN-001-V2-1-WV-0001` | WV-0001 | availability | —（裸 supply+fill） | KERNEL_ACCEPTED (exit 0) | ACCEPTED | **REJECTED_AS_EXPECTED (exit 42)** | EXACT_EXIT_STDOUT_STDERR_MATCH |
| `...-WV-23233` | WV-23233 | level | `availability_verdict_level_split` | KERNEL_ACCEPTED (exit 0) | ACCEPTED | **REJECTED_AS_EXPECTED (exit 42)** | EXACT_EXIT_STDOUT_STDERR_MATCH |
| `...-WV-0785` | WV-0785 | density | — | KERNEL_ACCEPTED (exit 0) | ACCEPTED | **REJECTED_AS_EXPECTED (exit 42)** | EXACT_EXIT_STDOUT_STDERR_MATCH |
| `...-WV-0786` | WV-0786 | density | — | KERNEL_ACCEPTED (exit 0) | ACCEPTED | **REJECTED_AS_EXPECTED (exit 42)** | EXACT_EXIT_STDOUT_STDERR_MATCH |

四个 kernel 见证覆盖 KERNEL_POLICY 的四个 cell（family-core availability / level×新 continuation /
density G-a / availability×`supplied_face_revealed`），全部 **L1-invisible**（输入 delayEquiv=true），
`KERNEL_FOUR_WAY_PASS`。`controls` 含两个正控制：同值对照（同一 context 作用于同一输入不分离）
与 delay 轴对照（`delayEquiv p q` 由原生核确认与 Python canonical 语义一致）。
`DENOMINATOR_SINGLE_SOURCE`（016 §3）：所有期望字面量由 `v2_cofibration.py` 计算，
与产生 search run 的同一 canonical 来源；`cross_check` 在任何 kernel 运行前先重算并断言
每个见证的分离性/机制/观察与记录一致。

## 3. 修订片 003 §4 的四项验收判据（逐项引用收据）

1. **分母固定且 remainder=0** — ✔ `checks_planned=checks_executed=3,377,136`，
   `complete_within_declared_grammar=true`，`checks_budget_exhausted=false`，
   `context_budget_exhausted=false`，`grammar_violations=0`，`order_independent=true`（换种子统计一致 + 归约见证集合相等）。
2. **至少一个候选是既有文法无法产出的** — ✔ 50,624/50,624 作用域内见证被 7 个既有 delay 文法
   全部拒绝且理由唯一（§1 表）。**作用域化**（012 §2.3）：只有绑定新 V2 continuation 或使用
   V2 结构 op 的见证计入越界分母；纯 race/deadline 见证 1,280 条列为 L1 共享 ingress（§4 Q1）。
3. **每个候选的 oracle verdict 由原生核而非启发式给出** — ✔ Cubical Agda 原生核 4 路收据，
   含必须被拒的负控制（exit 42，`wrongClaim = refl` 在 `false ≡ true` 上不可消解）
   与精确 replay 匹配（`EXACT_EXIT_STDOUT_STDERR_MATCH`）。Python 模型只负责**提出**候选
   与计算期望字面量，从不替代核。
4. **完整链 input → candidate → oracle → receipt** — ✔ 文法冻结 → search run →
   kernel verify run → kernel 收据 → 本报告，全部哈希绑定（§6）。

**判词：`GENERATOR_LINK_DEMONSTRATED_WITH_SCOPE`**
（generator_family：V2 L2-cofibration 片段的 typed term/proof synthesis 真实链；
scope：单一冻结任务族 + 其 6 个机制 cell；remainder=0；其余生成器族状态不变；
不声称开放候选空间的完备覆盖；不声称引擎具备自主发现能力。）

## 4. 强制披露段（012 三问 / 013 Q4 / 014 map 覆盖）

### Q1：本族的现象（omission shape）在旧文法中是否已可部分表达？

**部分可表达，必须标 PARTIAL**。机械证据（search 收据可复算）：

- **可复现的一半**：`value_mismatch`（31,872 条）与 `deadline_observation`（11,136 条）
  机制在 delay 片段中本身存在；1,280 条纯 race/deadline 见证（无结构 op、无新 continuation）
  被 L1 reader 判为可复现，登记为 **L1_SHARED_INGRESS**（012 §2.3 + 006 §5）。
  这些见证的**机制**不属于本族的新颖性。
- **不可复现的一半**：`availability_observation`（2,176）/ `level_observation`（3,840）/
  `density_observation`（2,624）三种新观察层在所有 7 个 delay 文法中**不存在对应 op**
  （拒绝理由 `UNKNOWN_OP:supply` / `UNKNOWN_OP:fill` / `UNKNOWN_OP:tower` / `UNKNOWN_OP:between`，
  或 `BIND_CONTINUATION` / `CONTEXT_DEPTH`）；且 51,904/51,904 的**输入对**在 delay 轴上不可区分。
- **结论**：本族的实质新颖性落在**新观察层与新 continuation verdict**上（把"可用性/层级/稠密度"
  显式化为可观察的分离轴），不落在 race/deadline 这些旧操作上。这是**部分达标**，
  交给外部审计复核。

### Q2：新构造子在该现象中承担什么？

- `supply(f)` + `fill`：把"cofibration 的可填充面"从**理论假设**变成**可登记、可核查的状态**
  （supplied 集合成员资格）。G-05 的 omission（"所有 cofibration 可填充"）在此被拆成
  "哪些面被声明可填充（`declared_faces=[0,3,5,15]`，16 面的真子集）"与
  "哪些面被实际供给"。可用性三态 `absent/pending/available` 是 D-04 的"存在 ≠ 可用"轴。
- 3 个新 continuation verdict（`supplied_face_revealed` / `never_supplied_face` / `level_split`）：
  把"供给状态"与"层级"提升为**延续的返回值**，使 delay 轴上的下游计算能**看见**它——
  这正是 G-05 的 omission 在程序上"被移出"的那一半：理论假设可填充性，但下游计算的
  可完成性依赖它。
- `tower(level)` / `between(a,b)`：层级轴与稠密轴（门槛 G-c / G-a），把"截断塔层级"
  与"面落在严格区间内"变成可观察的 Bool。

**不是"换标签"**：这些 op 在既有 delay 文法中连语法都不存在（`UNKNOWN_OP`），
且它们承载的观察层（availability/level/density）在旧文法中无对应分离种类。

### Q3：跨族机制重叠

- 与 5 个 delay 族的共享机制：`value_mismatch` / `completion_divergence` / `deadline_observation`
  （ingress，见 Q1）。**重叠不禁止**（片段共享分母是有意设计），但**族间独立性未证**，
  仅登记为 ingress。
- `deliver_business` / `const_omega` 两个 continuation 是**共享校准 continuation**
  （与 delay 片段同形），`continuation_map_coverage` 确认 5 个 continuation 的 map 互异
  且 L1 擦除后与 delay map 一致（`v2_maps_mutually_distinct=true`，逐 continuation 报告）。

### Q4（013 片，多成员族同族坍缩）：D-04 与 G-05 是否坍缩？

**坍缩到同一机制层；判 `PATTERN_REDUCED`，只报一个验收单元。**

机械证据（归约集 51,904 条的实际机制分布）：

| 机制层 | 归约见证数 | 归属 |
|---|---|---|
| `availability_observation` | 2,176 | **D-04 + G-05 共同的机制层**（supply + fill 的可用性三态） |
| `level_observation` | 3,840 | 门槛 G-c 的层级轴，**不属于** D-04/G-05 |
| `density_observation` | 2,624 | 门槛 G-a 的稠密轴，**不属于** D-04/G-05 |
| `value_mismatch` | 31,872 | L1 共享机制（ingress） |
| `deadline_observation` | 11,136 | L1 共享机制（ingress） |
| `completion_divergence` | 256 | L1 共享机制（ingress） |

- **D-04（存在 ≠ 可用）与 G-05（所有 cofibration 可填充设为构造可用）在本片段中不可机械区分**：
  两者都映射到同一个可观察量——一个被声明可填充的面从未被供给，`fill` 因此 pending。
  SUPPLY-005/009 的**合并建议正确**。
- **差异层**（ premise 层的框定「存在但未就位」vs「可填充性被预设为可用」）在本片段中
  **不可观察**，因此不构成独立机制 cell。
- **本族整体不是单一机制坍缩**：它携带 3 个新结构机制 cell + 3 个 L1 共享机制 cell，
  全部在表中列出。只报一个验收单元的理由是 D-04/G-05 的合并，不是全族单机制。

### 014 片：map 空间与现象饱和

- V2 map 空间：5 个 continuation × 2 个 Bool 输入 = 10 个 map 端点，全部被枚举覆盖
  （`continuation_map_coverage.continuation_count=5`，逐 continuation 报告 true/false 的
  L1 擦除值，`v2_maps_mutually_distinct=true`）。
- **现象饱和声明**：本族出现的 6 个分离种类 = 该文法可表达的**全部**分离种类
  （`separation_kind` 的 6 个构造子全部出现在归约集中，无未用种类）。这是"该文法内
  现象层饱和"的声明，**不是**"候选空间已穷尽"——新文法/新 op 仍可引入新现象（014 §2.3 门槛）。

## 5. V2 专属强制披露（015 §5）——外部审计请优先看这里

**每个见证必须声明它是枚举器（点集模型）内成立，还是已由原生核在真实区间 I 上确认。**

本族的 4 个 kernel 见证全部声明为：

```text
oracle_scope            = POINT_SET_MIRROR_MODEL_KERNEL_CONFIRMED
interval_i_confirmed    = false
interval_i_oracle_exists = false
conclusion_evidence_about_interval_I = false
gen001_capability_evidence = true   （链贯通的验收证据）
```

**为什么**：mirror `formal/V2Cofibration.agda` 定义 `Face = Point → Bool`，即**点集模型**。
mirror 自己在 §10 用 DM3（三元链 De Morgan 代数）反模型证明：点集模型对 De Morgan 代数
**可靠但不完备**——它验证布尔律 `f ∧ ¬f = 0`，而区间 I 作为 De Morgan 代数中该律**失效**。
mirror 明文写出"真实区间 I 的 oracle verdict 只能由 I 上的原生核给出，绝不能来自本 mirror（F-011）"，
而 **mirror 中不存在区间 I 的解释**。

因此：原生核的 `KERNEL_ACCEPTED` 证明的是**枚举器与 mirror 的声明片段语义逐项一致**
（`refl` 消解，DENOMINATOR_SINGLE_SOURCE），**不是**该分离在真实区间 I 上成立。
依 015 §5 / F-011，这些见证**一律不得作为关于 HoTT / 区间 I 的结论证据**。

**机械 model-dependency 审计**（每个见证分类分离由何种机制产生、是否调用点集专属律）：

| 见证 | 依赖类 | 调用点集专属律 | 说明 |
|---|---|---|---|
| WV-0001 | `SUPPLIED_SET_MEMBERSHIP` | 否 | 可用性判决只依赖 supplied 集合的可判定成员资格与 fill op，不调用任何格律；结构性、解释无关 |
| WV-23233 | `BOUNDED_LEVEL_COMPARISON` | 否 | tower 判决是有界格 `{b0,b1,b2}` 中的比较，有限可判定 |
| WV-0785 / WV-0786 | `FACE_LATTICE_ORDER` | **是** | density/between 调用 Face 上的点集序；mirror §10 证明该模型对 De Morgan 代数不完备，故此分离**仅为模型层**，无区间 oracle 不能提升 |
| （delay 轴的 `value_mismatch`） | `COMPUTATION_AXIS_BOOLEAN_PAYLOAD` | 否 | delayEquiv 只比较布尔载子 b；两个布尔的不等在 Bool 到任何 De Morgan 代数的标准嵌入下保持，但**此提升未经核证明**，登记为候选后续 |

**未声称**：不声称点集模型忠实于真实区间；不声称任何见证是关于 I 的结论；
不声称已构造区间 I 的 oracle（这是**已登记的缺口**，不是已完成的工作）。

## 6. 越界检查的作用域边界（诚实披露）

- 机械成员资格检查的**作用域 = 7 个既有 delay 文法**（唯一带 delay 轴、可能表达本族见证的文法）。
- 其余 **12 个 symbolic-horn 文法**（`machine-overview-grammar/v1`，backend `symbolic-horn-v1`）
  在结构上无法表达任何 delay/V2 见证：L1 reader 读取它们时甚至无法解析
  （缺 `delay_index_max` 等字段，`KeyError`）。这与 V1 报告的 `BACKEND_MISMATCH`
  论证相同，但**本单元未对它们跑机械检查**——这是作用域边界，不是已证的不相交。
  外部审计若要求，可补跑一个显式的 schema-level 不相交断言。

## 7. KEY_ADJUDICATION_AUDIT_TRAIL（017 §3）

本单元产生的每个关键判定都带可审计链（`question` / `verdict` / `verdict_reason` /
`falsifier` / `evidence_anchors` / `audit_status` / `depends_on`），存于每个 verify run 的
`RUN.json`。推翻任一判定的可操作条件：

- 推翻四路核判定：kernel ACCEPT `Falsify.agda`，或 REJECT `Verify.agda`，或 replay 不匹配。
- 推翻越界判定：任一既有 delay 文法接受某作用域内见证。
- 推翻 Q4 坍缩判定：在 availability 机制层内找到 D-04 与 G-05 的可机械区分差异。
- 推翻新颖性判定：在既有 delay 文法中用既有 op 复现 availability/level/density 三态之一。

`depends_on`（回滚清单）：`SEARCH-GEN001-V2-1-001`、4 个 `VERIFY-GEN-001-V2-1-WV-*`、
`machine-overview/formal/V2Cofibration.agda`、`machine-overview/machine_overview/v2_*.py`、
本报告与三个 JSON 交付物。

## 8. 全量见证清单的可审计性

全量 51,904 条归约见证清单（`witness-manifest.json`）保留在引擎工作树
（分支 `feat/machine-overview-m1`，commit `3a6ccd0`）。主 repo 只存 sha256 与统计：

```text
count  = 51904
path   = /Volumes/D/HoTT-machine-overview/machine-overview/runs/SEARCH-GEN001-V2-1-001/witness-manifest.json
sha256 = 见 GEN-001-V2-1-ENUMERATION.json / witness_manifest.sha256
```

外部审计可凭 sha256 在引擎工作树核验任一条见证；主 repo 不复制全量清单（体积纪律）。

## 9. 下一个单元（AI 全自动推进，017）

1. **区间 I oracle 缺口**（§5 已登记）：构造 DM3 或真实区间（min/max/neg）上的 V2 值解释，
   使结构性分离（availability/level/boolean payload）可由原生核在 De Morgan 代数上确认。
   这是把模型层分离升级为结论证据的**唯一**路径（015 §5 / F-011）。
2. V2 第二族（G-a 稠密族或 G-c 层级族的独立供给），或 SUPPLY-010 的新任务族。
3. 每个单元完成后：checkpoint --apply + 修订片登记 + goal-1 指针同步，全部 git 提交。
