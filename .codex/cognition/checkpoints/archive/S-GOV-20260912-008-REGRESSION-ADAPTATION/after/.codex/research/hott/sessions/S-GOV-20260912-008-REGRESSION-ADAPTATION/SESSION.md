# 回归测试与兼容 reader 适配 Session

- session_id: `S-GOV-20260912-008-REGRESSION-ADAPTATION`
- scope: 将继承的 governance/runtime/full-closure 测试夹具适配到当前顶层 core 与三件套合同；不改数学研究状态
- authorization: 用户已授权本地治理框架升级；不修改外部 WebGPT/LocalGPT repo、不恢复已移走目录
- mathematical_status: `UNCHANGED_FROM_R039`
- cognition_status: `BOUNDED_REGRESSION_ADAPTATION_WITH_FULL_KC_AUDIT`

## 实际修复

旧 `test_cognition_runtime.py` 仍使用 WebGPT 的 `hott-session-governance` 角色名、两项固定入口和旧夹具；已改为当前 `hott-local-session-governance`、`核心认知.md`→`方向追踪.md`→`全景视野.md`、当前 projection marker 和 `three_way_order`。

旧 `read_cognitive_closure.py`/`test_full_closure_loading.py` 仍指向 WebGPT 的第五闭包 `/mnt/data` 时代路径，且假设 131072 bytes 一次到 EOF；已改为当前 `核心认知.md` compatibility reader，并用连续分页测试大于旧 2115 行边界。它仍明确不替代三件套完整启动器。

## 验证结果

- `test_cognition_runtime.py`: `56/56 PASS`。
- `test_full_closure_loading.py`: `17/17 PASS`。
- `scripts/audit/test_three_way_cognition.py`: `3/3 PASS`。
- `verify_core_cognition.py`: `PASS`，903 KC，core SHA 不变。
- `verify_history_ledgers.py`: `PASS`，四类历史 ledger 分母不变。
- `verify_three_way_cognition.py`: `PASS`，state revision=8，24 directions/20 outcomes。
- `cognition_runtime.py plan`: `PASS`，固定前三项保持，`model_context=NOT_CERTIFIED_BY_TOOL`。

## 证据边界

这次 PASS 证明的是当前测试夹具、兼容 reader、runtime 状态机和三件套引用合同在声明范围内一致；不证明宿主自动加载、模型理解、历史方向全部语义整合、数学真理或现实桥梁。继承 WebGPT 的旧 73 项回归仍是历史证据，不被本次适配重写。
