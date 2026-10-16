# dev-04 线脉络（THREAD.md）

> 线：`dev-04`（导出标题 `# 04 - ZFC-1`）；分叉自 `dev-03` #13（`parent_rollout 01a1039a-331b-7c92-acdc-38841283cac8`；QA `_branch.json` 记 `fork.parent_doc = 13`、`cutoff.end_ordinal_exclusive = 45352`、`contiguous_in_own_export = true`）。
> 导出：`git-worktree对话录/dev-04 - 20261004T102801Z-01a10533-f07b-7d21-ada8-cd136ce61dd5-9c791ac1226d-gui.md`（13,784 行，sha256 `506f28eda4574b50b8945ce1b030a53318af990af4ca23efdf5d0722762d8706`）。
> worktree：`/Users/aurolafly/.codex/worktrees/3d2f/HoTT_AI_HANDOFF_20260911`，detached HEAD；`origin/dev-04` = `69aa5aabf4083f2508b9e48ab24160963cc9482d`（本线快照发布结果，八线复盘 §0 另记 `f97bbcb4` 为后续 HEAD）。
> **轮数口径（R4）**：本文件与 `DISCOVERIES.tsv` 全部用 **QA 块坐标**：`scope.json lines.dev-04.own_docs` = **15**（机械轮也计）；CL 口径 `adjudication_rounds` = **11** 只作并列引用（裁决 #3 分线总数），两者不互换。
> **行号口径（R1）**：`export_line` 一律取 `scope.json` 的锚点（`anchor_line` / `anchor_window`）。`audit/GUI-SYNTH-REDO/qa/dev-04/_index.jsonl` 的 `line_from/line_to` 是源 rollout(jsonl) 坐标，不是导出行号，本文件不以之作导出行号。
> **身份标注（R3）**：【原话】研究发起人原文；【自述】GPT 结论；【证明】机器运行结论（Lean/Agda 内核检查、receipt 判词，只证明其明确范围）；【判断】审计者或我的判断。四类不互相冒充。
> 本线无共享前缀骨架层任务（共享前缀 1–12,278 行属 `dev-03`，由其 R0143–R0220 系列与 `dev-08` 的共同前缀负责）；本线自有区间自 **12,279** 起，`unique_lines` = 1,131。
> **本线不是数学结论的产出层**：全文只登记研究脉络、判词身份与证据状态；所有 Lean/Agda 结果都以 `KERNEL_ACCEPTED_WITH_SCOPE` 一类收据判词转述，不升级为 HoTT/ZFC 的数学定理（R7）。

---

## L5 工作线快照发布到 origin/dev-04（轮 0012–0015，导出 13,519–13,784；含机械轮 0013）

**这一层在做什么**：把「detached contributor 面上已提交的 16 个候选提交 + 本 chat 必要未提交续写」固定成可审阅、可恢复的远端分支 `origin/dev-04`。

**为什么转向**：L4 结束时研究证据已闭合（`SOURCE_FRONTIER_REFINED` / `ZFC_Q_NOT_LOCATED`），研究发起人不再要求新数学内容，而要求把成果固化为 Git 实物。0012【原话】「我希望你把你所在的git worktree的git分支，以 `dev-04` 的分支名，所有内容在全部提交了之后，完整推送到远程，**先不要动手，先告诉我你打算如何做？**注意，我要的是你当前工作区中的内容的完整推送，**不要有代码放在`/tmp`这种临时目录中啊**。」只读核对给出三个事实：worktree 实际在 `detached HEAD=4ed282fd1d1b372a37965ff77127e62bfe4daf3f` 而非某本地 branch；本地与远端均不存在 `dev-04`；`origin = github.com/math-fournity/HoTT-Paradoxy.git`；25 个已跟踪修改 + 328 个未忽略新文件 ≈ 20.6 MiB，另有 10 个被 `.gitignore` 排除的 `.agdai/.pyc/__pycache__`。GPT 的第一版方案把范围读成「当前 worktree 中全部未忽略文件一并快照」。0014 研究发起人主动纠正：【原话】「**我担心你误解的我的意思**……我希望这些东西都能提交到远端的dev-04分支上，我们的理解是对齐的吗？」GPT 以【自述】「**现在对齐了**」重述目标＝本工作线已产生并已验证的研究成果＋必要未提交续写，并更正技术事实（detached HEAD 不是 branch），明确不混入其它并行工作单元的 `STATE`、README 投影、菲尔兹材料与治理 checkpoint。0015 研究发起人只说【原话】「开始」。执行结果：快照提交 `69aa5aab`、承接 `ab5a3542 … 4ed282fd` 共 16 个连续提交，以非强制显式 refspec `git push origin HEAD:refs/heads/dev-04` 推送，`ls-remote` 与本地 OID 逐字一致。

**本层判词与实物**：【自述】`verify_zfc_completion_observation_closure.py`（13 个正向/预期拒绝的证明运行 + 8 个冻结 P-DAG 输入）、`verify_governance_shards.py`、`verify_pattern_p_tool_history_sources.py --root .`（18 个 Pattern-P 来源）均通过；Git LFS 无新增对象；`git diff --cached --check` 唯一项是 `dev-notes` 历史归档中刻意保留的 Markdown 双空格换行，已登记、未静默改写。

**R9 缺口（不掩饰）**：0013 是机械轮（`anchor_window=13519-13642`），导出的 User 块只有 `<external_codex_apps_open_page>{"page_id":null}</external_codex_apps_open_page>`（L13640），该窗口同时覆盖 0012 的方案终局块（L13534–13636），后者归 0012；本层 `DISCOVERIES.tsv` 对 0013 以 round 单锚覆盖、判词标 `MISSING`，这是语料固有缺口而非覆盖缺口。

---

## L4 收敛收尾：B→P 回溯、Meta/Sub 与文献回流（轮 0009–0011，导出 13,165–13,518；含机械轮 0010）

**这一层在做什么**：把「从不合理 B 回溯到被加入的 P」做成受控定理；把 Q/P/A/B 放到同一过程状态上证明未付 bridge 的 promotion 不健全；再对另一条独立 worktree 的文献候选做 B0–B5 回流审计，以有界负结论收口。

**为什么转向**：0009 研究发起人逐字重贴 Q/P/A/B 判词全文并问【原话】「的形式化和机器证明，你是否还可以继续推进？还是说已经推进完成了？」GPT 答【自述】「**可以继续，而且我不能把这整条链说成“已经完成”**」，并把下一步定为「**下一步不是再证明一次 `P → A ∧ B`**」——即把叙述性的「反证回溯」升级为机器定理。0011 研究发起人只说【原话】「继续推进，直至完成」，GPT 随即补上用户更早提出的 Meta Theory / Sub Theory 层，并在同轮转入文献回流，因为自述「Meta/Sub Theory 的机器模型已经提交为 `5202eb1c`。下一步我不再扩写 toy model，而是回到另一个已冻结的 HoTT 创建动机—ZFC 文献候选包，检查它有没有给出实际的 meta-theory / sub-theory consumer、模型解释或完成政策来源」。

**关键成果（按证据等级）**：
- 【证明】`CommunityObservationPolicy.lean` 新增四定理：`undesirable_derivation_has_base_or_policy`、`nonbase_undesirable_derivation_backtracks_to_policy`、`zfc1_nonbase_B_backtracks_to_admitted_P`、`base_B_is_an_alternative_derivation_origin`；`POLICY-001-08` 收据（Lean 4.34.1）报告 20 个交付 theorem 无额外公理依赖。精确含义是 `Derives(T,B) ∧ B∉T 基础承诺 ∧ 产生 B 的规则是 P→B ⇒ Derives(T,P)`。
- 【证明】`CompletionPromotionTension.lean`（两状态过程）：采纳 P 并由 A 推导原过程完成、同一状态保留 B ⇒ 该政策相对过程语义**不健全**；`TENSION-001-02`（14 定理无额外公理）与 `NEG-001-02` 拒绝构成正负对，`-01` 因 import 放置错误失败并作为实现准备失败保留。
- 【证明】`MetaSubtheoryAudit.lean`：正向＝接受 `formalDone` 又升格 `originDone` 即已承担 bridge；反向＝粗元观察合并 `origin-complete` 与 `origin-incomplete` 状态时无法审计 origin Done，错误程序在 unresolved state 被 Lean 拒绝；正控制保证「不是任何元理论都必然失败」。
- 【控制】`PROFILE_MISMATCH_SOURCE_SUPPORTED`：芝诺任务与 main 固定 HoTT `QuestioningDelay` 任务不能直接叫作「同一个完整 Q」（对象、允许操作、观察、`Done_formal`、`Done_origin`、来源判词都不同）；`guardedPolicy` 证明 Q 缺失不逻辑蕴含 P 被采纳。
- 【证明】`RECEIPT-03` 被验证器正确拒绝覆盖——证据版本控制起作用，不是数学失败；同理 L12984 的 H100 字节漂移按 `Q_SAFETY_REPAIR` 用当前冻结字节重跑。
- 【来源】`codex/hott-motive-zfc-literature@352e9874…` 的 B0–B5 回流（八张 `RouteBackflowCard`）：判词 `SOURCE_FRONTIER_REFINED`，八条路线全部是 I1 的候选来源精度增益，`Q-0` 仍未形成、`ZFC_Q_NOT_LOCATED` 保持不变；结论入口被压成六个可证伪字段。
- 【判定】终局判词表：「ZFC 在时间维度上的观察力不完备」＝`COMPLETION_OBSERVATION_AUDIT_REQUIRED` 候选诊断，属基础使用层观察责任，不是 ZFC 对象语言缺陷定理；`ZFC ⊢ False` 未建立；继续重复同类卡片会变成 `TOOL_ONLY_DRIFT`。
- 【判断】本层仍全程无 bare ZFC 矛盾主张。CG-006 八线复盘 §5 记本线终点判词为 `ZFC_Q_NOT_LOCATED`，与本层 L13454 逐字一致。
---

## L3 收尾可检验化：复跑与并行候选线独立核验（轮 0008，导出 12,885–13,164）

**这一层在做什么**：把上一层的收束包从「旧运行的解释」升级为「对应当前源码的机器验证链」，并独立核验另一条已提交的并行候选线。

**为什么转向**：本轮 User 块是 goal 续跑块（objective【原话】「继续工作，直至彻底用形式化和机器证明收尾」，同文在 dev-08 导出 L13477；`Tokens used: 174481`）。GPT 自述「当前目标仍未达到“彻底用形式化和机器证明收尾”」，于是转向「**对这条 ZFC 诊断真正依赖的核心形式资产做一次当前工作树的复跑与完整性核对**」——IEP 完成观察的 Lean 边界、几何级数的极限／有限阶段分离、O3–O5 条件命题、P 来源状态模型、main HoTT 的 `QuestioningDelay` 与 C-83 截断对照。复跑中途发现一条必须纳入的并行证据线，于是再转向按路线级回流 SOP 对 `codex/zfc-q-policy-formalization@ea6c338f` 做冻结、排除 dirty、只读干净 worktree 独立重跑。

**关键成果（按证据等级）**：
- 【证明】新鲜 Agda 重放四项：`QuestioningDelay` 主包接受（约 90 秒，该时长只是本次观察窗内的运行记录）、其错误早停负控制被拒；C-83 截断主包接受、其错误「截断后仍沉默」负控制被拒；四个 ZFC Lean 包同轮复跑；九项 run 由新 closure verifier 判 `PASS`。
- 【控制】H100 字节漂移：运行使用格式化前 TaskCard 字节、后为 Git whitespace 检查移除末尾空行，内容同而哈希变；按 `Q_SAFETY_REPAIR` 用当前冻结字节重跑，不依赖「语义看起来一样」。
- 【证明】独立冻结并重跑 `codex/zfc-q-policy-formalization@ea6c338f` 的 C-359 至 C-365：C-359 只有把 `ZFCOneUse`、强完成政策、`PolicyScopeWitness` 与 HoTT 侧 B 都作为明确前提时 Lean 才导出 `False`，不是 bare ZFC 的矛盾；C-360 截断问题的 stage-one completion 推不出原 universe 有限 halt；C-361 固定几何级数收敛到 1 不推出某个有限 n 已等于 1，并保留闭连续时间端点正控制；**C-365**：只含 `=`、`∈`、`⊥`、`→`、`∀` 的最小一阶成员语言中，保持 membership 不变而改变未入语言的 `originDone` 谓词，不改变任一该语言公式或 theory 真值。
- 【控制】伪造「第 0 步就已停机」的 Cubical Agda 负控制在 `nothing != just 1` 处被内核拒绝；实分析控制明确保留 Mathlib 的 `propext`、`Classical.choice`、`Quot.sound` 依赖。
- 【方法】收敛＝**一个有限的判别树**：若来源真把 Standard Solution 完成政策扩张到圆环 `OriginDone` 与固定 HoTT completion contract，则 C-359/C-363 可被实例化；若来源明确限定或拒绝，则闭合为「有界的负结论，不是什么都没找到」。范围收缩被自述为收尾阶段真正的标志。
- 【治理】四个 contributor commits `bad180ce`、`943f3b85`、`f2e9aad6`、`a7e2c2a1`；未把当前 `/goal` 标记为完成，因为 actual source scope / same-task bridge 仍是真实开放条件。

---

## L2 P 的命名与收束判词（轮 0004–0007，导出 12,527–12,884）

**这一层在做什么**：给「数学幻觉 P」一个可操作的名字与形式定义，把 main 分支 HoTT 发现确立为 B 侧实物，并用 R1/R2/R3 门与来源仲裁写下本线的收束判词。

**为什么转向**：0004 研究发起人追问【原话】「所以，数学幻觉P到底是什么？你知道了吗？」GPT 的答案是回到 Lean 定义、H099 来源审计与核心原文对应段落后给出命名，而不是给一个修辞标签；它明确把「已精确定义的候选规则」与「已经被来源证明为数学界实际采用的规则」分开。0005【原话】「你是否可以继续工作，直至全部完成？」GPT 把「全部完成」读成「逐项关掉来源、任务保真和证明义务」，而不是「已经证明 ZFC 有形式矛盾」，于是转入两个精确问题（IEP 的明示改写是否已构成 P 的来源形状；`QuestioningDelay` 是否自己也做了完成代换）。0006 研究发起人追问【原话】「**我们自己不是有HoTT在main分支上的发现吗？**」——按 CG-006 GUI 查阅索引 §2，这句只在 dev-04 分支；GPT 因此把 main 发现固定为 B 侧实物并配一张防偷换的来源卡。0007 研究发起人给出总体判断【原话】「我们实际上已经处于ZFC问题查找工作的收尾阶段，也就是研究已经开始收敛了」，GPT 明确说这句话改变了工作姿态：「**P 是放大镜；靶是 ZFC 的理论观察力**」。

**关键成果（按证据等级）**：
- 【自述】核心命名：**P = 无桥完成代换（Completion-Substitution Without a Same-Task Bridge）**；形式形状 `Done_formal(y) ⇒_P Done_origin(x)`，桥须保住 ⟨对象来源, 输入, 允许操作, 过程／trace, 观察, Done⟩；「幻觉」在于中间那座证明同一性的桥没有付款。
- 【方法】三情形判定表（明说改写 Done＝任务转换公开；给出 trace 并逐项证明＝桥已付款；只给极限却说原过程已完成＝候选）；四场景同构表（罗素／芝诺圆环／HoTT 罗素线），并把罗素放在「形成端」、P 放在「完成端」。这是本线被 CG-006 下游吸收最多的结构性产出之一。
- 【概念】Q 被收窄为「完成观察力」；P 是**元层验收政策**而非 ZFC 对象语言公理，`ZFC-1 = ZFC + P` 读作「共同体实际采用的 ZFC 使用政策增加了 P」。
- 【来源】C-83 截断对照作为 B 侧材料：同一追问在原宇宙上不停、在 `∥Type∥₂` 上第一问停、路径被压平且无统一解码；与 IEP 的「旅行不需要最后一步」判为**结构同形**——都满足 R1/R2、都缺 R3，但不支持「共同体已采用统一 P」或「P 已因果产生 HoTT 结果」。
- 【门规格】R1/R2/R3 来源候选形状：R1 来源给出已解决/已完成/已停止结论；R2 该结论通过改写 Done 或被问对象得到；R3 来源给出同一任务保持桥。**R1 + R2 + R3 缺失**即 `CompletionSubstitutionP` 来源候选形状。
- 【判词】本层仲裁版终局语言（L12785）：「在 ZFC 作为 Standard Solution 实分析基础的实际使用中，来源可在显式改写完成条件后宣布命名问题得到解决，而冻结来源没有自动提供“修订完成仍是同一原过程完成”的 bridge；故该使用层需要显式 O3–O5 completion-observation audit。」
- 【证明】`CompletionSubstitutionProfile.lean`：15 个打印定理无额外公理，`-02` 收据 `KERNEL_ACCEPTED_WITH_SCOPE`；六节点 H100–H105 受控运行；`ab5a3542` / `6e7707c0` 提交。
- 【判定】P 状态七行表把四条未建立项（桥／统一 P／P→B／形式矛盾）单列为「收尾阶段留下的强版本桥」。
- 【判断】本层仍全程无 bare ZFC 矛盾主张；ZFC 在 Lean 里仍写成 `baseZFC` 占位符，属「形似」而非对实际 ZFC 公理集的断言（CG-006 八线复盘 §5）。

---

## L1 Q/P/A/B 元政策演算与来源审判（轮 0003，导出 12,291–12,526）

**这一层在做什么**：把研究发起人的 Q/P/A/B 判词拆成一个可机器检查的条件性政策演算，并用冻结来源逐项审判其中哪些环节已被来源支付。

**为什么转向**：本层是 dev-04 从 dev-03 #13 分出后的第一轮。研究发起人不重复父线议题，直接给出本 worktree 的总体论证与交付要求【原话】：ZFC 缺失理论观察力 Q ⇒ A（允许判定极限理论解决芝诺与圆环）与 B（main HoTT 罗素计算内核暴露 Q 不存在的不合理）；设 ZFC-1=ZFC+A 则 ZFC-1=ZFC+P，而 ZFC-1 导致 B；「选择数学幻觉P加在ZFC上，是数学社区与魔鬼达成了交易……数学的灵魂——数学真理性。**我需要你最大程度地形式化并机器证明这一切。**」GPT 随即声明两条纪律【自述】：「先在 Lean 中形式化一个**条件性的元理论／接受政策模型**」「**不把尚未证实的历史、物理或哲学前提伪装成 ZFC 内部矛盾**」，并在进入建模前先修正了最关键的一处逻辑层次：「**“数学家不想要 B”本身不是逻辑否定**」。来源审计（H099）返回决定性否定后，工作重心从「继续扩演算」转为「明确列出未被来源支付的四个签名」。

**关键成果（按证据等级）**：
- 【证明】`CommunityObservationPolicy.lean`（`POLICY-001-03`）：18 个经 Lean 打印为「不依赖任何公理」的定理；新增 `Q_absence_activates_A_and_B`、`Q_absence_produces_normative_tension`、`Q_absence_violates_truth_constraint`、`Q_absence_incompatible_A_and_B_yields_false`；反控制 `emptyTheory_derives_no_claim`、`zfc1_is_strict_over_empty`（A↔P 循环规则不无中生有）与 `normative_tension_fixture_is_inhabited`（张力模型不可偷换为对象层矛盾）。运行收据：Lean 4.34.1、exit 0、stderr 为空。
- 【判定】`TruthConstraint`：要把「数学的真理性」写成形式矛盾，必须额外给一条可审计的真理约束（B 不可能为真，或 A 与 B 在同一形式系统中不能同时成立）——「不想要 B」只构成规范性张力。
- 【判定】H099 六判词族：`P_CANDIDATE_ONLY` / `P_A_SIDE_SOURCE_NOT_ESTABLISHED` / `P_B_SIDE_SOURCE_NOT_ESTABLISHED` / `SAME_TASK_BRIDGE_MISSING` / `P_TO_B_SOURCE_UNPROVED` / `ACTUAL_COMMUNITY_ADOPTION_UNPROVED`；同轮另给 `P_SOURCE_NOT_MAPPED / P_TO_B_UNPROVED` 证据前沿。
- 【概念】`CompletionSubstitutionP`：把 formal/model completion 交付成 origin process completion，却没有来源定义的 same-task bridge。
- 【开放候选】魔鬼交易四签名（Q 精确定义与实际缺失／P 精确规则与社区实际采纳／A 与 P 真实互推／P→B 同任务桥＋B 与真理不相容根据）；任一被来源拒绝，模型相应收窄。
- 【方法】用户语言↔Lean 位置映射表八字段；`ZFC-1 = ZFC+A` 与 `baseZFC+P` 只在显式 A↔P 规则下有**相同可导后果**，不是实际 ZFC 公理集的字面相等。
- 【治理】H098/H099 均用 `gpt-5.6-terra / max` 受控 App Server source-match；贡献链 `6877e33d`、`8f1556f9`、`3586c246`、`00585d42`；`CANDIDATE_NOT_CURRENT`（contributor worktree 身份）。
- 【判断】本层确立了贯穿全线的分界：「逻辑骨架已可证明，实际 ZFC 指控尚无来源级实例」；该分界在 0007/0009/0011 三次复述，也是 CG-006 终局报告把它列为「P 的两个侧面」语义侧的依据。

---

## L0 机械轮（0001、0002，导出 12,279–12,291）

本层只有机械内容，无散文、无判词：

- **0001**：`<environment_context>`（cwd = `/Users/aurolafly/.codex/worktrees/3d2f/HoTT_AI_HANDOFF_20260911`，`current_date 2026-10-04`，含 workspace_roots 与 `permission_profile type="disabled"`）。`anchor_status=no_prose_mechanical_round`，`anchor_window=12279-12291`。
- **0002**：`<external_codex_apps_open_page>`，正文仅 `{"page_id":null}`；与 0001 同一窗口。

【判断】这两轮在 `DISCOVERIES.tsv` 中以 round + 窗口行号覆盖，`verdict_token` 一律标 `MISSING`——导出内确无判词文本可逐字摘录（R2 的 MISSING 分支），不是漏读。它们的源 rollout 坐标（`_index.jsonl` 的 `line_from=7/11`）不是导出行号，本文件与 TSV 均未据其定位。另两轮机械轮（0010 在 L4、0013 在 L5）同理，分别在各自层内说明。
---

## 分叉点与跨线关系

- **分叉点**：`dev-03` #13（QProfile 终局之后）。dev-04 的共享前缀为导出行 1–12,278；自有区间自 12,279 起。`_branch.json` 记 `thread_id = 01a10533-f07b-7d21-ada8-cd136ce61dd5`、`fork.parent_rollout = 01a1039a-331b-7c92-acdc-38841283cac8`、`cutoff.end_ordinal_exclusive = 45352`。
- **下游分叉**：无（本线是 3d2f worktree 线的终点，成果经 `origin/dev-04` 快照交付）。
- **与父线的分工**：父线 dev-03 提供 O1–O5 拆法、UOU 来源卡、`PROFILE_MISMATCH_CONTROL_CONFIRMED` / `EVIDENCE_FRONTIER_REACHED_WITH_SCOPE`；dev-04 接手的是「Q/P/A/B 政策演算 + P 的精确定义 + B 侧 HoTT 截断材料」，并给出自己的终点判词 `SOURCE_FRONTIER_REFINED` / `ZFC_Q_NOT_LOCATED`。
- **与主干的同文**：研究发起人同一段 Q/P/A/B 判词在 `dev-08#88`、`dev-02#3`、`dev-03#15` 与本线 0003 逐字重复，本线 0009 又重贴一次；`goal` objective「继续工作，直至彻底用形式化和机器证明收尾」与 dev-08 L13477 同文。`DISCOVERIES.tsv` 的 `notes` 逐行标明同文位置，未把别线别轮的同一段文本归到本轮（R1/轮次归属按 QA 块坐标）。
- **对 CG-006 的沉淀**：
  1. **P 的两个侧面之语义侧**：`dev-04` 的「无桥完成代换」与 dev-02 强 P、主干 #91 的 P₁ 同指 `Done_formal → Done_origin`（终局报告 §4、Targets G-3/Ⅲ-2）。
  2. **罗素「形成端」与 P「完成端」的对照**（八线复盘 §5 列为可吸收项；D4-031）。
  3. **C-83 截断作为 B 侧的用法**，以及 C-365 成员语言不变性的 `ea6c338f` 独立重验版（D4-067）。
  4. **`zfc-observation-boundary` 形式包族**（`CommunityObservationPolicy`、`CompletionSubstitutionProfile`、`MetaSubtheoryAudit`、`CompletionPromotionTension` 及正负控制）作为 S7 合并候选；八线复盘 §9.5 已提示 C-359–C-365 与 `dev` 撞号，合并前必须重编号。
  5. **A 侧来源纪律**：IEP Standard Solution 的显式完成改写只支持结构同形，不支持共同体统一 P 或因果链。
- **CG-006 对 dev-04 的批评（如实登记）**：ZFC 在 Lean 里仍写成 `baseZFC` 占位符、A↔P 与 P→B 是手放规则，属「形似」；其中的 PromotionPolicy 已被 C-90 的 `consistency_needed` / `soundness_needed` 与真正的魔鬼交易取代（八线复盘 §5、【判断】）。

---

## 关键一次转向（一句话）

**0007**：研究发起人说「我们实际上已经处于ZFC问题查找工作的收尾阶段，也就是研究已经开始收敛了」，GPT 据此把「给 P 起一个漂亮定义」正式改为「**P 是放大镜；靶是 ZFC 的理论观察力**」——从无限扩展符号演算转为用 R1/R2/R3 门逐项检验来源是否支付同一任务 bridge，并把未支付的强边（R3／共同 P／P→B）显式单列为收尾阶段留下的义务，从而让 0011 的 `SOURCE_FRONTIER_REFINED` / `ZFC_Q_NOT_LOCATED` 成为有界负结论而不是「什么都没找到」。

---

## 需要 Master 登记到 ledger 的不确定项（本 agent 不改 ledger）

1. **round 0008 与 0015 的 `codex_fallback` 窗口导致 14 行无法双锚**：0008 的 User 块是 goal 续跑块（标题 L12885、objective L12893），0015 的 User 块全文只有「开始」（L13698–13700），而 `scope.json` 的 `codex_fallback` 锚点分别落在回答块 L13054 与 L13706，G2 窗口自锚点起。因此这 14 行的 `export_line` 留空、以 round 单锚（R1 允许），真实导出行写进 `notes`。这与 dev-03 agent 对同源码件的处理一致；若 Master 认为 goal 续跑轮与短用户轮应另立窗口规则，需在方案 §4 明确。
2. **`type` 枚举不含「判词／门规格／开放候选」**：`TYPES = {判定,发现,来源,控制,拒绝,方法,概念,治理}`。本线原拟用「判词」登记终局措辞、「门规格」登记 R1/R2/R3、「开放候选」登记魔鬼交易四签名，已分别降为 `判定`／`方法`／`发现`（语义由 `claim` 的身份前缀承载）。分类口径需 Master 在方案 §4 明确是扩枚举还是固定此映射（dev-03 agent 也登记了同类的「证明」缺项）。
3. **四个机械轮没有可摘判词**：0001、0002、0010、0013 在 A 层导出确无 prose 判词，按 R2 标 `MISSING`；这不是覆盖缺口（round 锚已给），但 Master 需知道这 4 轮无可摘判词文本。
4. **`_branch.json` 的 `cutoff.end_ordinal_exclusive = 45352` 与 manifest/scope 的口径关系未在本线复核**：scope.json 的 `fork` 段只保留 `parent_branch`/`parent_doc`/`parent_rollout`；`byte_to = 43,240,412` 与 `list invisible_tails` 的关系属冻结输入层内部口径，本 agent 只引用未推导。
5. **`origin/dev-04` HEAD 与快照提交不同**：本线导出内 GPT 自述 `origin/dev-04 = 69aa5aab…`，而 CG-006 八线复盘 §0（2026-10-08 `git fetch` 后）记 `origin/dev-04 f97bbcb4`、领先 `dev` 40 个提交。二者不矛盾（快照后仍有交付提交），但本线只机器核验了 `69aa5aab` 树上 13 个 artifact 路径可解析；`f97bbcb4` 之后的提交内容未在本线覆盖。
6. **C-83 截断的实物路径由本 agent 选配**：导出只说「主分支的 C-83 截断对照」，未给路径；本 agent 在 `origin/dev-04` 上以 `HoTT/formal/claude-cg001/truncation-questioning/TruncationQuestioning.agda` 作为最接近的实物落点登记。该对应关系是本 agent 的【判断】，编号 `C-83` 与本 repo CG-001 的 `claude-cg001` 命名是否同一物，需 N9/N10 回到 `dev` 的 claim matrix 核对，不建议直接据本表合并。

---

## 审核记录（本 agent 实际执行的检查）

- 读出 `scope.json lines.dev-04`：`own_docs=15`、`anchor_summary{total:15, anchored:11, mechanical_window:4, export_absent_prose:0, unresolved_prose_docs:[]}`、`fork{parent_branch:dev-03, parent_doc:13}`、`adjudication_rounds=11`、`unique_lines=1131`、`export_tail{last_doc_anchored:0015, last_anchor_line:13706, export_lines:13784}`。
- 逐字复核 15 个锚点：11 个 `## User`／`## Codex` 锚点在导出原文定位成功（12291/12527/12667/12693/12713/13054/13165/13349/13519/13642/13706），4 个机械轮窗口内的 `## User` 机械块定位成功（12279–12291 内 L12287、L13347、L13640）。
- 复跑 `python3 -B wflow-lineage/tools/check_lineage.py`（本线部分）：G1 `dev-04: THREAD.md missing`→补齐后 `block 坐标 15/15；裁决#3 轮数 11`；**G2 `dev-04: 全部行双锚/枚举合法`**；G3_full 610 个非 MISSING 判词全部逐字命中语料（本线贡献 110 个 + 4 个 MISSING）；G5 241 个 carried 落点全部可解析（本线 99 个）。
- 自写等价校验（口径复制自该脚本）：114 行全部 12 列；round 覆盖 15/15、缺失 0；`export_line` 越界/窗口外 0；`type`/`status` 枚举非法 0；110 个非 `MISSING` 判词在导出原文逐字命中 110/110（修正 `有限判别树`→`一个有限的判别树` 后通过）；99 个 `carried` 行的 `path@ref` 全部可解析（`os.path.exists` 或 `git cat-file -e origin/dev-04:<path>`，逐条执行）。
- **未执行**：本线没有 Lean/Agda 内核可复跑环境，也未重跑 `verify_zfc_completion_observation_closure.py`；所有【证明】身份均按导出与 QA 原文的收据判词转述，未经本 agent 独立内核验证。
