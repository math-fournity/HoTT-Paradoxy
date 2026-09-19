# 接续指针

## 每个新 Session/压缩后的固定恢复

1. 读取根 `AGENTS.md`、`README.md`、`MEMORY.md`、`feature-list.md`、`rulings.md` 和本地治理 Skill/PROTOCOL/LOAD_SET/STATE。
2. 严格全文读取 `核心认知.md` → `方向追踪.md` → `全景视野.md`；当前 core 是 generation-3/27 KC，manifest/旧 receipt 不能替代。
3. 纯治理用 `cognition_runtime.py plan --profile governance`；数学研究用 `--profile research`。
4. 先 `query --record <ID>` 判断 lifecycle/evidence，再用 `plan --profile research --task <ID>` 水合本轮证据；不要自动读取所有 historical/review_required Session。
5. 运行 `scripts/audit/verify_core_cognition.py`、`verify_three_way_cognition.py` 和 `verify_projection_freshness.py`；实现审计再读 validator/runtime 源码。
6. 结束时为当前 generation 全部 KC 写人工回评，并经原子 checkpoint 更新真正变化的 owner。

## 当前停止点

generation-3、六层 LOAD_SET、runtime 3.0、STATE v2、27-KC回评和 revision 15 checkpoint 构成本轮交付。fresh Python receipt 只证明输入/工具行为；fresh 模型行为、数学正确性、aistudio coverage 和 2,396 条 claim 语义仍未由本轮完成。
