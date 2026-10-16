# PDF → Markdown 转换批次（2026-09-14）

本目录是 `LIT-CLASSICS-001` 及其直接机器化对照的统一转换入口。现有 16 个 `.pdf` 均已通过 PDF magic、页数和 SHA-256 检查；目录中没有把网页响应误命名成 PDF 的文件。首批 12 个内容组、补充批次 3 个内容组与 Rosser 1936 原文共 16 个不同内容组，均已有 MinerU 转换。

## 转换输出约定

1. 每个 PDF 生成一个同 basename 的 Markdown，例如 `Turing-1936-On-Computable-Numbers.pdf` → `Turing-1936-On-Computable-Numbers.md`。
2. Markdown 直接放在本目录，不覆盖或移动 PDF。
3. 使用 UTF-8；保留原始标题、章节、定理／引理编号、脚注、参考文献和表格。
4. 每页边界尽量写成 `<!-- page: 1 -->`、`<!-- page: 2 -->`；页码以 PDF 页序为准，可另外保留印刷页码。
5. 数学公式尽量保留为 LaTeX；无法可靠识别的局部用 `[OCR_UNCERTAIN: ...]` 标注，不凭上下文补造。
6. 扫描页或版式复杂页可以嵌入页图引用，但不要省略其可读文字。

## 已就绪文件

| 文件 | PDF 页数 | bytes | SHA-256 | 研究角色 |
|---|---:|---:|---|---|
| `Turing-1936-On-Computable-Numbers.pdf` | 38 | 339421 | `b88da293ad7965c53c2726c19cf3fe68c549a1202cfd6d1a79224890f11b627d` | 自动机、circle-free、universal machine、对角与 Entscheidungsproblem |
| `Church-1936-Unsolvable-Problem.pdf` | 20 | 920839 | `d5c7e12252d07bb07f1e5ceee1786008fc9cb0849778d6a585f092da35199323` | 有效可计算、λ-definability、一般递归与不可解性 |
| `Godel-1931-Unentscheidbare-Saetze.pdf` | 26 | 1431327 | `49e3116e2fea8026c7744976e5d4abb8fb08c381229c5f6164da5d73668d9b05` | 语法／证明算术化、表示性、对角与第一／第二不完备性 |
| `Rosser-1936-Extensions.pdf` | 6 | 538312 | `72a53b2c765df55b921b1d08ea584c76021af60aa2034ac3210e6697005bbb2a` | Rosser 1936 原文；第 1 页 JSTOR 封面，第 2–6 页为印刷页 87–91；simple consistency、证明比较与 Theorems I–V |
| `Kleene-1938-Ordinal-Notation.pdf` | 7 | 238353 | `4f08a85898e5642b92eff3337174675f970d0a9bca0a8c1b701bd92d53601d45` | 第二递归定理的原始短文；程序索引、自应用与计算定点 |
| `Rice-1953-RE-Classes.pdf` | 9 | 799682 | `9ac76ec7e30cd84512acea6b00f32cc9c46e1e25506323e6329eede22af43f34` | r.e. 集类别及非平凡语义性质的决定边界 |
| `Lob-1955-Henkin.pdf` | 5 | 303294 | `5f7b69331c8e83d56fc88c19e925e040701795ef4486e218cc38255a670b3c86` | 可证性、自担保命题与导出条件 |
| `Lawvere-1969-Diagonal.pdf` | 14 | 134978 | `65ae0958cb0f6350da05499f9d772732111338315c794fcb8aae37052b5f3897` | point-surjectivity、CCC 与定点／对角模式 |
| `OConnor-2005-Essential-Incompleteness-paper.pdf` | 17 | 188561 | `d5acae99fa9a5a55e041c99af50829225498083b134cdf2a10ca68fd367d9610` | Coq 中数值编码、表示性与 Gödel–Rosser |
| `OConnor-2005-Essential-Incompleteness-slides.pdf` | 28 | 932441 | `af5a5ccdbf83aa0030e9c2c77dacbcb0b3949d506207f9dc7d4559b4ef52a79f` | 同项目演示与工程边界对照 |
| `Kirst-Hermes-2021-Synthetic-Undecidability.pdf` | 20 | 801450 | `b5738da6699457c88a9040baf022ad4b750260bbbc8def2e6c3df4422e302d8a` | synthetic reductions、axiom systems 与机器化不完备性 |
| `Kirst-Peters-2023-Godel-Without-Tears.pdf` | 18 | 749481 | `422aa3f3aa6ee7d6721c029560d156fe86e34e96144ced5a68e495feea7231bf` | EPF、strong separation、self-return 与 synthetic essential incompleteness |
| `Annenkov-Capriotti-Kraus-Sattler-2017-2LTT.pdf` | 58 | 1100607 | `ac2a753e2e2e923d1aad19d324032299591b7d41504cfc289db65369a9fa958a` | inner HoTT／outer strict metatheory 与内部语法边界 |
| `Swan-Uemura-2019-Church-Thesis-Cubical-Assemblies.pdf` | 23 | 291460 | `417e713e4a4a2e9353d892551e52453c3e603f3b6b3e9340ca52cec41750fff0` | Church thesis、cubical assemblies、反射子宇宙与 univalence 适用域 |
| `Peter-Smith-Expounding-First-Incompleteness.pdf` | 33 | 391792 | `4ce2eebc1a2280f1169b4c09747afb94e691d8915cdb77edee7a504c4299bd1a` | 后世历史说明；§7 重构 Rosser proof-code comparison 与 consistency-only 路线，不是 Rosser 1936 原文 |
| `Peters-2022-Godel-Without-Tears-Bachelors-Thesis.pdf` | 48 | 710984 | `d186581905329d182d361dee3ab61ced9e1bc2b23778f43aab763dc7817dbeed` | Peters 机器化工作的学士论文长版；对 Rosser 1936 是后世说明 |

## 尚待取得有效 PDF

以下一项已经定位一手书目信息和正文入口，但当前本机尚未取得可作为对应原文正文的有效 PDF：

| 文献 | DOI／入口 | 当前状态 |
|---|---|---|
| Post, *Recursively Enumerable Sets of Positive Integers and Their Decision Problems* (1944) | DOI `10.1090/S0002-9904-1944-08111-1` | AMS 开放 PDF 已定位；当前响应为访问验证页 |

取得并验证 Post 后，会以 `Post-1944-RE-Sets.pdf` 加入同一目录。`Rosser-1936-Extensions.pdf` 现已占用 Rosser 原文身份；`Peter-Smith-Expounding-First-Incompleteness.pdf` 与 `Peters-2022-Godel-Without-Tears-Bachelors-Thesis.pdf` 保持其后世说明身份。

## MinerU 导入收据

用户给出的首批 12 个 MinerU 内容组已导入 `../LIT-CLASSICS-001/mineru/`：584 个文件、15,978,067 bytes、树 SHA-256 `cea1d6499750fbad9459aa710e0a1be8eaaf6fc86478f52fdb23ea37f0533853`，`scripts/audit/import_lit_classics_mineru.py --verify-only` 返回 `VALID`。

补充的 3 个内容组已导入 `../LIT-CLASSICS-001/mineru-supplement/`：130 个文件、3,618,881 bytes、树 SHA-256 `3109f828c6a4e0e60a1267c9851e0995eded00b8c7207dda7e23a45cde4dea14`。`RECEIPT.json` 是常规水合入口，以 bytes/SHA-256 绑定完整逐文件 `IMPORT.json`；后者扫描了 2026-09-14 的 41 个 MinerU 目录，并按 Markdown、正规化 PDF、页结构和引用图片的完整 bytes/SHA-256 归并为 15 个内容组：12 个已在首批导入，3 个进入补充导入，26 个目录是内容重复解析，0 个内容组未分类。所有 MinerU 源目录均保留，未执行删除。

Rosser primary 另由 `../LIT-CLASSICS-001/mineru-rosser-primary/` 保存：原始下载 PDF 538,312 bytes / SHA-256 `72a53b2c…`，MinerU 正规化 origin 539,387 bytes / SHA-256 `a7d3020c…`，导入树 10 files / 705,621 bytes / SHA-256 `3198764e…`。42 个当日 MinerU 目录现归并为 16 个不同内容组；新增 Rosser 组只有一个成员，既有 26 个重复目录仍全部保留。原文身份由题名、作者、卷期、印刷页 87–91、首尾与全部 6 个 PDF 页的视觉核对共同支持；定理仍是 `SOURCE_REPORTED_NOT_REPLAYED`。

三批 MinerU `origin.pdf` 都是正规化派生文件，不能用其哈希替代项目输入 PDF 身份；两套身份已分别保存。复核命令：

```bash
python3 -B scripts/audit/import_lit_classics_mineru.py --verify-only
python3 -B scripts/audit/import_lit_classics_mineru_supplement.py --verify-only
python3 -B scripts/audit/import_lit_classics_rosser_primary.py --verify-only
```
