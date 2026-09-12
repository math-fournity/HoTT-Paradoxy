# S-GOV-20260912-018-MERGE-COUNT-SEMANTICS

- 触发：理解章节正文正确写成 24 个同名对=15 identical+9 different、另有 1 个顶层独有文件，但 builder 把所有 10 个 non-identical union entries 都命名为 `different_pairs`。
- 修复：`different_pairs=9`；新增 `nonidentical_union_entries=10`；verifier 重算六类分母并拒绝伪造 10 的负向 fixture。
- 证据：实际 builder/manifest/verifier 为 25 union、24 same-name、15 identical、9 different、10 nonidentical union、1 top-only、0 nested-only、0 unresolved；负向返回 `COUNT_DIFFERENT_PAIRS_MISMATCH:10:9`。
- 边界：这只修复机器计数语义；2,396 条 claim 的直接句级/数学融合仍为 OPEN_ISSUE。
- 完成后：重跑 fresh/projection/full suite、JSON/schema、Git diff/check/status 并完成精确 commit/tag。
