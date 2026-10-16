# dev-09 研究脉络（THREAD.md）

> 线：`dev-09`（GUI 标题「🌟 09 - 哥德尔」；worktree `a38d` → `t-precision-tobs` → `t-precision-continuous` → `t-precision-tmeta` → `godel-zfc-r3-replay` → `dev-09-snapshot` → `godel-zfc-dev09-integration`）。
> 导出：`git-worktree对话录/dev-09 - 20261005T051816Z-01a10843-afd2-7063-82f8-259c56f359e9-a79ef407f501-gui.md`（18,698 行；`prefix_end_line = 15891`；`unique_lines = 2087`，全部落在 15892–18698）。
> 分叉：`fork.parent_branch = dev-08`、`parent_doc = 113`、`parent_rollout = 01a107f1-c8f6-7bb0-8b78-484d4565d489`（同 `audit/GUI-SYNTH-REDO/qa/dev-09/_branch.json`：`contiguous_in_own_export = true`，`own_docs = 16`）。
> **轮数口径（R4）**：本文论轮次一律用 `scope.json` 的 QA 块坐标 `docs[].doc`（本线自有轮 16 个，四轮机械轮也计）；裁决 #3 分线轮数 **8** 只作并列引用（来源 `audit/GUI-ASSET-RECOVERY/ledger.jsonl` PROTOCOL_NOTE `ruling3`），两者不互换。
> 锚点：`anchored 12`（`user_block 8`：0003、0004、0005、0008、0009、0010、0011、0016；`codex_fallback 4`：0006、0012、0013、0014）、`mechanical_window 4`（0001、0002、0007、0015）、`export_absent_prose 0`、`unresolved_prose_docs` 空。
> 层数：**9**。L0 机械轮（#0001、#0002）→ L1 想法 T 与 `T-PRECISION-DIAGONAL-SOP`（#0003–#0005）→ L2 T0 与连续执行 C-367／C-368 与 `set.mm` 拒绝（#0006–#0008，含机械轮 #0007）→ L3 远程 `dev-09` 快照 `1c34aaee`（#0009）→ L4 哥德尔路线继续性澄清（#0010）→ L5 `GODEL-ZFC-CONVERGENCE-SOP` 建立（#0011）→ L6 R3/R4 刀具链与 CCTTmini（#0012–#0013）→ L7 总闭环 C2/C3（#0014）→ L8 终局保存 merge（#0015–#0016）。
> 阅读顺序：**尾 → 分叉点**。`export_line` 均指上述 GUI 导出行号（不是 `_index.jsonl` 的 rollout 行号）；`【原话】/【自述】/【证明】/【判断】` 按 R3 标注；本文件不产出任何数学结论（R7）。
> 配套清单：`DISCOVERIES.tsv`（同目录，50 行 × 12 列，覆盖本线全部 16 个自有轮；其中 4 轮机械轮判词标 `MISSING` 并说明；另 2 行 `round = —` 的溯源行只登记 SHARED 前缀段的判词归属，不计入轮覆盖）。层名与本文件的小节一一对应；每行的 `export_line` 都等于 scope 的 `anchor_line`，四轮机械轮则取落在 `anchor_window` 内的 User 块内容行。
> 主干旁证：`.claude/goals/CG-006-zfc-complete-formalization/{八线分叉后复盘.md,GUI查阅索引.md,Targets与Profile.md}`、`docs/ZFC时间维度观察力不完备-哥德尔式Q终局报告-20261008.md`。

## 分叉入口（本线继承了 dev-08 #113 的什么）

- **分叉时点**：`prefix_end_line = 15891`。父线 dev-08 #113 的 Codex 终局回复末段在 `export_line 15881–15883`（「对一个固定的 ZFC-facing acceptance interface，能否构造一个保真自编码过程 d…」），`### Files changed in this reply` 落在 15887–15888；同一 `## User` 块标题行 15890 在两个导出中都出现，但其后内容分道——dev-08 侧是本线之外的 #114「调整方案」提问（`git-worktree对话录/dev-08 -…-gui.md:15892`），dev-09 侧从 15892 起是 environment_context 机械块。
- **继承的靶与刀具**【自述】：dev-08 #113 的问答确立了 `Code / Accept / OriginDone / diag / Reflection` 五个角色与六道门，CG-006 把它记为「哥德尔结构草图与六道门」之一（`GUI查阅索引.md:25`）。dev-09 的第一个自有轮（0003）即把它升级为想法 **T**。
- **本线没有共享前缀骨架层任务**：`unique_ranges` 的 `[1,1]` 是标题行「# 🌟 09 - 哥德尔」，其余唯一区间全在 15892 之后。下文 L0 只登记本线自有的机械轮，不建共享前缀骨架层；少数必须溯源的 SHARED 段判词只作为 `round = —` 的登记行进 `DISCOVERIES.tsv`（D09-0049、D09-0050）。

---

## L8 终局保存：远程 `dev-09` 双亲 merge（#0015–#0016）

- **目标/SOP**：无新 SOP；0015 是总闭环之后的机械续跑块（`<external_codex_apps_open_page>`，`export_line 18619–18621`），0016 由用户要求把当前 worktree「从代码到文档，包括对话录记录文件」保存到远程 `dev-09`【原话】「你现在的这个git worktree上的工作，从代码到文档，包括对话录记录文件，我希望保存到远程的dev-09分支上。」（`export_line 18625`）。
- **GPT 做了什么【自述】**：冻结 contributor 谱系 → 干净 integration worktree → 合并预演发现 **24 个本地提交 vs 35 个 `dev-09` 提交**分叉、**九个真实语义冲突**（证明矩阵、运行闭包、审计入口、理论精度方案、规则裁定、认知闭包）→ 逐文件语义裁决（工作面取当前 worktree 版本，`dev-09` 旧快照保留为 merge 第一父）→ 双亲 merge `ac6391b6` → 读远端 OID 裁决而非盲目重推。见 `export_line 18630–18693`。
- **发现与判词（逐字）**：`DUPLICATE_SESSION`（`export_line 18693`：「本次最终回复的自动 `dev-notes` 归档遇到 `DUPLICATE_SESSION`，原因是合并后的 `dev-09` 已有不止一份记录声明同一 Codex session。归档工具按合同拒绝擅自选择、覆盖或删除其中任一份」）。
- **实物**：`origin/dev-09` = `ac6391b6d559bcc1999394b182b795c167bbd6ef`（merge: preserve godel zfc convergence work on dev-09；第一父 `1c34aaee`、第二父 `2e64d99a`）；远端树可见 `HoTT/formal/cubical-godel-fragment/`、`20261005-GODEL-ZFC-I-001-声明路线总合成.md` 与既有对话记录。GUI 查阅索引把本轮列为「各线推送、快照、交接」（`GUI查阅索引.md:38`）。
- **为什么转向**：上一轮（0014）已把 `/goal` 按 SOP 的 C2/C3 关闭【自述】「该 `/goal` 已按 SOP 的 C2/C3 结束；系统记录的累计使用量为 **3,370,473 tokens**，累计执行时间约 **2 小时 58 分钟」；数学路线到达合法停止条件后，剩余动作只剩把这条 contributor 谱系落回它自己的分支——而这正是用户在 0009 已经做过一次、在 0016 因新分叉而必须重做的事。

## L7 总闭环：SOP 的 C2 与 C3（#0014）

- **目标/SOP**：`GODEL-ZFC-CONVERGENCE-SOP` 的下一步——由 0013 指定的 `GZ-012 / R4-CCTTMINI-REPRESENTABILITY-BOUNDARY-001`（`export_line 18200`），随后转 `S-001`，最后进 I-001 总合成门。
- **GPT 做了什么【自述】**：GZ-012 闭合为对象层缺口（提交 `aead18da`）→ S-001 审计 `SameFullQ` 与归因六前提 → I-001 逐路线核对 C1/C2/C3。见 `export_line 18417–18610`。
- **发现与判词（逐字）**：
  - `ALL_DECLARED_ROUTES_REJECTED_WITH_SCOPE`、`FORMAL_TARGET_UNDERDETERMINED_WITH_SCOPE`、`NO_BARE_ZFC_OBJECT_LANGUAGE_INCONSISTENCY_CLAIM`（`export_line 18461–18463`）；
  - `TOTAL_CLOSED_BY_C2_C3` / `DECLARED_ROUTE_DENOMINATOR_ONLY`（`export_line 18572–18573`）；
  - A-001 三判词 `SOURCE_TASK_CONTRACT_DIVERGENCE_ESTABLISHED_WITH_SCOPE` / `BRIDGE_UNPAID_FOR_STRICT_CONTROL` / `BARE_ZFC_SEMANTIC_COMPLETION_INTERFACE_UNDERDETERMINED`（`export_line 18495–18497`）；
  - `GZ-012` 判词：「CCTTmini 的 self-code syntax 和 meta-level certificate witness 没有被同一理论内部的可表示性定理接起来，因而不能充当 HoTT 的 proof predicate 或 Gödel固定点」（`export_line 18427`）。
- **实物**：`audit/20261005-GODEL-ZFC-I-001-声明路线总合成.md`、`audit/20261005-GODEL-ZFC-S-M4M5-001-SameFullQ与归因对账.md`、`audit/20261005-GODEL-ZFC-G1-R4-010-CCTTmini表示性边界.md`；提交 `58b68723`/`6a091daa`/`5ac3d1d7`/`aead18da`/`4f8d78e1`/`2e64d99a`，受保护 ref `codex/godel-zfc-r3-replay-run`。
- **为什么转向**：GZ-012 的缺口明确指向「D、A、H、G1 四条证据能否共同支付 `SameFullQ` 与 bare-ZFC attribution」【自述】「当前路线自动转入 `S-001`：不再增加局部片段，而是审计 D、A、H、G1 四条证据能否真的共同支付 `SameFullQ` 与 bare-ZFC attribution。」——因为继续做 CCTTmini 片段只会把「锻造片段本身」变成新终点，违反 SOP 的非饥饿规则（该规则在 0013 的同一根线上已经触发过一次）。

## L6 R3/R4 刀具链与 CCTTmini 片段（#0012–#0013）

- **目标/SOP**：`GODEL-ZFC-CONVERGENCE-SOP` 首个 `/goal`（`export_line 17657–17671` 注入 objective），先 `G0-R3-SOURCE-REPLAY-001`，随后 `G1/R4`；0013 是同一条 `/goal` 的连续推进。
- **GPT 做了什么【自述】**：历史 Coq 包 `uds-psl/coq-synthetic-incompleteness@cd7d849` 被判 `LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED` / `LATER_COMMAND_SOURCE_MISMATCH`，Docker 不可连 → 切 Lean Foundation `FormalizedFormalLogic/Foundation@f3972f4204fc…` → GZ-002 主/负运行与精确 rerun → GZ-003~005 目标链（groupoid → cooltt → cubicaltt → cctt）→ GZ-005 输入域资格化 → GZ-006 derivation contract 缺口 → GZ-007 三候选三角分诊 → GZ-008~011 的 CCTTmini₀ 片段（C-370–C-382）。
- **发现与判词（逐字）**：
  - `LATER_COMMAND_SOURCE_MISMATCH`、`LOCAL_EVIDENCE_PASS_NOT_VERSION_CLOSED`（`export_line 17748`、`17784`）；
  - cctt 边界判词：「cctt 的命令行进程即使打印类型错误，仍返回退出码 0。**所以“shell exit 0”甚至不能作为它的 checker 接受判据。**」（`export_line 17870`）；
  - GZ-006 判词：「`check` 的接口是 Haskell 的 `P.Tm -> GTy -> IO Tm`，返回 elaborated term，不返回一份可编码的 derivation certificate」（`export_line 17944`）；
  - GZ-007 三角对照：`cart-cube = 语义模型充分，证明码层缺失` / `redtt = 语言实现充分，证明证书与总检查器层缺失` / `TTasQIIRT = 内在 syntax 充分…`（`export_line 17980–17987`）；
  - 非饥饿自审：「GZ-008、009、010、011 已经连续四次深化同一条 `G1-R4` 线，而 `D-TDIAG` 已是 READY。继续只扩展 CCTTmini 会违背这份闭环 SOP 的要求，并把“锻造片段”本身变成新的终点。」（`export_line 18160`）；
  - 0013 终局恢复点 `GZ-012 / R4-CCTTMINI-REPRESENTABILITY-BOUNDARY-001`，最新受保护提交 `5ac3d1d7`（`export_line 18200`）。
- **实物**：`HoTT/formal/external-foundation-incompleteness/`（`Qualification.lean`、`WrongMissingSoundness.lean`、`CLAIM-R3-FOUNDATION-INCOMPLETENESS.md`）、`HoTT/formal/cubical-godel-fragment/`（`CCTTmini.agda`、`CCTTminiNat.agda`、`CCTTminiFormula.agda`、`CCTTminiFormulaCode.agda` + 三份 CLAIM + 三份 `Wrong…`）、`HoTT/formal/external-cctt-r4/`；提交 `cbceedf0`(GZ-005)、`0c7d55ce`(GZ-006)、`2178d788`(GZ-007)、`58b68723`、`6a091daa`(A-001)、`5ac3d1d7`(H-001)。
- **为什么转向**：用户用 `/goal` 把 SOP 变成「正在运行的总目标」【原话】「按照SOP=GODEL-ZFC-CONVERGENCE-SOP，恢复认知闭包 GODEL-ZFC-CONVERGENCE-001，并继续执行哥德尔式 ZFC 理论精度收敛闭环。…不得把一个局部关闭写成总完成。」（`export_line 17657–17671`）；而内部的每一次换靶都由前一条证据的形状决定——coq 包被版本闭合阻断就切 Foundation，cooltt/cubicaltt 缺工具链就换实现，同一路线连续收紧四次就按非饥饿规则切到 `D-TDIAG`【自述】「我会把 CCTTmini 的 representability 问题登记为 **parked、可重开**，转到 `D-TDIAG`」。

## L5 自己给自己设 `/goal`：哥德尔式 ZFC 收敛闭环 SOP（#0011）

- **目标/SOP**：用户要求一套「不会在中途停下」的自管机制，并要求给方案一个可被 `/goal` 引用的名字【原话】「那么你如何给自己设置好/goal，才能确保你自己不要再在中途停下，并且：**给方案一个名字，方便以后你在／goal中引用这个方案名，同时维护好这个方案你在执行的过程中的对应的认知闭包，从而保证你工作在多个Session的过程中，跨越压缩边界之后，可以保持前后认知的一致性，可以持续加载和写回方案执行过程中，对应的认知闭包。**」（`export_line 17462`）。
- **GPT 做了什么【自述】**：新建 **`GODEL-ZFC-CONVERGENCE-SOP`**（中文名「哥德尔式 ZFC 理论精度收敛闭环 SOP」）+ 四个分片 + `认知闭包/GODEL-ZFC-CONVERGENCE-001.md`；把已有三条线（`T-PRECISION-DIAGONAL-SOP`、`R3–R4` 任务、`ZFC-H0-FINAL-PROOF-CLOSURE-SOP`）降为它的理论规格/证明论路线/ZFC 实例路线。见 `export_line 17465–17647`。
- **发现与判词（逐字）**：
  - 状态机铁律：「这里最重要的一条是：**`LOCAL_CLOSED` 必定进入 `SUCCESSOR_REQUIRED`。**」（`export_line 17553`）；
  - 「“这一轮暂时想不到下一步”“这篇论文不够”“本机编译器没装好”“跑超时了”，都不再是总停止理由。」（`export_line 17563`）；
  - `GOAL_PREPARED_NOT_AUTOSTARTED`（`export_line 17633`）。
- **实物**：`dev-docs/哥德尔式ZFC理论精度收敛闭环SOP.md` + `001 - 总目标、边界与路线所有权.md` / `002 - 路线图、最小单元与证据产物.md` / `003 - 连续执行、局部停止与总完成状态机.md` / `004 - 认知闭包、恢复、写回与Goal启动词.md`；`认知闭包/GODEL-ZFC-CONVERGENCE-001.md`；提交 `0406460a`（方案）、`f95dd884`（自审），本地 ref `codex/godel-zfc-convergence-plan`。
- **为什么转向**：这是对 0008 那次「调度语义错误」的制度性收口。GPT 自己在 0010 承认停止的是归因桥而非方法后【自述】「过去的问题是把一个局部 verdict…误读成总路线结束」（`export_line 17538`），若不把停止权从「一个原子单元」上移到「总路线层」，同一个错误会在下一个 Session 重演——用户要的正是跨压缩边界仍成立的机械约束，而不是一句提醒。

## L4 澄清：哥德尔路线并没有走不下去（#0010）

- **目标/SOP**：无新 SOP；`repo-cognitive-closure` 建立「路线能否继续」的最小证据闭包。
- **GPT 做了什么【自述】**：先核对当前 worktree 现场（detached HEAD + 未提交 ZFC–H0 材料；T 方案在此仍标「已准备、尚未执行」），再重读 `T-DIAG/T-Meta/T-ZFC` owner，把「什么已证明、什么缺来源、什么可以继续」拆开；用 `dev-notes-archive` 保存这轮澄清。见 `export_line 17385–17458`。
- **发现与判词（逐字）**：`ACTIVE / TASKSPEC_FROZEN / IMPLEMENTATION_NOT_STARTED`（`export_line 17405`、`17419`）；T-DIAG 规格明写 `NO_DIAGONAL_THEOREM_YET`（`export_line 17438`）。
- **实物**：`.codex/research/hott/R3-R4-GODEL-RETURN-001.md`；`dev-docs/理论精度与哥德尔式自反方案/003 - T-DIAG自编码完成接口与对角化规格.md`；`audit/20261004-ZFC-H0-FINAL-PROOF-CLOSURE-F1E-FORCING-TICKS-CLOCKED-LIFT.md`。
- **为什么转向**：用户把 0009 之前 S 式收尾读成路线终止【原话】「你的意思是，哥德尔这条路，你已经没有办法继续推进下去了，是吗？」（`export_line 17382`）——GPT 判定这是自己的表述缺陷：被判「无法继续」的只是 `set.mm` 那个具体候选接口的实例化，而`R3`/`R4` 两段技术核仍各有明确的第一动作；若不拆开，下一次 Session 会把「当前来源分母收束」误读成「哥德尔路线穷尽」（这条澄清正是 L5 建 SOP 的直接动因）。

## L3 第一次保存：远程 `dev-09` 快照（#0009）

- **目标/SOP**：无新 SOP；Git 保存操作。
- **GPT 做了什么【自述】**：按「完整工作树快照」而非「推已提交历史」处理；盘点得 7 个非忽略增量（1 份修改的 `dev-notes/0109…` + 六份未跟踪 `git-worktree对话录/`）；在独立 worktree `dev-09-snapshot` 建 `dev-09`，逐文件比对字节与 SHA-256，非 force push。见 `export_line 17310–17378`。
- **发现与判词（逐字）**：「`git diff --check` 对保存的对话文本报告了既有尾随空白…为了保证对话记录逐字保存，我记录了警告而没有格式化或删除这些字符。」（`export_line 17370`）。
- **实物**：`origin/dev-09` = `1c34aaee734ef983d4f63eef8d8012b7dc7f3624`（snapshot: preserve current dev worktree and dialogue records）；`audit/20261004-DEV-09-WORKTREE-SNAPSHOT.md`。GUI 查阅索引把本轮列为推送/快照线（`GUI查阅索引.md:38`）。
- **为什么转向**：上一轮 0008 把 T 路线收在 `BARE_ZFC_COMPLETION_INTERFACE_FORMAL_TARGET_UNDERDETERMINED_WITH_SCOPE`，工作树里同时有他人 `dev-notes` 与六份未跟踪对话录；用户此时要求保存【原话】「你现在的这个git worktree上的工作，包括对话录记录文件，我希望保存到远程的dev-09分支上，你打算如何处理？」（`export_line 17307`）。「包括对话录记录文件」这几个字决定了它必须是快照提交而不能只推 `dev` 历史。

## L2 T0 与连续执行：C-367／C-368 与 `set.mm` 拒绝（#0006–#0008）

- **目标/SOP**：0006 起执行 `T-PRECISION-DIAGONAL-SOP` 的 T0（`/goal` objective 在 `export_line 16741–16749` 注入，末尾明写「必须做出来再停下，否则不要停下。」）；0007 是同一条 `/goal` 的机械续跑块；0008 进入 `T-DIAG-001 → T-Meta → T-ZFC` 的真实研究。
- **GPT 做了什么【自述】**：先承认调度语义错误，把「每次只推进一个最小判别单元」从停机条件降级为验证粒度；随后重开连续 Goal，连续完成 T-DIAG-001（C-368）、T-Meta（同一任务桥审计）、T-ZFC（`set.mm@160ebb…` 逐字段实例化裁决）。见 `export_line 16992–17303`。
- **发现与判词（逐字）**：
  - 四处终局判词：`CURRENT_T_PRECISION_SOURCE_DENOMINATOR_CLOSED_WITH_SCOPE` / `T_META_SAME_TASK_BRIDGE_UNPAID_WITH_SCOPE` / `T_ZFC_CURRENT_INTERFACE_REJECTED_WITH_SCOPE` / `BARE_ZFC_COMPLETION_INTERFACE_FORMAL_TARGET_UNDERDETERMINED_WITH_SCOPE`（`export_line 17212–17215`）；
  - `T0_COMPLETED / T-OBS_C367_MACHINE_PROVED_WITH_SCOPE`（`export_line 16927`）；
  - 自省判词：「这不是数学上的谨慎，而是我把研究程序做成了审批程序。」（`export_line 17000`）。
- **实物**：`HoTT/formal/t-precision-observation/ObservationPrecision.lean`、`HoTT/formal/t-precision-diagonal/AcceptanceDiagonal.lean`、`HoTT/verification/runs/20261004-MP-T-PRECISION-TDIAG-001-02/`、`audit/20261005-T-PRECISION-TMETA-001-SAME-TASK-BRIDGE-CARD.md`、`audit/20261005-T-PRECISION-TZFC-001-SETMM-INSTANCE-CARD.md`、`audit/20261005-T-PRECISION-CURRENT-SOURCE-DENOMINATOR-CLOSEOUT.md`；提交链 `575fce29`/`3e8c6111`/`7255929e`/`d2c8aa58`/`65b7edec`/`b150cd84`/`0131bc6b`（`origin/dev` = `0131bc6b`）。
- **为什么转向**：用户在 T0 刚闭合时直接质疑【原话】「为什么你没有全部做完再停下？」（`export_line 16989`）——GPT 判定自己把 SOP 中的「原子单元」节拍误当成了总停机条件，并把闭包里的 `NEXT_UNIT_REQUIRES_NEW_GOAL_DECISION` 视为把用户持续授权错误缩窄；纠正之后才可能在同一轮内完成 T-DIAG→T-Meta→T-ZFC 的三连推进，也才有可能发现真正的缺口在 `set.mm` 的 proof/database validity 与原过程完成之间无同源 `ρ`/bridge。

## L1 想法 T 与其方案化（#0003–#0005）

- **目标/SOP**：无前置 SOP；0004 起用户指示把两轮问答固化为「新方案」，0005 逐字贴回原文要求核验；随后建立 `T-PRECISION-DIAGONAL-SOP` 与 `T-PRECISION-DIAGONAL-001` 闭包。
- **GPT 做了什么【自述】**：把「ZFC 有问题」上移为理论观察精度问题，提出 T 的四层结构（相对可定义的精度 → 哥德尔进入点 → 元元层 → 哥德尔式升级候选）与六个观察程序问题；反对「一切不完备都等于维度缺失」的过强版本；给出 `T-OBS / T-DIAG / T-ZFC` 三层父命题。见 `export_line 15909–16134`、`15911–16134`。
- **发现与判词（逐字）**：`PLAN_READY / EXECUTION_NOT_STARTED`（`export_line 16671`）。
- **实物**：`sources/prompts/Codex-理论精度与哥德尔式自反两轮用户原文-20261004.md:15`（用户原话一一手快照，`# 🌟 09 - 哥德尔` 导出 `export_line 15906`）；`dev-docs/理论精度与哥德尔式自反方案.md` + 四分片（001 原始两轮对话与来源边界 / 002 T-OBS / 003 T-DIAG / 004 T-ZFC）；`认知闭包/T-PRECISION-DIAGONAL-001.md`；提交 `3635cbfd`/`2570f8a6`/`e3d9d729`（fast-forward 进 canonical `dev`）。
- **为什么转向**：用户在 dev-08 #113 的哥德尔「神似」讨论之后，把自己的问题升级成比 ZFC 更高的对象【原话】「我在想，我们这个事情啊，是在找ZFC的问题，但是这个问题的本质正像我说过的，是理论维度缺失、理论维度观察力不完备、理论精度不够导致的。这个想法=`T`其实是一个有点类似哥德尔不完备性的想法，它超越了对于单个理论，比如ZFC的考察。…我们何止可以和哥德尔神似，我们简直可以和哥德尔“神交”！…在证明想法T的过程中，我们得到了一套观察任意理论的脚手架，这套脚手架可能会告诉我们，如何捕捉ZFC的具体理论精度问题的方法。」（`export_line 15906`）。GPT 随即要求把靶心上移写成可证形状【自述】「当前总证明 Goal 仍保持暂停，我先恢复这份新 worktree 的认知边界，再给出严格的可证明形状。」（`export_line 15911`）；0004 用户进一步要求命名与跨 Session 连续性【原话】「给方案一个名字，方便以后你在/goal中引用这个方案名」——这一步的直接产物就是 `T-PRECISION-DIAGONAL-SOP`，也是后面五层所有 SOP 的原型。

## L0 机械轮（#0001、#0002）

本线共四轮 `anchor_status = no_prose_mechanical_round`：**#0001、#0002** 是想法 T 出现前的两个纯机械 User 块，归本层；**#0007** 夹在 L2 的 T0 闭合与 0008 追问之间、**#0015** 夹在 L7 总闭环与 L8 保存之间，按所在内容层计（L2／L8）。四轮都计入本线自有轮 16 个（R4）。

| 轮 | 归属层 | export_line（User 块内容首行，落在 scope `anchor_window` 内） | 内容 | scope `anchor_window` | 备注 |
|---|---|---|---|---|---|
| 0001 | L0 | 15892 | `<environment_context>`：cwd `/Users/aurolafly/.codex/worktrees/a38d/…`、shell zsh、current_date 2026-10-04、三个 workspace_roots、`permission_profile type="disabled"` | [15892, 15904] | QA 切片 `0001.md`：`items: 0`、rollout `line_from=7/line_to=7`（rollout 坐标，非导出行号，R1）；`notes/dev-09.md` R0517 同记 |
| 0002 | L0 | 15902 | `<external_codex_apps_open_page>{"page_id":null}</external_codex_apps_open_page>` | [15892, 15904] | 与 0001 共用同一窗口；`notes/dev-09.md` 记「L15902 external 页」 |
| 0007 | L2 | 16985 | 同上，`{"page_id":null}` | [16876, 16987] | 位于 0006（T0 闭合）之后、0008（追问）之前 |
| 0015 | L8 | 18621 | 同上，`{"page_id":null}` | [18425, 18623] | 位于 0014（总闭环）之后、0016（保存推送）之前 |

- **为什么没有转向**：四轮的 User 块都只有 environment／page/goal 注入一类的机械内容，没有自然语言提问，因此不产生任何研究决定、也不改变路线；它们在时间上只是相邻实质轮的续跑噪声（0001/0002 之后才是想法 T 的 0003，0007 之后才是「为什么你没有全部做完再停下？」的 0008，0015 之后才是保存推送的 0016）。把它们单列一层是为了让轮覆盖（16 个）与「有内容的层」区分开，而不是暗示它们有研究含义。

## 附录 A：判词在本线内外的逐字对照（R2）

| 判词 | 首现（本线唯一锚） | 本线轮 | 同时在别处 |
|---|---|---|---|
| `T0_COMPLETED / T-OBS_C367_MACHINE_PROVED_WITH_SCOPE` | 16927 | 0006 | — |
| `CURRENT_T_PRECISION_SOURCE_DENOMINATOR_CLOSED_WITH_SCOPE` | 17212 | 0008 | — |
| `BARE_ZFC_COMPLETION_INTERFACE_FORMAL_TARGET_UNDERDETERMINED_WITH_SCOPE` | 17215 | 0008 | 与 0014 的 `FORMAL_TARGET_UNDERDETERMINED_WITH_SCOPE` 同族；`八线分叉后复盘.md` 另记为 dev-01 F-050 的 `BARE_ZFC_COMPLETION_INTERFACE_FORMAL_TARGET_UNDERDETERMINED`（dev-01 侧，非本线锚） |
| `SOURCE_TASK_CONTRACT_DIVERGENCE_ESTABLISHED_WITH_SCOPE` | 18495 | 0014 | **同一导出 13568 也有此串**（位于 `prefix_end_line = 15891` 之前的 SHARED 前缀段，属父线更早轮）；本线 0014 的判词与本行归属必须分开（`DISCOVERIES.tsv` D09-0050 专列溯源行） |
| `ALL_DECLARED_ROUTES_REJECTED_WITH_SCOPE` / `FORMAL_TARGET_UNDERDETERMINED_WITH_SCOPE` / `NO_BARE_ZFC_OBJECT_LANGUAGE_INCONSISTENCY_CLAIM` | 18461–18463 | 0014 | `Targets与Profile.md:40` 记 SOP 三种总交付；`八线分叉后复盘.md:30` 概述为「C2/C3：形式目标未定义」 |
| `LATER_COMMAND_SOURCE_MISMATCH` | 17748 | 0012 | — |
| `DUPLICATE_SESSION` | 18693 | 0016 | — |

## 附录 B：身份与口径自记账（R3/R4）

- 【原话】均出自 GUI 导出 User 块，行号即 `export_line`；其中 0005 轮的 User 块（16158）是用户**逐字贴回** dev-08/本线前两轮问答（含父线 `dev-08/0113` 的「元思维／元元思维」段，该段在 dev-08 与 dev-09 导出同位于 15692），不是新的提问——本线只把「以上是我要求你记录到新方案中的两次问答…你看一下新方案，你记录的是完整版吗？」（16182）当作本轮原话。
- 【自述】均出自 `## Codex` 块；`anchor_status = codex_fallback` 的四轮（0006、0012、0013、0014）其最终判词段的 scope 锚点是该轮之内的一条 Codex 播报行（16876 / 17802 / 18190 / 18425），不是末条 Codex 行；末条判词仍可在同轮内找到（16878–16942、18190–18225、18439–18610、18666–18693）。
- 【判断】只用于本文件作者的对照结论（例：0008 的「调度语义错误」是 0011 建 SOP 的直接动因）；不替 GPT 的自述、也不冒充机器证明。
- 轮数口径：`own_docs = 16`（块坐标）与裁决 #3 的 `adjudication_rounds = 8` 是两套口径；本文件与 `DISCOVERIES.tsv` 一律用前者，后者只在文件头并列引用（R4）。
