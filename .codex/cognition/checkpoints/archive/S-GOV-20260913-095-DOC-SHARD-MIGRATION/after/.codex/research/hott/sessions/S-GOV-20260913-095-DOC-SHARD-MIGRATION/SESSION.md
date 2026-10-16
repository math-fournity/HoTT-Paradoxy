# S-GOV-20260913-095-DOC-SHARD-MIGRATION

- 用户要求见 `rulings.md` §17；CP-1（S094）已建立逻辑文档加载能力与合同，本轮执行实际迁移。
- 迁移对象与布局：`README.md`→4 片（topical）；`MEMORY.md`→3 片（sequential，append_target=`MEMORY/003`）；
  `理解章节/C1`→4、`C2`→6、`C3`→5、`C4`→6 片（topical，按原 H2 语义簇）。
- 对账：每个逻辑文档按索引顺序拼接 shard 正文后与 boundary tag 内容逐字节相同；`MEMORY` 因顺序日志需作为末片而重排片序，
  采用逐行多重集 + 每片逐字切片对账（工具报告 `content_preserved_multiset=true`）。
- 失败与修正：首轮迁移把分片目录写到仓库根（shard 路径应相对索引目录解析）；错误产物已移出仓库、五个文件从
  boundary tag 精确还原后重做。该失败写入 `LESSONS.md` 第 74 条与迁移证据。
- consumer 同步：`build_history_ledgers`（claim 枚举按逻辑文本）、`build_understanding_merge_manifest`/`verify_understanding_merge`
  （逻辑文本对账 + 逻辑 hash 校验）、STATE 中 3 类 source hash re-pin（merge manifest、C3、C4）。
- 不改任何 KC、mathematical status、proof source/run/index；`HoTT/CLAIM_EVIDENCE_MATRIX.md` 明确保留单文件。
- 本地 annotated `governance-v3.3.0` 指向本 checkpoint 后的 commit；不 push。
