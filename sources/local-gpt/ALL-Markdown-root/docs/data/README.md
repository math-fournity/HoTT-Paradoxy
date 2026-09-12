# Data

职责：数据模型、schema、血缘、质量、保留、迁移和恢复。

当前版本化文件格式是 `hott-discussion-corpus/v1`，owner 为
`../../HoTT/sources/aistudio-discussions/schema.json`，操作/保留合同为同目录 `README.md`，canonical
manager 为 `../../HoTT/tools/hott_discussion_corpus.py`。`manifest.jsonl` 逐条保存源 SHA、结构、连续
行区间和逐字哈希；`source_inventory.jsonl` 保存输入快照；`STATS.json` 保存可机械复算的结构与覆盖
统计。generation 不覆盖、默认不删除，`CURRENT` 只作原子指针；原始 Markdown 始终是权威数据。
讨论文档输入后缀为大小写不敏感的 `.md` 与 `.markdown`；CSV/TSV 归档报告、仓库配置和系统缓存
不进入 corpus inventory。格式变更必须升 schema/manager 并建立新 generation，不能就地迁改旧
raw capture。Secret 不在此记录。

第二个版本化派生格式是 `matrix-book-paradox-extract/v1`，owner/保留合同为
`../../HoTT/sources/user-originals/matrix-book-paradoxes/README.md`，manager 为
`../../HoTT/tools/matrix_book_paradox_extract.py`。它以指定外部源 SHA、固定连续行区间和全部图片
SHA 形成 immutable generation；`MANIFEST.json` 管 extract/图片/显式命中覆盖，完整源快照和独立
原文共享同代 `images/`。外部源 SHA 变化必须 fail closed 并重算行区间，不能沿用旧 offset；旧
generation 不删除。该 derived view 是用户原作血缘，不是数学/物理真值。
