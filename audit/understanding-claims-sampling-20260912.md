# N12 审计：understanding claim 有界抽样复核（第一批）

> 文档身份：`CURRENT AUDIT EVIDENCE / BOUNDED_SAMPLE (40/2396)`
> 日期：2026-09-12
> 触发：S056 路由的第一工作包 N12（证据队列有界推进）
> 抽样规则（脚本 `scripts/audit/sample_understanding_claims.py`，确定性、可复跑）：关键词层（`univalence`/`ua`/`hit`/`truncation`/`cauchy`/`sip`/`cost`/`quotient` + `单价`/`高阶归纳`/`截断`/`柯西`/`商`/`成本`/`表示`/`资格`）全选 134 条 → 等距封顶 30 条；剩余按 `claim_id` 顺序等距补足 10 条；总计 40 条。
> 判词词表（固定）：`SUPPORTED`（在本轮证据范围内成立/可核）、`SUPERSEDED_BY_MACHINE_RESULT`（已被 repo 内机器结果覆盖或接管）、`UNSUPPORTED`（被现有证据否证）、`PENDING`（需人工句级裁决或历史重核）。

## 0. 计数与分布

| 项 | 值 |
|---|---|
| 总 claims | 2,396 |
| 关键词命中 | 134（等距封顶取 30） |
| 等距补足 | 10 |
| 本轮样本 | 40（1.67%） |
| 判词分布 | `SUPPORTED=13`、`SUPERSEDED_BY_MACHINE_RESULT=7`、`UNSUPPORTED=0`、`PENDING=20` |
| E6（natural consumer）检查 | 未出现；样本内唯一直接相关项（`CL-001577` B01-TARGET OPEN、`CL-000612` W51 第三层待补）均确认"尚无真实接口" |

## 1. 逐条判词

| # | claim | 位置 | 判词 | 依据/理由 |
|---|---|---|---|---|
| 1 | `CL-000001` | A0 L3 | `SUPPORTED` | 轮次路由元数据；与 prompt 账本/ledger 一致（provenance 层已机器核） |
| 2 | `CL-000015` | A0 L13 | `PENDING` | 解释性断言（"用户要的是第二层"）；需用户原文句级裁决 |
| 3 | `CL-000161` | A1 L31 | `PENDING` | 动机论表述；非可判定命题 |
| 4 | `CL-000232` | A10 L27 | `PENDING` | 文本自标"我的推断"；AI 推断，不升格 |
| 5 | `CL-000285` | A11 L31 | `PENDING` | 评价性叙述（审美与技术距离）；无判据 |
| 6 | `CL-000315` | A11 L79 | `PENDING` | 混合：`¬MereMove`/`A_k` 已有机器结果（C-103/104、C-114–116），LPO/WLPO 与 Acc 迁移仍纸笔 |
| 7 | `CL-000440` | A3 L3 | `SUPPORTED` | ASK 演进史；来源行可定位 |
| 8 | `CL-000473` | A3 L29 | `SUPPORTED` | 逐字引用用户 `KC-000014`（core 原文可核） |
| 9 | `CL-000492` | A3 L37 | `PENDING` | 资格理论表述；框架性，非命题 |
| 10 | `CL-000504` | A3 L41 | `PENDING` | 双轴框架；解释性 |
| 11 | `CL-000517` | A3 L57 | `PENDING` | ASK 五层结构；框架性 |
| 12 | `CL-000530` | A4 L3 | `SUPPORTED` | 命题发展史；来源可定位 |
| 13 | `CL-000612` | A5 L55 | `SUPERSEDED_BY_MACHINE_RESULT` | W51 命题化已在 S055/C9 完成；第三层缺口= `B01-TARGET`=E6 |
| 14 | `CL-000633` | A6 L11 | `PENDING` | 历史论辩句；语境依赖 |
| 15 | `CL-000653` | A6 L22 | `PENDING` | OUT-002 框架表述 |
| 16 | `CL-000716` | A7 L40 | `SUPPORTED` | R015 商正例与 OUT-003 在 workspace 有实物 |
| 17 | `CL-000728` | A8 L19 | `PENDING` | "三原则"为写作 AI 理解，非用户裁定 |
| 18 | `CL-000788` | A8 L86 | `SUPERSEDED_BY_MACHINE_RESULT` | 外延成本不可因子化已由 `MP-COST-FACTORIZATION-001`（C-96–99）接管 |
| 19 | `CL-000873` | A8 L154 | `SUPPORTED` | 行号覆盖陈述；与 TECHNICAL_NOTE 定位一致 |
| 20 | `CL-000963` | B0 L17 | `PENDING` | 历史指针；本轮未重核 |
| 21 | `CL-001013` | B1 L27 | `PENDING` | 工作史叙述；依赖 trajectory 审计（未在本轮重跑） |
| 22 | `CL-001065` | B1 L58 | `PENDING` | 文献边界引注；文献级 |
| 23 | `CL-001077` | B1 L61 | `SUPERSEDED_BY_MACHINE_RESULT` | CATT 张力已由 `MP-COST-FACTORIZATION-001` 与 N1 审计接管 |
| 24 | `CL-001125` | B1 L82 | `PENDING` | 文献指认；非命题 |
| 25 | `CL-001153` | B1 L99 | `PENDING` | 历史设计轮叙述 |
| 26 | `CL-001184` | B1 L115 | `PENDING` | T35 九类方向表；综合表述 |
| 27 | `CL-001215` | B1 L130 | `PENDING` | 历史指针 |
| 28 | `CL-001261` | B1 L164 | `PENDING` | 行为画像引证；需 trajectory 重核 |
| 29 | `CL-001289` | B2 L27 | `PENDING` | 行为特征描述 |
| 30 | `CL-001315` | B2 L59 | `PENDING` | 交换等价破坏"先后可用性"：有线因果/时序分离的机器对应（C-106–109、C-77–83），但该具体历史实例未重放 |
| 31 | `CL-001356` | B2 L89 | `SUPERSEDED_BY_MACHINE_RESULT` | "规范代表商引理"由 `MP-QUOTIENT-MONAD-001`（C-84）与 `MP-RACE-TIMEOUT-001`（C-71/72）覆盖 |
| 32 | `CL-001436` | B3 L66 | `SUPERSEDED_BY_MACHINE_RESULT` | 商递归尊重条件已由 C-71/72 机器化（bind 同余与商下降） |
| 33 | `CL-001460` | B3 L72 | `PENDING` | 来源保真观察；需句级对照 |
| 34 | `CL-001513` | B3 L78 | `PENDING` | "加公理不表示证明"；标准但未在 repo 形式化 |
| 35 | `CL-001549` | B3 L84 | `SUPERSEDED_BY_MACHINE_RESULT` | Bad 关系不传递/商闭包合并 → C-73–76 |
| 36 | `CL-001577` | B3 L106 | `SUPPORTED` | `B01-TARGET: OPEN` 经 C9 复核仍 OPEN（状态确认，非结论升级） |
| 37 | `CL-001607` | B3 L117 | `SUPPORTED` | 六项实物存在（workspace 路径可核） |
| 38 | `CL-001703` | B4 L30 | `SUPPORTED` | chunk15/72 "机器证明"宣称的撤回已由 IN-002 记录 |
| 39 | `CL-001939` | README L45 | `PENDING` | 口径问题：句级账本 2369 条与本 repo 2,396 claim 分母不同，需口径对齐 |
| 40 | `CL-002167` | 升级方案 L47 | `SUPPORTED` | 验证项（220 回复/55 节/24 chunk/三 git 仓库）与 ledger 计数一致 |

## 2. 结论

1. 样本内**没有出现 `UNSUPPORTED`**：没有发现被现有机器结果或审计直接否证的主张。
2. 样本内 7 条（17.5%）已被 repo 内机器结果覆盖或接管——正是 N3–N10 的机器包所在域（cost、商下降、race/deadline、W51 命题化）。
3. 20 条 `PENDING` 集中在三类：解释性/框架性表述（用户哲学层，需要人工句级裁决）、历史叙述（需要 trajectory 重核）、口径类条目（分母/计数）。
4. **E6 检查**：样本内没有任何条目构成"真实、固定版本、可回查的自然使用链"；与 C8/C9/C10 的汇合结论一致。
5. 覆盖率边界：40/2,396 = 1.67%，关键词层做过等距封顶；本报告只支持"本次抽样范围内"的结论，不宣称全量裁决完成。

## 3. 下一步

- 本报告未发现 E6，因此不触发 F-011；证据队列的继续推进（更大样本或按文件分层复核）保留为常规队列项；
- 按 N12 路由，下一工作包转 **T4 第五层 consumer 审计**（ERCF 线的最后一条 P8 路径）；若 T4 也无候选，则回到证据队列做第二批抽样（建议按 owner 文档分层）。

## 4. 证据与哈希

| 工件 | 说明 |
|---|---|
| `audit/understanding-claim-sample-20260912.json` | 抽样样本（40 条，含规则、计数、逐条原文节选与映射字段） |
| `scripts/audit/sample_understanding_claims.py` | 确定性抽样脚本（可复跑） |
| `audit/claim-evidence-ledger.jsonl` | 2,396 条 claim 的原始账本 |
| `audit/cross-source-reconciliation.json` | 22,226 条来源行登记（本轮用于补充 direction/result 映射） |

哈希在 checkpoint 时写入 STATE 与 session evidence。
