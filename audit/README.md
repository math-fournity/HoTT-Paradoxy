# 审计资产入口

- [P-DAG-HOTT-DISCOVERY-004：长观察窗无泄漏 HoTT 发现结果（Terra / Max，2026-10-02）](20261002-P-DAG-HOTT-DISCOVERY-004-Terra-Max.md)：首次捕获 discovery trace，但候选落在 universe-index 元层问题；它促成 P1 的 `D-L5/native-task anchor`，不能算 HoTT replay pass。

- [P-DAG-HOTT-DISCOVERY-003：无泄漏 HoTT 一遍发现 NodeCard（2026-10-02）](20261002-P-DAG-HOTT-DISCOVERY-003-NODECARD.md)：90 秒没有终态输出，保留为 timing failure；H-004 是唯一改变观察窗与输出契约的后继重试。

- [P-DAG-HOTT-REPLAY-001：无答案泄漏 HoTT 校准 NodeCard（2026-10-02）](20261002-P-DAG-HOTT-REPLAY-001-NODECARD.md)：第一次 Book source packet 校准在输出可观察前超时；它留下冻结输入与终态边界，不能被读成 P 或 HoTT 的失败。

- [P-DAG-HOTT-REPLAY-002：修复输出捕获后的无泄漏 HoTT 校准结果（Terra / Max，2026-10-02）](20261002-P-DAG-HOTT-REPLAY-002-Terra-Max.md)：终态收据成功捕获，代理正确拒绝虚构 consumer；Master 据此发现 discovery 与 validation 被同一 gate 混淆，修订为 `P-DISCOVERY → source tracer → P-VALIDATION`。

- [P-DAG-SOURCE-005：Isabelle/ZF Cantor 来源卡的 Master 直接审读（2026-10-02）](20261002-P-DAG-SOURCE-005-Isabelle-ZF-Cantor-Master.md)：固定 Isabelle mirror commit 的 `PowI`／`PowD`／`cantor` 源码直接审读；证明任务提到 `Pow(A)` 不等于 source-defined same-`u` semantic consumer，也不提供 P2/P3 或 ZFC Q。

- [模式 P 刀具系统：起源—实作对照审计（2026-10-02）](20261002-模式P刀具系统起源—实作对照审计.md)：逐项回读罗素原初张力、P-first、Power Set 纠偏、一遍匹配、三把刀、案例、Terra/Max、MatchTrace 与动态 DAG 讨论；区分规格遗漏、执行偏差、runner/evidence failure 与原初理念是否被挑战，并释放 HoTT replay gate。

- [P-DAG-SOURCE-004：Isabelle/ZF Cantor 消费者的预封存 NodeCard（Terra / Max，2026-10-02）](20261002-P-DAG-SOURCE-004-NODECARD.md)：固定 `PowI`／`PowD`／`cantor` 来源包后，CLI 在模型输出前遭遇 `workspace routing discovery failed`；记录为 runner connection failure，不构成来源或 P1 判词。

- [P-DAG-SOURCE-003：Power Set 来源三节点的超时与收据纪律修订（Terra / Max，2026-10-02）](20261002-P-DAG-SOURCE-003-TIMEOUT-Terra-Max.md)：三张 `PRIMARY_WEB_SOURCE` 节点在四分钟观察窗内没有 terminal output 后被 Master 取消；没有 source claim，促成 prelaunch NodeCard、deadline 与 partial-output fail-closed 规则。

- [P-DAG-SOURCE-002 与 BATTLE-002：ZF/ZFC 语法、proof-layer 与 P3 层级分离（Terra / Max，2026-10-02）](20261002-P-DAG-SOURCE-002-与-BATTLE-002-Terra-Max.md)：Metamath `pwex` 作为 proof-system consumer 的层级边界、Isabelle/ZF 公式—满足—reentry P2 chain、同卡 P3 gap，以及由此新增的 P1 L2c/layer-integrity 门。

- [P-DAG-SOURCE-001：Power Set 的真实 consumer 来源节点与 P2/P3 接力（Terra / Max，2026-10-02）](20261002-P-DAG-SOURCE-001-Terra-Max.md)：网络来源节点找到了 Mathlib `ZFSet.powerset(prod x y) → funs x y` 的版本固定形式化 consumer card；P2 对该 card `NOT_APPLICABLE`、P3 `CONSTRUCTION_SEMANTICS_NOT_SUPPLIED`，因此不构成共同 Q。

- [P-DAG App Server 资格检查（2026-10-02）](20261002-P-DAG-AppServer-资格检查.md)：本机 `codex-cli 0.157.0` App Server schema 与共享 broker 的只读源码对照；schema 有 sandbox/approval 字段，但 broker 的 Codex adapter 尚未转发 sandbox，故动态 worker lane 保持 `APP_SERVER_PERMISSION_FORWARDING_NOT_QUALIFIED`。

- [P-DAG-BATTLE-001：动态 DAG 的 consumer-contract Battle（Terra / Max，2026-10-02）](20261002-P-DAG-BATTLE-001-Terra-Max.md)：两个 source-isolated 立场节点围绕 `∈` 是否构成 P1 consumer 产生明确字段冲突，独立 arbiter 以冻结 L2b/source card 给出 `RESOLVED_BY_SOURCE / SOURCE_CONSUMER_GAP`；验证的是 DAG 编排链，不是 ZFC 结论。

- [ZFC-COFORGE-005-P1：L0–L7 自我说明重跑（Terra / Max，2026-10-02）](20261002-ZFC-COFORGE-005-P1-L0-L7重跑-外部CLI-Terra-Max.md)：更新后的盲测比较幂集 membership 路线与 Foundation 邻近项，明确返回 `SOURCE_CONSUMER_GAP`；它把“关系符号”与拥有输入／输出／Done 的真实 consumer contract 分开。

- [ZFC-COFORGE-004：L7 obligation-mode 独立复核（Terra / Max，2026-10-02）](20261002-ZFC-COFORGE-004-L7复核-外部CLI-Terra-Max.md)：独立实例逐 E0–E7 审核 `a∈P(P(a))` 的完整匹配理由链；在最有利的 membership-consumer 读法下仍判 `ANSWERABLE_FALSE_BRANCH`，并明确该卡缺少 affirmative-only Done 的 source fact。

- [ZFC-COFORGE-003-P1：P1 MatchTrace + Q-friction 重选（Terra / Max，2026-10-02）](20261002-ZFC-COFORGE-003-P1-外部CLI-Terra-Max.md)：代理把 Power Set 位置细化至 `a∈P(P(a))`，完整交付 source→候选→归约→邻近项→反事实；主复核发现它是非平凡但可正常判假的 membership 查询，因而催生 L7/obligation mode，而非 ZFC Q。

- [P3-DELAY-001：实际 completion-process source card 外部状态机盲测（Terra / Max，2026-10-02）](20261002-P3-DELAY-001-外部CLI-Terra-Max.md)：真实 `Delay/now/later/never/askFrom/runFor` source 被正确识别为 P3 completion-process 正控制，不被误写为 admission cycle 或现实过程。

- [P2-DELAY-001：实际 completion-process source card 外部适用性盲测（Terra / Max，2026-10-02）](20261002-P2-DELAY-001-外部CLI-Terra-Max.md)：阶段 continuation 被正确区分于 formula-level reentry，P2 在真实 P3-positive source 上 fail closed。

- [P1-DELAY-001：实际 completion-process source card 外部定位盲测（Terra / Max，2026-10-02）](20261002-P1-DELAY-001-外部CLI-Terra-Max.md)：固定 universe questioning program、finite observer、`never` 与 bounded-height finite-now control 被正确分层，外部 bridge 保持 interpretation-only。

- [P2-CLIMBER-001：对象 provability／reflection source card 外部分类盲测（Terra / Max，2026-10-02）](20261002-P2-CLIMBER-001-外部CLI-Terra-Max.md)：真实 Formula/prov、Lean soundness 与 T₀→T₁ reflection step 被正确分类为 guarded upward rung，拒绝同层 reentry／fixed point／HoTT 外推。

- [P3-CFTT-001：实际 staged-operation card 外部构造语义盲测（Terra / Max，2026-10-02）](20261002-P3-CFTT-001-外部CLI-Terra-Max.md)：真实 staged code operation 与 P3 pending/admission lifecycle 被独立实例明确分离，避免把 code generation 误读为构造时序张力。

- [P2-CFTT-001：实际 staged-operation card 外部分类盲测（Terra / Max，2026-10-02）](20261002-P2-CFTT-001-外部CLI-Terra-Max.md)：真实 quote/splice/HOAS/LetRec operation 被识别为 staged code construction，但 generativity guard 阻断 formula-level P2 chain，避免把 staging 误报为自指灾难。

- [P3-ZFC-001：中性 ZFC-style theory card 外部构造语义盲测（Terra / Max，2026-10-02）](20261002-P3-ZFC-001-外部CLI-Terra-Max.md)：静态 Power Set／bounded separation card 不提供 P3 lifecycle；独立实例列出合法构造状态测试所需的 transition、guard、scheduler 和 oracle 证据。

- [P2-ZFC-001：中性 ZFC-style theory card 外部适用性盲测（Terra / Max，2026-10-02）](20261002-P2-ZFC-001-外部CLI-Terra-Max.md)：独立实例正确拒绝将 Power Set 或 bounded separation 误当无限制 Bind/Form/Bridge/Reenter，从而不生成 P2 residual。

- [P3-HOTT-001：中性 HoTT theory card 外部构造语义盲测（Terra / Max，2026-10-02）](20261002-P3-HOTT-001-外部CLI-Terra-Max.md)：独立实例正确拒绝将 Id/J/ua/HIT 静态规则读成 pending/admission 状态机，列出真实 P3 映射所需操作规则、实现和执行证据。

- [P2-HOTT-001：中性 HoTT theory card 外部适用性盲测（Terra / Max，2026-10-02）](20261002-P2-HOTT-001-外部CLI-Terra-Max.md)：独立实例在缺 binder、reification、bridge、reentry 的中性 HoTT 卡上正确 fail closed，不把 universe/Id/ua 术语误报为 P2 feedback。

- [P3-CIRCLE-001：外部 Codex CLI 原对象／repair 语义边界盲测（Terra / Max，2026-10-02）](20261002-P3-CIRCLE-001-外部CLI-Terra-Max.md)：在已有 origin package 和强／弱 Done、缺 repair transition 的条件下，独立实例正确输出 `CONSTRUCTION_SEMANTICS_NOT_SUPPLIED`，列出 P3 合法状态机的最小证据缺口。

- [P1-FORGE-001：外部 Codex CLI 前提／Done 分类盲测（Terra / Max，2026-10-02）](20261002-P1-FORGE-001-外部CLI-Terra-Max.md)：外部实例正确区分减半过程的有限阶段结果、阈值终步 control，以及圆环弱紧化与来源保持的强复原；两案均未被虚报为悖论结论。

- [P3-FORGE-001：外部 Codex CLI 状态／完成分类盲测（Terra / Max，2026-10-02）](20261002-P3-FORGE-001-外部CLI-Terra-Max.md)：独立 CLI 实例正确区分准入依赖环、有限阶段未完成和带终步的完成控制，并拒绝把它们升级为实际理论或全称不可完成结论。

- [P2-FORGE-001：外部 Codex CLI 分类盲测（Terra / Max，2026-10-02）](20261002-P2-FORGE-001-外部CLI-Terra-Max.md)：独立 scratch directory 的 read-only external CLI 实例按冻结预期区分无限制负极性、有界 guard 和正极性 sanity control；只验证 P2 fixture 分类能力。

- [P2：计算—逻辑翻译探针（Terra / Max，2026-10-02）](20261002-P2-计算逻辑翻译探针-Terra-Max.md)：把脱敏的形成、bridge、回代、极性和 guard 编译为 P2/v0 中间表示；区分有限规格冲突、上升准入过程、guard 阻断与未知，不能由任何固定点自动推出理论结论。

- [模式 P 的朴素集合论脱敏正控制：Terra / Max（2026-10-02）](20261002-模式P-朴素集合论脱敏正控制-Terra-Max.md)：不出现历史名称或著名公式的情况下，代理从无限制理解规则独立定位到自成员否定条件的形成／实例化位置。它验证脱敏定位能力，同时区分有限成员规格冲突与严格的对象准入未决／预支使用结构。

- [模式 P 的 HoTT 无泄漏盲重放：第一次负控制（2026-10-02）](20261002-模式P-HoTT无泄漏盲重放-Terra-Max.md)：fresh Terra/Max 请求代理没有复现既有 HoTT 主线，而是以外加 resizing/smallness 证书制造 W-type 自子树环。该输出被判 `MISSED_CORE_SITE / ARTIFICIAL_EXTENSION / TASK_SWITCH`，用于新增 `L3` 原生承诺门，而非作为 HoTT 候选。

- [模式 P 对 ZFC 的一遍匹配盲测：Terra / Max 子代理（2026-10-02）](20261002-模式P一遍匹配ZFC盲测-Terra-Max.md)：两个 prompt-bounded、只读的候选选择探针。第一次因缺少对象层入口门而误配 `Ord/V` 的元层总体；将 `L0–L2`（一等对象、直接形成／交付、同一对象交接）置于 P0–P6 之前后，第二次在未提供 Power Set 名称时选择幂集公理。该审计只支持选择层的有界行为判词；P3–P6、原典消费者、Q 与 UR 均未建立。

- [圆环作为“芝诺幽灵”的语义纠正与 Opus 意外收获审计（2026-10-01）](20261001-圆环作为芝诺幽灵的语义纠正与Opus意外收获审计.md)：研究发起人直接纠正 2026-09-27 总判定中的“芝诺幽灵”首先指其圆环悖论（去点圆 M、展开 N、反向逼近、此前已得 M），不是 A7 或 Q/UR；保留 A7、Q 的 A/UR 面和 B/罗素面为不同身份的候选/解释，不删除其证据。`main` 五语稿本轮不改，公开勘误另行处理。
- [Opus“两个幽灵”语义谱系与意外收获审计（2026-10-01，已更正的历史草稿）](20261001-Opus两个幽灵语义谱系与意外收获审计.md)：首次审计正确识别了“总判定不能自动回答 B 向两道门”，但错误地把“芝诺幽灵”的原始指称留作 A7/Q/并存的未定问题；直接用户纠正后已由上项取代，保留供来源谱系审计。

- [Codex 全局认知闭包持续生命周期升级（2026-09-23）](Codex全局认知闭包持续生命周期升级-20260923.md)：以本项目“构造过程”误读和四件套结构 PASS／语义消费 FAIL 为直接事故证据，先以v3.24补持续生命周期，再以v3.25补Task→Closure发现、复用/delta/owner组合和context/owner/Seed/Capsule/Audit持久化双轴；shared/runtime已以本地`governance-v3.25.0`闭合，fresh P7–P20仍未运行。
- [构造过程误读与认知消费审计（2026-09-23）](构造过程误读与认知消费审计-20260923.md)：核心／扩展全文复读、上一回答的构造过程→耗时误读、实际取材轨迹与纠正边界；不改变数学判词或当前研究队列。
- [P40–P47理论检视与原初问题对齐复核（2026-09-23）](P40-P47理论检视与原初问题对齐复核-20260923.md)：按更新后的持续认知闭包复核理论检视、Book形成规则与旧Russell模型，保留源文审读范围并降低P47候选优先级资格；不产生新数学证明。
- [四件套逐轮语义对齐治理修复（2026-09-23）](四件套逐轮语义对齐治理修复-20260923.md)：补上Session加载与当前turn语义消费之间的Gate、F-023、静态防退化及C01–C10；未来行为仍须实测。

`user-message-disposition.jsonl`、`ai-response-ledger.jsonl`、`tool-event-ledger.jsonl`、`webgpt-section-ledger.jsonl`、`gemini-thought-ledger.jsonl`、`gemini-execution-ledger.jsonl`、`work-product-ledger.jsonl` 和 `claim-evidence-ledger.jsonl` 是历史整合生成的 machine-managed ledger。`ledger-summary.json` 与 `verification-report.json` 给出分母和结构校验，但不认证数学真理或 AI 理解。`治理框架自反馈行为分析与未来优化依据-20260912.md` 拥有操作行为反思；`治理框架跨压缩连续性独立复审与精简升级方案-20260912.md` 是 current 分层加载方案；`核心认知generation-3与加载治理v3实施证据-20260912.md` 保存最近已封存版本，`核心认知generation-4与自反理论经济研究实施证据-20260912.md` 保存本轮 incremental core、C4、STATE/loader/C01–C10 和验证边界。旧框架对比与 generation-2 实施方案在 `history/governance-v2.1.0/`，只作历史证据。`方向追踪.md` 与 `全景视野.md` 是人读投影，不替代 ledger。

`数学结论机器证明交付门禁实施证据-20260912.md` 拥有 F-011 的 source/run/index 合同、C01–C10、正负向静态验证和历史兼容边界。它证明治理路由已实现，不证明任何数学命题，也不证明所有未来模型一定遵循。

`S086至S089-checkpoint收据缺失与治理修复设计-20260913.md` 保存四个历史 Session 的 canonical transaction/result 缺口、禁止追溯伪造边界与 runtime 3.2 前向修复设计。`agda-unimath-e6-source-scan-20260913.json` 由 `scripts/audit/scan_agda_unimath_e6.py` 确定性生成，严格区分源码审读、C-05 保存 run 的实际导入闭包和未进入该 run 的 `foundation.global-choice`。

`S090治理修复实施与验收证据-20260913.md` 与 `S090-governance-repair-verification-20260913.json` 保存真实 S090 canonical checkpoint、五个 record 的水合前后对照、0 query-first promotion、S086/S088 证据修正和 C01–C10；它们不认证模型理解或数学结论。

`governance-v3.2.0-release-evidence-20260913.md` 是本轮版本闭合入口；机器 registry 为 `HoTT/verification/PROOF_VERSION_CLOSURE.json`，verifier 为 `scripts/audit/verify_proof_version_closure.py`。Frozen proof rows 保持 run-time 状态文本，当前 Git 维度由追加 registry 解释。

`ERCF-1-2机器证明实施证据-20260912.md` 拥有 F-011 生效后的第一个真实数学 proof package：`MP-ERCF-001`/`C-59`–`C-66` 的形式命题、Lean 4.33.1 final indexed run、源码/输出哈希、重放结果和禁止外推。它证明一般 `Type` 值因子化骨架，不是 HoTT 原生证明或 HoTT 悖论；当前未提交，状态为 `MACHINE_PROVED_LOCAL_UNCOMMITTED`。

`ERCF-截断防御机器证明实施证据-20260912.md` 拥有首个 HoTT 原生信息经济判别：Agda 2.8.0/Cubical v0.9 的 squash-HIT `C-67`–`C-70`、官方 release asset/外置缓存哈希、五次预检谱系、final run/exact replay 和索引演进修复。结果是 `DEFENSE_WORKS`：命题截断允许 proposition consumer，并阻断逐点保真的 Bool witness extraction；不是 HoTT 悖论。

本轮新增的综合证据入口：

- `understanding-chapter-merge-manifest.json`：两个理解章节目录的逐文件 hash/diff/canonical/rollback 处置；nested 历史源不删除。
- `cross-source-reconciliation.json`：WebGPT 91 条 STATE record + LocalGPT 四类 ledger 共 22,226 条逐项 locator/register；原始 JSON 是按需审计底座，不是三件套每轮全文输入。
- `cross-source-reconciliation-report.md`：上述 register 的人读分母、映射模式和语义边界。
- `core-cognition-generation-3-transition-20260912.json`：generation-2 的 913 个旧 KC 到 generation-3 的逐项映射/退出理由，remainder=0；旧代由 `governance-v2.1.0` 恢复。
- `core-cognition-generation-4-transition-20260912.json`：generation-3 的 27 个 KC 到 generation-4 的逐项映射，27/27 为 `PRESERVED_EXACT`，remainder=0；新增 9 个单元来自 hash-pinned 当前用户原文。
- `fresh-three-way-verification-20260912.json`：新 Python 进程对 governance/research profile、三件套 EOF/hash、显式 task hydration 和 fail-closed 负向演练的收据；模型行为明确 NOT_RUN。
- `verify_projection_freshness.py`：只读核对 STATE revision、三件套 revision、core generation/hash、merge manifest、cross-source 输入 hash 和 fresh receipt。
- `core-cognition-generation-transition-20260912.json`：generation-1→2 的原文输入、前缀 identity 和回退 commit。

生成/核验入口：

```bash
rtk python3 scripts/audit/build_history_ledgers.py
rtk python3 scripts/audit/verify_history_ledgers.py
rtk python3 scripts/audit/build_core_cognition.py --transition-from-ref governance-v3.0.0  # 默认只检查当前 generation-4
rtk python3 scripts/audit/build_core_cognition.py --transition-from-ref governance-v3.0.0 --write
rtk python3 scripts/audit/verify_core_cognition.py
rtk python3 scripts/audit/verify_three_way_cognition.py
rtk python3 scripts/audit/verify_understanding_merge.py
rtk python3 scripts/audit/verify_cross_source_reconciliation.py
rtk python3 scripts/audit/verify_fresh_three_way.py
rtk python3 scripts/audit/verify_projection_freshness.py
rtk python3 scripts/audit/test_math_proof_delivery_governance.py
rtk python3 scripts/audit/verify_math_proof_delivery_governance.py
rtk python3 scripts/audit/verify_formal_proof_run.py --run-dir HoTT/verification/runs/20260912-MP-ERCF-001-02 --rerun
rtk python3 scripts/audit/verify_formal_proof_run.py --run-dir HoTT/verification/runs/20260912-MP-ERCF-TRUNC-001-01 --rerun
```

LocalGPT 的 raw trajectory 仅在 ignored `private-audit/`，公共 ledger 只保留完整可见回答或 bounded tool head + canonical locator；需要全文时回到 `/Users/aurolafly/codex/tools/session_trajectory.py` 和私有原件。
