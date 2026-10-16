# A - FR 来源身份重建增补

> 对应 GPT 原片：`../GPT的方案/HoTT机器统观后续工作方案/003 - FR来源身份重建与版本闭合.md`。
> 修改性质：新增系统性根因条款；不改变 FR-001 的双路径与完成判词。

## A1. 新增：FR-001 必须同时回答"为什么漂移未被主动探测"

FR-001 的现有目标（确定 intended content、消除 actual/pinned 冲突）不变。但 003 片 §1 只登记了
"两个文件漂移"这一事实，未追查"漂移为何未在发生时被探测到"。本增补要求 FR-001 的产物中
**新增一项系统性根因登记**：

```text
FR-DETECTION-GAP:
  - 是否存在一个启动/加载时对所有 active record source hash 的主动探测？
  - 若存在，为何 S151 之后 goal.md/R4 的漂移未被该探测捕获？
  - 若不存在，四件套之外的 current-truth 文件（goal.md、R4/R3 TaskSpec、CE-MAP 等）是否
    应纳入与四件套同强度的启动 hash 闭包检查？
  - 处置：只读登记根因，或提出最小治理补丁（不扩大授权、不新建第二套 manager）。
```

判词：`DETECTION_GAP_DOCUMENTED`（有登记即满足）；`DETECTION_GAP_FIX_PROPOSED`（若提出补丁，
补丁仍须走治理自维护 Gate C01–C10，且默认 dry-run）。

## A2. 依据

本审计独立复核（02 §1）确认 `核心认知.md`（四件套，受 current_core + manifest + curation 三重
hash 管理）未漂移，而 goal.md/R4（active record，hash 钉在 STATE.records.source_hashes）漂移。
这提示（candidate）四件套之外 active record 的 hash 探测强度不足。若不追根因，FR-001 只治标，
下一份非四件套 current-truth 文件仍可能漂移而不被发现。

## A3. 采纳判据

- [ ] FR report 含 `FR-DETECTION-GAP` 登记块；
- [ ] 根因结论标注证据状态（observed / candidate / confirmed）；
- [ ] 若提出治理补丁，补丁已通过 dry-run 且未扩大授权。
