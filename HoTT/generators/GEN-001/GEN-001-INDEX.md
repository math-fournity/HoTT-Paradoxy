# GEN-001 能力验收索引

> ⚠️ 本索引是**能力验收索引**，不是数学结论索引。
> 本索引中的条目 `registers_new_claim: false`，**不进入** `HoTT/CLAIM_EVIDENCE_MATRIX.md`。
> 依据：方案修订片 003 §4 + 010 §2（CE-MAP 归属澄清）与 F-011。

## 索引行

| unit_id | task_family | premise | supply | grammar | search_run | verify_runs | 越界证明 | 判词 |
|---|---|---|---|---|---|---|---|---|
| `GEN-001-1` | TASK-FAMILY-WITNESS-RECOVERABILITY | PREMISE-E-02（pending external audit） | SUPPLY-007（AI 供给） | `L1-WITNESS-RECOVERY-v1` | `20260916-SEARCH-GEN001-WITNESS-RECOVERY-001` | `...-040` / `...-041B` / `...-049` | `GEN-001-OUT-OF-ENVELOPE.json`（15/15 旧文法机械越界） | `GENERATOR_LINK_DEMONSTRATED_WITH_SCOPE` |

## 证据定位

- 冻结文法与族语义：`GEN-001-GRAMMAR.json`
- 分母、枚举、remainder、归约：`GEN-001-ENUMERATION.json`
- 越界机械证明：`GEN-001-OUT-OF-ENVELOPE.json`
- 原生核收据（F-011 五件套）：`../../verification/runs/20260916-VERIFY-GEN001-WITNESS-RECOVERY-{040,041B,049}/`
  （RUN.json / stdout.txt / stderr.txt / environment.txt / source-manifest.json / kernel/*/）
- 引擎内完整收据（含 correspondence review / report / runner snapshot）：
  `/Volumes/D/HoTT-machine-overview/machine-overview/runs/`（同 repo 的 `feat/machine-overview-m1` 工作树）
- 验收报告：`GEN-001-REPORT.md`

## 禁止外推

- 本索引**不声称** E-02 前提非现实（该判定 pending external audit，且需 GEN-001 链 + 原生核才能升级为结论）。
- 本索引**不声称**引擎具备自主发现新方向的能力（任务族由 AI 冻结供给）。
- 本索引**不声称**开放候选空间被穷尽。
- 其余四个任务族（DIVISIBILITY / EXISTENCE-VS-AVAILABILITY / COMPLETION-PROCESS /
  IDENTITY-OBSERVATION-LAYER）仍是后续单元，状态 `NOT_STARTED`。

## 后续单元状态

| task_family | 成员 | 状态 | 备注 |
|---|---|---|---|
| WITNESS-RECOVERABILITY | E-02 | `CHAIN_DEMONSTRATED`（本索引） | 52 个归约见证中 3 个已送核 |
| DIVISIBILITY-CONDITION-OR-CAPABILITY | D-01, E-04, G-03 | `NOT_STARTED` | corpus 风险最高三联；外部审计优先复核；区间建模成本高（010 §3） |
| EXISTENCE-VS-AVAILABILITY | D-04, G-05 | `NOT_STARTED` | 置信度最低；外部审计优先复核 |
| COMPLETION-PROCESS | A-03, A-11 | `NOT_STARTED` | L1 片段低成本（010 §3） |
| IDENTITY-OBSERVATION-LAYER | B-01 | `NOT_STARTED` | 需 definitional vs propositional equality 分离 |
