# dev-06 线研究脉络（尾 → 分叉点）

> 本文件由 dev-06 线提取员从八份冻结输入层重建，只读生成；未改动任何输入层，未写 ledger.jsonl。
> 权威轮数/锚点口径：`wflow-lineage/scope.json` 的 `lines.dev-06`（块坐标 `docs[]`，13 个自有轮）。
> `adjudication_rounds = 7`（`认知闭包/GUI-ASSET-RECOVERY-001.md` §8 裁决 #3，2026-10-07）只作并列引用，
> 与块坐标口径**不互换**：块坐标按 GUI 导出的 `## User` 块切分（含机械轮），裁决 #3 按
> 「raw `response_item/message role=user`，剔除机械前缀，annotation 包裹计一轮，rollover 同文重发不计」。
> 因此本文件所有 `round` 字段一律取块坐标；凡引用「7 轮」处均显式标注裁决 #3 口径。

## 0. 线身份与分叉点

| 项 | 值 |
|---|---|
| 线 | dev-06（GUI 标题行 `# 🌟 06 - ZFC-1`，导出 L1） |
| 导出 | `git-worktree对话录/dev-06 - 20261004T160420Z-01a106f7-75c0-7dd0-b135-63d0393bd6cf-cd2523908155-gui.md` |
| 导出行数 / sha256 | 15,468 行 / `49652da00c783b548cc1bb8cab14a176e6f29be93f395628349196b60f6401d1`（`scope.json`） |
| worktree | `/Users/aurolafly/.codex/worktrees/cad0/HoTT_AI_HANDOFF_20260911`（导出 L14598 `<cwd>`） |
| 分叉 | 子线自 **dev-08 #97** 分出；`fork.parent_rollout = 01a10097-8df9-7dd0-8009-8357ebc59781` |
| 下游分叉 | dev-06 #3 → dev-07（`八线分叉后复盘.md:15`） |
| 自有轮 | 13（块坐标 `0001`–`0013`）；裁决 #3 口径 7 轮 |
| 锚点摘要 | `total=13, anchored=9, mechanical_window=4, export_absent_prose=0, unresolved_prose_docs=[]` |
| unique 区间 | 58 个 / 639 行（相对父 dev-08）；`prefix_end_line = 14596` |
| 覆盖 | `audit/GUI-ASSET-RECOVERY/coverage.json`：dev-06 unique 639 行全部覆盖，`remainder=0` |

**分叉点语境**（`八线分叉后复盘.md:34`）：主干 dev-08 当时在追 MPIM 讲座与 cubical-set model，
想知道 Cubical Agda 证明能否转成集合论证明（H0→Z0 的来源支线）。dev-06 #3 的第一句用户提问
正是对这一支线的质疑，本线自此与主干分道。

**语料固有缺口**（不构成本提取员的失职，也不掩饰）：
1. SHARED 前缀 14,829 行以 manifest 指针免读（`notes/dev-06.md:3`）；本线只重建 unique 639 行。
   故 dev-08 #97 之前的共同前段不属本线自有轮，THREAD 不做追溯。
2. `scope.json` 标注 `anchor_status=no_prose_mechanical_round` 的 4 轮（0001/0002/0008/0012）
   在 GUI 导出的 User 块只有 `environment_context` / `<external_codex_apps_open_page>` /
   goal 续跑 `<codex_internal_context source="goal">` 等机械内容，**无 prose、无判词、无转向**；
   它们在 DISCOVERIES.tsv 中仍按 R6 覆盖，并在下文标注为机械轮。
3. 0003 轮的 `## My request` 与 `response-annotations` 属 annotation 包裹轮；裁决 #3 明确「annotation
   包裹消息计一轮」。GUI 查阅索引把 dev-06 的路编号为 `dev-06/0003` 起（`GUI查阅索引.md:43`），
   即该轮在 QA 树口径中即 #3。
4. `qa/dev-06/_index.jsonl` 记 doc 0001–0010 来自主 rollout，0012–0013 来自 rollover 文件
   `rollout-2026-10-04T11-35-11-..._01a1078e-0a8f-7d91-ad4e-cb0af2298950.jsonl`。
   按 R1，本文件所有 `L` 编号一律为 **GUI 导出行号**，不把 `_index.jsonl` 的 rollout 行号当导出行号。
5. `scope.json` 的 `docs[]` 未给出 codex_fallback 轮（0007/0010/0011）的 verdict 判词文本；
   本文件对这些轮的判词一律改写为「GPT 自述」或从同段后续 Codex 块中取逐字 token，并注明出处行。

---

## L1 · 成果保存：以 `86ad33c4` 首次创建并推送 `origin/dev-06`（round 0013）

- **导出行**：L15395（`## User` 块头，scope anchor_line）→ L15397 用户原话；L15400 起 Codex。
- **【原话】用户**（L15397）：「你现在的这个git worktree上的工作，我希望保存到远程的dev-06分支上，你打算如何处理？」
- **【自述】GPT**（L15402）：先「把『已版本化的 H0→Z0 工作』和工作树里尚未提交的归档／对话材料分开核对，
  并检查远端 `dev-06` 是否已存在、它与当前提交的共同基线是什么」。
- **【自述】远端判定**（L15406）：「现场已确认：远端目前**没有** `dev-06`，因此可以用非强制、首次创建的推送
  完成保存；不会覆盖任何已有远端 ref。我的处理会是：从当前 `5cf4ab06` 创建本地 `dev-06`，把工作树中尚未提交的
  三类材料逐项核查后做一个独立归档提交，再只推送 `dev-06`。」
- **【自述】归档内容**（L15410）：2 份 `dev-notes` 对话归档 + 3 份 `git-worktree对话录`，共约 4.3 MB；
  敏感模式扫描没有发现私钥、token 或 API key。
- **【自述】自约束**（L15418）：「推送命令在首次网络等待窗口内没有返回完整结果；我不会把它当作失败或成功猜测，
  而是直接核对远端 `refs/heads/dev-06` 的实际 OID，再只在确有需要时重试。」
- **【自述】边界保留**（L15422, L15451-15452, L15463）：`origin/dev-06` 与本地 `dev-06` 同为
  `86ad33c4a896931b9d5aa5158639e6a6b89dce15`；`codex/h0-z0-priority-realignment` 仍保留在 `5cf4ab06`，
  没有被改写，也没有触碰 canonical `dev`；历史对话录的原始尾随空白与 `git diff --check` 警告被显式保留。
- **【自述】终句**（L15426）：「已经按这个目标处理完毕：当前 worktree 的工作已保存到远程 `dev-06`，
  且没有覆盖 `dev`、没有重写任何已有远端分支。」
- **为什么转向**：用户要求把 worktree 工作保存到远程 `dev-06`；GPT 自述的处理原则是「从当前 `5cf4ab06` 创建
  本地 `dev-06`……不会合并或重写 canonical `dev`，也不会改动已经推送的 `codex/h0-z0-priority-realignment`」
  （L15406），即把「保存」拆成研究历史 + 独立归档提交两条，以避免静默混入别会话的未提交材料。
- **下游**：本轮的 `origin/dev-06` 正是八线分叉树中 dev-06 的远端分支；`八线分叉后复盘.md:20`
  记载 `git fetch` 后 `origin/dev-06`（当时 af0d9c5c）相对 `dev` 领先 10 个提交。

## L2 · 有界收尾：PF-B2 盲态 P1 负控制 → Goal 有界完成（round 0011；round 0012 为机械轮）

- **导出行**：L15284（scope anchor_line，goal 续跑块）；L15345–15353 记三提交与 Goal 用量。
- **【自述】方法规格修订**（L15258）：「我会把这次纠偏作为一次**方法规格修订**落盘：
  `IDEA_SPEC_INCOMPLETE / Q_SAFETY_REPAIR`。它不把『ZFC 没有原生过程锚点』当作结论；它只规定下一张 profile
  必须让 P1 有机会区分『静态形成对象』与『理论自己定义的、带过程完成条件的接口』。」
- **【自述】盲态卡冻结**（L15266）：「它匿名描述『最小归纳总体、逐步 successor、归纳/递归接口、有限迭代与
  有限上界对照』，但不告诉 worker 任何 ZFC 公理名、Power Set、现有候选或结论。它只允许一次 P1」。
- **【自述】运行事实**（L15270）：「P1 已自然终止，且结果正是这张卡应允许的负控制……运行约 47 秒，
  Terra/max、只读、禁网、`approval=never`、零工具调用、零文件改动；轨迹显示一个完成的 turn。」
- **【自述】隔离 P1 判词**（L15313，逐字）：
  ```text
  NO_MODEL_RECALL_CANDIDATE / FORMATION_ORIGIN_NOT_SUPPLIED
  ```
- **【自述】六行有界结论表**（L15328–15335，判词列逐字）：
  | 项（导出行） | 判词 |
  |---|---|
  | 初始 formation profile（L15330） | P1 只重定位位置；不是 Z0 候选 |
  | PF-B2 process-anchor profile（L15331） | `P_MATCH_NO_SITE_WITH_SCOPE` |
  | P2/P3（L15332） | `NOT_RUN_BY_PROTOCOL_NO_FROZEN_PARENT` |
  | PF-C（L15333） | `NOT_ENTERED_NO_SURVIVING_CANDIDATE` |
  | MPIM／一般模型论文（L15334） | 保持停泊，不能拿来补候选 |
  | bare ZFC（L15335） | 没有得到矛盾、缺陷定理或"没有过程"的结论 |
- **【自述】Goal 有界完成**（L15345, L15347, L15353）：「三个提交依次为 `45aae070`（过程锚再审）、
  `7c848e4f`（冻结 P1 卡）、`5cf4ab06`（运行、闭包和有界收尾）」；「这个 Host Goal 已按『所有 active lane
  到达有界终态』的条件标记为完成。Goal 记录的实际用量为 787,114 tokens、6,628 秒，约 1 小时 50 分钟」；
  重开条件被写成三条（不同显眼基础接口／版本固定来源定义 native process-wide completion task／推翻
  H0 process-anchor 字段设计）。
- **为什么转向**：L15270 自述「按 PF-B2 合同，P2/P3 现在**不运行**，因为没有同一卡父候选可以接力」；
  L15347 之后的自述是「所有 PF-B 活跃分支现在都有明确终态」。转向的来源是**合同自身**，不是外部新证据。
- **round 0012（机械轮）**：scope 标 `no_prose_mechanical_round`，窗口 L15284–15395；导出该段为
  L15387 空 `## Codex` 轮 + L15391 `<external_codex_apps_open_page>` 机械注入。无 prose、无发现。

## L3 · P 再审与 process-anchor：H0 的五关键部分（round 0010）

- **导出行**：L15212（scope anchor_line）；L15214–15232 GPT 中继；L15302 H0 五部分。
- **触发**（L15214【自述】）：「上一 Goal 单元属于实质进展：它把 PF-B 第一轮由『似乎找到了 ω』收紧为
  『没有 surviving candidate，必须重审 P』。现在没有可确认的 live contributor 进程可以作为等待理由……」
- **【自述】核心修正**（L15218）：「H0 的关键不只是『有无穷链』，而是理论内部已有一个**可运行、可观察、
  带有限 Done 与有界正控制的过程**。PF-B R1 的 `P(a)` 与 `ω` 都只有形成或上升叙述，缺这个过程锚点。」
- **【自述】为什么这不是 ZFC 的防御结论**（L15232）：「`QuestioningDelay` 的决定性因素不是『有无穷层级』，
  而是**理论已经给出一个逐层判定、带有限燃料运行和明确停止值的原生过程；每步都有否定证据，整体仍无有限完成
  见证**。此前匿名 ZFC profile 只给了形成闭包，所以 P1 能看见位置，P2/P3 却只能诚实地说『没有同一对象的
  再入／没有生命周期』。这不是 ZFC 的防御结论，是 profile 没把 H0 的过程锚点交给三把刀。」
- **【自述】现场纪律**（L15224, L15228）：「不把并行 worktree 的未提交实验当结论」；「本分支的 `ff56db82`
  只提交了路线偏航审查，未把并行 worktree 的未提交卡片混入当前真值」；未提交卡片维持 `CANDIDATE_NOT_CURRENT`（L15298）。
- **【自述】H0 五关键部分**（L15302）：「被问的 subject、逐步 operation、有限观察、process-wide Done、
  以及有界正控制」。同段给出 PF-B2 的设问：「一个 ZFC 的基础接口如果真能成为 H0 的反向样本，理论画像必须
  自己提供能被问的过程和完成条件；不能只给一个静态形成对象，再由我们从外面补进『它其实在经历时间』。」
- **为什么转向**：转向来自 L4 的 `P_REAUDIT_REQUIRED`（L15099、L15137）——第一轮失败被诊断为
  **profile 规格不全**而非 ZFC 无隙，故必须重写发现器的最低保真度，而不是扩大文献或加样本。
- **下游**：`八线分叉后复盘.md:35` 判 dev-06 的卡点是「一直在 ZFC 的『对象形成』（幂集、ω）里找过程锚，
  没有想到 ZFC 自己的证明搜索就是一个现成的、理论原生的过程锚」，并把「H0 过程锚七字段」列为对 CG-006
  最有用的东西；`Targets与Profile.md:304`（方向 Ⅳ-2）据此把 Z0 = ZFC 的矛盾搜索描述为「理论原生的逐步过程……
  正好是 dev-06 #10 自我修正所要求的那种过程锚」。

## L4 · 方向漂移五档审查：主航向 `ALIGNED`，执行序列有偏移（round 0009）

- **导出行**：L15069（scope anchor_line）→ L15071 用户原话；L15076–15099 中继；L15103–15142 终局。
- **【原话】用户**（L15071）：「你去观察了并行 worktree，你是否可以确认，你自己的工作方向没有漂移？」
- **【自述】GPT 拒绝无条件自认**（L15076）：「我不能直接给『完全没有漂移』的结论。」
- **【自述】五档逐项判定**（L15093–15097、L15114；表格 L15109–15114，判词列逐字）：
  | 对象 | 判词 |
  |---|---|
  | Goal 的主航向 | `ALIGNED`（L15093、L15109） |
  | 初始同 profile 的 P1/P2/P3 | `ALIGNED_WITH_SCOPE`（L15094、L15110） |
  | all-subobjects→ω 的 profile 扩展 | `EXECUTION_DEVIATION`（L15095、L15111） |
  | 命名 ZFC 的 P1 | `CALIBRATION_ONLY`（L15096、L15112） |
  | 没有 surviving candidate 时的 PF-C meta 节点 | `OUT_OF_PHASE_CONTROL`（L15097、L15113） |
  | MPIM／AWCCRS | `PARKED_ALIGNED`（L15114） |
- **【自述】状态收紧**（L15133–15137，逐字）：
  ```text
  PF_B_R1 = P_MATCH_RELOCATES_FOUNDATION_FORMATION_SITES_ONLY
  Candidate-Q = UNSET
  Z0_CANDIDATE = NOT_YET
  PF_C = BLOCKED_ON_SURVIVING_CANDIDATE
  Next = P_REAUDIT_REQUIRED
  ```
- **【自述】 `ω` 的定位**（L15126）：「`ω` 现在只能叫作 **formation/completion lead**，不能叫作 `Z0_CANDIDATE`。
  如果我把『有限前缀到 ω』的外部过程直接说成 ZFC 的时间缺口，就会恰好犯我们一直防止的错误：
  把自己的计算故事塞进静态理论，再把这个故事归罪于理论。」
- **Git 谱系**：`ff56db82`（`research: audit H0-Z0 pattern-first direction`，L15091、L15116）。
- **为什么转向**：用户直接质询漂移；GPT 自述该审查「不是一句『我觉得没漂移』的自述，而是逐项对照 Goal、
  方案、NodeCard、公开输出和 trajectory 边界后的裁决」（L15091）。转向的结果是把「下一动作」从扩大样本改为
  `P_REAUDIT_REQUIRED`（L15087、L15099、L15140）。
- **下游**：`八线分叉后复盘.md:36` 把五档判定列为 dev-06 的可吸收项之一；`GUI查阅索引.md:43`
  把它列为「Pattern-First 找 Z0」线头之一。

## L5 · PF-B 第一轮：三刀盲发现只重定位 formation 位点（round 0007；round 0008 为机械轮）

- **导出行**：L15045（scope anchor_line）→ L15047 首条中继；L15051–15063 中继；L15076–15081 FileChange。
- **【自述】从等待改为过门**（L15047）：「上一 Goal 单元属于实质进展：方案、闭包、Goal 绑定和 PF-0 已进入
  版本化 owner；PF-B 的并行 contributor 已准备来源脱敏 NodeCard，并有一个受控 Discovery 节点在运行。」
- **【自述】首轮结果**（L15055–15058）：「匿名三刀首先只重新定位了幂集形成邻域，P2/P3 都拒绝把静态上升
  虚构成同一对象再入或生命周期。随后，一个不含既有答案、只给『ZFC』名称的 P1 节点独立选中了 `ω` 与有限
  后继生成之间的完成张力。这仍然只是 `MODEL_RECALL_SITE_CANDIDATE`。」
- **【自述】Master 收敛**（L15061）：「无论是匿名 all-subsets 邻域、匿名最小后继总体，还是命名 ZFC 后
  独立选出的 `ω`，P2 与 P3 都拒绝把『无限上升』升级成同一对象再入或理论原生的准入／完成生命周期……
  第一轮尚未形成可进入 PF-C 的 `Z0_CANDIDATE`。」
- **落盘物**：`audit/20261004-H0-Z0-PATTERN-FIRST-PF1-Master集成审查.md`（新增，见 L15076–15081 FileChange）。
- **为什么转向**：L15047 自述节点已停、并行写出「第一轮三刀盲发现与 Master 收敛」报告，「现在不是等待」——即
  转向的触发是并行 contributor 的终态证据出现，GPT 从「有界等待」改为「读取并过门」。
- **round 0008（机械轮）**：scope 标 `no_prose_mechanical_round`，窗口 L15045–15069；该段为
  L15053/L15059 空 `## Codex` 轮 + L15065 `<external_codex_apps_open_page>`。无 prose、无发现。

## L6 · 方案复用与 Host Goal 绑定（round 0005、round 0006）

- **导出行**：L14833/L14835（0005 用户原话）；L14856/L14858（0006 用户原话）；L14840–14890 GPT。
- **【原话】用户**（L14835）：「你把后续的工作的方案写出来，起好名称。在/goal 中引用你的方案和对应的
  认知闭包，驱动你自己完成后续的工作。你自己管理/goal。」
- **【自述】GPT 复用而非另造**（L14846）：「我发现已有一个并行 worktree 已经完成了与本请求精确一致的方案草案，
  并以可恢复 commit 固定：`a9c27282` 的 **`H0-Z0-PATTERN-FIRST-CONVERGENCE-SOP`**……
  我会复用这份已审阅方案而不另造第二套。」
- **【原话】用户**（L14858）：「你是要跟它做一样的事吗？那何必呢？」
- **【自述】GPT 收敛职责**（L14863–14865）：「你说得对，我不应该再做一套同义方案，更不应该重新启动一遍它
  已经在跑的 P1/P2/P3。我已经确认：另一个 worktree 的 `a9c27282` 已经把
  `H0-Z0-PATTERN-FIRST-CONVERGENCE-SOP` 写好……我的正确职责是把这份已提交方案作为唯一方案复用，
  把那个 worktree 的工作作为 `PF-B` 的 contributor 输入，随后由我做来源、同一任务和 Git 集成裁决。
  剩下真正尚未有人完成的部分只有两项：为这份方案建立**可审计认知闭包**，并创建一个引用『该方案 + 该闭包』
  的 Host `/goal`。」
- **Git 谱系**：`fe07324a`（闭包、索引与 Goal 绑定，L14882、L14953）；`df4b636c`（闭包索引状态复核 PASS，L14955）。
- **PF 链路设问**（L14894–14937）：「把『发现 Z0』和『证明 ZFC 有问题』严格分开」，并给出 PF-A/B/C/4/5 与
  `SOURCE_DIRECT_PAYMENT_CONTROL`、`SOURCE_ACCEPTANCE_UNDERDETERMINED_WITH_SCOPE`、`H0_Q_PRESERVED_WITH_SCOPE`、
  `P_MATCH_NO_SITE_WITH_SCOPE`（L14935）与 `PARKED_SOURCE_CONTROL`（L14937）等有界结果族。
- **为什么转向**：用户先要求「写方案、起名、/goal 自管」（L14835），随即用 L14858 一句否决同义重复。
  GPT 的转向自述是「我不应该再做一套同义方案，更不应该重新启动一遍它已经在跑的 P1/P2/P3」（L14863），
  于是把自己压缩成「复用方 + 闭包/Goal 提供方」。
- **下游**：`assets-ledger.md:604`（A-0556）把 dev-07 记为「该 SOP 的原始创建指令所在线
  （本线=方案出生地，dev-06 系复用方）」；`GUI查阅索引.md:43` 的线头列为 `dev-06/0005–0010`。

## L7 · MPIM 降格 + 认知闭包执行失败自省（round 0003、round 0004）

- **导出行**：L14609/L14619（0003 用户原话，annotation 包裹轮）；L14624–14694 GPT；
  L14701/L14703（0004 用户原话）；L14708–14818 GPT。
- **【原话】用户**（L14619，随 response-annotation）：「这事很重要吗？你必须参考它吗？
  你自己的神经网络中的知识库中没有吗？」
- **【自述】首条判 MPIM 不支配路线**（L14624）：「这条 MPIM 讲座线索本身**不应当支配路线**。」
- **【自述】消歧结果**（L14630）：「MPIM 这条线在 H097 中完成了它应有的最小工作——证明讲座页混合了两条不同
  模型叙述，且没有给出 fixed H0 的映射或基础充分性判词。」
- **【自述】判 MPIM 不是主线**（L14636–14664）：「MPIM 的讲座页不是这项研究的必经来源，也不应继续占据主线……
  讲座页提到的第一条 Cubical Agda proof-to-set-theory 路线没有给出模型名称；紧随其后的 AWCCRS 预印本被页面
  明确说成在 *different* 的 cubical-set category 中建立的另一条 HoTT 模型路线。两条链都没有给出 fixed H0 的
  `H0Map`、H0 的 `never`／有限停机观察保持，或真正的 `AdequacyLift`。」
- **【自述】判词**：`VARIANT_GAP_WITH_SCOPE`（AWCCRS／H098-B，L14688）；
  `PARKED_CONDITIONAL_SOURCE_BRANCH`（MPIM／AWCCRS，L14776）。
- **【原话】用户**（L14703）：「你工作的时候，不维护认知文档，你干着干着就忘了啊，
  为什么认知闭包没有达到这个效果呢？」
- **【自述】GPT 承认真实执行失败**（L14708）：「你说得对。这不是『认知闭包做得不够多』，而是我在最关键的一个
  环节失效了：我把你对 MPIM 支线的质疑当成了对话中的分析问题，没有把它识别为**会改变当前下一动作与证据
  优先级的用户修正**。」
- **失败的直接后果**（L14714–14720）：「`F-050` 当前仍把 `H098-A/H098-B` 写成下一最小行动，而且已有一个
  H098 的来源节点在按这个旧队列运行」；H098 App Server 进程结束而无结果报告，只能登记为
  `STALE_PENDING_PRIORITY_REALIGNMENT`，「不能被当成主线证据」。
- **【自述】判词**：`EXECUTION_DEVIATION / COGNITIVE_WRITEBACK_OMISSION`（写入 rulings，L14763）；
  `H098_PRE_REALIGNMENT_CONTROL_RECORDED`（L14788）。
- **【自述】新运行顺序**（L14804）：「用户原件 → rulings → Feature 的 active / parked / next action →
  MEMORY 当前队列 → direction 与 task SOP → 回读这些 owner → 才能启动或继续节点」。
- **Git 谱系**：`131cecba`（`research: prioritize P-first H0-Z0 discovery`，L14730/L14816），
  推送 `origin/codex/h0-z0-priority-realignment`；自述「它没有新增数学结论，也没有把 H098 的来源控制
  夸大成 ZFC 结论」（L14730）。
- **为什么转向**：L14619 质疑来源支线的必要性与模型自身知识库的角色；GPT 的自述转向理由是
  「我的内在数学知识应该先负责**发现 Z0 的候选位置**；来源只在我们要断言某个具体模型、某个 ZFC 扩展或某个
  共同体验收实际做了什么时，才承担可复核证据的责任」（L14630 同段）。L14703 追问闭包失效后，
  第二次转向是把「认知加载」补成「认知加载 + 认知事务」。
- **下游**：`GUI查阅索引.md:43` 把 `dev-06/0004` 列为治理教训线头：「用户修正必须立刻写回 owner；
  『一次只推进一个单元』不等于『做完一个就停』」。

## L0 · 机械前缀（round 0001、round 0002）——机械轮，无 prose

- scope 对两轮均标 `anchor_status=no_prose_mechanical_round`，`anchor_window = [14597, 14609]`。
- 导出 L14598–14604：`<environment_context>`（`<cwd>` 为 cad0 worktree、`current_date` 2026-10-04、
  workspace_roots 含 cad0 与两个 visualization 根）。
- 导出 L14605–14607：`## User` 块内仅 `<external_codex_apps_open_page>{"page_id":null}`。
- **无 prose、无判词、无转向**；按 R6 仍在 DISCOVERIES.tsv 各占一行，以避免「机械轮=未覆盖」的假阴性。

---

## 附 A · 本线关键 Git 谱系（全部取自导出自述，未在本机复跑 git）

| 提交 | 出处（导出行） | 自述内容 |
|---|---|---|
| `131cecba` | L14730、L14816 | research: prioritize P-first H0-Z0 discovery（MPIM/AWCCRS 降为条件性来源支线） |
| `de13da0c` | L14951 | 复用 `H0-Z0-PATTERN-FIRST-CONVERGENCE-SOP` |
| `fe07324a` | L14882、L14953 | 建立闭包、索引与 Goal 绑定 |
| `df4b636c` | L14955 | 闭包索引状态复核为 PASS |
| `ff56db82` | L15091、L15116 | research: audit H0-Z0 pattern-first direction |
| `45aae070` | L15345、L15436 | H0 process-anchor 再审 |
| `7c848e4f` | L15345 | 冻结新的去标识 P1 盲态卡 |
| `5cf4ab06` | L15345、L15347 | PF-B2 运行、认知闭包、逐 KC 审计和有界收尾 |
| `86ad33c4` | L15418、L15451、L15463 | archive: preserve current worktree dialogue records（→ `origin/dev-06`） |

## 附 B · 身份标注约定

- 【原话】＝用户在 GUI 导出中的原文，逐字摘录（L 号为导出行）。
- 【自述】＝GPT/Codex 在导出中的最终回答或中继自述，**未逐项复核**；
  `八线分叉后复盘.md:6` 的读法声明亦作此区分。
- 【证明】＝机器证明/形式化证据（本线 unique 段内**没有**：GPT 在导出自述中明确「没有新数学命题，
  因此没有把这次行为实验伪装成 Lean 或 Agda 的数学证明」）。
- 【判断】＝审计者或本提取员的判断。
- `audit/GUI-ASSET-RECOVERY/assets-ledger.md` 与 `D3-资产登记v2-20261007.md` 中的 A-05xx 资产条目
  属**后续资产回收审计**的材料，本文件只在需要指明下游沉淀处引用，不充当本轮的原始判词。

## 附 C · 本线未产出任何数学结论

按 R7，本文件不含任何数学结论。dev-06 unique 段的全部判词都是**方法/治理/有界实验**层面的
（`P_MATCH_NO_SITE_WITH_SCOPE`、`NO_MODEL_RECALL_CANDIDATE` 等），且 GPT 在导出自述中明确
「它没有新增数学结论，也没有把 H098 的来源控制夸大成 ZFC 结论」（L14730）与
「bare ZFC 没有得到矛盾、缺陷定理或『没有过程』的结论」（L15335）。任何把它们读成
ZFC 数学性质的说法都是越界。
