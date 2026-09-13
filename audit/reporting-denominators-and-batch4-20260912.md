# N15：报告口径对照表与第四批证据队列抽样复核（2026-09-12）

> Session：`S-RES-20260912-061-N15-CALIBER-AND-BATCH4`。结论限定在本报告固定源、固定版本与固定抽样规则内；本报告不新增、不升级任何数学 claim。
>
> 机器可核产物：`audit/reporting-denominators-reconciliation-20260912.json`（口径重算）、`audit/understanding-claim-sample-batch4-20260912.json`（第四批抽样与逐条判词）、`audit/understanding-claim-batch4-spot-checks-20260912.json`（数字/哈希专项核验）。
>
> 只读脚本：`scripts/audit/reconcile_reporting_denominators.py`、`scripts/audit/sample_understanding_claims_batch4.py`、`scripts/audit/fill_understanding_claim_sample_batch4.py`、`scripts/audit/verify_batch4_spot_checks.py`。

## 1. 任务与背景

方向追踪 §6 第一工作包（N15）要求：先把剩余口径不一致一次性对齐（句级账本 2369 vs claims 2,396；119 vs 125 user messages 等），产出《口径对照表》；再按 owner 抽样比继续加深，四值判词与前批去重；若发现 E6 立即转 F-011。

## 2. 口径对照表（N15a 主体）

每一条口径都从自己的 canonical 来源重新计数，而不是引用旧文档数字。

| 口径 | 计数单位 | 权威来源 | 实测值 | 不能推出 |
|---|---|---:|---|---|
| 用户句级账本 | 句/引文片段（author 标注：user / relay-gpt / relay-gemini / ai / platform / relay） | `AI对话录/sentence_ledger_annotated.json` | **2,369 句**，0 缺锚 | 不是理解章节 claim，也不是 user messages 计数 |
| 句级账本的遍历单元 | 轮/节（38 Codex + 111 网页 + 22 Gemini） | 同上（`turn` 去重） | **171 单元** | 不是 119，也不是 125 |
| 归档 user messages | 逐条用户消息（含 disposition） | `audit/user-message-disposition.jsonl` | **125 条记录** | 包含并行会话 6 条越界补充 |
| 其中历史对话消息 | 三条对话录内的用户消息 | 同上（`source_file` + 越界集合剔除） | **119 条**（Web 56 + LocalGPT 41 = main 10 + parent 31 + Gemini 22） | 119/119 与 125 是范围差，不是丢件；37 条 supplemental 属 LocalGPT 父线程历史谱系 |
| 退出范围记录 | `EXCLUDED_OUT_OF_SCOPE` | 同上 | **32 条**（含并行会话 6 条全部退出） | 退出不等于删除；原文件与行锚仍在 |
| 冻结 claim 账本 | 理解章节行/句抽取行 | `audit/claim-evidence-ledger.jsonl` | **2,396 行 / 24 份 owner** | 不是句级账本的子集，两者来源、切分规则、单位都不同 |
| 冻结账本的逐 owner 复算 | 同一抽取规则重放到当前文档 | `理解章节/*.md`（复算） | 24 份 owner 中 **22 份计数完全一致（合计 2,268 行）**；仅 `C0`（82→91）与 `README.md`（46→60）增长 | 复算一致不等于行文本一致（行锚漂移已由 `verify_claim_ledger_anchors.py` 另行处理） |
| 当前文档 claim 面 | 同一抽取规则重放全目录 | `理解章节/*.md`（复算） | **4,547 行**；其中 C1–C10 十份增量为 **2,128 行** | 冻结的 2,396 仍是证据队列分母；重新抽取是需显式授权的另外动作 |

### 2.1 两条"不一致"的裁定

1. **2,369 vs 2,396 不是冲突**：前者是三条对话录的用户侧句级账本，后者是理解章节行/句抽取账本。实测复算显示 2,396 恰好是账本建立时 24 份 owner 的抽取行数，且其中 22 份今天仍逐条复现计数；增长集中在 C 系列新文档（2,128 行）与 README/C0 两处增量。
2. **119 vs 125 不是丢件**：125 是归档记录总数，含并行会话（素数与归档）6 条补充，其 disposition 全部为 `EXCLUDED_OUT_OF_SCOPE`；119 是三条对话录历史消息数。LocalGPT 侧的 41 = 主文件 10 + 父线程 31，父线程即句级账本聚合的 Codex 38 单元来源。

### 2.2 口径对照的政策含义

- 引用"2,396"时必须写明是**冻结账本分母**；引用"当前理解章节 claim 面"时必须写 4,547（或重新抽取后的新值），两者不能互换。
- 引用"119"时必须写明是**历史对话消息**；引用"125"时必须写明是**归档记录（含越界补充）**。
- 句级账本的 171 遍历单元、2,369 句与 claim 账本的 2,396 行、24 owner 分属两个审计层，未来报告应各带口径标签。

## 3. 第四批抽样（N15b）

### 3.1 固定抽样规则（无结果依赖）

1. 从冻结的 2,396 行账本出发；
2. 计算前 1–3 批之后每份 owner 的已抽样比；
3. 预算 40，按已抽样比升序（并列按路径）分配，每 owner 上限 5；
4. owner 内等距抽取，剔除前批已抽 id；
5. 逐条给四值判词：`SUPPORTED` / `SUPERSEDED_BY_MACHINE_RESULT` / `UNSUPPORTED` / `PENDING`。

覆盖的 8 份 owner（均为前批后抽样比最低档）：`A8`（3.0%）、`A0`（3.5%）、`B3`（3.6%）、`A5`（3.7%）、`读遍账本`（3.8%）、`升级方案-v2`（3.9%）、`A10`（4.0%）、`A2`（4.3%）。

### 3.2 判词汇总

| 批 | 条数 | SUPPORTED | SUPERSEDED | UNSUPPORTED | PENDING | 样本发现 E6？ |
|---|---:|---:|---:|---:|---:|---|
| 第 1 批（S057） | 40 | 13 | 7 | 0 | 20 | 否 |
| 第 2 批（S059） | 50 | 30 | 5 | 0 | 15 | 否 |
| 第 3 批（S060） | 32 | 22 | 0 | 0 | 10 | 否 |
| **第 4 批（本批）** | **40** | **28** | **0** | **0** | **12** | **否** |
| **累计** | **162/2,396（6.8%）** | **93** | **12** | **0** | **57** | **四批一致：未出现 E6** |

### 3.3 本批判词的表述类型分布

本批 40 条中：

- **SUPPORTED（28）**：直接引文（用户原文、KC 引用）、路由/覆盖元数据、对所有者文档自述内容的准确转述、与 `audit/ledger-summary.json` 一致的计数（Gemini 21/36/24、LocalGPT 220、WebGPT 111 节）、以及可核哈希（MinerU SHA `62cef548…affe2`）。
- **PENDING（12）**：解释性综合（CL-000071、CL-000579、CL-000589、CL-000600）、待复核进程条目（CL-002287）、计划条款（CL-002164）、范围断言（CL-000783）、账本切分残句（CL-000816）、以及被 C9 精确化后需重述的 CL-000610。
- **UNSUPPORTED（0）**：四批累计仍为 0；本批次内没有任何一句需要以反证方式否定。
- **SUPERSEDED_BY_MACHINE_RESULT（0）**：本批 strata 是历史叙述/材料与路由层，机器结果接管型条目少；这与第 3 批（低覆盖 owner 抽样）的分布同型。

### 3.4 无 E6（升格口）出现的复核

本批最接近 E6 的三条已逐条复核：

1. `CL-000610`（W51×RP-B01"精确互为表里"）：C9 已把 W51-1/W51-2 与 B01-M/B01-E 映射到机器证据，`B01-TARGET` 保持 OPEN，第三层四条件未满足 → 仍不能升格。
2. `CL-002324`（220 条 agentMessage 口径）：与 `ledger-summary.json` 一致，属历史审计分母，不含自然使用链。
3. `CL-000816`（后继-极限鸿沟+停机归约 R5 条目）：为历史材料条目，未构成真实 HoTT 接口的资格越级。

结论：本批在固定抽样规则内**未出现 E6**，因此不触发 F-011 打包；判词阶梯保持第二级 `REPRESENTATION_BOUNDARY`。

## 4. 专项核验（数字与哈希）

`scripts/audit/verify_batch4_spot_checks.py` 固定 14 项检查全部 PASS（结果见 `audit/understanding-claim-batch4-spot-checks-20260912.json`），覆盖：

MinerU SHA 登记、EARLY-GEMINI 三件归档存在性、B3 中 70/3 测试记录与 0ⁿ1 陈述、Löb 前提区分、Gemini 21 thoughts/36 executions/24 ordinary text、LocalGPT 220 条主谱系回复、WebGPT 111 节、A2 用户读法原则、读遍账本 HoTT-2 读数、以及本批 40 条判词完整性与"无无证据 UNSUPPORTED"。

边界声明（保持诚实）：`CL-001619` 的"497 行 / 32,478 字节逐字节保全"目前只支持到 **B3 owner 文本 + archive/STORE.json 存在性**；该历史原稿的字节级重哈希未在本轮重跑，不能被本报告认证。

## 5. 口径与证据边界（不得外推）

- 本报告只处理**报告口径与证据队列抽样**，不产生数学结论，不改变任何 claim 的判词阶梯。
- 2,396 的冻结分母在重新抽取前保持不变；4,547 只是"同一规则在当前文档上的重放值"，不是新分母。
- 抽样判词只覆盖样本；`PENDING` 不当作支持也不当作否证。
- `SUPPORTED` 只表示"该句在其登记角色（引文/路由/计数）上可核"，不表示其内容已被数学证明。
- 本轮未改写 `理解章节/` 任何正文，merge manifest 计数不变；本轮新增文件都在 `audit/` 与 `scripts/audit/`。

## 6. 下一步

1. 若继续证据队列：按同一比例规则推进第 5 批（下一档 owner：`A11` 5.2%、`B5` 5.2%、`A7` 6.5% 等），保持四值判词与前批去重。
2. 若追求升格：唯一有效口仍是 E6（真实、固定版本、可回查的 natural consumer 链）；四批抽样与五层审计塔均未发现。
3. 备选仍为 ERCF-3 T3（Gödel 句），按 C8 停止条件保持 gated。
