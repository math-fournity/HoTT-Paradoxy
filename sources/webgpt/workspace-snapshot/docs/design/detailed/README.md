# Detailed Design

职责：API/CLI/schema、算法、状态机、错误、并发、幂等、恢复和迁移合同。

当前稳定合同：`../../../HoTT/sources/aistudio-discussions/README.md` 与 `schema.json` 定义 HoTT
逐字语料的源根、结构分类、锚点、边界扩展、manifest、immutable generation、lock、原子
`CURRENT`、验证与查询 CLI。唯一实现是 `../../../HoTT/tools/hott_discussion_corpus.py`；不能手改
machine-managed 产物。ADR-003 保存取舍理由。

`../../../HoTT/sources/user-originals/matrix-book-paradoxes/README.md` 定义
`matrix-book-paradox-extract/v1`：固定外部源 SHA、自然解答链行区间、全图片 inventory、显式命中
覆盖、immutable generation、lock、原子 `CURRENT` 和 validate。唯一实现是
`../../../HoTT/tools/matrix_book_paradox_extract.py`；外部源改写必须 fail closed，不能复用旧行号或
手改 generation。
