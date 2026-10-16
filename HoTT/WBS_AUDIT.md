# 对 HOTT–Z 45 个工作包的审计

状态：`CURRENT AUDIT`
被审对象：`HOTT_Z_AI_HANDOFF_20260831/canonical/planning/HOTT_Z_WBS_REGISTRY_v1.json` 与
`HOTT_Z_WBS_EXECUTION_STATUS_v2.json`

## 1. 总裁决

这套 WBS 的机械结构合格：45 个 ID 唯一、依赖指向存在、依赖图无环、流和里程碑可解析。
但它不是可靠的完成证明，原因有四个：

1. 它把一个可压缩为“表示损失 + 无自然选点 + 方向 reduct”三件事的数学核心，扩成 45 个包、
   三篇论文、一篇哲学稿及一个发布项目，范围显著大于已得到的非平凡结果。
2. 37 个包被同一句 `COMPLETE_INTERNAL` 批量覆盖；原始状态仍包含 16 个 `READY`、6 个 `ACTIVE`、
   3 个 `BLOCKED`、1 个 `EXTERNAL_GATE` 等。这种覆盖没有逐项给出 acceptance-to-evidence 映射。
3. 至少 16 个已标 `COMPLETE_INTERNAL` 的包，验收文字明确要求 V4、编译、机器归约、权威文献或
   外部证据；当时相应证据并不齐全。
4. “内部工作已做到环境上限”与“工作包验收通过”被混用。前者可以是真的，后者必须逐条证明。

因此，45 包登记表应保留为 `HISTORICAL_PLANNING_EVIDENCE`，不再作为当前执行真值。

## 2. 分流规则

- `SUPPORTED`：精确、窄化后的核心有纸面或机器证据。
- `PARTIAL`：存在有价值产物，但原验收或标题范围没有全部满足。
- `CONSOLIDATE`：属于来源/编号/治理辅助，不应继续占一个独立数学工作包。
- `SEPARATE`：可能是合法研究，但与当前 HoTT–Z 窄主线不同，不能拼成一个“主定理”。
- `NOT_ESTABLISHED`：现有材料没有达到工作包声称的结果。
- `EXTERNAL_OPEN`：只能由独立外部行动关闭，本轮不能内部自证。

## 3. 逐包处置

| WP | 简称 | 审计处置 | 理由 |
|---|---|---|---|
| WP-000 | 规范基线与术语冻结 | `CONSOLIDATE` | 本审计的主张矩阵已承担该职责；不再维护另一套状态词。 |
| WP-010 | 来源谱系/去重 | `SUPPORTED` | 交接源注册表和本项目 `SOURCE_REGISTRY.md` 可追溯；AI 文本仍非独立数学证据。 |
| WP-020 | 编号治理 | `CONSOLIDATE` | ID 完整性通过，但编号平台本身不是研究成果。 |
| WP-030 | 旧攻击红队回归 | `PARTIAL` | 旧错误大多被识别；原 lint 当前误报且记录陈旧，不能称完整回归。 |
| WP-100 | 完备性分类/目标语义 | `SUPPORTED` | “内部一致性、表达、表示、有效性”必须分开，这个纠偏成立。 |
| WP-110 | 真值谱因子分解 | `SUPPORTED` | 必要方向已在 Agda 检查；任意余域充分方向没有被错误保留。 |
| WP-120 | 损失谱/精化单调性 | `PARTIAL` | 思路是一般序理论；有限原型不等于完整、原创的格论结果。 |
| WP-130 | 最小充分真值商 | `PARTIAL` | 商/泛性质需要精确截断和消去假设；现有机器文件未覆盖原验收。 |
| WP-140 | 无免费富化 | `SUPPORTED` | 作为条件性因子化推论成立；不是 HoTT 矛盾。 |
| WP-150 | Galois/格结构 | `NOT_ESTABLISHED` | 候选方向多于证明，且很可能是已知信息序/充分统计结构的改写。 |
| WP-200 | 固定点自由 monodromy | `SUPPORTED` | 一般引理在自包含 Agda 中通过；其应用仍须实际构造 loop 与无固定点 transport。 |
| WP-210 | 裸二事件无规范较早事件 | `PARTIAL` | 无统一选点定理通过；“较早”只是额外解释，不在机器类型中。 |
| WP-220 | 严格时间序与 `n≥2` | `NOT_ESTABLISHED` | 原 Agda `TemporalOrder` 仅有 `least-event`，未形式化严格序公理；一般化也未关闭。 |
| WP-230 | groupoid core/反演盲性 | `SUPPORTED_WITH_SCOPE` | core 忘掉非可逆箭头方向成立；有限 Lean/Agda 实例通过；不攻击普通 Hom。 |
| WP-240 | directed/temporal 富化边界 | `PARTIAL` | 一手文献支持“方向需额外结构”；“非保守性”需按具体理论/翻译逐项证明。 |
| WP-250 | HoTT 时间—历史主定理 | `NOT_ESTABLISHED_AS_MAIN_THEOREM` | 目前是已知无选点定理与一般 reduct 事实的综合，尚非新的 HoTT 不完备定理。 |
| WP-300 | 快照—来源不可定义 | `SUPPORTED_INSTANCE` | 二世界反例机器通过；只针对明确丢失来源的 snapshot。 |
| WP-310 | 语义角色/品牌/SIP | `PARTIAL` | 有限反例成立；任意外部意义与 SIP 的一般边界未完成。 |
| WP-320 | 无语境完美形式化器 | `SUPPORTED_INSTANCE_ONLY` | 二语境同文本反例通过；自然语言不可判定强版没有正式编码和归约。 |
| WP-330 | assertion/mere existence/witness | `PARTIAL` | 无全局选择的上游定理可用；三层障碍的全部专门化和系统假设需更精确。 |
| WP-340 | 表示独立/签名相对完备 | `PARTIAL` | 是合理框架语言，不是已完成的单一新定理。 |
| WP-400 | 外延函数不决定成本 | `SUPPORTED_INSTANCE` | 作为丢失成本注释的有限 reduct 例成立；并非普遍操作复杂度定理。 |
| WP-410 | Cartesian—linear 障碍 | `SEPARATE/PARTIAL` | 原“一次 transport”论证错误；可研究资源敏感翻译，但须另立精确演算。 |
| WP-420 | 完备 inhabitant synthesizer | `NOT_ESTABLISHED` | 缺目标演算、编码、soundness/completeness 与机械归约；只能保留条件性计算论模板。 |
| WP-430 | 未来最终稳定性/停机 | `SEPARATE/PARTIAL` | 对可计算预测器可做归约，但不是 HoTT 专属，也未关闭全部形式条件。 |
| WP-440 | guard erasure/固定点 | `SUPPORTED_CONDITIONAL` | 最小固定点引理通过；guardedness 的系统级结论需要具体 later/clock 理论。 |
| WP-450 | 极限/闭包/可达性/Zeno | `SEPARATE` | 重要概念澄清，但不是当前 HoTT–Z 核心证明。 |
| WP-460 | 有效极限/Specker | `SEPARATE` | 属可计算分析已知结果；必须以权威文献为主，不能包装为 HoTT 原创。 |
| WP-500 | Lawvere/Gödel 反射 | `SEPARATE/NOT_ESTABLISHED` | 原 `Map(1,G)` 前提错误；正确反射定理需独立设置和证明。 |
| WP-510 | 宇宙/resizing/predicativity | `SEPARATE/PARTIAL` | 有效风险清单，但未得到跨 HoTT 变体的统一否定结果。 |
| WP-600 | 工具链锁定 | `PARTIAL_REPAIRED_HERE` | 版本/commit 锁定正确；原构建脚本的全局 flags 错误，本项目已给出可运行替代。 |
| WP-610 | agda-unimath 无规范点 | `SUPPORTED` | 锁定上游定理存在且本地 wrapper 编译通过。 |
| WP-620 | 机器化严格时间序 | `NOT_ESTABLISHED` | 仅机器化“结构含 chosen point”；标题超出代码。 |
| WP-630 | 因子化/core/provenance 实例 | `SUPPORTED_WITH_SCOPE` | 自包含 Agda 核心和有限 Lean 模型均通过。 |
| WP-640 | 第二助手/自足 Cubical | `PARTIAL` | Lean 只交叉检查有限模型，不是第二个 univalence/no-section 实现。 |
| WP-650 | 回归/CI | `PARTIAL_BROKEN` | 文档引用的 `verification/run_all.sh` 不存在；活动 claim lint 当前失败且旧收据过时。 |
| WP-700 | 系统文献检索 | `PARTIAL` | 核心一手来源已校准；尚无可声称穷尽的系统综述或完整检索协议。 |
| WP-710 | 原创性矩阵 | `SUPPORTED_AS_NEGATIVE_AUDIT` | 本审计已明确：当前未建立新颖 HoTT 主定理。 |
| WP-720 | 内部对抗审稿 | `SUPPORTED` | 本审计复核类型、语义桥、反例、机器证据和构建路径；仍不能替代外审。 |
| WP-730 | 独立专家复核 | `EXTERNAL_OPEN` | 没有独立专家签名、报告或外部干净环境复现收据。 |
| WP-800 | 论文 I | `NOT_PUBLICATION_READY` | 可形成诚实技术说明；原创性与外审门未闭合。 |
| WP-810 | 论文 II | `DEFER/SEPARATE` | 签名、资源、自然语言和计算论问题过多，不应与第一条线并行宣称完成。 |
| WP-820 | 论文 III | `DEFER/SEPARATE` | 反射/宇宙支线未达到独立论文证明标准。 |
| WP-830 | 哲学综合 | `DRAFT_ONLY` | 可保留为动机和边界讨论，不能承担数学证明。 |
| WP-840 | 可复现发布包 | `PARTIAL` | 文件哈希与快照 parity 通过；构建入口缺失/错误、lint 陈旧、外部门未闭合。 |

## 4. 原状态覆盖的直接证据

`HOTT_Z_WBS_EXECUTION_STATUS_v2.json` 的 45 项分布为：37 项 `COMPLETE_INTERNAL`，其余 8 项各用
一个复合状态表示本地/外部门未闭合。37 项全部使用同一句执行说明：

> All planned internal analysis, paper proof, documentation, and available executable checks were completed.

与此同时，原注册状态仍是：`READY=16`、`PAPER_PROVED=13`、`ACTIVE=6`、`BLOCKED=3`、
`PAPER_PROVED_CONDITIONAL=3`、`BASELINED=2`、`BACKGROUND=1`、`EXTERNAL_GATE=1`。

至少以下 16 项在验收文本中显式要求机器、编译、权威文献或外部证据，但被批量标成
`COMPLETE_INTERNAL`：WP-030、110、120、130、200、210、220、230、250、300、310、330、420、
440、460、700。这足以否定“37 项均满足自身 acceptance criteria”的解释。

## 5. 替代方案：不再建第二套大型 WBS

当前只保留六个成果面：

| 成果面 | 完成条件 | 当前状态 |
|---|---|---|
| 来源与谱系 | 16 份迁移源、用户对话、相邻 proofs/dev-docs/handoff 职责和哈希可追溯 | `VERIFIED_LOCAL` |
| 主张纠错 | 每个强主张有接受/拒绝/条件化裁决，错误公式有替代 | `VERIFIED_LOCAL` |
| 数学核心 | 因子化必要条件、无免费富化、无统一选点、方向/来源有限反例 | `VERIFIED_LOCAL_WITH_SCOPE` |
| 可复现构建 | 当前项目脚本在锁定 Agda/unimath 下通过，Lean 可选交叉检查 | `VERIFIED_LOCAL` |
| 原创性边界 | 不宣称 HoTT 矛盾、绝对无时间或新主定理 | `VERIFIED_NEGATIVE_CONCLUSION` |
| 外部发表门 | 独立专家复核、真正新定理、外部干净环境复现 | `OPEN_EXTERNAL` |

前五项构成此次本地可闭合的整体目标；第六项不能由同一个 AI 在同一环境里自我宣告完成。
