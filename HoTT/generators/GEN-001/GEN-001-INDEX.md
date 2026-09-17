# GEN-001 能力验收索引

> ⚠️ 本索引是**能力验收索引**，不是数学结论索引。
> 本索引中的条目 `registers_new_claim: false`，**不进入** `HoTT/CLAIM_EVIDENCE_MATRIX.md`。
> 依据：方案修订片 003 §4 + 010 §2（CE-MAP 归属澄清）与 F-011。

## 索引行

| unit_id | task_family | premise | supply | grammar | search_run | verify_runs | 越界证明 | 判词 |
|---|---|---|---|---|---|---|---|---|
| `GEN-001-1` | TASK-FAMILY-WITNESS-RECOVERABILITY | PREMISE-E-02（pending external audit） | SUPPLY-007（AI 供给） | `L1-WITNESS-RECOVERY-v1` | `20260916-SEARCH-GEN001-WITNESS-RECOVERY-001` | `...-040` / `...-041B` / `...-049` | `GEN-001-OUT-OF-ENVELOPE.json`（15/15 旧文法机械越界） | `GENERATOR_LINK_DEMONSTRATED_WITH_SCOPE` |
| `GEN-001-2` | TASK-FAMILY-COMPLETION-PROCESS | PREMISE-A-03（pending external audit） | SUPPLY-001（AI 供给） | `L1-COMPLETION-PROCESS-v1` | `20260916-SEARCH-GEN001-COMPLETION-PROCESS-001` | `...-053` / `...-070` / `...-021` / `...-014` | `GEN-001-COMPLETION-PROCESS-OUT-OF-ENVELOPE.json`（15/15 旧文法机械越界，理由全部为 BIND_CONTINUATION） | `GENERATOR_LINK_DEMONSTRATED_WITH_SCOPE` |
| `GEN-001-4` | TASK-FAMILY-DIVISIBILITY-CONDITION-OR-CAPABILITY | PREMISE-D-01 / E-04 / G-03（pending external audit） | SUPPLY-004/006/008（AI 供给） | `L1-DIVISIBILITY-v1` | `SEARCH-GEN001-DIVISIBILITY-001` | `VERIFY-…-WV-0025` / `…-WV-0026` / `…-WV-0027` / `…-WV-0051` | `GEN-001-DIVISIBILITY-OUT-OF-ENVELOPE.json`（32 见证 × 6 旧 delay 文法 = 192/192 拒绝，理由全部唯一 BIND_CONTINUATION） | `GENERATOR_LINK_DEMONSTRATED_WITH_SCOPE`（PATTERN_REDUCED：三成员共享一机制 pattern，只报一个验收单元） |
| `GEN-001-5` | TASK-FAMILY-EXISTENCE-VERSUS-AVAILABILITY | PREMISE-D-04 / G-05（pending external audit；**置信度最低**） | SUPPLY-005/009（AI 供给） | `L1-EXISTENCE-v1` | `SEARCH-GEN001-EXISTENCE-001` | `VERIFY-…-WV-0017` / `…-WV-0018` / `…-WV-0043` / `…-WV-0051` | `GEN-001-EXISTENCE-OUT-OF-ENVELOPE.json`（32 见证 × 7 旧 delay 文法 = 224/224 拒绝，理由全部唯一 BIND_CONTINUATION） | `GENERATOR_LINK_DEMONSTRATED_WITH_SCOPE`（PATTERN_REDUCED：两成员共享一机制 pattern，只报一个验收单元） |
| `GEN-001-V2-1` | TASK-FAMILY-V2-EXISTENCE-VERSUS-AVAILABILITY | PREMISE-G-05 / D-04（pending external audit；**置信度最低**） | SUPPLY-009 / V2-A（AI 供给） | `L2-COFIBRATION-A-v1`（V2 片段，backend `v2-l2-cofibration`；门槛 G-b） | `SEARCH-GEN001-V2-1-001` | `VERIFY-GEN-001-V2-1-WV-{0001,23233,0785,0786}` | `GEN-001-V2-1-OUT-OF-ENVELOPE.json`（50,624/50,624 作用域内见证被 7 个旧 delay 文法全部拒绝，理由全部唯一；1,280 条纯 race/deadline 登记为 L1_SHARED_INGRESS） | `GENERATOR_LINK_DEMONSTRATED_WITH_SCOPE`（**PATTERN_REDUCED**：D-04/G-05 在 V2 片段坍缩到同一 availability 机制层，只报一个验收单元；现象新颖性 PARTIAL；**oracle_scope=POINT_SET_MIRROR_MODEL_KERNEL_CONFIRMED，interval_i 未确认**，不得作为区间 I 的结论证据） |
| `GEN-001-3` | TASK-FAMILY-IDENTITY-OBSERVATION-LAYER | PREMISE-B-01（pending external audit） | SUPPLY-003（AI 供给） | `L1-IDENTITY-OBSERVATION-v1` | `20260916-SEARCH-GEN001-IDENTITY-OBSERVATION-001` | `...-0014` / `...-0023` / `...-0044` / `...-0067` | `GEN-001-IDENTITY-OBSERVATION-OUT-OF-ENVELOPE.json`（17/17 旧文法机械越界，5 个 delay 文法理由全部唯一 BIND_CONTINUATION） | `GENERATOR_LINK_DEMONSTRATED_WITH_SCOPE` |

## 证据定位

- 冻结文法与族语义：`GEN-001-GRAMMAR.json`
- 分母、枚举、remainder、归约：`GEN-001-ENUMERATION.json`
- 越界机械证明：`GEN-001-OUT-OF-ENVELOPE.json`
- 原生核收据（F-011 五件套）：`../../verification/runs/20260916-VERIFY-GEN001-WITNESS-RECOVERY-{040,041B,049}/`
  （RUN.json / stdout.txt / stderr.txt / environment.txt / source-manifest.json / kernel/*/）
- `GEN-001-3` 收据：`../../verification/runs/20260916-VERIFY-GEN001-IDENTITY-OBSERVATION-{0014,0023,0044,0067}/`
- `GEN-001-4` 收据：`../../verification/runs/VERIFY-GEN001-DIVISIBILITY-WV-{0025,0026,0027,0051}/`（各含 RUN.json / kernel 四路五件套 / generated sources / main-repo-replay exit 0）
- `GEN-001-5` 收据：`../../verification/runs/VERIFY-GEN001-EXISTENCE-WV-{0017,0018,0043,0051}/`（各含 RUN.json / kernel 四路五件套 / generated sources / main-repo-replay exit 0）
- 引擎内完整收据（含 correspondence review / report / runner snapshot）：
  `/Volumes/D/HoTT-machine-overview/machine-overview/runs/`（同 repo 的 `feat/machine-overview-m1` 工作树）
- 验收报告：`GEN-001-REPORT.md` / `GEN-001-COMPLETION-PROCESS-REPORT.md` / `GEN-001-IDENTITY-OBSERVATION-REPORT.md` / `GEN-001-DIVISIBILITY-REPORT.md` / `GEN-001-EXISTENCE-REPORT.md` / `GEN-001-V2-1-REPORT.md`

## 禁止外推

- 本索引**不声称** E-02 前提非现实（该判定 pending external audit，且需 GEN-001 链 + 原生核才能升级为结论）。
- 本索引**不声称**引擎具备自主发现新方向的能力（任务族由 AI 冻结供给）。
- 本索引**不声称**开放候选空间被穷尽。
- **`GEN-001-4` 同族坍缩（修订片 013 §2.1 Q4）**：D-01 / E-04 / G-03 三成员在 delay 片段内**共享同一机制 pattern**（无界 delay 能力 vs 有界观察层；片段内无区间/截断塔/高阶迭代构造可区分三者），故只报**一个**验收单元，登记 `PATTERN_REDUCED_NOT_CERTIFIED_AS_FULL_TASK_EQUIVALENCE`；三成员的任务等价性**未被证明**。详见 `GEN-001-DIVISIBILITY-REPORT.md` §5。
- **`GEN-001-4` 现象新颖性（修订片 012 §2）**：**PARTIAL** —— 文法新颖性干净（唯一 BIND_CONTINUATION），但两个 continuation 是既有真/假分支发散形状的索引取值变体，第三个是同延迟相反值从 index 0 到 1 的移位；现象原语（单侧发散、同延迟相反值、bind 后越界）各自已在旧文法可部分表达。详见该 REPORT §4。
- **方向覆盖声明（修订片 013 §2.2）**：四族的分离机制全部属**方向 B**
  （delay-equivalent 对 + 观察层不同意；93/93 越界见证经 step-6 审计独立复算确认）。
  方向 A（现实可完成、理论化引入额外完成困难）在 delay 片段内**无对象承担**
  （引擎 `_witness_separates` 的前置条件即 `delay_equivalent`）。
  故本索引**不声称覆盖方向 A**。登记：`DIRECTION_A_UNREPRESENTABLE_IN_DELAY_FRAGMENT`。
- **`GEN-001-5` 同族坍缩（修订片 013 §2.1 Q4）**：D-04 / G-05 两成员在 delay 片段内**共享同一机制 pattern**（存在性判决被当作可调用资源而供给过程不可观察；片段内无 cofibration 结构、无 composition 操作、无资源消耗语义可区分两者），故只报**一个**验收单元，登记`PATTERN_REDUCED_NOT_CERTIFIED_AS_FULL_TASK_EQUIVALENCE`；两成员的任务等价性**未被证明**。详见 `GEN-001-EXISTENCE-REPORT.md` §5。
- **`GEN-001-5` 现象新颖性（修订片 012 §2）**：**PARTIAL** —— 文法新颖性干净（唯一 BIND_CONTINUATION），但三个 continuation 全部是真/假分支发散与同延迟相反值形状的索引取值变体；@index 1 的形状已被 GEN-001-4 占用，本族退到 @index 1 假分支晚负值与 @index 2 同延迟相反值。详见该 REPORT §4。
- **`GEN-001-5` 前提置信度（本族专属）**：D-04 / G-05 是 PREMISE-001/006 中**置信度最低、最可能被外部审计推翻为「现实」**的一对（可填充性是 cofibration 的定义条件）。前提判定保持 `AI_ADJUDICATED_PENDING_EXTERNAL_AUDIT`，本链不升级。详见该 REPORT §0。
- V2 片段首族（GEN-001-V2-1）收据：引擎 `runs/SEARCH-GEN001-V2-1-001/` + `runs/VERIFY-GEN-001-V2-1-WV-*/`（分支 `feat/machine-overview-m1`，commit `3a6ccd0`；四路核全 PASS，含 KEY_ADJUDICATION_AUDIT_TRAIL）。

## 后续单元状态

| task_family | 成员 | 状态 | 备注 |
|---|---|---|---|
| WITNESS-RECOVERABILITY | E-02 | `CHAIN_DEMONSTRATED`（本索引） | 52 个归约见证中 3 个已送核 |
| DIVISIBILITY-CONDITION-OR-CAPABILITY | D-01, E-04, G-03 | `CHAIN_DEMONSTRATED`（本索引，GEN-001-4） | corpus 风险最高三联；**PATTERN_REDUCED**：三成员共享一机制 pattern，只报一个验收单元；现象新颖性 PARTIAL；区间/截断塔/高阶迭代建模仍是 V2 候选（010 §3） |
| EXISTENCE-VS-AVAILABILITY | D-04, G-05 | `CHAIN_DEMONSTRATED`（本索引，GEN-001-5） | **置信度最低一对**（可填充性是定义条件；形式层理由最弱，与 GEN-001-4 的语料风险方向相反）；**PATTERN_REDUCED**：两成员共享一机制 pattern，只报一个验收单元；现象新颖性 PARTIAL；Kan composition / cofibration 结构建模仍是 V2 候选（010 §3） |
| COMPLETION-PROCESS | A-03, A-11 | `CHAIN_DEMONSTRATED`（本索引，A-03） | L1 片段；A-11 与 A-03 同形，合并与否由外部审计决定 |
| IDENTITY-OBSERVATION-LAYER | B-01 | `CHAIN_DEMONSTRATED`（本索引） | L1 片段；在 continuation 层表达"同一性结论随观察层改变"：delay 等价是理论的同一性判据，race/deadline 是看见被抹除轮次的观察层；44 越界见证拒绝理由全部唯一 BIND_CONTINUATION；4 见证原生核四路校验 + 主 repo 独立复现 |
