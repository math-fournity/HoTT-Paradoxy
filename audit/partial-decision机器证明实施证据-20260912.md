# MP-PARTIAL-DECISION-001 实施证据：strict 与 partial classifier 的最小原生边界

> 文档身份：F-011 implementation evidence
> 日期：2026-09-12
> proof ID：`MP-PARTIAL-DECISION-001`；claim IDs：`C-118`–`C-123`
> final run：`HoTT/verification/runs/20260912-MP-PARTIAL-DECISION-001-01/`
> 状态：`MACHINE_PROVED_LOCAL_UNCOMMITTED / PARTIAL_DECISION_BOUNDARY_WITH_POSITIVE_CONTROL`

## 0. 本轮目标

STATE revision 47 把第一工作包固定为 **N6：最小 quotient + partial/total（strict）classifier 边界**。目标是把 N5 审计中 D1（*Partiality, Revisited* §5.2）的结构——partial classifier 存在、total/strict 版本需要额外条件——做成原生 Cubical Agda 的最小机器实例，且不重述 race/timeout 或 R036/R038。

## 1. 形式化内容

源文件：`HoTT/formal/partial-decision/PartialDecision.agda`（`--safe --cubical --guardedness`）。

- 源状态 `A = {a,b,c}`，`R_A` 只识别 `a,b`；商 `Q = A / R_A`（Cubical SetQuotients HIT）；
- 最小 delay/partiality 片段 `Delay Bool = now Bool | later (Delay Bool)`；
- 弱互模拟式关系 `R_D (now x) (later (now y)) = (x ≡ y)`；商 `D≈ = Delay Bool / R_D`；
- 代表层分类器 `P0 a = now true`、`P0 b = later (now true)`、`P0 c = now false`；strict 观察 `strict (now _) = true`、`strict (later _) = false`。

六条 claim：代表层分类器存在（C-118）；strict 区分 `now/later`（C-119）；不存在 strict `Q → Delay Bool` 扩展（C-120）；`P0` 下降到 `Q → D≈` 的 partial classifier（C-121，正控制）；不存在 strict `Q → Bool` 消费者（C-122）；代表层消费者存在且区分 `a,b`（C-123）。

## 2. 实现选择与失败谱系

所有失败按责任点修复，命题未削弱：

1. **ClashingDefinition `true≢false`**：与 `Cubical.Data.Bool.Properties` 重名；删除本地版本，改用库定义。
2. **AmbiguousName `rec`**：`Cubical.Data.Empty.rec` 与 `SetQuotients.rec` 冲突；把集合商消去器重命名为 `SQ-rec`。
3. **UnequalTerms（路径复合方向）**：初版把 `sym pa ∙ cong g (eq/ …) ∙ pb` 写成 `pa ∙ … ∙ sym pb`；按“`now true` 经 `g [a]`、`g [b]` 到 `later (now true)`”重排。
4. **UnsolvedConstraints（`isSet/`）**：`squash/` 的数据参数无法反向推断；显式写 `squash/ {A = X} {R = R}`。
5. **UnsolvedConstraints（商注入）**：`[ P0 x ]` 的商参数无法推断；定义 `inj : Delay Bool → D≈` 并显式标注 `eq/ {A = Delay Bool} {R = R_D}`。

最终命令（由 `capture_agda_proof_run.py` 复现）：

```text
agda --ignore-interfaces --library-file=HoTT/formal/partial-decision/AGDA_LIBRARIES \
     -l cubical-0.9 -i HoTT/formal/partial-decision \
     HoTT/formal/partial-decision/PartialDecision.agda
```

final run：exit 0、stdout 11,353 bytes、stderr 0 bytes、零 warning。

## 3. Run/索引证据

- `RUN.json`：`KERNEL_ACCEPTED_WITH_SCOPE`、`INDEXED_IN_CLAIM_EVIDENCE_MATRIX`、exit 0；
- `source-manifest.json`：`PartialDecision.agda` + `TOOLCHAIN.json` + `AGDA_LIBRARIES` 哈希；
- `index-row-manifest.json`：proof row + 6 claim rows 冻结（7 行）；
- `verify_formal_proof_run.py --rerun`：

```text
kernel_status=KERNEL_ACCEPTED_WITH_SCOPE
index_status=INDEXED_IN_CLAIM_EVIDENCE_MATRIX
index_validation=EXACT_INDEX_SNAPSHOT_MATCH
replay=EXACT_EXIT_STDOUT_STDERR_MATCH
```

工具链身份与既有 `MP-*` 包相同：Agda 2.8.0-3d04bac、官方 release SHA-256、Cubical v0.9（tag commit `b150186d…`、tree SHA-256 `73ccfbaf…`）。

## 4. 旧包在矩阵增长后的重验

矩阵追加 C-118–C-123 后，十一个既有 package 全部重放：

```text
ROW_STABLE_AFTER_INDEX_EVOLUTION / EXACT_EXIT_STDOUT_STDERR_MATCH
```

详见本轮 Session 的 `RUNS.json` 与 `POST-CHECKPOINT.json`；旧 proof/claim 行未被改写。

## 5. 判词与边界

- 判词：`PARTIAL_DECISION_BOUNDARY_WITH_POSITIVE_CONTROL`（第二级；不是 HoTT 悖论）；
- 商层只能交付 up-to-weak-bisimilarity 的 partial classifier，strict delay 值与 strict Bool 消费者无法下降；
- 代表层的 strict 信息存在（C-118/C-119/C-123），因此缺口是商化丢弃展示差异，而非计算系统普遍失效；
- 本包是最小 delay 片段，不是完整 partiality monad；未形式化 `ℝq → 𝟐⊥`；
- 不证明任何真实库存在错误消费者，不主张原创性。

## 6. 证据锚点

- `HoTT/formal/partial-decision/PartialDecision.agda`；
- `HoTT/formal/partial-decision/README.md`、`TOOLCHAIN.json`、`AGDA_LIBRARIES`；
- `HoTT/verification/runs/20260912-MP-PARTIAL-DECISION-001-01/`；
- `HoTT/CLAIM_EVIDENCE_MATRIX.md`（`MP-PARTIAL-DECISION-001` 行与 C-118–C-123）；
- `audit/derived-development-consumer审计-20260912.md`（D1 §5.2 来源）；
- `.codex/research/hott/sessions/S-RES-20260912-043-NATURAL-CONSUMER-AUDIT/evidence/sources/full-1610.09254.txt`。
