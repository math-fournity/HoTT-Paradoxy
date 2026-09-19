# S-RES-20260912-061-N15-CALIBER-AND-BATCH4

- 触发：S060 路由的第一工作包 N15（口径统一 + 按比例继续抽样）。
- (a) 口径对照：`scripts/audit/reconcile_reporting_denominators.py` + `audit/reporting-denominators-reconciliation-20260912.json` 从各 canonical 源重算：句级账本 2,369 句 / 171 遍历单元（38 Codex + 111 网页 + 22 Gemini，0 缺锚）；归档 user records 125（119 历史对话 + 6 并行会话越界补充，32 条 EXCLUDED_OUT_OF_SCOPE）；冻结 claim 账本 2,396 行 / 24 owner。复算显示 22/24 owner 计数完全一致（2,268 行），仅 `C0`（82→91）与 `README.md`（46→60）增长；当前理解章节 claim 面 4,547 行（C1–C10 增量 2,128）。两条“不一致”均为单位/范围差，非丢件或冲突。
- (b) 第四批抽样：按前 1–3 批已抽样比升序分配 40 条（每 owner≤5），覆盖 A8/A0/B3/A5/读遍账本/升级方案-v2/A10/A2；判词 `SUPPORTED=28`、`SUPERSEDED=0`、`UNSUPPORTED=0`、`PENDING=12`；四批累计 162/2,396（6.76%）：93/12/0/57；E6 四批一致未出现，不触发 F-011。
- 专项核验：`scripts/audit/verify_batch4_spot_checks.py` 14/14 PASS（MinerU SHA、EARLY-GEMINI 归档、B3 70/3 与 0ⁿ1 陈述、Löb 前提、Gemini 21/36/24、LocalGPT 220、WebGPT 111、A2 读法原则、读遍账本 HoTT-2 读数、40 条判词完整性、无无证据 UNSUPPORTED）。
- 边界：冻结 2,396 分母不变；4,547 只是同规则在当前文档上的重放值；抽样判词只覆盖样本；`SUPPORTED` 只表示登记角色内可核，不表示数学已证；本轮不改写 理解章节。
- 三件套：direction/panorama revision 61/generation 045；core 不变；无 理解章节 变更。
- Git：未 commit、未 tag、未 push。
