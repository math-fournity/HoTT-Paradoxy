# mineru_md — MinerU 0.14.1 App 解析产物

9 份罗素考古工作包所需文献 PDF 经本地 MinerU 0.14.1 桌面 App
（`/Applications/MinerU.app`，本地 Torch 后端）解析得到的
`full.md`（Markdown 含 MinerU 渲染的页/段/表/公式结构）落地。

> 派生说明：`full.md` 是 MinerU 的派生阅读副本；做事实/页/图核查时
> 必须回原 PDF 页面（`../_upload/<name>.pdf`）。本目录的 SHA-256 与字节
> 记录在 `完整性证书-20261017.md`，并随同本轮工作回 Git 跟踪。

## 命名映射

源 PDF（`../_upload/`，本任务清单的 9 份） → 解析产物（本目录）：

| 源 PDF                                            | 解析产物                              | full.md 字节  | 用途                                |
| ------------------------------------------------ | ----------------------------------- | -----------: | --------------------------------- |
| `zermelo1908-pp261-281.pdf`                      | `zermelo1908-pp261-281.md`          |       56,278 | Q1 Zermelo 1908 原文 OCR（页 261–281）             |
| `rieger-foundation.pdf`                          | `rieger-foundation.md`              |       44,196 | Q3/Q4 Rieger 论正则公理与限制过度（23 页）         |
| `probe-mineru-test.pdf`                          | `probe-mineru-test.md`              |        2,075 | MinerU App 探针（单页图像 1200×1820，VLM 标注）  |
| `probe-clean.pdf`                                | `probe-clean.md`                    |        2,075 | MinerU App 探针（单页图像 2000×3034，VLM 标注）  |
| `kanamori.pdf`                                   | `kanamori.md`                       |       78,941 | Kanamori 32 页 A4 文献（Kunen 1980 之后基础）   |
| `kunen1980_part01_p001-163.pdf`                  | `kunen1980_part01_p001-163.md`      |      425,481 | Kunen 1980 Set Theory 第 1–163 页      |
| `kunen1980_part02_p164-325.pdf`                  | `kunen1980_part02_p164-325.md`      |      474,139 | Kunen 1980 Set Theory 第 164–325 页     |
| `enderton1977_part01_p001-150.pdf`               | `enderton1977_part01_p001-150.md`   |      300,441 | Enderton 1977 Elements of Set Theory 第 1–150 页 |
| `enderton1977_part02_p151-289.pdf`               | `enderton1977_part02_p151-289.md`   |      325,776 | Enderton 1977 Elements of Set Theory 第 151–289 页 |

合计 1,709,402 bytes（≈ 1.71 MB）Markdown。

## 限制与已知现象

- `probe-*.pdf` 是单页大幅面图像 PDF，full.md 仅含 VLM 识别出的图注/标题/
  文字块（约 2 KB），不是正文提取。`probe-clean.pdf` 与 `probe-mineru-test.pdf`
  的尺寸/清晰度不同（2000×3034 / 1200×1820），用做"同一文档不同清晰度对 VLM
  识别的影响"对照。
- `zermelo1908-pp261-281.pdf` 已按 200 页上限拆为 1 份（21 页），但 MinerU
  仍能在单次任务内处理；其余 200 页以上的 PDF（enderton1977 / kunen1980）
  按工作包 `_split/` 拆分规则切到 ≤ 200 页再送入。
- 所有产物均由 MinerU 本地默认后端产出；`full.md` 是含图像占位符的 Markdown，
  文本块可读、公式经 MinerU 排版提取后形式（`$...$` 风格）。

## 关联

- 上游 PDF（来源原件）：`../_upload/`（与 `../_split/` 互为同一来源的不同切分）
- 上游任务包：仓库根 `dev` 分支；本轮入口为本目录的"00-/01-/03-交接文档"
  + "搜索完整性证书-20261017.md"
- 工作记录与 Git：见仓库 `git log` 提交（含本目录与证书）
