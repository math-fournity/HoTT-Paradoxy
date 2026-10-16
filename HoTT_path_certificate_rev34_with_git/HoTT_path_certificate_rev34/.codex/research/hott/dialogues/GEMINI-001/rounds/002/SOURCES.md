# 本轮来源与证据分层

## 直接材料

S1 `../../000_SOURCE.md`：用户首次提供的完整Markdown；与当前挂载的Pasted markdown(1).md逐字节一致。S1a `../../005_GEMINI_ORIGINAL.md`是原始精确切片。
S2 `IN-002.md`：本轮转述回复；由`USER_MESSAGE.md`的四反引号边界间切片，保留空行。源消息手工转录可见正文，不冒报平台原始字节签名。修正全部写在ASSESSMENT/CONSTRUCTION，不回写源文。
S3 `../../TO_GEMINI_001.md`：我方首封信。IN-002声称已读；未直接验证发送渠道。
S4 本轮用户附言：配额已不足，要求综合并落盘。当前采用自主推进，不等待或模拟回信。

## 实際核对的一手来源

L1 锁定HoTT Book commit 578b85cc8d586b1677ec4335148adeb443057d24，logic.tex第358—418、797—839行：命题LEM／唯一选择。L2 basics.tex第1626—1654、1738—1785行：函数族运输、单价性与命题计算。L3 formal.tex第978—1015、1172—1192行：所选公理化呈现。精确字节和摘录在`artifacts/r021/SOURCE_IDENTITIES.json`、`SOURCE_EXCERPTS.md`。

W01 作者库master逻辑正文：https://raw.githubusercontent.com/HoTT/book/master/logic.tex 。web实际读取；和本地锁定版本分别标识，没有静默替换。固定hash URL的web请求返回cache miss，故固定证据仍以项目文件为准。
W02 Lean官方Modifiers：https://lean-lang.org/doc/reference/latest/Definitions/Modifiers/ 。web实际读取第68、122行；用于编译修饰符范围，不是全系统可靠性证明。
W03 Lean官方implemented_by：https://lean-lang.org/doc/api/Lean/Compiler/ImplementedByAttr.html 。web实际读取；编译器可使用替代实现，逻辑检查与运行实现的关系需要独立核验，尤其native调用情形。
W04 Rocq 9.0.1提取手册：https://rocq-prover.org/doc/v9.0/refman/addendum/extraction.html 。读取“Realizing axioms”；用户提供的ML实现不是自动证明其语义正确。没有执行提取命令，也未判定任何具体库错误。
W05 Simon Huber, Canonicity for Cubical Type Theory, arXiv:1607.04156v2：https://arxiv.org/abs/1607.04156 。只读摘要与版本元数据；结论针对其明确系统和名字变量上下文中的自然数，不是全部HoTT。没有分析PDF或重新核验正文证明。

## 限制

本輪的容器下载脚本全部遭遇DNS解析失败。web页面能够读取，不等于完整远端字节已下载。`artifacts/r021/web/MANIFEST.json`保留五次真实失败；本页是依据web工具结果写出的来源/阅读说明，不是远端完整快照。

没有新外部AI调用、库扫描、证明助手、物理验证或数学模拟器运行。第一轮的旧数值修辞、关于统一悖论的断言只作为来源保存，不构成事实依据。
