# R3→R4 Gödel 义务矩阵

资产类型：`MACHINE_MANAGED_CANONICAL`  
manager：`scripts/audit/build_r3_r4_obligations.py`  
schema：`hott-r3-r4-obligation-matrix/v1`

`R3-R4-OBLIGATIONS.json` 逐项登记 `.codex/research/hott/R3-R4-GODEL-RETURN-001.md` 冻结的十二项义务。状态只能是 `PRESENT_MACHINE_PROVED`、`PRESENT_SOURCE_REPORTED_NOT_REPLAYED`、`ABSENT_BY_DEFINITION`、`OPEN`、`NOT_APPLICABLE`。不要手改派生输出；更新证据或 curated matrix 后运行：

```bash
python3 -B scripts/audit/build_r3_r4_obligations.py build --write
python3 -B scripts/audit/build_r3_r4_obligations.py validate
python3 -B scripts/audit/build_r3_r4_obligations.py query --obligation H-NAT
python3 -B scripts/audit/test_r3_r4_obligations.py
```

本矩阵只完整登记当前 R3 source 与 current groupoid-syntax target 之间的证明义务。`OPEN`/`ABSENT_BY_DEFINITION` 不证明不可实现；`PRESENT_MACHINE_PROVED` 也受 `present_scope` 限制。
