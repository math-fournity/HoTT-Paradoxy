# project-local governance v4.0.0：三件套 → 四件套升级证据

> 会话：`S-GOV-20260913-100-FOUR-SET-UPGRADE`（revision 100）
> 授权：用户审阅长文后说“甚至我们要从三件套升级到四件套”，并在 A/B/C 中选择 **A**（`rulings.md` §19）
> 范围：把《从抽象到悖论——HoTT研究的核心问题意识与思想展开》提升为常驻**第四件**逻辑文档，并同步加载链、审计字段与校验器
> 回滚边界：本地 annotated `governance-v3.5.0`

## 1. 升级内容

| 层 | 变化 |
|---|---|
| 文档 | 长文 552 行 / 75,495 B → **v2 索引 + 5 分片**（问题意识与理论简化 / 前提改变·结果·时间 / 芝诺·圆环·ASK·两种方向 / 走进 HoTT·理论自反 / 表达界限·文章作为起点·编写说明）；索引保留 `essay-role:v1` 角色声明与首屏 banner；36 段用户原文**逐字未动**，"不改变加载配置"的旧自述原位改为 v4.0.0 常驻第四件 |
| 角色 | `LOAD_SET.full_set_roles` + 文档内 `essay-role:v1`：**AI 阐释层**（`AI_EXPOSITION_LAYER`）；`核心认知.md` 仍是唯一用户原文权威；长文不产出数学结论、不得反向改写原文 |
| runtime | 3.3.0 → **3.6.0**：`FULL_SET` 四元组、LOAD_SET schema `cognition-load-set/v4`、键改名 `always_full_documents`/`document_order`、`MUTABLE` 纳入长文（索引与分片由 checkpoint 管理与 HEAD 跟踪）、逐 KC 审计新增第 7 字段 `essay_change`、错误码 `FULL_SET_ORDER_INVALID` / `KC_AUDIT_FULL_SET_FIELD_MISSING` |
| 配置/协议 | `LOAD_SET` 4.0.0、`PROTOCOL` v2.6（§2/§3A/§3B/§4 全面改称四件套并写角色边界）、本地治理 Skill 3.6.0、根与 `.codex` AGENTS、分片合同 §7、`feature-list` F-014 |
| 校验器 | `verify_fresh_three_way.py`（四件套身份/顺序/全部分片展开 + 子进程复查）、`verify_three_way_cognition.py`（四件套固定顺序 + 长文角色 marker，仍做 `DIR-*`/`OUT-*` 交叉）、`build_core_cognition_audit.py`（脚手架 7 字段） |

## 2. 加载体量（实测）

- `plan --profile governance`：**41 文档 / 820,100 B / 9,237 行**（升级前 35 文档 / 724,970 B / 8,409 行）。
- 增量 ≈ **+95 KB**：其中长文正文 +75 KB（含 22.8 KB 与 core 重复的用户引文），其余是索引、片头与 banner。
- 结论：四件套让每次 Session/压缩恢复多读约 10%；**分片不减少必读量**，只提供导航与写入局部性。

## 3. 验证（revision 100 实测）

| 检查 | 结果 |
|---|---|
| runtime 单测 | 38/38（fixture 配置改 v4、长文 fixture 带角色 marker、负向用例改 `FULL_SET_ORDER`） |
| 三方校验单测 | 6/6（含分片投影与缺片 fail-closed） |
| 三方校验 | `PASS`：固定顺序 = 核心认知 → 方向追踪 → 全景视野 → 长文；28 方向 / 90 结果 / revision 100 |
| fresh 冷启动 | `PASS_WITH_SCOPE`（四件套身份、顺序、每件全部分片展开，含子进程复查） |
| 分片结构 + banner | `PASS`：9 个 canonical 索引（README/MEMORY/C1–C4/方向追踪/全景视野/长文）全部带 banner；checkpoint 副本不计入 |
| 其他 | projection freshness / math gate / core / merge / cross-source / history / proof-version-closure / formal-run rerun 全部 PASS |
| canonical checkpoint | `.codex/cognition/checkpoints/S-GOV-20260913-100-FOUR-SET-UPGRADE/result.json` = `CHECKPOINT_COMMITTED` |

## 4. 过程中处理的三个真实问题

1. **HEAD 引导**：`MUTABLE` 新增成员后 `plan` 直接 `HEAD_TRACKING_INCOMPLETE`；用 canonical `initialize_cognition_head.py` 重新引导，
   并把该脚本改为**从 `runtime.MUTABLE` 取集合**（消除重复清单，避免下次漏项）。
2. **矩阵 pin 漂移**：S099 把矩阵 9 行移到文末追加节时没有重签矩阵的记录级 hash（`plan` 在无 task 时不暴露）；
   本轮 repin 循环捕获并修复（34 条 matrix pin + 审计脚手架 pin + AGENTS pin，均带 `revalidation`）。
3. **长文自述冲突**：长文原写“不改变现行自动加载配置”，与升级冲突；只原位修订 AI 撰写句，36 段用户引文保持逐字不变。

## 5. 边界与残余

- 长文是 AI 阐释层：它的任何数学语气都不构成结论；数学结论仍必须走 `MATH_PROOF_BEFORE_DELIVERY_V1`。
- core generation 变化时，长文必须按新原文重新检查覆盖与展开（已在 rulings §19 与长文自述中写明）。
- fresh model behavior `NOT_RUN`：结构、加载与字节层已机械验证；模型是否真正按四件套思考仍需真实 Session 观察。
