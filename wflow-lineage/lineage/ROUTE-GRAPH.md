# ROUTE-GRAPH · 八线跨线传播图（节点＝层，边＝供给／否决／接走）

> 由 GUI-LINEAGE-KB 综合 agent（N9）生成，2026-10-10。节点取八份 `wflow-lineage/lineage/<线>/THREAD.md` 的层；
> 边只登记**跨线**作用（同线层间顺序由各 THREAD「尾→分叉」结构自证，不在此重复）。
> **R7**：本文件只登记脉络与判词的身份与传播，不产出任何数学结论；所有判词逐字照录并保留原身份（【原话】/【自述】/【证明】/【判断】）。
> **R1**：每条边都带轮次锚（QA 块坐标，来自 `wflow-lineage/scope.json` 每线 `docs[]`）与导出行号或 CG-006 文件行号。
> **R5**：两说冲突见图末「并陈」节，交审计员处置。

## 1. 分叉树（依据 `audit/GUI-SYNTH-REDO/qa/_tree.json`，2026-10-08 生成）

```text
archive-01a0fb08 ──#3→ archive-01a0fb73 ──#10→ dev-08（主干「🌟 08 - 哥德尔」；主 checkout 的 dev）
   dev-08 #75  ─→ dev-03 ──#13→ dev-04
   dev-08 #86  ─→ dev-02
   dev-08 #97  ─→ dev-06 ──#3→  dev-07
   dev-08 #111 ─→ dev-01
   dev-08 #113 ─→ dev-09
```

`_tree.json` 机械字段（`cutoff.end_ordinal_exclusive`）：dev-03 41209／dev-02 46347／dev-06 51663／
dev-01 55523／dev-09 55673／dev-04 45352／dev-07 51768／dev-08 4120；
各线 `fork.parent_doc` 与上表逐字一致（`wflow-lineage/scope.json` ↓lines.<线>.fork）。
八线自有轮合计 **239**（块坐标，机械轮也计）；裁决 #3 口径合计 124，两者不互换（R4、ledger PRE-4 DECISION）。

## 2. 节点表（层＝节点）

层名与轮次区间逐字取自各线 THREAD；「该层判词」取该层 `DISCOVERIES.tsv` 的 `verdict_token`（逐字，R2）。

| 节点（线/层） | 轮次 | 该层在做什么 | 该层判词（逐字） |
|---|---|---|---|
| dev-08／L0-共享前缀骨架层 | #0001–#0075 | 选靶→模式P三把刀→锻打与验收→审计与文献回流：六条支线共同继承的父线程内容（archive-01a0fb73#0003–0010 与 dev-08 自有前段） | `ZFC_Q_NOT_LOCATED`、`TOOL_ONLY_DRIFT`（#0072–0073 终点，Targets §2.0） |
| dev-08／L1-A侧：圆环与元层观察 | #0076–#0084 | 圆环=ZFC 的问题→ZFC-CIRCLE-Q0；三种 Done 分解；C-357/C-358 | `## 已启动：圆环成为 ZFC 连续统线的第一张候选卡` |
| dev-08／L2-Q/P/A/B 实际同Q 实例化 | #0085–#0092 | F-048 三种合法终局；C-359~C-363；#0091 风格化改写 P₀/P₁ | `**还不能说“我们已经形式化并机器证明了这个实际的 ZFC 矛盾”。**` |
| dev-08／L3-bare ZFC 理论精度 | #0093–#0096 | 「我一直说的都是 bare ZFC 理论精度不够」→F-049；C-364 | `BARE_SEMANTIC_INTERFACE_UNDERDETERMINED_WITH_SCOPE` |
| dev-08／L4-B侧 H0→Z0 与最终证明闭环 | #0097–#0114 | H0=B 反投影；F-050 M0–M5；#0111 暂停 | `**在所有可定义、可支付的 M1–M5 义务完成前，不会再关闭 `/goal`。**` |
| dev-08／L5-哥德尔式反射执行 G0 | #0115–#0120 | set.mm 冻结为 proof-acceptance 接口；252,401 statements 全库 replay | `ACTUAL_PROOF_ACCEPTANCE_INTERFACE_FROZEN_WITH_SCOPE` |
| dev-08／L6-上位方案 T-PRECISION-DIAGONAL | #0121–#0122 | T-OBS/T-DIAG/T-Meta/T-ZFC 四分片；哥德尔 SOP 降为 T-DIAG 执行模块 | `T-PRECISION-DIAGONAL-SOP`、`PLAN_ADOPTED_FOR_CONTINUED_EXECUTION` |
| dev-08／L7-C0 子理论充分性后继扫描 | #0123–#0125 | set.mm Appendix C（C-369）；Mizar SERIES_1 | `存在 Appendix C 的描述性 mapping specification` |
| dev-08／L8-终局推送 | #0126–#0127 | C-375~C-378；Bliudze–Furic；#0127 推送 dev-08 | `C0R11_SHARED_SIMULATION_TASK_CANDIDATE = SOURCE_SUPPORTED` |
| dev-03／L0 机械轮 | 0001、0002、0007 | 机械注入轮，无 prose | `MISSING` |
| dev-03／L1 元理论精度→O1–O5→候选终局判词 | 0003–0005 | Meta/Sub Theory；三层责任表；O1–O5 五层表 | `CANDIDATE_TERMINAL_WORDING`（候选终局语言） |
| dev-03／L2 来源卡转向机器证明 | 0006、0008 | IEP/SEP/Bathfield/KLV 四来源线；ObservationBoundary.lean；两次 Battle 失败收据 | `SOURCE_TASK_CONTRACT_SPLIT` |
| dev-03／L3 同 Q 异判与统一判词 | 0009–0014（0014 机械） | 「同 Q 异判悖论」命名；ZFC-HOTT-Q-UNIFORMITY-SOP；MetaObservationConsistency | `PROFILE_MISMATCH_CONTROL_CONFIRMED` |
| dev-03／L4 Q/P/A/B 政策演算与 P 的定义 | 0015–0017 | P(F,D) 定义；Q=完成资格观察力；QuestioningDelay 是 P 探测器 | `object_level_false_requires_formal_incompatibility` |
| dev-03／L5 实际映射与收敛收尾 | 0018–0021 | UOU 来源卡；四桥判定；M6 收敛 | `EVIDENCE_FRONTIER_REACHED_WITH_SCOPE`、`ACTUAL_P_CANDIDATE_CONFIRMED_WITH_SCOPE` |
| dev-03／L6 整树快照发布 | 0022–0026 | `origin/dev-03`=854a6aba 整树快照 | `PASS`（353 个 payload 逐项 SHA-256） |
| dev-04／L0 机械轮 | 0001、0002 | 机械注入轮，无 prose | `MISSING` |
| dev-04／L1 Q/P/A/B 元政策演算与来源审判 | 0003 | P 的两个侧面之语义侧起点；H099 六判词族 | `SAME_TASK_BRIDGE_MISSING`、`ACTUAL_COMMUNITY_ADOPTION_UNPROVED` |
| dev-04／L2 P 的命名与收束判词 | 0004–0007 | 核心命名「无桥完成代换」；R1/R2/R3 门；C-83 截断作 B | `CompletionSubstitutionP`（门规格 R1+R2+R3 缺失） |
| dev-04／L3 收尾可检验化：复跑与并行候选线独立核验 | 0008 | `ea6c338f` 独立重跑 dev-02 的 C-359~C-365；CCTTmini 之前四条 Agda 重放 | `Q_SAFETY_REPAIR`、`PASS`（九项 run） |
| dev-04／L4 收敛收尾：B→P 回溯、Meta/Sub 与文献回流 | 0009–0011（0010 机械） | B→P 回溯定理；MetaSubtheoryAudit；B0–B5 回流 | `SOURCE_FRONTIER_REFINED`、`ZFC_Q_NOT_LOCATED` |
| dev-04／L5 工作线快照发布到 origin/dev-04 | 0012–0015（0013 机械） | 用户目标澄清两次；detached HEAD 事实更正；`69aa5aab` 非强制显式 refspec 推送 | `PASS`（`verify_zfc_completion_observation_closure.py` 等三组校验）|
| dev-02／L8 机械前缀层与分叉基座 | 0001、0002 | 运行环境；dev-08#86 继承的 SOP 基座 | `MISSING`（机械轮） |
| dev-02／L7 首轮形式化层 | 0003 | Q/P/A/B/ZFC-1 拆三层；C-359/C-360/C-361 三链 | `ZFCOneUse + SameActualQ + B ⟹ False`（C-359 条件性） |
| dev-02／L6 P 定义定型层 | 0004 | `P(T) : formalDone_T(s) ⟹ originDone_T(s)`；弱/强 P 界线 | `weakP≠强P`（界线；原话见 L13490） |
| dev-02／L5 门槛降格层 | 0005 | TaskEquiv 降格为充分反类比控制 | `ALIGNED_WITH_SCOPE`（P1/P2/P3 同 profile） |
| dev-02／L4 收敛判据层 | 0006 | 「收尾阶段」宣告；三层来源结构；完成桥观察边界 Q | `ACTUAL_Q_POLICY_CONFLICT_WITH_SOURCE_BOUNDARY = NOT_REACHED` |
| dev-02／L3 形式化收尾层 | 0007+0008（机械） | C-364/C-365；七件套版本闭环 | `PASS_WITH_SCOPE`（C-360 Cubical Agda 重放） |
| dev-02／L2 判词分层再核层 | 0009 | 九步状态表；三类分层 | `形式核心已完成；整段论证作为关于实际 ZFC 的判词尚未完成` |
| dev-02／L1 身份与推送治理层 | 0010–0013 | 编号纪律；`origin/dev-02`=`4005fa80` | `CANDIDATE_NOT_CURRENT / INTEGRATION_REQUIRED` |
| dev-06／L0 机械前缀 | 0001、0002 | 机械注入轮，无 prose | `MISSING` |
| dev-06／L7 MPIM 降格 + 认知闭包执行失败自省 | 0003、0004 | MPIM/AWCCRS 降为条件支线；认知写回漏项 | `EXECUTION_DEVIATION / COGNITIVE_WRITEBACK_OMISSION` |
| dev-06／L6 方案复用与 Host Goal 绑定 | 0005、0006 | 复用 `a9c27282`（H0-Z0-PATTERN-FIRST-CONVERGENCE-SOP） | `SOURCE_ACCEPTANCE_UNDERDETERMINED_WITH_SCOPE` |
| dev-06／L5 PF-B 第一轮：三刀盲发现 | 0007（0008 机械） | 三把刀只重定位 formation 位点 | `P_MATCH_RELOCATES_FOUNDATION_FORMATION_SITES_ONLY` |
| dev-06／L4 方向漂移五档审查 | 0009 | 五档逐项判定 | `EXECUTION_DEVIATION`（all-subobjects→ω profile 扩展） |
| dev-06／L3 P 再审与 process-anchor | 0010 | H0 五关键部分；PF-B2 过程锚再审 | `IDEA_SPEC_INCOMPLETE / Q_SAFETY_REPAIR` |
| dev-06／L2 有界收尾：PF-B2 盲态 P1 负控制 | 0011（0012 机械） | 六行有界结论表；Goal 有界完成 | `NO_MODEL_RECALL_CANDIDATE / FORMATION_ORIGIN_NOT_SUPPLIED`、`P_MATCH_NO_SITE_WITH_SCOPE` |
| dev-06／L1 成果保存 | 0013 | `origin/dev-06`=`86ad33c4` 首次创建并推送 | （Git 谱系；无判词） |
| dev-07／L0 机械前缀 | 0001、0002 | 机械注入轮，无 prose | `MISSING` |
| dev-07／L5 方案原始创建与三刀首轮盲发现 | 0003 | `H0-Z0-PATTERN-FIRST-CONVERGENCE-SOP` 出生地；三把盲态刀 | `H0-Z0-PATTERN-FIRST-CONVERGENCE-SOP`（方案名） |
| dev-07／L4 PF-1 收官：命名 ZFC 的 P1 选中 ω 完成性 | 0004 | Metamath ω 来源卡；两个形成候选有界处理 | `P_CANDIDATE_NOT_YET_A_B_BRIDGE`（次轮降级） |
| dev-07／L3 用户 A/B 追问 → 五对象、ω 降级 | 0005 | A/B/Q/P/Z0 五对象定义表；limit-union 候选 | `P_CANDIDATE_NOT_YET_A_B_BRIDGE` |
| dev-07／L2 A/B 硬门、四站位筛选与 Goal 有界完成 | 0006 | AProjection+BProjection+SameQBridge 三项硬门；PF-B2 过程锚合同 | `ACTUAL_Z0_NOT_LOCATED`、`ACTUAL_SAME_Q_BRIDGE_NOT_LOCATED` |
| dev-07／L1 保存与远端 dev-07 收口 | 0007、0008 | `origin/dev-07`=`49624878`；「全部带上，全部推送」覆盖默认归档规则 | `PASS_WITH_SCOPE`（数学交付治理检查） |
| dev-01／L10 F-050 总闭环恢复与有界收尾 | 0001–0006 | 承接 dev-08#111 暂停点；M0–M5 有界收尾；forcing-ticks 受阻 | `BARE_ZFC_COMPLETION_INTERFACE_FORMAL_TARGET_UNDERDETERMINED_WITH_SCOPE`、`SYSTEM_GHC_COMPATIBILITY_PROBE_INCONCLUSIVE_NO_COMPILER_BUILD` |
| dev-01／L9 dev-01 首次保存为工作树快照分支 | 0007–0008 | `origin/dev-01`=`ca1259fe` 快照 | （Git 谱系） |
| dev-01／L8 F-050 收尾语义澄清 | 0009 | 「工作包完成≠研究结束」 | `CLOSED_WITH_SCOPE` |
| dev-01／L7 `/goal` 连续执行合同与方案命名 | 0010 | 三层停止表 | `T-PRECISION-DIAGONAL-SOP`（既有稳定名承接） |
| dev-01／L6 T-PRECISION-DIAGONAL-SOP 连续执行与 ACL2 入口 | 0011–0012 | ACL2 判别；T 分母闭合被拒绝读成研究结束 | `ACL2_ZENO_SOURCE_INGRESS_NO_ADMISSIBLE_T_TARGET_WITH_SCOPE`、`CURRENT_T_PRECISION_SOURCE_DENOMINATOR_CLOSED_WITH_SCOPE` |
| dev-01／L5 核心层偏航自省 | 0013 | set.mm proof acceptance 当观察接口＝最关键的偏航 | （自省；无判词令牌） |
| dev-01／L4 新核心方案建立 | 0014–0015 | `ZFC-META-SUBTHEORY-ADEQUACY-SOP` 落盘；C0 manifest | `C0_UNIVERSE_FROZEN / CORE_TARGET_NOT_YET_ENTERED` |
| dev-01／L3 C0–C6 执行与最终充分性判词 | 0016–0019 | C-369/C-370/C-371；六不证明+反控制 | `CORE_ADEQUACY_FAILURE_WITH_SCOPE`、`SELECTED_PACKAGES_VERSION_CLOSED / HEAD_BYTES_CHECKED` |
| dev-01／L2 「人话总对账」 | 0020 | 目标/进度/三座未付桥；四项终局义务 | （四项义务清单） |
| dev-01／L1 终态保存与全量推送 | 0021 | `origin/dev-01`=`cd9e34b2` | （Git 谱系） |
| dev-09／L0 机械轮 | 0001、0002 | 机械注入轮，无 prose | `MISSING` |
| dev-09／L1 想法 T 与其方案化 | 0003–0005 | 想法 T 原话；T 四层结构；T-OBS/T-DIAG/T-ZFC | `PLAN_READY / EXECUTION_NOT_STARTED` |
| dev-09／L2 T0 与连续执行 | 0006–0008（0007 机械） | C-367（T-OBS）/C-368（T-DIAG）；T-Meta/T-ZFC 的 set.mm 拒绝 | `BARE_ZFC_COMPLETION_INTERFACE_FORMAL_TARGET_UNDERDETERMINED_WITH_SCOPE`、`T0_COMPLETED / T-OBS_C367_MACHINE_PROVED_WITH_SCOPE` |
| dev-09／L3 第一次保存 | 0009 | `origin/dev-09`=`1c34aaee` 快照 | （Git 谱系） |
| dev-09／L4 哥德尔路线继续性澄清 | 0010 | 「哥德尔这条路已无法继续」被否；停的是归因桥 | `ACTIVE / TASKSPEC_FROZEN / IMPLEMENTATION_NOT_STARTED` |
| dev-09／L5 GODEL-ZFC-CONVERGENCE-SOP 建立 | 0011 | 四片 SOP＋闭包；LOCAL_CLOSED→SUCCESSOR_REQUIRED | `LOCAL_CLOSED` 必定进入 `SUCCESSOR_REQUIRED` |
| dev-09／L6 R3/R4 刀具链与 CCTTmini 片段 | 0012–0013 | Foundation 重放；CCTTmini₀（C-370~C-382） | `LATER_COMMAND_SOURCE_MISMATCH`、`LOCAL_EVIDENCE_PASS_NOT_VERSION_CLOSED` |
| dev-09／L7 总闭环 C2/C3 | 0014 | I-001 总合成；七路线核对 | `ALL_DECLARED_ROUTES_REJECTED_WITH_SCOPE`、`FORMAL_TARGET_UNDERDETERMINED_WITH_SCOPE`、`NO_BARE_ZFC_OBJECT_LANGUAGE_INCONSISTENCY_CLAIM`、`TOTAL_CLOSED_BY_C2_C3` |
| dev-09／L8 终局保存：双亲 merge | 0015（机械）–0016 | `origin/dev-09`=`ac6391b6`；DUPLICATE_SESSION | `DUPLICATE_SESSION` |

## 3. 边表 A：供给（父线程分叉点把什么交给子线）

| # | 源节点 | 分叉点锚 | 目标节点 | 交出了什么（判词/原话逐字） | 证据 |
|---|---|---|---|---|---|
| S-1 | dev-08 L0-共享前缀 | dev-08 #0001–#0075（前缀止 L15556；L2–1162 归属 archive-01a0fb73#0003–0010） | dev-03／dev-02／dev-06／dev-01／dev-09／dev-04（经 dev-03） | 靶=ZFC、模式 P 先于靶标、显眼起点、三把刀与盲测纪律；Q/P/A/B 判词长文亦在此首次成段 | `dev-08/THREAD.md` L0-a~L0-d 与附录 A.1；`Targets与Profile.md` §2.0；`GUI查阅索引.md` §2 |
| S-2 | dev-08 L1-A侧 | dev-08 #0075（导出行 10700【原话】） | dev-03 L1 | 【原话】「ZFC 的问题我们已经找到了，就是圆环悖论的存在」→开出 `ZFC-CIRCLE-Q0`，圆环成为第一张候选卡 | `dev-08/THREAD.md` 分叉出口表与层 L1；`八线分叉后复盘.md` §8 #76–#80；`Targets与Profile.md` §2.0 #74–#75 |
| S-3 | dev-08 L2-Q/P/A/B | dev-08 #0086（`ZFC-Q-ACTUAL-INSTANCE-FORMALIZATION-SOP` 刚落盘） | dev-02 L8 分叉基座 | 三种合法终局 SOP 词汇＋`OriginDone` 无法冻结时诚实停止为 `USER_DONE_ADJUDICATION_REQUIRED` | `dev-02/THREAD.md` §9「分叉基座」；`dev-08/THREAD.md` 分叉出口表 |
| S-4 | dev-08 L4-B侧 | dev-08 #0097（【原话】「为什么我觉得你要找的就是 main 分支上的 HoTT 那个事情呢？」） | dev-06 L7 | H0=B 的反投影路线刚开，`H0-Z0-FOUNDATION-ADEQUACY-SOP` | `dev-08/THREAD.md` 层 L4 与分叉出口表；`dev-06/THREAD.md` §0 分叉点语境；`八线分叉后复盘.md` §8 #97 |
| S-5 | dev-06 L7 | dev-06 #0003（【原话】「这事很重要吗？你必须参考它吗？……」） | dev-07 L5 | 一条对 MPIM 支线的质疑；a329 之外的并行 worktree 已有同题方案草案（后由 dev-07 在 #0003 原始创建为 `a9c27282`） | `dev-07/THREAD.md` §0 分叉点语境与 L5；`dev-06/THREAD.md` L6（L14846 自述复用）；`assets-ledger.md` A-0543/A-0556 |
| S-6 | dev-08 L4 | dev-08 #0111（【原话】「暂停一下」） | dev-01 L10 | 被暂停的 `ZFC-H0-FINAL-PROOF-CLOSURE-SOP`（F-050，M0–M5 未收）与 forcing-ticks 受阻现场 | `dev-08/THREAD.md` 层 L4 与分叉出口表；`dev-01/THREAD.md` 分叉点节与层 10 |
| S-7 | dev-08 L5 | dev-08 #0113（【原话】「神似，而不是形似的」；哥德尔原话 #0112 只在 `dev-notes/0109`） | dev-09 L1 | Code/Accept/OriginDone/diag/Reflection 五角色与六道门的「哥德尔结构草图」 | `dev-09/THREAD.md` 分叉入口节；`dev-08/THREAD.md` 层 L5；`GUI查阅索引.md` §1 #7 |
| S-8 | dev-03 L3 | dev-03 #0013（`PROFILE_MISMATCH_CONTROL_CONFIRMED` 终局之后） | dev-04 L1 | QProfile 终局与「芝诺与 H0 不是同一个完整 QProfile」的反控制；Q/P/A/B 判词同文 | `dev-04/THREAD.md` 分叉点节与「与父线的分工」；`dev-03/THREAD.md` L3 |

## 4. 边表 B：否决（用户或下游否定某条线／某个读法）

| # | 否决者（轮次锚） | 被否决者（节点） | 否决内容（原话/判词逐字） | 后果 | 证据 |
|---|---|---|---|---|---|
| V-1 | dev-01 #0013（导出行 16284） | dev-01 L5 自身 | 【原话】「所以你到底做到什么程度了？到底是不是一直在外围，没有进入问题的核心层？」→【自述】「把前者当作后者的入口，是我这段工作最关键的偏航」（L16332） | 核心靶重固定为 M/S/Q/FormalDone/OriginDone/P/Bridge；#0014 新建 `ZFC-META-SUBTHEORY-ADEQUACY-SOP` | `dev-01/THREAD.md` 层 5；`GUI查阅索引.md` §1 #6；`八线分叉后复盘.md` §9.4 |
| V-2 | dev-08 #0093（导出行；原话在 `dev-notes/0109` 第 58 轮） | dev-08 L3 自身＋跨线否决 dev-02 L7 的靶心 | 【原话】「我一直说的都是 bare ZFC 理论精度不够。」 | 【判断】八线复盘 §3：dev-02 的 `ZFCOneUse` 与该句同构；dev-02 THREAD 将此列为「本线最重要的一次下游否定性接走」 | `dev-08/THREAD.md` 层 L3；`dev-02/THREAD.md` §3；`八线分叉后复盘.md` §3【判断】 |
| V-3 | dev-02 #0004／#0005 | dev-02 L6/L5 自身 | 【原话】「所以，数学幻觉P到底是什么？你知道了吗？」（L13432）；「你是否可以继续工作，直至全部完成？」（L13568） | 把 P 从泛称钉成定义；`TaskEquiv` 从唯一同构降为「充分的反类比控制」（L13577） | `dev-02/THREAD.md` §6/§7 |
| V-4 | dev-06 #0004（导出行 14703） | dev-06 L7 自身 | 【原话】「你工作的时候，不维护认知文档，你干着干着就忘了啊，为什么认知闭包没有达到这个效果呢？」→判词 `EXECUTION_DEVIATION / COGNITIVE_WRITEBACK_OMISSION`（L14763） | 本线唯一一次由治理失败直接改变研究下一动作；靶点优先级从 MPIM 追来源改为 P-first | `dev-06/THREAD.md` L7；`GUI查阅索引.md` §1 #21 |
| V-5 | dev-06 #0006（导出行 14858） | dev-06 L6 自身 | 【原话】「你是要跟它做一样的事吗？那何必呢？」 | 否决再造同义方案；改为复用 `a9c27282` 并只补闭包/Goal 绑定 | `dev-06/THREAD.md` L6 |
| V-6 | dev-07 #0005（导出行 14801） | dev-07 L4 的 ω 自由生长线 | 【原话】「你还在处理A和B的事情吗？你知道这里的A是什么？B是什么吗？」→【自述】「我不能把 `ω` 这条线自己发展成一个『无穷总体』的独立故事」（L14806） | ω 当场降级为 `P_CANDIDATE_NOT_YET_A_B_BRIDGE`（L14816） | `dev-07/THREAD.md` L3；`GUI查阅索引.md` §2（只在 dev-07 分支） |
| V-7 | dev-03 #0008＋dev-08 #0080（同一句两处） | dev-03 L2 自身 | 【原话】「我是让你沿着我的思路，把该做的分析、证明、机器证明工作都做了，你现在是在做什么？」 | 停止同类来源扩张，改做「可证伪逻辑命题→反例结构→机器证明核心」 | `dev-03/THREAD.md` L2；`八线分叉后复盘.md` §8 #80 |
| V-8 | dev-09 #0008（导出行 16989） | dev-09 L2 自身 | 【原话】「为什么你没有全部做完再停下？」→【自述】「这不是数学上的谨慎，而是我把研究程序做成了审批程序。」（17000） | 「每次只推进一个最小判别单元」从总停机条件降为验证粒度；同轮连推 C-368 与三判词 | `dev-09/THREAD.md` L2；`GUI查阅索引.md` §1 #21 |
| V-9 | dev-08 #0081／#0083（主干交叉评审） | dev-03 L3 的同 Q 异判读法 | 【自述】QUniform 只是「同一输入不能有两个输出」；O3–O5 的 `false` 被当成「未观察到」 | 把「同 Q 异判悖论」降为「同 Q 异判检验」（与 CG-005 的 A1 一致） | `dev-03/THREAD.md` L3；`dev-08/THREAD.md` 层 L1；`八线分叉后复盘.md` §8 #81、#83 |
| V-10 | dev-06 #0009（导出行 15071） | dev-06 L4 自身 | 【原话】「你去观察了并行 worktree，你是否可以确认，你自己的工作方向没有漂移？」→【自述】「我不能直接给『完全没有漂移』的结论。」（L15076） | 下一动作从扩大样本改为 `P_REAUDIT_REQUIRED` | `dev-06/THREAD.md` L4 |
| V-11 | dev-04 #0007（导出行 12715） | dev-04 L2 自身 | 【原话】「我们实际上已经处于ZFC问题查找工作的收尾阶段，也就是研究已经开始收敛了」→【自述】「**P 是放大镜；靶是 ZFC 的理论观察力**」（L12720/12752） | 从「给 P 起一个漂亮定义」转为 R1/R2/R3 门逐项验桥；终点以有界负结论收口 | `dev-04/THREAD.md` 「关键一次转向」 |

## 5. 边表 C：接走（下游吸收、复用与并入）

分三类：**C-a 下游接走**（GPT 各线 → CG-006 理解层／`dev` 实物）；**C-b 横向接走**（一条线显式复用或独立核验另一条线的产物）；
**C-c 版本化落点**（快照、推送、交接）。每条都给轮次锚与可核验落点。

### 5.1 C-a 下游接走

| # | 源节点（轮次锚） | 接走者 | 被接走的内容（判词逐字） | 落点（可核验） |
|---|---|---|---|---|
| C-a1 | dev-01 L3（round 0019；导出行 16846） | CG-006 → `dev` | 【自述】`CORE_ADEQUACY_FAILURE_WITH_SCOPE`＋C-369/C-370/C-371 三台机器控制 | `HoTT/CLAIM_EVIDENCE_MATRIX.md:1895-1909`（`4a3535d9`，本机重放逐字节一致）；终局报告 §3 四项义务对照表、§7 反控制（`dev-01/THREAD.md`「本线的沉淀」1；`Targets与Profile.md` Ⅱ-3） |
| C-a2 | dev-01 L5（round 0013） | CG-006 终局报告 | 「侧移」自省 | `docs/ZFC时间维度观察力不完备-哥德尔式Q终局报告-20261008.md` §6「这一次不是侧移」（`八线分叉后复盘.md` §9.4） |
| C-a3 | dev-09 L2（round 0008；导出行 17212-17215） | CG-006 Ⅴa／Ⅴb | 【自述】`BARE_ZFC_COMPLETION_INTERFACE_FORMAL_TARGET_UNDERDETERMINED_WITH_SCOPE`、`T_META_SAME_TASK_BRIDGE_UNPAID_WITH_SCOPE`、`T_ZFC_CURRENT_INTERFACE_REJECTED_WITH_SCOPE`＋C-367/C-368 | `GUI查阅索引.md` #5/#7/#8/#9；`Targets与Profile.md` Ⅴa-1/Ⅴb-3（`八线分叉后复盘.md` §9.1 并列为「最接近突破的两处」之一） |
| C-a4 | dev-09 L1（round 0003；导出行 15906） | CG-006 Ⅴb-5 | 【原话】想法 T（「何止可以和哥德尔神似，我们简直可以和哥德尔『神交』！」） | `sources/prompts/Codex-理论精度与哥德尔式自反两轮用户原文-20261004.md:15`；`GUI查阅索引.md` §2；`Targets与Profile.md` Ⅴb-5 ◐ |
| C-a5 | dev-02 L6（round 0004）＋dev-04 L2（round 0004）＋dev-08 L2（#0091） | CG-006 Ⅲ-2／G-3 | P 的语义定义（强 P／无桥完成代换／P₀/P₁）三者并指 `Done_formal → Done_origin` | `GUI查阅索引.md` #10；`Targets与Profile.md` Ⅲ-2 ✅（两侧各自定义）；终局报告 §11「P 的两个侧面」 |
| C-a6 | dev-03 L1/L3（round 0005、0010） | CG-006 Ⅲ-1／Ⅱ-1 | O1–O5 拆法与「同 Q 异判」 | `GUI查阅索引.md` #11；`Targets与Profile.md` Ⅲ-1 ✅、Ⅲ-3 ◐；`八线分叉后复盘.md` §4【可吸收】 |
| C-a7 | dev-03 L5（round 0019） | CG-006 Ⅲ-5／Ⅱ-2 | UOU《Real Analysis》来源卡（`ACTUAL_P_CANDIDATE_CONFIRMED_WITH_SCOPE`）；SEP 反控制 | `GUI查阅索引.md` #14；`Targets与Profile.md` Ⅲ-5 ◐（来源层） |
| C-a8 | dev-06 L3（round 0010；导出行 15302） | CG-006 Ⅳ-2 | H0 process-anchor 五关键部分（复盘泛化为七字段） | `Targets与Profile.md:304`（Ⅳ-2）「正好是 dev-06 #10 自我修正所要求的那种过程锚」；`八线分叉后复盘.md` §1【可吸收】 |
| C-a9 | dev-07 L3/L2（round 0005、0006） | CG-006 Ⅳ-3 | A/B 精确定义＋`AProjection+BProjection+SameQBridge` 三项硬门 | `GUI查阅索引.md` #16；`Targets与Profile.md:305`（Ⅳ-3，状态 ◐）；`八线分叉后复盘.md` §25（列为对 CG-006 最有用的东西） |
| C-a10 | dev-08 L6（#0121–#0122） | CG-005 直接吸收 | T 框架（T-OBS/T-DIAG/T-Meta/T-ZFC） | `八线分叉后复盘.md` §9.3「T 的框架」；`Targets与Profile.md` Ⅴb-5 |
| C-a11 | dev-08 L5（#0119）＋dev-09 L2 | CG-006 S2/S3/S4 | `set.mm` 47,917 个 `$p` 全库 replay 与「被拒为父完成接口」 | `GUI查阅索引.md` #5；`dev:HoTT/verification/runs/20261004-SOURCE-REPLAY-SETMM-OBJECT-CODING-001/` |
| C-a12 | dev-08 L4（#0097–#0111） | CG-006 Ⅳ-4 判据 | 「M1 未付、forcing-ticks 受阻」成为判定「走 Z0 路线不需要 H0Map」的依据 | `Targets与Profile.md:306`（Ⅳ-4 ⊘／○＋【判断】） |
| C-a13 | dev-03 L6／dev-04 L3 形式包族 | CG-006 S7 合并候选 | `zfc-observation-boundary` 包（CommunityObservationPolicy、CompletionSubstitutionProfile、MetaSubtheoryAudit、CompletionPromotionTension 及正负控制） | `八线分叉后复盘.md` §9.3.7（**需先重新编号**——撞号区，见 CROSS-FEED §2.1） |
| C-a14 | dev-02 L7/L3（C-360/C-361） | CG-005 重放 | C-360（截断完成不推原 universe 有限 halt）、C-361（几何级数极限不等于有限阶段到达） | `八线分叉后复盘.md` §3【实物】「C-360、C-361 在 CG-005 中重放通过」 |
| C-a15 | dev-04 L4（round 0009；导出行 13268-13271） | CG-006 G-8 | B→P 回溯四定理（`zfc1_nonbase_B_backtracks_to_admitted_P` 等） | `Targets与Profile.md` G-8 ✅（魔鬼交易定理即反证法） |

### 5.2 C-b 横向接走（线↔线）

| # | 源节点（轮次锚） | 接走者 | 内容 | 证据 |
|---|---|---|---|---|
| C-b1 | dev-07 L5（dev-07/0003；导出 L14734，`a9c27282`） | dev-06 L6（dev-06/0005；导出 L14846） | dev-06 复用 dev-07 原始创建的 `H0-Z0-PATTERN-FIRST-CONVERGENCE-SOP`，不另造第二套 | `dev-06/THREAD.md` L6；`assets-ledger.md:587` A-0543、`notes/dev-07.md:4`「dev-06 所复用方案 a9c27282 的出处」 |
| C-b2 | dev-02 L3/L7（C-359~C-365，origin/dev-02） | dev-04 L3（dev-04/0008；导出行 12996-13116） | dev-04 冻结并独立重跑 `codex/zfc-q-policy-formalization@ea6c338f` 的七包（A-0483 清单；A-0480=C-365 独立重验版） | `dev-04/THREAD.md` L3；`assets-ledger.md` A-0480/A-0483 |
| C-b3 | dev-09 L1（T-PRECISION-DIAGONAL-SOP） | dev-08 L6（#0121–#0122） | 主干采纳 dev-09 带回的上位方案为 F-052，明确「不新建第二份同义闭包」 | `dev-08/THREAD.md` 层 L6；`八线分叉后复盘.md` §8 #121–#122 |
| C-b4 | dev-03 L3（dev-03 的回答） | dev-08 L1（#0081／#0083） | 研究发起人把 dev-03 的回答贴进主干交叉评审；主干认可 IEP 是真实消费者并收紧 QUniform 读法 | `八线分叉后复盘.md` §8 #81、#83 |
| C-b5 | dev-08 L1（#0112 哥德尔原话） | dev-01／dev-09（`dev-notes/0109`） | 该【原话】只以 `dev-notes/0109` 形式存在于 origin/dev-01、dev-08、dev-09 三分支，`dev` 上没有；dev-01 导出内 0 次命中 | `GUI查阅索引.md` §2；`dev-01/THREAD.md` 分叉点节（R9 缺口） |

### 5.3 C-c 版本化落点（快照／推送／交接）

| # | 源节点（轮次锚） | 落点 | 内容 | 证据 |
|---|---|---|---|---|
| C-c1 | dev-01 L9（0007–0008）、L1（0021） | `origin/dev-01` | `ca1259fe` 快照 → `cd9e34b2` 终态；复盘 §0 另记 fetch 时 `f10899cb` | `dev-01/THREAD.md` 层 9/层 1；`八线分叉后复盘.md` §0（两时点快照，不矛盾） |
| C-c2 | dev-02 L1（0010–0013） | `origin/dev-02`=`4005fa80` | 编号纪律＋`CANDIDATE_NOT_CURRENT / INTEGRATION_REQUIRED`＋dev-notes 全量归档推送 | `dev-02/THREAD.md` §2；`八线分叉后复盘.md` §0 |
| C-c3 | dev-03 L6（0022–0026） | `origin/dev-03`=`854a6aba` | 整树快照（354 staged、160,438 additions） | `dev-03/THREAD.md` L6；`八线分叉后复盘.md` §0 |
| C-c4 | dev-04 L5（0012–0015） | `origin/dev-04`=`69aa5aab`（复盘另记 `f97bbcb4`） | 16 个连续提交＋非强制显式 refspec 推送 | `dev-04/THREAD.md` L5；`八线分叉后复盘.md` §0 |
| C-c5 | dev-06 L1（0013） | `origin/dev-06`=`86ad33c4`（复盘 §0 记 fetch 时 af0d9c5c） | 首次创建并推送；不触碰 canonical `dev` | `dev-06/THREAD.md` L1；`八线分叉后复盘.md` §0 |
| C-c6 | dev-07 L1（0007–0008） | `origin/dev-07`=`49624878`→`9dd0b61b`（复盘记 `a753f9bc`） | 「全部带上，全部推送」覆盖默认归档规则 | `dev-07/THREAD.md` L1；`八线分叉后复盘.md` §0 |
| C-c7 | dev-08 L8（0127） | `origin/dev-08`=`7b1f7f60` | 快照提交推送 | `dev-08/THREAD.md` 层 L8；`八线分叉后复盘.md` §8 #127 |
| C-c8 | dev-09 L3（0009）、L8（0015–0016） | `origin/dev-09`=`1c34aaee`→`ac6391b6` | 快照 → 双亲 merge（24 本地 vs 35 远端分叉、九个语义冲突逐个保留） | `dev-09/THREAD.md` L3/L8；`八线分叉后复盘.md` §0 |
| C-c9 | dev-01 L10/L7、dev-09 L2 等 | canonical `dev` | `dfed5e7f`/`3bc07468`/`797571ce`（F-050、T-PRECISION 方案）、`619e1892`（C-367）、`0131bc6b`（C-368 等） | `八线分叉后复盘.md` §0；`dev-09/THREAD.md` L2 |

## 6. 跨线闭合性核对（G5 视角）

按方案 §5 G5：任一被标 `carried` 的发现都应能在 CG 理解层或 `dev` 实物找到落点。本节的核对结果：

| 核对项 | 结果 |
|---|---|
| 八线 `DISCOVERIES.tsv` 共 727 行，其中 `carried` 644 行 | 644 行的落点分三类：CG-006 理解层引用（`Targets与Profile.md`／`GUI查阅索引.md`／`八线分叉后复盘.md`／终局报告）、另一条线的显式复用或独立核验、`dev` 或 `origin/dev-0X` 的 `path@ref` 实物 |
| 撞号区（C-359~C-365／C-369／C-370 起）的 carried 行 | 按方案 §5 G5 预登记降级 `parked` 并登记，不计 agent 失败；详见 `CROSS-FEED.md` §2.1 |
| 未找到落点的 carried 行 | 0 条被判「有落点」；落点只到轮次级线头的资产在 `CROSS-FEED.md` 的理由列如实写明「资产级单独落点未见」 |
| 传播图闭环 | 无孤立节点：八线每层都至少有一条入边（分叉供给）或一条出边（版本化落点 C-c）|

## 7. 两说并陈（交审计员处置，本 agent 不裁决）

| # | 议题 | 一说 | 另一说 |
|---|---|---|---|
| R-1 | 分叉树父子关系 | `audit/GUI-SYNTH-REDO/qa/_tree.json`（机器导出树）：dev-02 自 dev-08 #86、dev-01 自 dev-08 #111、dev-04 自 dev-03 #13、dev-07 自 dev-06 #3 | GLM 战役 D2 全程叙事写「dev-02 分支自 dev-01」；`八线分叉后复盘.md` §9.6【判断】已判其「树的父子关系也有出入……不宜当底稿」。本图采用机器树 |
| R-2 | 各线远端分支 HEAD | 各线 GUI 导出自述落点（dev-01 `cd9e34b2`／dev-04 `69aa5aab`／dev-07 `9dd0b61b`） | `八线分叉后复盘.md` §0（2026-10-08 fetch）：dev-01 `f10899cb`／dev-04 `f97bbcb4`／dev-07 `a753f9bc`。各线 THREAD 已自证为不同时点快照、不矛盾；本图两说并陈 |
| R-3 | H0 过程锚字段数 | dev-06 导出自述五关键部分（`dev-06/THREAD.md` L3，导出行 15302） | `八线分叉后复盘.md` §36 与 `Targets与Profile.md:304` 用「七字段」表述。本图在 C-a8 两说并列 |
| R-4 | 轮数口径 | QA 块坐标（八线自有 239 轮），来自 `scope.json` 每线 `docs[]` | 裁决 #3 口径 124 轮（定义在 raw rollout，冻结输入层内不可重算）。R4/PRE-4 裁定：逐轮身份一律用块坐标，裁决 #3 只作并列引用 |
| R-5 | 哥德尔原话的语料归属 | 【原话】在 GUI 导出内存在（dev-08 导出行 15557） | 同一句的实物只在 `dev-notes/0109`（origin/dev-01、dev-08、dev-09），`dev` 上没有；dev-01 导出内检索 0 次命中（分叉 cutoff 在 L15556）|

## 8. 机验下界（本 agent 实跑）

- 分叉父子逐条比对 `audit/GUI-SYNTH-REDO/qa/_tree.json` 的 `forks` 段与 `wflow-lineage/scope.json` 每线 `fork` 段：8/8 一致
  （dev-03 parent_doc=75、dev-02=86、dev-06=97、dev-01=111、dev-09=113、dev-04 parent_branch=dev-03 parent_doc=13、
  dev-07 parent_branch=dev-06 parent_doc=3、dev-08 parent_branch=archive-01a0fb73 parent_doc=10）。
- 每条边引用的 CG-006 行号在本机用 `grep -n` 回读确认存在（如 `Targets与Profile.md:304`、`:305`、`GUI查阅索引.md:34`、`八线分叉后复盘.md` §25/§36）。
- 边表中的导出行号（如 L13432、L14703、L14801、L16284、L16989、L15302、L15906）均来自各线 `THREAD.md` 已登记的 scope 锚点，
  本 agent 未重新打开 GUI 导出逐行复核（R1 的锚点权威在 scope.json）。

