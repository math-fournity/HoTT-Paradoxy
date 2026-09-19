# 外部一手来源的精确消费位置

资产：HUMAN_EDITED。唯一 owner：本次 Astra 审计；只登记引用身份与实际消费范围。读取日期：2026-09-19。本表不是完整相关工作审计，也不将论文结果提升为本 repo 已重放定理。

| ID | 精确来源/版本 | 可直接查找的位置 | 本报告使用的内容 | 证据等级与限制 |
|---|---|---|---|---|
| E01 | Simon Huber，[Canonicity for Cubical Type Theory，arXiv:1607.04156v2](https://arxiv.org/abs/1607.04156v2)，2017-10-30 | Abstract；关键词 `only name variables`、`judgmentally equal to a numeral`；Comments 说明 v2 增加 propositional truncation | 论文陈述的演算/上下文范围 | SOURCE_REPORTED_NOT_REPLAYED；核对摘要与版本，不称证明全文已重放 |
| E02 | Coquand–Huber–Sattler，[arXiv:1902.06572v6](https://arxiv.org/abs/1902.06572v6)，2022-02-02；早期 [v1](https://arxiv.org/abs/1902.06572v1) 题名为 Homotopy canonicity for cubical type theory | 版本页、Abstract；v1 用 `path equal to a numeral` 描述 homotopy canonicity；v6 题名 Canonicity and homotopy canonicity for cubical type theory | 为区分两种 canonicity 提供相关工作入口 | REFERENCE_ENTRY / 摘要定位；没有将任一版本的定理直接套到本机全部选项 |
| E03 | de Jong–Escardó，[On Small Types in Univalent Foundations，arXiv:2111.00482v5](https://arxiv.org/abs/2111.00482v5)，2023-05-03；LMCS 19(2:8) | Abstract 中完整偏序、小型性、weak/full propositional resizing 的陈述；定位短语 `nontrivial`、`positivity` | 说明小型性与 resizing 已有精确研究传统 | 摘要级来源转述；不是当前 `Necessity` 的现成证明或反例 |
| E04 | de Jong–Escardó，[Examples and counterexamples of injective types，arXiv:2601.12536v2](https://arxiv.org/abs/2601.12536v2)，2026-09-04 | Abstract 含 `Dedekind reals`、`injectivity`、`weak excluded middle` 的段落 | 指明2026年相关工作的具体主题与前提 | 摘要级来源；injectivity 不等于本项目的 `ℝLayerAt`，未外推 |
| E05 | Escardó，[Introduction to Homotopy Type Theory and Univalent Foundations with Agda](https://martinescardo.github.io/HoTT-UF-in-Agda-Lecture-Notes/HoTT-UF-Agda.pdf)；原报告的[作者大学站副本](https://www.cs.bham.ac.uk/~mhe/HoTT-UF-in-Agda-Lecture-Notes/HoTT-UF-Agda.pdf) | 在 PDF 文本中查精确符号 `PR-gives-impredicativity⁺`、`PR-gives-impredicativity₁`、`Impredicativity-gives-PR` | 只定位 pointwise resizing、Ω 小型性及底层/后继宇宙区别的参考段 | 检索片段/符号定位；PDF URL 可变化，未保存或认证整份 PDF SHA，未重放对应 Agda 源；不要当作本包关系已证明 |
| E06 | [Agda 2.8.0：Postulates](https://agda.readthedocs.io/en/v2.8.0/language/postulates.html) | 页首定义段；Safe Agda 段；`Postulated built-ins` 小节 | 普通 postulate 没有定义、safe 禁止普通公设；内建特殊处理另列 | 官方版本文档说明，不替代本机源码/运行 |
| E07 | [Agda 2.8.0：Cubical](https://agda.readthedocs.io/en/v2.8.0/language/cubical.html) | 页首 Cubical mode 与 CCHM variation 说明；功能表；后续 Univalence、Cubical identity types | 本实现有原生计算性 univalence/HIT，不能将额外不透明 ua 常量等同其全部计算合同 | 官方文档层；不认证所有扩展的一致性或 canonicity |

HoTT Book 的决定性原文优先使用 repo 内 `logic.tex` 与 `reals.tex`。其上游身份为 `578b85cc8d586b1677ec4335148adeb443057d24`，来源说明在 `HoTT/theory-schema/upstream/README.md`，原始文件哈希在 `HoTT/theory-schema/SOURCES_AND_COVERAGE.md` 第39/45行。每个审计分片已给出相关定义的精确物理行；本次来源快照另保存实际 SHA 和当前 Git blob。

外部网页没有伪造本地文件哈希。E01–E04 有版本化 arXiv ID，E06–E07 固定文档版本；E05 保持“未锁定全文”的明确限制。后续若要依赖它们证明新的命题，必须加载所需正文、假设和对应机器证据。
