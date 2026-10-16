# 交接阶段经验

1. “用户提问已提取”不等于“AI 回答、工具事件、代码和 Git 已审计”；必须分开建立 ledger。
2. LocalGPT 的父线程和 HoTT-2 子线程不能用一个文件的数量替代 38-turn lineage；同一用户内容的重复和补充要显式标识。
3. WebGPT 的 workspace 快照是历史来源；其 `STATE`、R、SESSION 和 Git 需要重新绑定到顶层 repo，不能直接当作当前状态。
4. Gemini 的 `inlineFile` 是代码载荷，不能因为旧报告的摘要而分类成空记录；Drive 文档正文缺失必须保留缺口。
5. `/Volumes/D/ALL-Markdown/aistudio-docs/` 被用户移走是有效边界；替代文件是否覆盖原目录是待证事实，不是文件名可以解决的语义问题。
6. 核心认知的编号/hash/定位可以机械验证；是否深化、纠偏或偏航仍需当前 AI 写逐编号公开评估。
7. 22,226 条来源行可以全部登记而不等于 22,226 条语义已经人工判定；register 的 locator/ID/规则依据必须与 `PENDING_DIRECT_SENTENCE_ADJUDICATION` 同时保留。
8. 理解章节的逐文件“合并”可以安全地先形成 canonical 选择和 rollback receipt；保留 nested 源比未经授权删除更重要，line diff 也不等于数学内容等价。
9. core generation-2 只能通过新增用户原文输入和生成器重建；generation-1 前缀 identity check 是迁移证据，不能手工编辑旧 KC。
10. full EOF/hash、checkpoint、Git commit 和测试都不能认证模型理解；`model_context=NOT_CERTIFIED_BY_TOOL` 是必须保留的真实边界。
