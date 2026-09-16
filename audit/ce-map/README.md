# CE-MAP 机器管理资产

资产类型：`MACHINE_MANAGED_CANONICAL`  
schema：`hott-candidate-evidence-map/v1`  
唯一 manager：`scripts/audit/build_ce_map.py`  
语义输入 owner：`.codex/research/hott/STATE.json`、`HoTT/verification/PROOF_VERSION_CLOSURE.json`、`HoTT/CLAIM_EVIDENCE_MATRIX.md` 与 `audit/imports/machine-overview-ce-map-20260915/`

`CE-MAP.json` 是 478 个冻结输入的八轴 canonical registry；它体积较大，不应被未来 AI 当作普通文档全文水合。先读本文件与 `REPORT.md`，需要单项证据时使用：

```bash
python3 -B scripts/audit/build_ce_map.py query --id <canonical-id-or-source-id>
python3 -B scripts/audit/build_ce_map.py list-unclassified
python3 -B scripts/audit/build_ce_map.py validate
```

更新语义时修改上游 owner 或 manager 中显式 ID taxonomy，再执行 `build --write`；不得手改 `CE-MAP.json`、`UNCLASSIFIED.json`、`REPORT.md` 或 `RECEIPT.json`。这四个文件采用确定性序列化，validator 会检查分母、八轴、class membership、投影、receipt 哈希和来源新鲜度。

`validate` 首先验证冻结产物的内部完整性，然后报告 live source 是否演化；来源演化产生 `VALID_WITH_SOURCE_EVOLUTION`，表示历史快照仍完整但已不是当前输入。要求当前逐字重建时使用 `--require-current-sources`。

本资产的 `CE_MAP_V1_COMPLETE_WITH_SCOPE` 只说明 revision 149 的具名分母已全部登记；`UNKNOWN`/`UNCLASSIFIED` 必须保留。它不证明开放世界完备、HoTT 内部不一致、现实桥梁完成或研究 Goal 完成。
