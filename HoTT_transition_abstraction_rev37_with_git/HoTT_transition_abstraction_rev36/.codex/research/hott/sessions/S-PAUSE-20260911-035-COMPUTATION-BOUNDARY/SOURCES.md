# R035 来源与范围

## 本地完整回读的核心依据

- `AGENTS.md`、两类 Skills、角色表、LOAD_SET、治理协议、README、MEMORY、FRONTIER、RESUME。
- `HoTT/INTRINSIC_TEMPORALITY_OF_HOTT.md`：全文376行，分块补读；对象、归约、强时态与物理时间分层。初次聚合显示含截断，后续补读完整；不宣称全动态集合已读。
- `reviews/SELF-REFERENCE-003/PROOF_NOTE.md`：R031全文，条件 Löb 与局部证书/反射范围。
- `reviews/SELF-REFERENCE-006/PROOF_NOTE.md`：R034全文，有限证书与无统一 MereMove 的范围。
- 其余轮次通过最新MEMORY、原记录索引与既有会话定位，不冒称本次重新读遍或复现。

## 外部核查（2026-09-11，通过 web 浏览；非论文全文/内核运行）

S1. HoTT Book 项目页及作者原始 Introduction：
https://homotopytypetheory.org/book/
https://raw.githubusercontent.com/HoTT/book/master/introduction.tex
支持 HoTT 与同伦、类型论、逻辑与计算的关系。不是物理实在理论，也不是全部历史悖论覆盖证明。

S2. HoTT Book Appendix / formal.tex：
https://raw.githubusercontent.com/HoTT/book/master/formal.tex
核查基础归约、结构递归、规范性与扩展范围的分别说明。书中历史开放问题不当成2026年当前全领域状态。

S3. Jonathan Sterling, Carlo Angiuli, Normalization for Cubical Type Theory, arXiv:2101.11479v2 / LICS 2021：
https://arxiv.org/abs/2101.11479
本次读取摘要：一个明确的单价Cartesian cubical系统的规范化与判断相等可判定。未读/下载PDF，不称全文审查，不认证所有HoTT变体。

S4. Universal Turing Machine, Archive of Formal Proofs：
https://isa-afp.org/entries/Universal_Turing_Machine.html
本次读项目摘要和范围，用于通用机器模型的停机不可判定/递归函数区分。没有本地回跑Isabelle。

S5. An Abstract Formalization of Gödel's Incompleteness Theorems：
https://isa-afp.org/entries/Goedel_Incompleteness.html
https://isa-afp.org/thys/Goedel_Incompleteness/Loeb.html
核查条件化表述及明确编码/推导前提；不是本项目完整HoTT实例的证明。

S6. Cubical Type Theory: a constructive interpretation of the univalence axiom, arXiv:1611.02108：
https://arxiv.org/abs/1611.02108
摘要用于区分书式公理和计算型单价解释，不宣称全部闭项全呈现都有相同求值。

S7. Guarded Dependent Type Theory with Coinductive Types, arXiv:1601.01586：
https://arxiv.org/abs/1601.01586
摘要用于辨别 later/clock 等额外结构与裸HoTT，不把不同系统的性质合并。

只作有界事实核查；没有新增工具执行结果、原创定理或现实桥梁证据。
