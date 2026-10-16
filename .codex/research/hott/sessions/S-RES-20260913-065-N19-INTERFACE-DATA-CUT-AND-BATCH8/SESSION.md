# S-RES-20260913-065-N19-INTERFACE-DATA-CUT-AND-BATCH8

- 触发：S064 路由的 N19（队列第 8 批 + 库内接口对照）。
- (a) 固定库读取记录：`isFinOrd`（数据）/`isFinSet`（存在，命题）并置与 `isFinOrd→isFinSet` 单向性；不新增 claim。
- (b) 第八批抽样 40 条（B3/读遍账本/B1/全量精读/B5/A1/A8/C0 各 5）：`SUPPORTED=24`、`PENDING=16`、0 `UNSUPPORTED`、0 `SUPERSEDED`；八批累计 322/2,396（13.4%）：200/12/0/110；E6 未出现；记录 `16,151 vs 16,209` 口径差待复核。
- 边界：无新数学 claim；未 commit/tag/push；三件套 revision 65/generation 049；core 不变。
