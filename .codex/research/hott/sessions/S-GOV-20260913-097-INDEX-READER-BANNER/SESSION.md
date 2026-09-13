# S-GOV-20260913-097-INDEX-READER-BANNER

- 用户说“开始加固”，授权沿用 `rulings.md` §17/§18 的边界（本地、不 push、只改治理载体）。
- 动作：8 个 canonical 索引加首屏 banner（`> ⚠️ 逻辑文档索引：全文 = 本索引 + 下方 N 个分片；缺一片即未完成…`）；
  其中 `README.md`/`理解章节/C1`–`C4` 为非 MUTABLE，直接提交；`MEMORY.md`/`方向追踪.md`/`全景视野.md` 经本 checkpoint 写入。
- 强制：`scripts/audit/logical_document.banner_issues` + `verify_governance_shards.py`（缺失/残缺即 FAIL，退出码 1）；
  单测 `test_shard_index_banners.py` 5/5。
- 连带：`理解章节/C1`–`C4` 索引变更 → merge manifest 重建（计数不变：35/24/15/9）+ 14 条 record 重签；
  `AGENTS.md` 路由文本新增 banner 一行 → 1 条 record 重签。
- 不改任何 KC、数学判词、proof source/run/index；三件套全文语义不变。不 push。
