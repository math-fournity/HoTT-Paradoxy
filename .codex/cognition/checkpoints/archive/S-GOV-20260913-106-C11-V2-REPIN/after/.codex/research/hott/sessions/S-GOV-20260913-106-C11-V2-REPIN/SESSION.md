# S-GOV-20260913-106-C11-V2-REPIN

- 触发：S105 应用后跑 verifier，发现 C11 v2 的两处副作用——(a) 重写时误删了 v1 的 univalence/SIP 行；
  (b) `verify_ledger_retrodiction.py` 仍用 v1 的“#N”行标签。/ 另外 C11 哈希写入 merge manifest，重建后级联影响 14 条 record。
- 处置：补回 `#2b univalence（ua）/SIP` 行；校验脚本改为按 v2 表行号（1/2/2b/3/4/5/6a/6b/7/8/9）匹配；
  重建 `audit/understanding-chapter-merge-manifest.json`；本 checkpoint 重新绑定 16 条 record；五个 verifier 全部 PASS。
- 边界：语义零改动（数学判词、候选状态、研究队列不变）；不新增数学 claim；不 push。
