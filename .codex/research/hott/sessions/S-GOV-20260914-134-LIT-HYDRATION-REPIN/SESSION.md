# S-GOV-20260914-134-LIT-HYDRATION-REPIN

- 发现：S133 literature task hydration 为 4,121,461 bytes，最大两项是 TRIAGE 1,562,324 bytes 与 candidates 1,275,732 bytes。
- 修复：新增 `audit/literature/LIT-DENOMINATOR-001/discovery-20260914/TRIAGE-RECEIPT.json`，记录两项 bytes/hash 与 32/164/1745、33/13/20 计数；从 STATE source_hash hydration 删除大型正文。
- 边界：大型 JSON 原件未改、未删除；按需读取。S133 分母和下一 R1 不变；无数学 claim。
