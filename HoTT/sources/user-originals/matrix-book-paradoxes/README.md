# 《宇宙编程学》第三版悖论原文资产

资产身份：`USER_PRIMARY_SOURCE_DERIVED_VERBATIM_VIEW`

Schema：`matrix-book-paradox-extract/v1`

唯一 manager：`../../../tools/matrix_book_paradox_extract.py`

外部源：

`/Users/aurolafly/MinerU/The Art of The Matrix 宇宙编程学 —— 世界与意识、悖论与时空（第三版）.doc-49840494-168f-45cd-997a-0b1e891c222f/MinerU_markdown_202609010456973_03d86f36.md`

当前源身份：297,569 bytes、5,683 logical lines、SHA-256
`24530b89725d4043a7a5292a403ab50d48feed5417351c348790150726ae9409`。

本轮调查开始时同一路径曾为 299,836 bytes、5,758 logical lines、SHA
`62cef54875fbc0e654b71c9e17895381f4529cddde6ad3a3a7d96f31032affe2`，随后外部文件在
`2026-09-01T11:37:19-0400` 被改写。manager 对当前 SHA fail-closed；旧行号不得冒充当前来源。

## 为什么单独建立

原书同时讨论 Russell、Better Best、说谎者、计算合法性、芝诺、shenchensh 平行线转动、稠密/
非稠密空间解答、理论抽象的工具性及“悖论必然性”总论。未来 AI 若每次通读 5,758 行，会增加
遗漏和上下文成本；只写 AI 摘要又会丢失用户原话。因此本目录保存：

1. 完整 MinerU Markdown 原字节快照；
2. 源目录中全部 84 张图片，保证独立文档图像可读；当前 Markdown 引用其中 83 张，另 1 张是
   被改写前书首作者简介使用的源图，作为 MinerU 源资产保留；
3. 按自然问题/解答链形成的 10 份连续逐字原文；
4. 每份来源行区间、源 SHA、逐字 SHA、角色和主题；
5. 显式悖论族词项覆盖及书名/目录/致谢等非正文排除收据。

这些资产证明用户原作怎样提出和解答问题，不自动证明其中关于集合存在、程序停机、连续时空、
普朗克尺度、欧氏/非欧几何、相对论或宇宙结构的结论正确。当前数学裁决仍回到认知闭包、Z owner、
主张矩阵和未来的具体形式化。

## 目录结构

```text
matrix-book-paradoxes/
├── README.md
├── CURRENT
└── generations/<generation-id>/
    ├── INDEX.md
    ├── MANIFEST.json
    ├── 宇宙编程学第三版-MinerU全文原文.md
    ├── 00-...md 至 10-...md
    └── images/                     # 84 张源图
```

Generation 由 schema、manager、外部源 SHA、抽取范围、排除范围和全部图片 SHA 决定。build 使用临时
目录、排他 lock 和原子 `CURRENT` 更新；旧 generation 默认保留，不得手改 machine-managed 产物。

## 抽取单位

| ID | 自然单元 | 源行 |
|---|---|---:|
| MP-01 | 悖论研究缘起与总体路线 | 176–358 |
| MP-02 | 被推演世界中的离散时空前提 | 804–896 |
| MP-03 | 罗素悖论与假集合 | 3570–3626 |
| MP-04 | Better Best、说谎者、计算合法性与芝诺 | 3627–3939 |
| MP-05 | shenchensh 平行线转动悖论原始发难 | 3941–4001 |
| MP-06 | shenchensh：圆型体与稠密空间方案 | 4202–4872 |
| MP-07 | shenchensh：非稠密离散时空方案 | 4873–5175 |
| MP-08 | 芝诺与 shenchensh 的前提否定总结 | 5176–5212 |
| MP-09 | 理论抽象的工具性与悖论必然性 | 5213–5369 |
| MP-10 | 悖论研究后记综合 | 5472–5544 |

MP-04 与已有 `../Better-Best悖论-原文.md` 内容等价，但来源身份不同：已有文件保存早期 attachment
原字节；MP-04 保存本书 MinerU 快照中的连续行。manager 会校验二者仅相差 MinerU 导航 anchor 和
末尾空白，不能覆盖任一来源。

## 命令

从 repo 根执行：

```bash
# 只读查看预期 generation、图片和显式命中覆盖
python3 HoTT/tools/matrix_book_paradox_extract.py scan

# 完整计算但不写
python3 HoTT/tools/matrix_book_paradox_extract.py build --dry-run

# 生成 immutable generation
python3 HoTT/tools/matrix_book_paradox_extract.py build

# 从外部源重新核验全文、全部图片、所有逐字行片段、覆盖和孤儿文件
python3 HoTT/tools/matrix_book_paradox_extract.py validate

# 查看当前统计
python3 HoTT/tools/matrix_book_paradox_extract.py stats
```

## 覆盖与盲区

显式覆盖词表包括 `悖论/paradox`、Russell、说谎者、芝诺、shenchensh、Better Best、假集合、
平行线转动和停机等。书名、目录和致谢中的命中单独登记为 navigation/incidental，不做正文摘录。

此外，MP-02、MP-06、MP-07、MP-09 等范围是根据目录和完整解答链人工加入，不依赖某一行是否出现
“悖论”二字。Validator 要求显式词项 `uncovered=0`，但这仍不能证明书中每个未使用这些词的潜在
悖论或哲学矛盾都被语义穷尽；负结论必须按新问题扩大搜索。

## 编辑和证据纪律

- `generations/`、`CURRENT` 禁止手改；源或 manager 改变后建立新 generation。
- 每份独立文档的 `BEGIN VERBATIM` 至 `END VERBATIM` 是连续源字节，header/footer 不属于原文。
- 图片逐字节复制并校验 SHA；所有本地图片引用必须可解析。
- `USER_SOURCE_UNREVIEWED_CLAIMS` 不因“用户原作”身份升级为数学或物理真理。
- AI 的校准、接受/反驳和新形式化写入 current owners/claim matrix/认知闭包，不回写篡改原文。
- 本目录不授权删除外部源、旧 generation、已有 Better Best 来源或任何图片。
