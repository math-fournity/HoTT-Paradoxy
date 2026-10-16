# N13 审计：understanding claim 分层抽样复核（第二批）+ 行锚漂移发现

> 文档身份：`CURRENT AUDIT EVIDENCE / BOUNDED_SAMPLE_BATCH_2 (50/2,396)`
> 日期：2026-09-12
> 触发：S058 路由的第一工作包 N13（按 owner 文档分层抽样）
> 抽样规则（脚本 `scripts/audit/sample_understanding_claims_batch2.py`，确定性、可复跑）：按 owner 文档分层——C 系列（当前综合）10 条、meta 类（读遍账本/全量精读/升级方案/README/审计锚点）10 条、A 系列 15 条、B 系列 15 条；层内先剔除第一批样本，再按 `claim_id` 等距取样；总计 50 条。

## 0. 计数与分布

| 项 | 值 |
|---|---|
| 总 claims | 2,396 |
| 层规模 | C=82、meta=496、A=946、B=872 |
| 第二批样本 | 50（C 10 / meta 10 / A 15 / B 15） |
| 第二批判词 | `SUPPORTED=30`、`SUPERSEDED_BY_MACHINE_RESULT=5`、`UNSUPPORTED=0`、`PENDING=15` |
| 两批累计 | 90/2,396（3.76%）：`SUPPORTED=43`、`SUPERSEDED=12`、`UNSUPPORTED=0`、`PENDING=35` |
| E6 检查 | 第二批仍未出现 natural-use chain |

## 1. 逐条判词

| # | claim | 层/位置 | 判词 | 依据/理由 |
|---|---|---|---|---|
| 1 | `CL-001819` | C/C0 L3 | `SUPPORTED` | 当前 owner 指针；与三件套/audit owner 一致 |
| 2 | `CL-001827` | C/C0 L7 | `SUPPORTED` | 审计原则；已由 ledger 体系实现 |
| 3 | `CL-001835` | C/C0 L18 | `SUPERSEDED_BY_MACHINE_RESULT` | **行锚漂移**：账本文本为 generation-2 的 903 KC；当前 C0 该行为 generation-3 的 27 KC，当前 core 为 generation-4/36 |
| 4 | `CL-001843` | C/C0 L23 | `SUPPORTED` | Gemini 计数（24 ordinary text）与 gemini-ledger 一致 |
| 5 | `CL-001851` | C/C0 L24 | `SUPPORTED` | "语义 evidence mapping 待人工复核"状态仍真实（本批即其部分推进） |
| 6 | `CL-001860` | C/C0 L35 | `SUPPORTED` | 1143 call/result 对与 tool-event ledger 一致 |
| 7 | `CL-001868` | C/C0 L39 | `SUPPORTED` | 55 Response 的人工因果 mapping 仍未完成（状态确认） |
| 8 | `CL-001876` | C/C0 L47 | `SUPERSEDED_BY_MACHINE_RESULT` | **行锚漂移**：账本文本的"core 903"为 generation-2 口径；当前为 generation-3/4 |
| 9 | `CL-001884` | C/C0 L51 | `SUPPORTED` | `HoTT_is_GONE_COMPLETE.md` 的 SHA 可在 source manifest 复核 |
| 10 | `CL-001892` | C/C0 L57 | `SUPPORTED` | `discover_sources.sh` 行为描述与审计记录一致 |
| 11 | `CL-001901` | meta/README L3 | `SUPPORTED` | 当前审计层指针；与 C0 一致 |
| 12 | `CL-001951` | meta/全量精读 L10 | `PENDING` | 口径：119/119 与当前 125 user messages、2,369 与 2,396 claims 属不同账本/批次，需口径对齐 |
| 13 | `CL-002000` | meta/全量精读 L80 | `PENDING` | 工作方法步骤；非命题 |
| 14 | `CL-002050` | meta/全量精读 L109 | `PENDING` | 指针条目 |
| 15 | `CL-002099` | meta/全量精读 L158 | `SUPPORTED` | `upstream/` 处置与 SOURCE_MANIFEST 一致 |
| 16 | `CL-002149` | meta/升级方案 L28 | `SUPPORTED` | 锚点清单存在且为五类 |
| 17 | `CL-002199` | meta/审计锚点 L20 | `SUPPORTED` | 所列 owner 路径存在 |
| 18 | `CL-002248` | meta/读遍账本 L47 | `SUPPORTED` | 历史读态记录（网页 55 节）与读态账本一致 |
| 19 | `CL-002298` | meta/读遍账本 L110 | `SUPPORTED` | `r024/COMPILER_RESULTS.json` 计数与 work-product ledger 一致 |
| 20 | `CL-002347` | meta/读遍账本 L138 | `SUPPORTED` | proofs/ 处置表定性已记录 |
| 21 | `CL-000002` | A/A0 L3 | `PENDING` | 工作方法；非命题 |
| 22 | `CL-000064` | A/A0 L75 | `PENDING` | 问句片段 |
| 23 | `CL-000126` | A/A1 L9 | `PENDING` | 用户 Z 铁律立场；其机械版本仍需依赖证据（C4 §13 已列条件版） |
| 24 | `CL-000189` | A/A1 L65 | `PENDING` | 问句 |
| 25 | `CL-000252` | A/A10 L41 | `SUPPORTED` | "先验生成 6–10 个候选"方法已在 N4（C6）与 N11（C10）实际执行 |
| 26 | `CL-000316` | A/A11 L79 | `SUPERSEDED_BY_MACHINE_RESULT` | "A 方向缺的是主攻"被 S056/C10 重新评估：13 个候选全部归约为已知形状（不只是注意力问题） |
| 27 | `CL-000377` | A/A2 L39 | `PENDING` | 用户要求提取 shenchensh 悖论为独立文档；仍为开放条目 |
| 28 | `CL-000439` | A/A3 L3 | `SUPPORTED` | 轮次路由元数据 |
| 29 | `CL-000505` | A/A3 L41 | `PENDING` | 方法表述 |
| 30 | `CL-000569` | A/A5 L3 | `SUPPORTED` | 怀疑演进时间线与 prompt/ledger 一致 |
| 31 | `CL-000632` | A/A6 L11 | `SUPPORTED` | "TIMEOUT ≠ 不可停机"已是 repo 的固定校准（lesson 33 系列） |
| 32 | `CL-000695` | A/A7 L11 | `SUPPORTED` | 用户工作指令（Thinking in my math philosophy）已记录为工作原则 |
| 33 | `CL-000759` | A/A8 L54 | `SUPPORTED` | 史料学执行与其 Git 版本控制可核 |
| 34 | `CL-000822` | A/A8 L120 | `PENDING` | 指针 |
| 35 | `CL-000885` | A/A9 L9 | `PENDING` | 用户问句（"为什么这么久"） |
| 36 | `CL-000947` | B/B0 L3 | `SUPPORTED` | 历史 transform 边界横幅存在 |
| 37 | `CL-001004` | B/B1 L19 | `SUPPORTED` | Matrix 原文链计数与 LOCAL-GPT 语料记录一致 |
| 38 | `CL-001062` | B/B1 L55 | `PENDING` | 解释性引文 |
| 39 | `CL-001121` | B/B1 L82 | `SUPPORTED` | 历史运行记录（3 wrapper + 9 Agda + Lean exit 0） |
| 40 | `CL-001180` | B/B1 L112 | `SUPERSEDED_BY_MACHINE_RESULT` | 其中 `E⇒K` 必要性缺口已由 `MP-ERCF-001`（C-59–C-66）在一般层机器证明（具体实例未重放） |
| 41 | `CL-001239` | B/B1 L150 | `SUPPORTED` | R035 三区分已写入 owner 顶部（历史记录） |
| 42 | `CL-001298` | B/B2 L37 | `SUPPORTED` | "停在审计边界"的自我评估与 B3/S 系列一致 |
| 43 | `CL-001357` | B/B2 L89 | `PENDING` | WebGPT R014 的 `I≃K`（Canon isProp）；本 repo 的商 section 已有机器对应（C-84），该具体实例未重放 |
| 44 | `CL-001413` | B/B3 L54 | `SUPPORTED` | 历史落盘记录 |
| 45 | `CL-001472` | B/B3 L75 | `SUPPORTED` | OUT-002 三层分解提出史（后续入库） |
| 46 | `CL-001530` | B/B3 L81 | `SUPPORTED` | 引文记录 |
| 47 | `CL-001589` | B/B3 L111 | `PENDING` | R027 寄存器机布局细节；未重放 |
| 48 | `CL-001647` | B/B3 L141 | `PENDING` | P3b 圆布尔双覆盖无截面；与 `MP-PATH-CERTIFICATE-001` 同型但具体实例未重放 |
| 49 | `CL-001705` | B/B4 L34 | `SUPERSEDED_BY_MACHINE_RESULT` | "内部化 ASK 的戏剧化版本"已被 S053/C8 收窄：强读法在编码层被对角核反驳，ERCF-3 本体 gated |
| 50 | `CL-001762` | B/B5 L33 | `SUPPORTED` | Theory Schema 来源数/SHA 已在来源 manifest 记录 |

## 2. 本批唯一新发现：claim 账本的行锚/文本漂移

`CL-001835` 与 `CL-001876` 的账本文本仍为 **generation-2 口径**（`KC-000001`–`KC-000903`、"core 903"），而 `理解章节/C0-当前整合审计与证据边界-20260912.md` 当前该位置已是 generation-3 文本（`KC-000001`–`KC-000027`），当前 core 又是 generation-4/36。原因是 `audit/claim-evidence-ledger.jsonl` 是**快照账本**：它记录 `claim_owner_document` 与 `claim_line`，但不记录 owner 文档的内容 hash，因此 owner 文档在账本建立后被更新时，行号与文本都会漂移。

处置（本轮记录，不静默修正）：

- 新开 issue：`A-CLAIM-LEDGER-DRIFT-001`（OPEN_ISSUE / `REVIEW_REQUIRED`）——给 claim 账本增加 **owner-document hash + 行锚复核**（或按变更文件集重抽取）；在此之前，引用任何 claim 行时必须先核 owner 文档当前内容。
- 该漂移不影响已机器闭合的数学结果（那些结果由 `HoTT/CLAIM_EVIDENCE_MATRIX.md` 与 runs 拥有，不依赖 claim 账本的行号）。
- 两批抽样中按此规则复核的其余 88 条未见同类漂移（其余被抽 owner 文档未在账本建立后被改写，或其改动不落在被抽行）。

## 3. 结论

1. 第二批 50 条无 `UNSUPPORTED`；5 条被机器结果/后续综合接管；15 条 `PENDING` 集中在解释性表述、问句片段、历史技术与指针条目。
2. 两批累计 90/2,396（3.76%）：`SUPPORTED=43`、`SUPERSEDED=12`、`UNSUPPORTED=0`、`PENDING=35`。
3. **E6 仍未出现**；与 C8/C9/C10 的汇合结论一致。
4. 新发现的行锚漂移是**证据卫生问题**而非研究结论问题，已建 issue 与边界说明。

## 4. 下一步

- N14（若用户主方向无新优先级）：a) `A-CLAIM-LEDGER-DRIFT-001` 的有界修复（owner-hash + 复核脚本或重抽取）；b) 证据队列第三批（优先覆盖仍未抽到的 owner 文档：A4/A9/B0/B5 等）；
- 备选：ERCF-3 T3（Gödel 句，按 C8 停止条件仍 gated）。

## 5. 证据与哈希

| 工件 | 说明 |
|---|---|
| `audit/understanding-claim-sample-batch2-20260912.json` | 第二批样本（50 条，含分层、计数、原文节选） |
| `scripts/audit/sample_understanding_claims_batch2.py` | 分层抽样脚本（确定性、可复跑） |
| `audit/understanding-claims-sampling-20260912.md` | 第一批报告（对照） |
| `audit/claim-evidence-ledger.jsonl` | 2,396 条 claim 快照账本（漂移问题的对象） |
