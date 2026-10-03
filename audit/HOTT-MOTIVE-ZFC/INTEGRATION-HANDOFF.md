# HOTT-MOTIVE-ZFC 候选集成交接单

> **身份：** CANDIDATE_NOT_CURRENT / CROSS_WORKTREE_INTEGRATION_RELAY / HUMAN_EDITED。
>
> **目的：** 让 /Volumes/D/HoTT_AI_HANDOFF_20260911 主 worktree 上的集成者或 Codex 会话，能在不依赖本对话、不中断其现有工作树的前提下，定位、审阅并按需集成 HoTT 创建动机反投影 ZFC 文献调查项目。
>
> **不是：** 主分支当前真值、自动 merge 授权、对 ZFC 的数学结论，或另一个 HOTT-MOTIVE-ZFC 内容索引。

## 1. 已冻结的候选快照

| 字段 | 值 |
|---|---|
| 候选分支 | codex/hott-motive-zfc-literature |
| 候选内容 payload tip（本交接单除外） | c606514b research: complete Maddy foundation control screen |
| 已闭合来源调查快照 | 7e1a111af545f5c458d36b59e16c248fca1c077a |
| 分叉共同基线 | 6341e337b578e77149444a7b4ca243a109121840 |
| 目标分支（观察时） | refs/heads/dev = 0ab997b17102119582ed7b542d6f7aa65fe6302b |
| 主 worktree（观察时） | /Volumes/D/HoTT_AI_HANDOFF_20260911；其工作区有 322 条状态记录；不得在该 checkout 直接集成。 |
| 内容规模 | 772e0fca^..7e1a111a 含 245 条受影响路径、227 个新增路径、约 12.52 MiB 新增 blob；其中只有一个新增 blob 超过 1 MiB。322c6e2f 另增加文献地图协议、初始检索记录和质量审计。 |

上述 target OID 和工作区状态只是本交接单写入时的现场快照。集成开始前必须重新读取 target ref、worktree list、完整 index 和 dirty 状态；任何变化都会使旧 review 失效。

## 2. 集成范围：选择提交，不 merge 整条候选分支

本候选分支的祖先中混有一份不属于该调查项目的 worktree snapshot。因此集成者不得对候选分支做整支 merge，也不得以“所有 dev..candidate 的提交”作为选取范围。

应按下列两个集合审阅：

1. **路线种子：** 913a1a18 research: map HoTT motivations to ZFC candidate seeds。它建立 R_i → Z_i → Q_i 以及 H0→Z0→Q0 的路线 owner。
2. **SOP 与调查成果：** 772e0fca^..7e1a111a，共 23 个逻辑提交，从 SOP 整备到九个冻结来源 run、十一份预检、P 字段矩阵、防重复恢复规则和两份用户可见归档。
3. **文献地图质量升级：** 322c6e2f research: start HOTT motive literature map。它新增 SOP 2.0 的文献地图阶段、地图质量审计、OpenAlex／Crossref／zbMATH／arXiv／IAS／citation 初始检索记录；它不产生新的 ZFC Q。
4. **总语料工程定义：** b58efeb7 feat: define ZFC Q corpus map SOP。它定义 ZFC-Q-CORPUS-MAP-SOP，作为 HOTT-MOTIVE 支线之外的总 acquisition、PDF核验、MinerU、书目／引文地图和Q lead routing合同。
5. **首个总语料 batch：** b72c94df research: seed ZFC Q corpus and visual source audit。它创建 ZQCM-001，记录十个work family、九个已核验work family、W-005期刊版的13页原件级视觉阅读、W-010的关键比较控制页、W-005 backward citation 与W-006 chapter map。它同时留下远程MinerU的两条实际失败收据；没有把原件视觉阅读称为MinerU成功，也没有形成ZFC Q。该提交新增原始PDF与审计页图，`.gitattributes`因而将PDF声明为byte-preserved binary。
6. **ZFC identity／formation seeds：** 4638f3f6 research: map ZFC identity and formation source seeds。它新增Klev的直接比较章节及关键页视觉证据，登记`EXTENSIONALITY_SITE_SEED`，并把Klev 2024 的stage／purely-iterative set论文登记为未取得全文的高优先级seed。它明确不把任一source seed升级为ZFC Q。
7. **形成一手控制与研究型 profile：** 53a578f4 research: add formation source controls and governed corpus profile。它以经DOI、首页、页数和hash核验的Aczel 1978原件补入CZF、Power Set、type-of-sets formation、recursion和presentation的primary control，并保存12页150dpi、7页300dpi视觉证据及两条remote MinerU失败收据；同时登记Linnebo 2013的官方摘要级potential／actual hierarchy seed，并把ZQCM-001明确为只投影既有owner的`RESEARCH_PROFILE_GOVERNED`。它不产生ZFC Q或数学结论。
8. **Klev identity 全文筛读：** 6f247692 research: complete Klev identity source screen。它补足W-011余下17页二值视觉证据，以全文确认Klev 2019是概念／逻辑语法比较，完整原文没有ordinary ZFC actual consumer；它把`EXTENSIONALITY_SITE_SEED`保留为来源精度增益和严格的`NOT_Q`。d7380ada同步修正F-046的当前筛读状态。
9. **Altenkirch 全文筛读：** ab51edd8 research: complete Altenkirch source screen。它补足W-009余下26页150dpi和6页300dpi证据；全文确认其universe、choice、internal `Set`／`extSet`、HIT与quotient都是类型论内部构造或比较，未交付ZFC actual consumer。它保持`NOT_QUALIFIED_R_ONLY`，不产生ZFC Q。
10. **Maddy foundation-control 全文筛读：** c606514b research: complete Maddy foundation control screen。它补足W-010余下15页150dpi和4页300dpi证据；全文将set-theoretic foundations、category theory和univalent foundations的不同任务、历史known-paradox context、来源归属和proof-checking分开，形成完整的same-task／scope control，不产生ZFC Q。

可选的归档增量 67cce86a 只追加了当前 worktree 集成交接对话记录。是否移植该一项取决于目标 dev 的 dev-notes 归档策略；它不影响研究内容、SOP 或文献地图。

明确**排除**：

    674df726 Codex worktree snapshot: archive-cleanup

它是当时 worktree 的广泛快照，不是 HOTT-MOTIVE-ZFC 的可选择性集成单元。

## 3. 主 worktree AI 的最小读取顺序

主 worktree 的 AI 要理解这批工作，只需要按下面顺序从候选分支读取，不要尝试从 Git log 反推结论：

1. 本文件；
2. [项目档案根](README.md)；
3. [ZFC Q corpus archive](../ZFC-Q-CORPUS-MAP/README.md)；
4. [ZQCM-001 findings](../ZFC-Q-CORPUS-MAP/ZQCM-001-open-foundations-and-delivery-seeds/FINDINGS.md)、[W-005 source notes](../ZFC-Q-CORPUS-MAP/ZQCM-001-open-foundations-and-delivery-seeds/SOURCE-NOTES-W005.md)、[W-010 control notes](../ZFC-Q-CORPUS-MAP/ZQCM-001-open-foundations-and-delivery-seeds/SOURCE-NOTES-W010.md)、[W-011 precision notes](../ZFC-Q-CORPUS-MAP/ZQCM-001-open-foundations-and-delivery-seeds/SOURCE-NOTES-W011.md)、[W-012 iterative-set seed](../ZFC-Q-CORPUS-MAP/ZQCM-001-open-foundations-and-delivery-seeds/SEED-W012-ITERATIVE-SET.md)、[W-013 Aczel source notes](../ZFC-Q-CORPUS-MAP/ZQCM-001-open-foundations-and-delivery-seeds/SOURCE-NOTES-W013.md)与[W-014 potential-hierarchy seed](../ZFC-Q-CORPUS-MAP/ZQCM-001-open-foundations-and-delivery-seeds/SEED-W014-POTENTIAL-HIERARCHY.md)；
5. [P 字段来源矩阵](P-ANTECEDENT-EVIDENCE-SYNTHESIS.md)；
6. [第一阶段来源综合](PHASE-1-SOURCE-SYNTHESIS.md)；
7. [HOTT-MOTIVE-ZFC-SOP](../../dev-docs/HoTT创建动机反投影ZFC文献调查SOP.md)；
8. [路线种子 009](../../dev-docs/菲尔兹奖后续理论级目标路线图/009%20-%20HoTT创建动机反投影ZFC候选路线.md)；
9. 每个 run 的 MANIFEST.md、FINDINGS.md 和必要的 source card。

由此能够恢复的当前研究结论是：九个冻结来源分母和十一份预检均已存档；ZQCM-001已积累完整筛读后仍为R-source的W-005/W-009、完整筛读后仍为`NOT_Q`的`EXTENSIONALITY_SITE_SEED`、完整foundation-job control的W-010、Aczel的CZF／Power Set／formation control，以及stage／potential formation全文未得seed；当前是 CURRENT_SOURCE_ADMISSION_FRONTIER；没有 ZFC_Q、没有 H0→Z0 正向传输，也没有数学证明结论。下一轮只允许由新的、能改变 P1/P2/P5/P6、同一任务或 T0–T5 前沿的来源触发。

## 4. 推荐的集成程序

1. **保全主 worktree。** 主 worktree 的实际维护者先完成或保留其自身 dirty/index 工作；不得由本候选的集成者在该树中执行 reset、restore、clean、stash、pull 或切分支。
2. **冻结目标。** 从共享 refs 读取当前 refs/heads/dev OID 和 git worktree list --porcelain。若目标、AGENTS、Feature、rulings 或当前 owner 已变化，重新审阅本交接单。
3. **建立干净的集成 worktree。** 从冻结的 dev 建一个短期 integration branch/worktree；它是审阅与冲突解决场所，不是主 worktree 的替代品。
4. **选择性移植。** 先 cherry-pick 913a1a18，跳过 674df726，再 cherry-pick 772e0fca^..7e1a111a、322c6e2f、b58efeb7、b72c94df、4638f3f6、53a578f4、6f247692、d7380ada、ab51edd8 和 c606514b。每个冲突都按当前目标分支的语义裁决，不能整仓使用 ours 或 theirs。
5. **重点审阅重叠 owner。** 当前三方 merge 预演已显示实际文本冲突至少涉及：

    .codex/skills/SKILL_ROLES.json
    feature-list.md
    rulings.md

   另有语义重叠但未必会产生 Git 冲突的 owner：

    AGENTS.md
    MEMORY/001 - 当前执行队列.md
    dev-docs/README.md
    dev-docs/刀具系统理念.md
    dev-docs/模式P刀具持续锻造SOP/001 - 操作合同、检查维度与幂集防御账本.md

   集成者必须在 dev 的当前内容中原位吸收已接受的意义，不能把候选 branch 的 current-state 行整块覆盖回去。
6. **验证集成候选。** 至少执行 git diff --check、python3 -B scripts/audit/verify_governance_shards.py、python3 -B scripts/audit/verify_pattern_p_tool_history_sources.py --root .，并复核 archive manifest、链接和候选范围。结果应标明“来源调查档案已集成”，不能提升为 ZFC 数学结论。
7. **再推进主分支。** 只有 clean integration worktree 已被审阅、主 worktree 自身的进行中工作已经处理，且具备对 dev 的集成授权时，才由唯一 CANONICAL_INTEGRATOR 把该集成 commit 进入 dev。是否 push、生成 main 发布投影或改变主 worktree，分别需要其独立步骤与授权。

## 5. 为什么只新增这一份交接单

Codex 官方资料建议把长时程工作的规格、状态和决策外化在 repository 中，并把 worktree 用于隔离运行和保持 diff 可审阅；Git 的 worktree 文档也说明 worktree 共享 refs/config，而不是独立的语义状态。因此本项目不需要为这次交接另建一套数据库、工作包平台或总索引。

现有 archive 已经拥有研究内容和来源证据；这份交接单只补上跨 worktree 必需的五项信息：候选 ref、精确 base/target、选择性提交范围、冲突风险和安全的集成顺序。它使主 worktree AI 可以通过 branch + Git + owner 文档复原工作，而不需访问本会话。

## 6. 复审与失效条件

本交接单在以下任一情形发生后须重新审阅：

- dev 的 OID、主 worktree 的 index/dirty 状态或当前 owner 改变；
- 候选分支被追加、rewritten 或 archive 来源再被修订；
- 集成者选择的提交范围不同于本文件第 2 节；
- 新来源改变 CURRENT_SOURCE_ADMISSION_FRONTIER；
- 用户要求合并到 main、推送或生成 release projection。

在这些条件未发生前，候选分支和本交接单是足以让主 worktree AI 开始审阅的最小闭包。
