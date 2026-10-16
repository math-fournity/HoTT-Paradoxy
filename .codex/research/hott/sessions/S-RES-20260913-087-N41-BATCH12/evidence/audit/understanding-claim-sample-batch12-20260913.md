# N41：理解章节 claim 证据队列第十二批抽样复核（S087）

日期：2026-09-13。Session：`S-RES-20260913-087-N41-BATCH12`。本轮沿用 N12–N39 的固定规则继续按比例抽样：不改变 2,396 行冻结分母，只对未抽过的新样本做句级裁决。

## 1. 抽样规则与分配（确定性）

`scripts/audit/sample_understanding_claims_batch12.py`：按 owner 的「前 11 批已抽比例」升序（同比例按路径序）分配 40 条预算，每个 owner 上限 5 条，owner 内等距抽取并排除前 11 批全部已抽样 ID。

| owner | 冻结行数 | 前 11 批已抽 | 前比例 | 本批 |
|---|---:|---:|---:|---:|
| B3-网页GPT工作史-II | 305 | 46 | 0.1508 | 5 |
| 全量精读工作方案 | 177 | 28 | 0.1582 | 5 |
| B4-Gemini工作史 | 44 | 7 | 0.1591 | 5 |
| A0-总目标 | 114 | 19 | 0.1667 | 5 |
| A1-Z铁律 | 100 | 17 | 0.17 | 5 |
| A2-参照悖论谱 | 116 | 20 | 0.1724 | 5 |
| B1-本地GPT工作史 | 276 | 48 | 0.1739 | 5 |
| 读遍账本 | 183 | 32 | 0.1749 | 5 |

## 2. 判词（40 条）

| 判词 | 本批 | 说明 |
|---|---:|---|
| `SUPPORTED` | 20 | 用户原文引句、可机器复核的计数/文件条目、仍成立的概念澄清 |
| `SUPERSEDED_BY_MACHINE_RESULT` | 2 | `CL-001048`（一般因子化条件句 → `MP-ERCF-001` C-59–C-66）；`CL-001564`（RP-B01/race-timeout 历史缺口 → `MP-RACE-TIMEOUT-001` C-71–C-76 + N2 审计 PARKED） |
| `UNSUPPORTED` | 0 | 无 |
| `PENDING` | 18 | 残句/标题片段 10、解释性或评价性条目 4、口径/回源待核 4 |

累计（12 批）：`482/2,396 = 20.1%`，`SUPPORTED=308`、`SUPERSEDED=14`、`UNSUPPORTED=0`、`PENDING=160`。

本轮 PENDING 偏高的原因是本批命中的 owner 以残句密集的 A1/A2/B4/全量精读为主；这不改变「已判条目无 UNSUPPORTED」这一连续记录，也不把 PENDING 当作支持或否证。

## 3. 本批的机器/现场复核项

| claim | 复核 | 结果 |
|---|---|---|
| `CL-002366` | `workspace/.codex/research/hott/sessions` 计数、`reviews` 计数、`PROOF_NOTE.md` 计数 | 44 SESSION ✓、10 reviews ✓、9 PROOF_NOTE ✓（owner 8 份未单独复核） |
| `CL-002022` | `workspace/artifacts/` 是否存在 r006–r015 | r006–r015 缺失、r016 起存在 ✓（与「留在 archive 旧 ZIP」的覆盖边界记录一致） |
| `CL-001626` | `4,330` 标签模型穷举 | 与 `workspace/artifacts/r027/FINITE_MODEL_RESULTS.json`（`labelled_models=4330`）一致（batch 6 已核，本轮沿用） |
| `CL-001953` | Gemini 实质 chunk 计数 | 24/24 ✓（`verify_history_ledgers`：ordinary text 24；另 thought 21 / executableCode 17 / codeExecutionResult 17 / inlineFile 2）；`125KB` 未单独复核 |
| `CL-001680` | inlineFile 不再是 empty | ✓（ledger 与 lesson 4；与上一行计数互证） |
| `CL-002292` | `workspace/scripts/research/r024_diagonal_machine.py` | 文件存在（7,304 bytes）✓ |

## 4. 口径差记账（不静默修正历史正文）

1. `CL-000994`：B1 记「2,091 份讨论源→2,006 逐字片段；2094 文件对账」，而 batch 9 核过的 A8 记录为「2,087 源→2,006 excerpt（131MB，18.39%）」。两处 `2,006` 一致；源数 2,091 vs 2,087 与对账数 2,094 属未合并的口径差，保持 `PENDING` 待回源，不改任何历史正文。
2. `CL-002292`：账本记「238 行全文」，现场 `wc -l` 为 237 行（文件以换行结束，字节数 7,304）。判 `SUPPORTED`（文件与内容吻合），但把行数口径差记入 `review_summary.caliber_items`，不回头改写账本。

## 5. E6 检查（第 12 批）

- 本批样本中没有出现「把较弱资格当作较强交付」的真实自然消费链（E6）：`CL-001048` 是历史一般条件句，已由 `MP-ERCF-001` 的机器化因子化接管；`CL-001564` 是 RP-B01/race-timeout 的历史未执行记录，已由 `MP-RACE-TIMEOUT-001` 与 N2 审计接管并 PARKED。两者都不是「同一任务下未声明假设的资格越级」。
- 因此十二批抽样一致：E6 未出现；判词仍停在 `DEFENSE_WORKS / REPRESENTATION_BOUNDARY`，升格口不变。

## 6. 不能推出

- 本报告只支持样本范围（40/2,396）的结论；不宣称全量裁决，不新增数学 claim，不修改 claim ledger 与理解章节正文。
- PENDING 不是否证；SUPPORTED 也不是数学认证，只表示该句与当前 owner 记录/现场一致。
- 抽样规则确定性可复跑；样本本身不提高任何数学证据等级。
