# HoTT–Z 主张—证据矩阵

<!-- math-proof-index-contract:v1
authoritative_index: HoTT/CLAIM_EVIDENCE_MATRIX.md
proof_source_root: HoTT/formal
proof_run_root: HoTT/verification/runs
-->

状态：`CURRENT`
裁决日期：2026-08-31；扩展：2026-09-01

本表是当前主张状态的唯一快速入口。正文推理见 `AUDIT_AND_RECONSTRUCTION.md`；机器证据见
`verification/VERIFICATION_REPORT.md`。`VERIFIED` 只表示表中精确命题在注明范围内有直接证据，
不把解释性外推一并升级。

## 数学结论机器证明交付索引合同

从 `MATH_PROOF_BEFORE_DELIVERY_V1` 生效后，每个由当前 AI 交付为数学结论的 claim 行必须连接稳定 proof ID、精确形式命题、`formal/` 源码、`verification/runs/<run-id>/` 收据、proof assistant/kernel 版本、状态和禁止外推。只有源码和 run 都在 repo 内、实际 kernel 结果通过且索引完整时，状态才能是 `MACHINE_PROVED_LOCAL_UNCOMMITTED` 或 `MACHINE_PROVED_VERSION_CLOSED`。

现有证明在新门禁生效前使用 aggregate receipt，继续保持历史范围；未来重新交付时必须产生新 run package，不因旧 `exit 0` 自动豁免：

| proof_id | 关联 claim | 形式化源码 | 历史运行证据 | 当前门禁身份 |
|---|---|---|---|---|
| `MP-LEGACY-ZCORE` | `C-01`–`C-04`、`C-24`、`C-41` | `formal/self-contained/ZCore.agda` | `verification/VERIFICATION_REPORT.md` §5–§7 | `LEGACY_AGGREGATE_RECEIPT_REPLAY_REQUIRED_FOR_NEW_DELIVERY` |
| `MP-LEGACY-NO-CANONICAL-POINT` | `C-05` | `formal/agda-unimath/hott-z/NoCanonicalPoint.agda` | `verification/VERIFICATION_REPORT.md` §3–§7；新重放见 `MP-UNIMATH-NOSECTION-REPLAY-001` | `LEGACY_AGGREGATE_RECEIPT_SUPERSEDED_BY_PINNED_REPLAY_20260913` |
| `MP-LEGACY-TWO-EVENT` | `C-04` | `formal/lean/TwoEvent.lean` | `verification/VERIFICATION_REPORT.md` §5–§7 | `LEGACY_AGGREGATE_RECEIPT_REPLAY_REQUIRED_FOR_NEW_DELIVERY` |
| `MP-ERCF-001` | `C-59`–`C-66` | `formal/ercf-factorization/ERCF.lean` | `verification/runs/20260912-MP-ERCF-001-02/`；Lean 4.33.1；exit 0；source/output hashes verified | `MACHINE_PROVED_LOCAL_UNCOMMITTED` |
| `MP-ERCF-TRUNC-001` | `C-67`–`C-70` | `formal/ercf-truncation-defense/TruncationDefense.agda` | `verification/runs/20260912-MP-ERCF-TRUNC-001-01/`；Agda 2.8.0；Cubical v0.9；`--safe --cubical`；exit 0 | `MACHINE_PROVED_LOCAL_UNCOMMITTED / DEFENSE_WORKS` |
| `MP-RACE-TIMEOUT-001` | `C-71`–`C-76` | `formal/partiality-race-timeout/PartialityRaceTimeout.agda` | `verification/runs/20260912-MP-RACE-TIMEOUT-001-01/`；Agda 2.8.0；Cubical v0.9；`--safe --cubical`；exit 0 | `MACHINE_PROVED_LOCAL_UNCOMMITTED / REPRESENTATION_BOUNDARY` |
| `MP-CONTEXTUAL-EQUIV-001` | `C-77`–`C-83` | `formal/partiality-race-timeout/ContextualEquivalence.agda` | `verification/runs/20260912-MP-CONTEXTUAL-EQUIV-001-01/`；Agda 2.8.0；Cubical v0.9；`--safe --cubical`；exit 0 | `MACHINE_PROVED_LOCAL_UNCOMMITTED / REPRESENTATION_BOUNDARY` |
| `MP-QUOTIENT-MONAD-001` | `C-84`–`C-88` | `formal/partiality-race-timeout/QuotientMonad.agda` | `verification/runs/20260912-MP-QUOTIENT-MONAD-001-01/`；Agda 2.8.0；Cubical v0.9；`--safe --cubical`；exit 0 | `MACHINE_PROVED_LOCAL_UNCOMMITTED / MONAD_STRUCTURE_CONSTRUCTED` |
| `MP-CONTEXT-CHARACTERIZATION-001` | `C-89`–`C-91` | `formal/partiality-race-timeout/ContextCharacterization.agda` | `verification/runs/20260912-MP-CONTEXT-CHARACTERIZATION-001-01/`；Agda 2.8.0；Cubical v0.9；`--safe --cubical`；exit 0 | `MACHINE_PROVED_LOCAL_UNCOMMITTED / CONTEXTUAL_EQUIVALENCE_FULLY_CHARACTERIZED` |
| `MP-GUARD-ERASURE-001` | `C-92`–`C-95` | `formal/partiality-race-timeout/GuardErasure.agda` | `verification/runs/20260912-MP-GUARD-ERASURE-001-01/`；Agda 2.8.0；Cubical v0.9；`--safe --cubical`；exit 0 | `MACHINE_PROVED_LOCAL_UNCOMMITTED / GUARD_ERASURE_EQUIVALENT_TO_FIXED_POINT_EXISTENCE` |
| `MP-COST-FACTORIZATION-001` | `C-96`–`C-99` | `formal/partiality-race-timeout/CostFactorization.agda` | `verification/runs/20260912-MP-COST-FACTORIZATION-001-01/`；Agda 2.8.0；Cubical v0.9；`--safe --cubical`；exit 0 | `MACHINE_PROVED_LOCAL_UNCOMMITTED / NON_FACTORIZATION_WITH_COST_REFINEMENT_POSITIVE_CONTROL` |
| `MP-PATH-CERTIFICATE-001` | `C-100`–`C-105` | `formal/partiality-race-timeout/PathCertificate.agda` | `verification/runs/20260912-MP-PATH-CERTIFICATE-001-01/`；Agda 2.8.0；Cubical v0.9；`--safe --cubical`；exit 0 | `MACHINE_PROVED_LOCAL_UNCOMMITTED / MERE_MOVE_NON_INHABITED_WITH_NATIVE_PATH_CONTROLS` |
| `MP-ONLINE-CAUSALITY-001` | `C-106`–`C-109` | `formal/partiality-race-timeout/OnlineCausality.agda` | `verification/runs/20260912-MP-ONLINE-CAUSALITY-001-01/`；Agda 2.8.0；Cubical v0.9；`--safe --cubical`；exit 0 | `MACHINE_PROVED_LOCAL_UNCOMMITTED / ONLINE_CAUSALITY_BOUNDARY_WITH_POSITIVE_CONTROLS` |
| `MP-TRANSITION-LIFT-001` | `C-110`–`C-117` | `formal/transition-lift/TransitionLift.agda` | `verification/runs/20260912-MP-TRANSITION-LIFT-001-01/`；Agda 2.8.0；Cubical v0.9；`--safe --cubical`；exit 0 | `MACHINE_PROVED_LOCAL_UNCOMMITTED / TRANSITION_LIFT_BOUNDARY_WITH_POSITIVE_CONTROLS` |
| `MP-PARTIAL-DECISION-001` | `C-118`–`C-123` | `formal/partial-decision/PartialDecision.agda` | `verification/runs/20260912-MP-PARTIAL-DECISION-001-01/`；Agda 2.8.0；Cubical v0.9；`--safe --cubical`；exit 0 | `MACHINE_PROVED_LOCAL_UNCOMMITTED / PARTIAL_DECISION_BOUNDARY_WITH_POSITIVE_CONTROL` |
| `MP-SIP-REPRESENTATION-001` | `C-124`–`C-128` | `formal/sip-representation/SIPRepresentation.agda` | `verification/runs/20260912-MP-SIP-REPRESENTATION-001-01/`；Agda 2.8.0；Cubical v0.9；`--safe --cubical`；exit 0 | `MACHINE_PROVED_LOCAL_UNCOMMITTED / SIP_REPRESENTATION_BOUNDARY_WITH_POSITIVE_CONTROL` |
| `MP-CAUCHY-MODULUS-001` | `C-129`–`C-133` | `formal/cauchy-modulus/CauchyModulus.agda` | `verification/runs/20260912-MP-CAUCHY-MODULUS-001-01/`；Agda 2.8.0；Cubical v0.9；`--safe --cubical`；exit 0 | `MACHINE_PROVED_LOCAL_UNCOMMITTED / CAUCHY_MODULUS_BOUNDARY_WITH_POSITIVE_CONTROLS` |
| `MP-TRUNC-NORECOVERY-001` | `C-134`–`C-141` | `formal/truncation-no-recovery/TruncationNoRecovery.agda` | `verification/runs/20260913-MP-TRUNC-NORECOVERY-001-03/`（含 C-141；`-02`/`-01` 为同源前次运行）；Agda 2.8.0；Cubical v0.9；`--safe --cubical`；exit 0 | `MACHINE_PROVED_LOCAL_UNCOMMITTED / SET_VALUED_TRUNCATION_NO_RECOVERY_FAMILY` |
| `MP-NOCANONICAL-001` | `C-142`–`C-148` | `formal/truncation-no-recovery/NoCanonicalPoint.agda`（bridge：`formal/truncation-no-recovery/NoCanonicalFinite.agda`） | `verification/runs/20260913-MP-NOCANONICAL-001-02/`（`-01` 为同源前次运行，加 C-148 后被取代）；Agda 2.8.0；Cubical v0.9；`--safe --cubical`；exit 0 | `MACHINE_PROVED_LOCAL_UNCOMMITTED / UNLABELED_FINITE_NO_CANONICAL_POINT` |
| `MP-UNIMATH-NOSECTION-REPLAY-001` | `C-05` | `formal/agda-unimath/hott-z/NoCanonicalPoint.agda`（外部库 agda-unimath@`7b81411d`，按 commit SHA、库文件哈希与确定性源码树哈希固定） | `verification/runs/20260913-MP-UNIMATH-NOSECTION-REPLAY-02/`；Agda 2.8.0-3d04bac；agda-unimath `7b81411d`；`--without-K --exact-split`；exit 0（`-01` 为被保留的 include 根配置失败尝试） | `REPLAYED_EXTERNAL_LIBRARY_WITH_SCOPE` |

未机器证明的新内容只能使用 `QUESTION`、`CONJECTURE`、`HEURISTIC`、`PAPER_ONLY`、`COUNTEREXAMPLE_CANDIDATE` 或 `SOURCE_REPORTED_NOT_REPLAYED`，不得用旧矩阵中相似标题反向推定已证。

| ID | 主张 | 裁决 | 直接依据 | 禁止外推 |
|---|---|---|---|---|
| C-01 | 若 `J = decode ∘ α`，则 `J` 在 `α` 的每个纤维上常值。 | `VERIFIED` | `formal/self-contained/ZCore.agda` 的 `fiber-truth-invariant`；纯因子化必要条件。 | 不自动得到充分性；一般余域上的延拓可能需要额外条件。 |
| C-02 | 若 `α` 合并两个 `J` 值不同的世界，而 `(α,β)` 可精确恢复 `J`，则 `β` 必须区分这两个世界。 | `VERIFIED` | `ZCore.agda` 的 `no-free-enrichment`。 | “必须增加信息”不是原理论矛盾，也不说明任何特定富化唯一。 |
| C-03 | 从丢失来源的相同快照不能恢复两个不同来源。 | `VERIFIED_INSTANCE` | `ZCore.agda` 的 `snapshot-cannot-recover-provenance`。 | 只攻击给定 reduct；显式携带 provenance 后当然可恢复。 |
| C-04 | 从把正向/反向过程都映到同一 core 的 reduct 不能恢复方向。 | `VERIFIED_INSTANCE` | `ZCore.agda` 的 `core-cannot-recover-direction`；`formal/lean/TwoEvent.lean` 独立有限模型。 | 不是“范畴或 HoTT 中所有态射可逆”；普通函数和 Hom 可以有方向。 |
| C-05 | `agda-unimath` 中不存在对所有无标签二元素类型统一选点的 section。 | `MACHINE_REPLAYED_EXTERNAL_LIBRARY_WITH_SCOPE` | 定义位于 agda-unimath@`7b81411d` 的 `src/univalent-combinatorics/2-element-types.lagda.md:501`；本 repo 派生文件 `formal/agda-unimath/hott-z/NoCanonicalPoint.agda` 在固定 Agda 2.8.0-3d04bac 下重放通过（run `20260913-MP-UNIMATH-NOSECTION-REPLAY-02`（`-01` 为被保留的 include 根配置失败尝试））；历史记录（旧 commit 简写 `88cfce0…` 与当时本地薄封装编译）保留于 Git 与 source ledger。 | 这是无自然/统一选点，不是一般全局选择公理的全部内容。 |
| C-06 | 因而“每个无标签二事件载体都有规范较早事件”不成立。 | `CONDITIONAL_INTERPRETATION` | C-05，加桥梁定义“较早事件 = 无额外定向数据的统一选点”。 | 桥梁不是上游定理的一部分；若输入已经有顺序，最小元可被选择。 |
| C-07 | 交接包的 `TemporalOrder` 已形式化严格时间序。 | `FALSE_AS_STATED` | 该 record 只有 `least-event` 字段，没有关系、非自反、传递或全序公理。 | 其编译通过也只能证明“所选结构含一个点”。 |
| C-08 | 标准 HoTT 的 identity/path 层是群胚式的，单靠 groupoid core 看不到非可逆箭头方向。 | `ESTABLISHED_WITH_SCOPE` | HoTT Book 的路径/∞-群胚解释；Riehl–Shulman 通过额外 directed interval 构造 directed theory；C-04 为有限 reduct 例。 | “identity 层群胚式”不等于“HoTT 不能定义有向关系、状态机或时间索引”。 |
| C-09 | 标准 HoTT 没有 primitive time，因此无法表示任何时间或动态。 | `REFUTED` | 原论证把“非原语”偷换成“不可编码”；自然数、关系、序列、状态转换均可作为结构形式化；guarded/directed 类型论展示的是更原生的额外结构。 | 仍可研究某种表示是否不自然、非内生或丢失特定可观察量。 |
| C-10 | `Map(1,G)` 是 `G` 的 loop space。 | `FALSE` | 对终对象 `1`，`Map(1,G) ≃ G`；基点 `g` 的 loop space 是 `g =_G g`。 | 由错误等式推出的循环/自指悖论全部失效。 |
| C-11 | 不同宇宙角色相似即可推出宇宙等价；某次 lift 失败即可推出不存在等价。 | `UNPROVED/INVALID_INFERENCE` | 原材料没有构造等价，也没有排除全部候选等价；“角色相似”不是等价数据。 | 不得把宇宙大小、resizing、predicativity 问题混成同一反例。 |
| C-12 | `Id_A(a,b)` 可在 `a:A, b:B` 时直接形成。 | `ILL_TYPED_AS_WRITTEN` | identity type 要求两端在同一类型（或先给出运输/等价后的同型端点）。 | 不能用未定型表达式作为悖论前提。 |
| C-13 | 线性逻辑只允许整个系统发生一次 transport。 | `FALSE` | 线性资源约束针对具体假设/资源的使用；多个独立资源可分别使用一次。 | 不得从“每份资源一次”推成“宇宙总共一次”。 |
| C-14 | type checking 与 proof search 的差异证明 HoTT 本体论失败。 | `NON_SEQUITUR` | 这是算法任务、可判定性和资源界限的差异，不是对象论矛盾。 | 计算限制须绑定精确语法、编码和归约。 |
| C-15 | 未定义的 `Translate : InformalProblem → Type` 可直接由停机问题推出“不存在完美形式化器”。 | `UNPROVED` | 输入语言、正确性谓词、编码和归约均未给出；现有二比特证明只建立语境欠定实例。 | 不得把自然语言歧义自动升级为不可判定性定理。 |
| C-16 | `n → ∞` 是需要完成字面无限次步骤的单一过程。 | `FALSE_AS_GENERAL_READING` | 极限、完备化、可达性和算法收敛是不同概念；数学极限不等于执行一个“最后无限步”。 | Specker/有效收敛等结果需要具体可计算分析设定。 |
| C-17 | Univalence 会把“理论本质”与社会表现、品牌、历史角色自动判同。 | `FALSE` | univalence 连接类型相等与类型等价，不把任意外在社会谓词强制成结构不变量。 | 外在角色不可恢复可以是真命题，但源于选择的表示/签名。 |
| C-18 | 已证明 `HoTT ⊢ ⊥`，或 HoTT 已被推翻。 | `REJECTED` | 交接包自己的规范文本也明确否认此结论；所有可保留定理均为目标相对的表示/自然性陈述。 | 标题、角色扮演评价、AI 共识和“最终判决”不是证明。 |
| C-19 | 当前成果已达到新颖的 HoTT 不完备主定理。 | `NOT_ESTABLISHED` | 机器核心由一般因子化、二元素无 section 和有限反例组成；尚无超越已知结果的 HoTT 专属定理。 | 在原创性逐定理比对和独立专家复核前不得使用“首次、推翻、主定理”宣传。 |
| C-20 | 45 个工作包已经全部满足各自验收。 | `FALSE` | 37 项被同一句 `COMPLETE_INTERNAL` 批量覆盖；至少 16 项验收含机器/文献/外部证据而当时证据不足。 | “做过内部分析”与“验收通过”必须分开。 |
| C-21 | HoTT 完全不能处理任何关于自身的问题。 | `FALSE_AS_ABSOLUTE / REAL_METATHEORETIC_GAP` | 旧对话明确存在自指/元观察者支线；HoTT 社区公开研究 self-metatheory，2LTT 用 outer strict layer 内部化 HoTT 元理论；见 `SELF_REFERENCE_AND_REFLECTION_INVESTIGATION.md`。 | 不得把旧 `G ≃ Map(1,G)` 当证明；准确问题是完整 syntax/semantics/reflection/consistency 能否在同层、无富化地内部化。 |
| C-22 | HoTT 能定义 `Time`，所以 HoTT 理论自身已经具有强时间维度。 | `FALSE_EQUIVOCATION` | HoTT 可表示时间；其 λ-calculus 也有有向 reduction，故并非绝对静态。但标准 judgment 不默认以 clock/stage/causality/resource/trace 为不可擦除坐标；见 `INTRINSIC_TEMPORALITY_OF_HOTT.md`。 | 必须区分对象时间、弱操作时间、强内生时态和物理时间；不得把“能建模”或“能归约”直接等同于强时间本体。 |
| C-23 | 当前 HoTT 研究目标是优先证明内部不一致 `HoTT ⊢ ⊥`。 | `REFUTED_BY_CURRENT_USER_REQUIREMENT` | R-007 与 `sources/user-originals/Z铁律-抽象-圆环-时间维度-用户原始论述-20260901.md`：用户明确要求寻找 Thinking in HoTT 产生的现实相对非现实性。 | 不降低旧内部一致性审计的有效性；只是改变当前验收目标。 |
| C-24 | 对会合并某个现实过程、结论或现象观察量取值不同状态的非平凡抽象，完整现实推演效应谱 `X` 与只依赖抽象的理论谱 `Y` 必然分岔。 | `VERIFIED_WITH_DEFINITIONS` | `Z_LAW_REALITY_RELATIVE_PARADOXES.md` §2 的异质观察族；`formal/self-contained/ZCore.agda` 的纤维不变量给出逐观察量必要方向。 | 二值命题—判定谱只是特例；“所有抽象”须限定为实质删除目标区分的 proper abstraction；不自动得到理论内部 `φ∧¬φ`。 |
| C-25 | “计算合法性/因果准入先于真值”是后续 AI 推断，不是用户原始思想。 | `FALSE / VERIFIED_USER_SOURCE` | `sources/user-originals/Better-Best悖论-原文.md` 与本轮用户原文逐字提出序列点、落定、伪命题和计算合法性。 | 用户术语“可计算性”与标准 computability/decidability/termination 仍须分层。 |
| C-26 | 圆环悖论的严格核心是点没有大小，因此拓扑上开区间无法回到断圆。 | `FALSE_AS_TOPOLOGY / SUPPORTED_AS_HISTORY_ERASURE` | `S¹\{p} ≃ (0,1)`，保留同胚可逆；真实障碍是从带环境、共同缺口和展开史的丰富对象忘到裸区间后，端部共同来源/闭合关系不再可恢复；见 Z owner §4.4。 | 不得把距离趋零、端点等同、拓扑同胚和物理复原混称。 |
| C-27 | 标准单价基础中 pointwise equal functions 可以由 function extensionality 得到函数 identity。 | `ESTABLISHED_PRIMARY_SOURCE` | HoTT Book §4.9：univalence implies function extensionality；Z owner §7。 | 是函数行为 identity，不自动等于程序代码、运行史或物理实现 identity。 |
| C-28 | 两个实现可有相同外延函数而时间/资源成本不同；真实 cost 不经裸外延函数因子化。 | `ESTABLISHED_WITH_SCOPE` | 交接 Claim Z-156/Result R-71/PA-73；Niu–Harper *Cost-Aware Type Theory* 明确讨论 cost 与 function extensionality 张力；Z owner §7。 | 需固定 Program、Sem、Cost 和操作语义；可由 cost-aware/trace/quantitative 富化表达。 |
| C-29 | “同函数异时”已经是新的、机器形式化并经外部专家认可的 HoTT 悖论。 | `PRIMARY_SUPPORTED_CANDIDATE / NOT YET FORMALIZED_OR_EXTERNAL` | Z owner §7 给出 fast/slow 纸笔构造和现实桥梁；底层张力有一手文献。当前 `formal/` 尚无专门实现，也无独立 HoTT 专家报告。 | 不得宣称原创主定理、发表就绪或 HoTT 内部矛盾。 |
| C-30 | Guard-Erasure 已经给出标准 HoTT 缺时间的具体 no-go theorem。 | `GENERAL_LEMMA_VERIFIED / HOTT INSTANTIATION OPEN` | 交接 Claim Z-158/PA-74：遗忘阶段且保持更新律会要求固定点；`INTRINSIC_TEMPORALITY_OF_HOTT.md` 与 Z owner §10 记录具体翻译缺口。 | 必须固定 source/target 演算、forgetful translation 和不可擦除 observable，不能从一般动态系统直接外推。 |
| C-31 | 16 份迁移全文和现有摘要已经穷尽 `aistudio-docs` 中可回顾的 HoTT 历史讨论。 | `REFUTED_BY_CORPUS_EVIDENCE` | `hott-discussion-corpus/v1` CURRENT 扫描 2,091 份讨论源，登记 441 份候选与 2,006 个逐字片段；19 份非问答候选全部全文保留；全量 validator PASS。 | 这些数字相对于 v1 锚点，不证明完全无锚点的隐喻讨论也已发现。 |
| C-32 | 逐字语料被全量验证，所以其中主张正确且所有语义相关讨论均已完备收录。 | `FALSE_EQUIVOCATION` | validator 只证明 inventory、SHA、连续字节、结构统计、孤儿和锚点覆盖；所有条目仍为 `UNREVIEWED_RAW_CAPTURE`。 | 不得把抽取完整性外推为数学正确、用户采纳、原创性、外审或语义全覆盖。 |
| C-33 | corpus 的 `source_files=2,087` 与对照目录的“2,094 个文件”应当相等；差额七项都表示丢失原文。 | `FALSE_METRIC_CONFLATION / RECONCILED` | R-009 与来源 registry §1.2：旧 2,087 只计两个源根的小写 `*.md`；2,094 包含 2,091 份大小写不敏感 Markdown、CSV/TSV 报告和仓库 `.gitignore`。唯一真正缺失的 73,698-byte Markdown 已复制；两对精确名差异为 Unicode 等价别名；全文件多重集对账 PASS。 | 不能为追求数字相等把生成报告、配置或 `.DS_Store` 冒充讨论文档，也不能复制同字节 Unicode 别名。 |
| C-34 | “前提中的任意 `T` 变为 `¬T`，任意结论 `C` 必然变为 `¬C`”是无条件的标准数理逻辑定理。 | `FALSE_UNQUALIFIED / ACCEPTED_AS_CONDITIONAL_Z_ROOT` | 当前用户裁定 R-010 与 Z owner §2：当 `T` 是有效前提、目标效应对 `T` 本质敏感时，前提翻转必改变该对应效应；二值敏感情形表现为 `C→¬C`。无关或冗余前提不保证指定 `C` 翻转。 | 不能删除“有效前提、对应效应、本质依赖”三个条件，也不能用无关 `C` 反例抹去完整效应谱分岔的研究原则。 |
| C-35 | 把现实/理论差异写成命题—判定集合 `X/Y`，意味着只应在二值结论中寻找悖论。 | `FALSE_SCOPE_RESTRICTION` | R-010 与 Z owner §2.3–2.5：`X/Y` 已推广为过程、结论、现象的异质观察族；命题真值只是 `D_ω=𝟚` 的投影。 | 非二值搜索仍必须精确定义值域和比较关系；“过程/现象”不能成为免除形式化的模糊标签。 |
| C-36 | 本项目必须等待 HoTT 实例证明后，才能确认一般“抽象—否定—悖论潜势”原则。 | `REFUTED_BY_R-012 / PROJECT_FOUNDATIONAL_RESEARCH_PRINCIPLE` | R-012 与 Z owner §0/§2.6：用户明确把它设为研究起点；本项目定义 proper abstraction 为实质删除至少一个现实区分的理论抽象，条件非因子化给出悖论潜势。 | 这不是“当前 HoTT 已证明无条件外部全称定理”；不得把任意改名/忠实编码也算 proper abstraction，或声称任意结论都取反。 |
| C-37 | 说谎者、Russell 和 Better Best 都已严格归约为同一个不可停机程序/一般 Halting Problem。 | `FALSE_CONFLATION / PROGRAM SEMANTICS OPEN` | R-011、Matrix MP-03/MP-04 与 Z owner §4.5：现有材料支持形成/准入、无二值固定点、约束冲突和修订振荡等不同解释；没有给出统一语言和停机归约。 | 不得把 formation rejection、可立即检测的不满足、振荡、发散和不可判定停机混称；“无法构造 S”也不自动等于某程序永不停止。 |
| C-38 | shenchensh 悖论已经证明实数稠密性错误、物理时空离散且普朗克长度是最小单位。 | `USER_PHYSICAL_HYPOTHESIS / FORMAL COMPARISON OPEN` | Matrix MP-05–MP-08、R-011 与 Z owner §4.6：原作保存圆型闭合与离散转角两条解答；当前尚未完成连续仿射、射影无穷点和离散模型的严格比较，也无经验桥梁。 | 仿射交点趋于无穷/平行态无有限交点不自动要求物理点穿越无穷；Planck 尺度不能被写成已实验证实的最小像素。 |
| C-39 | 《宇宙编程学》第三版中全部显式悖论讨论已形成可回源独立原文。 | `VERIFIED_EXPLICIT_LEXICAL_AND_MANUAL_CHAIN_SCOPE` | generation `a18a4dcec701895cc959`：当前源 SHA `24530b89…9409`、10 个连续原文、84 张图；98 个显式悖论族命中中 86 入正文、12 为目录/书名/致谢、uncovered=0；manager validate PASS。 | 只覆盖当前词表和人工加入的完整解答链；不证明所有未命名隐喻、矛盾或潜在悖论已语义穷尽，也不证明原文解答正确。 |
| C-40 | 本研究所说的“否定”只指对象语言中明确写出的 `¬p`。 | `FALSE_SCOPE_RESTRICTION` | R-012 与 Z owner §2.6：除强否定外，还定义结构否定、形成域否定、操作/时态否定和理想化替换；共同要求是明确的现实前提/区分及其丢失或不相容。 | 省略不自动等于句法否定；单纯改名、可逆编码、目标域上的忠实等价和无关冗余删除不算实质否定。 |
| C-41 | 对 `Proper_Ω(α)`，必然存在至少一个现实观察量不通过 `α` 因子化；若只从抽象结果给出完整现实效应，至少一个现实状态必然失配。 | `VERIFIED_WITH_PROJECT_DEFINITIONS` | Z owner §2.4/§2.6.1；`formal/self-contained/ZCore.agda` 的纤维不变量。`Proper_Ω` 的定义直接给出同纤维异观察量状态。 | 保证的是悖论潜势，不是每条推论错误；实际悖论还需要合法理论推演、完整性提升和明确非现实爆点。 |
| C-42 | HoTT 中一个尤其由时间维度否定引发、达到芝诺/Russell/圆环式清晰度的具体悖论已经严格证明。 | `HOTT_SPECIFIC_PARADOX_MANIFESTATION / OPEN` | R-012、Z owner §2.6.2/§13 P0-0：同函数异时和 Guard-Erasure 仍是优先候选；C-29/C-30 分别缺项目内完整形式化、HoTT 特定 translation/现实桥梁。 | 不得用一般信息丢失、候选名称、纸笔直觉或项目基础原则冒充 HoTT 具体实例已经完成。 |
| C-43 | Russell 主要位于 Z 抽象—时间框架之外，因为它不涉及完成性提升或时间构造。 | `REFUTED_BY_R-013 / USER_PHILOSOPHY_CURRENT_INTERPRETATION` | R-013、用户原文七、Matrix MP-03/MP-04 与 Z owner §3.4：朴素集合本体把未落定的负向自依赖 specification 提升为完成集合；阶段构造反复拿入／拿出自身。 | 这是用户数学哲学中的 current interpretation；标准集合论比较仍须分列，不能以“用户裁定”代替技术模型。 |
| C-44 | Russell 自成员资格的最小阶段程序可写成 `rₙ₊₁=¬rₙ`，从任一布尔初值永久交替且无稳定固定点。 | `VERIFIED_ELEMENTARY_DYNAMIC_MODEL` | Z owner §3.4：`0→1→0→…`、`1→0→1→…`；静态完成态要求无解的 `r=¬r`。 | 该一比特模型刻画用户的拿入／拿出核心，不声称已形式化全部集合成员或唯一 Russell 语义。 |
| C-45 | 因为 Russell 构造不稳定，所以检测器也必不停止，且一般 Halting Problem 归约已经完成。 | `FALSE_CONFLATION` | R-013 与 Z owner §3.3–§3.4：validator 可检测负向同阶段依赖／无布尔固定点并有限返回 `REJECT_ILLEGAL_FORMATION`；尚无一般停机归约。 | 必须区分被请求构造、formation rejection、轨道振荡、程序发散与不可判定停机。 |
| C-46 | 一个理论拒绝非法 Russell 构造，说明该理论失败。 | `FALSE_BY_CAUSAL_ADMISSIBILITY_CONTRACT` | Better Best 原文、用户原文七、R-013 与 Z owner §3：准入判断先于成员／真值计算；拒绝非法输入是理论的成功行为。 | 朴素无限制概括的失败在于先准入完成 `S`；不把现代 ZFC、类型论或全部集合论统称为失败。 |
| C-47 | 未来 AI 应以训练数据中的主流／既有 Russell、悖论和 HoTT 解释作为默认裁判，再据此改写用户问题。 | `REFUTED_BY_USER_RESEARCH_METHOD` | R-013、用户原文七、HoTT README 与 docs/ai：当前合同为 `USER_MATH_PHILOSOPHY_FIRST / EVIDENCE_CRITICAL`；先内部重建，后外部比较。 | 既有知识仍用于反例、比较、形式化和证据审计；不是禁止读取或故意忽视。 |
| C-48 | Thinking in my math philosophy 意味着用户哲学中的数学／物理主张无需证明或不得被反驳。 | `FALSE_EQUIVOCATION` | R-013 与 docs/ai：研究问题和解释顺序由用户哲学拥有；技术真值仍须证明、反例、机器／经验和外审。 | 不能把 consensus-first 替换成 user-assertion-is-proof。 |
| C-49 | 现实相对悖论的 G4 只允许“理论表示提升为现实完整身份”，不能包含“未落定 specification 提升为完成对象”。 | `REFUTED / COMPLETION_OR_REALITY_PROMOTION` | R-013 与 Z owner §2.6.2：G4 现分 `FORMATION_PROMOTION` 和 `REALITY_PROMOTION`；Russell 属于前者。 | 两种提升仍须具体理论规则和爆点，不能用“完成性”模糊绕过 G2/G3。 |
| C-50 | Z 铁律的最高定性只是“某些抽象可能具有悖论潜势”，而不是“理论抽象必然导致悖论”。 | `REFUTED_BY_R-014 / Z_STRONG_PHILOSOPHICAL_LAW` | 用户原文八、R-014、Z owner §0 与 USER_CORE_DOUBT：工具性实质抽象必否定现实前提，完整效应谱中至少一个对应效应必分岔。 | “必然”是完整谱上的存在量词，不是每条理论推论都错误；对外普遍元定理量词化仍开放。 |
| C-51 | 用户强式“任何 T 变非 T，C 必成非 C”要求任意与 T 无关的 C 也翻转。 | `FALSE_MISREADING` | R-014 与 Z owner §2.1–2.2：`T` 是有效前提，`C` 是与它对应且本质依赖它的效应；二值完全反向才写 `C→¬C`，一般为 `X≠Y`。 | 不能用无关 C 反例抹去用户强律，也不能删除本质依赖条件。 |
| C-52 | 朴素集合论在 Z 视角下的根本否定只是“没有限制 comprehension”，与时间维度无关。 | `REFUTED_BY_USER_FINAL_QUALITATIVE_JUDGMENT` | 用户原文八、R-014、Z owner §0/§3.4：朴素静态集合本体把描述、构造、存在合一，不携带 formation stage/order/settlement；`rₙ₊₁=¬rₙ` 是被擦除时间的动态形状。 | 当前是用户数学哲学中的最高定性；标准理论可把问题描述为 unrestricted comprehension inconsistency，但不能静默覆盖该诊断。 |
| C-53 | 在用户程序解释中，说谎者若等待一个稳定真值会不断反转／无法完成。 | `USER_PROGRAM_INTERPRETATION / MINIMAL_REVISION_MODEL_SUPPORTED` | 用户原文八、Better Best 原文、Z owner §3.2/§4.5：`p_{t+1}=¬p_t` 为 period-2 修订轨道。 | 不自动等于标准一般 Halting Problem；其他真值语义可采用拒绝、未定义或分层。 |
| C-54 | 在用户程序解释中，Russell 构造等待稳定 `S` 时无法停机，但 validator 可停机拒绝。 | `VERIFIED_WITH_MINIMAL_STAGE_MODEL` | C-44–C-46、R-013/R-014、Z owner §3.4。 | “对象构造不终止”与“判定器不可停机／不可判定”必须分开。 |
| C-55 | Better Best 与说谎者/Russell 完全相同，任何实现都必然无限循环。 | `FALSE_CONFLATION / USER_UNIFIED_ILLEGAL_PROGRAM_FAMILY` | 用户原文八与 Z owner §4.1/§4.5：三者共享静态逻辑先偷渡完成／准入资格；Better Best 可由顺序和承诺 Gate 有限拒绝。 | 统一的是计算合法性哲学，不是相同运行时或相同 Halting 结论。 |
| C-56 | HoTT 已被证明重复朴素集合论的无时间错误。 | `USER_CORE_HOTT_HYPOTHESIS / ACTIVE_RESEARCH / NOT ESTABLISHED` | 用户原文八、R-014、Z owner §0/§11：怀疑来自数学理论构建者无时间化的认知惯性／路径依赖；具体 formation/identity/forgetful proof 尚未完成。 | 不得把深切怀疑写成已证事实；也不得以“HoTT 能定义 Time／有 reduction”提前关闭。 |
| C-57 | 技术上的潜势／显现分层可以把 Z 强律降格为不确定的“也许产生悖论”。 | `REFUTED_BY_TRUTH_OWNERSHIP` | R-014：技术层用于证明、分类和找实例；最高项目定性仍是完整效应谱中必有分岔。 | 对外定理边界继续披露；不以哲学强律冒充已完成全称形式证明。 |
| C-58 | “Russell 击退朴素集合论作为整个数学基础的企图”已经由本轮历史一手资料独立验证。 | `USER_HISTORICAL_INTERPRETATION / NOT EXTERNALLY_AUDITED_THIS_TURN` | 用户原文八与 R-014 保存该判断；本轮未进行 Russell／基础史的一手文献调查。 | 可作为用户思想史和研究定性，不能伪称本轮完成外部历史证明。 |
| C-59 | 若 `observe` 通过 `abstract` 因子化，则 `observe` 在 `abstract` 的每个纤维上常值。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `MP-ERCF-001` theorem `factorsThrough_implies_fiberConstant`；run `20260912-MP-ERCF-001-02`。 | 只给必要方向；逆向仍需额外条件。 |
| C-60 | 一个同抽象值、异观察值的 `ParadoxWitness` 排除 `observe` 通过 `abstract` 因子化。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `MP-ERCF-001` theorem `paradoxWitness_implies_not_factorsThrough`；同一 final run。 | “ParadoxWitness”是本文件定义的表示反例，不自动成为 HoTT 悖论或现实矛盾。 |
| C-61 | 若 `observe` 在纤维上常值且 `abstract` 有一个 section，则 `observe` 通过 `abstract` 因子化。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `MP-ERCF-001` theorem `fiberConstant_and_section_implies_factorsThrough`；同一 final run。 | section 是明确附加假设；不证明任意商/像都自动有 section。 |
| C-62 | 给定 `a₀:A` 与 `s₀≠s₁:S`，投影 `A×S→A` 合并 `(a₀,s₀)/(a₀,s₁)`，第二分量观察形成 witness 且不能通过该投影因子化。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `MP-ERCF-001` theorems `e0_has_paradoxWitness`、`e0_secondObservation_does_not_factor`；同一 final run。 | 这是通用乘积模型；不证明 HoTT 特定规则强制删除 `S`。 |
| C-63 | 由抽象值定义的观察必然通过该抽象因子化；E₀ 的第一分量观察是具体正控制。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `MP-ERCF-001` theorems `abstractDerivedObservation_factors`、`e0_firstObservation_factors`；同一 final run。 | 不证明所有现实任务都由抽象值定义。 |
| C-64 | 对 subsingleton 余域不存在 `ParadoxWitness`；任意 `Unit` 值观察都通过任意抽象因子化。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `MP-ERCF-001` theorems `subsingletonCodomain_has_no_paradoxWitness`、`unitObservation_factors`；同一 final run。 | 这是“非单射本身不足以产生任意余域反例”的负控制，不否定 separating 观察结果。 |
| C-65 | 若 `abstract` 非单射且一族观察能分离每一对被合并的不同状态，则该族中存在一个观察不通过 `abstract` 因子化。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `MP-ERCF-001` theorem `separatingFamily_detects_nonfactorization`；同一 final run。 | 分离性是前提；不从非单射单独推出任意固定观察失败。 |
| C-66 | 若 identity 观察 `R→R` 通过 `abstract:R→A` 因子化，则 `abstract` 单射。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `MP-ERCF-001` theorem `identityObservation_factors_implies_injective`；同一 final run。 | 只说明包含 identity 的全观察充分性排除信息合并；不自动给等价、满射或现实解释。 |
| C-67 | 对 Cubical Agda 原生 squash HIT `∥ A ∥₁`，若 `P` 是 mere proposition，则任意 `A→P` 可扩张为 `∥ A ∥₁→P`。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `MP-ERCF-TRUNC-001` 的 `protectedRecursor`；Agda 2.8.0 + Cubical v0.9 final run。 | 只允许给出 `isProp P` 的目标；不提供一般 witness-valued extraction。 |
| C-68 | 二重命题截断可由受保护 recursor 压平为单次截断，并在 point constructor 上按 `refl` 满足 β。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `flattenTruncation`、`flattenTruncation-β`；同一 Cubical Agda run。 | 只恢复单次截断层的信息，不恢复原始 `A` witness。 |
| C-69 | 任意 `f : ∥ Bool ∥₁ → Bool` 都满足 `f ∣ false ∣₁ ≡ f ∣ true ∣₁`。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `truncatedBoolMapIsConstant` 对 `squash₁` 使用 Cubical `congS`；同一 run。 | 不声称不存在从 `∥ Bool ∥₁` 到 `Bool` 的常值函数；只证明所有输入点输出 path-equal。 |
| C-70 | 不存在同时给出 `extract : ∥ Bool ∥₁ → Bool` 和逐点保持律 `(b:Bool)→extract ∣b∣₁≡b` 的 consumer。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED / DEFENSE_WORKS` | `noPointPreservingBoolExtraction`：squash 路径经 `extract` 导出 `false≡true`，与 `false≢true` 矛盾；同一 run。 | 这是截断接口正确阻断“mere existence→原 witness”的防御，不是 HoTT 内部矛盾、现实相对悖论或一般全局选择否定。 |
| C-71 | 若 `p ≈ p'` 且 `f`、`g` 逐点结果等价，则 `bind p f ≈ bind p' g`。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `MP-RACE-TIMEOUT-001` 的 `bind-cong`；Agda 2.8.0 + Cubical v0.9 final run。 | 只覆盖本目录固定的确定性 delay 模型与 R041 `bind` 子句；不等于一般单子律或 QIIT 商结论。 |
| C-72 | 对固定 continuation `f`，`bind` 下降到集合商 `Delay A / ≈`，且在代表层满足 β。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `bind-descends`、`bindQ`、`bindQ-β`；使用 Cubical `SetQuotients` 的 `rec`。 | 固定代表函数 `f` 的下降；不构造 `Q(A)×(A→Q(B))→Q(B)` 一般商单子（R041 §2.1 的限制保留）。 |
| C-73 | `p0 = now true`、`p2 = δδ now true`、`q1 = δ now false`：`p0 ≈ p2` 但 `race p0 q1` 与 `race p2 q1` 不等价。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `race-noncongruent`；左右胜者分别由 `leb` 归约确定。 | 只说明 `race` 不尊重 `≈`；不证明所有竞争语义或所有平局政策都不可下降。 |
| C-74 | `deliver(true)=now true, deliver(false)=ω` 下，`Composed = bind(race(·,q1), deliver)` 使 `Composed p0` 返回而 `Composed p2` 发散，故二者不等价。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `completion-gap`。 | 完成性差异是本模型内的过程反差；不把它升级为现实并发系统失配。 |
| C-75 | `deadline 1 p0 = some true` 而 `deadline 1 p2 = none`，截止期 consumer 分离同一等价对。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `deadline-separation`。 | 超时返回 `none` 只表示截止期内未取得结果，不证明原过程发散。 |
| C-76 | 不存在 `r : Q Bool → Q Bool → Q Bool` 使 `r [p] [q] ≡ [race p q]` 对所有 `p q` 成立。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `no-quotient-race`，经 `effective`（`≈` 为命题值等价关系）反推，与 `C-73` 矛盾。 | 商上不存在 race 选择子；不证明商没有其他（如携带时序数据的）细化结构。 |
| C-77 | 在 R041 delay 片段上，`≡c`（全部固定上下文保持结果等价，且叠加 deadline 观察不可区分）是等价关系。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `MP-CONTEXTUAL-EQUIV-001` 的 `≡c-refl`、`≡c-sym`、`≡c-trans`；Agda 2.8.0 + Cubical v0.9 final run。 | 只覆盖本文件固定的 `Ctx`（hole/bind/两侧 race）与 deadline 观察族。 |
| C-78 | `≡c` 精化结果等价：`p ≡c q → p ≈ q`（取空上下文的结果观察）。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `≡c-to-≈`；同一 run。 | 只给“上下文等价蕴含结果等价”一个方向；反向被 `C-83` 否证。 |
| C-79 | `¬ (ret (suc n) a ≡c ret zero a)`：deadline 0 区分“至少晚一步返回”与“立即返回”。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `deadline-zero-separates`；同一 run。 | 只分离 0 步与 ≥1 步；更一般的严格时间差由 `C-82` 给出。 |
| C-80 | `¬ (ret n a ≡c ω)`：与 ω 竞争的上下文区分“返回”与“发散”。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `divergence-separates`；同一 run。 | 不证明一般发散判定的可判性；只给出本片段中的区分上下文。 |
| C-81 | 若 `a ≠ b`，则 `¬ (ret n a ≡c ret n b)`：延续 `x ↦ ret 0 (not x)` 分离同刻不同值。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `value-separates`；同一 run。 | 使用 Bool 上的 `not` 作为值移动延续；不主张对任意值类型都有类似延续。 |
| C-82 | 若 `lt n m ≡ true`，则 `¬ (ret n a ≡c ret m a)`：时间对齐 race 上下文分离严格更晚的返回。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `lt-timing-separates`，配合 `leb-refl`、`lt-leb`；同一 run。 | 假设形式是 Bool 计算 `lt n m ≡ true`，不是对象语言顺序公理。 |
| C-83 | `(p0 ≈ p2) × ¬ (p0 ≡c p2)`：结果等价严格粗于上下文等价。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED / REPRESENTATION_BOUNDARY` | `result-coarser-than-contextual`；同一 run。 | 这是本固定上下文族下的层次定理；不证明所有可能上下文语言都如此，也不构成 HoTT 内部矛盾。 |
| C-84 | `≈`-商 `Q A` 有 canonical section：`sec [ p ] ≡ canon p`，`[ sec x ] ≋ x`；`Delay A` 在 `A` 为集合时是集合。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `MP-QUOTIENT-MONAD-001` 的 `isSetDelay`、`canon-respects`、`sec`、`sec-section`；Agda 2.8.0 + Cubical v0.9 final run。 | section 依赖"每类有可定义最小代表"这一片段性质；不推广到一般商。 |
| C-85 | 商值 continuation bind `bindQQ : Q A → (A → Q B) → Q B` 存在，且 `bindQQ [ p ] ([_] ∘ f) ≋ [ p bind f ]`。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `bindQQ`、`bindQQ-β`；同一 run。 | 只给出该构造与代表层相容性；单位律与关联律分别由 C-86/C-88 覆盖。 |
| C-86 | 左单位 `bindQQ [ ret 0 a ] f ≋ f a`；右单位 `bindQQ q ([_] ∘ (λ a → ret 0 a)) ≋ q`。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `bindQQ-left-unit`、`bind-unit-≈`、`bindQQ-right-unit`；同一 run。 | 是商层等式（模 `≋`），不声称语法层归一。 |
| C-87 | 代表层关联律（模 `≈`）：`((p bind f) bind g) ≈ (p bind (λ a → f a bind g))`。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `bind-later-eq`、`later-≈-cong`、`bind-iterLater-≈`、`bind-assoc-≈`；同一 run。 | 只到 `≈`（结果等价）；商层版本由 C-88 给出。 |
| C-88 | 商层关联律：`bindQQ (bindQQ q f) g ≋ bindQQ q (λ a → bindQQ (f a) g)`。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED / MONAD_STRUCTURE_CONSTRUCTED` | `assocQ-β`、`assocQ`（用 C-84 的 section 改写）；同一 run。 | 单子结构仅在本片段（可分裂商）成立；不证明一般商上的同类结构。 |
| C-89 | `lt` 三分律：`(n ≡ m) ⊎ ((lt n m ≡ true) ⊎ (lt m n ≡ true))`。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `MP-CONTEXT-CHARACTERIZATION-001` 的 `lt-trichotomy`；Agda 2.8.0 + Cubical v0.9 final run。 | 是 Bool 计算层面的三分，不是对象语言全序公理。 |
| C-90 | 一般严格时间分离：`¬ (n ≡ m) → ¬ (ret n a ≡c ret m a)`。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `timing-separates`（用 `C-89` 与 `lt-timing-separates`）；同一 run。 | 只对同值同型的 canonical 返回；不覆盖不同值情形（由 C-91 内部处理）。 |
| C-91 | 完整刻画：`(p q : Delay Bool) → (p ≡c q) ⇔ (p ≡ q)`。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED / CONTEXTUAL_EQUIVALENCE_FULLY_CHARACTERIZED` | `≡c-iff-≡`（含 `deadline-lt/gt-separates`、`same-time-values`）；同一 run。 | 只覆盖 Bool 片段与固定上下文族；代表相等已是最细，故任何上下文扩展不能区分更多（该结论限于本片段）。 |
| C-92 | 若忘却翻译 `g` 同时满足阶段不变性与保更新律，则 `f` 有不动点（`Σ x, x ≡ f x`）。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `MP-GUARD-ERASURE-001` 的 `collapse-forces-fixed-point`；Agda 2.8.0 + Cubical v0.9 final run。 | 条件式结论：只在"同时要求两条"时成立；不否定其它形式的抽象。 |
| C-93 | `X = Bool`、`f = not` 时不存在保律的阶段擦除翻译。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `no-collapse-for-negation`（用 `no-fixed-point-of-not`）；同一 run。 | 只针对否定律；常值/幂等律的反例见 `C-94`。 |
| C-94 | 任何不动点 `x₀` 给出常值翻译 `const x₀`，同时满足阶段不变性与保更新律。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `collapse-exists-if-fixed-point`；同一 run。 | 正向控制：说明 `C-92/C-93` 的障碍是具体的、非空泛的。 |
| C-95 | 振荡轨道 `orbit (suc n) = not (orbit n)` 在源演算中可实现，且 `¬ (orbit 0 ≡ orbit 1)`。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `orbit-law`、`orbit-stages-differ`、`oscillating-orbit`；同一 run。 | 只说明该具体轨道的阶段可观察；不主张物理时间或现实过程。 |
| C-96 | 对任意 `k`：`fun fast ≡ fun (slow k)` 且 `¬ (cost fast 0 ≡ cost (slow k) 0)`。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `MP-COST-FACTORIZATION-001` 的 `same-function-different-cost`；Agda 2.8.0 + Cubical v0.9 final run。 | `cost` 是明示语法导向计数；不主张真实编译器/硬件成本。 |
| C-97 | 不存在能区分两个外延相等程序的裸函数谓词。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `no-distinguishing-predicate`（funext 路径 + transport）；同一 run。 | 只针对由 funext 得到等式的程序对；不否定显式携带成本的表示。 |
| C-98 | 不存在从裸函数恢复成本值的 consumer `r : (ℕ→ℕ) → ℕ`。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `no-cost-value-recovery`（C-97 的谓词实例）；同一 run。 | 是"该形状 consumer 不存在"的必要性结论；自然性判断不在本 claim 内。 |
| C-99 | 细化表示可恢复成本且能区分两个程序。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `refined-cost-recovery`、`refined-separates`；同一 run。 | 正控制仅说明"补回成本分量即可恢复"；不证明一般表示选择最优。 |
| C-100 | `transport (ua notEquiv) ≡ not`（单价路径按等价计算）。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `MP-PATH-CERTIFICATE-001` 的 `ua-move-computes`、`ua-move-is-not`（`uaβ`）；Agda 2.8.0 + Cubical v0.9 final run。 | 只覆盖 Bool 取反等价；不主张单价性独立公理选择。 |
| C-101 | `∥ Bool ≡ Y ∥₁` 是命题，且 `∥ Bool ≡ Bool ∥₁` 有元素。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `H-is-prop`、`H-inhabited`（`squash₁`）；同一 run。 | 截断命题性不提供具体路径或选择函数。 |
| C-102 | 固定端点弱接口 `∥ Bool ≡ Bool ∥₁ → Bool → Bool` 存在。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `fixed-pair-interface`；同一 run。 | 只处理固定载体；不承担全宇宙自然性。 |
| C-103 | 固定源统一变体 `(Y : Type) → ∥ Bool ≡ Y ∥₁ → Bool → Y` 不可栖居。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `no-fixed-source-mere-move`（Σ回路 + `fromPathP` + `uaβ`）；同一 run。 | 依赖截断是命题这一规则；不把固定端点反例扩大化。 |
| C-104 | `MereMove := (X Y : Type) → ∥ X ≡ Y ∥₁ → X → Y` 不可栖居。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `no-mere-move`（`C-103` 的推论）；同一 run。 | 只排除该全宇宙相干统一选择；不排除所有局部实例。 |
| C-105 | 路径版接口 `(X ≡ Y) → X → Y` 由 `transport` 构造。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `path-move`；同一 run。 | 有路径即有迁移；是否保留时限/成本是额外任务。 |
| C-106 | 不存在在时刻 0 读出第二个输入的在线策略。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `MP-ONLINE-CAUSALITY-001` 的 `no-zero-time-lookahead`；Agda 2.8.0 + Cubical v0.9 final run。 | 只针对"时刻 n 只读前缀"的在线模型；不排除离线/完整知识版本。 |
| C-107 | 第一个输入在时刻 0 即可在线读取。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `first-input-online`、`readFirst`、`first-correct`；同一 run。 | 正控制；不说明其它任务可在线完成。 |
| C-108 | 第二个输入从时刻 1 起可在线读取。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `second-input-online-later`、`readSecond`；同一 run。 | 在线资格与时刻和任务都相关。 |
| C-109 | 完整流函数 `s ↦ s 1` 存在且正确，但时刻 0 在线策略不存在。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED / ONLINE_CAUSALITY_BOUNDARY_WITH_POSITIVE_CONTROLS` | `complete-second`、`complete-second-correct`、`knowledge-gap`；同一 run。 | 是"完整知识 ≠ 在线资格"的边界判据；不构成 HoTT 内部矛盾。 |
| C-110 | 固定三状态过程从 `a` 经两步到达 `d`，且 `d` 无出边。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `C-110-terminates`、`C-110-d-terminal`；`MP-TRANSITION-LIFT-001` 的 Agda 2.8.0 + Cubical v0.9 final run。 | 只覆盖该固定有限模型；不推出一般终止性。 |
| C-111 | 存在像 `E` 在 `w` 上有自环，且常值路径给出任意长的抽象运行。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `C-111-e-ww`、`C-111-e-wW`、`C-111-beta-path`；同一 run。 | `E` 是 may 过近似；抽象无限路径不证明具体发散。 |
| C-112 | 抽象两步前缀 `w,w,w` 在抽象上有证据，但从初态 `a` 没有相容具体提升。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `C-112-abstract-two-www`、`C-112-no-lift-two`；同一 run。 | 只排除该两步前缀的统一提升；不排除每一条边可单独提升。 |
| C-113 | 不存在把每个 `E(α s, v)` 变为 `C(s, v)` 的当前态提升函数；见证在 `(b,w)`。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `C-113-no-current-lift`；同一 run。 | 不排除携带额外代表或时序信息的更宽接口。 |
| C-114 | `A k = Σ m, k ≤ m` 的精确相容极限为空。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `C-114-LimA-empty`；同一 run。 | 只覆盖该塔；不使用 LEM 或选择。 |
| C-115 | 同一塔逐层截断后的相容极限有元素。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `C-115-limTrunc`；同一 run。 | 逐层命题性由截断提供；不外推到非命题塔。 |
| C-116 | 不存在从截断极限回到精确极限的函数（故比较映射无逆）。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `C-116-no-inverse`；同一 run。 | 只排除该方向的反函数；不否定前向比较映射。 |
| C-117 | 不存在同时在 `R` 上严格下降、在 `α` 纤维上恒定的自然数等级。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `C-117-no-descending-fiber-constant-rank`；同一 run。 | 是该固定合并的反例；一般图的等级判据仍为 paper + finite。 |
| C-118 | 代表层 strict 分类器 `P0 : A → Delay Bool` 存在。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `C-118-P0`；`MP-PARTIAL-DECISION-001` 的 Agda 2.8.0 + Cubical v0.9 final run。 | 只覆盖该固定有限模型；不推出一般分类器存在性。 |
| C-119 | strict 观察区分 `now` 与 `later`。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `C-119-strict-separates`；同一 run。 | 只针对该 delay 片段的构造子区分。 |
| C-120 | 不存在 strict `g : Q → Delay Bool` 同时满足 `g [a] ≡ now true` 与 `g [b] ≡ later (now true)`。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `C-120-no-strict-quotient`（`[a]≡[b]` 迫使 `now true ≡ later (now true)`）；同一 run。 | 只排除该 strict 扩展；不排除 up-to-≈ 版本。 |
| C-121 | `P0` 到 `R_D` 意义下不变，故存在 partial classifier `P : Q → D≈`。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `C-121-partial-classifier`；同一 run。 | 是正控制；`D≈` 是最小 delay 商，不是完整 partiality monad。 |
| C-122 | 不存在 strict `Bool` 消费者 `h : Q → Bool` 同时取 `h [a] ≡ true`、`h [b] ≡ false`。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `C-122-no-strict-consumer`；同一 run。 | 只排除该 strict 消费者；携带代表或额外时序数据可恢复。 |
| C-123 | 代表层 strict 消费者存在并区分 `a,b`；信息只在商化时丢失。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `C-123-representative-consumer`；同一 run。 | 是该固定商的反例；不推出一般表示边界。 |
| C-124 | `transport (ua notEquiv) true ≡ false`，且点结构 `(Bool,true)` 与 `(Bool,false)` 由原生路径识别。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `C-124-ua-transport`、`C-124-identification`；`MP-SIP-REPRESENTATION-001` 的 Agda 2.8.0 + Cubical v0.9 final run。 | 是该点结构 SIP 实例；不构造一般结构范畴 SIP。 |
| C-125 | 签名外可观察量在两个结构上不同。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `C-125-obs-differs`；同一 run。 | 可观察量需要额外“carrier 是 Bool”表示数据，不是 `Str → Bool` 全函数。 |
| C-126 | 任意 `f : Str → Bool` 都被识别强制在 `s,t` 上相等。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `C-126-any-function-constant`；同一 run。 | 只针对该识别；不排除带额外表示数据的消费者。 |
| C-127 | 不存在统一恢复 `f : Str → Bool` 同时取 `f s ≡ true`、`f t ≡ false`。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `C-127-no-recovery`；同一 run。 | 是 SIP/UA 表示边界；不证明真实库存在错误消费者。 |
| C-128 | 细化结构把可观察量纳入签名：投影区分两点，且 `¬ (s' ≡ t')`。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `C-128-obs'-differs`、`C-128-no-identification`；同一 run。 | 正控制；只说明“加入签名后恢复”，不推广到任意富化。 |
| C-129 | 按极限值取商的 Cauchy 商允许 limit 函数 `Q → Bool` 下降。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `C-129-limit`；`MP-CAUCHY-MODULUS-001` 的 Agda 2.8.0 + Cubical v0.9 final run。 | 只覆盖该最小序列模型；不构造完整实数。 |
| C-130 | 同一常值序列的两个表示（modulus 0 与 1）被商识别，但其 modulus 不同。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `C-130-related`、`C-130-moduli-differ`；同一 run。 | 只说明给定 modulus 属于表示数据。 |
| C-131 | 不存在 `f : Q → ℕ` 统一恢复每个表示的给定 modulus。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `C-131-no-modulus-recovery`；同一 run。 | 不排除携带额外 modulus 数据的消费者。 |
| C-132 | 把 modulus 纳入同一性判据后，细化商有 `Q' → ℕ` 的 modulus 函数。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `C-132-modulus-refined`；同一 run。 | 正控制；不改写原商语义。 |
| C-133 | 细化关系不识别两个表示：`¬ (c0 ≈' c1)`。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `C-133-refined-not-related`；同一 run。 | 只覆盖该最小关系；不推出一般 Cauchy 商的性质。 |
| C-134 | 任意源 `A`、集合 `S`、实现 `h : A → S` 与读出 `g : ∥ A ∥₁ → S`：若 `g` 在每个 point constructor 上与 `h` 一致，则任意两点 `h a₀ ≡ h a₁`。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `pointConstructorsForceEquality`；`MP-TRUNC-NORECOVERY-001` 的 Agda 2.8.0 + Cubical v0.9 final run。 | 目标必须是集合（路径类型才是命题）；不推出非集合目标的同类结论。 |
| C-135 | 若 `h` 分离 `x₀` 与 `x₁`，则不存在同时逐点保持的读出与一致性证明。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `noPointRecovery`；同一 run。 | 不声称所有 `∥ A ∥₁ → A` 都不存在；只排除带逐点恢复合同的读出。 |
| C-136 | `extract : ∥ Bool ∥₁ → Bool` 不可能同时满足 `extract ∣ b ∣₁ ≡ b`。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `boolRecoveryImpossible`；同一 run。 | 与 C-70 同向；本包给的是族群化证明路径，不主张原创性。 |
| C-137 | 同一定理对 `ℕ` 成立（分离对 0/1）。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `ℕRecoveryImpossible`；同一 run。 | 说明障碍非二元目标假象；不推广到非集合值域。 |
| C-138 | 当目标是 mere proposition 时，`rec Pprop f` 形式的消费者存在。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `propositionValuedTestExists`；同一 run。 | 正控制；不表示可以恢复见证身份。 |
| C-139 | `Bool` 的 section-candidate 类型为空：不存在同时逐点保持的 `P : ∥ Bool ∥₁ → Bool`（理论的内部否定形式）。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `noSectionCandidate`；`MP-TRUNC-NORECOVERY-001` 的 Agda 2.8.0 + Cubical v0.9 final run `-02`。 | 与 C-136 同向的改写；不新增独立强度，不证明理论内部矛盾。 |
| C-140 | 一般分离实现下 completion-candidate 类型为空（应用形式，分离见证由消费者提供）。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `noCompletionCandidate`；同一 run `-02`。 | 不推广到非集合目标；不声称现实中不存在完成过程。 |
| C-141 | 对 `isFinSet` 形状的库接口（`Σ n × ∥ A ≃ Fin n ∥₁`），不存在统一读出具体枚举的 pick 函数：任何逐点保持的 `pick : ∥ E ∥₁ → E` 迫使被读出的两个枚举相等。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `isFinSetLikeNoUniformEnumeration`；`MP-TRUNC-NORECOVERY-001` 的 Agda 2.8.0 + Cubical v0.9 final run `-03`。 | 这是接口形状的边界，不是“某个库误用接口”的实例；E6 未因此成立。 |
| C-142 | unlabeled 二元素呈现 `Σ A × ∥ A ≃ Bool ∥₁` 上存在由 swap 自同构 `notEquiv` 诱导的非平凡自识别 `swapSelfIdentification : identityPresentation ≡ identityPresentation`：carrier 分支为 `ua notEquiv`（非平凡性见 C-148），标签分支由截断的命题性填满。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `swapSelfIdentification`；`MP-NOCANONICAL-001` 的 Agda 2.8.0 + Cubical v0.9 final run `-02`。 | 依赖 univalence 与截断命题性；不声称该识别唯一，也不外推到标签未截断的接口。 |
| C-143 | 该族的任何 section 必须尊重族自身的识别：`subst unlabeledCarrier swapSelfIdentification (u X) ≡ u X`。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `sectionRespectsSelfIdentification`；同一 run。 | 这是相干义务的形式化；不声称任何具体 section 存在。 |
| C-144 | 任何假想的统一选点被强制为 `not` 的不动点：`not (u X) ≡ u X`。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `uniformChoiceFixedPoint`；同一 run。 | 依赖 `uaβ notEquiv` 的计算规则；与 C-145 合取才得出矛盾。 |
| C-145 | 不存在对所有 unlabeled 二元素呈现的统一选点：`((X : UnlabeledTwoElement) → unlabeledCarrier X) → ⊥`；与 agda-unimath `no-section-type-2-Element-Type` 同内容。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `noUniformChoice`；同一 run。 | 是该固定呈现类在固定工具链下的否定；不外推到含标签接口或其它“二元素类型”概念，也不证明任何库误用该接口。 |
| C-146 | 保留标签数据（`Σ A × (A ≃ Bool)`）时存在规范选点：围栏来自被遗忘的标签，而非二元素载体。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `labeledChoice`；同一 run。 | 正控制；不声称任何自然消费者在未声明假设下使用该接口。 |
| C-147 | 界面把 id-标签与 swap-标签识别为一（`labelingsIdentified`），而二者作为标签数据仍不同（`labelingsDistinct`）：截断遗忘的正是具体识别。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `labelingsIdentified`、`labelingsDistinct`；同一 run。 | 不推出任何库误用；不把识别升级为“标签不存在”。 |
| C-148 | 该自识别的 carrier 分支不是恒等路径：`ua notEquiv ≡ refl → ⊥`，故自识别是非平凡的。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `uaNotEquivNotRefl`；同一 run `-02`。 | 只针对该具体自同构；不推出一般完整群的非平凡性判据。 |

## 当前允许的总论断

> 对一个明确的表示/忘却映射，凡在其纤维上变化的目标信息，都不能仅由该表示精确、统一地
> 恢复；方向、来源、意图、成本或时间结构若被忘掉，就必须通过额外结构重新提供。当前研究
> 以 `Z_STRONG_PHILOSOPHICAL_LAW`“理论抽象必然导致悖论”为最高原则；proper abstraction、
> 非因子化以及 formation/reality promotion 是其技术核心。HoTT 不负责确认该项目原则，而负责
> 提供一个合法、尤其涉及时间否定的具体非现实实例。同函数异时是第一候选，
> Guard-Erasure 的 HoTT 特定翻译开放。Russell 在用户数学哲学中是 formation/temporality 中心实例：
> `rₙ₊₁=¬rₙ` 不落定，合法 validator 应拒绝形成，朴素静态集合本体的失败是先把 specification
> 提升为完成集合。标准 HoTT 的 identity/groupoid 层本身不提供无标签对象的
> 规范方向，但这既不是 HoTT 的内部矛盾，也不阻止显式编码顺序、动力学、cost 或时间系统。

这个表述是“表示相对限制”，不是“理论绝对失败”。

## Git 版本闭合登记（2026-09-13）

本节是当前 Git 可恢复性维度的唯一登记，不改写上面的 frozen proof/claim 行。上表中的
`MACHINE_PROVED_LOCAL_UNCOMMITTED` 与 `REPLAYED_EXTERNAL_LIBRARY_WITH_SCOPE` 是各 run 建立索引时的
证据状态文本，已被 `index-row-manifest.json` 固定；把它们原位改成新状态会破坏历史 run 的逐行收据。

当前 Git 维度如下：

- proof source、final/superseded run、索引行与 S090/S091 治理修复已进入 commit
  `d3dfb0e1869f5f05527f23ef4cb05dc95352eb10`；tree
  `e78cfa44f086cb0d6bb6fae75837deedfa920e21`；
- 该 commit 中本矩阵为 58,897 bytes / 210 行，SHA-256
  `e598228bb3c04f2a84cece955680381b16fb92f140c336abe0da2e6f4b6e7a18`；
- 当前文件只在其后 append 本登记，旧行保持逐字前缀；现有 run 因索引演进应显示
  `ROW_STABLE_AFTER_INDEX_EVOLUTION`，数学 proof source/run 未被改写；
- 当前 17 个 package 的 Git 状态由 `HoTT/verification/PROOF_VERSION_CLOSURE.json` 统一解释为
  `MACHINE_PROVED_VERSION_CLOSED`；外部 C-05 为
  `MACHINE_REPLAYED_EXTERNAL_LIBRARY_VERSION_CLOSED_WITH_SCOPE`；
- `governance-v3.2.0` 是本轮治理 release ref；数学资产的 version closure 已由上述 exact commit
  满足，不依赖把历史 RUN.json 改写成新状态。

特别边界：C-145 行中的“与 agda-unimath 同内容”只保留为当时的非正式对照措辞；S090 已明确项目
没有机器证明本地 Cubical/Type₀ 规格与外部 universe-polymorphic without-K 规格的保真翻译或等价。
真正的外部源码重放只有 `MP-UNIMATH-NOSECTION-REPLAY-001` / C-05。

## 追加登记：MP-VERIFICATION-EVENT-001（外部导入 + 项目内重放，2026-09-13）

> 本节按 `verify_proof_version_closure.py` 的冻结前缀要求**追加在文末**；不改写 d3dfb0e 快照的任何字节。
> 精确范围与禁止外推见 `HoTT/formal/verification-event/README.md` 与 `audit/verification-event吸收与独立核验-20260913.md`。

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-VERIFICATION-EVENT-001` | `C-149`–`C-156` | `formal/verification-event/VerificationEvent.agda`（外部独立来源：`audit/imports/verification-event-20260913-01a099e9/`，本地 ID `EVT-01`–`EVT-08`） | `verification/runs/20260913-MP-VERIFICATION-EVENT-001-01/`；Agda 2.8.0-3d04bac；Cubical v0.9 载入命令（证明本身只用 Agda 内建 Cubical 原语，未导入 `Cubical.*`）；`--safe --cubical --ignore-interfaces`；exit 0；负向校准 `BadCast.agda` 由 `audit/imports/.../project-negative-probe/` 与外部 `negative-002` 两份收据固定 | `MACHINE_PROVED_LOCAL_UNCOMMITTED / VERIFICATION_EVENT_STAGE_BOUNDARY_WITH_POSITIVE_CONTROL` |

| ID | 主张 | 裁决 | 直接依据 | 禁止外推 |
|---|---|---|---|---|
| C-149 | 两个 Step 构成明确事件链：`twoEventTrace : Step initial afterP × Step afterP afterHistory`。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `twoEventTrace`；`MP-VERIFICATION-EVENT-001` 的 final run `20260913-MP-VERIFICATION-EVENT-001-01`（本地 ID `EVT-01`）。 | 明示的有限事件模型，不是真实设备或真实验证流程的轨迹。 |
| C-150 | 该有限登记规则健全：`∀ s c → K s c → Meaning s c`。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `knowledgeSound`；同一 run。 | 只证明此有限注册规则，不证明 HoTT 自身全局健全性。 |
| C-151 | 固定原子与定义下：`Current initial` 成立，`Current afterP` 与 `Current afterHistory` 均为空，`decideCurrent` 对应 true/false。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `currentInitial`、`noCurrentAfterP`、`noCurrentAfterHistory`、`decideCurrent`；同一 run。 | 只针对该状态、原子与定义；不是一般知识的判定算法。 |
| C-152 | 后来可以登记并核查固定的过去：`K afterHistory historical`、`Historical`、`historicalKnownLater`。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `historicalKnownLater` 等；同一 run。 | 只说明“后来可核查固定过去”；不声称当前仍未知。 |
| C-153 | 不存在把固定过去改写成当前判断的转换：`¬ (Historical → Current afterP)`，且 `¬ (Current initial ≡ Current afterP)`（原生 Path 不可得）。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `noHistoricalToCurrentAfterP`、`noCurrentPath`；同一 run。负向校准：`project-negative-probe`（exit 42、`BadCast.agda:10`、`afterP != initial`）与外部 `negative-002`。 | 不说明任意不同时标命题都不同；只否定这一次“过去→当前”的改写。 |
| C-154 | 在 `Trunc Stage` 上不存在与每个 `Current s` 双向对应的谓词族（完全阶段擦除不保真）。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `noStageErasingFamily`；同一 run。 | 只否定这一次完全阶段擦除的双向保真，不证明所有抽象都会丢掉阶段信息。 |
| C-155 | 保留阶段时有正向控制：`∀ s → Current s → stageAwareFamily s`（`stageAwareIdentity`）。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `stageAwareFamily`、`stageAwareIdentity`；同一 run。 | 正控制；不证明任何现实模型充分。 |
| C-156 | 在显式 factivity 与 conjunction-closure 参数下，`Know (A × ¬ Know A) → Empty`（`noKnownMoore`）。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `noKnownMoore`；同一 run。 | 不是完整 Fitch/Gödel 定理，也不证明 HoTT 存在这种全域 Know 算子。 |

## 追加登记：MP-ERCF3-T3-JOINT-001（ERCF-3 T3 第十四脉冲，2026-09-13）

> 本节按 `verify_proof_version_closure.py` 的冻结前缀要求**追加在文末**；不改写 d3dfb0e 快照或既有追加节的任何字节。
> 精确范围与禁止外推见 `HoTT/formal/ercf3-t3/README.md` 与 run `20260913-MP-ERCF3-T3-JOINT-001-02` 的 `RUN.json`。
> 该包**不改变** ERCF-3 的 gated 状态：它只闭合编码层的替换/编码一致义务（C8 §9 的 P2/P3 层），不涉及证明谓词表示性、反射或对角线不动点。

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-ERCF3-T3-JOINT-001` | `C-157`–`C-159` | `formal/ercf3-t3/JointRecursion.agda`（依赖 `ObjectSyntax.agda`、`DiagonalCore.agda`、`DiagonalLemma.agda`、`CodeStoreFix.agda`、`MutualInduction2.agda`、`DecisionParam.agda`；全部按 run 的 `source-manifest.json` 哈希固定） | `verification/runs/20260913-MP-ERCF3-T3-JOINT-001-02/`；Agda 2.8.0-3d04bac、Cubical v0.9 库声明、仅 Agda builtins；exit 0、stderr 0；`-01` 为 `--safe` pragma 触发 `CoInfectiveImport` 的失败尝试（保留）；工具链 `formal/ercf3-t3/TOOLCHAIN.json` | `MACHINE_PROVED_LOCAL_UNCOMMITTED / ERCF3_T3_SHARED_DECISION_JOINT_RECURSION` |

| ID | 主张 | 裁决 | 直接依据 | 禁止外推 |
|---|---|---|---|---|
| C-157 | 对显式共享判定 `d`，码级修正替换与语法级共享判定替换一致：`(d : Bool) (k i : Nat) (t : Tm) → substFixTd d k i t ≡ codeT (substTd d k i t)`。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `substFixTd-agrees`；run `20260913-MP-ERCF3-T3-JOINT-001-02`。 | 只覆盖显式判定版本的两种替换；不涉及证明谓词 `P`、反射、对角线不动点或 ERCF-3 本体。 |
| C-158 | 原始逐出现判定的**项层恒等式**成立：`(k i : Nat) (t : Tm) → substFixT k i t ≡ codeT (substT k i t)`（即 N34 记录的剩余义务在项层被联合递归收口）。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `fixT-agrees`；同一 run。 | 只到项层；公式层的量词/影子分支另见 C-159；不证明对象层替换算术化（对角引理本体）。 |
| C-159 | 修正后的公式层码替换与语法替换一致：`(k i : Nat) (φ : Fml) → substFixFc k i φ ≡ codeF (substF k i φ)`；`substFixFc` 修正了 `CodeStoreFixF.substFixF` 在 `all` 影子分支把 `codeF φ` 误写为 `codeF (all m φ)` 的双重编码错误；既有脉冲文件逐字节未改。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `substFixFc`、`fixF-agrees`；同一 run；错误与修正说明见 `formal/ercf3-t3/README.md`。 | 修正只在该新模块中给出；不重写历史脉冲与其会话证据；不改变 ERCF-3 的 gated 状态或任何既有判词。 |

## 追加登记：MP-ERCF3-T3-DECODING-001（T3 decodability/injectivity fence，2026-09-13）

> 本节按 `verify_proof_version_closure.py` 的冻结前缀要求**追加在文末**；不改写 d3dfb0e 快照或任何既有追加节的字节。
> 精确范围与禁止外推见 `HoTT/formal/ercf3-t3/README.md` 与 run `20260913-MP-ERCF3-T3-DECODING-001-01` 的 `RUN.json`。
> 该包只覆盖**前置条件 (a) 的编码可解码性缺口**；不进入 ERCF-3 本体（P 表示性/反射/对角不动点），`GATED` 状态不变。

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-ERCF3-T3-DECODING-001` | `C-160`–`C-162` | `formal/ercf3-t3/DecodingFence.agda`（依赖 `ObjectSyntax.agda`、`DiagonalCore.agda`、`DiagonalLemma.agda`；按 run 的 `source-manifest.json` 哈希固定） | `verification/runs/20260913-MP-ERCF3-T3-DECODING-001-01/`；Agda 2.8.0-3d04bac、Cubical v0.9 库声明、仅 Agda builtins；exit 0、stderr 0；工具链 `formal/ercf3-t3/TOOLCHAIN.json` | `MACHINE_PROVED_LOCAL_UNCOMMITTED / ERCF3_T3_DECODABILITY_FENCE` |

| ID | 主张 | 裁决 | 直接依据 | 禁止外推 |
|---|---|---|---|---|
| C-160 | 具体编码在项层**不是单射**：`codeT (var 2) ≡ codeT (num 0)` 而 `var 2 ≢ num 0`，因此不存在 `(t u : Tm) → codeT t ≡ codeT u → t ≡ u` 的单射解码器（`no-injective-codeT`）。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `var2-num0-collide`、`var≢num`、`no-injective-codeT`；run `20260913-MP-ERCF3-T3-DECODING-001-01`。 | 只针对 `DiagonalCore` 的具体编码；不推出任何编码都不单射，也不改变 ERCF-3 状态。 |
| C-161 | 同一碰撞提升到公式层：`codeF (var 2 =f var 2) ≡ codeF (num 0 =f num 0)` 而两条公式不同，故 `codeF` 也不是单射。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `eqVar2-collides-eqNum0`、`varEq≢numEq`、`no-injective-codeF`；同一 run。 | 同上；不声称对角引理不可形式化，只说明当前编码不可解码。 |
| C-162 | 正控制：数字片段的编码在码上单射——`(n m : Nat) → codeT (num n) ≡ codeT (num m) → n ≡ m`；说明碰撞来自构造子标签范围重叠，而不是编码整体失效。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `num-code-injective`；同一 run。 | 正控制只覆盖数字片段；不提供任何修复方案的单射性证明。 |

## 追加登记：MP-ERCF3-T3-REPAIR-SPEC-001（T3 编码修复规格，2026-09-13）

> 本节按 `verify_proof_version_closure.py` 的冻结前缀要求**追加在文末**；不改写 d3dfb0e 快照或任何既有追加节的字节。
> 精确范围与禁止外推见 `HoTT/formal/ercf3-t3/README.md` 与 run `20260913-MP-ERCF3-T3-REPAIR-SPEC-001-01` 的 `RUN.json`。
> 该包把"修复编码"固定为可机器检查的规格；不给出 Nat 值修复编码本身，不进入 ERCF-3 本体（`GATED` 不变）。

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-ERCF3-T3-REPAIR-SPEC-001` | `C-163`–`C-165` | `formal/ercf3-t3/CodingRepair.agda`（依赖 `ObjectSyntax.agda`、`DiagonalCore.agda`、`DiagonalLemma.agda`、`DecodingFence.agda`；按 run 的 `source-manifest.json` 哈希固定） | `verification/runs/20260913-MP-ERCF3-T3-REPAIR-SPEC-001-01/`；Agda 2.8.0-3d04bac、Cubical v0.9 库声明、仅 Agda builtins；exit 0、stderr 0；工具链 `formal/ercf3-t3/TOOLCHAIN.json` | `MACHINE_PROVED_LOCAL_UNCOMMITTED / ERCF3_T3_REPAIR_SPECIFICATION` |

| ID | 主张 | 裁决 | 直接依据 | 禁止外推 |
|---|---|---|---|---|
| C-163 | 结构化（树）编码可解码：`encT : Tm → CodeT`、`decT : CodeT → Tm` 满足 `∀ t → decT (encT t) ≡ t`，故 `encT` 单射（`encT-injective`）。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `encT-roundtrip`、`encT-injective`；run `20260913-MP-ERCF3-T3-REPAIR-SPEC-001-01`。 | 只是**结构**层的正控制；不提供 Nat 值编码，也不解决算术层配对/标签问题。 |
| C-164 | 通用规格引理：对任意目标类型 `A`，若 `c : Tm → A` 存在往返解码器 `dec`（`∀ t → dec (c t) ≡ t`），则 `c` 单射。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `roundtrip-implies-injective`；同一 run。 | 只是"修复"的必要规格；不声称任何具体算术编码满足它。 |
| C-165 | 当前 Nat 编码**不存在解码器**：`Σ (dec : Nat → Tm), (∀ t → dec (codeT t) ≡ t)` 蕴含 `Empty`。这正是"修复编码"义务的精确形式。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `no-decoder-for-codeT`（由 C-164 与 `DecodingFence.no-injective-codeT` 合取）；同一 run。 | 只针对 `DiagonalCore.codeT`；不推出 Nat 值编码不可能，也不改变 ERCF-3 状态。 |

## 追加登记：MP-ERCF3-T3-ARITH-TAGS-001（T3 修复编码的算术半第一片，2026-09-13）

> 本节按 `verify_proof_version_closure.py` 的冻结前缀要求**追加在文末**；不改写 d3dfb0e 快照或任何既有追加节的字节。
> 精确范围与禁止外推见 `HoTT/formal/ercf3-t3/README.md` 与 run `20260913-MP-ERCF3-T3-ARITH-TAGS-001-01` 的 `RUN.json`。
> 只覆盖 var/num 片段的标签不相交算术；不给出应用结点编码与全解码器，不进入 ERCF-3 本体（`GATED` 不变）。

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-ERCF3-T3-ARITH-TAGS-001` | `C-166`–`C-168` | `formal/ercf3-t3/ArithmeticTags.agda`（依赖 `ObjectSyntax.agda`、`DiagonalCore.agda`、`DecodingFence.agda`、`CodingRepair.agda`；按 run 的 `source-manifest.json` 哈希固定） | `verification/runs/20260913-MP-ERCF3-T3-ARITH-TAGS-001-01/`；Agda 2.8.0-3d04bac、Cubical v0.9 库声明、仅 Agda builtins；exit 0、stderr 0；工具链 `formal/ercf3-t3/TOOLCHAIN.json` | `MACHINE_PROVED_LOCAL_UNCOMMITTED / ERCF3_T3_ARITHMETIC_TAGS_FRAGMENT` |

| ID | 主张 | 裁决 | 直接依据 | 禁止外推 |
|---|---|---|---|---|
| C-166 | 偶/奇标签的算术核心：`double` 单射（`(n m : Nat) → double n ≡ double m → n ≡ m`）且 `double n ≢ odd m`（`double n = 2n`、`odd m = 2m+1`），另有 `odd` 单射。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `double-injective`、`double≠odd`、`odd-injective`；run `20260913-MP-ERCF3-T3-ARITH-TAGS-001-01`。 | 只到 `double`/`odd` 两个具体函数；不声称一般模算术引理已形式化。 |
| C-167 | var/num 片段上的 Nat 值编码 `codeAtom`（`avar n ↦ 2n`、`anum n ↦ 2n+1`）**单射**——本链条第一个 Nat 值单射编码。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `codeAtom-injective`；同一 run。 | 只覆盖 var/num 片段；应用结点 `_+t_` 尚未编码，故不声称完整 `Tm` 已有 Nat 值单射编码。 |
| C-168 | 该编码**非满射**：`1` 没有原像（`¬ Σ m, double m ≡ 1`），因此任何**全**解码器必须带缺省分支。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `one-has-no-preimage`；同一 run。 | 只是解码器形态的控制；不构造解码器本身，也不涉及码的语义解释。 |

## 追加登记：MP-ERCF3-T3-BIT-CODING-001（T3 修复编码的算术半第二片：位级底座与燃料界，2026-09-13）

> 本节按 `verify_proof_version_closure.py` 的冻结前缀要求**追加在文末**；不改写 d3dfb0e 快照或任何既有追加节的字节。
> 精确范围与禁止外推见 `HoTT/formal/ercf3-t3/README.md` 与 run `20260913-MP-ERCF3-T3-BIT-CODING-001-01` 的 `RUN.json`。
> 只覆盖位列表的捆绑/抽取与燃料界；不给出符号层、解析器或全解码器，不进入 ERCF-3 本体（`GATED` 不变）。

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-ERCF3-T3-BIT-CODING-001` | `C-169`–`C-172` | `formal/ercf3-t3/BitCoding.agda`（依赖 `ObjectSyntax.agda`、`DiagonalCore.agda`、`DecodingFence.agda`、`CodingRepair.agda`；按 run 的 `source-manifest.json` 哈希固定） | `verification/runs/20260913-MP-ERCF3-T3-BIT-CODING-001-01/`；Agda 2.8.0-3d04bac、Cubical v0.9 库声明、仅 Agda builtins；exit 0、stderr 0；工具链 `formal/ercf3-t3/TOOLCHAIN.json` | `MACHINE_PROVED_LOCAL_UNCOMMITTED / ERCF3_T3_BIT_SUBSTRATE` |

| ID | 主张 | 裁决 | 直接依据 | 禁止外推 |
|---|---|---|---|---|
| C-169 | 数字算术：`(n : Nat) → parity (twice n) ≡ false`、`parity (suc (twice n)) ≡ true`、`half (twice n) ≡ n`、`half (suc (twice n)) ≡ n`（`parity` 取最低位、`half` 折半、`twice n = 2n`）。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `parity-twice`、`parity-suc-twice`、`half-twice`、`half-suc-twice`；run `20260913-MP-ERCF3-T3-BIT-CODING-001-01`。 | 只到三个具体函数（`parity`/`half`/`twice`）；不声称一般二进制算术或 div/mod 已形式化。 |
| C-170 | 捆绑/抽取的两侧引理：`(b : Bool) (c : Nat) → parity (pack b c) ≡ b` 与 `half (pack b c) ≡ c`（`codeBits [] ≡ 1`、`codeBits (b ∷ bs) ≡ pack b (codeBits bs)`）。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `parity-code`、`half-code`；同一 run。 | 只是读取一位的两侧引理；不声称整串抽取正确（那需长度，见 C-171）。 |
| C-171 | 已知长度的往返：`(bs : List Bool) → unbits (LEN bs) (codeBits bs) ≡ bs`。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `unbits-code`；同一 run。 | 长度必须由外部提供；不声称 `unbits` 对任意燃料或任意码都还原原列表。 |
| C-172 | 码支配自身长度：`(bs : List Bool) → suc (LEN bs) ≤ codeBits bs`，因此解析器的燃料可直接取自码本身。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `codeBits-dominates`（辅助 `≤-refl`/`≤-suc`/`≤-trans`/`n≤twice`/`suc≤pack`）；同一 run。 | 只到该界；不给出解析器、符号层或全解码器，也不声称该界是紧的。 |

## 追加登记：MP-ERCF3-T3-STREAMING-PARSER-001（T3 修复编码的算术半第三片：符号层 + 流式解析器 + Nat 值修复编码，2026-09-13）

> 本节按 `verify_proof_version_closure.py` 的冻结前缀要求**追加在文末**；不改写 d3dfb0e 快照或任何既有追加节的字节。
> 精确范围与禁止外推见 `HoTT/formal/ercf3-t3/README.md` 与 run `20260913-MP-ERCF3-T3-STREAMING-PARSER-001-01` 的 `RUN.json`。
> 本包在**编码层**闭合 `CodingRepair` 记录的修复义务（C-163/C-164/C-165）；不进入 ERCF-3 本体（P 表示性/反射/对角不动点），`GATED` 状态不变。

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-ERCF3-T3-STREAMING-PARSER-001` | `C-173`–`C-176` | `formal/ercf3-t3/StreamingParser.agda`（依赖 `ObjectSyntax.agda`、`DiagonalCore.agda`、`DecodingFence.agda`、`CodingRepair.agda`、`BitCoding.agda`；按 run 的 `source-manifest.json` 哈希固定） | `verification/runs/20260913-MP-ERCF3-T3-STREAMING-PARSER-001-01/`；Agda 2.8.0-3d04bac、Cubical v0.9 库声明、仅 Agda builtins；exit 0、stderr 0；工具链 `formal/ercf3-t3/TOOLCHAIN.json` | `MACHINE_PROVED_LOCAL_UNCOMMITTED / ERCF3_T3_REPAIRED_NAT_CODING` |

| ID | 主张 | 裁决 | 直接依据 | 禁止外推 |
|---|---|---|---|---|
| C-173 | 自定界索引层：`unary n`（`n` 个 `true` 后随一个 `false`）可被读取——`(m k : Nat) (b : Bool) (stk : Stack) (rest : List Bool) (f : Nat) → run (suc (m + f)) (unary m ++ rest) (readIndex b k stk) ≡ resume (close (leafTerm b (k + m)) stk) rest f`，即索引自带结束位，读取后剩余燃料恰为 `f`。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `unary-run`；run `20260913-MP-ERCF3-T3-STREAMING-PARSER-001-01`。 | 只覆盖一元索引层；不涉及符号层标签本身，也不涉及 Nat 层解码器。 |
| C-174 | 符号层与流式解析器：`bits`（`var`/`num` 两位标签 + 一元索引；应用结点一位标签）与 `BLEN` 下，`(t : Tm) (stk : Stack) (rest : List Bool) (f : Nat) → run (BLEN t + f) (bits t ++ rest) (startSub stk) ≡ resume (close t stk) rest f`——**燃料精确**（消耗 `BLEN t` 个单位后剩余恰为 `f`），解析器用显式框架栈在燃料上结构递归，故顺序消费问题（左子解析后仍需右子）在同一个递减递归内解决。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `parse-run`、`parse-run-app`（辅助 `+-assoc`/`++-assoc`）；同一 run。 | 只到 `bits`/`BLEN` 这一具体层与 `run` 这一具体解析器；不声称一般解析器/文法正确性，也不涉及对象层替换一致（那是 `codeT`/`substFix` 的义务）。 |
| C-175 | 长度对账与燃料分解：`(t : Tm) → LEN (bits t) ≡ BLEN t`；界即和分解 `{n m : Nat} → n ≤ m → Σ' Nat (λ k → m ≡ n + k)`；多余燃料下的 `unbits` 分解 `(i j c : Nat) → unbits (i + j) c ≡ unbits i c ++ unbits j (halfs i c)`（辅助 `LEN-++`、`LEN-unary`、`halfs`）。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `bits-length`、`≤-split`、`unbits-split`；同一 run。 | 只是机械对账：不声称编码最优、不声称界是紧的，也不涉及 `unbits` 在任意燃料下的语义解释。 |
| C-176 | 修复后的 Nat 值编码 `codeT'`（`t ↦ codeBits (bits t)`）带**全解码器** `dec : Nat → Tm`（含缺省分支，符合 C-168）满足往返 `(t : Tm) → dec (codeT' t) ≡ t`；由 C-164 得 `(t u : Tm) → codeT' t ≡ codeT' u → t ≡ u`。**`CodingRepair` 记录的修复义务（C-163/C-164/C-165）在编码层闭合**。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `codeT'`、`dec`、`codeT'-roundtrip`、`codeT'-injective`（`codeT'-bound` 由 C-172 与 C-175 长度对账组合）；同一 run。 | 只覆盖 **Tm** 的编码/解码与单射性；不修复公式层 `codeF` 的实现、不重做 `codeT`/`codeF` 的对象层替换一致义务、不涉及证明谓词 `P` 的表示性、反射或对角不动点；ERCF-3 保持 `GATED`。 |

## 追加登记：MP-ERCF3-T3-FORMULA-CODING-001（T3 修复编码的公式层：复用项层解码器，2026-09-13）

> 本节按 `verify_proof_version_closure.py` 的冻结前缀要求**追加在文末**；不改写 d3dfb0e 快照或任何既有追加节的字节。
> 精确范围与禁止外推见 `HoTT/formal/ercf3-t3/README.md` 与 run `20260913-MP-ERCF3-T3-FORMULA-CODING-001-01` 的 `RUN.json`。
> 本包把 C-176 的修复从 `Tm` 提升到 `Fml`（对角化真正需要的层）；不进入 ERCF-3 本体（P 表示性/反射/对角不动点），`GATED` 状态不变。

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-ERCF3-T3-FORMULA-CODING-001` | `C-177`–`C-180` | `formal/ercf3-t3/FormulaCoding.agda`（依赖 `ObjectSyntax.agda`、`DiagonalCore.agda`、`DecodingFence.agda`、`CodingRepair.agda`、`BitCoding.agda`、`StreamingParser.agda`；按 run 的 `source-manifest.json` 哈希固定） | `verification/runs/20260913-MP-ERCF3-T3-FORMULA-CODING-001-01/`；Agda 2.8.0-3d04bac、Cubical v0.9 库声明、仅 Agda builtins；exit 0、stderr 0；工具链 `formal/ercf3-t3/TOOLCHAIN.json` | `MACHINE_PROVED_LOCAL_UNCOMMITTED / ERCF3_T3_REPAIRED_FORMULA_CODING` |

| ID | 主张 | 裁决 | 直接依据 | 禁止外推 |
|---|---|---|---|---|
| C-177 | 公式符号层与流式解析器：`bitsF`（`=f`/`bot`/`=>f` 两位标签 + `all` 的两位标签与一元索引）与迭代数 `STEPS` 下，`(φ : Fml) (stk : Stack) (rest : List Bool) (f : Nat) → run (wantFml stk) (STEPS φ + f) (bitsF φ ++ rest) ≡ resume (close φ stk) rest f`；`all` 的索引读取 `run (index k stk) (suc (m + f)) (unary m ++ rest) ≡ run (wantFml (wantAll (k + m) ▷ stk)) f rest` 单独收口。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `parse-run`、`index-run`；run `20260913-MP-ERCF3-T3-FORMULA-CODING-001-01`。 | 只到 `bitsF`/`STEPS` 这一具体层与该解析器；不声称一般文法正确性，也不涉及公式层替换一致。 |
| C-178 | 项层解析器作为黑箱：`(t : Tm) (rest : List Bool) → tmFrom (bits t ++ rest) ≡ res t rest`，其中 `tmFrom bs = SP.run (LEN bs) bs (SP.startSub SP.ε)`——`=f` 的 `Tm` 子项燃料直接取自"剩余位数"，因此公式层不必重写项层解析器。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `tmFrom-run`、`eq-node`、`eqRight-step`（辅助 `SP.parse-run`、`SP.LEN-++`、`SP.bits-length`）；同一 run。 | 只说明该复用方式正确；不声称 `SP.run` 对任意燃料/任意位串都可判定（那仍需 C-172 的界）。 |
| C-179 | 长度对账：`(φ : Fml) → STEPS φ ≤ LEN (bitsF φ)`（辅助 `≤-self-add-right`、`≤-add-right`、`+-right-mono`、`+-left-mono`、`≤-add`、`BLEN-nonzero`、`one≤bits`），故公式码本身仍可充当燃料。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `STEPS≤LEN`；同一 run。 | 只是界；不声称界是紧的，也不声称迭代数与位数相等（`=f` 的迭代数严格小于其位数）。 |
| C-180 | 修复后的公式编码 `codeF'`（`φ ↦ codeBits (bitsF φ)`）带**全解码器** `decF : Nat → Fml` 满足 `(φ : Fml) → decF (codeF' φ) ≡ φ`，故 `codeF'` 单射（`roundtrip-implies-injective-F` 是 C-164 原理在 `Fml` 上的实例——C-164 本身只对 `Tm` 陈述）。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `codeF'`、`decF`、`codeF'-roundtrip`、`codeF'-injective`；同一 run。 | 只覆盖 `Fml` 的编码/解码与单射性；不宣称公式层与对象层替换（`substF`/`substFix` 系列）一致、不构造 `⌜φ⌝` 的算术化表示、不涉及 P 表示性/反射/对角不动点；ERCF-3 保持 `GATED`。 |

## 追加登记：MP-ERCF3-T3-REPAIRED-SYNTAX-001（T3 修复编码之上的替换一致与引用，2026-09-13）

> 本节按 `verify_proof_version_closure.py` 的冻结前缀要求**追加在文末**；不改写 d3dfb0e 快照或任何既有追加节的字节。
> 精确范围与禁止外推见 `HoTT/formal/ercf3-t3/README.md` 与 run `20260913-MP-ERCF3-T3-REPAIRED-SYNTAX-001-01` 的 `RUN.json`。
> 本包把 C-158/C-159 的**码级替换与语法级替换一致**这一义务，在**修复后的编码**上以推论形式收口；不进入 ERCF-3 本体，`GATED` 状态不变。

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-ERCF3-T3-REPAIRED-SYNTAX-001` | `C-181`–`C-183` | `formal/ercf3-t3/RepairedSyntax.agda`（依赖 `ObjectSyntax.agda`、`DiagonalCore.agda`、`CodingRepair.agda`、`BitCoding.agda`、`StreamingParser.agda`、`FormulaCoding.agda`；按 run 的 `source-manifest.json` 哈希固定） | `verification/runs/20260913-MP-ERCF3-T3-REPAIRED-SYNTAX-001-01/`；Agda 2.8.0-3d04bac、Cubical v0.9 库声明、仅 Agda builtins；exit 0、stderr 0；工具链 `formal/ercf3-t3/TOOLCHAIN.json` | `MACHINE_PROVED_LOCAL_UNCOMMITTED / ERCF3_T3_REPAIRED_SUBSTITUTION_AND_QUOTATION` |

| ID | 主张 | 裁决 | 直接依据 | 禁止外推 |
|---|---|---|---|---|
| C-181 | 项层码级替换：`substCodeT k n c = codeT' (substT k n (dec c))` 满足 `(k n : Nat) (t : Tm) → substCodeT k n (codeT' t) ≡ codeT' (substT k n t)`——**在修复编码的像上，码级替换与语法级替换一致**（旧编码的对应义务要 C-157–C-159 的联合递归工程）。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `substCodeT`、`substCodeT-agrees`（用 C-176 的往返）；run `20260913-MP-ERCF3-T3-REPAIRED-SYNTAX-001-01`。 | `substCodeT` 经**解码器**定义（解码—替换—编码）；本主张不包含"对象理论可表示该替换"，也不重做旧 `substFixT` 义务。 |
| C-182 | 公式层同型结论：`substCodeF k n c = codeF' (substF k n (decF c))` 满足 `(k n : Nat) (φ : Fml) → substCodeF k n (codeF' φ) ≡ codeF' (substF k n φ)`。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `substCodeF`、`substCodeF-agrees`（用 C-180 的往返）；同一 run。 | 同上：不主张表示性；不涉及 `substF` 的量词/影子分支等结构性质（那些已在 T2 层机器化）。 |
| C-183 | 引用与对角实例：`⌜ φ ⌝' = num (codeF' φ)` **单射**（`⌜-injective'`）；`diagonalize' φ = substF (codeF' φ) 0 φ` 是同一公式的替换实例（`refl`），且其码可由码级替换算出：`codeF' (diagonalize' φ) ≡ substCodeF (codeF' φ) 0 (codeF' φ)`。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `⌜_⌝'`、`⌜-injective'`、`diagonalize'`、`diagonalize'-is-subst`、`diagonalize'-code`；同一 run。 | 这是对角引理所需的**形状**，不是对角不动点：不构造 `P`、不证明表示性或反射；对象层可表示性仍归门 B。 |

## 追加登记：MP-ERCF3-T3-C168-COUNTERCHECK-001（独立审计反证在本 repo 内的重放，2026-09-13）

> 本节按冻结前缀要求**追加在文末**；不改写 d3dfb0e 快照、任何既有追加节或任何既有 run 收据。
> 来源：外部独立审计（`audit/imports/audit-c168-20260913/`，其发现 F1）。审计指出：C-168 的中文叙述把
> **`double` 的性质误交付成 `codeAtom` 的性质**——矩阵中 C-168 行引用的形式引理 `one-has-no-preimage` 的类型是
> `Not (Σ' Nat (λ m → double m ≡ suc zero))`，与 `codeAtom` 无关；而 `codeAtom` 实际**满射**。
> 本节只登记纠正证据；C-168 原行与其冻结收据保持原样供审计，narrative 由本 repo 重新推导的两条命题覆盖。

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-ERCF3-T3-C168-COUNTERCHECK-001` | `C-184`–`C-185` | `formal/ercf3-t3/C168Countercheck.agda`（**完整传递闭包**：`ArithmeticTags.agda`、`CodingRepair.agda`、`DecodingFence.agda`、`DiagonalLemma.agda`、`DiagonalCore.agda`、`ObjectSyntax.agda`；按 run 的 `source-manifest.json` 哈希固定） | `verification/runs/20260913-MP-ERCF3-T3-C168-COUNTERCHECK-001-01/`；Agda 2.8.0-3d04bac、仅 Agda builtins；exit 0、stderr 0；工具链 `formal/ercf3-t3/TOOLCHAIN.json` | `MACHINE_PROVED_LOCAL_UNCOMMITTED / ERCF3_T3_C168_NARRATIVE_CORRECTED_BY_COUNTERCHECK` |

| ID | 主张 | 裁决 | 直接依据 | 禁止外推 |
|---|---|---|---|---|
| C-184 | `codeAtom (anum zero) ≡ suc zero`：`1` 在 `ArithmeticTags.codeAtom` 下有**显式原像**。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `one-has-codeAtom-preimage`；run `20260913-MP-ERCF3-T3-C168-COUNTERCHECK-001-01`。 | 不否定 `double` 的"1 无原像"引理（该引理为真）；不涉及后续树/公式编码。 |
| C-185 | `(n : Nat) → Σ' Atom (λ a → codeAtom a ≡ n)`：原子编码 `codeAtom` **满射**。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `codeAtom-surjective`；同一 run。 | 只针对 `codeAtom`；`codeT'`/`codeF'` 的位串非空，故 `1` 确实不在其像中（其全解码器的缺省分支由**它们自己**的非满射性说明，而不是由 C-168）。 |

**由此产生的三处更正（当前真值已在 `HoTT/formal/ercf3-t3/README.md` §4、`audit/统观工作技术报告-20260913.md` §8.3(d)/§10 与本节同步）：**

1. C-168 的精确内容限定为：`double` 单射、`double n ≢ odd m`，以及 **`double` 下 `1` 无原像**（`avar`-only 片段非满射）；
2. 撤回"`codeAtom` 非满射 ⇒ 全解码器必须有缺省分支"的叙述——`codeAtom` 满射（C-185）；
3. `codeT'`/`codeF'` 的全解码器需要缺省分支这一点**仍然成立**，但依据是它们自身的像不含 `1`（见下方 C-186）。

## 追加登记：MP-ERCF3-T3-CODING-IMAGE-001（缺省分支的替换性论证，2026-09-13）

> 本节按冻结前缀要求**追加在文末**；不改写既有各节。承接上一节：C-168 的错误叙述被撤回后，必须为
> "修复后的全解码器带缺省分支"提供**真正成立**的依据，本节把它机器化。

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-ERCF3-T3-CODING-IMAGE-001` | `C-186`–`C-187` | `formal/ercf3-t3/CodingImage.agda`（**完整传递闭包**：`ObjectSyntax.agda`、`DiagonalCore.agda`、`DiagonalLemma.agda`、`DecodingFence.agda`、`CodingRepair.agda`、`BitCoding.agda`、`StreamingParser.agda`、`FormulaCoding.agda`） | `verification/runs/20260913-MP-ERCF3-T3-CODING-IMAGE-001-01/`；Agda 2.8.0-3d04bac、仅 Agda builtins；exit 0、stderr 0 | `MACHINE_PROVED_LOCAL_UNCOMMITTED / ERCF3_T3_REPAIRED_CODING_MISSES_ONE` |

| ID | 主张 | 裁决 | 直接依据 | 禁止外推 |
|---|---|---|---|---|
| C-186 | `(t : Tm) → codeT' t ≢ suc zero`：修复后的项编码**不含** `1`，故其全解码器 `dec` 的缺省分支是**可达的**（因而对全函数是必要的）。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `codeT'-misses-one`（辅助 `twice≠one`、`pack≠one`、`code-sentinel`）；run `20260913-MP-ERCF3-T3-CODING-IMAGE-001-01`。 | 只针对 `codeT'`；不涉及 `codeAtom`（C-185 已证其满射），也不涉及旧 `codeT`。 |
| C-187 | `(φ : Fml) → codeF' φ ≢ suc zero`：修复后的公式编码同样不含 `1`。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `codeF'-misses-one`；同一 run。 | 只针对 `codeF'`；不涉及旧 `codeF`、不涉及 P 表示性/反射/对角不动点。 |

## 追加登记：MP-CUBICAL-MACHINE-HALTING-001（固定程序的停机／发散校准，2026-09-14）

> 本节按冻结前缀要求追加在文末，不改写任何既有 proof/claim 行或 run 收据。证明源码逐字节取自只读贡献
> worktree 的候选，但本节只引用当前主库新建的 proof/claim/run 身份和当前工作根中的独立 kernel 运行。

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-CUBICAL-MACHINE-HALTING-001` | `C-188`–`C-190` | `formal/cubical-machine-halting/MachineHalting.agda`；精确规格与来源说明见同目录 `CLAIM.md`；工具链与 library registry 按 run 的 `source-manifest.json` 固定 | `verification/runs/20260914-MP-CUBICAL-MACHINE-HALTING-001-01/`；Agda 2.8.0-3d04bac、Cubical v0.9；`--safe --cubical --guardedness --ignore-interfaces`；exit 0、stderr 0 | `MACHINE_PROVED_LOCAL_UNCOMMITTED / FIXED_MACHINE_HALTING_DIVERGENCE_CALIBRATION` |

| ID | 主张 | 裁决 | 直接依据 | 禁止外推 |
|---|---|---|---|---|
| C-188 | 在源码给定的双计数器语言、步进函数与命题截断停机定义下，`halt-now : Halts haltProgram initial`：固定正控制程序在步数 `zero` 已经停机。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `halt-now = ∣ zero , refl ∣₁`；run `20260914-MP-CUBICAL-MACHINE-HALTING-001-01`。 | 只证明该固定程序；不推出任意程序的停机性。 |
| C-189 | `loop-diverges : (n : ℕ) → isFinal loopProgram (iterate n (step loopProgram) initial) ≡ false`：固定循环程序在每个有限观察下标都没有到达 `halt`。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `loop-diverges n = refl`；同一 run。 | 这是一个可直接化简的固定程序不变量；不是通用停机不可判定性，也没有证明校验器发散。 |
| C-190 | `loop-not-halts : ¬ Halts loopProgram initial`：固定循环程序不存在命题截断的有限停机见证。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED / R1_FIXED_MACHINE_CALIBRATION_COMPLETE` | `PT.rec isProp⊥` 把任意假想的截断见证消去到 `false ≢ true`；同一 run。 | 不构造通用机、程序编码、Gödel 句或可证性谓词；不说明发散具有 HoTT 特有原因；不建立自然消费者、同一现实任务对应或 HoTT 非现实性悖论。 |

## 追加登记：MP-CUBICAL-PROGRAM-CODE-001（R2 有限程序与有界解释器基础，2026-09-14）

> 本节追加在 R1 校准之后。它把函数空间程序收窄为有限指令表并提供统一的 bounded evaluator；“统一”只量化
> 当前有限语法，不能读成已经证明该语言通用或其停机问题不可判定。

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-CUBICAL-PROGRAM-CODE-001` | `C-191`–`C-194` | `formal/cubical-machine-halting/ProgramCode.agda`；依赖 `MachineHalting.agda`；精确规格见 `CLAIM-R2-PROGRAMCODE.md`；全部按 run source manifest 固定 | `verification/runs/20260914-MP-CUBICAL-PROGRAM-CODE-001-01/`；Agda 2.8.0-3d04bac、Cubical v0.9；`--safe --cubical --guardedness --ignore-interfaces`；exit 0、stderr 0 | `MACHINE_PROVED_LOCAL_UNCOMMITTED / R2_PROGRAMCODE_BOUNDED_EVALUATOR_FOUNDATION` |

| ID | 主张 | 裁决 | 直接依据 | 禁止外推 |
|---|---|---|---|---|
| C-191 | 归纳类型 `ProgramCode` 给出有限指令表；`decode : ProgramCode → Program` 是总函数，表头、表尾与空表外标签的三条方程分别由 `decode-head`、`decode-tail`、`decode-outside-empty` 证明。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `ProgramCode`、`lookupInstr`、`decode-*`；run `20260914-MP-CUBICAL-PROGRAM-CODE-001-01`。 | 还没有 `ProgramCode ↔ ℕ` 的 Gödel 编码／解码或公平枚举。 |
| C-192 | `runFor` 对任意 fuel、有限程序表和状态总结束，并满足 `runFor fuel code state ≡ iterate fuel (step (decode code)) state`；`finalAt` 因而与 R1 终止观察一致。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `runFor-agrees`、`finalAt-agrees`；同一 run。 | bounded evaluator 的总性只来自 fuel 递减；不构成无界停机判定器或语言通用性证明。 |
| C-193 | `haltCode` 的 `haltsWithin` 在任意 fuel 上为 `true`。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `haltCode-within`；同一 run。 | 停机正控制，只覆盖一个单指令程序表。 |
| C-194 | `loopCode` 在每个精确有限步都非终止，在每个有限界内 `haltsWithin = false`，且不存在截断的有限停机见证。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED / R2_PROGRAMCODE_THIN_SLICE_COMPLETE` | `loopCode-not-final`、`loopCode-never-within`、`loopCode-not-halts`；同一 run。 | 仍不证明通用停机不可判定、s-m-n／自应用或 certified reduction；不依赖 HoTT 特有机制，不建立自然 consumer、现实桥梁、Gödel 不完备性或内部矛盾。 |

## 追加登记：MP-CUBICAL-NAT-PROGRAM-CODE-001（R2 指令／程序自然数编码与数值有界解释器，2026-09-14）

> 本节在 R2 ProgramCode 第一薄层之后追加。它关闭 `R2-NATCODE-001`，使每个有限程序表进入一个可解码的自然数位置；
> 它尚未给出 `(program,input,fuel)` 的公平调度、语言通用性或停机不可判定性。

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-CUBICAL-NAT-PROGRAM-CODE-001` | `C-195`–`C-198` | `formal/cubical-machine-halting/NatProgramCode.agda`；依赖 `MachineHalting.agda`、`ProgramCode.agda`；精确规格见 `CLAIM-R2-NATCODE.md`；全部按 run source manifest 固定 | `verification/runs/20260914-MP-CUBICAL-NAT-PROGRAM-CODE-001-01/`；Agda 2.8.0-3d04bac、Cubical v0.9；`--safe --cubical --guardedness --ignore-interfaces`；exit 0、stderr 0 | `MACHINE_PROVED_LOCAL_UNCOMMITTED / R2_NATURAL_CODE_AND_BOUNDED_EVALUATOR_ALIGNMENT` |

| ID | 主张 | 裁决 | 直接依据 | 禁止外推 |
|---|---|---|---|---|
| C-195 | 五个 `Instr` 构造子与有限 `ProgramCode` 具有自然数编码和对全部 `ℕ` 有定义的 decoder。参数码与程序终止位自定界；fuel 为零或提前结束返回 `pcNil`，未分配标签 `101/110/111` 解释为 `halt`。`decodeNat zero ≡ pcNil`，且具体非法 `101` 自然数码解为 `pcCons halt pcNil`。`Instr` 通过单指令程序获得 `encodeInstrNat/decodeInstrNat`。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `bitsInstr`、`bitsProgram`、`codeBits`、`run`、`invalid101/110/111`、`decodeNat-zero`、`decodeNat-invalid101`、`encodeInstrNat`、`decodeInstrNat`；run `20260914-MP-CUBICAL-NAT-PROGRAM-CODE-001-01`。 | decoder 的默认语义是本 TaskSpec 的显式选择；不主张每个自然数都是合法编码，也不涉及程序语义通用性。 |
| C-196 | 合法像往返与覆盖：`(p : ProgramCode) → decodeNat (encodeNat p) ≡ p`；故 `encodeNat` 单射，且 `decodeNat` 对每个有限程序表有显式原像。对 `Instr` 同样有 `decodeInstrNat (encodeInstrNat i) ≡ i` 与编码单射。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `unbits-code`、`codeBits-dominates`、`parseInstr`、`parseProgram`、`decodeNat-encodeNat`、`encodeNat-injective`、`decodeNat-surjective`、`decodeInstrNat-encodeInstrNat`、`encodeInstrNat-injective`；同一 run。 | 这里只证明程序维度可数覆盖；没有证明程序／输入／fuel 三元组的公平或无饥饿调度。 |
| C-197 | 数值有界解释器在合法编码像上保持 R2 语义：`runNat fuel (encodeNat p) s ≡ runFor fuel p s`，并且 `finalNat`、`haltsWithinNat` 分别等于既有 `finalAt`、`haltsWithin`。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `runNat-on-image`、`finalNat-on-image`、`haltsWithinNat-on-image`；同一 run。 | 总性来自 decoder 与有限 fuel 的结构递减；不构成无界停机判定器。 |
| C-198 | R2 的停机／循环控制经自然数编码保持：编码后的 `haltCode` 在任意 fuel 内为 `true`；编码后的 `loopCode` 在任意精确有限步与任意有限界内均为 `false`。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED / R2_NATCODE_COMPLETE_FAIRNESS_OPEN` | `haltNat-within`、`loopNat-not-final`、`loopNat-never-within`；同一 run。 | 不证明当前语言计算通用、通用停机不可判定、s-m-n／自应用、Gödel/Rosser/Löb、HoTT essentiality、natural consumer、现实桥梁或内部矛盾。 |

## 追加登记：MP-CUBICAL-FAIR-ENUMERATION-001（R2 program/input/fuel 公平有限阶段枚举，2026-09-14）

> 本节在 NATCODE 之后追加。它用显式有限索引和 `AppearsBy` 到达界关闭 `R2-FAIR-001`，并把每个 schedule
> 位置的观察连接回原 `haltsWithin`；尚未构造不停机时保持 partial 的 semi-halting search。

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-CUBICAL-FAIR-ENUMERATION-001` | `C-199`–`C-202` | `formal/cubical-machine-halting/FairEnumeration.agda`；依赖 `MachineHalting.agda`、`ProgramCode.agda`、`NatProgramCode.agda`；精确规格见 `CLAIM-R2-FAIR.md`；全部按 run source manifest 固定 | `verification/runs/20260914-MP-CUBICAL-FAIR-ENUMERATION-001-01/`；Agda 2.8.0-3d04bac、Cubical v0.9；`--safe --cubical --guardedness --ignore-interfaces`；exit 0、stderr 0 | `MACHINE_PROVED_LOCAL_UNCOMMITTED / R2_FAIR_FINITE_STAGE_NO_STARVATION` |

| ID | 主张 | 裁决 | 直接依据 | 禁止外推 |
|---|---|---|---|---|
| C-199 | 固定三元组自然数码满足 `decodeTriple (encodeTriple a b c) ≡ triple a b c`，编码单射且 decoder 覆盖全部三元组；`Config=(pc,r0,r1)` 因而具有 `encodeConfig/decodeConfig` 往返、单射和 decoder 覆盖。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `readUnary-unary`、`parseTriple-junk`、`decodeTriple-encodeTriple`、`encodeTriple-injective`、`decodeTriple-surjective`、`decodeConfig-encodeConfig`、`encodeConfig-injective`、`decodeConfig-surjective`；run `20260914-MP-CUBICAL-FAIR-ENUMERATION-001-01`。 | 固定 arity 三元组编码；默认分支把缺参数读为 0；不主张编码唯一覆盖或资源最优。 |
| C-200 | 对任意有限 `program : ProgramCode`、`input : Config`、`fuel : ℕ`，显式 `caseIndex program input fuel` 满足 `caseAt caseIndex ≡ searchCase program input fuel`。`AppearsBy` 保存 `index ≤ stage` 与该等式；`eventuallyVisited` 以 `caseIndex` 本身为有限到达界，`noStarvation` 给出存在 stage。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED / R2_FAIR_FINITE_STAGE_NO_STARVATION` | `caseAt-caseIndex`、`eventuallyVisited`、`noStarvation`；同一 run。 | 公平性只指每个有限 case 有有限到达界；不限制索引大小、不要求唯一索引，也不等于搜索已找到首个 true。 |
| C-201 | schedule 保持任务：`observeAt (caseIndex program input fuel) ≡ haltsWithin fuel program input`。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `observeAt-caseIndex`；同一 run。 | 仍是给定 fuel 的 bounded observation；没有得到无界停机否定答案。 |
| C-202 | 公平 schedule 的控制：`haltCode` 的规范索引观察在任意 fuel 为 `true`，`loopCode` 的规范索引观察在任意 fuel 为 `false`。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED / R2_FAIR_COMPLETE_SEMIHALT_NEXT` | `haltCase-visited-true`、`loopCase-visited-false`；同一 run。 | 不证明 `CodeHalts` 已 semi-decidable、不证明计算通用性／停机不可判定、s-m-n、Gödel/Rosser/Löb、HoTT essentiality、natural consumer、现实桥梁或内部矛盾。 |

## 追加登记：MP-CUBICAL-SEMI-HALTING-001（R2 分阶段停机半判定与公平正见证枚举，2026-09-14）

> 本节在 R2 公平有限阶段枚举之后追加。它关闭 `R2-SEMIHALT-001`：有限 stage 的 `nothing` 只表示尚未发现，
> `just` 与有限停机见证双向对应；仍未证明当前语言通用或其停机问题不可判定。

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-CUBICAL-SEMI-HALTING-001` | `C-203`–`C-207` | `formal/cubical-machine-halting/SemiHalting.agda`；依赖 `MachineHalting.agda`、`ProgramCode.agda`、`NatProgramCode.agda`、`FairEnumeration.agda`；精确规格见 `CLAIM-R2-SEMIHALT.md`；全部按 run source manifest 固定 | `verification/runs/20260914-MP-CUBICAL-SEMI-HALTING-001-01/`；Agda 2.8.0-3d04bac、Cubical v0.9；`--safe --cubical --guardedness --ignore-interfaces`；exit 0、stderr 0 | `MACHINE_PROVED_LOCAL_UNCOMMITTED / R2_SEMI_HALTING_POSITIVE_SEARCH_AND_FAIR_ENUMERATION` |

| ID | 主张 | 裁决 | 直接依据 | 禁止外推 |
|---|---|---|---|---|
| C-203 | `semiHaltAt stage program input : Maybe Unit` 对每个有限 stage 总结束；其 `isSome` 精确等于 `haltsWithin stage`，而且正答案在后继 stage 保持。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `semiHaltAt`、`isSome-semiHaltAt`、`haltsWithin-next-stage`、`semiHaltAt-persistent`；run `20260914-MP-CUBICAL-SEMI-HALTING-001-01`。 | 有限 stage 的 `nothing` 不表示无界否定；这里只构造 stage-indexed approximants。 |
| C-204 | 精确步停机见证蕴含同界 bounded positive；bounded positive 又可构造某个精确有限步的截断 `CodeHalts` witness。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `finalAt-implies-haltsWithin`、`or-true-split`、`haltsWithin-implies-CodeHalts`；同一 run。 | 不选择最小停机时刻；不从截断中恢复规范 witness。 |
| C-205 | 对任意当前有限程序表与输入，`CodeHalts program input` 与“某个有限 stage 的 `semiHaltAt` 返回正答案”具有显式双向函数。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED / R2_SEMIHALT_CORRECT_COMPLETE` | `SemiReturns`、`CodeHalts-to-SemiReturns`、`SemiReturns-to-CodeHalts`、`CodeHalts↔SemiReturns`；同一 run。 | 这是当前 TaskSpec 的正半判定正确性／完备性；不证明不存在另一种总判定器。 |
| C-206 | `enumerateHalting` 是公平 schedule 上的全域正见证流；每个 bounded positive case 在规范 `caseIndex` 处发射，且规范位置的正发射还原为同一个 `haltsWithin=true`。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `enumerateHalting`、`isSome-enumerateHalting`、`enumerated-positive-sound`、`bounded-case-eventually-emitted`、`canonical-emission-sound`；同一 run。 | 枚举顺序不保证最小 witness 或复杂度界；无输出不是有限可观察的否定结论。 |
| C-207 | `haltCode` 在 stage 0 返回正答案；`loopCode` 在所有有限 stage 都不返回正答案且不存在 `SemiReturns` witness；公平全域枚举中的规范控制保持。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED / R2_SEMIHALT_COMPLETE_UNIVERSALITY_NEXT` | `haltCode-returns-at-zero`、`loopCode-never-returns`、`loopCode-not-SemiReturns`、`haltCode-scheduled-positive`、`loopCode-scheduled-negative`；同一 run。 | 具体循环的归纳不变量不等于通用停机不可判定；仍无 universality/reduction、Gödel/Rosser/Löb、HoTT essentiality、natural consumer、现实桥梁或内部矛盾。 |

## 追加登记：MP-COQ-MM2-UNDECIDABILITY-REPLAY-001（外部 MM2 synthetic undecidability 定理重放，2026-09-14）

> 上游：Coq Library of Undecidability Proofs，`coq-8.15` commit `c486697da8cfa4b9bb11b4c53eea7d57781c0deb`。
> 本包只登记上游定理在其自身定义下的原样重放；不会把 `undecidable` 改写成无条件 `¬ decidable`。

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-COQ-MM2-UNDECIDABILITY-REPLAY-001` | `C-208` | `formal/external-coq-mm2/CheckMM2Undec.v`；关键上游源码 12 份、777 文件全树 manifest、Docker image identity 与重放脚本均按 run source manifest 固定 | `verification/runs/20260914-MP-COQ-MM2-UNDECIDABILITY-REPLAY-001-01/`；Coq 8.15.2 / OCaml 4.07.1；完整干净树串行构建；exit 0；`Print Assumptions` 为 `Closed under the global context` | `REPLAYED_EXTERNAL_LIBRARY_WITH_SCOPE / SYNTHETIC_UNDECIDABILITY_DEFINITION_PRESERVED / LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED` |

| ID | 主张 | 裁决 | 直接依据 | 禁止外推 |
|---|---|---|---|---|
| C-208 | 在上游 `coq-8.15@c486697` 的精确定义中，Coq kernel 接受 `MM2_HALTING_undec : undecidable MM2_HALTING`，且 `Print Assumptions` 报告 `Closed under the global context`。这里 `undecidable P` 定义为 `decidable P -> enumerable (complement SBTM_HALT)`；`decidable P` 定义为存在逐点反映 `P` 的总 Bool 函数。 | `REPLAYED_EXTERNAL_LIBRARY_WITH_SCOPE / LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED` | `external-coq-mm2/upstream-coq-8.15-c486697/theories/Synthetic/Definitions.v`、`.../Synthetic/Undecidability.v`、`.../MinskyMachines/MM2.v`、`.../MM2_undec.v`；run `20260914-MP-COQ-MM2-UNDECIDABILITY-REPLAY-001-01`。两条 coqdep 告警只涉及本目标闭包之外的 `L/Tactics/{Extract,GenEncode}.v` 对 MetaCoq `bytestring` 的全项目扫描；目标依赖和 probe 均编译成功。 | 不等于纯构造元理论中的无条件 `¬ decidable MM2_HALTING`；不证明当前 rocq-9.2 commit 的 kernel replay；不证明上游 MM2 到 Cubical Agda `ProgramCode` 的编译等价；不证明 exact HoTT 不完备性、HoTT essentiality、natural consumer、现实桥梁或内部矛盾。 |

## 追加登记：MP-CUBICAL-MM2-BRIDGE-001（R2 MM2 到 ProgramCode 编译保持核心，2026-09-14）

> 本节把与上游 MM2 指令约定逐项对应的函数式源模型编译到当前 `ProgramCode`，并在 Agda 内证明停机双向保持。
> Coq 关系语义与该 Agda 源模型的跨语言 theorem transport 仍单列为未闭合义务。

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-CUBICAL-MM2-BRIDGE-001` | `C-209`–`C-213` | `formal/cubical-machine-halting/MM2Bridge.agda`；依赖 `MachineHalting.agda`、`ProgramCode.agda`、`NatProgramCode.agda`；精确规格见 `CLAIM-R2-MM2-BRIDGE.md`；全部按 run source manifest 固定 | `verification/runs/20260914-MP-CUBICAL-MM2-BRIDGE-001-01/`；Agda 2.8.0-3d04bac、Cubical v0.9；`--safe --cubical --guardedness --ignore-interfaces`；exit 0、stderr 0 | `MACHINE_PROVED_LOCAL_UNCOMMITTED / R2_MM2_TO_PROGRAMCODE_HALTING_EQUIVALENCE / CROSS_LANGUAGE_TRANSPORT_OPEN` |

| ID | 主张 | 裁决 | 直接依据 | 禁止外推 |
|---|---|---|---|---|
| C-209 | 函数式 `MM2Instr` 固定 label 1 起始、INC fall-through、DEC 正数跳转／零 fall-through 和表外停止；`compileMM2` 在目标 label 0 放 `halt` 哨兵。对所有程序和 label，编译后查表等于在该 label 编译源查表结果。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `lookup0`、`lookupMM2`、`compileInstr`、`compileTail`、`compileMM2`、`lookup-compileTail`、`lookup-compileMM2`；run `20260914-MP-CUBICAL-MM2-BRIDGE-001-01`。 | 源模型与 Coq `mm2_step/mm2_stop` 的跨语言等价还不是机器定理。 |
| C-210 | 对任意源程序和状态，源 finality 等于编译后 `ProgramCode` finality；源单步状态等于编译后 `universalStep`。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `compileFinal-agrees`、`sourceStep-compileObserved`、`compileStep-agrees`；同一 run。 | 只在本 Agda 文件定义的源模型与目标模型之间成立。 |
| C-211 | 对任意有限步数、源程序与状态，源 `mm2Run` 等于目标 `runFor`，源 `mm2FinalAt` 等于目标 `finalAt`。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `compileRun-agrees`、`compileFinalAt-agrees`；同一 run。 | 有限运行保持不独自给出 universality 或不可判定性。 |
| C-212 | `MM2Halts program state` 与 `CodeHalts (compileMM2 program) state` 具有显式双向函数，并保持相同有限步 witness 后再做命题截断。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED / AGDA_LOCAL_HALTING_REDUCTION_BIDIRECTIONAL` | `MM2Halts-to-CodeHalts`、`CodeHalts-to-MM2Halts`、`MM2Halts↔CodeHalts`；同一 run。 | C-208 的 Coq synthetic theorem 尚不能仅凭名称对应自动迁移；没有无条件 `¬ decidable CodeHalts`。 |
| C-213 | 空表停止、单 INC fall-through、DEC 零 fall-through、DEC 正数 jump 0 及编译后停机 witness 五项控制均成立。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED / R2_MM2_BRIDGE_CORE_COMPLETE` | `empty-program-final`、`single-incA-step`、`single-incA-final-after-one`、`single-decA-zero-fallthrough`、`single-decA-positive-jump-zero`、`single-incA-CodeHalts`；同一 run。 | 控制不证明复杂源程序覆盖、s-m-n、自应用、Gödel/Rosser/Löb、HoTT essentiality、natural consumer、现实桥梁或内部矛盾。 |

## 追加登记：MP-COQ-MM2-PROGRAMCODE-BRIDGE-001（同核 MM2 到显式 target 的归约，2026-09-14）

> 本节在 Coq 8.15.2 同一 kernel 内把上游关系式 `MM2_HALTING` 归约到与 Agda `ProgramCode` TaskSpec 同构的显式分支目标。
> 结论继续使用上游 synthetic `undecidable` 定义，不升级为无条件 `¬ decidable`。

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-COQ-MM2-PROGRAMCODE-BRIDGE-001` | `C-214`–`C-218` | `formal/external-coq-mm2/MM2ProgramCodeBridge.v`；`coq-8.15@c486697` 的 12 个关键原文件与 777 文件全树 manifest；精确规格见 `CLAIM-R2-COQ-MM2-BRIDGE.md`；全部按 run source manifest 固定 | `verification/runs/20260914-MP-COQ-MM2-PROGRAMCODE-BRIDGE-001-01/`；Coq 8.15.2 / OCaml 4.07.1；干净树串行构建；exit 0；`Print Assumptions PC_HALTING_undec` 为 `Closed under the global context` | `MACHINE_PROVED_LOCAL_UNCOMMITTED / SAME_KERNEL_TOTAL_REDUCTION / SYNTHETIC_UNDECIDABILITY_SCOPE` |

| ID | 主张 | 裁决 | 直接依据 | 禁止外推 |
|---|---|---|---|---|
| C-214 | Coq target 定义显式 INC/DEC 双分支/halt、有限表、表外默认 halt、deterministic bounded run 与有限停机；MM2 compiler 在 label 0 放 halt 哨兵，且所有 label 的查表保持。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `pc_instr`–`PC_HALTING`、`compile_instr`–`compile_program`、`nth_compile_tail`、`nth_compile_program`；run `20260914-MP-COQ-MM2-PROGRAMCODE-BRIDGE-001-01`。 | target 与 Agda 源码同构是 correspondence 结论，不是 Coq 内的 Agda AST 等式。 |
| C-215 | 上游关系式 `mm2_terminates program state` 当且仅当存在有限 `steps` 使函数式 `source_final_at steps program state=true`。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `nth_error_mm2_instr_at`、`mm2_instr_at_nth_error`、`source_final_false_step`、`mm2_step_source_complete`、`source_functional_to_relational`、`source_reaches_run`、`mm2_terminates_source_iff`；同一 run。 | 只关闭同一 Coq 中关系闭包与函数式有限观察的差异。 |
| C-216 | 对任意程序、状态和有限步数，源函数式 finality/step/run/final_at 与编译后的显式 target 对应量相等。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED` | `source_final_compile`、`source_step_compile`、`source_run_compile`、`source_final_at_compile`、`source_target_halting_iff`；同一 run。 | 有限运行保持本身不等于无条件不可判定，也不使用 HoTT higher structure。 |
| C-217 | `compile_problem` 是 total many-one reduction：`MM2_to_PC_HALTING : MM2_HALTING ⪯ PC_HALTING`。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED / SAME_KERNEL_REDUCTION_COMPLETE` | `MM2_to_PC_HALTING`；同一 run。 | 证明的是 Coq target；到 Agda target 的跨 kernel 保真需结合 C-209–C-213 与 correspondence 审计。 |
| C-218 | 从 C-208 上游 theorem 与 C-217 导出 `PC_HALTING_undec : undecidable PC_HALTING`；`Print Assumptions` 为 `Closed under the global context`。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED / SYNTHETIC_UNDECIDABILITY` | `PC_HALTING_undec`；同一 run。两条 coqdep 告警仍只涉及目标闭包外的 MetaCoq `bytestring` 扫描项并原样保留。 | `undecidable P` 仍是 `decidable P → enumerable(complement SBTM_HALT)`；不推出纯构造内部 `¬ decidable`、CT/EPF、s-m-n、Gödel/Rosser/Löb、exact HoTT 不完备性、HoTT essentiality、natural consumer、现实桥梁或矛盾。 |

## 追加登记：MP-COQ-PARAMETRIC-CT-INTERNAL-UNDEC-001（显式 EPF/SCT 前提下的内部不可判定性，2026-09-14）

> 上游：Yannick Forster `coq-synthetic-computability`，branch `code`，commit `b9523cb33180dc58b227432e60045cc38615b711`。
> 本包把 R2 从 synthetic implication 推进到 Coq 对象语言内的 `~ decidable`，但 `EPF_bool + SCT` 仍是显式前提；不把它写成 ambient HoTT 的无条件结论。

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-COQ-PARAMETRIC-CT-INTERNAL-UNDEC-001` | `C-219`–`C-222` | `formal/external-coq-parametric-ct/CheckInternalUndec.v`；109 文件全树 manifest、20 文件 target closure、Docker recipe/image identity 与重放脚本均按 run source manifest 固定 | `verification/runs/20260914-MP-COQ-PARAMETRIC-CT-INTERNAL-UNDEC-001-01/`；Coq 8.13.2 / OCaml 4.07.1 / Equations 1.2.3+8.13 / stdpp 1.5.0；干净闭包串行构建；exit 0；三个 `Print Assumptions` 均为 `Closed under the global context` | `MACHINE_PROVED_LOCAL_UNCOMMITTED / CONDITIONAL_INTERNAL_NOT_DECIDABLE / EXPLICIT_EPF_BOOL_OR_SCT_PREMISE` |

| ID | 主张 | 裁决 | 直接依据 | 禁止外推 |
|---|---|---|---|---|
| C-219 | 在显式前提 `EPF_bool + SCT` 下，存在谓词 `K : nat → Prop`：`K` 可半判定，`compl K` 不可半判定，且 `K` 与 `compl K` 都不可判定。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED / CONDITIONAL_INTERNAL_NEGATION` | 上游 `Axioms/bestaxioms.v` 的 `EPF_halting`/`CT_halting` 与 `Axioms/halting.v` 的 `EPF_SCT_halting`；run `20260914-MP-COQ-PARAMETRIC-CT-INTERNAL-UNDEC-001-01`。 | `EPF_bool + SCT` 是 sum premise（给出任一分支）；本包没有证明 EPF_bool 或 SCT 在 ambient HoTT 中成立。 |
| C-220 | 在同一显式前提下，`K_nat_bool_undec : ~ decidable (compl K_nat_bool)`；这里 `K_nat_bool f := exists n, f n = true`。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED / CONDITIONAL_INTERNAL_NOT_DECIDABLE` | `Axioms/halting.v` 的 `K_nat_bool_complete`、`K_nat_bool_undec`；同一 run。 | 这是 Coq CIC 内部否定，但仍有 EPF_bool/SCT 前提；不等于当前 Agda `ProgramCode` 的无条件停机不可判定。 |
| C-221 | 在同一显式前提下，`K_nat_undec : ~ decidable (fun f : nat → nat => forall n, f n = 0)`。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED / CONDITIONAL_INTERNAL_NOT_DECIDABLE` | `Axioms/halting.v` 的 `K_nat_bool_equiv`、`K_nat_equiv`、`K_nat_undec`；同一 run。 | 不主张此函数空间命题就是 HoTT 的 exact calculus theoremhood，不建立 Gödel/Rosser/Löb 或现实桥梁。 |
| C-222 | `Print Assumptions` 对 `EPF_SCT_halting`、`K_nat_bool_undec`、`K_nat_undec` 各输出一次 `Closed under the global context`；目标依赖闭包在作者指定的 Coq 8.13.2 时代环境中重建成功。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED / ASSUMPTION_CLOSURE_REPLAYED` | `CheckInternalUndec.v` 与保存 stdout；20 个实际源依赖逐文件固定；Coq 8.15.2/stdpp 1.7.0 的版本不兼容尝试另作失败证据保留。 | “global context closed”不消除定理箭头左侧的显式 EPF_bool/SCT 前提；不证明 HoTT essentiality、natural consumer、same-task reality、内部矛盾或原创性。 |

## 追加登记：MP-CUBICAL-GROUPOID-SYNTAX-REPLAY-001（G-HOTT-SYNTAX 首个精确机器切片，2026-09-14）

> 上游：Altenkirch–Kaposi–Xie，`akaposi/cohtt` master commit `5babc385d01500c1777ff932dd8c79299a1d766a`。
> 本包冻结并重放一个确切的 Cubical Agda groupoid-syntax，而不把它扩大成完整 HoTT 自语法或 R4 不完备性。

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-CUBICAL-GROUPOID-SYNTAX-REPLAY-001` | `C-223`–`C-226` | `formal/external-cubical-groupoid-syntax/CheckGroupoidSyntax.agda`；91 文件全树 manifest、22 文件 target manifest、derived library-name wrapper、上游 source 与重放脚本均按 run source manifest 固定 | `verification/runs/20260914-MP-CUBICAL-GROUPOID-SYNTAX-REPLAY-001-01/`；Agda 2.8.0-3d04bac、Cubical v0.9；两阶段 full-source replay；exit 0；stderr 只有四个空 phase 标记 | `MACHINE_PROVED_LOCAL_UNCOMMITTED / EXACT_HOTT_RELEVANT_SYNTAX_SLICE_REPLAYED / FULL_HOTT_CALCULUS_OPEN` |

| ID | 主张 | 裁决 | 直接依据 | 禁止外推 |
|---|---|---|---|---|
| C-223 | 固定 groupoid syntax 是四 sort 的 Cubical HIIT 编码：`Con`、`Sub`、`Ty`、`Tm`；它包含 substitution/composition、terminal context、context extension、`U/El`、Π、`lam/app`、β/η，以及 `U/El/Π` substitution 与 composition/identity 的二阶 coherence。`Sub` 与 `Tm` 由构造器截为 set，`Ty` 先截为 groupoid。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED / EXACT_SYNTAX_DEFINITION_REPLAYED` | 上游 `TT/Groupoid/Syntax.agda`、`TT/Groupoid/CwF.agda`；run phase 1/2 都重新检查对应模块。 | 对象理论只含当前列出的构造；不含 Nat、一般 identity type、对象层 univalence/HIT、proof checker 或 arithmetic。 |
| C-224 | α-normalisation 定义 normal types `NTy`、`norm : Ty Γ → NTy Γ` 与 retraction `⌜ norm A ⌝ ≡ A`，并证明 `isSetTy : (Γ : Con) → isSet (Ty Γ)`。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED / GROUPOID_SYNTAX_TYPES_ARE_SETS` | `TT/Groupoid/NTy.agda` 的 `isSetNTy`、`norm`、`⌜⌝-norm`、`isSetTy`；项目探针 `groupoid-types-are-sets`；同一 run。 | setness 不自动给 decidable equality、proof enumeration、normalisation of all terms 或 Gödel coding。 |
| C-225 | `TT.Groupoid.IsoSet` 构造 `isoCon`、`isoSub`、`isoTy`、`isoTm`，把 groupoid syntax 的 contexts、substitutions、types、terms 与 set syntax 的相应 sort 同构；项目探针逐项按原类型复述并由原定理填充。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED / GROUPOID_AND_SET_SYNTAX_SORT_ISOMORPHISMS` | `TT/Groupoid/IsoSet.agda` 与 `CheckGroupoidSyntax.agda` 的四个 alias；同一 run phase 2/3。 | 不证明两套语法拥有本项目 R4 所需的所有 HoTT 构造或算术解释；不建立现实相对失配。 |
| C-226 | 上游当前 20 个 `TT` 模块先在 fresh pinned dependency source 上通过，再删除全部 cohtt `.agdai` 并按上游 flags 重查；项目 theorem probe 随后通过。上游 `cohtt.agda-lib` 缺 `name:`，derived wrapper 只增加 library name。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED / TWO_PHASE_EXACT_SOURCE_REPLAY` | `TT/README.agda` 导入分母、`TARGET_SOURCE_MANIFEST.json`、`cohtt-replay.agda-lib`、run stdout/stderr 与 exact replay。 | 直接把 `--hidden-argument-puns` 应用于 Cubical v0.9 全源会触发依赖解析失败；两阶段边界不应被隐去。此包不证明 R4 不完备性、HoTT essentiality、natural consumer、现实桥梁或悖论。 |

## 追加登记：MP-CUBICAL-2LTT-FIBRANT-REPLACEMENT-UIP-001（内部纤维替换导致 UIP 的最小两层机器构造，2026-09-15）

> 本包以外层 Agda 类型、内层 code/`El`、受限内层 `Jᵢ` 和 context-uniform `R` 重构 2LTT Theorem 2.20 的核心推演。
> 它故意阻止宿主 Cubical Path 直接消去到任意外层类型；COMP-R 不在接口中，因而机器结果显示 FORM/INTRO/dependent-ELIM 已经足够。

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-CUBICAL-2LTT-FIBRANT-REPLACEMENT-UIP-001` | `C-227`–`C-232` | `formal/two-level-fibrant-replacement-uip/TwoLevelReplacementUIP.agda`；精确接口、论文对应和禁止外推见同目录 claim 文档；2LTT primary §2.7 进入 run source manifest | `verification/runs/20260915-MP-CUBICAL-2LTT-FIBRANT-REPLACEMENT-UIP-001-01/`；Agda 2.8.0-3d04bac、Cubical v0.9；`--safe --cubical --guardedness --ignore-interfaces`；exit 0、stderr 0 | `MACHINE_PROVED_LOCAL_UNCOMMITTED / TWO_LEVEL_CONTEXT_UNIFORM_REPLACEMENT_IMPLIES_INNER_UIP / NATIVE_S1_CONTROL` |

| ID | 主张 | 裁决 | 直接依据 | 禁止外推 |
|---|---|---|---|---|
| C-227 | 对任意内层类型 `A`、点 `u` 和外层严格环路 `h : u E.≡ u`，外层 UIP 经 `strictCong encode` 与第二次 `encode` 产生 `encode h =ᶦ reflᵢ`；这是论文式 (2.14) 的机器对应。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED / FORMAL_CHECKED_WITH_SCOPE` | `strict-loop-canonical`；run `20260915-MP-CUBICAL-2LTT-FIBRANT-REPLACEMENT-UIP-001-01`。 | 外层 UIP 是 `TwoLevelReplacement.strictUIP` 的显式字段；本包不在 Cubical Path 中证明 strict UIP。 |
| C-228 | `StrictWitness A u v p` 是论文式 (2.13) 内 `R` 的外层见证类型；`lifted-witness` 通过受限内层路径归纳，构造 `El (R (StrictWitness A u v p))`。其 motive 能成为内层 code，正是因为统一 `R` 可作用于依赖内层路径 `p` 的外层类型。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED / CONTEXT_UNIFORM_R_WITNESS` | `StrictWitness`、`lifted-witness`；同一 run。 | 这没有构造一个实际 fibrant replacement；它证明任何提供该统一接口的两层 fragment 都必须承担后果。 |
| C-229 | 从 ELIM-R 的常值族实例 `recR` 在严格反身环路处求值，`based-uip` 收缩任意内层环路；再用内层 Π 与 J，`inner-uip` 证明任意两个内层恒等证明相等。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED / INNER_UIP_FROM_REPLACEMENT_FRAGMENT` | `recR`、`based-uip`、`inner-uip`；同一 run。 | COMP-R 未声明也未使用；结论依赖完整 record 的内层 J/Π、外层 UIP 和 context-uniform R/intro/elim，不是 basic HoTT 或 basic 2LTT 的无前提定理。 |
| C-230 | 若该 fragment 的某个内层类型带一个不能等于 `reflᵢ` 的环路，则 `replacement-excludes-nontrivial-loop` 导出 `⊥`。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED / NONTRIVIAL_INNER_LOOP_EXCLUSION` | `NontrivialInnerLoop`、`replacement-excludes-nontrivial-loop`；同一 run。 | 这是条件不相容定理；没有声称 record 有 inhabitant，也没有把抽象 fragment 与原生 Cubical `Type` 自动等同。 |
| C-231 | 原生 Cubical `S¹` 中，Möbius family 把 `refl ≡ loop` 送到 `false ≡ true`，故 `refl≢loop`；对称地 `loop≢refl`。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED / NATIVE_CUBICAL_NONTRIVIAL_LOOP_CONTROL` | `möbius`、`odd?`、`refl≢loop`、`loop≢refl`；同一 run。 | 该控制与抽象 fragment 分开定义；它确认通常 HoTT 高阶结构会被 UIP 消灭，但不冒充 record 的语义实例。 |
| C-232 | 删除两层 strict-UIP 桥后，原生 Cubical universe 中 `NativeR X = X`、`native-r` 与 `native-elimR` 同时满足 FORM/INTRO/依赖 ELIM 形状。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED / POSITIVE_ABLATION_CONTROL` | `NativeR`、`native-r`、`native-elimR`；同一 run。 | 不能把任意“R 形接口”单独当作矛盾；决定性组合是外层 UIP、内外层等式编码以及 R 在内层路径依赖语境中的统一可用性。论文已公开指出 base-change/context-stability 障碍与 crisp 规避方向；本包不认领新 HoTT BUG。 |

## 追加登记：MP-AGDA-FLAT-INTERNAL-UNIVERSES-REPLAY-001（内部 fibration universe no-go 与 crisp 恢复，2026-09-15）

> 上游：Licata–Orton–Pitts–Spitters, *Internal Universes in Models of Homotopy Type Theory*, FSCD 2018；官方 Cambridge dataset DOI `10.17863/CAM.22369`。
> 13 个 Agda source 在从 `agda/agda` flat commit `70899fb` clean 构建的 Agda-flat 2.6.0.1 中整包重放；本项目另加一正一负 modal typing control。

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-AGDA-FLAT-INTERNAL-UNIVERSES-REPLAY-001` | `C-233`–`C-238` | `formal/external-agda-flat-internal-universes/upstream/README.agda` 及其 12 个 source；官方 ZIP/source-tree/image/build recipe/controls 均固定 | `verification/runs/20260915-MP-AGDA-FLAT-INTERNAL-UNIVERSES-REPLAY-001-01/`；Agda-flat 2.6.0.1-70899fb；full suite + positive control + expected negative；exit 0、stderr 0 | `MACHINE_REPLAYED_EXTERNAL_LIBRARY_LOCAL_UNCOMMITTED / INTERNAL_CLASSIFIER_NO_GO_AND_CRISP_RECOVERY` |

| ID | 主张 | 裁决 | 直接依据 | 禁止外推 |
|---|---|---|---|---|
| C-233 | Cambridge 官方 ZIP `56b18248…` 中 13 个 Agda source（44,374 bytes）逐字进入 main；Agda-flat 从 exact `flat@70899fb` / git tree `0e9f8802…` clean 构建，版本串无 `-dirty`；`README.agda` 的全部导入闭包通过。 | `MACHINE_REPLAYED_EXTERNAL_LIBRARY_LOCAL_UNCOMMITTED / SOURCE_AND_TOOLCHAIN_QUALIFIED` | `SOURCE_TREE_MANIFEST.json`、`AGDA_FLAT_IMAGE.json`、Docker recipe、run stdout/source manifest。 | 项目复制与 kernel replay不证明 postulates 在任意模型中成立，也不认证原创性。 |
| C-234 | `IntUniv.fiberwise-fibrant-is-fibrant` 从普通 internal weak classifier 把逐点 fibrant family 提升为整体 fibration；若 composition有 interval transport且每个常值严格等式 family fibrant，则 `NoIntUniv` 对 `P i = (O ≡ i)` 导出 `O ≡ I`，与 `O≠I` 矛盾。 | `MACHINE_REPLAYED_EXTERNAL_LIBRARY_LOCAL_UNCOMMITTED / INTERNAL_CLASSIFIER_NO_GO` | `upstream/theorem-3-1.agda` 的 `IntUniv`、`fiberwise-fibrant-is-fibrant`、`NoIntUniv`；同一 run。 | 显式依赖 `funext`、UIP、nontrivial interval、cofibrancy 和给定 composition/transport；不是无前提 HoTT 矛盾。 |
| C-235 | 同一官方源码为 CCHM composition 与 Cartesian Cubical composition分别构造 `coe`、常值严格等式 fibrancy，并得到 `NoIntCCHMUniv` 与 `NoIntCCTTUniv`。 | `MACHINE_REPLAYED_EXTERNAL_LIBRARY_LOCAL_UNCOMMITTED / TWO_FIBRATION_NOTIONS` | `agda/cchm.agda`、`agda/cctt.agda` 与 `theorem-3-1.agda` 两个实例；同一 run。 | 两个实例扩大模型相关性，但不证明所有 fibration notions 都满足前提。 |
| C-236 | 在 crisp modal type theory 中，若 path functor 的指数具有由 tiny interval 给出的外部右伴随 `√` 及 `R/L/LR/RL/R℘`，Theorem 5.2 构造 `U`、fibration `El`、crisp `code`、`Elcode`、`codeEl` 与 `prf : Univ l`；正向 classifier 只接收 crisp/global fibration。 | `MACHINE_REPLAYED_EXTERNAL_LIBRARY_LOCAL_UNCOMMITTED / CRISP_CLASSIFIER_CONSTRUCTED` | `upstream/agda-flat/tiny.agda`、`upstream/theorem-5-2.agda`；同一 run。 | tiny/right-adjoint 数据是显式 postulate；crisp classifier 的任务契约不同于 C-234 中允许 local-dependent input 的 ordinary classifier。 |
| C-237 | Agda-flat 接受 crisp function 应用于 crisp argument；把 argument 改为普通 local variable 后同一编译器以 `Variable x is declared top, so it cannot be used here` 拒绝。该限制机械阻止把 `code` 应用于依赖 local `i : I` 的 pointwise fibration。 | `MACHINE_REPLAYED_EXTERNAL_LIBRARY_LOCAL_UNCOMMITTED / MODAL_TYPING_ABLATION` | `controls/CrispPositive.agda`、`controls/CrispNegative.agda`；run phase `CRISP_POSITIVE` 与 `CRISP_NEGATIVE_EXPECTED_REJECTION`。 | 控制验证 modal rule 的实施，不独自证明所有 crisp 程序保真或所有现实消费者可接受该限制。 |
| C-238 | 官方 `README.agda` 同时接受相对 universe 版本和 Proposition 6.2；后者在给定 crisp universe/`El`/`code`/β/η 前提下构造 fibration-notion morphism的 identity 与 composition。 | `MACHINE_REPLAYED_EXTERNAL_LIBRARY_LOCAL_UNCOMMITTED / RELATIVE_UNIVERSE_AND_MORPHISM_LAYER` | `upstream/theorem-5-2-relative.agda`、`upstream/proposition-6-2.agda`；同一 run。 | Proposition 6.2 自身另有显式 universe postulates；不把它外推成完整多宇宙模型、现实桥梁或最终悖论。 |

## 追加登记：MP-COQ-INTERVAL-REPLACEMENT-BOUNDARY-001（regular/degenerate fibrancy 正负对照，2026-09-15）

> 上游：Boulier–Tabareau, *Model structure on the universe of all types in interval type theory*，论文所指 GitLab `emptyctx@28a2568`。
> 源 subtree 未发现 license，故不复制正文；20 文件通过 deterministic git archive、逐文件 hash 与 git tree 固定。

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-COQ-INTERVAL-REPLACEMENT-BOUNDARY-001` | `C-239`–`C-243` | `formal/external-coq-interval-replacement/CheckReplacementBoundary.v`；外部 `InternalCubical-Coq` 20 文件 archive/tree manifest | `verification/runs/20260915-MP-COQ-INTERVAL-REPLACEMENT-BOUNDARY-001-01/`；Coq 8.13.2；fresh archive build + assumptions probe；exit 0 | `MACHINE_REPLAYED_EXTERNAL_LIBRARY_LOCAL_UNCOMMITTED / REGULAR_REPLACEMENT_NO_GO_AND_DEGENERATE_TRANSPORT_RECOVERY` |

| ID | 主张 | 裁决 | 直接依据 | 禁止外推 |
|---|---|---|---|---|
| C-239 | `InternalCubical-Coq` 的 20 文件/177,150 bytes 被固定到 `emptyctx@28a2568`、subtree git tree `51ec7ae9…`、derived tree SHA `43557c5c…`；`Inconsistency.vo`、`FibRepl.vo` 与项目 probe 在 Coq 8.13.2 fresh extraction 中编译。 | `MACHINE_REPLAYED_EXTERNAL_LIBRARY_LOCAL_UNCOMMITTED / SOURCE_AND_TOOLCHAIN_QUALIFIED` | `SOURCE_TREE_MANIFEST.json`、`COQ_IMAGE.json`、run source manifest/stdout/stderr。 | 该 subtree 无 license 文件，未进入 repo 正文；8.13.2 通过本目标不证明作者全部 8.10-era 工程通过。 |
| C-240 | `Inconsistency.Unnamed_thm : False` 在显式 `repl`、`η`、fibrant-target recursor `repl_rec'` 与对任意 open family 的 `RFib_repl` 下成立；`Print Assumptions` 同时固定 nontrivial interval 与 cofibration/equality基础。 | `MACHINE_REPLAYED_EXTERNAL_LIBRARY_LOCAL_UNCOMMITTED / REGULAR_FAMILY_REPLACEMENT_CONTRADICTION` | `Inconsistency.v` 与 probe 的 `regular_replacement_contradiction`；同一 run assumptions block。 | 结论来自显式 regular-family replacement 假设；不证明实际 degenerate `FibRepl.repl` 矛盾。 |
| C-241 | `FibRepl.v` 的 private inductive/QIT `repl`、`η/hcomp/qq` 编译，并得到 `Fib_repl : DFib repl`、只对 `RFib` motive 的 `repl_ind'`、fibrant-target `repl_rec'` 与 `repl_f` functor laws。 | `MACHINE_REPLAYED_EXTERNAL_LIBRARY_LOCAL_UNCOMMITTED / DEGENERATE_REPLACEMENT_CONSTRUCTED` | `FibRepl.v`；probe 的 `Check` 与 `Print Assumptions`；同一 run。 | `qq` 与 interval/cofibration axioms 显式保留；`DFib repl` 不等于对任意 open family的 `RFib (repl ∘ P)`。 |
| C-242 | `RFib_DFib`、`RFib_Trans` 与 `TransFib_HFib` 分别给出 regular→degenerate、regular→transport、degenerate+transport→regular，机械固定 `RFib` 的两部分结构。 | `MACHINE_REPLAYED_EXTERNAL_LIBRARY_LOCAL_UNCOMMITTED / REGULAR_FIBRANCY_DECOMPOSITION` | `Fibrations.v` 三个定义与 probe；同一 run。 | 分解说明支付位置，不证明任意输入 family 自动带 transport。 |
| C-243 | `repl_ind'` 的 motive 必须 `RFib`；`repl_J` 的 assumptions 额外出现 `extension_rule__emptyctx`。因此可用 replacement 的高阶消去与 regularity 依赖 motive/context 限制，而不是无条件恢复 C-240 的 open-family `RFib_repl`。 | `MACHINE_REPLAYED_EXTERNAL_LIBRARY_LOCAL_UNCOMMITTED / ELIMINATION_AND_CONTEXT_PAYMENT` | `FibRepl.v:41-93,212-260` 与 exact assumptions output。 | 完整 `Model_structure.v` 未在本 run 通过；Coq 8.13.2 在旧 implicit placeholder 失败，作者 history 目标为 8.10。不能冒充完整 pre-model structure replay、basic HoTT 矛盾或现实桥梁。 |

## 追加登记：MP-COQ-SYNTHETIC-INCOMPLETENESS-R3-001（一般 R3 essential incompleteness 与 Robinson Q，2026-09-15）

> 上游：`uds-psl/coq-synthetic-incompleteness`，branch `csl`，commit `cd7d8490f8542bfe85658c465bcb26b2ed163f53`。
> 本包从 repo-contained deterministic archive 全新构建作者的 first-order incompleteness target；它校准 R3，不把一阶算术理论 `T` 冒充 exact HoTT calculus。

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-COQ-SYNTHETIC-INCOMPLETENESS-R3-001` | `C-244`–`C-249` | `formal/external-coq-synthetic-incompleteness/`；807-file exact source archive、CeCILL license、source manifest、Docker recipe、Qualification probe 与逐 claim 规格均由 run source manifest 固定 | `verification/runs/20260915-MP-COQ-SYNTHETIC-INCOMPLETENESS-R3-001-01/`；Coq 8.15.2；fresh build约 614 s；target/stable artifact/prior logs exact；qualification 两次 exact；exit 0 | `MACHINE_REPLAYED_EXTERNAL_LIBRARY_LOCAL_UNCOMMITTED / R3_CONDITIONAL_ESSENTIAL_INCOMPLETENESS_AND_ROBINSON_Q / HOTT_R4_OPEN` |

| ID | 主张 | 裁决 | 直接依据 | 禁止外推 |
|---|---|---|---|---|
| C-244 | exact commit 的 deterministic Git archive 解压为 807 个 tracked files / 7,423,361 bytes，逐文件与 source manifest 相同，tree SHA 为 `d9dd001b…80ca`；CeCILL license 与 derived Coq 8.15.2 image `sha256:d4a84f07…010b` 均固定。 | `MACHINE_REPLAYED_EXTERNAL_LIBRARY_LOCAL_UNCOMMITTED / SOURCE_LICENSE_TOOLCHAIN_QUALIFIED` | `SOURCE_ARCHIVE.json`、`SOURCE_TREE_MANIFEST.json`、`TOOLCHAIN.json`、`CeCILL_LICENSE.txt`、run source manifest。 | 来源和工具链资格化本身不是数学定理；image 存在不证明 target 构建。 |
| C-245 | 给定 `is_universal theta`，`self_halting_diverge` 与 `recursively_separating_diverge` 对正确分类 self-halting 或两个 `theta_self_return` predicate 的 partial Boolean classifier 构造某个 `c`，并证明对每个 Boolean 都不收敛。 | `MACHINE_REPLAYED_EXTERNAL_LIBRARY_LOCAL_UNCOMMITTED / CONDITIONAL_CLASSIFIER_DIVERGENCE` | 作者 `epf.v`；`Qualification.v` 的 exact signature；同一 run。 | 显式依赖 universality 与 classifier correctness；不是任意程序、HoTT kernel 或普通 proof checker 的发散。 |
| C-246 | `insep_essential_incompleteness`：给定 universal `theta`、`fs'` 对 `fs` 的 extension，以及 `fs'` 对两个 self-return 集的 strong separation 表示，存在对 `fs` independent 的 `r n`。 | `MACHINE_REPLAYED_EXTERNAL_LIBRARY_LOCAL_UNCOMMITTED / CONDITIONAL_ESSENTIAL_INCOMPLETENESS` | 作者 `abstract_incompleteness.v`；exact theorem type与同一 run。 | `Universal`、extension、strong separation 都是显式参数；没有实例化 HoTT syntax。 |
| C-247 | 在隐式 Peirce 参数下，`epf_mu_ctq : is_universal epf_mu.theta_mu → CTQ`，把 CTQ 归约到具体 μ-recursive interpreter 的 universality。 | `MACHINE_REPLAYED_EXTERNAL_LIBRARY_LOCAL_UNCOMMITTED / EPF_MU_TO_CTQ` | 作者 `ctq.v`；exact theorem type与同一 run。 | 构建不产生 universality proof，不把 CTQ/Church thesis变成 ambient Coq 或 HoTT 无条件定理。 |
| C-248 | `Q_incomplete`：在显式 Peirce 与 CTQ 下，每个包含 `Qeq`、可枚举且一致的同语言理论 `T` 都有 closed `Σ₁` 句 `φ`，使 `T` 既不证明 `φ` 也不证明 `¬φ`。 | `MACHINE_REPLAYED_EXTERNAL_LIBRARY_LOCAL_UNCOMMITTED / CONDITIONAL_ROBINSON_Q_INDEPENDENT_SENTENCE` | 作者 `fol_incompleteness.v`；资格化输出中的完整 theorem type；同一 run。 | 没有证明 exact HoTT calculus 包含 Q、可枚举、一致或满足 CTQ；没有现实同任务结论。 |
| C-249 | fresh archive build 的 stdout/stderr、1,284 个 `.vo/.vos/.vok/.glob` stable artifacts 与 target `.vo` 均匹配此前两次独立 clean build；qualification 连续两次 byte-exact，后三个定理各输出一次 `Closed under the global context`。 | `MACHINE_REPLAYED_EXTERNAL_LIBRARY_LOCAL_UNCOMMITTED / EXACT_BUILD_AND_ASSUMPTION_REPLAY` | run stdout/stderr/environment/source manifest；target SHA `e770c7bf…33e4`；stable manifest `6c2bd66c…b958`；qualification SHA `505b84bb…41d`。 | “global context closed”不消除 theorem type中的 universality、separation、Peirce、CTQ、Q containment、enumerability 与 consistency 参数；不证明 HoTT essentiality、内部矛盾、原创性或现实桥梁。 |

## 追加登记：MP-DEDEKIND-OMEGA-M1（Dedekind-Ω 第一枚·过程层，2026-09-17）

来源：用户 2026-09-17「必须击落 / 执行而非测试」指令（修订片 024）；供给为
`.codex/research/hott/PREMISE-001/008`（SUPPLY-010，F2-7 Dedekind-Ω 簇，唯一命中
`PROCESS_DECLARATION_GAP` 的候选）。本登记是**执行产物**，不是供给单元的候选判定；
`registers_new_claim` 语义 = 候选的非现实性被机械锚定，非已注册数学主张。

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-DEDEKIND-OMEGA-M1` 第04run·重复登记（历史行，身份行为主表第 44 行） | `CAND-F2-7-M1` | `formal/dedekind-omega-missile/MissileOneProcessLayer.agda`；`CLAIM-PACKAGE.md` 固定精确命题、量词、假设与禁止外推；`TOOLCHAIN.json`/`AGDA_LIBRARIES` 固定工具链身份 | `verification/runs/20260917-MP-DEDEKIND-OMEGA-M1-04/`；Agda 2.8.0；Cubical v0.9；`--safe --cubical --guardedness`；exit 0；51s；`-01`–`-03` 保留为被 Gate 使用过的失败 run | `MACHINE_PROVED_LOCAL_UNCOMMITTED / PROCESS_LAYER_GAP_ANCHOR_NOT_HOTT_CONTRADICTION` |

| ID | 主张 | 裁决 | 直接依据 | 禁止外推 |
|---|---|---|---|---|
| CAND-F2-7-M1 | 在纯 Cubical Agda（无 LEM、无 resizing、无追加公理）中，√2 的 Pell 最优有理夹钳序列 `p_n/q_n`（互递推 `p'=p+2q`、`q'=p+q`，初值 (1,1)）的判别式 `D n = p_n²-2q_n²` 恒等于交替 ±1：`pell-gap-never-closes : (n : ℕ) → (D n ≡ 1r) ⊎ (D n ≡ -1r)`，故 `gap-never-zero : (n : ℕ) → ¬ (D n ≡ pos 0)`——夹钳两端在 ℚ 上永不相遇。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED / PELL_GAP_NEVER_CLOSES` | run `20260917-MP-DEDEKIND-OMEGA-M1-04/` 的 `RUN.json`（`KERNEL_ACCEPTED_WITH_SCOPE`，exit 0）、`stdout.txt`、`source-manifest.json`；环恒等式由 `Cubical.Tactics.CommRingSolver` 的 `solve! ℤCommRing` 反射求解。 | **不**声称这是 HoTT 内部矛盾或 HoTT 不一致；**不**声称 `∀ q:ℚ, q·q≠2`（全称无理性，第二枚目标，未证）；**不**声称「实数完备性非现实」可交付；命题本身是 `ℤ` 上的环计算，不依赖 univalence / cubical path / HIT 等 HoTT 特有规则；有限 run 与编译缓存不证明无限域外结论。 |

**语义边界**（修订片 024 §2）：「击落」在本 repo 的唯一可执行读法是把
`PROCESS_DECLARATION_GAP` 的非现实性**数学锚定**，不是在 HoTT 内导出矛盾。
任何把本行读成「HoTT 被证明矛盾」的解读都是误读。

## 追加登记：MP-DEDEKIND-OMEGA-M2（Dedekind-Ω 第二枚·声明层，2026-09-17）

来源：修订片 024 §4（第二枚规格）+ 修订片 025 §5（三枚齐射、M2→M3 链式不可倒置）。
本登记是**执行产物**；`registers_new_claim` 语义 = 候选的非现实性被机械锚定，
非已注册数学主张。

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-DEDEKIND-OMEGA-M2` | `CAND-F2-7-M2` | `formal/dedekind-omega-missile/MissileTwoUniversalIrrationality.agda`；`CLAIM-PACKAGE-M2.md` 固定精确命题、量词、假设与禁止外推 | `verification/runs/20260917-MP-DEDEKIND-OMEGA-M2-01/`；Agda 2.8.0；Cubical v0.9；`--safe --cubical --guardedness`；exit 0；43.9s；`--ignore-interfaces` 全量复检 | `MACHINE_PROVED_LOCAL_UNCOMMITTED / DELIVERY_TYPE_SPEC_B_UNINHABITED_NOT_HOTT_CONTRADICTION` |

| ID | 主张 | 裁决 | 直接依据 | 禁止外推 |
|---|---|---|---|---|
| CAND-F2-7-M2 | 在纯 Cubical Agda（无 LEM、无 resizing、无追加公理）中，`√2-irrational : ∀ q : ℚ → ¬ (q ·ℚ q ≡ 2r)` 与 `spec-B-empty : ¬ (Σ q : ℚ, q ·ℚ q ≡ 2r)` 成立——「输出 √2 的有理位置」任务的交付类型 `Spec_B` 的居住性为空。证明路径：ℚ set quotient 提取（`rec2` 点构造子定义性归约 + `eq/⁻¹` + `Int.abs`）→ ℕ 无穷下降（奇偶工具包 + 平方膨胀 `sq-double` + 偶平方引理 + 手写强归纳）。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED / SPEC_B_EMPTY_UNIVERSAL_IRRATIONALITY` | run `20260917-MP-DEDEKIND-OMEGA-M2-01/` 的 `RUN.json`（`KERNEL_ACCEPTED_WITH_SCOPE`，exit 0，43.9s）、`stdout.txt`、`source-manifest.json`、`environment.txt`；ℚ 为 `Cubical.Data.Rationals.Base` 的 set quotient 标准构造。 | **不**声称这是 HoTT 内部矛盾或 HoTT 不一致；**不**声称「任何过程不停机」的元语言命题（证的是交付类型无居住者；「任何策略不可能交付」为语义读法，按 `ARGUMENT_ANCHORED_ON_MACHINE_PROOVED_FACTS` 交付）；**不**声称「实数完备性非现实」可交付；命题是 ℚ/ℕ 层标准计算，不依赖 univalence / cubical path / HIT 特有规则；开发期编译迭代未另立 run，正式 run 为全量复检。 |

**语义边界**（修订片 025 §6，全套继承 024 §2）：第二枚 = 声明层锚点；第三枚
（识别层 M3-L1）消费本行，序列不可倒置。「击落」的可执行读法不变：非现实性的
数学锚定，不是 HoTT 内部矛盾。

## 追加登记：MP-DEDEKIND-OMEGA-M3（Dedekind-Ω 第三枚·识别层，2026-09-17）

来源：修订片 025 §3/§5（Spec_A/Spec_B 双规格、M3-L1 引理候选、逼选结构、
M2→M3 链式）；供给侧为 GLM 独立分析（025 片 §7 对撞评估采纳）。
本登记是**执行产物**；`registers_new_claim` 语义 = 候选的非现实性被机械锚定，
非已注册数学主张。

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-DEDEKIND-OMEGA-M3` | `CAND-F2-7-M3` | `formal/dedekind-omega-missile/MissileThreeVerdictCollision.agda`；`CLAIM-PACKAGE-M3.md` 固定精确命题、量词、假设与禁止外推 | `verification/runs/20260917-MP-DEDEKIND-OMEGA-M3-01/`；Agda 2.8.0；Cubical v0.9；`--safe --cubical --guardedness`；**LEM 为显式假设 `LEMᵒ`**；exit 0；55.6s | `MACHINE_PROVED_LOCAL_UNCOMMITTED / TASK_IDENTIFICATION_REFUTED_BY_KERNEL_NOT_HOTT_CONTRADICTION` |

| ID | 主张 | 裁决 | 直接依据 | 禁止外推 |
|---|---|---|---|---|
| CAND-F2-7-M3 | 在含第二枚结论的 Cubical Agda 中，`LEMᵒ = (A : Type₀) → isProp A → A ⊎ (A → ⊥)` 为显式假设下：(1) `specA-inhabited : LEMᵒ → Spec_A`——√2 判定表 `f : ℚ → Bool`（`f q ≡ true ↔ q·ℚq < 2r`，逐点由 LEM 定义）作为给定数据居住（过程 A「读出」的数据层合法性）；(2) `M3-L1 : LEMᵒ → ¬ (Spec_A ≃ Spec_B)`——读出任务与算出任务的规格类型不等价（等价传输居住性即与 `spec-B-empty` 矛盾）。核拒绝「读出 = 算出」的任务同一性；理论把二者当同一任务使用的位置在前提层（Book §11.2 Ω 依赖链）。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED / SPECA_INHABITED_LEM_CONDITIONAL_AND_M3_L1` | run `20260917-MP-DEDEKIND-OMEGA-M3-01/` 的 `RUN.json`（`KERNEL_ACCEPTED_WITH_SCOPE`，exit 0，55.6s）、`stdout.txt`、`source-manifest.json`（含 M2 源码哈希——消费依赖）；`isProp<` 来自 `Cubical.Data.Rationals.Order`。 | **不**声称 HoTT 不一致；**不**声称爆炸原理被点燃；**不**声称用户第③件事（A=B）内部可证——M3-L1 恰证明其在判据 J=规格等价下被核否定；寻找使 ③ 可证的 J 等价于寻找 HoTT(+LEM) 不一致性证明，登记为开放前沿、不预设不追逐；**不**声称 Spec_A 无条件居住（LEM 显式假设 = Ω 依赖链的证据）；逼选「两支都命中」为论证（`ARGUMENT_ANCHORED_ON_MACHINE_PROOVED_FACTS`，锚 = M1+M2+M3 收据 + §11.2 逐字定位），非单一机器定理。 |

**语义边界**（修订片 025 §6）：三枚齐射的层关系——第一枚 = 过程层、第二枚 =
声明层、第三枚 = 识别层；链式（M3 消费 M2）。「炸弹在前提里，不在核里」；
「击落」的可执行读法不变：`PROCESS_DECLARATION_GAP` 非现实性的数学锚定
（现含第三条「识别腿」），不是 HoTT 内部矛盾。

## 追加登记：MP-DEDEKIND-OMEGA-TA（第四弹·靶 A 路径 (i)——canonicity 反例的元层检查演示，2026-09-17）

来源：修订片 027 §3.1 靶 A + §3.2 打法原则 + §4（拒证二元性）+
`CanonicityCounterexample-DESIGN.md`（路径 (i) 设计）。`registers_new_claim:
false`；**状态为元层工具检查记录（META_TOOL_CHECKED），不冒充对象层
MACHINE_PROVED 定理**（027 §4 边界）。

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-DEDEKIND-OMEGA-TA` | `CAND-F2-7-TA` | `formal/dedekind-omega-missile/MissileFourTargetA-UACounterexample.agda`（UA-作公理反例项：`n = if subst (λX→X) (ua not not not-not not-not) true then 0 else 1`）+ 探针/对照三件（ProbeControl/ProbeZero/ProbeSucZero）；`CanonicityCounterexample-DESIGN.md` | runs `20260917-MP-DEDEKIND-OMEGA-TA-01`（主模块 exit 0）/`-02`（对照 exit 0）/`-03`（探针 exit 1，**预期失败即收据**）/`-04`（探针 exit 1，预期失败即收据）；TA-03/04 错误消息含 n 的卡住范式 `if transp (λ i → e i) i0 true then zero else 1`——内核亲自打印中性范式 | `META_TOOL_CHECKED / CANONICITY_BREAKAGE_DEMONSTRATED_NOT_OBJECT_PROOF_NOT_INCONSISTENCY` |

| ID | 主张 | 裁决 | 直接依据 | 禁止外推 |
|---|---|---|---|---|
| CAND-F2-7-TA | UA-作公理（postulate，无计算规则）注入下，存在闭 ℕ 项 `n = if b' then 0 else 1`（`b' = subst (λX→X) (ua not not not-not not-not) true`），其范式为中性卡住形态——内核对 `n ≡ zero` 与 `n ≡ suc zero` 的 refl 均判不可互换（TA-03/04 错误消息含 n 的完整卡住范式），对照探针同法通过（TA-02）。即：UA-作公理时 canonicity 被收费——「显式化并丧失完成义务」支的 UA 实例演示。 | `META_TOOL_CHECKED / CANONICITY_BREAKAGE_DEMONSTRATED` | runs `20260917-MP-DEDEKIND-OMEGA-TA-01`（主模块 exit 0）/`20260917-MP-DEDEKIND-OMEGA-TA-02`（对照 exit 0）/`20260917-MP-DEDEKIND-OMEGA-TA-03`/`20260917-MP-DEDEKIND-OMEGA-TA-04`（探针 exit 1，错误消息存档 stdout.txt）；构造草图 = 027 §3.1 靶 A + DESIGN 文档。 | **不**声称 HoTT 不一致（非规范 ≠ 矛盾，027 §8）；**不**声称本演示为对象层定理（元层工具检查记录，027 §4）；**不**声称覆盖全部 canonicity 破坏形态（Huber 完整结果仍为 `SOURCE_REPORTED_NOT_REPLAYED`）；刻意无 `--safe` 的 postulate 注入是演示内容本身，非工程疏忽。 |

## 追加登记：MP-DEDEKIND-OMEGA-M3-UNC（第四弹首靶·M3 去条件化 + 027 §5 核实，2026-09-17）

来源：修订片 027 §5（待核发现与债务定位）+ §2（身份陈述与主定理模式）。本包为
第三弹识别层收据的去条件化加强，同时为第四弹靶 B（对齐矩阵）登记 ℚ 层免费格。
`registers_new_claim` 语义 = 候选锚点，非已注册数学主张。

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-DEDEKIND-OMEGA-M3-UNC` | `CAND-F2-7-M3-UNC` | `formal/dedekind-omega-missile/MissileThreeUnconditional.agda`（复用 M3 的 Spec_A/Spec_B 类型与 M2 的 spec-B-empty）；`CLAIM-PACKAGE-M3-UNC.md` | `verification/runs/20260917-MP-DEDEKIND-OMEGA-M3-UNC-01/`；Agda 2.8.0；Cubical v0.9；`--safe --cubical --guardedness`；**无 LEM、无 resizing、无任何追加假设**；exit 0；55.6s | `MACHINE_PROVED_LOCAL_UNCOMMITTED / SPEC_A_UNCONDITIONAL_AND_IDENTIFICATION_REFUTED_NOT_HOTT_CONTRADICTION` |

| ID | 主张 | 裁决 | 直接依据 | 禁止外推 |
|---|---|---|---|---|
| CAND-F2-7-M3-UNC | 在纯 Cubical Agda（无 LEM、无 resizing、无任何追加假设）中：(1) `specA-inhabited-unc : Spec_A` 无条件居住——判定表 `f : ℚ → Bool`（`f q ≡ true ↔ q·ℚq < 2r`）由 ℚ 序可构造判定 `_≟_ : (m n : ℚ) → Trichotomy m n` 直接定义，不需要 LEM（027 §5 待核发现**核实为真**）；(2) `M3-L1-unc : ¬ (Spec_A ≃ Spec_B)` 识别拒绝去条件化。债务定位：判定表在 ℚ 层免费，理想元素本体（判定表升格为实数层对象、完整 cut）才收费——完成义务在承载层跨界处收费。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED / SPEC_A_UNCONDITIONAL_AND_IDENTIFICATION_REFUTED` | run `20260917-MP-DEDEKIND-OMEGA-M3-UNC-01/` 的 `RUN.json`（`KERNEL_ACCEPTED_WITH_SCOPE`，exit 0，55.6s）与收据文件；`_≟_`/`isIrrefl<`/`isAsym<` 来自 `Cubical.Data.Rationals.Order`。 | **不**声称 HoTT 不一致；**不**推翻 M3 条件版收据（条件版仍真，本版为去条件化加强）；**不**声称完整 cut / 实数对象已无条件构造（「升格处收费」为语义读法与靶位指引）；不可证性证书属元理论（027 §4 拒证二元性），本包是对象层拒绝收据。 |

## 追加登记：MP-DEDEKIND-OMEGA-BP（Dedekind-Ω 簇·廉价副产品，2026-09-17）

来源：修订片 025 §5 保留项（「序列层存在命题可判定、搜索过程不可停机」须
分开登记；非第三枚，不得冒充识别层）。

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-DEDEKIND-OMEGA-BP` | `CAND-F2-7-BP` | `formal/dedekind-omega-missile/MissileByproductGapDecidable.agda`（消费 M1 的 `D`/`gap-never-zero`） | `verification/runs/20260917-MP-DEDEKIND-OMEGA-BP-01/`；Agda 2.8.0；Cubical v0.9；exit 0；60.6s | `MACHINE_PROVED_LOCAL_UNCOMMITTED / GAP_DECIDABLE_AND_NO_WITNESS_DISTINGUISHED` |

| ID | 主张 | 裁决 | 直接依据 | 禁止外推 |
|---|---|---|---|---|
| CAND-F2-7-BP | `decGapAt : (n : ℕ) → (D n ≡ pos 0) ⊎ ¬ (D n ≡ pos 0)`——序列层存在命题的逐点判定是已完成对象（判定为「否」）；`noGapWitness : ¬ (Σ n : ℕ, D n ≡ pos 0)`——Σ 居住性否定，与第二枚 `spec-B-empty` 同形、证据路径独立（Pell 不变量 vs 下降法）。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED / DECIDABLE_OBJ_VS_UNHALTING_SEARCH` | run `20260917-MP-DEDEKIND-OMEGA-BP-01/` 的 `RUN.json`（exit 0，60.6s）与收据文件。 | 本登记机械确认「判定已完成 ≠ 搜索不终止」的区分（025 片 §5 更正的根据）；**不**声称它是 A=B 对撞或第三枚；**不**声称 HoTT 不一致。 |

## 追加登记：MP-DEDEKIND-OMEGA-GOLD（金形态 cut·第一装配期，2026-09-17；**已被 -02 四条件完整版取代**）

> 2026-09-18 注：本节 proof 行已**降格为历史行**（`MP-DEDEKIND-OMEGA-GOLD` 的唯一
> 身份行是下方「四条件完整版」节的 -02 行——`verify_formal_proof_run.py` 要求每个
> proof_id 在当前矩阵唯一；GOLD-01 run 保留为部分装配期历史收据，见下节 claim 行
> 的「GOLD-01 保留为部分装配期历史收据」）。roundedL←/roundedU← 已在 -02 完成。

来源：修订片 027 §5/§9（金形态 cut 构造）+ CutGoldForm-DESIGN.md（勘误版，
plan-revise `0150b29`：U 须带正性合取——初版 `U q := 2r <ℚ q·ℚq` 的「负数自然
不在上集」为假，反例 q=−2 同时入 L 与 U、破坏不交性）。本包登记金形态的
**已装配部分**：ℚ 序算术基础设施（CutInfra，crux）+ 四条件中的
inhabited×2 / disjoint / rounded→→ / located；roundedL← 与 roundedU← 为
显式登记的未装配义务（见下）。

| Package ID（历史行） | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-DEDEKIND-OMEGA-GOLD` 第01run·部分装配（历史，superseded by -02） | `CAND-F2-7-GOLD` | `formal/dedekind-omega-missile/CutInfra.agda`（`<-≤`、`·-mono-≤-nn` crux、`·-mono-<-nn`）+ `formal/dedekind-omega-missile/CutGoldForm.agda`（勘误版 L/U + isProp + hProp 包装 + inhabited×2 + disjoint + roundedL→ + roundedU→ + located，eq 支消费 M2 的 `√2-irrational`）；`CLAIM-PACKAGE-GOLD.md` | `verification/runs/20260917-MP-DEDEKIND-OMEGA-GOLD-01/`；Agda 2.8.0；Cubical v0.9；`--safe --cubical --guardedness`；**无 LEM、无 resizing、无任何追加假设**；exit 0；stderr 0 | `MACHINE_PROVED_LOCAL_COMMITTED_NOT_PUSHED / GOLD_FORM_PARTIAL_ASSEMBLY_NOT_HOTT_CONTRADICTION`（证据随 commit `615fbd2` 入库；未 push，非 VERSION_CLOSED） |

| ID | 主张 | 裁决 | 直接依据 | 禁止外推 |
|---|---|---|---|---|
| CAND-F2-7-GOLD | 在纯 Cubical Agda 中：(1) `·-mono-≤-nn : (k a b : ℚ) → 0r ≤ k → a ≤ b → k·ℚa ≤ k·ℚb` 与 `·-mono-<-nn : 0r < k → a < b → k·ℚa < k·ℚb`（0022 §二.1 定案的 elimProp3+代表元 ℤ 链+`≤-·o` 路线；lib 无 ℚ 乘法单调性引理的缺口已补）；(2) 勘误版谓词 `L q := (q<0r) ⊎ ((0r≤q)×(q·ℚq<2r))`、`U q := (0r<q)×(2r<q·ℚq)` 均为 hProp 值（`Lₚ`/`Uₚ`），且 Book §11.2 四条件中的 inhabitedL/inhabitedU/disjoint（`L q → U r → q < r`）/roundedL→/roundedU→/located（`q<r → L q ⊎ U r`）全部机器检查通过——located 的 `q²≡2r` 支消费 `√2-irrational`。 | `MACHINE_PROVED_LOCAL_COMMITTED_NOT_PUSHED / GOLD_FORM_PARTIAL_ASSEMBLY`（commit `615fbd2`） | run `20260917-MP-DEDEKIND-OMEGA-GOLD-01/` 的 `RUN.json`（`KERNEL_ACCEPTED_WITH_SCOPE`，exit 0，stderr 0）与收据文件；`source-manifest.json` 固定 CutGoldForm/CutInfra/M2 哈希。 | **未装配部分不得冒充已证**：`roundedL←`（`L q → ∃ p, q<p × L p`）与 `roundedU←`（`U r → ∃ q, q<r × U q`）未装配——已登记工程障碍：**依赖代表元的见证（如 (4ab+1)/(4b²)、Pell 中项 (3a+4b)/(2a+3b)）在商上不良定义**，须走内在 ℚ 项路线（δ := (2−q²)·¼ 类；U 侧须 `inv`（代表交换 (a,b)↦(b,a) 可经 rec 良定义）），并先补 ℚ 加法/减法与 ℚ 级乘法消去基础设施；**不**声称 Book §11.2 四条件全部完成；**不**声称 HoTT 不一致；**不**声称 LEM 收费位置（ℝ 层塌缩处）已被机械化（按 DESIGN §4 仅登记）；本包构造是 ℚ 层标准计算，不依赖 univalence / cubical path / HIT 特有规则。 |

## 追加登记：MP-DEDEKIND-OMEGA-GOLD（金形态 cut·四条件完整版，2026-09-18）

接续第一装配期（`615fbd2`，rounded→ 双向 + located）与 δ 路线基础设施（`4bc020d`，
`roundedL←` 完整过核）。本节登记 **Book §11.2 四条件首次全部机器接受**：在
`roundedU←`（上集圆整 ← 方向）补齐后，`CutGoldForm.agda` 全模块 exit 0。

| proof_id | claim_id | 源码 / 包 | 运行收据 | 证据等级 |
|---|---|---|---|---|
| `MP-DEDEKIND-OMEGA-GOLD` | `CAND-F2-7-GOLD` | `formal/dedekind-omega-missile/CutInfra.agda`（`<-≤`、`·-mono-≤-nn` crux、`·-mono-<-nn`）+ `formal/dedekind-omega-missile/CutGoldForm.agda`（勘误版 L/U + isProp + hProp 包装 + inhabited×2 + disjoint + rounded→ 双向 + located + **roundedL← + roundedU← 双向见证方向**，δ := t·¼r 内在路线 + `sq-minus` 差平方展开）；`CLAIM-PACKAGE-GOLD.md` | `verification/runs/20260918-MP-DEDEKIND-OMEGA-GOLD-02/`（`--ignore-interfaces` 全量 clean 重放）；Agda 2.8.0；Cubical v0.9；`--safe --cubical --guardedness --two-level`；**无 LEM、无 resizing、无任何追加假设**；exit 0；stderr 0；stdout 哈希与 GOLD-01 一致（同一依赖树，均为纯检查日志） | `MACHINE_PROVED_LOCAL_COMMITTED_NOT_PUSHED / GOLD_FORM_FOUR_CONDITIONS_COMPLETE`（证据随 commit `f2fd012` 入库；未 push，非 VERSION_CLOSED） |

| claim | 命题（机器检查形态） | 证据等级 | 证据 | 禁止外推 |
|---|---|---|---|---|
| CAND-F2-7-GOLD-FULL | 在纯 Cubical Agda 中：(1) `·-mono-≤-nn : (k a b : ℚ) → 0r ≤ k → a ≤ b → k·ℚa ≤ k·ℚb` 与 `·-mono-<-nn : 0r < k → a < b → k·ℚa < k·ℚb`；(2) 勘误版谓词 `L q := (q<0r) ⊎ ((0r≤q)×(q··ℚq<2r))`、`U q := (0r<q)×(2r<q··ℚq)` 均为 hProp 值（`Lₚ`/`Uₚ`）；(3) Book §11.2 四条件 **全部** 机器检查通过——inhabitedL、inhabitedU、disjoint（`L q → U r → q < r`）、rounded 双向（`roundedL→`/`roundedU→` 与 **`roundedL←`/`roundedU←`**：`L q → ∃ p, q<p × L p`、`U r → ∃ q, q<r × U q`，δ 内在路线，U 侧 `q := r - (r·r-2r)·¼r`）、located（`q<r → L q ⊎ U r`，eq 支消费 `√2-irrational`）。 | `MACHINE_PROVED_LOCAL_COMMITTED_NOT_PUSHED`（commit `f2fd012`） | run `20260918-MP-DEDEKIND-OMEGA-GOLD-02/` 的 `RUN.json`（`KERNEL_ACCEPTED_WITH_SCOPE`，exit 0，stderr 0，duration 73.2s）与收据五件套；`source-manifest.json` 固定 CutGoldForm/CutInfra/DESIGN/compile.sh 哈希；GOLD-01 保留为部分装配期历史收据。 | **边界**：(a) 这是 **ℚ 层单个 cut（√2）** 的四条件构造，**不**声称 Book §11.2 意义下「实数完备性」「ℝ 不可达」或任何 ℝ 层命题——把 cut 取等价类、把「ℝ 取值命题」塌缩到单一 Ω 的下一升格仍需 LEM 或 propositional resizing（DESIGN §4 登记的收费位置，未机械化）；(b) **不**声称 HoTT/立方类型论内部矛盾或不一致；(c) `rounded←` 的 witness 是 ℚ 层显式 δ 项，**不**依赖代表元选择；(d) registers_new_claim:false——ℚ 层标准可构造计算，非 HoTT 元定理，不依赖 univalence / HIT 特有规则。 |
## 追加登记：MP-DEDEKIND-OMEGA-TA-AC（靶 A·AC 格 stuckness 演示，2026-09-17 收据 / 2026-09-18 补登记）

来源：修订片 027 §2.2（显式化 surface）+ §3.2 打法原则 +
`MissileFourChargeDemo.agda`（收费演示二：AC 格）+ `ALIGNMENT-MATRIX-F2.md` 的
F2-4 格。源码、双探针与收据五件套随 commit `9be3cbe` 入库；**矩阵行此前缺失**
（收据 `RUN.json` 的 `index_status: INDEXED_IN_CLAIM_EVIDENCE_MATRIX` 未兑现），
本节为补登记。`registers_new_claim:false`——元层工具检查记录（META_TOOL），
不冒充对象层定理（027 §4 拒证二元性）。

| proof_id | claim_id | 源码 / 包 | 运行收据 | 证据等级 |
|---|---|---|---|---|
| `MP-DEDEKIND-OMEGA-TA-AC` | `CAND-F2-7-TA-AC` | `formal/dedekind-omega-missile/MissileFourChargeDemo.agda`（postulate `P : ℕ → ℕ → Set` + `ch : (n : ℕ) → Σ[ k ∈ ℕ ] P n k`；闭项 `n-ac = ch 0 .fst`）+ 探针双件 `MissileFourTargetA-ProbeACZero.agda` / `MissileFourTargetA-ProbeACSuc.agda` | runs `20260917-MP-DEDEKIND-OMEGA-TA-AC-01`（`n-ac ≡ zero` 的 refl 被核拒绝，exit 1 记录值，**预期失败即收据**）／`-02`（`n-ac ≡ suc zero` 被拒）；错误消息分别打印中性卡住范式 `ch 0 .fst != zero` / `ch 0 .fst != 1`；Agda 2.8.0-3d04bac；Cubical v0.9；`--cubical --guardedness`（刻意无 `--safe`：postulate 注入是演示内容本身，非工程疏忽） | `META_NEGATIVE_CHECK_AS_EXPECTED / AC_AXIOM_STUCKNESS_DEMONSTRATED_NOT_OBJECT_PROOF_NOT_INCONSISTENCY`（证据随 commit `9be3cbe` 入库；未 push，非 VERSION_CLOSED） |

| claim | 命题（机器检查形态） | 证据等级 | 证据 | 禁止外推 |
|---|---|---|---|---|
| CAND-F2-7-TA-AC | AC 格（公理化选择函数 `ch : (n : ℕ) → Σ[ k ∈ ℕ ] P n k` 以 postulate 注入，无计算规则）下，闭 ℕ 项 `n-ac = ch 0 .fst` 的范式为中性卡住形态——内核对 `n-ac ≡ zero`（TA-AC-01）与 `n-ac ≡ suc zero`（TA-AC-02）的 refl 均判不可互换，错误消息分别含 `MissileFourChargeDemo.ch 0 .Cubical.Foundations.Prelude.fst != zero` 与 `!= 1`。与 TA（UA 格，`9d4b3c5`）同法的 stuckness 演示，构成 027 §2.2「显式化 surface」的第二个机械实例。 | `META_NEGATIVE_CHECK_AS_EXPECTED`（commit `9be3cbe`） | runs `20260917-MP-DEDEKIND-OMEGA-TA-AC-01 / 20260917-MP-DEDEKIND-OMEGA-TA-AC-02` 的 `RUN.json`（`META_NEGATIVE_CHECK_AS_EXPECTED`，stderr 0）、`stdout.txt`（内核拒绝消息 + 中性范式）、`source-manifest.json`（固定 ProbeACZero / ProbeACSuc / ChargeDemo / TOOLCHAIN / AGDA_LIBRARIES 哈希）。**收据完整性注**：当前机器按 `command_argv` 重放 TA-AC-01，stdout/stderr 与收据**逐位一致**（431B，sha256 `f7b37d65…`），但退出码观察为 42 而收据字段记 1——内核拒绝证据完全可复现，仅 exit_code 整数字段为记录偏差（同见的还有 TA-03/04）；不予改写历史收据，在此如实登记。 | **不**声称 HoTT 不一致（公理注入导致的非规范是已知元定理现象，非矛盾，027 §8）；**不**声称「不可归约」已被内部证明——本包是**负向探针**（refl 被核拒绝）+ 内核亲自打印卡住范式，不是对象层 `¬ (n-ac ≡ zero)` 的证明（027 §4 拒证二元性）；**不**声称覆盖全部显式假设收费形态（LEM 格见下节 `MP-DEDEKIND-OMEGA-TA-LEM`，UA 格见 `CAND-F2-7-TA`，Huber 完整结果仍为 `SOURCE_REPORTED_NOT_REPLAYED`）；exit≠0 是**预期失败即收据**，非工程失败；`registers_new_claim:false`。 |

## 追加登记：MP-DEDEKIND-OMEGA-TA-LEM（靶 A·LEM 格 stuckness 演示，2026-09-18）

来源：修订片 027 §2.2（显式化 surface）+ `MissileFourChargeDemo.agda`（收费演示一：
LEM 格）。该演示此前仅在源码注释中声明（「内核照样接受闭的 ℕ 项 n-lem / n-ac——
但这两个项的头部符号是公理应用」），AC 格已有探针收据而 **LEM 格无收据**——
本轮（四弹全面审计）发现并补齐：两个负向探针分别核判 `n-lem` 不归约到 `zero` /
`suc zero`。与 TA（UA 格）/ TA-AC（AC 格）完全同法。`registers_new_claim:false`。

| proof_id | claim_id | 源码 / 包 | 运行收据 | 证据等级 |
|---|---|---|---|---|
| `MP-DEDEKIND-OMEGA-TA-LEM` | `CAND-F2-7-TA-LEM` | `formal/dedekind-omega-missile/MissileFourChargeDemo.agda`（postulate `LEM : (A : Set) → A ⊎ (A → ⊥)`；闭项 `n-lem` 由 `with LEM ℕ` 的分支定义）+ 探针双件 `MissileFourTargetA-ProbeLEMZero.agda` / `MissileFourTargetA-ProbeLEMSuc.agda` | runs `20260918-MP-DEDEKIND-OMEGA-TA-LEM-01/-02`（历史；依赖闭包不完整）+ **`20260919-MP-DEDEKIND-OMEGA-TA-LEM-03/04`（当前：A04 命名精确化 + 补全闭包 pin ChargeDemo；同命题 refl 拒绝，exit 42 预期失败即收据）**；`--ignore-interfaces` 全量复检形态（与 M1-04/M2-01/GOLD-02 同款确定性可重放 argv）；错误消息分别打印中性卡住范式 `n-lem \| MissileFourChargeDemo.LEM ℕ != zero` 与 `!= 1`（头部 = 公理化 LEM 应用的 with 归约）；Agda 2.8.0-3d04bac；Cubical v0.9；`--cubical --guardedness`（刻意无 `--safe`：postulate 注入是演示内容本身，非工程疏忽） | `META_NEGATIVE_CHECK_AS_EXPECTED / OPAQUE_LEM∞_POSTULATE_STUCKNESS_DEMONSTRATED_NOT_OBJECT_PROOF_NOT_INCONSISTENCY`（**身份修正（A04）**：公设为不受限排中 LEM∞ 型，非 Book LEM₋₁；Book thm:not-lem：LEM∞+UA 不相容（SOURCE_REPORTED）——组合系统按 Book 不一致，stuckness 演示不依赖该不一致性；证据随本轮提交入库；未 push，非 VERSION_CLOSED） |

| claim | 命题（机器检查形态） | 证据等级 | 证据 | 禁止外推 |
|---|---|---|---|---|
| CAND-F2-7-TA-LEM | LEM 格（公理化排中律 `LEM : (A : Set) → A ⊎ (A → ⊥)` 以 postulate 注入，无计算规则）下，闭 ℕ 项 `n-lem`（`with LEM ℕ` 分支归约）的范式为中性卡住形态——内核对 `n-lem ≡ zero`（TA-LEM-01）与 `n-lem ≡ suc zero`（TA-LEM-02）的 refl 均判不可互换。与 TA-AC（AC 格，`9be3cbe`）/ TA（UA 格，`9d4b3c5`）结构对称，三者合取 = 027 §2.2「显式化 surface」三类公理注入的 stuckness 机械演示。 | `META_NEGATIVE_CHECK_AS_EXPECTED`（本轮提交） | runs `20260918-MP-DEDEKIND-OMEGA-TA-LEM-01 / 20260918-MP-DEDEKIND-OMEGA-TA-LEM-02` 的 `RUN.json`（`META_NEGATIVE_CHECK_AS_EXPECTED`，exit 42，stderr 0）、`stdout.txt`、`environment.txt`、`source-manifest.json`（固定 ProbeLEMZero / ProbeLEMSuc / ChargeDemo / TOOLCHAIN / AGDA_LIBRARIES 哈希）。**可重放性已现场双重验证**：按 `RUN.json` 的 `command_argv`（`/usr/bin/env` + XDG 环境 + `--ignore-interfaces`，自包含、不依赖接口缓存状态）从仓库根独立重放两次，exit / stdout / stderr 与收据**逐位一致**（stdout 3117B / 3108B，exit 42）。 | **不**声称 HoTT 不一致（公理注入导致的非规范是已知元定理现象，非矛盾，027 §8）；**不**声称「不可归约」已被内部证明——本包是**负向探针**（refl 被核拒绝）+ 内核亲自打印卡住范式，不是对象层 `¬ (n-lem ≡ zero)` 的证明（027 §4 拒证二元性）；**不**声称 LEM 的对象层后果（M3 的 `LEMᵒ` 假设用法与 M3-UNC 的去条件化仍是对象层收据，本包仅在元层演示 canonicity 收费）；exit≠0 是**预期失败即收据**，非工程失败；`registers_new_claim:false`。 |

## 追加登记：MP-DEDEKIND-OMEGA-REAL-LAYER（Book §11.2「ℝ 层」陈述精确化 B0 + 充裕性 B1a，2026-09-18）

来源：修订片 029 §4.1（第一前置任务：陈述精确化，不可跳过）。本节钉死收费命题的
精确形态、登记 (b′) 路径 1 的可行性裁定（B0），并证明 (a) 充裕性方向（B1a，run `-02`）。
`registers_new_claim:false`。

**B0 陈述勘误（三项：2026-09-18 ×2 + 2026-09-19 ×1；勘误细节见
`CLAIM-PACKAGE-REAL-LAYER.md` 勘误节）**：
3. **located 析取忠实化**（Astra 审计 A02 采纳）：Book §3.7 Defn (logical
   notation) 逐字 `P ∨ Q ≝ ∥P+Q∥`；原 `dcut` 的 located 用裸 `⊎`（携带分支
   选择数据的强化变体）。修正后六分量全部 mere proposition，`isPropDCut` 成立，
   与 Book「dcut(L,U) is a mere proposition」逐字一致。B1a 构造结构不变，
   run `-03` 重新过核。`-01`/`-02` 保留为勘误前变体的历史收据。
   **另（Astra A08/A09 采纳）**：NECESSITY-LEM-02 补 pin 定义 owner
   CutRealLayer；GOLD-03 补 pin M2（√2-irrational 消费）；verifier 的
   `--safe` 检查改为 OPTIONS pragma 实际解析（TA-01 作为公设控制在新检查下
   正确 FAIL，其收据属控制类非 safe 证明类——原 PASS 系注释文字误命中，
   Astra A09 指认成立）。
1. `dcut` 存在量词忠实化：Book §11.2 Defn 11.2.1 的 `\exis` 在 HoTT 中是命题截断，
   inhabited×2 / rounded×2 右侧由裸 `Σ` 改为 `∥_∥₁`（裸 `Σ` 非 prop，被 `≃` 强制为
   prop 时对非平凡 cut 不可满足）。
2. `Sufficiency` 付费假设深化（B0 深化）：由 `PropResizing ℓ →` 收窄为
   `SingleOmega ℓ →`（pointwise PropResizing 不蕴含整体 hProp ℓ 塌缩；Book 取法 2
   原文的忠实形态是「存在低层级 Ω」）。`Necessity` 侧不受影响（B0 时已是 SingleOmega）。

| proof_id | claim_id | 源码 / 包 | 运行收据 | 证据等级 |
|---|---|---|---|---|
| `MP-DEDEKIND-OMEGA-REAL-LAYER` | `CAND-F2-7-REAL-LAYER` | `formal/dedekind-omega-missile/CutRealLayer.agda`（`PropResizing` / `LEMProp` 公理形态；`SingleOmega`（基层级命题塌缩结构）；Defn 11.2.1 四条件的量词显式形态 `dcut`（含 ∥_∥₁ 截断勘误）；`DedekindReals`；`ℝLayerAt`（实数作为基层级已完成集合对象）；方向类型 `Sufficiency`（= `SingleOmega ℓ → ℝLayerAt ℓ`）/ `Necessity`；**B1a 证明体 §7**：`isSetDCut` / `DedekindReals-isSet` / `DedekindReals*-isSet`（代理空间）/ `Σ-cong-iso-fst-cross`（跨层 Σ-cong 自克隆，库版钉同层）/ `sufficiency`）+ `ProbeCrossIso.agda`（`isoToEquiv` 跨层探针）+ `CLAIM-PACKAGE-REAL-LAYER.md`（Book §11.2 逐字原文转写 + 逐项对照 + §3 可行性裁定 + 勘误节） | runs `20260918-MP-DEDEKIND-OMEGA-REAL-LAYER-01`（statement 阶段，`--ignore-interfaces` 全量确定性可重放 argv；exit 0；**源码 hash 已因两项 B0 勘误过期，陈述以 `-02` 的源 manifest 为准**）；`20260918-MP-DEDEKIND-OMEGA-REAL-LAYER-02`（B1a 证明体全量重查；exit 0；**勘误二形态，勘误三后为历史收据**）；**`20260919-MP-DEDEKIND-OMEGA-REAL-LAYER-04`（当前陈述依据：located ∥⊎∥ 截断（勘误三）+ isPropDCut + B1a 重查；Agda 2.8.0-3d04bac；Cubical v0.9；`--safe --cubical --guardedness --two-level`；exit 0；stderr 0）** | B0：`STATEMENT_ACCEPTED_WITH_SCOPE / CHARGED_PROPOSITION_PINNED_NOT_PROVED`（经三项勘误后由 `-03` 源码背书）；**B1a：(a) 充裕性 `sufficiency : (ℓ : Level) → SingleOmega ℓ → ℝLayerAt ℓ` = `MACHINE_PROVED_WITH_SCOPE`**（无 postulate，收费假设为显式前提；证据随本轮提交入库；未 push，非 VERSION_CLOSED） |

| claim | 命题（机器检查形态） | 证据等级 | 证据 | 禁止外推 |
|---|---|---|---|---|
| CAND-F2-7-REAL-LAYER | Book §11.2 的「ℝ 层」收费命题被钉死为精确类型：`ℝLayerAt ℓ = Σ[ R ∈ Type ℓ ] (isSet R × (R ≃ DedekindReals ℓ))`，其中 `DedekindReals ℓ = Σ[ LU ∈ (ℚ → hProp ℓ) × (ℚ → hProp ℓ) ] dcut (fst LU) (snd LU)`，`dcut` 为 Defn 11.2.1 四条件的量词显式形态（inhabited×2 / rounded×2 为 `∥ Σ … ∥₁` 命题截断形态且 rounded 双向 `≃`；disjoint `¬ (L q × U q)`；located `(q < r) → ∥ L q ⊎ U r ∥₁`，Book ∨ 截断记号，勘误三后形态；三项勘误史见本节头部与 CLAIM-PACKAGE §3-E）；付费方式精确化为 `PropResizing ℓ`（取法 2）与 `LEMProp ℓ`（取法 3）；「单一 Ω」精确化为 `SingleOmega ℓ = Σ[ Ω ∈ Type ℓ ] (isSet Ω × (Ω ≃ hProp ℓ))`。**关键裁定（§3）**：Book §11.2 取法 4（初始 σ-frame）证伪了「ℝ层 ⇒ LEM 或 resizing」的直接必要性，故 `Necessity ℓ` 收窄为 `ℝLayerAt ℓ → SingleOmega ℓ`，并按 029 §2 降格条款登记为 `CONJECTURE`。**(a) 充裕性已机器证明（B1a）**：`sufficiency : (ℓ : Level) → SingleOmega ℓ → ℝLayerAt ℓ`——给定基层级 Ω 与 `Ω ≃ hProp ℓ`，代理空间 `DedekindReals*`（Ω-值 cut 的子集型）活在 ℓ 层、是 set、且 `≃ DedekindReals ℓ`（经逐点 e 搬运的载体 iso + 跨层 Σ-cong）。 | **(a) 充裕性 `MACHINE_PROVED_WITH_SCOPE`**（B1a，run `-02`，纯构造无 postulate）；(b′) 必要性维持 `CONJECTURE` | run `20260918-MP-DEDEKIND-OMEGA-REAL-LAYER-02`（勘误二形态，历史）与 **`20260919-MP-DEDEKIND-OMEGA-REAL-LAYER-04`（当前）** 的 `RUN.json`（`KERNEL_ACCEPTED_WITH_SCOPE`，exit 0，stderr 0）与收据五件套；`source-manifest.json` 固定 CutRealLayer（含勘误后陈述与 B1a 证明体）/ TOOLCHAIN / AGDA_LIBRARIES 哈希；statement 阶段历史收据 `-01`（其源 hash 因 B0 勘误过期，已在本节头部登记）；逐字原文转写于 `CLAIM-PACKAGE-REAL-LAYER.md §1`（源：`HoTT/theory-schema/upstream/book-578b85cc/reals.tex` §11.2）；勘误节登记两项陈述修订。 | **(b′) 必要性 `Necessity ℓ` 未证并维持 `CONJECTURE`**（029 §2 条款；`SingleOmega` 与 `PropResizing` 的等价/蕴含方向未论证）；**「收费位置」判词（不可免费/击落）在 (b′) 证明出现前不得升级为 `MACHINE_PROVED`——B1a 证明的只是「付费即得」，不是「必付费」**；**不**声称等价定理已证、resizing/LEM 必要性已证、ℝ 层完备性已证；**不**声称 HoTT 不一致；**确认** ℚ 层四条件已机器证明（GOLD-02 收据，本表前节）；B1a 证明形态为「假设作为显式前提的构造性蕴含」，偏离 checklist 原计划的 postulate 形态（已登记，属加强而非减弱）；`registers_new_claim:false`。 |

## 追加登记：B 线收官（B1b 诊断绕过结局 + B1b′/B2 降格确认 + B3 基准，2026-09-18，修订片 030）

> 本节登记 029 §2「两个都要」合同的收官侧。**B1b/B1b′/B2 的论断全部为元层分析
> （`AI_ADJUDICATED_PENDING_EXTERNAL_AUDIT`），非内核收据**；机器证据仅限本表
> 各节既有 run。`registers_new_claim:false`。

| 项 | 结局（机器检查形态） | 证据等级 | 证据 | 禁止外推 |
|---|---|---|---|---|
| **B1b 诊断绕过** | 零付费读法**失败**：(i) 直接构造撞尺码墙（载体 `(ℚ→hProp ℓ₀)` 活在 `Type (ℓ-suc ℓ₀)`，使 cut 降到 ℓ₀ 的 `Ω : Type ℓ₀` 即 `SingleOmega` 本身）；(ii) σ-frame（Book 取法 4）是**换靶**（σ-frame-值 cut 的另一套实数，非钉死的 `DedekindReals`）+ 新费（HIT-II 与比较义务）。换币读法**原则上存在**：(iii) Cauchy 实数免费活在 `Type₀`，但 `≃ DedekindReals` 需可数选择类原则（元层引述）。 | `META_ANALYSIS_REGISTERED`（诊断对照，非证明） | 修订片 030 §2（三路线逐条 + Book §11.2 取法 4 逐字在 CLAIM-PACKAGE §1.1）；尺码墙的机器面 = `CutRealLayer.agda` 宇宙层级（REAL-LAYER-02 源） | 结局是「某种原则必付」的**证据**、「SingleOmega 型收费必付」的**负结果**（币种不确定）；CC 路线未机械化，不据此交付任何数学结论；不静默、不以 (a) 冒充 |
| **B1b′ 必要性** | `Necessity ℓ = ℝLayerAt ℓ → SingleOmega ℓ` **正式确认 `CONJECTURE`**（029 §2 硬条款执行）。路径 1 失败分析：0/1-cut 编码 `hProp ↪ DedekindReals` 的 locatedness 在 `0≤q<r≤1` 窗口强制 `P ∨ ¬P`；路径 2 缺模型（`HoTT+CC+¬SingleOmega` 模型存在性未论证——若成立则 Necessity 在其中为假，不可证且可能不可反驳）；LEM 下后件免费（Book 取法 3 逐字）⇒ 必要性问题纯属构造性片段。 | `CONJECTURE`（不升级） | 修订片 030 §3（路径分析 + 三观察）；Book §11.2 取法 3/4 逐字（CLAIM-PACKAGE §1.1） | 收费位置判词不得 `MACHINE_PROVED`；`SingleOmega↔PropResizing` 蕴含方向仍开放；不声称「必付费」任何币种 |
| **B2 靶 A 不可归约** | **声模型论证撤回**（Astra 二审 005 采纳，030 §4 勘误）：原「两方向各有声模型」只指定单次 `LEM ℕ` 应用取值，非完整模型；且 Book `thm:not-lem`（SOURCE_REPORTED）：LEM∞ 与 univalence 不相容——ChargeDemo 组合（LEM∞ 公设 + `--cubical` 原生 UA）按 Book 不一致，无声模型，「内部证明不可能」随之失效。已机器见证仅剩**语法层事实**（refl 拒绝 + 内核亲印中性范式；exit≠0 须核对预期诊断类别）。 | `QUESTION`（理由修正：声模型/不可证论证未成立，依赖未完成模型工作或 Book 反论形式化；UA-opaque 演示（TA-01）公设非 LEM∞ 不触发不相容，原则上可救但须构造完整模型） | 030 §4 勘误块（2026-09-19 晚）+ TA 族收据（本表前节；身份修正见 TA-LEM 行） | 不因探针收据升格；Huber 维持 `SOURCE_REPORTED_NOT_REPLAYED` 按其论文演算范围使用；不声称对象层定理 |
| **B3 范围诚实性** | 当前 repo **无公开稿文本**（028 为修复方案非公开稿）——三方对照的公开稿一侧为空集，今日平凡成立。**判词基准落盘**（公开稿产生时强制）：(1) 不得「击落 HoTT」作数学主张；(2) 最高措辞 =「非现实性机械锚定 + 逼选结构」；(3) 收费表述保留币种不确定性；(4) B1b′/B2/Huber 三等级不得升格。 | `BASELINE_READY_VACUOUS_TODAY`（公开稿产生时转为对照执行） | 修订片 030 §5；audit map §5 基准条目 | 空集对照不冒充实质对照；公开稿产生之日重跑 |

## 追加登记：收官补强两件（反弹消毒收据 + 必要性 LEM-条件版，2026-09-19）

> 用户指令「开始，全部做了」的产出（dev-notes/0048/0049 脉络）。两件均为
> `registers_new_claim:false` 的候选收据，无 postulate。

| proof_id | claim_id | 源码 | 运行收据 | 证据等级 |
|---|---|---|---|---|
| `MP-DEDEKIND-OMEGA-REBOUND-DISARM` | `CAND-F2-7-REBOUND-DISARM` | `formal/dedekind-omega-missile/ReboundDisarm.agda`（S¹ = 紧化的显式构造形态：`ideal-point-is-explicit = base` 构造子；`endpoint-identification-is-a-path = loop` 路径构造子；`hit-computation-witness : intLoop (pos 0) ≡ refl` 由 refl 证明——经 HIT 的闭计算取得典范形） | runs `20260919-MP-DEDEKIND-OMEGA-REBOUND-DISARM-01`（--safe 零公理，exit 0，stderr 0） | `MACHINE_PROVED_WITH_SCOPE / LIBRARY_CONSTRUCTION_AND_CLOSED_COMPUTATION_POSITIVE_CONTROL`（A07 降格：原 REBOUND_DISARMAMENT_WITNESS 判词过强——三别名与一个计算特例不承载紧化重建；学说层结论见 B 线收官节） |
| `MP-DEDEKIND-OMEGA-NECESSITY-LEM` | `CAND-F2-7-NECESSITY-LEM` | `formal/dedekind-omega-missile/MissileFourNecessityLEM.agda`（`hProp≃Bool`：LEMProp ℓ → hProp ℓ ≃ Bool；`SingleOmega-from-LEM`：Ω := Lift Bool；**`LEM→Necessity : LEMProp ℓ → Necessity ℓ`——前提 ℝLayerAt 未被使用**） | runs `20260919-MP-DEDEKIND-OMEGA-NECESSITY-LEM-01`（manifest 漏 pin CutRealLayer，Astra A08，历史收据）+ `20260919-MP-DEDEKIND-OMEGA-NECESSITY-LEM-02`（**当前依据，补全闭包重捕获**，exit 0，stderr 0） | `MACHINE_PROVED_WITH_SCOPE / NECESSITY_IS_CONSTRUCTIVE_ONLY`（LEM 下后件无条件成立 ⇒ B1b′ 必要性问题的全部内容在构造性片段；Book 取法 3「LEM ⇒ Ω≡Bool」原文首次收据化） |

| claim | 命题（机器检查形态） | 证据等级 | 证据 | 禁止外推 |
|---|---|---|---|---|
| CAND-F2-7-REBOUND-DISARM | **（A07 降格后判词：库构造 + 闭计算正控制——Astra 二审 004 §5 采纳）**三陈述机器成立：S¹ 的 base 为显式构造子、loop 为路径构造子、intLoop (pos 0) ≡ refl by refl（经 HIT 的闭项取得典范形的正控制）；canonicity 不被 HIT 收费的**单点正控制**。「紧化的构造性重建/消毒」为学说层结论（B 线），不由本收据单独承载。 | `MACHINE_PROVED_WITH_SCOPE` | run `-01` 的 `RUN.json`（`KERNEL_ACCEPTED_WITH_SCOPE`，exit 0，stderr 0） | 紧化**古典用法**的非现实性未被形式化（论证层）；不据此升级对极限理论本身的任何否定判词；攻击面在「完成声明的免费化」（Ω 塌缩，见 REAL-LAYER 节）而非紧化 |
| CAND-F2-7-NECESSITY-LEM | `LEMProp ℓ → SingleOmega ℓ`（经 hProp ℓ ≃ Bool），从而 `LEMProp ℓ → Necessity ℓ` 且 ℝLayerAt 前提未被使用——经典语境中必要性空洞。 | `MACHINE_PROVED_WITH_SCOPE` | run `-01` 的 `RUN.json`（exit 0，stderr 0）+ `source-manifest.json` | 无条件 Necessity 维持 `CONJECTURE`（真值依赖模型，CC 换币候选未决）；`SingleOmega↔PropResizing` 蕴含方向仍开放；不声称 LEM 为真；不声称 HoTT 不一致 |

## 追加登记：Astra 审计修复三收据（2026-09-19，A02/A08/A09 采纳）

> 依据《Astra对击落HoTT工作的第一次审计》（A02/A08/A09 三项经本会话独立核验
> 成立并当场修复）。判词口径不变：机器定理保持为真；被修复的是规格忠实性标签、
> 证据闭包与校验器语义。逐项裁定见《GLM的审计报告》。

| run | 内容 | 状态 |
|---|---|---|
| `20260919-MP-DEDEKIND-OMEGA-REAL-LAYER-03` | located ∥⊎∥ 截断（勘误三）后 B0+B1a 全量重查；`isPropDCut` 新增（dcut 成为真 prop，与 Book 逐字一致） | KERNEL_ACCEPTED / 见本节 |
| `20260919-MP-DEDEKIND-OMEGA-NECESSITY-LEM-02` | 同命题重捕获 + manifest 补 pin 定义 owner CutRealLayer.agda（A08） | KERNEL_ACCEPTED / 见本节 |
| `20260919-MP-DEDEKIND-OMEGA-GOLD-03` | 同命题重捕获 + manifest 补 pin M2（√2-irrational 消费，CutGoldForm.agda:67/232）（A08） | KERNEL_ACCEPTED / 见本节 |
| verifier 修复 | `verify_formal_proof_run.py` 的 `--safe`/`--cubical` 检查由全文子串改为 OPTIONS pragma 实际解析（A09）；TA-01 在新检查下正确 FAIL（公设控制类），safe 主证明不受影响 | 代码已改，语法/行为实测 |

**Astra 审计中本会话未采纳或部分采纳的项（A01/A03/A05/A06/A07）的逐项裁定与
证据**：见《GLM的审计报告》分片 002。

## 追加登记：Astra 二审修复（2026-09-19 晚）

> 依据《Astra对击落HoTT工作的第二次审计》（003/004/005 片）。本轮采纳并执行：
> A09 残留（校验器块注释误识别）、owner 行同步（REAL-LAYER located/run、
> ReboundDisarm 降格落行、NECESSITY-LEM run ID、B2 理由修正）、030 §4 声模型
> 论证撤回（LEM∞/UA 不相容冲突）、A04/A05 头注释落地与重收据。

| run / 修复项 | 内容 | 状态 |
|---|---|---|
| verifier v3 | `strip_agda_comments`：嵌套块注释深度计数 + pragma `{-#…#-}` 保真拷贝 + 行注释剥离，再提取 OPTIONS token。五控制回归（SafePositive/UnsafeNegative/CommentPragma/LineComment/Nested）全对；TA-01 正确 FAIL；safe 收据 PASS | 代码已改，行为实测 |
| `20260919-MP-DEDEKIND-OMEGA-M1-05` | M1 同命题重捕获（A05 头注精确化触发 hash 变更；命题体零改动） | KERNEL_ACCEPTED |
| `20260919-MP-DEDEKIND-OMEGA-TA-LEM-03/04` | TA-LEM 探针重捕获（A04 命名精确化触发；**补全闭包 pin ChargeDemo**；预期 exit 42 = 内核拒绝即收据） | KERNEL_REJECTED (expected) |
| 矩阵 owner 行 | REAL-LAYER claim 行 located 改 ∥⊎∥；proof/claim 行当前依据改 -03；ReboundDisarm 行 A07 降格落行（`LIBRARY_CONSTRUCTION_AND_CLOSED_COMPUTATION_POSITIVE_CONTROL`）；NECESSITY-LEM 行补全 run ID；B2 行修正声模型论证；M1/TA-LEM 行更新与身份修正 | 10 处原位编辑 |
| 030 §4 勘误块 | 声模型论证撤回（LEM∞+UA 不相容冲突，Book thm:not-lem SOURCE_REPORTED）；分层修正（LEM∞ 演示仅剩语法层事实；UA-opaque 可救但须完整模型） | 已写入 |
| CLAIM-PACKAGE §3-E | 勘误三补录 + located set→prop 旧表述修正 + §4 B1a 当前依据 -03 | 已写入 |
| A04 落地 | ChargeDemo 头注释精确命名（LEM∞ 型不受限排中公设 / 现成选择函数公设）+ Book thm:not-lem 不相容性登记（SOURCE_REPORTED） | 已写入 |
| A05 落地 | M1 头注释范围精确化（判别式恒±1 全称命题；不收敛读法排除出机器结论） | 已写入 |

**Astra 二审中本会话未采纳或待后续的项**：A01 仍 OPEN_SUBSTANTIVE（维持解释
合同定位，接受「写合同≠履行合同」裁定）；A03 无条件必要性仍 OPEN（共识）；
A06 后续（027 勘误指针 + 探针正负控制细化）列 R3；标准 LEM₋₁ 样例（R2）、
GOLD packing（R5）未做；A10 送审维持；「10 旧 + 3 新全部双重复放绿」口径
按二审 002 片修正为**带时间/基线/分类限定**（旧 REAL-LAYER-02 hash 过期为
历史预期，TA-01 FAIL 为正确分类）。


## 追加登记：Astra 断点与证明机制有界检查（2026-09-19）

原生 Cubical Agda 2.8.0 / Cubical v0.9。下列11包均为本轮内核接受且可逐包核验的形式规格。历史全局版本闭包检查仍报 CURRENT_MATRIX_NOT_APPEND_ONLY_SUCCESSOR；因此登记状态为 `KERNEL_ACCEPTED_INDEXED_LOCAL / GLOBAL_DELIVERY_GATE_PARTIAL`，不以本表宣布全项目版本闭合或 HoTT 缺陷。精确假设以源码签名为准；完整报告：`Astra继续尝试/断点与证明机制系统检查/第一轮执行报告.md`。

| proof_id | claim | 源码 | 运行收据 | 状态 |
|---|---|---|---|---|
| `MP-ASTRA-PATH-001` | C-250 | `formal/astra-breakpoint-check/PathControls.agda` | `verification/runs/20260919-MP-ASTRA-PATH-01` | KERNEL_ACCEPTED_INDEXED_LOCAL；LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED |
| `MP-ASTRA-EXCLUSION-001` | C-251 | `formal/astra-breakpoint-check/PathExclusion.agda` | `verification/runs/20260919-MP-ASTRA-EXCLUSION-01` | KERNEL_ACCEPTED_INDEXED_LOCAL；LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED |
| `MP-ASTRA-FRAME-001` | C-252 | `formal/astra-breakpoint-check/FixedFrame.agda` | `verification/runs/20260919-MP-ASTRA-FRAME-01` | KERNEL_ACCEPTED_INDEXED_LOCAL；LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED |
| `MP-ASTRA-ELIM-001` | C-253 | `formal/astra-breakpoint-check/EliminationControls.agda` | `verification/runs/20260919-MP-ASTRA-ELIM-01` | KERNEL_ACCEPTED_INDEXED_LOCAL；LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED |
| `MP-ASTRA-LOCAL-001` | C-254 | `formal/astra-breakpoint-check/LocalCoherence.agda` | `verification/runs/20260919-MP-ASTRA-LOCAL-02` | KERNEL_ACCEPTED_INDEXED_LOCAL；LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED |
| `MP-ASTRA-QCIRCLE-001` | C-255 | `formal/astra-breakpoint-check/RationalPointSet.agda` | `verification/runs/20260919-MP-ASTRA-QCIRCLE-01` | KERNEL_ACCEPTED_INDEXED_LOCAL；LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED |
| `MP-ASTRA-ENDPOINT-001` | C-256 | `formal/astra-breakpoint-check/EndpointMaps.agda` | `verification/runs/20260919-MP-ASTRA-ENDPOINT-01` | KERNEL_ACCEPTED_INDEXED_LOCAL；LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED |
| `MP-ASTRA-COMPUTATION-001` | C-257 | `formal/astra-breakpoint-check/ClosedComputation.agda` | `verification/runs/20260919-MP-ASTRA-COMPUTATION-01` | KERNEL_ACCEPTED_INDEXED_LOCAL；LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED |
| `MP-ASTRA-HOLDOUT-001` | C-258 | `formal/astra-breakpoint-check/UpstreamLoopHoldout.agda` | `verification/runs/20260919-MP-ASTRA-HOLDOUT-01` | KERNEL_ACCEPTED_INDEXED_LOCAL；LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED |
| `MP-ASTRA-BOUNDED-001` | C-259 | `formal/astra-breakpoint-check/BoundedConsumers.agda` | `verification/runs/20260919-MP-ASTRA-BOUNDED-03` | KERNEL_ACCEPTED_INDEXED_LOCAL；LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED |
| `MP-ASTRA-BOUNDARY-001` | C-260 | `formal/astra-breakpoint-check/BoundaryIncidence.agda` | `verification/runs/20260919-MP-ASTRA-BOUNDARY-01` | KERNEL_ACCEPTED_INDEXED_LOCAL；LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED |

| claim | 形式命题及自然语言范围 | 证据等级 | 证据 | 禁止外推 |
|---|---|---|---|---|
| C-250 | 任意匹配端点的路径可以连接；不存在对任意 A,a,b,c,d 从 a≡b 与 c≡d 免费给出 a≡d 的函数。Bool 的 ua(notEquiv) 运输及往返观察控制。 | KERNEL_ACCEPTED_INDEXED_LOCAL；GLOBAL_DELIVERY_GATE_PARTIAL | `MP-ASTRA-PATH-001`；`HoTT/formal/astra-breakpoint-check/PathControls.agda`；`HoTT/verification/runs/20260919-MP-ASTRA-PATH-01` | 不证明物理复原、证明搜索不可判定或理论矛盾。 |
| C-251 | 对有显式 merely-connected 见证的 A，Σx:A.((x≡a)→⊥) 可映到⊥；HIT S¹实例及空类型等价；Bool 补集非空正控制。 | KERNEL_ACCEPTED_INDEXED_LOCAL；GLOBAL_DELIVERY_GATE_PARTIAL | `MP-ASTRA-EXCLUSION-001`；`HoTT/formal/astra-breakpoint-check/PathExclusion.agda`；`HoTT/verification/runs/20260919-MP-ASTRA-EXCLUSION-01` | 路径排除不是点集圆去掉一个几何点；不说 HoTT 不能删点。 |
| C-252 | Bare=ΣX:Type.X 中所选两项有 ua 路径；Framed=ΣX.(X×(X≃Bool)) 中保持固定坐标的两项不同，实际参照观察随合法重参数化保持。 | KERNEL_ACCEPTED_INDEXED_LOCAL；GLOBAL_DELIVERY_GATE_PARTIAL | `MP-ASTRA-FRAME-001`；`HoTT/formal/astra-breakpoint-check/FixedFrame.agda`；`HoTT/verification/runs/20260919-MP-ASTRA-FRAME-01` | 这是携带真实参照等价的结构控制；未形式化实际圆环与线段。 |
| C-253 | 不存在 f:∥Bool∥₁→Bool 满足所有 b 的 f∣b∣=b；全关系商同样不能恢复原代表；目标 isProp 时有合法截断恢复，常值商观察及混合消费者可构造。 | KERNEL_ACCEPTED_INDEXED_LOCAL；GLOBAL_DELIVERY_GATE_PARTIAL | `MP-ASTRA-ELIM-001`；`HoTT/formal/astra-breakpoint-check/EliminationControls.agda`；`HoTT/verification/runs/20260919-MP-ASTRA-ELIM-01` | 不声称所有 Bool 输出函数不存在，也不声称每种消去都丢失任务所需信息。 |
| C-254 | 相容的 Partial 面、满面消费者、给定 Glue 边界和 HIT 路径消费者通过；常值圆消费者保持所给 loop 条件。 | KERNEL_ACCEPTED_INDEXED_LOCAL；GLOBAL_DELIVERY_GATE_PARTIAL | `MP-ASTRA-LOCAL-001`；`HoTT/formal/astra-breakpoint-check/LocalCoherence.agda`；`HoTT/verification/runs/20260919-MP-ASTRA-LOCAL-02` | 有限原生规则控制，不是所有高阶粘合或现实运动的全称定理。 |
| C-255 | ℚ 坐标方程 x²+y²=1 定义的集合是 set；去掉 east 后 north 连同其不等见证给出非空元素。 | KERNEL_ACCEPTED_INDEXED_LOCAL；GLOBAL_DELIVERY_GATE_PARTIAL | `MP-ASTRA-QCIRCLE-001`；`HoTT/formal/astra-breakpoint-check/RationalPointSet.agda`；`HoTT/verification/runs/20260919-MP-ASTRA-QCIRCLE-01` | 不是 ℝ 圆、拓扑等价或从 N 到 M 的操作模型。 |
| C-256 | 一般单射和等价保持给定不同点；所定义 Reach 仅改变内部坐标时 N 不可达 M，扩充 construct 操作后可达。 | KERNEL_ACCEPTED_INDEXED_LOCAL；GLOBAL_DELIVERY_GATE_PARTIAL | `MP-ASTRA-ENDPOINT-001`；`HoTT/formal/astra-breakpoint-check/EndpointMaps.agda`；`HoTT/verification/runs/20260919-MP-ASTRA-ENDPOINT-01` | Reach 为明确受限的构造语言；不代表所有实际允许的形变或制造操作。 |
| C-257 | 原生 ua(notEquiv) 的闭运输在本例以 refl 通过；存在具体 (p,β) 实现另设 opaque 控制的精确公设合同。 | KERNEL_ACCEPTED_INDEXED_LOCAL；GLOBAL_DELIVERY_GATE_PARTIAL | `MP-ASTRA-COMPUTATION-001`；`HoTT/formal/astra-breakpoint-check/ClosedComputation.agda`；`HoTT/verification/runs/20260919-MP-ASTRA-COMPUTATION-01` | 一个闭计算实例不证明整个系统规范化；opaque 对照不等于原生 ua 不计算。 |
| C-258 | 库内整数绕数消费者给出 oneLoop 与 refl 的不同；不能将 base≡base 中所有证明识别为同一路径。 | KERNEL_ACCEPTED_INDEXED_LOCAL；GLOBAL_DELIVERY_GATE_PARTIAL | `MP-ASTRA-HOLDOUT-001`；`HoTT/formal/astra-breakpoint-check/UpstreamLoopHoldout.agda`；`HoTT/verification/runs/20260919-MP-ASTRA-HOLDOUT-01` | 源码来源交叉检查，不是盲测；不声称所有不同语法证明都不等。 |
| C-259 | 冻结的 id/not 长度0至3的15个语法词 ×4个 Bool 真值表，60个消费者各有全关系兼容证明或其否定证明。 | KERNEL_ACCEPTED_INDEXED_LOCAL；GLOBAL_DELIVERY_GATE_PARTIAL | `MP-ASTRA-BOUNDED-001`；`HoTT/formal/astra-breakpoint-check/BoundedConsumers.agda`；`HoTT/verification/runs/20260919-MP-ASTRA-BOUNDED-03` | 只覆盖冻结语法60成员；不能外推全部 HoTT 上下文、无限搜索或物理操作。 |
| C-260 | 若 n:Bool→A 两端不同而 m:Bool→B 所有端部像相同，则任意环境等价 e:A≃B、端标签等价 labels:Bool≃Bool 都没有所列交换见证。 | KERNEL_ACCEPTED_INDEXED_LOCAL；GLOBAL_DELIVERY_GATE_PARTIAL | `MP-ASTRA-BOUNDARY-001`；`HoTT/formal/astra-breakpoint-check/BoundaryIncidence.agda`；`HoTT/verification/runs/20260919-MP-ASTRA-BOUNDARY-01` | 需由真实几何模型提供 n,m 及其端部性质；没有由定义标签直接宣布真实 M/N 不等。 |


## 追加登记：Astra 指定点自然恢复与表示对照（2026-09-19）

BP-GEO-RESTORE-01；原生safe Cubical Agda，规格C-261–C-264。内核接受是本地运行事实，包关系/全局门禁仍PARTIAL；不宣布完整F-011数学交付或圆环目标完成。量词、假设及每个符号以精确源码为准。

| proof_id | claim | 源码 | 主run | 状态 |
|---|---|---|---|---|
| `MP-ASTRA-RESTORE-CRITERION-001` | C-261–C-262 | `formal/astra-breakpoint-check/PointRestoration.agda` | `verification/runs/20260919-MP-ASTRA-RESTORE-CRITERION-01` | KERNEL_ACCEPTED_INDEXED_LOCAL / GLOBAL_DELIVERY_GATE_PARTIAL |
| `MP-ASTRA-QCIRCLE-RESTORE-001` | C-263 | `formal/astra-breakpoint-check/RationalRestoration.agda` | `verification/runs/20260919-MP-ASTRA-QCIRCLE-RESTORE-01` | KERNEL_ACCEPTED_INDEXED_LOCAL / GLOBAL_DELIVERY_GATE_PARTIAL |
| `MP-ASTRA-HIT-RESTORE-CONTROL-001` | C-264 | `formal/astra-breakpoint-check/HomotopyRestorationControl.agda` | `verification/runs/20260919-MP-ASTRA-HIT-RESTORE-CONTROL-02` | KERNEL_ACCEPTED_INDEXED_LOCAL / GLOBAL_DELIVERY_GATE_PARTIAL |

| claim | 形式规格 | 证据等级 | 证据 | 禁止外推 |
|---|---|---|---|---|
| C-261 | 任意ℓ、C:Type ℓ与p:C。Puncture=Σx:C.¬(x≡p)，Completed=Puncture⊎Unit，extend为自然包含/指定点映射。SplitRestore=Σdecode:C→Completed.∀x extend(decode x)≡x，与PointDecidable=∀x Dec(x≡p)之间有两个方向的函数。 | KERNEL_ACCEPTED_INDEXED_LOCAL / GLOBAL_DELIVERY_GATE_PARTIAL | `MP-ASTRA-RESTORE-CRITERION-001`；`HoTT/formal/astra-breakpoint-check/PointRestoration.agda`；`HoTT/verification/runs/20260919-MP-ASTRA-RESTORE-CRITERION-01` | 不声称两个证据类型之间的≃，不赋予拓扑，不将可判定性默认为实数输入已有；无物理复原或HoTT缺陷结论。 |
| C-262 | 同一C,p，给定PointDecidable，构造Iso Completed C与Completed≃C，正向函数正是extend，逆向为decode，双逆律显式检查；不需附加isSet C。 | KERNEL_ACCEPTED_INDEXED_LOCAL / GLOBAL_DELIVERY_GATE_PARTIAL | `MP-ASTRA-RESTORE-CRITERION-001`；`HoTT/formal/astra-breakpoint-check/PointRestoration.agda`；`HoTT/verification/runs/20260919-MP-ASTRA-RESTORE-CRITERION-01` | 不声称两个证据类型之间的≃，不赋予拓扑，不将可判定性默认为实数输入已有；无物理复原或HoTT缺陷结论。 |
| C-263 | 既有QCircle={(x,y):ℚ²&#124;x²+y²=1}及east=(1,0)，由discreteℚ与命题纤维获得pointDecision，构造(PuncturedQCircle⊎Unit)≃QCircle；正向保留删点包含与east；ua运输对任意Completed元素与extend有路径相等。 | KERNEL_ACCEPTED_INDEXED_LOCAL / GLOBAL_DELIVERY_GATE_PARTIAL | `MP-ASTRA-QCIRCLE-RESTORE-001`；`HoTT/formal/astra-breakpoint-check/RationalRestoration.agda`；`HoTT/verification/runs/20260919-MP-ASTRA-QCIRCLE-RESTORE-01` | 仅有理代数点集及原生类型等价；无拓扑/同胚/连续路径/实数完成/物理动作许可证明。 |
| C-264 | 对HIT S¹与base，沿同一内部路径排除定义的自然extend不存在SplitRestore，且不存在PointDecidable。证明消费circleExclusion及整数绕数的非平凡路径控制。 | KERNEL_ACCEPTED_INDEXED_LOCAL / GLOBAL_DELIVERY_GATE_PARTIAL | `MP-ASTRA-HIT-RESTORE-CONTROL-001`；`HoTT/formal/astra-breakpoint-check/HomotopyRestorationControl.agda`；`HoTT/verification/runs/20260919-MP-ASTRA-HIT-RESTORE-CONTROL-02` | 不是点集圆删一个几何点的命题；不是HoTT无法处理几何复原。首次失败只是extend导入名冲突。 |

## 追加登记：MP-G4-RING-ORIGIN（圆环主线单元一·来源携带胚型，2026-09-19）

> 用户 2026-09-19 立项「Flash 的第一次寻找尝试」（圆环主线 G4；工作目录
> `Flash的第一次寻找尝试/`，隔离纪律见其 001 片）。本 run 为该线第一张
> canonical 收据。`registers_new_claim:false`。

| proof_id | claim_id | 源码 | 运行收据 | 证据等级 |
|---|---|---|---|---|
| `MP-G4-RING-ORIGIN` | `CAND-G4-RING-ORIGIN` | `formal/flash-first-hunt/RingOrigin.agda`（`SourceCarrier C p := Σ x:C, ¬(x≡p)`——去点载体来源携带；正控制 `postulate-free-build`/`instance-witness`（ℤ，零 postulate）；靶形 `BreakoutFromM` 以 p 为显式来源参数） | runs `20260919-MP-G4-RING-ORIGIN-01`（失败教训：命名空间与 capture 的 -i root 冲突，保留）→ **`20260919-MP-G4-RING-ORIGIN-02`（当前，exit 0，stderr 0）** | `MACHINE_PROVED_WITH_SCOPE / SOURCE_CARRIER_POSITIVE_CONTROL` |

| claim | 命题（机器检查形态） | 证据等级 | 证据 | 禁止外推 |
|---|---|---|---|---|
| CAND-G4-RING-ORIGIN | 「来源携带胚型」最小类型化：去点载体的每个点携带「不是断点」的来源证据（`¬(x≡p)`），且该携带是零 postulate 的合法构造；断点取出函数以来源参数 p 为显式类型成分。 | `MACHINE_PROVED_WITH_SCOPE / SOURCE_CARRIER_POSITIVE_CONTROL` | run `-02` 的 `RUN.json`（exit 0，stderr 0） | 不声称 S¹(HIT) 等同点集圆；不声称找到 HoTT 共同体的实际植入现场（G1 未启动）；不声称不可定义性已证（靶形仅参数化陈述）；不声称圆环悖论完整形式化 |

> 2026-09-19 深夜修订注记：本修订仅为使 G4-RING-ORIGIN-02 的 index 快照选择满足
> backfill 的时序要求（run 目录入库 5194378 之后需存在含其身份的矩阵修订）；
> 内容无变化。


## M1索引位置修复（不改原行内容）

本行原被插入旧冻结前缀，现逐字移入追加区；源码、运行指针及其证据等级不因移动而改变。旧位置与行SHA由本轮修复基线保留。

| proof_id | claim | 源码 | 运行收据 | 证据等级 |
|---|---|---|---|---|
| `MP-DEDEKIND-OMEGA-M1` | `CAND-F2-7-M1`（候选锚点） | `formal/dedekind-omega-missile/MissileOneProcessLayer.agda`（发射包 `CLAIM-PACKAGE.md` / `README.md`） | `verification/runs/20260917-MP-DEDEKIND-OMEGA-M1-04/`（历史；`-01`–`-03` 为失败 run 保留）+ **`20260919-MP-DEDEKIND-OMEGA-M1-05/`（当前：同命题重捕获，A05 头注精确化后）**；Agda 2.8.0；Cubical v0.9；`--safe --cubical --guardedness`；exit 0 | `MACHINE_PROVED_WITH_SCOPE / PROCESS_LAYER_GAP_ANCHOR_NOT_HOTT_CONTRADICTION` |

## 追加登记：MP-G4-BREAKPOINT-BRIDGE（圆环线↔ℝ层线连通件，2026-09-19）

> Flash 线（圆环主线 G4）单元一后续，用户四项指令之③。`registers_new_claim:false`。

| proof_id | claim_id | 源码 | 运行收据 | 证据等级 |
|---|---|---|---|---|
| `MP-G4-BREAKPOINT-BRIDGE` | `CAND-G4-BREAKPOINT-BRIDGE` | `formal/flash-first-hunt/BreakpointBridge.agda`（`ExcludedCarrier C r := Σ q:C, ¬(q≡r)`——与 `RingOrigin.SourceCarrier` 同型的排除证据载体；桥命题 `bridge`；实例正控 `ℤ∖{0}` 排除证据构造性） | run `20260919-MP-G4-BREAKPOINT-BRIDGE-03`（exit 0，stderr 0；`-01`/`-02` 为 capture 命名空间 bug 的失败 run，已删，教训= capture 已修为命名空间感知） | `MACHINE_PROVED_WITH_SCOPE / EXCLUSION_CARRIER_TYPE_BRIDGE` |

| claim | 命题（机器检查形态） | 证据等级 | 证据 | 禁止外推 |
|---|---|---|---|---|
| CAND-G4-BREAKPOINT-BRIDGE | 圆环悖论的「断点排除」（RingOrigin.SourceCarrier）与 Dedekind cut 的「无理排除」在类型层为同一 Σ 构造——两线共用排除证据检查方式。 | `MACHINE_PROVED_WITH_SCOPE / EXCLUSION_CARRIER_TYPE_BRIDGE` | run `20260919-MP-G4-BREAKPOINT-BRIDGE-03` 的 `RUN.json`（exit 0，stderr 0） | 不声称 GOLD L/U 全谓词族已重表述（谓词族级，下一单元）；不声称圆环=实数（共用检查方式 ≠ 同一对象）；无 ∀ 新主张；不声称 HoTT 不一致 |

## 追加登记：MP-G4-NO-BREAKOUT（裸载体断点取出不可构造，2026-09-19 深夜）

> Flash 线单元二，用户四项指令之①。`registers_new_claim:false`。

| proof_id | claim_id | 源码 | 运行收据 | 证据等级 |
|---|---|---|---|---|
| `MP-G4-NO-BREAKOUT` | `CAND-G4-NO-BREAKOUT` | `formal/flash-first-hunt/NoBreakoutFromBare.agda`（`no-breakout-from-bare : ∀ C p → ¬((x:C) → ¬(x≡p))`——参数多态否定；Unit/tt 实例化） | run `20260919-MP-G4-NO-BREAKOUT-01`（exit 0，stderr 0） | `MACHINE_PROVED_WITH_SCOPE / PARAMETRIC_NO_BREAKOUT` |

| claim | 命题（机器检查形态） | 证据等级 | 证据 | 禁止外推 |
|---|---|---|---|---|
| CAND-G4-NO-BREAKOUT | 裸载体上断点取出函数不可构造：∀ C p, ¬((x:C) → ¬(x≡p))——「不知道 p 就无法排除 p」的参数化定理（Unit/tt 具体化给出 tt≢tt 与 refl 矛盾）。 | `MACHINE_PROVED_WITH_SCOPE / PARAMETRIC_NO_BREAKOUT` | run `-01` 的 `RUN.json`（exit 0，stderr 0） | **范围限定**：closed-argument 参数多态不可行 + 具体反例实例；**非**任意实现/任意演算的不可定义性元定理（元定理须精确演算+归约定义，另立义务）；不声称 HoTT 不一致 |

## 追加登记：G1 圆环版狩猎第一批（HoTT 语料：cubical v0.9 + agda-unimath，2026-09-19 深夜）

> Flash 线（用户四项指令之②）。 hunting 口径：在 HoTT 语料中寻找「使用去点/
> 补点/低层实数对象而**丢来源**」的位置（用户「植入」问题的实证检验）。
> 本批为负结果 + 正面卫生证明，如实登记（030 §5 结果原则）。

| 猎场 | 检索 | 结果 | 裁定 |
|---|---|---|---|
| cubical v0.9 库 | puncture / S¹ 去点 / Σx∈S¹, x≠base 形态 | 无此类构造（S1/Properties 仅有 IsoFunSpace 等无关形态） | **负结果**：cubical 库无「丢来源的去点对象」 |
| agda-unimath real-numbers | ℝ 的宇宙位置；locatedness 析取 | `ℝ l : UU (lsuc l)`（dedekind-real-numbers L116）——**从不降到 l**；locatedness 用 `disjunction-Prop` = `trunc-Prop (A + B)`（foundation/disjunction L103-124）= **命题截断，与我们勘误三同型** | **正面卫生证明**：unimath 知情且正确（不降层 + 截断析取）——「传统同胚/免费塌缩思维被植入」在该语料中**未发现** |
| HoTT Book reals.tex | （已由 Astra/本方多轮对照）§11.2 明文招认层级问题与三路线 | 招认在案 | 奠基层知情（认知分层 L1） |

**对用户「植入」问题的当前裁定**：在已检语料（cubical 库 + unimath real-numbers
+ Book §11.2/§3）内，**未发现**「忘掉圆环悖论类差异而默认 H 判据」的实际使用
位置。 hunted 面仍小（两库；Book 后续章节/UniMath 其余/mathlib 未检）——维持
G1 为开放狩猎，非终结判定。

## 追加登记：MP-G4-CUT-AS-SOURCE（cut 成员的排除证据族，2026-09-19 深夜）

> Flash 线单元三，用户四项指令之③′（GOLD 谓词族→SourceCarrier 重表述第一件）。
> `registers_new_claim:false`。

| proof_id | claim_id | 源码 | 运行收据 | 证据等级 |
|---|---|---|---|---|
| `MP-G4-CUT-AS-SOURCE` | `CAND-G4-CUT-AS-SOURCE` | `formal/flash-first-hunt/CutAsSourceCarrier.agda`（`ExclFamily C r q := ¬(q≡r)` 谓词族 + `FamilyCarrier` 族形态载体 + `family-to-point` 族→单点桥，与 RingOrigin 类型学同一） | run `20260919-MP-G4-CUT-AS-SOURCE-01`（exit 0，stderr 0） | `MACHINE_PROVED_WITH_SCOPE / EXCLUSION_FAMILY_CARRIER` |

| claim | 命题（机器检查形态） | 证据等级 | 证据 | 禁止外推 |
|---|---|---|---|---|
| CAND-G4-CUT-AS-SOURCE | cut 成员携带排除证据的谓词族形态：ExclFamily + FamilyCarrier + family-to-point（族→单点桥）内核成立——「cut 的每个成员都携带排除证据」的类型学同一性机器化。 | `MACHINE_PROVED_WITH_SCOPE / EXCLUSION_FAMILY_CARRIER` | run `-01` 的 `RUN.json`（exit 0，stderr 0） | 完整 L/U 序结构谓词族重表述（le-ℚ 链）未做，列下一单元；不声称 GOLD 已被替代；不声称圆环=实数；无 ∀ 新主张 |

## 追加登记：G1 圆环版狩猎第二批（UniMath real-numbers 全目录 + Book surreals 段，2026-09-19 深夜）

> Flash 线。第二批口径同前批；本批含一个**文献级高价值命中**（非机器收据）。

| 猎场 | 检索/阅读 | 结果 | 裁定 |
|---|---|---|---|
| UniMath real-numbers 全目录（addition 等） | `ℝ l` 层级一致性 | 全部在 `lsuc l` 参数化下运算，无降到 l 的使用 | **负结果**（续）：该线维持卫生 |
| **Book reals.tex surreals 段（L2487-2490）** | Dedekind reals 与 surreals/ord/card/V 并列 | **明文**：「…or even the Dedekind reals in the absence of propositional resizing」与真类级对象同类 | **文献级高价值命中（SOURCE_REPORTED）**：Book 自我把「无 resizing 的 Dedekind reals」与**真类级现象**归为一类——比 §11.2 招认更进一步（招认的是「要付费」，此处是「不付费时它与真类同级」）。精确意义待与 surreals 构造对照后评估；不升级为危机判词 |
| cubical 库 + unimath 构造代码 | （前批） | 无丢来源现场 | 维持负结果 |

**裁定更新**：G1 的「共同体不知情」分支在**代码层**仍未命中（unimath 干净），
但在**文献层**命中 Book 的自我归类——「共同体知情」需再分层：知情并有意以
真类级现象使用 ≠ 知情且披露每次使用的代价。G1 第三批方向 = surreals 的
family-of-surreals 构造（Book 明言 UU-small families）与 Dedekind 线的对照
——这是用户圆环之问（来源/大小被理论经济性抹除的位置）的文献侧最近靶。

## 追加登记：NO-BREAKOUT-02（元层边界节落地，2026-09-19 深夜）

> run `20260919-MP-G4-NO-BREAKOUT-02`（当前依据）；`-01` 为无边注记历史收据。

> 同命题重捕获（源码 hash 因 §5 边界注记变更）；回应 Astra 二审 005 片
> 「精确演算」要求：定理精确强度 = Agda 参数多态 closed-term 不可行性；
> 显式排除 (a) 任意外部实现元定理 (b) 归约不可终止证明 (c) 独立性结果——
> (a)-(c) 登记为开放义务，不以边界注记伪装达成。`registers_new_claim:false`。
> `-01` 保留为无边注记的历史收据。
> 时序修订注记（2026-09-19 深夜）：为 NO-BREAKOUT-02 的 index 快照选择提供
> 含完整 run ID 的已提交矩阵修订；其余内容无变化。

## 追加登记：MP-ASTRA-REAL-CIRCLE-001（真实实数去点圆与开区间，2026-09-20）

经典Lean4.34.0/mathlib v4.34.0 `5ed2965256430c3649e86755f9576b54eca72435`；辅助点集几何，不是原生HoTT或物理过程命题。命题固定后实际内核检查；标准公理输出为propext、Classical.choice、Quot.sound，无sorryAx。源码、依赖源码/编译接口、Lean/Std运行输入由manifest逐文件固定；导入使用官方预编译库，本轮未从源码重建全部mathlib。

| proof_id | claim_ids | 源码与规格 | 运行收据 | 证据等级 |
|---|---|---|---|---|
| `MP-ASTRA-REAL-CIRCLE-001` | `C-265` | `formal/astra-real-geometry/PuncturedCircle.lean`、`TOOLCHAIN.json`；真实二维实数EuclideanSpace单位圆，指定点p的补子类型，N为Ioo(0,1) | `verification/runs/20260920-MP-ASTRA-REAL-CIRCLE-001-02/`；exit0、零stderr；22923个外部源码/运行输入文件哈希；-01为增加显式TOOLCHAIN索引前的成功捕获，不作当前primary | `FORMAL_CHECKED_WITH_SCOPE / CLASSICAL_LEAN_GEOMETRY / LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED` |

| claim | 精确命题及实现 | 证据等级 | 证据 | 禁止外推 |
|---|---|---|---|---|
| C-265 | 对任意`p : sphere (0 : EuclideanSpace ℝ (Fin 2)) 1`，`Punctured p = {x : Circle // x ≠ p}`到`Ioo (0:ℝ) 1`有`Homeomorph`；`pole`给出显式非空实例，`actualMToN`及surjective、exact_inverse_roundtrip、forward_continuous、inverse_continuous逐项过核。 | `FORMAL_CHECKED_WITH_SCOPE / CLASSICAL_LEAN_GEOMETRY / LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED` | `puncturedToEuclidean`、`euclideanLineToReal`、`rescaleInterval`、`puncturedCircleHomeomorph`；run `20260920-MP-ASTRA-REAL-CIRCLE-001-02` | 只比较内在拓扑；未证明保持环境/端部/来源/允许操作的复原；不把noncomputable定义当物理Trace；未建立到原生HoTT的保真翻译；未得HoTT缺陷。 |

## 追加登记：MP-ASTRA-AMBIENT-CIRCLE-001（实数平面的环境条件，2026-09-20）

固定同一`Plane = EuclideanSpace ℝ (Fin 2)`，`M=circleOpen`为单位圆删去`pole`的像，`N=lineOpen`为`t↦(t,0)`对`Ioo(0,1)`的像。经典Lean4.34.0/mathlib固定依赖；显式`-t 0`，不声称完成独立全导入重检或全库源码重建；公理仅propext/Classical.choice/Quot.sound。

| proof_id | claim_ids | 源码与规格 | 运行收据 | 证据等级 |
|---|---|---|---|---|
| `MP-ASTRA-AMBIENT-CIRCLE-001` | `C-266..C-268` | `formal/astra-real-geometry/AmbientCircle.lean`、`AMBIENT-TOOLCHAIN.json`，复用C-265具体模型 | `verification/runs/20260920-MP-ASTRA-AMBIENT-CIRCLE-001-02/`；exit0、零stderr；-01类型检查失败完整保留 | `FORMAL_CHECKED_WITH_SCOPE / CLASSICAL_LEAN_GEOMETRY / LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED` |

| claim | 精确命题及实现 | 证据等级 | 证据 | 禁止外推 |
|---|---|---|---|---|
| C-266 | `closure M ∖ M = {pole}`；`closure N ∖ N = {lineEmbed 0,lineEmbed 1}`，且两端点不同；同时`embeddedIntrinsicHomeomorph : ↥M ≃ₜ ↥N`。 | `FORMAL_CHECKED_WITH_SCOPE / CLASSICAL_LEAN_GEOMETRY / LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED` | `circle_missing_boundary`、`line_missing_boundary`、`line_endpoints_distinct`、`embeddedIntrinsicHomeomorph`；run `20260920-MP-ASTRA-AMBIENT-CIRCLE-001-02` | 差集是相对于指定平面的闭包余集，不是平面拓扑边界frontier，也不是M的两个实体端点；不能外推所有嵌入。 |
| C-267 | 不存在`h : Plane ≃ₜ Plane`满足`h '' M = N`；反向也不存在。 | `FORMAL_CHECKED_WITH_SCOPE / CLASSICAL_LEAN_GEOMETRY / LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED` | `no_ambient_homeomorph`、`no_ambient_homeomorph_reverse`；run `20260920-MP-ASTRA-AMBIENT-CIRCLE-001-02` | 否定环境同胚的扩张，未否定C-266的内在同胚；不是同一命题P与¬P。 |
| C-268 | 对任意有限列表`hs : List (Plane ≃ₜ Plane)`，逐步取像的`runAmbient hs N ≠ M`；单步正控制`runAmbient [h] N = h '' N`。 | `FORMAL_CHECKED_WITH_SCOPE / CLASSICAL_LEAN_GEOMETRY / LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED` | `ambient_run_is_image`、`no_finite_ambient_reconstruction`、`one_step_positive_control`；run `20260920-MP-ASTRA-AMBIENT-CIRCLE-001-02` | 操作类仅整平面同胚；不包含切割/加点/重新嵌入/任意非单射连续过程/无限极限，未证明所有现实构造不可能；不是native HoTT缺陷。 |

## 追加登记：MP-ASTRA-CURVE-DEFORMATION-001（同一M/N的连续嵌入变形，2026-09-20）

复用C-265–C-268的精确`Plane/lineOpen/circleOpen`。当前采用闭时间区间和开曲线参数区间，要求联合连续与逐时拓扑嵌入，不要求延伸为整平面同胚。经典Lean4.34.0/mathlib固定输入，公理propext/Classical.choice/Quot.sound；非原生HoTT翻译。

| proof_id | claim_ids | 源码与规格 | 运行收据 | 证据等级 |
|---|---|---|---|---|
| `MP-ASTRA-CURVE-DEFORMATION-001` | `C-269..C-270` | `formal/astra-real-geometry/DeformationCircle.lean`、`DEFORMATION-TOOLCHAIN.json`；具体stretch/bend/turn复合 | `verification/runs/20260920-MP-ASTRA-CURVE-DEFORMATION-001-02/`；exit0，零stderr；-01为界证明未闭合的失败捕获 | `FORMAL_CHECKED_WITH_SCOPE / CLASSICAL_LEAN_GEOMETRY / LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED` |

| claim | 精确命题及实现 | 证据等级 | 证据 | 禁止外推 |
|---|---|---|---|---|
| C-269 | 存在`F : Icc(0,1) → Ioo(0,1) → Plane`，`(t,u)↦F t u`联合连续，每个t的切片为`IsEmbedding`，t=0的像精确等于`lineOpen`、t=1的像精确等于`circleOpen`。显式见证为`curveMotion`。 | `FORMAL_CHECKED_WITH_SCOPE / CLASSICAL_LEAN_GEOMETRY / LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED` | `exists_curve_deformation`、`deformation_continuous`、`deformation_isEmbedding`、`deformation_initial_image`、`deformation_final_image`；run `20260920-MP-ASTRA-CURVE-DEFORMATION-001-02` | 不要求环境同胚；未加入长度、速度、材料、物理实现条件；开区间端点不属于曲线参数域；未证明闭参数延拓或原生HoTT命题。 |
| C-270 | 同一个显式见证`deformation`对所有`0≤t≤1`和所有`u : Ioo(0,1)`满足两个平面坐标绝对值都≤60。 | `FORMAL_CHECKED_WITH_SCOPE / CLASSICAL_LEAN_GEOMETRY / LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED` | `deformation_uniform_box`、`stretch_small_time_bound`、`bend_motion_bounds`；run `20260920-MP-ASTRA-CURVE-DEFORMATION-001-02` | 统一空间界不是有限速度、等长或物理可实施证明；60为便利的粗界，未主张最优。 |

## 追加登记：MP-ASTRA-ENDPOINT-CLOSURE-001（同一变形的闭参数延拓，2026-09-20）

固定C-269的实际`deformation`，消去参数ρ的端点分母后定义`extendedDeformation`。时间与曲线参数均取闭区间[0,1]；内点一致定理保证没有改换上一轮的变形。经典Lean4.34.0/mathlib，标准三公理；非原生HoTT几何翻译。

| proof_id | claim_ids | 源码与规格 | 运行收据 | 证据等级 |
|---|---|---|---|---|
| `MP-ASTRA-ENDPOINT-CLOSURE-001` | `C-271..C-273` | `formal/astra-real-geometry/EndpointClosure.lean`、`ENDPOINT-TOOLCHAIN.json` | `verification/runs/20260920-MP-ASTRA-ENDPOINT-CLOSURE-001-01/`；exit0、零stderr，十项公理检查无sorryAx | `FORMAL_CHECKED_WITH_SCOPE / CLASSICAL_LEAN_GEOMETRY / LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED` |

| claim | 精确命题及实现 | 证据等级 | 证据 | 禁止外推 |
|---|---|---|---|---|
| C-271 | `extendedDeformation`在`Icc(0,1)×Icc(0,1)`联合连续；对任意实数t和任意内点u，`extendedDeformation t u = deformation t u`；t=0时延拓为指定闭线段参数化。 | `FORMAL_CHECKED_WITH_SCOPE / CLASSICAL_LEAN_GEOMETRY / LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED` | `closingDen_pos`、`extendedDeformation_continuous`、`extended_agrees_interior`、`extended_initial`；run `20260920-MP-ASTRA-ENDPOINT-CLOSURE-001-01` | 连续性域是声明的闭方形；未声称闭参数切片始终为嵌入、有限速度或物理实现。 |
| C-272 | `endpointGap(t)=dist(F̄(t,0),F̄(t,1))`在闭时间连续，初值1，所有t<1时严格正，t=1时为0；两个末端像都等于pole。 | `FORMAL_CHECKED_WITH_SCOPE / CLASSICAL_LEAN_GEOMETRY / LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED` | `endpointGap_continuous/initial/pos_before/zero_at_end`、`extended_final_left/right`；run `20260920-MP-ASTRA-ENDPOINT-CLOSURE-001-01` | 参数标签0、1不同，但末态像相同；不存在“两个不同的平面像距离0”的结论；未证明距离全过程单调递减。 |
| C-273 | 闭参数末态像为整个单位圆，末态不单射；精确纤维条件为`F̄(1,u)=F̄(1,v) ↔ u=v ∨ (u=0∧v=1) ∨ (u=1∧v=0)`；映到pole的参数恰为0或1，所有内点避开pole。 | `FORMAL_CHECKED_WITH_SCOPE / CLASSICAL_LEAN_GEOMETRY / LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED` | `extended_final_image/not_injective/fibers/eq_pole_iff`、`extended_final_interior_avoids`；run `20260920-MP-ASTRA-ENDPOINT-CLOSURE-001-01` | 端点不属于原开参数域；闭参数非单射不否定C-269内点嵌入；未把普通Lean相等当HoTT类型路径。 |

## 追加登记：MP-ASTRA-PELL-CURVE-COMPARISON-001（同题算术与曲线命题对照，2026-09-20）

回应用户“为何Lean通过而Agda不通过”的问题：在Lean按Agda M1相同初值(1,1)、相同递推(p+2q,p+q)定义整数Pell对，实际检查相同判别式结论及其与C-269曲线存在命题的合取。不是一般跨内核保真翻译或一致性证明。

| proof_id | claim_ids | 源码与规格 | 运行收据 | 证据等级 |
|---|---|---|---|---|
| `MP-ASTRA-PELL-CURVE-COMPARISON-001` | `C-274` | `formal/astra-real-geometry/PellCurveComparison.lean`、`COMPARISON-TOOLCHAIN.json` | `verification/runs/20260920-MP-ASTRA-PELL-CURVE-COMPARISON-001-01/`；exit0、零stderr；Pell单独公理为propext，合取另用Classical.choice/Quot.sound | `FORMAL_CHECKED_WITH_SCOPE / LEAN_ARITHMETIC_AND_GEOMETRY_COMPARISON / LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED` |

| claim | 精确命题及实现 | 证据等级 | 证据 | 禁止外推 |
|---|---|---|---|---|
| C-274 | `pellPair 0=(1,1)`、`pellPair(n+1)=(p+2q,p+q)`，D(n)=p²−2q²；任意n有D(n)=1或−1，故D(n)≠0；Lean同时接受`(∀n,D(n)≠0) ∧ (∃F, 联合连续 ∧ 逐时嵌入 ∧ 初像N ∧ 末像M)`。 | `FORMAL_CHECKED_WITH_SCOPE / LEAN_ARITHMETIC_AND_GEOMETRY_COMPARISON / LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED` | `pellDiscriminant_sign/never_zero`、`pell_and_continuous_curve`；run `20260920-MP-ASTRA-PELL-CURVE-COMPARISON-001-01` | D是该整数递推判别式，未与实际端点距离识别；不是Agda对完整F的重放；未提供一般Agda↔Lean或实数→HoTT翻译，也不证明任一内核元层一致性。 |

## 追加登记：实际曲线结构与原生边界观察（2026-09-20）

当前单元`BP-GEO-STRUCTURED-CONSUMER-01`区分两个包：经典Lean实际几何/精确整数观察，与原生Cubical Agda的整数边界图。边界数据由实际completion求值得到；两个内核分别核验各自命题，不宣称整个实数几何已跨内核移植。

| proof_id | claim_ids | 源码与规格 | 运行收据 | 证据等级 |
|---|---|---|---|---|
| `MP-ASTRA-STRUCTURED-CURVE-001` | `C-275..C-277` | `formal/astra-real-geometry/StructuredCurve.lean`、`STRUCTURED-TOOLCHAIN.json` | `verification/runs/20260920-MP-ASTRA-STRUCTURED-CURVE-001-02/`；-01为加入坐标交换对应前的成功捕获，非当前primary | `FORMAL_CHECKED_WITH_SCOPE / CLASSICAL_LEAN_GEOMETRY / LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED` |
| `MP-ASTRA-NATIVE-BOUNDARY-OBSERVATION-001` | `C-278..C-279` | `formal/astra-breakpoint-check/GeometricBoundaryObservation.agda`，实际导入BoundaryIncidence；safe/cubical/guardedness | `verification/runs/20260920-MP-ASTRA-NATIVE-BOUNDARY-OBSERVATION-001-01/`；exit0、零stderr | `FORMAL_CHECKED_WITH_SCOPE / NATIVE_CUBICAL_BOUNDARY_DIAGRAM / LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED` |

| claim | 精确命题及实现 | 证据等级 | 证据 | 禁止外推 |
|---|---|---|---|---|
| C-275 | 实际`nPresentation/mPresentation`含开参数嵌入、闭参数连续completion和内点一致；其BareCarrier有具体Homeomorph，但不存在保持整completion及端标签的PresentationEquivalence；不存在由任意BareEquivalent自动运输BoundaryCoincident的通用规则。 | `FORMAL_CHECKED_WITH_SCOPE / CLASSICAL_LEAN_GEOMETRY / LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED` | `concreteBareHomeomorph/no_concrete_structure_equivalence/no_bare_coincidence_transport`；run `20260920-MP-ASTRA-STRUCTURED-CURVE-001-02` | Rich仅为声明的完成图/环境结构，不包含全部来源历史/物理条件；未证明任何HoTT真实使用曾承诺该自动提升。 |
| C-276 | 对任意环境Homeomorph，连同interior/completion一起变换有PresentationEquivalence且保持端点重合谓词；对完整闭/开参数同时反向并交换端标签，也有PresentationEquivalence。 | `FORMAL_CHECKED_WITH_SCOPE / CLASSICAL_LEAN_GEOMETRY / LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED` | `ambientTransportEquivalence/ambientTransport_preserves_coincidence/reversePresentationEquivalence`；run `20260920-MP-ASTRA-STRUCTURED-CURVE-001-02` | 坐标和参数运输正控制不等于满足任何额外固定物理位置/材料条件。 |
| C-277 | `integralEmbedding : ℤ×ℤ→Plane`单射；n的实际边界图恰为(0,0)/(1,0)，m的实际边界图恰为常值(1,0)在该嵌入下的像；交换两坐标与该嵌入交换，运输后n边界仍精确对应。 | `FORMAL_CHECKED_WITH_SCOPE / EXACT_SELECTED_OBSERVATION / LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED` | `integralEmbedding_injective/n_integral_observation_exact/m_integral_observation_exact/integral_swap_commutes/swapped_n_observation_exact`；run `20260920-MP-ASTRA-STRUCTURED-CURVE-001-02` | 保真对象是这些边界值和指定坐标动作；不是所有实数点、曲线、连续性或完整Agda↔Lean翻译。 |
| C-278 | 原生Agda对相同整数坐标表n/m证明：任意环境等价和Bool端标签等价均不能形成所给交换图；RichDiagram的两实例无Path；忘去边界函数后的环境载体Path为refl，单一恢复函数不能同时恢复这两实例。 | `FORMAL_CHECKED_WITH_SCOPE / NATIVE_CUBICAL_BOUNDARY_DIAGRAM / LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED` | `noCommutingBoundaryEquivalence/noRichDiagramPath/bareCarrierPath/noOneBareRecovery`；run `20260920-MP-ASTRA-NATIVE-BOUNDARY-OBSERVATION-001-01` | native Bare是边界图的环境载体，不是完整实数曲线；两个实例的无共同恢复不是任何信息都不可恢复的定理；没有HoTT矛盾。 |
| C-279 | 对任意Coord等价e，原生ua与ΣPathP把完整n边界图运输为`(Coord, e∘n)`；坐标交换非恒等实例有Rich路径，右端坐标计算为(0,1)，分离性质沿路径保持。 | `FORMAL_CHECKED_WITH_SCOPE / NATIVE_UA_STRUCTURED_TRANSPORT / LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED` | `transportDiagram/swappedDiagramPath/swappedRightCoordinate/swappedStillSeparate`；run `20260920-MP-ASTRA-NATIVE-BOUNDARY-OBSERVATION-001-01` | 正控制要求数据一起运输；不声称ua自动保留已被用户代码忘掉的边界函数，也不声称完整实数模型已经native重放。 |

## 原生实数模型与额外归约配置资格（2026-09-20）

本节的配置诊断、实际模型和同源码复核分别定级。C-05旧run及冻结行只保存其原配置接受的历史事实；当前新增支持来自`MP-ASTRA-NOSECTION-RESTRICTED-001`，旧原树不能作为未经限定的普通HoTT验证环境继续使用。旧run/source不改写，当前环境资格由registry中该旧包的`qualification_status`和本节新proof行共同定位。

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-ASTRA-ERASURE-CONFIG-001` | `C-280` | `formal/agda-unimath/hott-z/ErasureConfigurationDiagnostic.agda`；上游原树和额外primEraseEquality | `verification/runs/20260920-MP-ASTRA-ERASURE-CONFIG-001-01/`；exit0并保留warning；同源码普通函数负控制为`20260920-MP-ASTRA-ERASURE-CONTROL-001-01`，exit42/loopRefl | `FORMAL_CHECKED_WITH_SCOPE / EXTRA_REDUCTION_CONFIGURATION_DIAGNOSTIC` |
| `MP-ASTRA-NATIVE-REAL-001` | `C-281` | `formal/agda-unimath/hott-z/NativeRealCircleQualification.agda`；两文件no-erasure派生库 | `verification/runs/20260920-MP-ASTRA-NATIVE-REAL-001-01/`；exit0；实数、度量及公理依赖明确 | `FORMAL_CHECKED_WITH_SCOPE / ACTUAL_DEDEKIND_MODEL_WITH_DECLARED_POSTULATES` |
| `MP-ASTRA-NOSECTION-RESTRICTED-001` | `C-282` | 与旧C-05 run完全相同的`formal/agda-unimath/hott-z/NoCanonicalPoint.agda`；两文件no-erasure派生库 | `verification/runs/20260920-MP-ASTRA-NOSECTION-RESTRICTED-001-02/`；`-01`成功但重复使用C-05而未通过registry关系检查，原件保留；仍有声明的基础公设 | `REPLAYED_WITH_SCOPE / ERASURE_RULE_REMOVED / NOT_GLOBAL_SOUNDNESS_CERTIFICATION` |

| Claim ID | 精确主张 | 状态 | 证据 | 禁止外推 |
|---|---|---|---|---|
| C-280 | 在固定Agda without-K加上游primEraseEquality额外归约及库univalence配置中，源码构造`∀{ℓ A x}(p:x＝x),p＝refl`，并由Bool交换的univalence路径构造`configurationEmpty : empty`。 | `FORMAL_CHECKED_WITH_SCOPE / EXTENDED_CONFIGURATION_DIAGNOSTIC` | `eraseRetract/loopRefl/swapAction/collapsedAction/configurationEmpty`；run `20260920-MP-ASTRA-ERASURE-CONFIG-001-01`；同源码消融run拒绝loopRefl | 不是普通HoTT仅用标准规则的不一致证明；不是首次发现；不把不一致配置中接受任意项当一般数学真理。 |
| C-281 | 在声明公设的no-erasure库变体中，`ℝ lzero`平面及实际乘积/子空间度量可构造；`x*x+y*y=1`圆有east/north，north≠east；逻辑去点圆有puncturedNorth；严格开区间(0,1)有intervalHalf。 | `FORMAL_CHECKED_WITH_SCOPE / ACTUAL_NONEMPTY_REAL_POINTSETS` | `Real/realPlaneMetric/circleMetric/east/north/northNotEast/puncturedNorth/intervalMetric/intervalHalf`；run `20260920-MP-ASTRA-NATIVE-REAL-001-01` | 未证明此处两空间同胚、完整F、Lean保真翻译、逻辑不等于正分离的等价、最小公理集或物理完成；不假设SingleOmega，但导入公设另列。 |
| C-282 | 在去掉primEraseEquality特殊归约的固定库变体及其声明公设下，同一旧源码仍给出`∀{ℓ}, ¬((X:2-Element-Type ℓ)→type-2-Element-Type X)`及无统一PointedOrientation推论。 | `FORMAL_CHECKED_WITH_SCOPE / EXISTING_C05_SOURCE_REQUALIFIED` | `no-canonical-point/no-canonical-pointed-orientation`；run `20260920-MP-ASTRA-NOSECTION-RESTRICTED-001-02` | 这是C-05的配置重资格化身份，不是新发现定理；不扩大到带顺序输入、一般选择公理或物理端点任务；不认证整库一致性。 |

## 实际圆的逻辑删点、apartness与逆元条件（2026-09-20）

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-ASTRA-PUNCTURE-APARTNESS-001` | `C-283..C-284` | `formal/agda-unimath/hott-z/PunctureApartness.agda`；导入同一NativeRealCircleQualification；no-erasure变体及声明公设 | `verification/runs/20260920-MP-ASTRA-PUNCTURE-APARTNESS-001-01/`；Agda实际`--ignore-interfaces`，exit0 | `FORMAL_CHECKED_WITH_SCOPE / ACTUAL_CIRCLE_INPUT_AND_INVERSE_CRITERION` |

| Claim ID | 精确主张 | 状态 | 证据 | 禁止外推 |
|---|---|---|---|---|
| C-283 | 对C281实际圆C、e=(1,0)，第一坐标为1的点等于e；令W(p)=¬(p=e)、A(p)=apart(x(p),1)，则W(p)↔¬¬A(p)。保持原点的统一refinement、Lift=(∀p,W(p)→A(p))、LocalStability=(∀p,¬¬A(p)→A(p))互相蕴含；显式DNE₀及LEM₀各足以给Lift。 | `FORMAL_CHECKED_WITH_SCOPE / LOGICAL_IFF_NOT_TYPE_PATH` | `firstCoordinateOneIsEast/weakIffDoubleNegStrong/refinementIffLift/liftIffLocalStability/dneGivesLift/excludedMiddleToDNE`；run `20260920-MP-ASTRA-PUNCTURE-APARTNESS-001-01` | 未无条件证明Lift/LocalStability或其否定、独立性；未证明全局LEM必要；W宇宙与A宇宙不同，↔不是≃或ua路径。 |
| C-284 | 同一C上令d(p)=1−x(p)、I(p)=Σr:Real,d(p)*r=1，对任意p有A(p)↔I(p)；统一给全部逻辑去点输入逆元↔LocalStability；显式LEM₀充分。强域上前向坐标y/d实际可构造，north映到1且east不在强域；W(p)→¬¬I(p)，故¬Σp,W(p)×¬I(p)。 | `FORMAL_CHECKED_WITH_SCOPE / ARBITRARY_INVERSE_NECESSITY_AND_CONTROLS` | `rawInverseToStrong/strongIffRawInverse/uniformInverseIffStability/stereographicForward/northForwardOne/eastNotStrong/noMissingInverseWitness`；同run | I中r没有预设apartness；必要性仅指本地A族稳定性，不是LEM/resizing必要性；没有完整反参数化、连续性、同胚或物理还原证明，不能称HoTT矛盾。 |

## 实际原生有理参数化、复合律与univalence作用（2026-09-20）

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-ASTRA-NATIVE-STEREOGRAPHIC-001` | `C-285..C-286` | `formal/agda-unimath/hott-z/NativeStereographic.agda`；实际导入C281模型和C283/C284条件；no-erasure变体与声明公设 | `verification/runs/20260920-MP-ASTRA-NATIVE-STEREOGRAPHIC-001-01/`；原生Agda `--ignore-interfaces` exit0 | `FORMAL_CHECKED_WITH_SCOPE / ACTUAL_POINTSET_EQUIVALENCE_AND_NATIVE_PATH_ACTION` |

| Claim ID | 精确主张 | 状态 | 证据 | 禁止外推 |
|---|---|---|---|---|
| C-285 | 对每个实际Real参数t，D=t²+1严格正，构造q=D⁻¹与圆点φ(t)=((t²−1)q,(t+t)q)及apartness。实际投影f满足∀t,f(φ(t))=t及∀w:StrongPuncture,φ(f(w))=w，组成StrongPuncture≃Real。Lift下原PuncturedRealCircle也与Real等价；LEM₀为显式充分输入。 | `FORMAL_CHECKED_WITH_SCOPE / ACTUAL_BOTH_ROUNDTRIPS` | `positiveD/paramEquation/paramStrong/forwardParameter/parameterForward/strongCircleEquivReal/weakCircleEquivReal/classicalWeakCircleEquivReal`；run `20260920-MP-ASTRA-NATIVE-STEREOGRAPHIC-001-01` | 无条件强域与条件弱域分开；未证明连续性、同胚、开区间接口、Lean保真翻译、物理变形或无条件Lift。 |
| C-286 | 对C285实际等价使用公理式原生univalence得到StrongPuncture＝Real；对任意w，equiv-eq还原该Path后的作用等于实际投影f(w)，north作用结果等于1。Lift下另有原弱删点类型到Real的Path。 | `FORMAL_CHECKED_WITH_SCOPE / PROPOSITIONAL_NATIVE_UNIVALENCE_ACTION` | `strongTypePath/strongTypePathAction/typePathNorthOne/weakTypePath`；同run | 这是底层类型Path与命题作用等式，不声称refl判断归约、Cubical计算规则、原给定metric/来源/端部结构相等或HoTT矛盾。 |

## 实际取逆局部模数与原度量下的双向连续（2026-09-20）

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-ASTRA-NATIVE-CONTINUITY-001` | `C-287..C-288` | `formal/agda-unimath/hott-z/StereographicContinuity.agda`，显式依赖ReciprocalContinuity及C281/C284/C285三个旧模块；no-erasure变体 | `verification/runs/20260920-MP-ASTRA-NATIVE-CONTINUITY-001-01/`；原生Agda `--ignore-interfaces` exit0；五本地Agda模块全部pin | `FORMAL_CHECKED_WITH_SCOPE / SAME_METRIC_SAME_MAP_HOMEOMORPHISM` |

| Claim ID | 精确主张 | 状态 | 证据 | 禁止外推 |
|---|---|---|---|---|
| C-287 | 对实际apart非零Dedekind实数子空间，recip=real-inv-nonzero-ℝ逐点连续。给定正有理r及2r≤abs(x)，C=(inv r)²、μ(r,ε)=min(r,inv(C)·ε)满足原邻域下的逆元误差≤ε；由abs(x)>0的截断有理下界合法构造连续模数的截断存在。 | `FORMAL_CHECKED_WITH_SCOPE / EXPLICIT_LOCAL_RATIONAL_MODULUS` | `reciprocalDistance/inverseBound/nearbyLower/budgetIdentity/localEstimate/reciprocalContinuous`；ReciprocalContinuity.agda；run `20260920-MP-ASTRA-NATIVE-CONTINUITY-001-01` | 非零域是apart-from-zero；没有新增或传入选择公理/LEM，不声称最小公理集已提取、全局数值模数选择器、双向一致连续或物理可执行性。 |
| C-288 | 在C281原实数/乘积/子空间度量下，C285同一投影与参数化均逐点连续；连同原两复合律，填满PointwiseHomeomorphism六字段，得到StrongPuncture↔Real的双向连续互逆。原弱删点域在Lift下亦有此同胚，LEM₀为显式充分输入。 | `FORMAL_CHECKED_WITH_SCOPE / EXPLICIT_POINTWISE_HOMEOMORPHISM` | `stereographicContinuous/parameterizeContinuous/strongHomeomorphism/weakHomeomorphism/classicalWeakHomeomorphism`；StereographicContinuity.agda；同run | 不声称uniform-homeo、等距、原metric数据相等、无条件弱Lift、与(0,1)已连通、完整Lean翻译、固定端部物理变形或HoTT矛盾。 |

## 原开区间连续互逆及圆同胚复合（2026-09-20）

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-ASTRA-NATIVE-INTERVAL-001` | `C-289..C-290` | `formal/agda-unimath/hott-z/NativeOpenInterval.agda`；SignedIntervalHomeomorphism及五个已核本地模块全部pin | `verification/runs/20260920-MP-ASTRA-NATIVE-INTERVAL-001-01/`；原生Agda `--ignore-interfaces` exit0；固定no-erasure配置/声明公设 | `FORMAL_CHECKED_WITH_SCOPE / ORIGINAL_OPEN_INTERVAL_HOMEOMORPHISM` |

| Claim ID | 精确主张 | 状态 | 证据 | 禁止外推 |
|---|---|---|---|---|
| C-289 | 实际Real上的t/(1+abs(t))与SignedInterval={abs(z)<1}上的z/(1−abs(z))具有正分母、严格范围、两复合律及原metric连续性；仿射½(1+z)与(u+u)−1接到C281原OpenRealInterval(0,1)，得到Real↔(0,1)的六字段同胚。 | `FORMAL_CHECKED_WITH_SCOPE / STRICT_MEMBERSHIP_AND_BOTH_CONTINUOUS_INVERSES` | `realSignedHomeomorphism/signedUnitHomeomorphism/realUnitHomeomorphism`；SignedIntervalHomeomorphism.agda、NativeOpenInterval.agda；run `20260920-MP-ASTRA-NATIVE-INTERVAL-001-01` | 不换闭区间，不额外假定Lift/LEM，不声称全局一致连续、等距或物理过程；继承库公设不等于无公设体系。 |
| C-290 | C289与C288实际复合产生StrongPuncture↔C281原(0,1)同胚；原W域有Lift及LEM₀充分输入下的同胚。提取实际等价后univalence给StrongPuncture＝OpenRealInterval及与真实复合映射一致的命题作用，原W域Path仍以Lift为条件。 | `FORMAL_CHECKED_WITH_SCOPE / ACTUAL_CIRCLE_ORIGINAL_INTERVAL_AND_NATIVE_ACTION` | `strongCircleUnitHomeomorphism/weakCircleUnitHomeomorphism/classicalWeakCircleUnitHomeomorphism/strongIntervalTypePath/strongIntervalPathAction/weakIntervalTypePath`；同run | 内在几何子命题不自动证明无条件弱Lift、带来源/端部结构相等、环境延拓、允许运动或Done-EXACT；不把原生证明冒称全Lean演算翻译或HoTT矛盾。 |

## 同一圆参数映射的闭参数延拓与端部（2026-09-20）

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-ASTRA-NATIVE-COMPLETION-001` | `C-291..C-292` | `formal/agda-unimath/hott-z/NativeCompletion.agda`；HomogeneousCircle及七个既有本地模块全部pin | `verification/runs/20260920-MP-ASTRA-NATIVE-COMPLETION-001-01/`；原生Agda完整依赖 `--ignore-interfaces` exit0；固定no-erasure配置/声明公设 | `FORMAL_CHECKED_WITH_SCOPE / SAME_MAP_CLOSED_EXTENSION` |

| Claim ID | 精确主张 | 状态 | 证据 | 禁止外推 |
|---|---|---|---|---|
| C-291 | 对全部实际Real输入u，v=(u+u)−1、d=1−abs(v)、K=v²+d²严格正，齐次公式((v²−d²)/K,(2vd)/K)给圆上点并在原metric连续；限制到ClosedParameter=[0,1]得mCompletion。对全部C281原(0,1)输入，mInterior证明该值等于C290同一Strong圆同胚的实际逆映射。nCompletion(u)=(u,0)另有同一参数度量下连续性。 | `FORMAL_CHECKED_WITH_SCOPE / POSITIVE_DENOMINATOR_CONTINUITY_AND_EXACT_INTERIOR_AGREEMENT` | `homogeneousEquation/homogeneousMatchesParam/completionPositive/mCompletionContinuous/nCompletionContinuous/mInterior`；两新源码；run `20260920-MP-ASTRA-NATIVE-COMPLETION-001-01` | 这里completion仅是闭参数连续延拓，不是Cauchy完备化泛性质、物理Trace完成或完整Lean F的翻译；继承库公设，无新增LEM/Lift输入。 |
| C-292 | 同一mCompletion的0与1边界值由公式推出均为east；普通nCompletion两边界值不同。全部原开区间内点避开east且mCompletion限制到内点为单射；整个闭参数mCompletion非单射，由两个不同参数同像给出实际否定证明。 | `FORMAL_CHECKED_WITH_SCOPE / DERIVED_BOUNDARY_DIFFERENCE_AND_DOMAIN_DISTINCTION` | `mAtZero/mAtOne/mEndsCoincide/nEndsDistinct/interiorNotEast/interiorInjective/completionNotInjective`；NativeCompletion.agda；同run | 边界参数不属于原开区间，east不属于内点像；不声称两个M内点零距离却不相等。内点与闭域的单射命题定义域不同；不推出任意复原不可能、丰富结构可识别或HoTT矛盾。 |

## 实际内在丰富结构与有限环境任务（2026-09-20）

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-ASTRA-NATIVE-RICH-TASK-001` | `C-293..C-294` | `formal/agda-unimath/hott-z/NativeCurveTaskControls.agda`；NativeRichCurve、FiniteTrace、NativeCurveTask及九个既有本地模块全部pin | `verification/runs/20260920-MP-ASTRA-NATIVE-RICH-TASK-001-02/`；原生Agda完整依赖 `--ignore-interfaces` exit0；固定no-erasure配置 | `FORMAL_CHECKED_WITH_SCOPE / ACTUAL_INTRINSIC_RICH_AND_FINITE_TASK` |

| Claim ID | 精确主张 | 状态 | 证据 | 禁止外推 |
|---|---|---|---|---|
| C-293 | RichCurve=Σ A:UU₁,CurveData A，含实际参数等价、平面实现、原metric连续闭图及内点一致。mRich/nRich以C290强删点圆与原开区间为实际Bare，有C290裸Path，但无指定Rich路径；任意Bare路径运输mData均不等于预选nData，且仅输入裸类型的统一函数不能同时精确恢复这两份预选Rich。完整字段运输给mRich=transportedRich，逐参数闭图及端部同像保持。 | `FORMAL_CHECKED_WITH_SCOPE / ACTUAL_RICH_SEPARATION_AND_FULL_FIELD_TRANSPORT` | `barePath/noRichPath/noAnyBarePathLift/noUniformBareRecovery/fullTransportPath/transportKeepsClosedImage/fullTransportKeepsEnds`；NativeRichCurve.agda；run `20260920-MP-ASTRA-NATIVE-RICH-TASK-001-02` | transportedRich的载体为区间但不是普通直线nData。无全现实来源穷尽、无条件弱Lift或同命题P/非P；不宣称HoTT自动删除结构，也不否定带原数据的恢复。 |
| C-294 | AmbientStep由真实平面双向连续同胚及同一闭参数下的交换图定义；端部同像/异像保持与反射由函数/逆律推导。有限Trace归纳、拼接与Done=r=target给两方向N↔M无该类有限成功，N→M截断成功也不成立。实际坐标交换有非平凡Success；完整字段运输mRich→transportedRich在同一AmbientStep/Done模型有一步Success。裸Path给BareTrace/BareSuccess，但不存在对任意Rich对将BareTrace全部提升为AmbientTrace的函数。 | `FORMAL_CHECKED_WITH_SCOPE / FINITE_TASK_NO_GO_AND_SAME_MODEL_POSITIVE_CONTROLS` | `noTraceNtoM/noTraceMtoN/noSuccessNtoM/noSuccessMtoN/noMereSuccessNtoM/swapSuccess/noUniversalTraceLift/fullTransportSuccess`；FiniteTrace、NativeCurveTask、NativeCurveTaskControls；同run | 操作类限定全平面同胚与固定参数图；不涵盖所有曲线变形、重参数化/加点/合并或物理复原。不从非紧性/超时推不完成；不证明HoTT许诺裸Trace提升，也不替代原Input/Denotes/允许操作对应。 |

## 给定来源数据的重呈现与精确图对应（2026-09-20）

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-ASTRA-NATIVE-SOURCE-CONTRACT-001` | `C-295..C-296` | `formal/agda-unimath/hott-z/NativeSourceContract.agda`；十三个既有本地模块全部pin | `verification/runs/20260920-MP-ASTRA-NATIVE-SOURCE-CONTRACT-001-01/`；原生Agda完整依赖 `--ignore-interfaces` exit0；固定no-erasure配置 | `FORMAL_CHECKED_WITH_SCOPE / SOURCE_SUPPLIED_REPRESENTATION_CONTRACT` |

| Claim ID | 精确主张 | 状态 | 证据 | 禁止外推 |
|---|---|---|---|---|
| C-295 | Input显式给定完整source Rich、targetCarrier及Bare(source)≃targetCarrier；State/Step/Observation/Denotes/Output/Satisfies/Done/Run均定义。整体运输所得reexpressed逐闭参数与source图相同，满足目标载体与Denotes；对每个Input构造有限同模型Run，任意Done推出Satisfies，checkedOutput从Run给出实际终态及正确性。actualInput用mRich、原区间和C290真实等价实例化，输出就是transportedRich。 | `FORMAL_CHECKED_WITH_SCOPE / EXPLICIT_SOURCE_INPUT_AND_SOUND_REEXPRESSION` | `denotesReexpression/runReexpression/doneIsSound/checkedOutput/actualRun/actualCheckedOutput`；NativeSourceContract.agda；run `20260920-MP-ASTRA-NATIVE-SOURCE-CONTRACT-001-01` | source/等价是本合同给定数据，不是从裸N免费恢复；不声称其为所有方法的最小必要输入。Denotes为最终精确闭图，不是全部物理历史或任意形变身份，未断言每个AmbientStep中间态都保持它。 |
| C-296 | 对同一actualInput，普通nRich满足目标载体检查，但不满足全图Denotes/Satisfies；不存在把任意同载体输出都判为Denotes的函数。实际重呈现输出不等于nRich，且源到预选直线目标的AmbientStep Success仍被否定。 | `FORMAL_CHECKED_WITH_SCOPE / SAME_INPUT_BARE_OUTPUT_CHECK_IS_INSUFFICIENT` | `plainNBareAccepted/plainNDoesNotDenote/plainNNotSatisfied/bareCheckIsInsufficient/actualOutputNotPlainN/straightTargetStillFails`；同run | 这是具体不足规格的反例，不证明HoTT强制使用该规格或许诺免费来源恢复；不推出任意现实复原不可能、唯一生成方法、无条件弱Lift、GOLD闭环或内部矛盾。 |

## GOLD标准切割装配、原典记号桥与精确查询（2026-09-20）

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-ASTRA-STANDARD-GOLD-CUT-001` | `C-297..C-299` | `formal/dedekind-omega-missile/Sqrt2TableRecovery.agda`；StandardDedekind/Sqrt2CutBridge/Sqrt2CutQueries及六个原模块全部pin | `verification/runs/20260920-MP-ASTRA-STANDARD-GOLD-CUT-001-02/`；原生Cubical Agda完整依赖exit0；safe/cubical/guardedness，主模块及旧层级桥显式two-level | `FORMAL_CHECKED_WITH_SCOPE / STANDARD_CUT_PACKED_AND_QUERIES_CONSTRUCTED` |

| Claim ID | 精确主张 | 状态 | 证据 | 禁止外推 |
|---|---|---|---|---|
| C-297 | 对任意ℓ及L/U:ℚ→hPropℓ，带截断inhabited/rounded存在/located的dcutStd在Typeℓ且为Prop，StandardRealsℓ在Type(ℓ+1)且为Set。rounded双向函数对与Book字面类型Path记号的dcutBook（Type(ℓ+1)）有原生等价，后者也为Prop；dcutStd与已修正CutRealLayer.dcut亦有明确等价。 | `FORMAL_CHECKED_WITH_SCOPE / STANDARD_LOGIC_PROP_AND_UNIVERSE_BRIDGES` | `isPropDcutStd/standardRealsAreSet/isPropDcutBook/stdBookEquiv/stdLegacyEquiv`；StandardDedekind/Sqrt2CutBridge；run `20260920-MP-ASTRA-STANDARD-GOLD-CUT-001-02` | literal Book Path的层级未偷偷压低；不证明SingleOmega、同层小实数载体、全局resizing或所有实数的统一计算性。 |
| C-298 | 不改旧GOLD的Lₚ/Uₚ，实际装配goldStd、goldBook、goldLegacy，并得到goldReal:StandardReals0及goldLegacyReal:旧DedekindReals0，两者在Type1。L/U投影与旧谓词refl一致，无LEM/resizing/SingleOmega输入；在1<2处，未截断的L1⊎U2不是Prop，形成标准截断语义的实际对照。 | `FORMAL_CHECKED_WITH_SCOPE / ACTUAL_STANDARD_AND_LEGACY_GOLD_PACKING` | `goldStd/goldBook/goldLegacy/goldReal/goldLegacyReal/goldLowerIdentity/goldUpperIdentity/untruncatedLocatedValueNotProp`；Sqrt2CutBridge；同run | 是标准载体中的具体切割元素，不追加实数环x²=2或完备性定理；Type1元素存在不等于ℝLayerAt0的缩层命题；不能保留“该单个cut升格一律需LEM/resizing”的笼统解释。 |
| C-299 | 对任意q:ℚ构造GOLD真实L/U的Dec查询，并直接接到goldReal投影；q=−3时真实下切割tag归约为true，实际旧M3平方表归约为false。任意旧Spec_A正确表加有理符号判断可构造lowerViaTable，并逐q等于正确lowerQuery；原表实例在−3恢复后归约true。精确有理根交付类型仍为空。 | `FORMAL_CHECKED_WITH_SCOPE / TOTAL_EXACT_QUERY_AND_TASK_PRESERVING_RECOVERY` | `classify/packedLowerQuery/packedUpperQuery/minusThreeLowerTag/oldSquareTableRejectsMinusThree/squareFromTable/lowerViaTable/recoveryAgrees/recoveredMinusThree/noRationalRootOutput`；Queries/Recovery；同run | 比较的是同输入的谓词答案，不声称两个正确查询规格类型本身不等价；原表不能原样重命名但有明确恢复。未证明全精度近似、任意cut可计算、现实完成或四弹闭环。 |

## 固定GOLD的全二进制精度夹逼与精确相遇对照（2026-09-20）

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-ASTRA-SQRT2-APPROX-001` | `C-300..C-301` | `formal/dedekind-omega-missile/ApproxPellComparison.agda`；Sqrt2Bisection及十个原依赖全部pin | `verification/runs/20260920-MP-ASTRA-SQRT2-APPROX-001-01/`；原生Cubical完整依赖exit0；固定safe/cubical/guardedness，显式two-level | `FORMAL_CHECKED_WITH_SCOPE / ALL_BINARY_PRECISION_APPROXIMATION` |

| Claim ID | 精确主张 | 状态 | 证据 | 禁止外推 |
|---|---|---|---|---|
| C-300 | 在原GOLD的同一ℚ和L/U中，从下界1、上界2递归二分；Bracket携带真实L(lo)/U(hi)，中点严格位于两端之间，两子宽度均为旧宽度乘1/2。对全部n:ℕ，approx n嵌套且在初界内，宽度=dyadicWidth n（d0=1，d(n+1)=d(n)/2）；ApproxTask/CertifiedApprox返回实际端点、成员、宽度及恰n次refine见证，并接到goldReal谓词投影。n=2端点5/4与3/2由refl归约检查。 | `FORMAL_CHECKED_WITH_SCOPE / GENERATED_BRACKETS_AND_EXACT_REFINEMENT_CERTIFICATE` | `leftHalf/rightHalf/middleAbove/middleBelow/refineWidth/lowerFromInitial/upperToInitial/approxWidth/packedBounds/certifiedApprox/twoStepLower/twoStepUpper`；Sqrt2Bisection.agda；run `20260920-MP-ASTRA-SQRT2-APPROX-001-01` | 精度为自然数n的二进制界，不新增任意正实数ε的共终性/实数度量收敛定理；Trace计refine调用，不是CPU/物理时间或实际资源界；不一次执行全部n，不换QuoQ有理模型。 |
| C-301 | 任意有效Bracket的宽度严格正、两端不同，refine使宽度严格减少；初始Bracket不满足精度1。对每个n，依赖Σ见证同一成功ApproxTask输出宽度非零；本二分的有限ExactMeetingTask为空。该精度成功可与原Pell.D n≠0及原有理根输出空性在同一原生环境同时构造。 | `FORMAL_CHECKED_WITH_SCOPE / PRECISION_SUCCESS_DISTINCT_FROM_EXACT_MEETING` | `widthPositive/widthNeverZero/boundsNeverMeet/widthStrictlyDecreases/initialFailsPrecisionOne/successWithPositiveGap/noExactMeeting/simultaneous`；两新源码；同run | 不是精确相遇任务的成功恢复，未把Pell整数判别式当区间宽度；不声称Pell收敛/最优性、所有逼近失败或物理过程不可能，更不构成P与非P或四弹整体完成。 |

## 原四弹算术规格的请求响应总对照（2026-09-20）

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-ASTRA-SQRT2-TASK-COMPARISON-001` | `C-302..C-303` | `formal/dedekind-omega-missile/Sqrt2TaskComparison.agda`；十三个现有本地依赖全部pin | `verification/runs/20260920-MP-ASTRA-SQRT2-TASK-COMPARISON-001-01/`；原生Cubical完整依赖exit0；固定safe/cubical/guardedness及显式two-level | `FORMAL_CHECKED_WITH_SCOPE / DECLARED_ARITHMETIC_TASKS_INTEGRATED` |

| Claim ID | 精确主张 | 状态 | 证据 | 禁止外推 |
|---|---|---|---|---|
| C-302 | Request明确九族，Output/Done/Response用显式向上Lift统一层级；dispatch对每个本域请求返回Dec(Response)。六族表示/两侧查询/按n近似/旧表生成/给定旧表的下切割查询有认证响应；有理根、本二分精确相遇、Pell D归零三族响应为空。表示Done固定原GOLD L/U且任意合格表示的值等于goldReal；近似响应接实际n次Trace。输入2的下切割查询可交付，但其答案为false。不存在给本域每个请求都生成成功Response的函数。 | `FORMAL_CHECKED_WITH_SCOPE / EXPLICIT_INPUT_OUTPUT_DONE_AND_FEASIBILITY` | `dispatch/representationCanonical/approximationReplyTrace/queryAtTwoIsFeasible/queryAtTwoAnswersFalse/rootIsNotFeasible/noUniversalSuccessfulResponder`；同run | 九族含无限q/n参数，但不等于所有HoTT命题/程序；不检查任意外来候选答案。no是响应空性证书，不是已交付所请求见证；Lift不是resizing；不把请求可完成与对象命题为真混同。 |
| C-303 | 新oldTable/rationalRoot响应分别与原Spec_A/Spec_B有明确跨层等价，保留原q²=2未加正号的类型；正根细化仍为空。给定旧表的下切割响应逐q等于生成响应；−3处原表直接解释为下切割答案不满足Done。原M3否定等价保持，且无Spec_A→Spec_B总映射，新响应类型亦不等价。第四层SingleOmega→ℝLayerAt充分性以原显式输入保留。 | `FORMAL_CHECKED_WITH_SCOPE / ORIGINAL_SPEC_FIDELITY_AND_SCOPED_REFUSAL` | `tableResponseEquivOriginal/rootResponseEquivOriginal/noPositiveRootResponse/suppliedGeneratedAgreement/oldAnswerFailsLowerDone/originalM3Refusal/noOldTableToRoot/responseRefusal/smallnessIfProvided`；同run | 这些否定定理由内核接受，不是编译器报错或Agda/HoTT不对齐证据；未证明HoTT曾许诺被否定的任务等价，未证明SingleOmega必要、无条件缩层、现实失配或完整四弹闭环。 |
