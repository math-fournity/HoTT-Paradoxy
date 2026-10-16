# GUI-LINEAGE-KB：八线研究脉络知识库提取 Workflow 方案

> **stable id**：`GUI-LINEAGE-KB`。**建立**：2026-10-08，ZCode（GLM-5.3）设计会话；研究发起人需求【原话】：“我要把它……的知识库建立起来——过去的东西，不能就这么丢了，不能没有系统化的整理、梳理。”
> **服务对象**：dev 线上继续研究的 AI（CG-006/CG-007 及其后继）。
> **载体**：分支 `wflow/gui-lineage-kb`（基于 `dev-glm-5.3` 并 fast-forward 合入 `dev`，含 glm 线全部产物＋QA 树＋CG-005/006/007 理解与形式化资产），worktree `~/.codex/worktrees/wflow-gui-lineage-kb/HoTT_AI_HANDOFF_20260911`。
> **总判词目标**：对 8 条 GUI 线的自有增量（尾→分叉节点），逐线重建**研究脉络**（分层：目标/SOP、为什么转向、做了什么）、**路上的发现**（判词、来源、控制、被拒候选与被拒理由）、**演进思路**（关键概念如何跨轮跨线变形），并给出跨线传播图；全部带可回放定位；未合并分支实物与判词颗粒度不得再丢。

## 0. 开工前预处置记录（2026-10-09，Master；本方案尚未派发任何节点）

在执行 DAG 之前完成四件事，全部只读输入层、未提交、未 push：

1. **口径桥落地为机器产物**：新增 `wflow-lineage/tools/build_scope.py` 与 `wflow-lineage/scope.json`——把「QA 块坐标轮号 ↔ GUI 导出行号 ↔ 裁决#3 轮数」三套坐标合成一张表（生成方法与失效案例见脚本 docstring 与 §1 坐标系声明）。顺带发现并更正原稿一处范畴错误：manifest 的 UNIQUE 区间是**文本级**唯一性，不是轮次归属（dev-03 自有轮有 24 行落在 SHARED 段），范围权威改为 QA 树归属。
2. **门禁脚本**：新增 `wflow-lineage/tools/check_lineage.py`，机械验 G1/G2/G6/G8 并提供 G3 抽样预检（不替代 N10 的独立复跑）。
3. **语料固有缺口登记**（方案 §4 R-9）：dev-08 第 0127 轮在 A 层导出中无原文（导出止于 0126）；8 个 rollout 共 9 个用户轮不可见（`qa/_tree.json → invisible_tails`）。两者都不是 agent 失职，但必须写进 AUDIT。
4. **K4 撞号与 G5 的交互预登记**（方案 §5 G5）：未合并包撞号（C-359~C-365、C-369 三义、C-370 起三组）未解，撞号区的 `carried` 落点必然多义，按"降级 parked 并登记"处理。

预置状态：`wflow-lineage/ledger.jsonl` 仅有 schema 说明、0 条执行记录；`wflow-lineage/lineage/` 尚无产物。N1-N8 未派发。

## 1. 输入层（冻结；全部只读）

| 层 | 路径（worktree 相对） | 用途 |
|---|---|---|
| A. GUI 导出 | `git-worktree对话录/dev-0*.md` | 唯一可见内容原件；定位底座 |
| B. QA 树 | `audit/GUI-SYNTH-REDO/qa/<line>/NNNN.md`、`.../_index.jsonl`、`.../_branch.json`、`.../_tree.json` | 机器按轮切片（**块口径**，含机械块；见 R-4） |
| C. 第一战役 | `audit/GUI-ASSET-RECOVERY/{manifest.json, notes/<line>.md, assets-ledger.md, D3-资产登记v2-20261007.md}` | 全行分层笔记＋619 条资产（含 CG 线未携带的判词字符串/Git 谱系/门规格） |
| D. CG 理解层 | `.claude/goals/CG-006-zfc-complete-formalization/{Targets与Profile.md, GUI查阅索引.md, 八线分叉后复盘.md}`、`docs/ZFC时间维度观察力不完备-哥德尔式Q终局报告-20261008.md` | 研究面综合；**只读不抄**，冲突时并陈 |
| E. 分支实物 | `git show origin/dev-0X:<path>`（原分支文件）、本仓 `dev` 上的 `HoTT/formal/**`、`audit/**` | 判词的物理落点 |

上下文副本：`wflow-lineage/context/20261008-八线掌握度与路线保全审计-ZCode.md`（设计者对 D 层的掌握度审计，K1-K5 风险登记）。

**坐标系声明（开工前必读，2026-10-09 预处置追加）**——三层输入各说各的坐标，混用会产出不可验的锚：

1. `qa/<line>/_index.jsonl` 与 `NNNN.md` frontmatter 的 `line_from/line_to`、`byte_from/byte_to` 是**源 rollout（jsonl）坐标**，不是导出行号：dev-08 最后一轮 `byte_to=166,684,447`，而导出文件只有 1,637,525 字节。引用它们时必须写清"rollout 坐标"。
2. `manifest.json → alignment.per_file[tag].unique_ranges` 是**文本级**唯一区间（与父线导出逐行 diff），**不是轮次归属**：研究发起人同一段核心提问在 dev-08 与 dev-03 逐字重复时，dev-03 自己那一轮有 24 行落在 SHARED 段（dev-03 12282–12305，src dev-08 13148–13171）。它只用来定**前缀/自有边界**（`ranges` 里 start≤2 的那个 SHARED 段的 `end`），轮次归属只认 QA 树（`qa/<line>/NNNN.md` 存在即该线自有轮）。
3. 裁决#3 的 124 轮口径定义在 raw rollout 上（`认知闭包/GUI-ASSET-RECOVERY-001.md` §8），冻结输入层内不可重算，只引用不推导。

**机器范围产物**：`wflow-lineage/scope.json` 由 `wflow-lineage/tools/build_scope.py` 从上述冻结输入层生成，把三层坐标合成一张可验表——每线：导出路径/行数/sha256、分叉父子、自有轮列表（块坐标）、每轮的 `anchor_line`（GUI 导出 `## User` 块标题行）与 `anchor_block_end`、机械轮的 `anchor_window`、裁决#3 轮数。`wflow-lineage/tools/check_lineage.py` 依它验 G1/G2/G6/G8 并带 G3 抽样预检。两工具只读输入、不写任何输入层文件；重跑 `build_scope.py` 必得同一输出。


## 2. 范围与分工（避免重复劳动）

- **每线 agent 只覆盖本线自有增量**：从导出末轮回到本线分叉点。**轮次归属以 QA 树为权威**（`qa/<line>/NNNN.md` 存在即该线自有轮；manifest 的 UNIQUE 区间是文本级唯一性，不当轮次边界，只定前缀/自有边界，见 §1 坐标系声明）；`dev-08` agent 额外承担共享前缀的“骨架层”（#1–#75 只建层名与一句话，不逐轮展开——避免 8 份重复）。
- **分叉图不是平的**（`qa/_tree.json` 的 `forks`）：`dev-04` 分叉自 `dev-03#13`、`dev-07` 分叉自 `dev-06#3`，其余六线（dev-01/02/03/06/08/09）分叉自 `dev-08`（分别在 #111、#86、#75、#97、以及 dev-08 自身自 archive-01a0fb73#10、#113）。因此 dev-04/dev-07 的“为什么转向”必须读父线对应轮次的语境，它们的自有文档数分别是 15 和 8，不是从 dev-08 直接继承。
- 不再全行重读 126,503 行（已完成的战役除外）：本 workflow 的源是 A-E 五层切片产物；允许为**取证**回读本线自有增量原文的有界窗口（每次 ≤300 行，须在 THREAD.md 的取证记录注明行号）。
- QA 树轮号是本线的稳定坐标：`dev-08/0117`＝`qa/dev-08/0117.md`；每线 THREAD.md 必须以轮号＋文件行号双锚。**行号一律用 scope.json 的 `anchor_line`/`anchor_block_end`/`anchor_window`**（GUI 导出 1-based），不要把 `_index.jsonl` 的 rollout 行号当导出行号写进产物。
- **自有轮数与两套口径**（同一线、不同定义，禁止互换）：块坐标（QA 树 `NNNN.md`）= dev-08 127 / dev-03 26 / dev-01 21 / dev-04 15 / dev-09 16 / dev-02 13 / dev-06 13 / dev-07 8，合计 239；裁决#3 权威轮数 = 56/18/10/11/8/10/7/4，合计 124。全树 `NNNN.md` 252 个 = 8 线 239 + archive-01a0fb08 3 + archive-01a0fb73 10。


## 3. 执行 DAG（并发子代理）

```
N1 dev-08 ┐ N2 dev-03 ┐ N3 dev-04 ┐ N4 dev-02 ┐ N5 dev-06 ┐ N6 dev-07 ┐ N7 dev-01 ┐ N8 dev-09 ┘
        （8 个并发，最多 4 个同时在跑）
                 └──────────► N9 综合 agent（ROUTE-GRAPH / EVOLUTION / CROSS-FEED / KB-INDEX）
                                   └──► N10 审计 agent（AUDIT.md 门禁报告）
```

- **N1-N8 每线 agent** 产出：
  - `wflow-lineage/lineage/<line>/THREAD.md`：分层脉络，尾→分叉。每层按模板：层名与轮次区间｜目标/SOP（含用户原话逐字锚点）｜GPT 做了什么【自述】｜发现与判词（verbatim token）｜实物（path@ref）｜**为什么转向**（引用户话或自述里的理由）｜沉淀给后续线/被后续线接走什么。
  - `wflow-lineage/lineage/<line>/DISCOVERIES.tsv`：机器行（无表头注释）：`id  line  layer  round  export_line  type  claim  verdict_token  artifact_ref  status  propagated_to  notes`。type ∈ {判定, 发现, 来源, 控制, 拒绝, 方法, 概念, 治理}；status ∈ {carried（被CG/dev继承）, parked, superseded, cold, open}。列数必须恒为 12（`check_lineage.py` 会把列数不符判为 G2 FAIL）。
  - 每线 agent 的第一动作是读 `wflow-lineage/scope.json` 里本线段，按其 `docs[]` 的轮号清单与锚点工作；`anchor_status` 为 `user_block`/`codex_fallback` 的轮有确定 `anchor_line`，`no_prose_mechanical_round` 的轮只有 `anchor_window`（该轮用户块只有环境上下文/页面标记等机械内容，仍须覆盖并在 THREAD.md 说明它是机械轮），`export_absent_prose` 的轮在 A 层导出里找不到原文（见 §4 R-9）。
- **N9 综合 agent** 产出：`ROUTE-GRAPH.md`（R_i→Z_i→Q_i 与线—层映射，节点＝层，边＝“供给/否决/接走”）、`EVOLUTION.md`（P/Q/Done/Z0/T 五个概念的跨线演变史，每步带轮次锚）、`CROSS-FEED.md`（D3 619 资产逐条“被谁继承/停在哪”）、`KB-INDEX.md`（总入口＋链接校验表）。
- **N10 审计 agent** 产出 `AUDIT.md`：按 §5 门禁逐项 PASS/FAIL＋证据；不得修改 N1-N9 任何文件。

## 4. 口径与证据规则（R1-R9，全部硬性）

- **R1 双锚**：每条发现必须能定位到 `导出文件:行号` 与 QA 轮号至少其一；实物类再加 `路径@git-ref`。导出行号用 scope.json 的锚点（`anchor_line`/`anchor_block_end`/`anchor_window`），**不得**把 `_index.jsonl` 的 rollout 行号当导出行号。
- **R2 判词逐字**：verdict_token 必须与语料逐字节一致（大小写下划线；不改写）；只在 D3/C 层找不到时标 `MISSING` 并记入 AUDIT。
- **R3 身份分离**：用户原话【原话】；GPT 结论【自述】（未复核）；机器证明【证明】；审计者/agent 判断【判断】。四类不得互相冒充。
- **R4 口径声明（BK-1）**：论“问答轮”一律用裁决#3 口径（全树 124；分线 dev-08 56/dev-03 18/dev-04 11/dev-02 10/dev-01 10/dev-09 8/dev-06 7/dev-07 4，来源 `认知闭包/GUI-ASSET-RECOVERY-001.md` §8）；QA 树的“252 轮”是**块口径**（含机械注入：8 线自有 239 + archive 两目录 13），只可用来当检索坐标，不可当用户问题数。裁决#3 口径定义在 raw rollout 上、冻结输入层内不可重算，因此只引用其**分线总数**，逐轮身份一律用 QA 块坐标 round 号。
- **R5 不重算、只引用**：CG-理解层的结论可引用并标注【D层】；发现冲突时两说并陈，由 Master 登记 `CONFLICT` 到 `wflow-lineage/ledger.jsonl`，不擅自裁决。
- **R6 冻结输入**：子代理不得写 A-E 层任何路径；不得 `git add`、不得切分支、不得 push；只写自己被分配的 `lineage/` 子路径。
- **R7 无数学结论**：本 workflow 只做脉络与资产提取；不得把任何命题提升为已证/已否。
- **R8 幂等与断点**：每个 agent 完成一节即向 `wflow-lineage/ledger.jsonl` 追加 `{"agent":..., "node":..., "path":..., "sha256":..., "ts":...}`；Master 崩溃恢复后按 ledger 重算未完成节点。
- **R9 语料固有缺口（开工前已登记，不得当作 agent 失职）**：
  1. **dev-08 第 0127 轮**（用户要求把 worktree 推到远程 dev-08）的原文在 A 层导出中不存在（导出止于 0126）；该轮只能以 QA 轮号锚定，verdict 只能引 QA 文档。
  2. **9 个不可见用户轮**：`qa/_tree.json → invisible_tails` 记录 8 个 rollout 共 9 个 `user_turns_not_visible`（GUI 导出未渲染），任何 agent 都无法覆盖，AUDIT.md 须列为固有缺口。
  3. **goal 续跑块会逐字嵌入用户早先的提问**：`<codex_internal_context source="goal">` 负载里可能出现早轮原文，不能据此把判词归到错误的轮次；锚点已在 scope.json 阶段排除机械区，agent 仍须自行警惕。

## 5. 完成门禁（Master 逐门验，全部 PASS 才收）

- **G1 覆盖**：8 线 THREAD.md 齐备；每线的自有轮次集合 = scope.json 该线 `docs[]` 的 100%（块坐标口径，机械轮也计——它是该线自有内容；同时并列裁决#3 轮数做口径核对，两者不互换）。
- **G2 双锚**：DISCOVERIES.tsv 每行 R1 满足，且 `round` 是该线自有轮、`export_line` 落在该轮锚点区间内（脚本可验：`python3 -B wflow-lineage/tools/check_lineage.py`）；缺锚/越界/错轮/枚举非法行数 = 0。
- **G3 判词保真**：审计 agent 用**自己的新鲜种子**抽 30 个 verdict_token 回导出原文逐字比对（不采信 agent 自述）。Master 在派 N10 前可先用 `check_lineage.py --seed <seed>` 自查，其结果**不替代** N10 的独立复跑。
- **G4 不丢**：D3 登记 619 条资产，在 CROSS-FEED.md 逐条有归宿（carried/parked/superseded/cold/open 之一＋一句理由）；未归宿数 = 0。机验下界：`check_lineage.py` 的 G4_mech 证明 619 个 A-ID（A-0001…A-0624）全部在 CROSS-FEED.md 出现过；「出现过」不等于「有归宿＋一句理由」，语义部分由 N10 逐条核。
- **G5 传播图闭合**：N9 之后，任一被标 `carried` 的发现都能在 CG 理解层或 `dev` 实物找到落点（git 可验），找不到的降级为 `parked` 并登记。**撞号区预登记**：C-359~C-365（dev/dev-02 同号异组）、C-369 三义、C-370 起三组（审计 K4）未解，撞号区的 carried 落点必然多义，按"降级 parked 并登记"处理，不计 agent 失败。机验下界：G5_mech 证明 carried 行的 `artifact_ref`（path@ref）path 在工作树或所引 ref 可解析；落点是否真承载该判词由 N10 核。
- **G6 链接**：KB-INDEX 全部相对链接解析成功（脚本检查：`check_lineage.py` G6 项）。
- **G7 口径一致**：AUDIT.md 确认全部文本的轮数字段符合 R-4（块坐标 round + 裁决#3 总数分列，不互换）。
- **G8 零未申报未知**：ledger 无 OPEN 状态的 `CONFLICT/UNKNOWN` 未结条目；结不了的转写进 AUDIT.md“遗留未知”节，由研究发起人裁定。

**停止条件**：预算耗尽或环境故障时，Master 按 CL-E 移交（未完成节点、下一步缺口、恢复入口），不宣称完成。

## 6. 子代理提示词模板（Master 原样套用）

### per-line agent（N1-N8）

```text
你是 GUI-LINEAGE-KB 的 <LINE> 线提取 agent（只读子代理）。工作根：~/.codex/worktrees/wflow-gui-lineage-kb/HoTT_AI_HANDOFF_20260911（下称 W）。
第一动作：读 W/wflow-lineage/scope.json 的 lines.<LINE> 段——它给本线权威的自有轮清单（docs[].doc）、每轮在 GUI 导出里的锚点（anchor_line/anchor_block_end/anchor_window）、分叉父子（fork）与裁决#3 轮数。你的 round 字段必须取自该清单。
输入（全部只读，路径相对 W）：git-worktree对话录/<导出文件>；audit/GUI-SYNTH-REDO/qa/<LINE>/（NNNN.md 切片 + _index.jsonl 源 rollout 坐标 + _branch.json）；audit/GUI-ASSET-RECOVERY/{manifest.json, notes/<LINE>.md, assets-ledger.md, D3-资产登记v2-20261007.md}；.claude/goals/CG-006-zfc-complete-formalization/{八线分叉后复盘.md, GUI查阅索引.md, Targets与Profile.md} 中与 <LINE> 相关的节；docs/ZFC时间维度观察力不完备-哥德尔式Q终局报告-20261008.md。
任务：为 <LINE> 写 W/wflow-lineage/lineage/<LINE>/THREAD.md（分层脉络，尾→分叉；dev-08 另加共享前缀 #1–#75 骨架层，只建层名＋一句话）与 DISCOVERIES.tsv（12 列，制表符分隔，无表头：id line layer round export_line type claim verdict_token artifact_ref status propagated_to notes）。
硬规则：R1 双锚（每行给 export_line 与 round 至少其一；export_line 用 scope.json 的锚点，不许把 _index.jsonl 的 rollout 行号当导出行号）；R2 判词逐字（从导出原文摘，不改大小写/下划线，MISSING 要登记）；R3 身份四类标注；R4 轮数口径（块坐标 round 来自 scope.json 清单＋裁决#3 分线总数 <N>，两者不互换）；R6 只写你的两个文件，每完成一节向 W/wflow-lineage/ledger.jsonl 追加 {agent,node,path,sha256,ts}；R7 不得产出任何数学结论；R9 语料固有缺口（见方案 §4）不得算你的失职，也不得掩饰。
已知陷阱：判词字符串大量存在于 assets-ledger.md/D3（如 TERMINAL_CLEANUP_WITHOUT_CLOSE、NO_MODEL_RECALL_CANDIDATE）；机械轮（anchor_status=no_prose_mechanical_round）只有机械内容，仍须在 DISCOVERIES 覆盖并在 THREAD.md 说明；research发起人的核心提问段落在多条线逐字重复（Q/A/B 段），勿把别线/别轮的同一段文本归到本轮；goal 续跑块内嵌有早轮原文；dev-08 的 #112 哥德尔原话只在分支 dev-notes，GUI 导出内有；export_absent_prose 轮在 A 层无原文，只能引 QA 文档。
完成判据：DISCOVERIES.tsv 覆盖 scope.json 给的本线全部 round；THREAD.md 每层有"为什么转向"。
```

### synthesis agent（N9）

```text
你是 GUI-LINEAGE-KB 综合 agent。读 W/wflow-lineage/lineage/*/THREAD.md 与 DISCOVERIES.tsv 全部，加上 audit/GUI-ASSET-RECOVERY/D3-资产登记v2-20261007.md 与 .claude/goals/CG-006-zfc-complete-formalization/{Targets与Profile.md}。写四文件：ROUTE-GRAPH.md（节点=层、边标注 供给/否决/接走，带轮次锚）；EVOLUTION.md（P/Q/Done(OriginDone)/Z0/想法T 五概念的跨线演变，每步锚 round+行号）；CROSS-FEED.md（D3 619 条逐条归宿：carried/parked/superseded/cold/open＋一句理由）；KB-INDEX.md（总入口、所有相对链接校验表）。规则同 R1-R9；冲突两说并陈并登记 CONFLICT。分叉图按 qa/_tree.json：dev-04 分叉自 dev-03#13、dev-07 分叉自 dev-06#3，其余六线分叉自 dev-08。
```

### audit agent（N10）

```text
你是 GUI-LINEAGE-KB 审计 agent。对 lineage/ 全部产物按 §5 门禁 G1-G8 逐项验：G1 轮覆盖（与 wflow-lineage/scope.json 的自有轮清单逐线比）；G2 双锚（可先跑 `python3 -B wflow-lineage/tools/check_lineage.py --lineage W/wflow-lineage/lineage` 看机器结果，再自行复核其判 negative 的行）；G3 用**你自己新取的种子**抽 30 个 verdict_token 回导出原文逐字比对（不得采用 Master 或 check_lineage.py 的抽样结果）；G4 D3 619 归宿核对；G5 carried 落点 git 可验（撞号区 C-359~C-365/C-369/C-370 起按 §5 G5 预登记处理）；G6 链接解析；G7 R-4 口径；G8 ledger 无未结 OPEN。产出 W/wflow-lineage/AUDIT.md（逐门 PASS/FAIL＋证据定位）。不得改任何既有文件；发现问题只写 AUDIT.md 并在 ledger 登记。
```

## 7. Master 压缩协议（Master Agent 专用）

- 常驻工作集：本方案、`wflow-lineage/scope.json`（冻结输入层的机器投影，输入未变则不必重跑）、`ledger.jsonl` 尾、当前节点契约、产出树 `find wflow-lineage/lineage -name '*.md' | sort`。
- 压缩边界触发（新会话/被告知压缩/自检缺项）：停写→重读本方案＋ledger 尾→以 ledger 重算未完成节点→继续。禁止凭记忆重派节点。
- 输入层指纹核对：开工或恢复时跑 `python3 -B wflow-lineage/tools/build_scope.py`，若 scope.json 内容不变（锚点/轮数一致）则输入层未被改动；若变化，先查是哪一层被改，报告后再继续。
- 任务完成前禁止 push；提交由 Master 以精确路径 `wflow-lineage/**` 一条提交完成（信息注明 workflow id 与完成门结果）。

## 8. 验收口径（交付研究发起人）

KB-INDEX.md 为唯一入口；任一未来 AI 从它出发，能在 ≤3 跳内回答：某条线在某个阶段想做什么、得到了什么判词、为什么转向、哪个发现被哪条线接走、某资产现在何处。达不到即 G8 不通过。
