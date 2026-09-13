# Semantic Overview 分支 Relay

> 资产身份：`CANDIDATE_NOT_CURRENT`
>
> 角色：`CONTRIBUTOR`
>
> integration_state：`NOT_SUBMITTED`
>
> 更新日期：2026-09-13

## 分支与目标身份

| 字段 | 值 |
|---|---|
| `repo_root` | `/Volumes/D/HoTT-semantic-overview` |
| `git_common_dir` | `/Volumes/D/HoTT_AI_HANDOFF_20260911/.git` |
| `branch` | `codex/semantic-overview` |
| `write_root` | `/Volumes/D/HoTT-semantic-overview` |
| `base_oid` | `a22f41ecf5c3becdd192383ff6cdbc846982813b` |
| `candidate_content_oid` | `214b15dcca4be0562c37aa536fe9eb5ace3a7365` |
| `canonical_target` | `/Volumes/D/HoTT_AI_HANDOFF_20260911`；branch `main` |
| `target_oid_observed` | `a22f41ecf5c3becdd192383ff6cdbc846982813b` |
| `machine_lane_oid_observed` | `1aa1a6e32c0f59459f79ebc76f74e8f2b5be97a5`；观察时该 worktree 另有未提交 M2–M6 候选工作，不属于本分支输入 |

用户在 2026-09-13 明确裁定：两个 AI 各自在自己的 Git worktree 工作，最终由用户从两者中指定一个执行集成。因此本分支不是 canonical integrator，不预先决定最终 target 的集成内容或顺序。

用户随后以 ruling §22 明确授权本分支执行 worktree evidence portability 修复。因此本分支在
F-016 的精确范围内生成了 revision 130/131 current-owner **candidate transactions**；它们只在
本分支成立，不自动占用 `main` 的 canonical revision。未来 integrator 若接受，必须按 target
当时 HEAD 重建/重编号冲突的 checkpoint，不能盲目移植候选序号。

## 独占路径与本轮治理例外

语义研究阶段的默认独占写入前缀是：

```text
semantic-overview/**
```

F-016 之前，以下 current-owner 集合保持只读。ruling §22 只为 worktree portability 修复授权了
这些 owner 的候选分支修改：AGENTS/Skill/PROTOCOL/LOAD_SET、Feature/ruling、source/merge
manifests 与 verifiers、相关 evidence locators、STATE/MEMORY/方向/全景/FRONTIER/LESSONS/RESUME
及 revision 130/131 session/checkpoint。数学 proof owners 仍未修改。

继续保持排除：

- `核心认知.md` 与其 manifest/curation；
- `HoTT/CLAIM_EVIDENCE_MATRIX.md`、proof closure/current proof index；
- `main`、共享 tags、共享 repo config 与另一个 contributor 的 worktree。

如果后续候选需要新增形式源码、测试或 run receipt，应先在本 relay 中分配不与其他 lane 重叠的前缀，再写入；不得仅因位于不同 worktree 就假定语义上无冲突。

## 当前目标与非目标

当前目标是从被审计的第一次“统观”路线继续独立研究，优先补 C11 v2 尚未独立落行的 B 方向：检查真实 HoTT/类型论消费者是否把命题存在或数学函数资格提升为有效程序或现实交付资格。

本分支的 runner 只固定单个语义判断所需的命令、哈希、退出码和原始收据；它们不是通用
自动统观系统。本分支不实现 machine-overview 的 schema、registry、grammar、索引、搜索器、
评估器或 verifier。

当前不做：

- 重复 machine-overview 已覆盖的 strict L1 与首个 L3 时间/运动切片；
- 把源码可定义、kernel 可检查、闭合项可归约、后端可执行和现实完成混成一个状态；
- 在没有真实自然使用链时追加同型小定理；
- 把本分支 revision 130/131 候选序号冒充 `main` canonical history；
- merge、tag、push 或向另一 AI 发送控制消息。

## 已完成候选

| 候选 | 状态 | 定位 |
|---|---|---|
| `SEM-B01`：两个真实截断消费者的 B 方向资格检查 | `KERNEL_CHECKED_AND_RUNTIME_OBSERVED_WITH_SCOPE / EXECUTION_GAP_WITHOUT_DELIVERY_PROMISE / E6_BOUNDED_NEGATIVE` | content commit `9d928ba629adf36796e64bb74059d58cefa8b456`；`semantic-overview/research/SEM-B01-truncation-consumer-audit.md` |
| `SEM-B02`：仅仅有限、决定数据与自然分支消费者 | `NATURAL_THEORY_BRANCH_CONSUMER_FOUND / EFFECTIVE_DELIVERY_LIFT_NOT_ESTABLISHED` | content commit `2de235a9c80fcad77e87135a7b2cda2c1bc755b4`；`semantic-overview/research/SEM-B02-finite-decision-consumer-audit.md` |
| `SEM-B03`：finite decision 的外部有效交付消费者搜索 | `WEB_SEARCH_WITH_SCOPE / E6B_CONSUMER_SOURCE_GAP` | content commit `c9a5ba13b67bcaaddd0eac5434e658f103284cbb`；`semantic-overview/research/SEM-B03-external-delivery-consumer-search.md` |
| `SEM-B04`：precategory reflection solver 的证明生成与拒绝边界 | `REFLECTION_SOLVER_GENERATES_CHECKED_PROOF_TERM / FALSE_AND_MALFORMED_GOALS_REJECTED / DECLARE_POSTULATE_NOT_USED / DEFENSE_WORKS_WITH_SCOPE` | content commit `d6e119a35993211413f16a3083ad4b9fd3e6c5bd`；`semantic-overview/research/SEM-B04-precategory-reflection-solver-audit.md` |
| `SEM-B05`：显式 reflection 公理引入与 safe-mode 边界 | `EXPLICIT_REFLECTION_POSTULATE_EXTENDS_THEORY_IN_DEFAULT_MODE / SAFE_MODE_REJECTS_THE_POSTULATE / SAFE_ORDINARY_REFLECTION_ACCEPTED / CONTROLLED_CAPABILITY_BOUNDARY_OBSERVED` | content commit `ac8c33a45d6084cb63acb883ce116d053227b513`；`semantic-overview/research/SEM-B05-reflection-postulate-safe-boundary.md` |
| `GOV-WORKTREE-PORTABILITY`：ignored evidence islands 迁移与治理修复 | `VERIFIED_WITH_SCOPE_ON_EXACT_COMMIT_FRESH_WORKTREE / CANDIDATE_NOT_INTEGRATED` | source `80da06e…`；static `d58dbfd…`；implementation checkpoint `802e4f8…`；acceptance `a8e948d…`；final checkpoint `214b15d…`；`audit/Git-worktree证据可移植性修复与验收-20260913.md` |

`SEM-B01` 的当前结果是：

- `apply-universal-property-trunc-Set'` 的选定下游链仍只输出命题截断中的居留；
- `map-universal-property-set-quotient-trunc-Prop` 的多项式求值链输出集合数据，但接口要求显式弱常值证明项；固定源码中的四个直接调用者都提交了对应同余/弱常值证明项；
- 多项式模块及 622 个实际加载模块通过 fresh kernel 重放；闭合命题等式正例通过，而同一等式的 `refl` 负例被 `[UnequalTerms]` 拒绝；
- JS 后端可生成代码，直接 Bool 正控实际输出 `TRUE`；强制消费截断项时在未实现的 `unit-trunc` 处显式失败，GHC 生成源码也为四个 postulate 保留运行错误；
- 已检查的自然源码没有执行/资源/现实交付承诺，因此该 Q3/Q4 断层未建立 `Q1/Q3 → Q4/Q7` 的自然资格升级；
- 历史扫描 JSON 的 repo-formal 文件清单已不是当前快照，外部 agda-unimath 部分仍与固定树一致。

`SEM-B02` 的当前结果是：

- `is-finite X = ∥ count X ∥` 可以在 kernel 中消去到命题性的 `has-decidable-equality X`；固定源码有 16 个文件使用该接口；
- exclusive-sum 与 orientation 调用链真实对 `A + ¬A` 分支匹配，因此理论内自然消费者已经找到；
- 显式 Bool 决定过程经修正后的 Scott-constructor FFI 实际输出 `FALSE`；有限性定理模块在普通及优化 JS 下都于 eager postulate 初始化处失败，没有产生错误决定值；
- 固定源码未承诺后端/资源/现实交付，同输入现实基线也未建立；本分支候选地把 E6 细分为理论消费 `E6a`、交付承诺 `E6b`、同任务失配 `E6c`，本轮状态为 `YES / NOT_FOUND / NOT_ESTABLISHED`。

`SEM-B03` 的当前结果是：公开 exact-name 搜索只定位到 agda-unimath 自己的生成文档，没有找到独立第三方 main、服务或插件；Agda 2.8 官方合同确认 postulate 没有定义，后端运行含义需要 `COMPILE` FFI，而固定 truncation postulate 没有这项支付。外部状态据此登记为 `E6B_CONSUMER_SOURCE_GAP`，不写成全网不存在。

`SEM-B04` 的当前结果是：固定 agda-unimath `solve-Precategory!` 宏以 soundness lemma、归一形
等式的 `refl` 和最终 `unify` 构造受 Agda 类型检查的证明项；结合律正例通过，任意平行态射
等式被 `[UnequalTerms]` 拒绝，非等式目标被 `[GenericDocError]` 拒绝。reflection TCM API
暴露 `declare-postulate`，但固定 solver 对它的直接调用数为零。该案例是“支付装置实际工作”
的正控制，不建立自然使用失配。

`SEM-B05` 的当前结果是：受控宏在默认模式下明确声明目标类型的新 postulate 后可使
`true ≡ false` 文件通过；同一源字节加 `--safe` 及源码级 safe 版本都被
`[SafeFlagPostulate]` 拒绝。另一个只提交 `refl` 的 safe reflection 宏通过，无公理直接证明
`true ≡ false` 则被 `[UnequalTerms]` 拒绝。结果说明默认成功来自显式理论扩展，safe 防线
针对该公理引入生效；它不构成 kernel 不一致，也不改变 B04 solver 零调用的事实。

## 验证与认知快照

- 四件套完整加载：`核心认知.md` generation 4 / 36 KC；方向 5 shards；全景 8 shards；essay 5 shards。
- governance snapshot：`fa264da418b1f4babb70295ffc014bba387d7cadea45da5ecbca15ca8b7811ea`，`SNAPSHOT_UNCHANGED`。
- research snapshot：`d2171122bcfda2eaac1daeca0af0734426a55ecd5d67f78065c9dbd74ac7fbdb`，`SNAPSHOT_UNCHANGED`。
- task hydration `A-COARSE-CONSUMER-SCAN-001`：`ed24a811b0d62c4fd484f7d34a70a631b2b3b9f7bc9138d871c20c7929f04880`，`SNAPSHOT_UNCHANGED`。
- 扫描器只读重跑：Cubical `1091/30/7`、agda-unimath `3056/50/30`、repo-formal `44/6/6`（文件数/命中/无 token 命中）。
- 候选报告提交前通过 `git diff --cached --check`；外部源码文件 SHA-256 逐文件复核。
- 第二阶段 run `20260913-SEM-B01-TRUNCATION-DELIVERY-001-01`：12/12 步符合冻结判据；18 项 source/toolchain manifest 复核无漂移；直接 Node 正控与截断失败均保留原始输出。
- run 具有拒绝覆盖行为；重复调用 exit 2，不会静默改写历史收据。
- `SEM-B02` run `20260913-SEM-B02-FINITE-DECISION-001-01`：13/13 步符合冻结判据；310 模块 fresh kernel；22 项 manifest 与 7 个保留生成物 hash 对账；普通/优化 JS 失败一致。
- B02 的承诺词汇扫描保留了 README `informative resources` 与 `effective quotient` 假阳性，语义分类没有用零命中粉饰结果。
- B03 记录 6 个公开查询、agda-unimath 官方生成页/GitHub 入口与 Agda 2.8 compiler/postulate/FFI 三份官方合同；未使用 authenticated GitHub code search，也未穷举 forks/dependents。
- B04 run `20260913-SEM-B04-PRECATEGORY-REFLECTION-001-01`：5/5 步符合冻结判据；固定 solver
  fresh 检查产生 273 行含 `Checking` 的导入诊断；14 项 source/toolchain manifest 无哈希漂移；
  一个正例与两个负例均保留原始 stdout/stderr。
- B04 runner 具有拒绝覆盖行为；重复调用 exit `2`。
- `A-THEORY-ECONOMY-LEDGER-001` task hydration snapshot
  `2c7e4ced3ccba1c1812363237cd9c8da087007057abfba4c7373f020fa51f985` 复核为
  `SNAPSHOT_UNCHANGED`。
- B05 run `20260913-SEM-B05-REFLECTION-POSTULATE-SAFE-001-01`：6/6 步符合冻结判据；
  默认/safe、普通 reflection 正控和无公理负控均保存原始输出；22 项 manifest 无哈希漂移。
- B05 unsafe/source-safe 规范化宏体相同，SHA-256 均为
  `1bb92b865b1bff62ad359d7d40e647a83bf2068aa7d86629af2286c13dc8b1b1`；runner 重算 B04
  solver 的 `declare-postulate` 直接调用数仍为零。
- B05 runner 具有拒绝覆盖行为；重复调用 exit `2`。
- revision 129 的历史可移植性基线为 4 PASS / 2 FAIL，已由 F-016 修复。exact `802e4f8…`
  fresh worktree（无顶层 workspace/dialogues/legacy LocalGPT path）中：42-file import、5 task
  plans（全部 `untracked_documents=[]`）与 6 canonical verifiers 全 PASS；4 个 byte/index/route/path
  负控全部按特定错误拒绝，恢复后 clean。
- final checkpoint `214b15d…` 又在第二个全新 detached worktree 正向复核：revision 131、
  36 KC、31 directions、111 outcomes、understanding 36/24、5 task plans、6/6 verifier 全 PASS；
  worktree clean 后删除。

## 失败、冲突与未知

- `CLOSED_FAILURE`：revision 129 的 A-HOTT task missing-workspace、understanding missing nested
  directory 与 fresh missing LocalGPT path 均已在 candidate 修复；它们保留为负基线，不再是
  revision 131 当前阻塞。
- `CONFLICT`：项目旧 current queue 把 S lane 放在主线；用户先把本分支定为 contributor，后以
  ruling §22 单独授权 F-016 current-owner candidate transactions。revision 130/131 只证明本分支
  自洽，不能与 target 后续同号事务并存；最终 integrator 必须在 target 原位重述被接受语义。
- `GOVERNANCE_GAP`：对 candidate branch 已 `CLOSED_WITH_SCOPE`。42-file transform snapshot 已
  tracked；8 个 workspace refs 改 existing tracked snapshot；LocalGPT current route 改已有同字节
  tracked file；manifest/verifier 检查 path/tracked/tree。`main` 集成与共享通用治理吸收仍开放。
- `UNKNOWN`：未被公开搜索索引的外部应用、fork/private consumer；同任务现实基线；其它具计算语义的截断实现；其它 Agda reflection primitives/版本；现实桥。
- `STALE_IF`：canonical target、相关 API 源码树、B 方向定义或另一 lane 的路径所有权发生改变。

## 下一动作

`SEM-B01`–`SEM-B05` 均已达到各自停止条件，reflection primitive 枚举在此停止。下一单元
回到人工语义主线：只选择具有固定版本、自然 consumer 和明确交付承诺的一个新机制，先核
承诺所在阶段，再判断是否存在理论资格提升。该单元不建设 task grammar、registry、case
evaluator、verifier 或跨层调度；这些属于 machine-overview lane。

## 集成候选

未来 integrator 应以 exact candidate OID 审查本分支，只提取接受的独占实物，并在 canonical target 上一次性更新 current owners。当前建议项仅包括：

1. 将两个初始消费者及弱常值泛性质的四个直接调用点细分为已语义检查的负控制；
2. 将 finite decision 的 16 文件自然理论消费登记为 `E6a` 已见，同时保持 `E6b/E6c` 开放；
3. 评估是否接受 `E6a/E6b/E6c` 三分，避免“理论 consumer”与“有效交付 consumer”混同；
4. 将 postulated truncation 的 kernel 接受、后端生成与运行失败登记为 Q3/Q4 分层实例，不升级为悖论；
5. 以后修订扫描器时增加 `weakly-constant` 提示，并以新版本快照刷新 repo-formal 扫描，不覆盖历史 JSON。
6. 将 finite-decision 外部状态登记为 `E6B_CONSUMER_SOURCE_GAP`，保留第三方 fixed-commit consumer、FFI 实现或完整代码语料三类重开条件。
7. 将 B04 登记为资格审计的正控制：proof generator 的经济收益由 soundness lemma 与 Agda
   类型检查支付，两个越界目标在固定输入上失败关闭。
8. F-016 已完成候选实现和 fresh 验收；integrator 审查 exact `214b15d…`，按 target HEAD
   重建可能冲突的 revision 130/131，并在 target fresh worktree 重跑同一套 5 task/6 verifier/4
   negative acceptance。
9. 将 B05 登记为显式假设边界控制：默认模式的成功依赖新增公理，safe 模式拒绝该操作但
   允许普通 proof-term reflection；不得把 API 能力归因给未调用它的 solver。
10. 保持 lane 分工：本分支提供人工语义判例与自然 consumer 证据，machine-overview 分支
    负责自动化统观基础设施；概念交集不转化为共同路径或重复实现。

以上均未提交集成，也不是项目 current truth。
