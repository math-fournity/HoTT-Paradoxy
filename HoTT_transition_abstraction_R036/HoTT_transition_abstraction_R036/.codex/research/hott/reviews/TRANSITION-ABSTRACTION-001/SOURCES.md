# R036 来源与使用范围

## 当前任务与继承资料
R035/REQUEST.md、ASSESSMENT.md：用户暂停及“逻辑＋几何＋程序／共享界限”的怀疑与助手评估，逐字保留并纳入第五闭包§22。
R036/REQUEST.md：当前恢复与治理对齐授权。
R014/PROOF_NOTE.md：已全文回查，不把本轮重新写成Done擦除或黑箱无限流。
R034/PROOF_NOTE.md：已回查，统一MereMove障碍保持原状态，不在本轮重证。
三问、第五闭包、AGENTS、业务Skill及时间owner：当前owner对齐，不变更既有加载引擎或原用户文稿。

## 一手规则
锁定HoTT Book commit 578b85cc8d586b1677ec4335148adeb443057d24：
- HoTT/theory-schema/upstream/book-578b85cc/logic.tex：命题截断、消去至命题与唯一选择；本轮用来说明关系像和等级下降的合法消去。
- HoTT/theory-schema/upstream/book-578b85cc/hits.tex §6.10：集合商；本轮可用显式二元素归纳类型呈现该有限商，不要求完整商实现。
- 公开读取hits.tex成功；同commit的logic.tex一次web cache miss，规则回到已提供本地固定源码，不将失败的web请求当成功。

## 机制比较（不是本文证明的替代）
1. Thomas Ball. Formalizing Counterexample-driven Refinement with Weakest Preconditions. MSR-TR-2004-134, December 2004.
https://www.microsoft.com/en-us/research/publication/formalizing-counterexample-driven-refinement-with-weakest-preconditions/
仅使用其对过近似和虚假反例问题的说明；网页摘要一处refinement句子疑有笔误，不据此推导。
2. GaHee Fan and Robert C. Holte. The Spurious Path Problem in Abstraction. SOCS proceedings article.
https://ojs.aaai.org/index.php/SOCS/article/view/18356
检索到摘要说明spurious paths可以并不伴随spurious states；年份未作为本轮结论前提，不混用网页迁移日期与论文历史年份。

本轮没有读取PDF、没有OCR，没有原生证明助手运行，没有外部专家或其它AI调用。所有新代码保存到scripts后才调用。
