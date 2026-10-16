# dev-01 研究脉络（尾 → 分叉点）

- **线**：dev-01（GUI 标题 `# 🌟 01 - ZFC-1`）
- **导出**：`git-worktree对话录/dev-01 - 20261005T093957Z-01a1083d-3515-7403-9b43-a5e02d8fc2d5-3647494d3660-gui.md`，17,161 行；sha256 `2db6eeeaad4fff09df8465151e64eb8fe30e6cae37187d2990a1a979f3438c80`（`audit/GUI-ASSET-RECOVERY/manifest.json`）
- **分叉**：自 **dev-08 #111**（`wflow-lineage/scope.json` lines.dev-01.fork；`audit/GUI-SYNTH-REDO/qa/dev-01/_branch.json` cutoff end_byte_offset 12006738 / end_ordinal_exclusive 55523）。导出前缀（同 dev-08 逐行共享）止于 **L15556**（`scope.json` prefix_end_line），自有内容从 L15557 起。
- **轮数口径（R4）**：
  - 自有轮清单 = `scope.json` lines.dev-01.docs[] 的 **21 个块坐标 round（0001–0021）**；本文件与 `DISCOVERIES.tsv` 的 `round` 字段一律取该清单。
  - **并列引用**：闭包 §8 裁决 #3（`认知闭包/GUI-ASSET-RECOVERY-001.md:89-98`）口径为 raw `role=user` 记录，dev-01 = **10 轮**；该口径只在此并列引用，**不与块坐标互换**。
- **锚点**（`scope.json` anchor_summary）：total 21、anchored 14、mechanical_window 7、export_absent_prose 0、unresolved_prose_docs 空。7 个机械轮 = 0001/0003/0004/0008/0012/0015/0017（`anchor_status=no_prose_mechanical_round`，User 块只有 environment_context / external_codex_apps_open_page / goal 注入）。
- **身份标注（R3）**：【原话】用户原文；【自述】GPT 结论；【证明】机器证明（本线所见均为导出内 GPT 自述的证明收据，未在本线重跑 kernel）；【判断】审计者或本提取员判断。
- **`DISCOVERIES.tsv` 列约定**：12 列 `id line layer round export_line type claim verdict_token artifact_ref status propagated_to notes`，无表头、制表符分隔。`type` 与 `status` 取 `wflow-lineage/tools/check_lineage.py` 的枚举（type∈判定/发现/来源/控制/拒绝/方法/概念/治理；status∈carried/parked/superseded/cold/open）；R3 身份标注写在 `claim` 列首（【原话】/【自述】/【机械轮】）；`verdict_token` 逐字抄自导出（无判词留空，机械轮记 `MISSING` 并在 notes 说明）；`export_line` 取 scope.json 锚点，凡落在本轮 `codex_fallback` 锚点之前的正文一律留空并在 notes 记录真实行号（R1 由 round 定位）。
- **本文件不产出任何数学结论（R7）**：凡涉及 ZFC/HoTT/芝诺的命题，一律按其在导出中的身份与范围照录，并保留原有禁止外推。

## 工作树链（【自述】+【判断】）

dev-01 是同一 Codex 线程跨三个工作树的连续线：`bdfd`（detached 6eee28d9）→ 隔离候选 `zfc-core-adequacy` → 集成 `zfc-core-adequacy-dev01-integration`；分支 `origin/dev-01` 先以 `ca1259fe`（L15837）保存 bdfd 对话快照，再以 merge `bcecbc12`（L16885）合入核心充分性线，终态 `cd9e34b2`（L17144）。【判断】这条链解释了本线两处「保存到 dev-01」请求（#0007、#0021）为什么措辞不同：第一次只保存 worktree 快照与对话录，第二次要求保存全部代码/文档/对话录。

## 分层脉络（每层含"为什么转向"）

### 层 1｜终态保存与全量推送（round 0021；L17126-17161）
- 【原话】L17128：「你现在的这个git worktree上的工作，我希望保存到远程的dev-01分支上，包括所有代码、文档和对话录记录文件。」
- 【自述】L17135-17156：`origin/dev-01` = `cd9e34b26b797df46989d33ebf944544d134f9d9` = HEAD；`git status --porcelain=v1 --untracked-files=all` 返回 0 条；`dev-notes/` 共 114 个 Git 追踪归档（含本会话 `0111` 与 `0112`）；并明确 `AI对话录/`、`workspace/`、`private-audit/` 在该工作树不存在。
- **为什么转向**：用户要求"包括所有代码、文档和对话录记录文件"地保存当前 worktree；GPT 因此把上一轮只做"研究归档"的状态推进为一次全量、可核验的远端保存。

### 层 2｜「人话总对账」：目标 / 进度 / 三座未付桥（round 0020；L16996-17119）
- 【原话】L16998-17000：「人话告诉我：1、我们一直以来，迭代了这么多个/goal，到底是为了证明什么？2、我想要的最终的形式化和机器证明，做到什么程度了？」
- 【自述】L17009：「我上一轮说"Goal 完成"时，说的是 **最后那个 SOP 的有界合同已经闭合**，不能等同于"你最初想证明的 ZFC 理论精度问题已经被最终机器证明"。」
- 【自述】L17015：终局目标的人话版——「你一路要证明的，不是"ZFC 推出矛盾"，而是：ZFC 作为数学的基础框架，对时间化、可计算的过程完成缺少足够的理论观察力」，由此容许"数学幻觉 P"把连续模型里的 `FormalDone` 当成原过程里的 `OriginDone`；并要 HoTT H0 作为"同一个 Q，一边放过、一边暴露"的终局判词。
- 【自述】L17082：C-369 的边界——「`C-369` 没有在 Lean 里推导“ZFC 缺少 Q”。它定义了一个 `ApplicationCase`，然后证明：**如果** `applicationClaim=True`、`claimsOriginalResolution=True`、`requiresBridge=True`、`bridgePaid=False`、`explicitTaskSwitch=False`，那么这个 case 满足 `ApplicationAdequacyFailure`」；Lean 没有读 IEP，也没有把 ZFC 公理译进该结构。
- 【自述】L17119：四项终局义务仍未完成；下一方案必须把四个未付款项直接写成完成条件，「否则，再多的 Lean 控制都只能证明我们在外围越来越精确」。
- **为什么转向**：用户要"人话"对账，GPT 主动纠正自己上一轮"Goal 完成"的措辞，把"SOP 完成"与"研究终局未完成"分开，并把未完成的四项义务固定为下一方案的完成条件。

### 层 3｜C0–C6 执行与最终充分性判词（round 0016–0019；L16543-16915）
- 【自述】L16626：C1A 首条可复核推进——固定 **ZFC-founded extension（Mizar TG）→几何级数子理论（MML `SERIES_1`）** 的来源链；同时暴露"无实际消费者映射、无过程完成 bridge"的缺口。
- 【自述】L16646：Isabelle/ZF 与 Foundation 双 lane 有界结果；H0 逐字段审计显示与当前物理芝诺任务不是同一个 Q，已从 verdict 前提排除；`OriginDone` 必须回到用户原始任务合同。
- 【自述】L16650：一手原文给出关键校正——用户在芝诺／圆环线上真正盯住的首要前提是 **连续、稠密、无限可分的时空模型** 与现实离散运动前提之间的差；C6A 是有价值的 B 向控制，但 A 向主线是 C2C/C3C。
- 【自述】L16768：C3C 改变下一步性质——IEP 明确承认 Achilles 的论证依赖连续、无限可分的时空；真正未支付的是"有限自然数阶段余量归零"与连续端点／极限完成条件非同一任务。
- 【自述】L16804/16808：C4D 把"同一段半程叙述"与"同一个完成条件"分开；IEP 的"resolution"与"不需要最后一步"两种读法都保留，由用户固定任务合同裁定，改题读法留作反控制。
- 【自述】L16846：最终判词（在用户固定的"有限自然数阶段余量精确为零"`OriginDone` 下，来源未支付 completion bridge）→ `CORE_ADEQUACY_FAILURE_WITH_SCOPE`。
- 【自述】L16859：C-369/C-370/C-371 的 Lean 4.34.1 运行均通过，closure 为 `SELECTED_PACKAGES_VERSION_CLOSED / HEAD_BYTES_CHECKED`。
- 【自述】L16861-16877：六不证明 + 保留反控制（若接受 IEP 的 revised continuous completion 为 `OriginDone`，C5D `explicit task switch` 分支取代 failure 分支）。
- 【自述】L16836/16891：八项总完成门全部通过、Goal 标记 complete；merge `bcecbc12`（对话归档第一父 + 核心充分性候选第二父），`0111` 按 turn ID 合并为 7 个唯一 turn。
- **为什么转向**：从 C1A 起，用户原始"稠密性—运动"合同被 GPT 认作必须形式化的 A 向主线（L16650），于是 C2C/C3C/C4C/C4D 依次固定"稠密 vs 量化"的同一任务合同；C6D 把这套 source-to-spec 字段收成条件性核心后果，八门通过后 Goal 收口。

### 层 4｜新核心方案建立（round 0014–0015；L16397-16644）
- 【原话】L16399：「我觉得你要给我一个确定性的/goal内容，确保你不会继续出现这种错误，并且，没有拿到最终的结果，你不能停下啊，你现在每次停下都告诉我事情并没有完全搞定，但是我再问你，你又说可以工作，我要的不是你的这种工作模式，我要的是一个/goal，完成全部的形式化和机器证明啊！」
- 【自述】L16404-16436：新稳定方案名 `ZFC-META-SUBTHEORY-ADEQUACY-SOP`，核心问题固定为"bare ZFC 或实际 ZFC-founded `M` 支撑连续统／极限子理论 `S`；`S` 对芝诺／圆环原任务 `Q` 给出 `FormalDone`；实际 promotion `P` 是否在未支付 Bridge 时把 `FormalDone` 升格为 `OriginDone`；`M` 是否承担并实际履行这项审查责任"。
- 【自述】L16444 状态串：`C0_UNIVERSE_FROZEN / CORE_TARGET_NOT_YET_ENTERED / C1_C6_NOT_STARTED / FINAL_CORE_VERDICT_NOT_PROVED`；set.mm、ACL2、generic Gödel、C-367/C-368、H0 未支付 Same-Q 映射全部降为**控制层**。
- 【自述】L16462/16478：每叶 `successor scan`——「不能暂停 Goal，不能要求你重新说"继续"」；contract 未固定时必须保持 `CORE_CONTRACT_NOT_YET_FIXED` 与 active。
- 【自述】L16496-16510：落盘 SOP 五片、闭包 `ZFC-META-SUBTHEORY-ADEQUACY-001`、C0 manifest、F-053 与用户原文；checkpoint revision 302 `CHECKPOINT_COMMITTED`；提交 `797571ce` 推送 `origin/dev`；下一步固定为 **C1A**。
- **为什么转向**：用户要求把"确定性 /goal + 方案名 + 认知闭包"写成硬合同，并明确反感"每次停下都说没搞定、再问又能继续"的模式；GPT 因此把"来源没付 bridge"从总停机理由改写成叶节点状态，完成条件锁到 actual `M/S/Q/P/Bridge/Adequacy` 的 source-to-spec machine proof。

### 层 5｜核心层偏航自省（round 0013；L16282-16395）
- 【原话】L16284：「所以你到底做到什么程度了？到底是不是一直在外围，没有进入问题的核心层？」
- 【自述】L16293：「是。更准确地说：**我已经把"怎样检验理论精度不足"这把尺子做到了较深的位置，却没有把它真正压到你要打的 ZFC 核心位置上。**」
- 【自述】L16307：若"核心层"指 ZFC 为什么没识别它所支撑的连续统／极限理论在芝诺、圆环原任务上的完成合同替换——「那么我还没有进入这个核心层。」
- 【自述】L16332：关键偏航自认——set.mm 回答"一份形式证明是否按这个数据库的规则被接受"，用户问的是"ZFC 作为基础性元理论，能不能看出它所支撑的极限／连续统子理论把'形式极限或端点完成'越级当成'芝诺／圆环的原过程已经完成'"，「把前者当作后者的入口，是我这段工作最关键的偏航」。
- 【自述】L16377-16390：先把四件固定（S 的精确版本 / 原任务 Q 合同 / 提升点 P / ZFC 的基础责任这个待论证 adequacy criterion），再建新核心单元 `ZFC-META-SUBTHEORY-ADEQUACY-001`。
- **为什么转向**：用户直接质问是否"一直在外围"，GPT 承认此前把最容易 machine-check 的 `set.mm` proof acceptance 放到中心、犯了"先造一个可形式化对象，再把它当成理论 X 真正在回答的对象"的错误，从而重固定核心靶并新建下一层 SOP。

### 层 6｜T-PRECISION-DIAGONAL-SOP 连续执行与 ACL2 入口（round 0011–0012；L16030-16282）
- 【自述】L16105：新 source-ingress 判据——已检查分母的收束"不是'所有可能来源都查完'"，而是 `set.mm / Foundation / H0 / IEP-Norton` 链没有同源的 `Process → ρ → Accept → OriginDone` 合同；要找"由 ZFC 或明确集合论基础支撑、且同一版本固定来源同时把芝诺／连续运动过程、形式证明接受和完成桥放在一个合同里"的形式系统。
- 【自述】L16129：ACL2 判别结果——README 把"physical path 的有限步完成"说成 machine-checked，但 `zeno-dichotomy-resolution` 只在给定 rational `dist` 与正整数 `omega` 时证明 `dist * omega` 是有理数；没有原物理过程定义、没有 `ρ`、没有 `Accept → OriginDone` bridge；本机无 ACL2 runtime，不把 README 的 certification 升级为重放证据。
- 【自述】L16199：判词 `ACL2_ZENO_SOURCE_INGRESS_NO_ADMISSIBLE_T_TARGET_WITH_SCOPE`（L16201 明确：非 ACL2 的形式反驳，也非 bare ZFC 的结论）。
- 【自述】L16216/16218：总体身份 `CURRENT_T_PRECISION_SOURCE_DENOMINATOR_CLOSED_WITH_SCOPE`，并显式声明它"不表示想法 T 已被证明为所有理论的通论，也不表示 bare ZFC 推出矛盾"。
- 【自述】L16236-16248：认知加载器 bootstrap repair（revision 298→299）与两个正式 checkpoint（300/301，均 `CHECKPOINT_COMMITTED`）；`3bc07468` 推送 `origin/dev`。
- **为什么转向**：T 分母"已闭合"被 GPT 拒绝读成"研究结束"，于是启动范围固定的跨理论 source-ingress；ACL2 项目因同页同时声称 machine checking 与芝诺物理有限步完成而成为可证伪候选，核对源码后作为受控拒绝关闭，goal 以有界总收口结束。

### 层 7｜`/goal` 连续执行合同与方案命名（round 0010；L15944-16028）
- 【原话】L15946：「那么你如何给自己设置好/goal，才能确保你自己不要再在中途停下，并且：**给方案一个名字，方便以后你在／goal中引用这个方案名，同时维护好这个方案你在执行的过程中的对应的认知闭包…**」
- 【自述】L15955-15973：不另造竞争总方案，采用既有稳定名 `T-PRECISION-DIAGONAL-SOP`（连续程序 `T-OBS → 哥德尔机制基线 → T-DIAG → T-Meta → T-ZFC`；`GODEL-Q-REFLECTION-SOP` 是 T-DIAG 执行模块；唯一跨 Session 闭包 `T-PRECISION-DIAGONAL-001`）。
- 【自述】L15993-16021：三层停止表（原子单元 / 子线 / 整体 SOP）——「一条来源线停了不再等于研究结束」，同时防止"所有已承诺路径都关闭后仍为了不停止而随机制造新的模型、接口或形式化玩具"；跨 Session 七步恢复顺序；并如实声明「无法从逻辑上保证任何未来模型永远不会中断」。
- **为什么转向**：用户要求一个可被 `/goal` 直接引用的持续执行合同（方案名 + 认知闭包 + 跨压缩一致）；GPT 用已有的 T-PRECISION-DIAGONAL-SOP 承接，并把"局部停止不等于总体停止"写成可检查的规则。

### 层 8｜F-050 收尾语义澄清（round 0009；L15872-15943）
- 【原话】L15875-15882（annotation 包裹轮）：追问 F-050 收尾段——「你的意思是，后续再无可以推进的形式化与机器化内容了，是吗？」
- 【自述】L15895：「不是。:codex-annotation{index="1"}」
- 【自述】L15897/15901/15910：F-050 的完成只表示版本固定的 M0–M5 分母到达 SOP 预先写明的有界结束条件；它停止的是"在同一批来源与同一份未固定的 bare-ZFC completion interface 上继续重复造 fixture"；结束判词即 `CLOSED_WITH_SCOPE`，不等于"再也没有可形式化的命题"。
- 【自述】L15914-15937：仍可推进表（M1 缺 matching forcing-ticks compiler；M2–M5 缺真实来源同时给 `C_accept`/`OriginDone`/bridge/H0-Zeno consumer；F-051 哥德尔式 completion reflection；F-052 理论精度 T），以及"真正推进"的五条件。
- **为什么转向**：用户以 annotation 形式质疑上一轮"已按总完成条件收尾"的语气；GPT 明确把"工作包完成"与"研究结束"分开，并列出后续可机器化的四项缺口，直接引出 #0010 的方案命名请求。

### 层 9｜dev-01 首次保存为工作树快照分支（round 0007–0008；L15818-15871）
- 【原话】L15820：「你现在的这个git worktree上的工作，我希望保存到远程的dev-01分支上，你打算如何处理？包括对话录记录文件。」
- 【自述】L15825-15861：按"工作树快照与远端分支保全"处理而非推脏 `dev`；`bdfd` 是 detached `6eee28d9`（含 800 行 `dev-notes/0109` 增量 + 5 份未跟踪 GUI 对话录）；`dev-01` 从该精确提交分出，快照提交 `ca1259fe`（archive: preserve bdfd worktree dialogue snapshot），6.45 MiB 逐文件 SHA-256 原字节保存，尾随空格不改写；`origin/dev-01` 与本地逐字节核对。
- **为什么转向**：用户要求保存当前 worktree 与对话录；GPT 选择"从精确 HEAD 分叉 + 只提交自己的修改与五份对话录"，避免把 canonical `dev` 的后续状态混入快照。

### 层 10｜F-050 总闭环恢复与有界收尾（round 0001–0006；L15557-15817）
- 【自述】L15626-15630：切换到新受管工作树，先核对与暂停点一致的 Git/证明资产/Goal 状态；确认承接 `9ffca5e0` 之后未提交的 F1-E 续作；不把 Stack 环境失败当成 M1 结论，而是把 CCHM/GCTT/forcing-ticks/CCTT 与公开精确 H0 检索整理成版本固定的 M1 来源分母。
- 【自述】L15634：C-359 至 C-366 八个直接 proof package 逐个通过选择性证据闭合检查；C-365 补齐遗漏的 transitive import `UniverseHasNoLevel.agda` 并以新 Agda 主运行重放；全局 Coq/Docker 旧包问题保持为全局治理缺口，不削弱八包验证范围。
- 【原话】L15679：「立即恢复，继续」（在 #0004/#0005 之间的机械 external 块之后）。
- 【自述】L15692-15696：F1-E 唯一可执行缺口 = 让冻结的 forcing-ticks 编译器源码在本机已有 GHC 环境完成一次受控构建，并明确「成功只会证明该编译器可运行」。
- 【原话】L15711（goal 编辑注入追加）：「做不完不要停。」
- 【自述】L15749-15771：F-050 收尾判词表——M1 `SOURCE_PROVIDED_ROUTE_REJECTED_WITH_SCOPE`、M2 `STRICT_P_SOURCE_PAYMENT_REJECTED_WITH_SCOPE`、M3 `BARE_INTERFACE_UNDERDETERMINED_WITH_SCOPE`、M4 `ACTUAL_Q_UNIFICATION_REJECTED_WITH_SCOPE`、M5 `ATTRIBUTION_UNDERDETERMINED_WITH_SCOPE`；总判词 `SOURCE_DENOMINATOR_ACTUAL_INSTANCE_REJECTED_WITH_SCOPE` + `BARE_ZFC_COMPLETION_INTERFACE_FORMAL_TARGET_UNDERDETERMINED_WITH_SCOPE`；四个重开触发器（L15771）。
- 【自述】L15779：forcing-ticks 边界——`in∀/out-in-∀` 保留 postulate；GHC 8.10.7 卡本机 Xcode toolchain；GHC 9.4 Stack probe 在 Hackage 索引下载七分钟后仍未进入 dependency solving，人工中止并记为 `SYSTEM_GHC_COMPATIBILITY_PROBE_INCONCLUSIVE_NO_COMPILER_BUILD`；`ClockedLiftDelayControl.agda` 仍是未运行候选规格，未进 claim matrix。
- 【自述】L15783-15804：集成 fast-forward 到 canonical `dev` 的 `dfed5e7f` 并推送；验证 test_proof_dependency_scope 20/20、test_proof_evidence_links 9/9；Goal 用量 937,457 tokens / 36m54s。
- **为什么转向**：dev-08 #111 暂停后，用户先「立即恢复，继续」，再在 goal 里追加「做不完不要停。」；GPT 因此在恢复现场核对后完成 F-050 的 M0–M5 有界收尾与 canonical 集成，为后续"研究是否真的结束"的追问（#0009）留下语义接口。

## 分叉点（dev-08 #111 → dev-01）

- 分叉父轮：dev-08 #111（暂停 ZFC-H0-FINAL-PROOF-CLOSURE-SOP 的那一轮）。dev-01 导出前缀与 dev-08 逐行共享至 L15556；L15555 只有一个空的 `## User` 块标题，随后 rollout 头部重放新的 environment_context（L15557 起）即 dev-01 自有内容起点。
- **语料缺口（R9，须显式登记）**：dev-08 #112 的研究发起人原话「想这样一个问题，如果ZFC有我们说的那种问题……哥德尔如何证明了哥德尔不完备性？」**不在 dev-01 的 GUI 导出里**（本提取员在本导出内检索 `如果ZFC有我们说的那种问题` 得 0 次命中；该分叉 cutoff 位于 L15556）。该句只以分支 `dev-notes/0109` 的形式存在于 dev-01/dev-08/dev-09 分支（`.claude/goals/CG-006-zfc-complete-formalization/GUI查阅索引.md:56`）。因此本线任何自有轮都不得把该句当作本轮证据；需要它时必须引 `dev-notes/0109`。
- **共享前缀内的判词不属于本线**：`TERMINAL_CLEANUP_WITHOUT_CLOSE`（A-0058，dev-08:L1741）、`NO_MODEL_RECALL_CANDIDATE`（A-0159 dev-08:L5406；A-0553 dev-06:L15313）等判词字符串虽在 `assets-ledger.md`/`D3` 与共享前缀中大量存在，但归属 dev-08/dev-06，**不属 dev-01 自有轮**。

## 机械轮说明（anchor_status=no_prose_mechanical_round）

0001、0003、0004、0008、0012、0015、0017 共 7 轮的 User 块在 QA 切片中只有 `<environment_context>`、`<external_codex_apps_open_page>` 或 goal 注入，没有用户散文。它们仍被 `DISCOVERIES.tsv` 逐轮覆盖（export_line 取 scope.json `anchor_window` 起点，因为 `anchor_line` 为 null），判词列记 MISSING 并说明原因；这些轮次正文（goal objective 全文、budget 行）对理解相邻 prose 轮的转向是必要上下文，但不构成本线的研究发现。

## 本线的沉淀（供后续线/CG-006 取用；身份照录）

1. **最终判词 + 四个机器控制**：`CORE_ADEQUACY_FAILURE_WITH_SCOPE` 与 C-369/C-370/C-371。2026-10-08 已由 CG-006 以 `D01-C-NNN` 前缀并入 `dev` 的 `HoTT/CLAIM_EVIDENCE_MATRIX.md:1895-1909`（`4a3535d9`），并注明本机重放逐字节一致；`docs/ZFC时间维度观察力不完备-哥德尔式Q终局报告-20261008.md` §3 用四项义务对照表、§7 用 C-370/C-371 作反控制引用。
2. **核心层偏航自省**：#0013 承认把 `set.mm` proof acceptance 当作 ZFC 观察接口是"最关键的偏航";终局报告 §6「这一次不是侧移」正是对该自省的正面回应（`Targets与Profile.md` §6 与八线复盘 §9.4 都把它列为必须回应的反驳）。
3. **用户稠密性—运动原合同**：L16650 的 A 向校正把"连续、稠密、无限可分的时空模型 vs 现实离散运动"固定为 C2C/C3C/C4D 主线，产出 C-370/C-371 两台机器控制。
4. **治理层**：`T-PRECISION-DIAGONAL-SOP` 三层停止表与 `ZFC-META-SUBTHEORY-ADEQUACY-SOP` 的 successor scan 纪律（"不能暂停 Goal，不能要求你重新说继续"）被 CG-006 GOAL 的工作循环引用（`GUI查阅索引.md:39`）。

## 未决与需登记项（交 Master 入 ledger）

1. dev-08 #112 哥德尔原话在 dev-01 导出中缺失（见"分叉点"），引用必须回 `dev-notes/0109`。
2. 轮数两口径（块坐标 21 / 裁决#3 10）不可互换；DISCOVERIES 用块坐标。
3. `ZFC-META-SUBTHEORY-ADEQUACY-001-C6D-ACTUAL-CONTRACT-KERNEL-VERDICT.md`、`…-C0R5-TOTAL-GATE-AUDIT.md` 等分支审计文件名在当前 `dev` 工作树不存在（本地等价族为 `audit/20261005-ZFC-META-SUBTHEORY-ADEQUACY-C0R5-*.md`），引用时以 `origin/dev-01` 分支路径标注。
4. 导出内 C-369/C-370/C-371 的"Lean 通过/版本闭合"均为 GPT 自述收据；本线未重跑 kernel。`dev` 上 2026-10-08 的本机重放结论来自 `HoTT/CLAIM_EVIDENCE_MATRIX.md`，不是本线执行。
5. 7 个机械轮与相邻 prose 轮的块边界依 `scope.json` `anchor_window` 推定，未逐块解剖 raw rollout（裁决#3 已定义 GUI `## User` 块 ≠ 问答轮）。
6. `origin/dev-01` 的 head 在本导出结束（2026-10-05）时为 `cd9e34b2`（L17144）；`.claude/goals/CG-006-zfc-complete-formalization/八线分叉后复盘.md:104` 记 2026-10-08 `git fetch` 时为 `f10899cb`（§0 记领先 `dev` 15 个提交）。两者是不同时点的远端快照，不矛盾；引用分支当前状态应另行 fetch 核验。
7. 本线自有轮的用户散文没有出现 Q/P/A/B 长段（该段只在共享前缀 L13658/13891/14006 等处）；导出独有段里的 `ZFC最大的问题…`（L15793、L15848）只是 `dev-notes/0109` 文件名，不是研究发起人核心提问的重发。
