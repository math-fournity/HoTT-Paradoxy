# S-RES-20260912-060-EVIDENCE-HYGIENE-BATCH3

- 触发：S059 路由的第一工作包 N14（证据卫生 + 第三批）。
- (a) 漂移修复：新增 `scripts/audit/verify_claim_ledger_anchors.py`（只读检查）+ `audit/claim-ledger-owner-hashes-20260912.json`（24 份 owner hash sidecar）+ `audit/claim-ledger-drift-check-20260912.json`；全量 2,396 条检查：`MATCH=327`、`PREFIX=550`、`CONTAINED=1490`、`DRIFTED=29`（README 14 + C0 15）、`LINE_OUT_OF_RANGE=0`、`MISSING_FILE=0`；引用政策固定（引用 claim 行先核 owner 当前文本）；`A-CLAIM-LEDGER-DRIFT-001` → `CLOSED_WITH_SCOPE`。
- (b) 第三批抽样：按前两批抽样比最低的 8 个 owner（A2/B5/A9/读遍账本/全量精读/A4/审计锚点/A1）各等距取 4 条 → 32 条；判词 `SUPPORTED=22`、`SUPERSEDED=0`、`UNSUPPORTED=0`、`PENDING=10`；三批累计 122/2,396（5.09%）：65/12/0/45；E6 连续三批未出现。
- 边界：漂移检查不改写历史账本；全量重抽取保留为可选项；PENDING 不当作支持或否证。
- 三件套：direction/panorama revision 60/generation 044；core 不变；无 理解章节 变更。
- Git：未 commit、未 tag、未 push。
