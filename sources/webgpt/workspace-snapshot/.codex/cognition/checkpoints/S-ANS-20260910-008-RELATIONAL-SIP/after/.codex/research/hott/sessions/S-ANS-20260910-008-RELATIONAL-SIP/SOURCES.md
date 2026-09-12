# 本轮来源与范围

读取日期：2026-09-10。精确范围而非全领域排查。

## S01 固定HoTT Book本地原文
`HoTT/theory-schema/upstream/book-578b85cc/categories.tex`
SHA256 `141332f0b27d5ab055419e02bada9664561758d129ebe4d52e43bb8e290b275f`，1854行，108084字节。
本轮定位并读§9.1同构/idtoiso相关段（含88—177行）与§9.8全节1205—1363行。
重点：1277—1284明确同时要求H(f)和H(f⁻¹)，1325—1328仅把关系的正向蕴涵作为一般homomorphism要求。
编号副本见SOURCE_EXCERPTS.md，原文件未改。

## S02 作者公开说明（实际web读取）
https://homotopytypetheory.org/2012/09/23/isomorphism-implies-equality/
Nils Anders Danielsson，2012-09-23，叙述与Thierry Coquand的结果。
本轮读取其主文结构代码和同构定义；主文的编码由运算与命题公理组成。
只用来解释为何代数运算的同态双射可作同构，不将其泛化成全部关系同态。不以评论或历史日期证明目前全部代码正确。

## S03 §9.8公开转录对照
https://planetmath.org/98thestructureidentityprinciple
本轮网页检索返回该节完整核心证明文字；与本地S01关于逆同态条件一致。
这是书的转载对照而非本轮使用的独立研究证据；决定性源为S01，不依赖其他二手释义。
未作远端全文字节校验、没有下载完整PDF。

## 远端访问失败
https://raw.githubusercontent.com/HoTT/book/578b85cc8d586b1677ec4335148adeb443057d24/categories.tex
web返回Cache miss。
https://github.com/HoTT/book/blob/578b85cc8d586b1677ec4335148adeb443057d24/categories.tex
web返回Internal Error。
这不影响本地固定源可读，但不能称远端获取成功。
搜索也返回其它关系/结构主义论文；没有据其标题或摘要推出标准HoTT库错误。

## S04 前轮实质记录
`.codex/research/hott/sessions/S-ANS-20260910-007-CAUSAL-EQUIVALENCES/PROOF_NOTE.md`
本轮直接复读其判据、Nat例、二进制流正向对照和所选下一接口。
只继承其待复核状态；未重新运行旧代码，不将R001旧实验当证据。
Book基础运输回源文件 `HoTT/theory-schema/upstream/book-578b85cc/basics.tex` SHA256 `516b469d7356e9d20df5539e726a0468760f9fa7b7f440b9c054981e803d7533`，本轮不称重新全读该2699行正文；只在既有来源身份下使用前述原始规则。

## 新结果身份
PROOF_NOTE§3—7均有独立公开推导；一般关系等价、结构identity、有限协议与查询类是标准材料的本轮组织/特例，未做穷尽新颖性排查。
局部代码只作有限sanity，并非HoTT机器形式化。
