# dev-08 研究脉络（THREAD.md）

> 线：`dev-08`（GUI 标题「🌟 08 - 哥德尔」，主 checkout 的 `dev` / `origin/dev-08`）。
> 导出：`git-worktree对话录/dev-08 - 20261005T140115Z-01a0fc02-3a4c-7a00-8ab9-f4441dacc4b5-042fff9e8b82-gui.md`（18,458 行，sha256 `845facd9…7752`，见 `wflow-lineage/scope.json`）。
> 分叉：`fork.parent_branch = archive-01a0fb73`、`parent_doc = 10`、`parent_rollout = 01a0fb73-d88b-78b3-a677-349c4641c47e`（同 `audit/GUI-SYNTH-REDO/qa/dev-08/_branch.json`）。
> **轮数口径（R4）**：本文论轮次一律用 `scope.json` 的 QA 块坐标 `docs[].doc`（本线自有轮 127 个，机械轮也计）；裁决 #3 分线轮数 **56** 只作并列引用（来源 `认知闭包/GUI-ASSET-RECOVERY-001.md` §8），两者不互换。
> 锚点：`anchored 102`（`user_block`/`codex_fallback`）、`mechanical_window 24`、`export_absent_prose 1`（0127）。
> 阅读顺序：**尾 → 分叉点**。`export_line` 均指上述 GUI 导出行号；`【原话】/【自述】/【证明】/【判断】` 按 R3 标注，本文件不产出任何数学结论（R7）。

## 分叉出口（本线往后续线交出什么）

| 后续线 | 分叉点 | 该点本线状态 |
|---|---|---|
| dev-03 | 自主干 #75 | 用户判定「ZFC 的问题就是圆环悖论的存在」，ZFC-CIRCLE-Q0 即将开卡 |
| dev-02 | 自主干 #86 | ZFC-Q-ACTUAL-INSTANCE-FORMALIZATION-SOP 刚落盘，C-359/C-360 在造 |
| dev-06 | 自主干 #97 | H0 = B 的反投影路线刚开，H0-Z0-FOUNDATION-ADEQUACY-SOP |
| dev-01 | 自主干 #111 | 总证明闭环刚被用户「暂停一下」 |
| dev-09 | 自主干 #113 | 哥德尔式「神似」讨论刚结束，GODEL-Q-REFLECTION-SOP 将出生 |

树依据 `audit/GUI-SYNTH-REDO/qa/_tree.json`（dev-04 分叉自 dev-03#13、dev-07 分叉自 dev-06#3，其余六线分叉自 dev-08）。

---

## L8 终局推送（#0126–#0127）

- **目标/SOP**：`ZFC-META-SUBTHEORY-ADEQUACY-SOP` 的 C0 后继；末轮为用户要求把 worktree 存到远程 `dev-08`【原话】「你现在的这个git worktree上的工作，我希望保存到远程的dev-08分支上，包括所有代码、文档和对话录记录文件。」
- **GPT 做了什么【自述】**：沿 C0 路线做了两套 Lean 控制（`C-375`–`C-378`：MSS 定义域/时间 carrier 与参数顺序控制），把「时间被消去」分解为四个不可混用的问题；给出 Bliudze–Furic 2014 弹跳球 `SameModelAndConsumerCandidate` 与 Kanovei–Lyubetskii 2007 反控制；末态四行判词写进 C0 manifest。见 `export_line 18229–18311`。
- **发现与判词（逐字）**：`C0R11_SHARED_SIMULATION_TASK_CANDIDATE = SOURCE_SUPPORTED`、`BARE_ZFC_LINK_AND_ADEQUACY = UNPAID`、`SAME_Q_WITH_USER_ZENO_OR_CIRCLE = NOT_YET_PAID`、`C6_CORE_VERDICT = NOT_RELEASED`；0127 推送回执 `本地快照提交已经生成：`7b1f7f60`。`
- **实物**：`HoTT/formal/zfc-mss-domain-time-control/MSSDomainTimeControl.lean`、`HoTT/formal/zfc-mss-phase-order-control/MSSPhaseOrderControl.lean`、`audit/20261005-ZFC-META-SUBTHEORY-ADEQUACY-C0R11-BOUNCING-BALL-SHARED-CONSUMER-CANDIDATE.md`、`audit/20261005-ZFC-META-SUBTHEORY-ADEQUACY-C0R10-NSA-ZFC-SUBTRACTION-SCREEN.md`、`audit/ZFC-META-SUBTHEORY-ADEQUACY-001-C0-CANDIDATE-MANIFEST.md`。
- **为什么转向**：用户从「把工作保存到远程」出发（#0127【原话】），而 GPT 在 #0126 已把 C0 的候选从「抽象时间维度不足」收紧为「标准连续时间 → Zeno 语义边界 → operational-time repair」的来源链【自述】「而不再只是抽象地说“时间维度不足”」；推送只是把这条已收敛的产物固化。
- **沉淀/被接走**：`origin/dev-08` 成为八线共同的快照来源；C-375–C-378 与 C0R10/C0R11 卡进入 `dev`，被 CG-006 的 `Targets与Profile.md` §2.5（Ⅱ-5）引用为「两线没有合账」的未合账项。

## L7 C0 子理论充分性后继扫描（#0123–#0125）

- **目标/SOP**：`ZFC-META-SUBTHEORY-ADEQUACY-SOP`（F-053）后续单元 C1A/C1B/C0R。
- **GPT 做了什么【自述】**：源头核验 set.mm Appendix C（`C-369`：355 变量+$f 类型生成器逐字重生，Lean 无公理证明可数无限新变量扩张）；在 Mizar 原件中定位 `SERIES_1:Th22`/`Th24` 的几何级数形状，与 IEP 的 $1/2+1/4+1/8+\cdots$ 对齐。
- **发现与判词（逐字）**：`存在 Appendix C 的描述性 mapping specification`（同时登记「尚不存在把该 specification 实例化为 `set.mm` 内部 `mFS` witness…的支付」）。
- **实物**：`HoTT/formal/godel-q-reflection/SetMMAppendixCVarExtension-CLAIM.md`、`audit/20261005-ZFC-META-SUBTHEORY-ADEQUACY-C1B-MIZAR-GEOMETRIC-SOURCE-TO-SPEC-CARD.md`。
- **为什么转向**：G0 的哥德尔化在 set.mm 侧碰到「有限数据库 ≠ 无限形式系统」的边界，GPT 自述必须先把 mFS 定义前置条件补上（`C-369`），再转向 C0 的候选重选。
- **沉淀/被接走**：C-369 被 CG-006 记为「补 mFS 定义前置条件，未构造完整 mFS」；因 `C-369` 属三义撞号区，本线该行按 G5 预登记降级 `parked`。Mizar 来源卡进 CG-006 Ⅱ-2 来源链。0125 为机械轮（窗口内只有文件改动清单）。

## L6 上位方案 T-PRECISION-DIAGONAL-SOP（#0121–#0122）

- **目标/SOP**：把用户的想法 `T` 写成可逐层检验的研究程序。
- **GPT 做了什么【自述】**：建立四分片 `T-OBS/T-DIAG/T-Meta/T-ZFC`，并把已有的 `GODEL-Q-REFLECTION-SOP` 明确降级为 `T-DIAG` 的执行模块（复用 G0–G5 与 `CC-20261004-godel-q-reflection`）；同时明确「不新建第二份同义闭包」。
- **发现与判词（逐字）**：`T-PRECISION-DIAGONAL-SOP`、`PLAN_ADOPTED_FOR_CONTINUED_EXECUTION`（`认知闭包/T-PRECISION-DIAGONAL-001.md`）。
- **实物**：`dev-docs/理论精度与哥德尔式自反方案.md`、`认知闭包/T-PRECISION-DIAGONAL-001.md`、提交 `3b516c4a`。
- **为什么转向**：用户在 #0113–#0114 要求「神似而不是形似」地借鉴哥德尔，GPT 在 #0121 自述需要一条能同时容下观察精度与哥德尔式反射的上位程序，否则两条线会各建一份同义闭包。
- **沉淀/被接走**：CG-005 直接吸收 T 框架（`八线分叉后复盘.md` §9.3「T 的框架（T-OBS/T-DIAG/T-Meta/T-ZFC）」）；`C-367` 成为 CG-006 Ⅴa/T-OBS 的机器化前作。

## L5 哥德尔式反射执行 G0（#0115–#0120）

- **目标/SOP**：`GODEL-Q-REFLECTION-SOP` + `CC-20261004-godel-q-reflection`，从 G0 冻结真实 `Accept_T` 开始。
- **GPT 做了什么【自述】**：把 Metamath `set.mm@160ebb63` 冻结为 ZFC-facing proof-acceptance 接口；完成 252,401 statements / 47,917 个 `$p` 的全库 replay；用 Foundation Lean 做正负对照；两轮生态筛选（Mizar/Isabelle/ZF/Coq）作 holdout；Rosetta + Stack 3.11.1/GHC 8.6.5 冻结工具链身份。
- **发现与判词（逐字）**：`ACTUAL_PROOF_ACCEPTANCE_INTERFACE_FROZEN_WITH_SCOPE`、`PARENT_COMPLETION_ACCEPTANCE_INTERFACE_UNDERDETERMINED_WITH_SCOPE`、`完整 Metamath replay成功`。
- **实物**：`dev-docs/哥德尔式ZFC完成观察反射方案SOP.md`、`认知闭包/2026-10-04-哥德尔式ZFC完成观察反射-认知闭包.md`、`HoTT/verification/runs/20261004-SOURCE-REPLAY-SETMM-OBJECT-CODING-001/`。
- **为什么转向**：#0112/#0113 用户提出「哥德尔如何证明了哥德尔不完备性」「神似而不是形似」【原话】，GPT据此判定不能把 proof checker 当成过程完成接口，必须先冻结一个真实、版本固定的接受接口。
- **沉淀/被接走**：G0 的三类来源分离表、`set.mm` replay 收据、Foundation 缺口（`NumeralBridge`/`InternalProvabilityAdequacy`）被 CG-006 的 S2/S3/S4 直接接手（`GUI查阅索引.md` #1、#5）。

## L4 B 侧 H0→Z0 与最终证明闭环（#0097–#0114）

- **目标/SOP**：`H0-Z0-FOUNDATION-ADEQUACY-SOP`（F-047）→ `ZFC-H0-FINAL-PROOF-CLOSURE-SOP`（F-050，M0–M5）→（用户叫停后）`GODEL-Q-REFLECTION-SOP`。
- **GPT 做了什么【自述】**：以 main 的固定 H0 为唯一 B 输入追集合论侧验收链；C-366 在 Foundation 的 Zermelo 模型里实际编译出序数索引序列图；C-365 记 H0 有限 trace；forcing-ticks 编译器停在 GHC 9.0.1/macOS ARM 环境缺口；MPIM 题名消歧后分出 CCHM 与 AWCCRS 两条模型链。
- **发现与判词（逐字）**：`SOURCE_ACCEPTANCE_UNDERDETERMINED_WITH_SCOPE`、`我遇到的是**证据登记层的问题，不是 C-365 的数学失败**`、`**在所有可定义、可支付的 M1–M5 义务完成前，不会再关闭 `/goal`。**`。
- **实物**：`dev-docs/H0-Z0基础验收反投影SOP.md`、`dev-docs/ZFC-H0最终形式化与机器证明闭环SOP.md`、`HoTT/formal/zfc-h0-final-closure/`、`audit/20261004-H0-Z0-HZ0-2-MPIM模型链源追溯.md`。
- **为什么转向**：#0097 用户一句「为什么我觉得你要找的就是 main 分支上的 HoTT 那个事情呢？」【原话】把主线从芝诺侧应用合同扭到 H0→Z0 反投影；#0100 用户质问「为什么你没做完就停下了？」【原话】迫使 GPT 承认把来源停止条件当成总任务停止条件；#0111 用户「暂停一下」【原话】后，#0112–#0114 的哥德尔提问直接生出新方案。
- **沉淀/被接走**：H0 侧材料（C-357/C-358/C-360/C-365/C-366）进入 CG-006 G-5/Ⅳ-4；「M1 未付、forcing-ticks 受阻」成为 CG-006 判定「走 Z0 路线不需要 H0Map」的依据。

## L3 bare ZFC 理论精度（#0093–#0096）

- **目标/SOP**：F-049 + `BARE-ZFC-Q-PRECISION-SOP`（P0–P3 来源合同）。
- **GPT 做了什么【自述】**：固定 bare ZFC 语言/表示层（SEP）、ZFC-supported 应用层完成政策（IEP）、完成合同改写（Norton），再用 Lean 把「只读粗 resolved view 不能决定 OriginDone、富 contract/有限 process code 可以」机器化。
- **发现与判词（逐字）**：`SOURCE_APPLICATION_INTERFACE_CONTROL_COMPLETE`、`BARE_SEMANTIC_INTERFACE_UNDERDETERMINED_WITH_SCOPE`。
- **实物**：`HoTT/formal/bare-zfc-q-precision/BareZFCPrecision.lean`（C-364）、`audit/20261004-BARE-ZFC-Q-PRECISION-P0-P3-来源接口与完成合同.md`。
- **为什么转向**：#0093 用户更正「我一直说的都是 bare ZFC 理论精度不够」【原话，原文见 `dev-notes/0109` 第 58 轮，GUI 导出内为 response-annotations 轮】，GPT 承认此前把用户靶心推成了形式矛盾【自述】「我刚才犯的错，不在于保留“不能写成 `ZFC ⊢ False`”这个边界……」，于是重开 bare ZFC 精度假说。
- **沉淀/被接走**：C-364 成为 CG-006 Ⅴa-2 与 T-OBS 的正控制；`BARE_SEMANTIC_INTERFACE_UNDERDETERMINED` 成为 CG-006 改用「ZFC 可证明哪些过程完成事实」固定接口的动机。

## L2 Q/P/A/B 实际同 Q 实例化（#0085–#0092）

- **目标/SOP**：`ZFC-Q-ACTUAL-INSTANCE-FORMALIZATION-SOP`（F-048），三种合法终点。
- **GPT 做了什么【自述】**：把 Q/P/A/B/ZFC-1 拆成对象层/来源层/政策层；Lean 侧 C-359（政策内矛盾）与 Cubical Agda 侧 C-360（B 证书）；A1–A5 收尾时按来源把终点定为第二种（实际同 Q 被控制拒绝）。
- **发现与判词（逐字）**：`不完全对。`、`**还不能说“我们已经形式化并机器证明了这个实际的 ZFC 矛盾”。**`、`**就这段 Q / P / A / B / ZFC-1 的形式化任务而言，当前这一轮已经完成了。**`。
- **实物**：`dev-docs/ZFC实际同Q实例化与机器证明SOP.md`、`HoTT/formal/zfc-actual-q-policy/`。
- **为什么转向**：#0085 用户问「我们形式化并机器证明了这一点，对吗？」【原话】，GPT 明确否定并把两层分开；#0090 用户要求「继续工作，直至彻底用形式化和机器证明收尾」【原话】；#0092 收在 SOP 预设终点而不再发散。
- **沉淀/被接走**：#0091 的风格化改写（P₀/P₁ 与「数学的灵魂……」句）成为 CG-006 终局判词的前作（`Targets与Profile.md` G-11/Ⅲ-2/Ⅲ-7）；C-359–C-363 与 dev-02 同号异组，按门禁降级 parked 并登记撞号。

## L1 A 侧：圆环与元层观察（#0076–#0084）

- **目标/SOP**：`ZFC-CIRCLE-Q0` 候选卡 + 交叉评审候选 worktree 的形式化包。
- **GPT 做了什么【自述】**：把「圆环复原已完成」变成可反驳问题（什么同一任务内的桥允许这么说）；分出 `Done_formal/Done_revised/Done_strict`；核 IEP/Norton/Bathfield/Sierpińska 原文；评估 dev-03 侧 Lean 三件五命题，指出其证明的是自定义谓词不等价、尚不能单独证明 IEP 偷换原过程。
- **发现与判词（逐字）**：`## 已启动：圆环成为 ZFC 连续统线的第一张候选卡`、`Done_revised`、`O1–O5 问的是**元层**的问题`。
- **实物**：`audit/20261003-ZFC-CIRCLE-Q0-连续统完成与圆环复原候选卡.md`、`HoTT/formal/claude-cg001/`、候选分支 `codex/zfc-observation-boundary-proof`（`CANDIDATE_NOT_CURRENT`）。
- **为什么转向**：#0075 用户判定「ZFC 的问题我们已经找到了，就是圆环悖论的存在」【原话】，GPT 随即把 Power Set 线降级、把圆环设为第一张候选卡；#0077 用户补上 Meta Theory/Sub Theory 的时间维度论证【原话】；#0080 用户批评「你现在是在做什么？」【原话】直接把工作推回来源核对与机器证明。
- **沉淀/被接走**：三种 Done 分解与「完成合同改写」进入 CG-006 Ⅱ-1/Ⅱ-2；C-357/C-358（粗完成不反射原完成）成为 B 侧（G-5）的机器证据。

---

## L0 共享前缀骨架层（#0001–#0075，仅建层名＋一句话）

> 该段是本线与父级 `archive-01a0fb73` 及其余五条支线共有的前缀；六条支线都从这里出发，因此本文件只列层名与一句话，不逐轮展开。逐轮登记见 `DISCOVERIES.tsv` 的 `L0-共享前缀` 行。

| 子层 | 轮次 | 一句话 |
|---|---|---|
| L0-a 选靶层 | #0001–#0007 | 用户从菲尔兹奖得主工作中挑下一个进攻目标，最终把靶定成 ZFC 并要求从罗素悖论计算视角提取模式 P，同时授权 Terra/Max 子代理。 |
| L0-b 模式 P 三把刀 | #0008–#0017 | 盲测负/正控制反复打磨 P：入口门修正后独立选中 Power Set，脱敏正控制通过，P2 未直接表达「张力」从而分出 P3，三把刀各自独立文件＋总索引。 |
| L0-c 锻打与验收 | #0018–#0055 | 「来，现在开始锻刀！」到 V1 打造验收、Tool-BirthCard、全历史逐段对照审计、`P-FORGE-SOP` 与 PowerSetDefenseLedger，最后用户「暂停一下」。 |
| L0-d 审计与文献回流 | #0056–#0075 | 兵棋推演式原子审计、H0–Z0 反投射线索、路线级文献回流收敛出 SourceBackflowGate；判词停在 `ZFC_Q_NOT_LOCATED`，用户随即提出「圆环悖论就是 ZFC 的问题」引出分叉。 |

---

## 附录 A：机械轮（24 轮，`anchor_status=no_prose_mechanical_round`）

`0001 0002 0008 0011 0014 0020 0025 0027 0034 0046 0049 0054 0060 0065 0071 0079 0082 0087 0101 0106 0107 0108 0110 0125`

这些轮的用户块只有 `<external_codex_apps_open_page>`／`<environment_context>`／`<codex_internal_context source="goal">` 等机械注入，没有自然语言提问；`scope.json` 只给 `anchor_window`。它们在 `DISCOVERIES.tsv` 中各有一行，`export_line` 取窗口内可定位行，`verdict_token` 用该机械标记或窗口内的 GPT 自述。注意 0106/0107/0108 共享窗口 `[15218,15490]`，0101 的窗口内是 goal 续跑块（内嵌早轮原文，判词不归该机械轮）。

## 附录 B：0127 轮（`export_absent_prose`，R9.1）

A 层导出止于 0126，0127 在 GUI 导出里没有原文，只能以 QA 轮号锚定；逐字引文取自 `audit/GUI-SYNTH-REDO/qa/dev-08/0127.md`，`DISCOVERIES.tsv` 中该行 `export_line` 留空、`verdict_token` 标 `MISSING`。

## 附录 C：本线读法与陷阱自记账

1. **共享前缀里的父级原文**：`export_line 2–1162`（0001/0002 的窗口）内的菲尔兹奖选靶、另一 AI 回答、Gemini 来源审计等内容归属父级 `archive-01a0fb73#0003–0010`，不算 dev-08 自有提问。
2. **逐字重复的核心提问**：Q/P/A/B 判词段在 #0088/#0091/#0092 连续出现，且同样文本也出现在 dev-02/dev-03/dev-04；本文件只把它归到 dev-08 这些轮的锚点上。
3. **goal 续跑块**：#0019/#0022–#0024/#0031–#0033/#0041–#0045/#0051/#0053/#0063/#0064/#0070/#0101–#0105/#0107–#0109/#0115–#0123/#0126 的锚点是 Codex 汇总块，其用户侧只是 goal 续跑注入。
4. **#0112 哥德尔原话**：实物只在分支 `dev-notes/0109`（`origin/dev-01`、`dev-08`、`dev-09`），`dev` 上没有；GUI 导出内有该句（`export_line 15557`）。
5. **判词字符串来源**：`TERMINAL_CLEANUP_WITHOUT_CLOSE`、`NO_MODEL_RECALL_CANDIDATE` 等在 `assets-ledger.md`/D3 有登记，本文件所选判词均逐字回导出处。
