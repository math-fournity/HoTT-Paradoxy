# S-GOV-20260915-147-LOGICAL-SHARD-ORDER

- 类型：S146 后的认知水合顺序 corrective。
- 触发：活动候选先选中 `LIT-HOTT-COMPUTABILITY-001` 第 004 片，Goal task plan 随后展开 index 时输出 004→001→002→003。
- 修正：runtime 3.6.1 在识别 canonical index 后按 table 顺序重排已有分片，并保留原 selection reasons。
- 验证：runtime 单测 39/39 PASS；实际 Goal task plan 输出 001→002→003→004，`review_required=[]`、`query_first_promoted=[]`。
- 边界：只证明输入计划的机械顺序；模型理解与数学不由本轮认证。
- 研究：2LTT internal fibrant replacement→UIP 仍是下一 active candidate；Goal 保持 active。
- Git：`LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED`；未 push、未 tag。
