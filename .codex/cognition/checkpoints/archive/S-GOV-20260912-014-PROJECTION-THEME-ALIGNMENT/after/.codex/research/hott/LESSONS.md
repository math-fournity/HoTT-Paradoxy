# 交接阶段经验

1. “用户提问已提取”不等于“AI 回答、工具事件、代码和 Git 已审计”；必须分开建立 ledger。
2. LocalGPT 的父线程和 HoTT-2 子线程不能用一个文件的数量替代 38-turn lineage；同一用户内容的重复和补充要显式标识。
3. WebGPT 的 workspace 快照是历史来源；其 `STATE`、R、SESSION 和 Git 需要重新绑定到顶层 repo，不能直接当作当前状态。
4. Gemini 的 `inlineFile` 是代码载荷，不能因为旧报告的摘要而分类成空记录；Drive 文档正文缺失必须保留缺口。
5. `/Volumes/D/ALL-Markdown/aistudio-docs/` 被用户移走是有效边界；替代文件是否覆盖原目录是待证事实，不是文件名可以解决的语义问题。
6. 核心认知的编号/hash/定位可以机械验证；是否深化、纠偏或偏航仍需当前 AI 写逐编号公开评估。
7. 22,226 条来源行可以全部登记而不等于 22,226 条语义已经人工判定；register 的 locator/ID/规则依据必须与 `PENDING_DIRECT_SENTENCE_ADJUDICATION` 同时保留。
8. 理解章节的逐文件“合并”可以安全地先形成 canonical 选择和 rollback receipt；保留 nested 源比未经授权删除更重要，line diff 也不等于数学内容等价。
9. core 当前代必须由人工 curation + canonical manager 生成；任何用户新悖论/元数学原文进入新 generation，旧代由 tag/transition 保留，不能手工编辑生成物。
10. full EOF/hash、checkpoint、Git commit 和测试都不能认证模型理解；`model_context=NOT_CERTIFIED_BY_TOOL` 是必须保留的真实边界。
11. `role=user` 只证明消息由用户通道发送，不证明其中每段都是用户原创；Response annotations、转发信件、复合 briefing 必须逐项区分，不能把 AI 文字注入 core。
12. “core 必须全文加载”保护的是用户定义的当前逻辑文档，不保护旧生成器的错误边界；重建可缩小当前输入，但必须精确原文、逐消息 disposition、完整迁移和可回滚历史。
13. `evidence_status=REVIEW_REQUIRED` 不等于 `lifecycle_status=ACTIVE_WORK`。把二者混成一个 status 会让历史 Session/逐-KC表永久复活并形成自激压缩循环。
14. 失败要按责任点记录：错误 unittest 入口不是测试失败；旧 2115 行下限是坏 oracle；旧 payload 含 `---` 使“完全相等”预期错误。修命令/规格后复跑，不能改数据求绿。
15. 一个 compatibility runtime 副本若可直接路由到 canonical 实现，就不应长期维护第二份独立代码；路径兼容和真值唯一可以同时成立。
16. core 换代后必须让 direction→core 主题通过当前 manifest 集合校验；只更新主要结果行仍可能留下一个旧标签，负向 validator 应使这种残留 fail closed。
