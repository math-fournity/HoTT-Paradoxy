# GLM-5.3-Flash 工作区

> 建立日期：2026-09-26（用户裁定：GLM 侧工作不与 Opus/Claude 侧工作树混放，见 `rulings.md` 第 33 条）。
> 宿主/模型：ZCode Desktop / GLM-5.3-Flash。本目录是 GLM 模型在本 repo 的专属工作区，**不是第二份治理真值**：共享真值 owner（四件套、STATE、rulings、README、证明门禁基建）全部不变。

## 1. 为什么有这个目录

- 本 repo 已有按模型/角色分树的先例：`.claude/`（Claude/Opus 的治理与研究树）、`Terra对Opus的审计/`（Terra 的审计线）、`Flash的第一次寻找尝试/`（早期 Flash 的工作记录）、`.codex/`（canonical 共享治理树）。
- 2026-09-26 用户裁定：GLM 侧后续工作不得写入 `.claude/`，在本目录自立账目。此前 GLM 会话（如 2026-09-26 的中断点诊断）只做过读取，未写 `.claude/`。

## 2. 读写边界

| 区域 | GLM 权限 |
|---|---|
| `.claude/`（Opus 树：总索引、思考与发现、goals、relay、handoff） | **默认只读**。引用给 locator；跨树写入仅在用户对具体任务明确授权时进行 |
| 四件套（核心认知/方向追踪/全景视野/扩展认知） | 按档位只读消费；写入走 curation manager / 授权 checkpoint，不经本目录 |
| STATE.json、`.codex/cognition/`、checkpoint 事务 | 只读；mutation 走授权 checkpoint（T3） |
| `HoTT/formal/`、`HoTT/verification/runs/` | 数学证明门禁共享基建照常使用；包目录用 `glm-` 前缀（如 `glm-cg001/`），运行 ID 用 `GLM-`（如 `20260926-GLM-...`），与 `claude-cg001` 平行 |
| `rulings.md`、`feature-list.md`、`README/` | 仅按既有 owner 登记用户明确裁定/需求；不夹带 GLM 自创事实 |
| 本目录 | GLM 的日志、笔记、goal 包、目标内索引、与用户的问答整理 |

## 3. 目录内约定

- 笔记编号用 `GN-xxx`（GLM Note），与 Opus 的 `CN-xxx` 平行，编号各自独立、互不占用。
- 结构按需生长、不预建空目录：`思考与发现/`、`goals/`、`工作日志.md`。
- 目标内证据索引（仿 Opus 的 `证据索引.md`）放 `goals/<goal>/` 内，标 `GOAL_LOCAL_INDEX_ONLY`；共享矩阵 `HoTT/CLAIM_EVIDENCE_MATRIX.md` 的行仍由 integrator 裁定并入。
- 本目录内的判断一律标注身份（观察/登记/解释/猜想/证明）；不把 Opus 成果的 `待登记`/`CANDIDATE` 等状态擅自升级。
- 跨树引用给可点击相对路径；引用 Opus 思考笔记时保留其 `CN-` 编号。

## 4. 当前接手状态（2026-09-26）

Opus 会话 7f138325 的中断点判定与未完成清单见[思考与发现/GN-001](思考与发现/GN-001%20-%2020260926%20Opus会话7f138325中断点判定与接手清单.md)。
