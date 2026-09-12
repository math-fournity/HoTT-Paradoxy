# R019 来源与使用范围

## 被审材料

原始 HoTT-2(1).json 599415 bytes，SHA256 c2da542fdcc7b7a691242d991c21f7778c5c0ecda7e9a26cb2ab598dbab5ed27。23段公开文字、17段Python代码及17份结果、两段Lean围栏、两份base64脚本附件已定位；13个thought块只记录身份，不作公开证明。所有parts重复去重，不把签名当认证。外部Drive只含ID，无正文。

原文件说什么由 PUBLIC_TRANSCRIPT / 原JSON / 代码和原结果决定；本轮诊断是另行审计证据，不替原作者补证明。

## 固定项目原规则

HoTT/theory-schema/upstream/book-578b85cc/{logic,formal,basics,hits}.tex，范围及整文件SHA见 SOURCE_EXCERPTS.md / SOURCE_IDENTITIES.json。只回查本论证实际依赖，不声称通读核验整个HoTT。

## 实际联网回查的一手来源（2026-09-10）

1. HoTT Book 作者仓库 logic.tex： https://raw.githubusercontent.com/HoTT/book/master/logic.tex 。在线正文核对唯一选择/排中律，具体本地行号以固定项目版本为准；远端master不是固定快照。
2. HoTT Book 作者仓库 formal.tex： https://raw.githubusercontent.com/HoTT/book/master/formal.tex 。核对公理呈现与判断等式说明。
3. Lean 官方 Theorem Proving in Lean 4, Propositions and Proofs： https://lean-lang.org/theorem_proving_in_lean4/Propositions-and-Proofs/ 。实际查看 proof irrelevance 与 axiom 的意义。只支持宿主Lean规则，不是已编译本稿的证据。
4. Lean 官方 Axioms and Computation： https://lean-lang.org/theorem_proving_in_lean4/Axioms-and-Computation/ 。区分内核归约、编译执行与choice产生非计算数据；商递归也有明确计算规格。
5. Cohen/Coquand/Huber/Mörtberg, Cubical Type Theory: a constructive interpretation of the univalence axiom： https://arxiv.org/abs/1611.02108 。读取作者/摘要/版本信息；只用于该系统有构造性单价解释，不声称全文重证。
6. Huber, Canonicity for Cubical Type Theory： https://arxiv.org/abs/1607.04156 （v2，2017-10-30）。读取摘要及版本范围；其自然数规范性针对指定系统，不推广所有扩展。
7. Hossenfelder, Minimal Length Scale Scenarios for Quantum Gravity： https://arxiv.org/abs/1203.6191 。摘要级背景对照：最小尺度是多种方案的研究问题；没有由“量子”一词证明固定离散时空或最小瞬移。

本轮没有下载或分析PDF图页，没有调用远端仓库连接器改变任何内容；上述材料均为公开一手文档/作者论文。没有声称跨来源全部表述完全等同。

## 原生工具与独立复核

TOOLCHAIN_STATUS.json实测本机未找到lean/lake/elan/agda/coqc。未安装依赖，未编译两段Lean。纸笔反证和软件缺陷诊断不冒充内核认证。没有其它AI、独立Fresh Session或物理实验。
