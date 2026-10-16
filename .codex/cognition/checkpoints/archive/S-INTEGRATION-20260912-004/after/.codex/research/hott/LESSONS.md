# 交接阶段经验

1. “用户提问已提取”不等于“AI 回答、工具事件、代码和 Git 已审计”；必须分开建立 ledger。
2. LocalGPT 的父线程和 HoTT-2 子线程不能用一个文件的数量替代 38-turn lineage；同一用户内容的重复和补充要显式标识。
3. WebGPT 的 workspace 快照是历史来源；其 `STATE`、`R`、SESSION 和 Git 需要重新绑定到顶层 repo，不能直接当作当前状态。
4. Gemini 的 `inlineFile` 是代码载荷，不能因为旧报告的摘要而分类成空记录；Drive 文档正文缺失必须保留缺口。
5. `/Volumes/D/ALL-Markdown/aistudio-docs/` 被用户移走是有效边界；替代文件是否覆盖原目录是待证事实，不是文件名可以解决的语义问题。
6. 核心认知的编号/hash/定位可以机械验证；是否深化、纠偏或偏航仍需当前 AI 写逐编号公开评估。

7. runtime 先拒绝依赖状态不一致，再在显式降级 review_required 后提交成功；拒绝收据和开放项都应保留。
