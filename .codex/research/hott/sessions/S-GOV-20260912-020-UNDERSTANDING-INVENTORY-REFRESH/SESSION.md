# S-GOV-20260912-020-UNDERSTANDING-INVENTORY-REFRESH

- 触发：S019 新增 C1/C2 并更新理解章节 README 后，projection freshness 正确报告 `MERGE_SOURCE_STALE:README.md:top_level`；旧 manifest 仍是 25/24。
- 修复：重建非破坏性 merge manifest；当前 top-level=27、nested=24、union=27、same-name=24、identical=15、different=9、top-only=3、nonidentical-union=12、unresolved-nontrivial=0。
- 路由：全景 OUT-UNDERSTANDING-MERGE 和 STATE scope 同步；方向数学语义、C1/C2、core 均不变。
- 边界：新增 C1/C2 是当前综合文件，不与 nested 历史源竞争同名；2,396 条旧 claim 的句级数学裁决没有因此完成。
- Git：runtime checkpoint applied locally；未 commit、未 push。
