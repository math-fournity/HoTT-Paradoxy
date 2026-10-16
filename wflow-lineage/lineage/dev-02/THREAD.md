# dev-02 线脉络（"02 - ZFC-1"）

> 本文件是 GUI-LINEAGE-KB 的逐线提取产物，只描述 dev-02 这一条 worktree 对话线自己的研究脉络。
> 它不产出任何数学结论：文中出现的命题、判词、令牌一律标注身份（【原话】= 研究发起人原话、
> 【自述】= GPT 自述，【自述·带收据】= GPT 自述但导出原文同行给出版本闭环/重放令牌，
> 【判断】= 本 agent 或下游审计者的判断）。所有内核是否真的通过，本 agent 未在本机重跑，
> 只按导出原文登记；要升级为"机器证明"须另走项目 F-011 门禁。

## 0. 线身份与坐标口径

| 项 | 值 | 来源 |
|---|---|---|
| 导出 | `git-worktree对话录/dev-02 - 20261004T101101Z-01a10533-7f5c-79b2-8d00-a5d797205ee5-b04cf56b8548-gui.md`（14,194 行；sha256 `f57baad95286b0d179654bc30b918f2a78122a170612946c19d0828c410ffaa7`） | `wflow-lineage/scope.json` lines.dev-02 |
| 分叉 | 自主干 `dev-08` 第 86 号块分出（parent_doc=86，parent_rollout `01a10097-8df9-7dd0-8009-8357ebc59781`） | 同上；`audit/GUI-SYNTH-REDO/qa/dev-02/_branch.json` |
| 自有轮 | 13 个块坐标轮（QA 树 `qa/dev-02/0001.md`–`0013.md`） | scope.json docs[] |
| 裁决#3 轮数 | 10（口径定义在 raw rollout 上，冻结输入层内不可重算，只作并列引用，不与块坐标互换） | scope.json caliber / `认知闭包/GUI-ASSET-RECOVERY-001.md` §8 裁决 #3 |
| 前缀边界 | `prefix_end_line = 13132`；L1–13132 为 dev-08 共享前缀，本文件**不建共享前缀骨架层** | scope.json |
| 自有文本 | UNIQUE=781 行 / 78 区间；SHARED=13,413 行（与 dev-08 逐行 diff） | `audit/GUI-ASSET-RECOVERY/manifest.json` alignment.per_file[dev-02] |
| 锚点概况 | 唯一锚 10、机械轮窗口 3、导出缺文轮 0 | scope.json anchor_summary |
| 运行环境 | linked worktree `/Users/aurolafly/.codex/worktrees/a329/HoTT_AI_HANDOFF_20260911`，2026-10-04，`permission_profile type="disabled"` + `file_system type="unrestricted"` | 导出 L13133-13137 |

**三套坐标不互换**：本文的 `round` 一律是 scope.json 的块坐标轮号（`0001`–`0013`）；`export_line`
是 GUI 导出行号；`qa/dev-02/_index.jsonl` 的 `line_from/line_to`（如 0003 → 13–1652）是**源 rollout
jsonl 坐标，不是导出行号**，本文不把它当导出行号用。

## 1. 分层总表（尾 → 分叉点）

| 层 | 名称 | 覆盖轮（块坐标） | 该层回答的问题 |
|---|---|---|---|
| L1 | 身份与推送治理层 | 0010–0013 | 这条线的成果与归档到底以什么身份、什么 ref、什么范围进入远端 |
| L2 | 判词分层再核层 | 0009 | "形式核心已完成"与"实际 ZFC 判词未完成"的分界线划在哪里 |
| L3 | 形式化收尾层 | 0007、0008 | 语言层/模型层/政策层补齐到 C-365 后，收尾矩阵与停止条件是什么 |
| L4 | 收敛判据层 | 0006 | "研究已进入收尾阶段"意味着什么；完成桥观察边界 Q 如何命名 |
| L5 | 门槛降格层 | 0005 | 同一实际 Q 的门槛从唯一同构降为充分反类比控制后，缺口移到哪里 |
| L6 | P 定义定型层 | 0004 | 数学幻觉 P 到底是什么；弱 P / 强 P 的界线 |
| L7 | 首轮形式化层 | 0003 | Q/P/A/B/ZFC-1 首轮被拆成哪三条机器证据链与哪些反控制 |
| L8 | 机械前缀层（含分叉基座） | 0001、0002 | 运行环境与页面标记；dev-08#86 继承而来的 SOP 基座 |

## 2. L1 身份与推送治理层（round 0010–0013）

**发生了什么。** 形式化收尾后，线尾四轮全部是治理动作：研究发起人要求把 worktree 成果推送到远程
并主动提出 `branch=dev-02`（L14024），GPT 首次拒绝该命名、改推无编号的
`codex/zfc-q-policy-formalization`（L14041）；研究发起人立即否决并给出编号纪律
"现在有4个git worktree，都是同一主题的工作，所以必须编号，你的编号就是02，你必须把这个编号带入。"
（L14045【原话】），GPT 承认"我刚才只按“候选主题分支”的惯例命名，忽略了这四个并行 worktree
属于同一主题、必须用编号建立身份的项目约束"（L14050【自述】），本地分支改名 `dev-02`、
提交 `4ab6bf54` 记录身份、推送 `origin/dev-02` 并删除误建的无编号远端 ref（L14054/L14058）。
随后两轮转向 `dev-notes` 归档：研究发起人问"你记录的问答对话录都推送了吗？"（L14109【原话】），
GPT 核对出 8 项未推送偏差并说明归档 Skill 的默认边界（"它会把用户可见问答保存成本地明文记录，
文件默认是 `0600`，但不会自动 stage、commit 或推送"，L14141【自述】），请用户明确范围（L14145）；
用户答"全部推送"（L14154【原话】），GPT 做密钥模式预检后以 `4005fa80` 精确提交并推送（L14171）。

**为什么转向。** 转向不是 GPT 发起的：第一动因是研究发起人在 L14024 的推送请求 + L14045 的编号
裁定；第二动因是 L14109 对归档可见性的追问。GPT 自己的转向理由写在 L14078【自述】："四个并行
worktree 都在同一主题下推进，编号承担了更重要的协作含义：它让未来的 integrator 一眼知道这份候选
来自哪一个并行工作面。" 同时它在 L14083 用 `CANDIDATE_NOT_CURRENT / INTEGRATION_REQUIRED`
把自己和 canonical `dev` 切开——这与项目治理"git worktree 只能交付 CANDIDATE_NOT_CURRENT"
（顶层 `AGENTS.md` 模式 P 段）一致。审阅范围被固定为 `35448f86^..5e04698c`（L14093），
而不是整条分支历史；`origin/dev` 与 `origin/main` 全程未改、无 force push、未创建 PR（L14098）。

**沉淀。** 编号纪律（A-0531）、`CANDIDATE_NOT_CURRENT / INTEGRATION_REQUIRED` 标注（A-0533）、
归档机制默认边界（A-0534）、`4005fa80` 全量归档推送（A-0535）分别落到
`audit/GUI-ASSET-RECOVERY/assets-ledger.md`，并被
`.claude/goals/CG-006-zfc-complete-formalization/八线分叉后复盘.md` §0 实物表
（`origin/dev-02` = `4005fa80`，领先 `dev` 17 提交）与 `GUI查阅索引.md` #20 引用。

## 3. L2 判词分层再核层（round 0009）

**发生了什么。** 研究发起人把整段 Q/P/A/B/ZFC-1 判词重贴一遍（L13919-13941），问
"的形式化和机器证明，你是否还可以继续推进？还是说已经推进完成了？"（L13943【原话】）。
GPT 给出九步状态表，把整段论证切成三类：已机器化的条件性逻辑核、只局部成立的来源范围、
属数学哲学判断的现实/真理性层。终局判词两句（L13952/L13954【自述】）：
"形式核心已完成；整段论证作为关于实际 ZFC 的判词尚未完成"与"可以继续推进，但不能诚实地说你
整段话已经全部被机器证明。" 它明确否掉了三处容易蒙混的等价：`Q 缺失导致 P` 不能写成纯逻辑定理
（代码作 `gapAdmitsZenoP` 显式前提，L13963）、`ZFC-1 导致 B` "目前没有、也不应声称已经证明"
（L13968）、"反现实、不可计算、数学真理性被交易掉"是数学哲学判断而非 proof assistant 可直接判的
命题（L13970）。当前状态被写成 `SOURCE_POLICY_UNDERDETERMINED_WITH_SCOPE`（L14012）。

**为什么转向。** 直接动因是研究发起人 L13943 的"是继续还是已完成"二选一提问——它迫使 GPT
把"做到哪一步"变成可判定的分层，而不是继续加定理。GPT 自述的理由在 L13972【自述】：
"Q 缺失本身不会在逻辑上强迫 P 出现"，所以"社区实际采用 P"必须由来源支付，这是本轮从
"还能不能再推进"转向"什么样的继续才有实际价值"的关键。

**沉淀与被接走。** 九步状态表与三层状态被 `Targets与Profile.md` §5.3 Ⅲ-5 与 G-7 引用；
`gapAdmitsZenoP`/`QMissing ⇏ P` 与 G-1「对象是 bare ZFC，不是使用模型」直接对应——
`八线分叉后复盘.md` §3【判断】写着"dev-02 的 `ZFCOneUse` 与它同构"、被研究发起人
"我一直说的都是bare ZFC理论精度不够"这句话否定。这是本线最重要的一次**下游否定性接走**。

## 4. L3 形式化收尾层（round 0007 + 机械轮 0008）

**发生了什么。** 研究发起人下令"继续工作，直至彻底用形式化和机器证明收尾"（L13758【原话】）。
GPT 补了两层：C-364——`originDone` 未进入基础层/子理论公开合同时，可构造保留
`membership/input/step/observe/formalDone` 全部不变、却拒绝 `originDone` 的保字段反模型（L13775）；
C-365——最小一阶成员关系语言对所有公式与 theory 的语义不变性，并把连接词范围补全为 `∧`、`∨`、`∃`
（L13777/L13781）。随后是七件套版本闭环、收尾矩阵与两次精确提交
`5e04698c`（收尾矩阵）/`2f30307d`（交接刷新，集成范围固定 `35448f86^..5e04698c`，L13891）。
C-360 的 Cubical Agda 重放被报告为"实际完成"，结果 `PASS_WITH_SCOPE`，"不是只复用旧收据"（L13884）。
中间夹一个纯机械轮：`<external_codex_apps_open_page>{"page_id":null}`（L13915，无 prose）。

**为什么转向。** 动因是研究发起人 L13758 的"直至彻底……收尾"指令；GPT 自述的转向理由在
L13820【自述】："形式化链现在已到达可停止状态：没有留下能靠再补一个抽象 Lean/Agda fixture
消除的逻辑缺口"——即从"继续造定理"转向"把停止条件写成可证伪的两类输入"，并在 L13874 明确
"这不是未完成的 Lean 工作，而是一个被明确隔离的来源／过程合同问题"。

**沉淀。** 收尾矩阵 `audit/20261004-ZFC-FORMAL-CLOSURE-MATRIX.md`、收敛报告
`audit/20261004-ZFC-ACTUAL-Q-RESEARCH-CLOSURE.md`、集成交接单
`audit/20261004-ZFC-Q-POLICY-CANDIDATE-INTEGRATION-HANDOFF.md` 均落在
`origin/dev-02`（本 agent 已用 `git cat-file -e origin/dev-02:<path>` 逐条核过可解析）。

## 5. L4 收敛判据层（round 0006）

**发生了什么。** 研究发起人宣布"我们实际上已经处于ZFC问题查找工作的收尾阶段，也就是研究已经
开始收敛了"（L13607【原话】）。GPT 把靶点改写为可检验版本："当前靶点不是 `ZFC ⊢ False`"
（L13614【自述】），回到 `ZFC-Q-ACTUAL-INSTANCE-FORMALIZATION-SOP`（L13627），
把 IEP 的原典核对从"完全找不到政策 owner"修正为三层来源结构（L13635）：芝诺侧局部完成政策已有
来源、对用户圆环原过程的桥无来源、对 HoTT 的跨案例范围无来源；并命名
"完成桥观察边界 Q"（L13655）。本层产出五部件表（C-359/C-360/C-361/C-362/C-363，L13676-13686）
与七条收尾判词（L13690-13698），其中 `ACTUAL_Q_POLICY_CONFLICT_WITH_SOURCE_BOUNDARY = NOT_REACHED`。
同层给出反控制：Diezel–Goncharov 2020 在 cubical Agda 混合语义中把 Zeno behaviour 与连续时间
当作必须建模的语义因素，"禁止我们声称类型论社区从未看见时间问题"（L13704）。

**为什么转向。** 动因是研究发起人 L13607 的收敛宣告；GPT 的自述理由是 IEP 原文逼出了三层结构
（L13633："IEP 的 Standard Solution 不只是含糊地提“极限有用”"），以及"继续增加泛泛的
‘ZFC、极限、实际无穷、HoTT、完成’材料不会改变这个结论"（L13712）——于是从"找更多来源"
转向"把可结束的判据写死"。

**沉淀与被接走。** 完成桥观察边界 Q 被 `Targets与Profile.md` §5.3 Ⅲ-1 记为本线对"定义 Q"的贡献；
芝诺侧局部完成政策（IEP/SEP/Norton）被 §5.2 Ⅱ-2 与 `GUI查阅索引.md` #14 引用；
`COMPLETION_BRIDGE_OBSERVATION_BOUNDARY_CANDIDATE` 与七判词落 A-0515/A-0519。

## 6. L5 门槛降格层（round 0005）

**发生了什么。** 研究发起人问"你是否可以继续工作，直至全部完成？"（L13568【原话】）。
GPT 回答"我会继续，不把“已经有三条形式定理”误当成整体完成"（L13573【自述】），
随后作出本线最关键的一次**方法退让**：把 `TaskEquiv` 从"同一个实际 Q 的唯一形式"降格为
"充分的反类比控制"（L13577："芝诺运动与 HoTT 程序不必有可逆的状态空间同构"），并把 P 的来源
形态从"隐形偷换"扩展为"来源归属的完成范围政策"（L13583）。同时声明自己分支的身份：
"当前分支不是 `dev` 的 current truth，而是一个可审计的候选分支"（L13595）。最后拒绝把
`PolicyScopeWitness` 当历史证据：它"只能形式化适用范围的蕴含，不能在内核里证明某篇文献的作者
确实承担了这个范围"（L13599），并重新捕获 C-359 收据（L13603）。

**为什么转向。** 动因是研究发起人 L13568 的"直至全部完成"——它问的是完成度，GPT 因此必须检查
"还差什么"，检查结果就是门槛过强。自述理由见 L13577/L13583：跨领域比较过强、来源从不说
"极限一出来原过程当然完成"，因此唯一同构门槛与"隐形偷换"叙事都必须放宽，否则会把未支付的
范围承诺伪装成已证前提。

**沉淀。** A-0509（TaskEquiv 降格 + C-359 两层化）、A-0510（完成范围政策 + PolicyScopeWitness）、
A-0511（完成模式共享 vs 政策范围未共享）、A-0512（非历史证据修正）。`PolicyScopeWitness`
成为 L2/L3 层"外部前提必须独立支付"的形式落点。

## 7. L6 P 定义定型层（round 0004）

**发生了什么。** 研究发起人只问了一句："所以，数学幻觉P到底是什么？你知道了吗？"
（L13432【原话】）。GPT 先回读核心认知再给定义（L13437），定型为
"数学幻觉 P 是一种未经支付的“完成提升规则”：它把某个形式模型中的完成 `Done_formal`，升级为
原来的、带时间和过程要求的任务已经完成 `Done_origin`，却没有证明两者是在同一任务、同一状态、
同一允许操作、同一观察和同一完成标准下等价"（L13449【自述】），并写成
`P(T) :  formalDone_T(s)  ⟹  originDone_T(s)`（L13454）。同时钉死三条界线：
"极限不是 P；‘极限已经替原过程完成了那件事’才是 P 的候选位置"（L13481）；
弱 P（改称 `revisedResolved`、公开承认标准变）还不是幻觉，强 P（无桥冒充原完成）才是（L13490）；
关键是"重新定义之后，是否仍声称已经完成了原来的问题"（L13492）。
最后把开放问题改写为可来源推翻的一句（L13557）："哪一份实际来源，在什么精确任务上，把它的
`Done_formal` 当作原过程的 `Done_origin`，又没有支付这一提升？"

**为什么转向。** 动因就是研究发起人这一问——它不要求新定理，只要求把术语钉住。GPT 的自述理由
在 L13437【自述】："P 不是‘极限’本身，也不是 ZFC 的某条公理，更不是只要看到数学模型就叫幻觉的
泛称"，所以要"先对齐原文，再给出一个不偷换强弱层次的定义"。这一层之后，全线的问题形态从
"极限理论是不是幻觉"变成"哪一个来源在哪个任务上没付桥"。

**沉淀与被接走（本线最主要的下游去向）。** A-0506/A-0507/A-0508 三条资产被
`Targets与Profile.md` §5.3 Ⅲ-2 与 G-3、`GUI查阅索引.md` #10 引用为"P 的语义定义"来源；
`docs/ZFC时间维度观察力不完备-哥德尔式Q终局报告-20261008.md` §11 附近写着"语义侧：dev-02 的强 P
（把形式完成冒充原过程完成）、dev-04 的‘无桥完成代换’、主干第 91 轮的 P₁，说的都是
`Done_formal → Done_origin`"。

## 8. L7 首轮形式化层（round 0003）

**发生了什么。** 本线的种子轮：研究发起人给出 Q/P/A/B/ZFC-1 全篇（L13146-13165【原话】），
要求"最大程度地形式化并机器证明这一切"（L13165）。GPT 的第一动作是分层（L13170）：
"可证明的数学核、可核验的来源事实、以及仍属于研究假说的现实与‘数学真理性’判断"。
随后它在 a329 工作树里发现一份**未提交**的 `zfc-actual-q-policy` 初稿并指出其缺陷：
"目前‘同一个 Q’仍由来源状态指纹相等表达，两个都‘未观察到’的字段可能被误当成相同 Q"
（L13174）；又发现"Lean 部分原本并未通过，错误被 `#print axioms` 的输出掩盖了"（L13178），
用实际任务等价模型替代错误路径后无公理重跑。工具侧修了收据捕获器把 linked worktree 的 `.git`
文件误判为"必须是目录"的问题（L13190）。数学侧产出三链：C-359（Lean 条件性政策后果）、
C-360（原生 Cubical Agda 完成反射反例，`¬ ((runFor 0 (question TU judgeTU) ≡ just 1) → ...)`，
L13320）、C-361（几何级数 `1-2^{-n}` 与闭区间端点正控制，L13341）。两条反作弊控制写进终局
（L13211/L13212）："来源表相等不等于任务相同"、"ZFC-1 不会凭逻辑自动制造 B"。
提交落在本地候选分支 `codex/zfc-q-policy-formalization`：`35448f86`、`d17abfb9`、`0c170c4b`
（L13382-13388）。core 侧准备了 generation-14 curation 候选，预演生成 `KC-000063`、保留 62/62
前代映射，但因 canonical STATE/HEAD 已有未提交 checkpoint 而未覆盖（L13392）。

**为什么转向。** 动因是研究发起人 L13165 的最高强度指令（"最大程度地形式化并机器证明这一切"）。
GPT 的自述转向理由集中在两处：L13182"两条必须同时闭合的链"（逻辑核 + 实际实例链），
以及 L13230-13231 与 dirty `dev` 里 10c8 候选的分工——"保留它的 C-361，采用我的 `TaskEquiv`
门槛替换它的 metadata-equality 门槛"。后者正是本线与后来 dev-03 线（worktree `10c8`）的
互补关系：实分析控制归 C-361，同 Q 门槛归本线的 `TaskEquiv`。

**文本归属警告（语料固有重复，须按块坐标读）。** 本轮用户长文 L13146-13163 与父线 dev-08
L13149-13166 **逐字节相同**（manifest 判 SHARED）；本行独有的只有 L13164-13165 的
"魔鬼交易"结尾（一行合并写法）。L6 层引用的"与魔鬼交易"因此属研究发起人原话，其文本在
`sources/prompts/Codex-ZFC-Q-P-A-B-ZFC1-用户原文-20261004.md`（`origin/dev-02` 上可解析）。
到 round 0009，研究发起人重贴的同一段全文（L13919-13941）与 dev-08 L13868-13899 逐字节相同
（manifest SHARED），且该段在 dev-08 的 0091/0092 两轮都出现过——**不能**因为文本相同就把它
归到 dev-08 的轮或本线的 L7 层：块坐标上它是 dev-02 的 round 0009。

**沉淀与被接走。** A-0495~A-0505、A-0508 等落在 `assets-ledger.md`；
C-360/C-361 被 `八线分叉后复盘.md` §3【实物】记为"C-360、C-361 在 CG-005 中重放通过（CG-005 审计
报告 §5）"；同时 §3【判断】记下本线的局限："ZFC 被写成占位符，A↔P、P→B 是手放的规则（“形似”，A1）"
——`Targets与Profile.md` §9.5 另记"C-359 至 C-365（`dev` 与 dev-02）撞号"，合并前须重新编号。

## 9. L8 机械前缀层与分叉基座（round 0001、0002）

**发生了什么。** 前两个自有轮没有 prose：round 0001 只有 `<environment_context>`
（cwd=`/Users/aurolafly/.codex/worktrees/a329/HoTT_AI_HANDOFF_20260911`、2026-10-04、
America/New_York、`permission_profile type="disabled"`、`file_system type="unrestricted"`，
导出 L13130-13138）；round 0002 只有 `<external_codex_apps_open_page>{"page_id":null}`（L13140-13142）。
round 0008（L13915）是同型机械轮，归入 L3 层登记。

**为什么转向。** 这一层没有研究转向，它是运行包裹。它仍然必须出现在 DISCOVERIES 里：scope.json
把 `anchor_status=no_prose_mechanical_round` 也算作本线自有轮（块坐标），
`check_lineage.py` 的 G1 分母同样计入机械轮。

**分叉基座。** dev-02 从 `dev-08` 第 86 块分出。该块（`audit/GUI-SYNTH-REDO/qa/dev-08/0086.md`）
建立了可引用的 `ZFC-Q-ACTUAL-INSTANCE-FORMALIZATION-SOP`，把终局定义为三种同等有效的可审计结果：
`ACTUAL_Q_POLICY_CONFLICT_WITH_SOURCE_BOUNDARY` / `ACTUAL_Q_UNIFICATION_REJECTED_WITH_SCOPE` /
`SOURCE_POLICY_UNDERDETERMINED_WITH_SCOPE`，并规定原过程 `OriginDone` 无法冻结时诚实停止为
`USER_DONE_ADJUDICATION_REQUIRED`。dev-02 的 L2/L3 层判词（`NOT_REACHED`、
`SOURCE_POLICY_UNDERDETERMINED_WITH_SCOPE`、`USER_DONE_ADJUDICATION_REQUIRED`）正是这套 SOP
词汇——这条基座是 dev-02 全部判词语言的来源，但它属于父线程内容，本文件不展开为骨架层。

## 10. 语料固有缺口与本 agent 的未知项（供 Master 登记 ledger）

1. **机械轮无 prose**：round 0001、0002、0008 的 User 块分别是 environment_context 与页面标记，
   导出内没有任何可摘判词；DISCOVERIES 中这三轮的 `verdict_token` 一律为 `MISSING`
   （已按 R2 说明原因）。这不影响 G1 覆盖。
2. **裁决#3 轮数（10）与块坐标（13）不同源**：前者定义在 raw rollout（冻结输入层不可重算），
   后者是 QA 树块坐标。本文两者并列，不互换、不互相校验。
3. **共享段重复**：L13146-13163 与 L13916-13947 是全语料级的重复用户原话（src dev-08）。
   轮次归属只认 QA 树块坐标；文本相似度不能反推轮次归属。
4. **本轮所有"内核通过/版本闭环/重放完成"令牌都是 GPT 自述**：C-360 的 `PASS_WITH_SCOPE`、
   `SELECTED_PACKAGES_VERSION_CLOSED`、`4005fa80` 等，本 agent 未在本机重跑任何 Lean/Agda 内核，
   只核对了 `origin/dev-02:<path>` 的 git 可解析性。要让它们成为"机器证明"，须另走项目
   数学结论机器证明门禁。
5. **`origin/dev-02` 与 canonical `dev` 撞号**：C-359–C-365 在 `dev` 上另指一组
   （`八线分叉后复盘.md` §9.5、`Targets与Profile.md` §9.5）；dev-02 与 dev-03 各有一份互相竞争的
   generation-14 core curation 草稿（§9.2），`KC-000063` 未成为 current core。
6. **dev-08 #112 哥德尔原话只存在于 dev-notes 分支**，GUI 导出内有、但不在 dev-02 分叉点之后，
   本线从未读到它；本线也不承载任何哥德尔路线内容。

## 11. 本线的关键一次转向（一句话）

**round 0004 研究发起人一句"所以，数学幻觉P到底是什么？你知道了吗？"（L13432）逼出了
`P(T) : formalDone_T(s) ⟹ originDone_T(s)` 的定型定义与弱/强 P 界线**——此后全线不再问
"极限理论是不是幻觉"，而是问"哪一份来源、在什么任务上把 `Done_formal` 当 `Done_origin`
又没付桥"，round 0005 的门槛降格、round 0006 的三层来源结构、round 0009 的
`SOURCE_POLICY_UNDERDETERMINED_WITH_SCOPE` 都由这一问派生。
