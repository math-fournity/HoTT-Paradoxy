# R032 来源与使用范围

## 项目内依据（已存在，不是本轮新增结论）
- `.codex/research/hott/reviews/SELF-REFERENCE-003/PROOF_NOTE.md`、`PLAN.md`：R031条件Löb与当前受限解释任务。
- `.codex/research/hott/reviews/SELF-REFERENCE-002/PROOF_NOTE.md`：R030旧评价器/新语言覆盖区分（本轮沿用记录身份，不重认证）。
- `HoTT/THEORY_SCHEMA.md`：框架索引，不是本轮完整元理论证明。
- `HoTT/theory-schema/upstream/book-578b85cc/formal.tex`：变量、Π、空类型、结构归纳、替换/弱化的理论规则。
- 当前第五闭包、三问、AGENTS、治理Skill、业务Skill和动态工作记忆：恢复问题身份，保留原双向目标、ASK、脚本先落盘、本地Git要求。全文读取不等于理解正确；读取后实际发生压缩，动态全集未完整装入。

## 外部一手回查（本轮实际使用web工具）
1. 固定版HoTT Book正式附录：
   https://raw.githubusercontent.com/HoTT/book/578b85cc8d586b1677ec4335148adeb443057d24/formal.tex
   用途：共享类型形成/解释以及结构规则的依据。不是所有依赖HoTT元理论都已内化的证据。
2. Agda官方Reflection，页面标记2.8.0：
   https://agda.readthedocs.io/en/stable/language/reflection.html
   用途：TC的上下文、检查和unquote接口；宏类型/目标hole与--safe下postulate限制。回查范围为接口文档；没有执行宏，没有审计全部实现。
3. Shulman，2014-03-03，HoTT should eat itself：
   https://homotopytypetheory.org/2014/03/03/hott-should-eat-itself/
   用途：历史真实自元理论问题及依赖替换相干与简单归纳语法的区别。不将2014研究状态说成2026的全部最新状态。

## 本轮自行推导与实现
- 桥接证书⇄全部保公式迁移（两个蕴含，不认领数据类型等价）。
- proof-producing扩展的保守展开、结构解释和used-support充分性。
- 源目标环境各自相容的旧标记失配反例；支持集并非所有替代证明必要条件。
这些是明确小片段的标准推导方法与应用，不声称原创或已在原生HoTT内核中验证。

没有新的Gemini来信，也没有发送新信或启动其他AI。自动显示的旧Gemini附件不是本轮任务的替代依据。
