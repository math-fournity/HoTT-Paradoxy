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

## 历史候选解释区：Dedekind-Ω 四层登记

> **HISTORICAL_EVIDENCE / FROZEN_TABLE_ROWS**。下方至“Astra 审计修复三收据”之前的段落和 CAND 行保存 2026-09-17—19 的历史候选解释；其中“非现实性已机械锚定”“升格才收费”“逼选已闭环”等不能作为当前结论。所有既有表格行逐字保留用于原收据身份核对，原位调整的是解释层生命周期，不修改原 run 或冻结行哈希。数学效力只按精确形式类型与当前限定判断：M1/M2/M3 的局部定理、REAL-LAYER-04 的条件充分性仍可使用，但不继承旧的理论/现实归因。当前算术与层级范围见 C297–303，实际几何与固定 Weak 原则见 C311–319，同对对象的操作分离见 C320；完整原文—代码—原典裁决由[第三十一轮执行报告](../Astra继续尝试/断点与证明机制系统检查/第三十一轮执行报告.md)拥有。此区不是当前公开判词模板。

### 历史登记：MP-DEDEKIND-OMEGA-M1（Dedekind-Ω 第一枚·过程层，2026-09-17）

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

### 历史登记：MP-DEDEKIND-OMEGA-M2（Dedekind-Ω 第二枚·声明层，2026-09-17）

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

### 历史登记：MP-DEDEKIND-OMEGA-M3（Dedekind-Ω 第三枚·识别层，2026-09-17）

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

### 历史登记：MP-DEDEKIND-OMEGA-TA（第四弹·靶 A 路径 (i)——canonicity 反例的元层检查演示，2026-09-17）

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

### 历史登记：MP-DEDEKIND-OMEGA-M3-UNC（第四弹首靶·M3 去条件化 + 027 §5 核实，2026-09-17）

来源：修订片 027 §5（待核发现与债务定位）+ §2（身份陈述与主定理模式）。本包为
第三弹识别层收据的去条件化加强，同时为第四弹靶 B（对齐矩阵）登记 ℚ 层免费格。
`registers_new_claim` 语义 = 候选锚点，非已注册数学主张。

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-DEDEKIND-OMEGA-M3-UNC` | `CAND-F2-7-M3-UNC` | `formal/dedekind-omega-missile/MissileThreeUnconditional.agda`（复用 M3 的 Spec_A/Spec_B 类型与 M2 的 spec-B-empty）；`CLAIM-PACKAGE-M3-UNC.md` | `verification/runs/20260917-MP-DEDEKIND-OMEGA-M3-UNC-01/`；Agda 2.8.0；Cubical v0.9；`--safe --cubical --guardedness`；**无 LEM、无 resizing、无任何追加假设**；exit 0；55.6s | `MACHINE_PROVED_LOCAL_UNCOMMITTED / SPEC_A_UNCONDITIONAL_AND_IDENTIFICATION_REFUTED_NOT_HOTT_CONTRADICTION` |

| ID | 主张 | 裁决 | 直接依据 | 禁止外推 |
|---|---|---|---|---|
| CAND-F2-7-M3-UNC | 在纯 Cubical Agda（无 LEM、无 resizing、无任何追加假设）中：(1) `specA-inhabited-unc : Spec_A` 无条件居住——判定表 `f : ℚ → Bool`（`f q ≡ true ↔ q·ℚq < 2r`）由 ℚ 序可构造判定 `_≟_ : (m n : ℚ) → Trichotomy m n` 直接定义，不需要 LEM（027 §5 待核发现**核实为真**）；(2) `M3-L1-unc : ¬ (Spec_A ≃ Spec_B)` 识别拒绝去条件化。债务定位：判定表在 ℚ 层免费，理想元素本体（判定表升格为实数层对象、完整 cut）才收费——完成义务在承载层跨界处收费。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED / SPEC_A_UNCONDITIONAL_AND_IDENTIFICATION_REFUTED` | run `20260917-MP-DEDEKIND-OMEGA-M3-UNC-01/` 的 `RUN.json`（`KERNEL_ACCEPTED_WITH_SCOPE`，exit 0，55.6s）与收据文件；`_≟_`/`isIrrefl<`/`isAsym<` 来自 `Cubical.Data.Rationals.Order`。 | **不**声称 HoTT 不一致；**不**推翻 M3 条件版收据（条件版仍真，本版为去条件化加强）；**不**声称完整 cut / 实数对象已无条件构造（「升格处收费」为语义读法与靶位指引）；不可证性证书属元理论（027 §4 拒证二元性），本包是对象层拒绝收据。 |

### 历史登记：MP-DEDEKIND-OMEGA-BP（Dedekind-Ω 簇·廉价副产品，2026-09-17）

来源：修订片 025 §5 保留项（「序列层存在命题可判定、搜索过程不可停机」须
分开登记；非第三枚，不得冒充识别层）。

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-DEDEKIND-OMEGA-BP` | `CAND-F2-7-BP` | `formal/dedekind-omega-missile/MissileByproductGapDecidable.agda`（消费 M1 的 `D`/`gap-never-zero`） | `verification/runs/20260917-MP-DEDEKIND-OMEGA-BP-01/`；Agda 2.8.0；Cubical v0.9；exit 0；60.6s | `MACHINE_PROVED_LOCAL_UNCOMMITTED / GAP_DECIDABLE_AND_NO_WITNESS_DISTINGUISHED` |

| ID | 主张 | 裁决 | 直接依据 | 禁止外推 |
|---|---|---|---|---|
| CAND-F2-7-BP | `decGapAt : (n : ℕ) → (D n ≡ pos 0) ⊎ ¬ (D n ≡ pos 0)`——序列层存在命题的逐点判定是已完成对象（判定为「否」）；`noGapWitness : ¬ (Σ n : ℕ, D n ≡ pos 0)`——Σ 居住性否定，与第二枚 `spec-B-empty` 同形、证据路径独立（Pell 不变量 vs 下降法）。 | `MACHINE_PROVED_LOCAL_UNCOMMITTED / DECIDABLE_OBJ_VS_UNHALTING_SEARCH` | run `20260917-MP-DEDEKIND-OMEGA-BP-01/` 的 `RUN.json`（exit 0，60.6s）与收据文件。 | 本登记机械确认「判定已完成 ≠ 搜索不终止」的区分（025 片 §5 更正的根据）；**不**声称它是 A=B 对撞或第三枚；**不**声称 HoTT 不一致。 |

### 历史登记：MP-DEDEKIND-OMEGA-GOLD（金形态 cut·第一装配期，2026-09-17；**已被 -02 四条件完整版取代**）

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

### 历史登记：MP-DEDEKIND-OMEGA-GOLD（金形态 cut·四条件完整版，2026-09-18）

接续第一装配期（`615fbd2`，rounded→ 双向 + located）与 δ 路线基础设施（`4bc020d`，
`roundedL←` 完整过核）。本节登记 **Book §11.2 四条件首次全部机器接受**：在
`roundedU←`（上集圆整 ← 方向）补齐后，`CutGoldForm.agda` 全模块 exit 0。

| proof_id | claim_id | 源码 / 包 | 运行收据 | 证据等级 |
|---|---|---|---|---|
| `MP-DEDEKIND-OMEGA-GOLD` | `CAND-F2-7-GOLD` | `formal/dedekind-omega-missile/CutInfra.agda`（`<-≤`、`·-mono-≤-nn` crux、`·-mono-<-nn`）+ `formal/dedekind-omega-missile/CutGoldForm.agda`（勘误版 L/U + isProp + hProp 包装 + inhabited×2 + disjoint + rounded→ 双向 + located + **roundedL← + roundedU← 双向见证方向**，δ := t·¼r 内在路线 + `sq-minus` 差平方展开）；`CLAIM-PACKAGE-GOLD.md` | `verification/runs/20260918-MP-DEDEKIND-OMEGA-GOLD-02/`（`--ignore-interfaces` 全量 clean 重放）；Agda 2.8.0；Cubical v0.9；`--safe --cubical --guardedness --two-level`；**无 LEM、无 resizing、无任何追加假设**；exit 0；stderr 0；stdout 哈希与 GOLD-01 一致（同一依赖树，均为纯检查日志） | `MACHINE_PROVED_LOCAL_COMMITTED_NOT_PUSHED / GOLD_FORM_FOUR_CONDITIONS_COMPLETE`（证据随 commit `f2fd012` 入库；未 push，非 VERSION_CLOSED） |

| claim | 命题（机器检查形态） | 证据等级 | 证据 | 禁止外推 |
|---|---|---|---|---|
| CAND-F2-7-GOLD-FULL | 在纯 Cubical Agda 中：(1) `·-mono-≤-nn : (k a b : ℚ) → 0r ≤ k → a ≤ b → k·ℚa ≤ k·ℚb` 与 `·-mono-<-nn : 0r < k → a < b → k·ℚa < k·ℚb`；(2) 勘误版谓词 `L q := (q<0r) ⊎ ((0r≤q)×(q··ℚq<2r))`、`U q := (0r<q)×(2r<q··ℚq)` 均为 hProp 值（`Lₚ`/`Uₚ`）；(3) Book §11.2 四条件 **全部** 机器检查通过——inhabitedL、inhabitedU、disjoint（`L q → U r → q < r`）、rounded 双向（`roundedL→`/`roundedU→` 与 **`roundedL←`/`roundedU←`**：`L q → ∃ p, q<p × L p`、`U r → ∃ q, q<r × U q`，δ 内在路线，U 侧 `q := r - (r·r-2r)·¼r`）、located（`q<r → L q ⊎ U r`，eq 支消费 `√2-irrational`）。 | `MACHINE_PROVED_LOCAL_COMMITTED_NOT_PUSHED`（commit `f2fd012`） | run `20260918-MP-DEDEKIND-OMEGA-GOLD-02/` 的 `RUN.json`（`KERNEL_ACCEPTED_WITH_SCOPE`，exit 0，stderr 0，duration 73.2s）与收据五件套；`source-manifest.json` 固定 CutGoldForm/CutInfra/DESIGN/compile.sh 哈希；GOLD-01 保留为部分装配期历史收据。 | **边界**：(a) 这是 **ℚ 层单个 cut（√2）** 的四条件构造，**不**声称 Book §11.2 意义下「实数完备性」「ℝ 不可达」或任何 ℝ 层命题——把 cut 取等价类、把「ℝ 取值命题」塌缩到单一 Ω 的下一升格仍需 LEM 或 propositional resizing（DESIGN §4 登记的收费位置，未机械化）；(b) **不**声称 HoTT/立方类型论内部矛盾或不一致；(c) `rounded←` 的 witness 是 ℚ 层显式 δ 项，**不**依赖代表元选择；(d) registers_new_claim:false——ℚ 层标准可构造计算，非 HoTT 元定理，不依赖 univalence / HIT 特有规则。 |
### 历史登记：MP-DEDEKIND-OMEGA-TA-AC（靶 A·AC 格 stuckness 演示，2026-09-17 收据 / 2026-09-18 补登记）

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

### 历史登记：MP-DEDEKIND-OMEGA-TA-LEM（靶 A·LEM 格 stuckness 演示，2026-09-18）

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

### 历史登记：MP-DEDEKIND-OMEGA-REAL-LAYER（Book §11.2「ℝ 层」陈述精确化 B0 + 充裕性 B1a，2026-09-18）

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

### 历史登记：B 线收官（B1b 诊断绕过结局 + B1b′/B2 降格确认 + B3 基准，2026-09-18，修订片 030）

> 本节登记 029 §2「两个都要」合同的收官侧。**B1b/B1b′/B2 的论断全部为元层分析
> （`AI_ADJUDICATED_PENDING_EXTERNAL_AUDIT`），非内核收据**；机器证据仅限本表
> 各节既有 run。`registers_new_claim:false`。

| 项 | 结局（机器检查形态） | 证据等级 | 证据 | 禁止外推 |
|---|---|---|---|---|
| **B1b 诊断绕过** | 零付费读法**失败**：(i) 直接构造撞尺码墙（载体 `(ℚ→hProp ℓ₀)` 活在 `Type (ℓ-suc ℓ₀)`，使 cut 降到 ℓ₀ 的 `Ω : Type ℓ₀` 即 `SingleOmega` 本身）；(ii) σ-frame（Book 取法 4）是**换靶**（σ-frame-值 cut 的另一套实数，非钉死的 `DedekindReals`）+ 新费（HIT-II 与比较义务）。换币读法**原则上存在**：(iii) Cauchy 实数免费活在 `Type₀`，但 `≃ DedekindReals` 需可数选择类原则（元层引述）。 | `META_ANALYSIS_REGISTERED`（诊断对照，非证明） | 修订片 030 §2（三路线逐条 + Book §11.2 取法 4 逐字在 CLAIM-PACKAGE §1.1）；尺码墙的机器面 = `CutRealLayer.agda` 宇宙层级（REAL-LAYER-02 源） | 结局是「某种原则必付」的**证据**、「SingleOmega 型收费必付」的**负结果**（币种不确定）；CC 路线未机械化，不据此交付任何数学结论；不静默、不以 (a) 冒充 |
| **B1b′ 必要性** | `Necessity ℓ = ℝLayerAt ℓ → SingleOmega ℓ` **正式确认 `CONJECTURE`**（029 §2 硬条款执行）。路径 1 失败分析：0/1-cut 编码 `hProp ↪ DedekindReals` 的 locatedness 在 `0≤q<r≤1` 窗口强制 `P ∨ ¬P`；路径 2 缺模型（`HoTT+CC+¬SingleOmega` 模型存在性未论证——若成立则 Necessity 在其中为假，不可证且可能不可反驳）；LEM 下后件免费（Book 取法 3 逐字）⇒ 必要性问题纯属构造性片段。 | `CONJECTURE`（不升级） | 修订片 030 §3（路径分析 + 三观察）；Book §11.2 取法 3/4 逐字（CLAIM-PACKAGE §1.1） | 收费位置判词不得 `MACHINE_PROVED`；`SingleOmega↔PropResizing` 蕴含方向仍开放；不声称「必付费」任何币种 |
| **B2 靶 A 不可归约** | **声模型论证撤回**（Astra 二审 005 采纳，030 §4 勘误）：原「两方向各有声模型」只指定单次 `LEM ℕ` 应用取值，非完整模型；且 Book `thm:not-lem`（SOURCE_REPORTED）：LEM∞ 与 univalence 不相容——ChargeDemo 组合（LEM∞ 公设 + `--cubical` 原生 UA）按 Book 不一致，无声模型，「内部证明不可能」随之失效。已机器见证仅剩**语法层事实**（refl 拒绝 + 内核亲印中性范式；exit≠0 须核对预期诊断类别）。 | `QUESTION`（理由修正：声模型/不可证论证未成立，依赖未完成模型工作或 Book 反论形式化；UA-opaque 演示（TA-01）公设非 LEM∞ 不触发不相容，原则上可救但须构造完整模型） | 030 §4 勘误块（2026-09-19 晚）+ TA 族收据（本表前节；身份修正见 TA-LEM 行） | 不因探针收据升格；Huber 维持 `SOURCE_REPORTED_NOT_REPLAYED` 按其论文演算范围使用；不声称对象层定理 |
| **B3 范围诚实性** | 当前 repo **无公开稿文本**（028 为修复方案非公开稿）——三方对照的公开稿一侧为空集，今日平凡成立。**判词基准落盘**（公开稿产生时强制）：(1) 不得「击落 HoTT」作数学主张；(2) 最高措辞 =「非现实性机械锚定 + 逼选结构」；(3) 收费表述保留币种不确定性；(4) B1b′/B2/Huber 三等级不得升格。 | `BASELINE_READY_VACUOUS_TODAY`（公开稿产生时转为对照执行） | 修订片 030 §5；audit map §5 基准条目 | 空集对照不冒充实质对照；公开稿产生之日重跑 |

### 历史登记：收官补强两件（反弹消毒收据 + 必要性 LEM-条件版，2026-09-19）

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

## 实际圆HIT整数覆盖的依赖消费链（2026-09-20）

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-ASTRA-S1-CONSUMER-001` | `C-304` | `formal/astra-s1-consumer-check/SC00.agda`；原Cubical0.9 S¹/ℤ及固定上游证明片段 | `verification/runs/20260920-MP-ASTRA-S1-CONSUMER-001-02/`；safe/cubical/guardedness，fresh完整依赖exit0；初次01的出处快照分类问题另留存 | `FORMAL_CHECKED_WITH_SCOPE / ACTUAL_DEPENDENT_CONSUMER_AND_UPSTREAM_FIDELITY` |

| Claim ID | 精确主张 | 状态 | 证据 | 禁止外推 |
|---|---|---|---|---|
| C-304 | 在原库S¹、base、loop与ℤ上，逐字提取helix至winding-hom的实际证明链，构造Iso(base≡base,ℤ)、decodeEncode的全部x/p依赖逆律、全部n的整数逆律以及全部回路p/q的winding(p∙q)=winding(p)+winding(q)。显式helixAgreement与encodeAgreement连接上游类型族/编码，windingAgreement及intLoopAgreement逐输入连接原上游函数；末端roundTripLoop/roundTripInteger/composedObservation实际消费该链。 | `FORMAL_CHECKED_WITH_SCOPE / REPLAYED_LIBRARY_CHAIN_WITH_EXPLICIT_BRIDGES` | `helix/decodeSquare/decode/decodeEncode/ΩS¹Isoℤ/winding-hom/helixAgreement/encodeAgreement/windingAgreement/intLoopAgreement/roundTripLoop/roundTripInteger/composedObservation`；SC00.agda；同run | 这是既有库证明链及保真桥的核验，不主张该基本结果原创。未用新本地HIT替代原S¹；不证明几何删点、物理时间过程、全部库消费者正确或四弹闭合。单因素修改的类型拒绝是运行对照，不增加相应数学不可能性定理。 |

## 同GOLD有理数商与截断后的实际数据消费（2026-09-20）

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-ASTRA-QUOTIENT-CONSUMER-001` | `C-305..C-306` | `formal/astra-quotient-consumer/QuotientConsumer.agda`；原CutGoldForm/CutInfra/M2 | `verification/runs/20260920-MP-ASTRA-QUOTIENT-CONSUMER-001-01/`；safe/cubical/guardedness，fresh完整依赖exit0 | `FORMAL_CHECKED_WITH_SCOPE / ACTUAL_QUOTIENT_AND_SET_VALUED_TRUNCATION_CONSUMER` |

| Claim ID | 精确主张 | 状态 | 证据 | 禁止外推 |
|---|---|---|---|---|
| C-305 | 在原GOLD使用的Rationals.Base.ℚ上，实际加乘及GOLD.L/U保持代表关系。对每个q，Rep(q)=Σr:ℤ×ℕ₊₁,pack(r)=q有[]surjective给出的mere代表；squareRep在该fiber上有显式常值性，实际rec→Set返回ℚ平方值并证明等于q·q。suppliedSquare/generatedSquare带真实Done，全部响应等于直接平方响应。目标ℚ为Set且已证明不是Prop；1/1与2/2的平方输出有明确相等证明。 | `FORMAL_CHECKED_WITH_SCOPE / INVARIANT_DATA_RECOVERY_WITH_EXPLICIT_CONSTANCY` | `addRespects/mulRespects/lowerRespects/upperRespects/mereRep/squareRepConstant/squareFromMereCorrect/squareResponseCanonical/quotientNotProp/twoOverTwoSquared`；同run | q本来就是输入，正构造不提供选择原历史代表的新能力；不把截断到Set的有条件接口说成任意数据都能恢复，也不证明全部商/截断正确或现实完成。 |
| C-306 | 真实代表1/1与2/2在ℚ中相等而原分子1与2不同；不存在observe:ℚ→ℤ对每个原分数r都满足observe(pack r)=fst r，也不存在restore:ℚ→Frac对每个r满足restore(pack r)=r。在固定q=1的Rep fiber上，rawNumerator不满足常值性，且不存在从mere Rep(1)返回并保留每个原代表分子的函数。Rich=Σq,Rep(q)显式保留给定源；两个实例裸q相等而Rich不等，给定源观察正确。 | `FORMAL_CHECKED_WITH_SCOPE / ORIGINAL_PROVENANCE_CONTRACT_SEPARATED_FROM_VALUE_TASK` | `sameRational/differentNumerators/noOriginalNumerator/noOriginalFraction/noNumeratorConstancy/noRawFromMere/sameBare/differentRich/chosenSourceLaw`；同run | 否定的是恢复每个原输入的左逆/原始分子合同，不是否定选取某个规范代表或商映射的任意右逆；加入给定原代表是输入变化。没有HoTT承诺裸商类保留该历史的证据，不构成原圆环或四弹整体失配。 |

## 原真实圆弱域Lift的统一实数原则刻画（2026-09-20）

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-ASTRA-WEAK-LIFT-PRINCIPLE-001` | `C-307..C-308` | `formal/agda-unimath/hott-z/WeakLiftConsumer.agda`；WeakLiftPrinciple及七个原点集/参数化/连续依赖 | `verification/runs/20260920-MP-ASTRA-WEAK-LIFT-PRINCIPLE-001-01/`；固定no-erasure agda-unimath，without-K，fresh完整依赖exit0 | `FORMAL_CHECKED_WITH_SCOPE / REAL_PRINCIPLE_AND_ORIGINAL_CIRCLE_LIFT` |

| Claim ID | 精确主张 | 状态 | 证据 | 禁止外推 |
|---|---|---|---|---|
| C-307 | 对原Real=Dedekindℝ₀与C281实际点集圆，RealNonzeroApartness=(∀r,¬(r=0)→apart(r,0))与原Lift=(∀p,Weak(p)→Strong(p))双向蕴含。反向用原参数化后反射第一坐标的encodeReal(r)，证明r≠0→Weak(encodeReal r)、其分母=2r²/(1+r²)，以及Strong(encodeReal r)→apart(r,0)。encodeReal(0)=east、零参数不在弱域，1参数给出弱域实例。 | `FORMAL_CHECKED_WITH_SCOPE / ACTUAL_COORDINATE_REDUCTION_AND_LOGICAL_IFF` | `realApartnessToLift/reflectFirst/encodedWeak/encodedDenominator/encodedStrongToApartness/realApartnessIffLift/encodedZeroIsEast/encodedZeroNotWeak/encodedOneWeak`；两新源码；同run | 双向是明确函数组成的逻辑↔，不是无条件原则、其否定或独立性证明；固定ℝ₀而非未声明的任意实数表示，不证明LEM必要、标准二进制Markov等价或现实失配。 |
| C-308 | 同一实数原则与实数apartness双否定稳定性、统一从r≠0输出任意实数右逆的类型互相蕴含；经C283/C284又与原保持点的refinement及原圆统一分母逆元合同互相蕴含。显式LEM₀足以给该原则。给定该原则，可取得原弱去点圆与原(0,1)度量的PointwiseHomeomorphism、原生类型路径及其实际映射作用；refinement保持原点。 | `FORMAL_CHECKED_WITH_SCOPE / EXPLICIT_INVERSE_CONTRACTS_AND_CONDITIONAL_GEOMETRIC_CONSUMER` | `realApartnessIffStability/realApartnessIffInverse/liftIffRealInverse/excludedMiddleGivesRealApartness/realPrincipleIffSamePointRefinement/realPrincipleIffCircleInverse/refinementPreservesPoint/weakIntervalHomeomorphismFromRealPrinciple/weakIntervalPathActionFromRealPrinciple`；同run | 必要性限于所列refinement/逆元合同，不是任意可能同胚的必要性；同胚这里只证给定原则的充分方向。未取得无条件弱域结果、物理变形/来源保持或全四弹闭合；继承库公设及no-erasure配置边界明确。 |

## 实数原则与二进制Markov表述的精确翻译（2026-09-20）

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-ASTRA-REAL-PRINCIPLE-SCOPE-001` | `C-309..C-310` | `formal/agda-unimath/hott-z/RealPrincipleBookScope.agda`、MarkovBookForms及四个原实数/圆依赖 | `verification/runs/20260920-MP-ASTRA-REAL-PRINCIPLE-SCOPE-001-01/`；固定no-erasure without-K，fresh完整依赖exit0 | `FORMAL_CHECKED_WITH_SCOPE / TWO_FORMULATION_TRANSLATIONS_NOT_A_REAL_MARKOV_BRIDGE` |

| Claim ID | 精确主张 | 状态 | 证据 | 禁止外推 |
|---|---|---|---|---|
| C-309 | 在原Real=ℝ₀上，RealNonzeroApartness=(∀r,¬(r=0)→apart(r,0))与RealPairApartness=(∀x y,¬(x=y)→apart(x,y))通过实际差运算双向蕴含；全点对形式又与原Circle Lift、统一实数右逆合同双向蕴含。差为零推出相等的引理显式给出。 | `FORMAL_CHECKED_WITH_SCOPE / ZERO_PAIR_TRANSLATION_ON_ORIGINAL_REALS` | `differenceZeroImpliesEqual/zeroToPairApartness/pairToZeroApartness/zeroIffPairApartness/pairPrincipleIffCircleLift/pairPrincipleIffRealInverse`；同run | 这是原模型上与原典全点对表述对应的类型，不是所有Book实数构造/宇宙的整体解释；不推出Markov、无条件原则、任意同胚必要性或现实失配。 |
| C-310 | 对原库ℕ/bool和命题性存在，BookMarkov=(∀f:ℕ→bool,¬¬∃n,f(n)=true→∃n,f(n)=true)与库Markov's-Principle（否定处处为真→mere存在假值）有显式双向函数。翻译使用bool反转及命题性存在消去，保留mere存在，不增加选定索引或搜索时限。 | `FORMAL_CHECKED_WITH_SCOPE / EXACT_BINARY_POLARITY_AND_LOGICAL_FORM_TRANSLATION` | `SomeTrue/SomeFalse/BookMarkov/flip/flipTrueToFalse/flipFalseToTrue/bookToLibrary/libraryToBook/bookIffLibraryMarkov`；同run | 只证明两种二进制表述互推，不证明任一种原则成立、否定或独立；没有把C309实数原则连接为Markov等价，仍缺相应实数编码/模型桥；不是有界搜索算法或整个理论一致性认证。 |


## 原生时间曲线族的联合连续性与原图初末态（2026-09-20）

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-ASTRA-NATIVE-MOTION-001` | `C-311..C-312` | `formal/agda-unimath/hott-z/NativeMotionBridge.agda`、NativeMotion/NativeMotionEndpoints及原几何依赖 | `verification/runs/20260920-MP-ASTRA-NATIVE-MOTION-001-01/`；固定no-erasure without-K，fresh完整依赖exit0 | `FORMAL_CHECKED_WITH_SCOPE / TIME_FAMILY_STAGE1_FULL_MOTION_TASK_OPEN` |

| Claim ID | 精确主张 | 状态 | 证据 | 禁止外推 |
|---|---|---|---|---|
| C-311 | 对原Real=ℝ₀、RealPlane积度量及原(0,1)，显式定义r(u)、正分母E(t,r)=1+(1−t)²abs(r)、stretch、bend、turn及固定y反射后的motion。对所有实时间与开参数，E正；bend分母由positiveD给资格；motionRaw与motion在Real×(0,1)联合点态连续，限制到原ClosedParameter×(0,1)仍连续。 | `FORMAL_CHECKED_WITH_SCOPE / NATIVE_RATIONAL_FAMILY_AND_JOINT_CONTINUITY` | `stretchDenPositive/motionRawContinuous/motionContinuous/closedTimeMotionContinuous`；三新原生源与同run | 不能把联合连续性当所有切片嵌入；全闭参数扩展、端部纤维、空间界、现实速度/材料/操作尚未在本包证明；不是整个Lean与HoTT模型的保真翻译。 |
| C-312 | 同一motion在t=0逐点等于(pr1 u,0)，在t=1逐点等于原paramPlane(realParameter u)，由原mInterior准确接到既有mCompletion(openIntoClosed u)，初态准确接到nCompletion。固定reflectY为对合、保持初始直线，rawFinalOrientation给出原负y公式与当前m图的反射关系；曲线参数u不变。 | `FORMAL_CHECKED_WITH_SCOPE / EXACT_ORIGINAL_ENDPOINT_DIAGRAMS_AND_ORIENTATION` | `motionAtZero/motionAtOne/motionAtOneOriginal/initialOriginalDiagram/finalOriginalDiagram/reflectionInvolution/reflectionFixesLine/rawFinalOrientation`；同run | 初末态等式不是全过程保持固定端部/环境同胚/源历史；最终图是原Strong参数化，未无条件声称覆盖全Weak去点圆；全R-CURVE及四层共同任务、HoTT失配仍未完成。 |


## 原生时间曲线族的每片拓扑嵌入（2026-09-20）

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-ASTRA-NATIVE-EMBEDDING-001` | `C-313` | `formal/agda-unimath/hott-z/NativeMotionEmbedding.agda`、NativeStretchInverse/NativeBendInverse/NativeTurnInverse及原F依赖 | `verification/runs/20260920-MP-ASTRA-NATIVE-EMBEDDING-001-01/`；固定no-erasure without-K，fresh完整依赖exit0 | `FORMAL_CHECKED_WITH_SCOPE / ACTUAL_SLICE_TO_IMAGE_HOMEOMORPHISMS` |

| Claim ID | 精确主张 | 状态 | 证据 | 禁止外推 |
|---|---|---|---|---|
| C-313 | 对每个原Real时间t，未改动的motion(t)给出原OpenRealInterval到curveImageMetric(t)=im-Metric-Space intervalMetric realPlaneMetric (motion t)的PointwiseHomeomorphism。forward准确为map-unit-im(motion t)，backward为显式recoverInterval(t)；双方连续及两个逆律均证明，导出单射及原闭时间限制。逆链中stretch/bend坐标图分母和turn行列式均具正性证明，mere像成员只消去到命题，不选取任意原像。 | `FORMAL_CHECKED_WITH_SCOPE / NATIVE_TOPOLOGICAL_EMBEDDING_WITH_ACTUAL_AMBIENT_SUBSPACE_METRIC` | `stretchLeftInverse/stretchInverseContinuous/bendLeftInverse/bendInverseContinuous/turnDetPositive/turnLeftInverse/turnUndoContinuous/imageInduction/recoverIntervalContinuous/recoverIntervalLeft/recoverIntervalRight/motionSliceHomeomorphism/motionSliceInjective/closedTimeSliceHomeomorphism`；四新原生源与同run | 不是仅集合is-emb；也不是全平面环境同胚过程、完整闭参数延拓/纤维、空间界或物理执行。未无条件覆盖全Weak去点圆，未建立全Lean模型保真或HoTT全局一致性/失配；完整F与四层目标仍开放。 |


## 原生时间族的同源闭参数延拓（2026-09-20）

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-ASTRA-NATIVE-CLOSED-MOTION-001` | `C-314..C-315` | `formal/agda-unimath/hott-z/NativeClosedMotionEndpoints.agda`、NativeClosedMotionBase/Continuity/Interior及原F依赖 | `verification/runs/20260920-MP-ASTRA-NATIVE-CLOSED-MOTION-001-01/`；固定no-erasure without-K，fresh完整依赖exit0 | `FORMAL_CHECKED_WITH_SCOPE / SAME_CLOSED_EXTENSION_AND_EXACT_DIAGRAMS` |

| Claim ID | 精确主张 | 状态 | 证据 | 禁止外推 |
|---|---|---|---|---|
| C-314 | 原Real时间t、原ClosedParameter u∈[0,1]上，closingD=gap(u)+(1−t)²abs(center(u))、closingN=scale(t)center(u)+offset(t)closingD、closingK=closingD²+(t closingN)²；证明对所有t/u有closingK>0，定义同源closedBase/closedMotion，证明在Real×[0,1]联合连续及原闭时间方形限制。正性使用严格序和apartness cotransitivity，无需决定t=1的新原则参数。 | `FORMAL_CHECKED_WITH_SCOPE / POSITIVE_CLOSED_DENOMINATOR_AND_JOINT_CONTINUITY` | `closedCenterAbsBound/closingDPositiveBefore/closingKFromNonzeroCenter/closingKPositive/closedMotionContinuous/closedSquareMotionContinuous`；同run | 原有库公设仍明确；不称其最小性/一致性；不自动证明完整纤维、t<1端部分离、空间/速度界、物理执行或全模型翻译。 |
| C-315 | 对所有原实时间t与原开参数u，closedMotion(t,openIntoClosed u)=motion(t,u)。在整个原闭参数域，t=0逐点等于nCompletion，t=1逐点等于mCompletion的平面图。最终两个边界参数都映到east，故最终闭域函数非单射；同一closedMotion限制到原开参数对每个t仍单射，由C313及内点一致性连接。 | `FORMAL_CHECKED_WITH_SCOPE / EXACT_INTERIOR_AND_FULL_INITIAL_FINAL_DIAGRAMS` | `stretchAsClosingFraction/closedBaseMatchesBend/closedAgreesInterior/closedInitialDiagram/closedFinalDiagram/closedFinalLeft/closedFinalRight/closedFinalNotInjective/closedInteriorInjective`；同run | 闭参数新增的0/1不是原开区间成员；闭域非单射与开域单射不是同一命题矛盾。未证明最终只有两端形成非平凡纤维，未证明所有t<1端部分离/统一空间界、全Weak覆盖或原现实任务/四层完成。 |


## 原闭时间族的精确相遇时刻与完整末态纤维（2026-09-20）

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-ASTRA-NATIVE-ENDPOINT-FIBERS-001` | `C-316..C-317` | `formal/agda-unimath/hott-z/NativeCompletionFibers.agda`、NativeEndpointSeparation及原F依赖 | `verification/runs/20260920-MP-ASTRA-NATIVE-ENDPOINT-FIBERS-001-01/`；固定no-erasure without-K，fresh完整依赖exit0 | `FORMAL_CHECKED_WITH_SCOPE / EXACT_TIME_AND_COMPLETE_FIBER_RELATION` |

| Claim ID | 精确主张 | 状态 | 证据 | 禁止外推 |
|---|---|---|---|---|
| C-316 | 对未改动的closedMotion，∀原实t<1，两个闭参数端点的像不相等；在原ClosedParameter时间域[0,1]中，两端同像当且仅当t=closedOne。证明通过反射/turn/bend的实际逆、正分母和两端分数差归约，不以有限采样替代。 | `FORMAL_CHECKED_WITH_SCOPE / ENDPOINT_MEETING_IFF_FINAL_TIME` | `reverseClosedBase/closedFractionEquality/endpointDZero/endpointDOne/endpointNZero/endpointNOne/closedEndpointsDistinctBefore/endpointMeetingTime`；同run | t<1不同与t=1相同是不同条件，不是矛盾；未另定义/证明物理距离或速度、未给空间界或环境同胚过程；原参数端点非原开区间元素。 |
| C-317 | 对所有原闭参数u,v，mCompletion(u)=mCompletion(v) iff FullFiberRelation(u,v)，其中关系为命题性(u=v)或(u=0且v=1)或(u=1且v=0)。通过原closedFinalDiagram，同一双向分类准确适用于closedMotion(1)。先由实际分母证明内点纤维唯一，再证明严格有序同像参数为端点，最后用abs(u−v)的located分支构造全关系。 | `FORMAL_CHECKED_WITH_SCOPE / COMPLETE_FINAL_FIBERS_AS_PROPOSITIONAL_RELATION` | `completionDenominator/gapPositiveFromStrong/fiberAtInterior/orderedFiberEndpoints/pointEqualityToFiberRelation/fiberRelationToPointEquality/completionFiberClassification/closedFinalFiberClassification`；同run | 析取在Prop中，不是任意实数相等decider、可选输出标签或有界搜索算法；没有新LEM/Lift/choice参数不证明库公理最小性/一致性；不升级为全Weak覆盖、物理任务或四层整体完成。 |


## 原生时间族统一空间界与同图证据记录（2026-09-20）

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-ASTRA-NATIVE-MOTION-BUNDLE-001` | `C-318..C-319` | `formal/agda-unimath/hott-z/NativeMotionComplete.agda`、NativeSpatialInequalities/NativeClosedSpatialCoefficients/NativeClosedSpatialBounds及原F/Weak原则依赖 | `verification/runs/20260920-MP-ASTRA-NATIVE-MOTION-BUNDLE-001-01/`；固定no-erasure without-K，fresh完整依赖exit0 | `FORMAL_CHECKED_WITH_SCOPE / DECLARED_GEOMETRY_COMPLETE_WEAK_CONDITIONAL` |

| Claim ID | 精确主张 | 状态 | 证据 | 禁止外推 |
|---|---|---|---|---|
| C-318 | 对原闭时间t∈[0,1]和原闭参数u∈[0,1]，未改动closedMotion两个坐标绝对值均≤real-ℕ256；沿全内点一致性，同一界适用于原motion的所有开参数。证明由原系数/分子界、t<1/2或t>1/4的located分支、正分母与平方和估计给出，无有限采样。 | `FORMAL_CHECKED_WITH_SCOPE / UNIFORM_COORDINATE_BOUND_256` | `absProductSquares/quotientAbsBound/closingNAbsBound/earlyKScale/lateNSquareBound/closedBaseBounds/closedMotionUniformBound/motionUniformBound`；同run | 明确粗坐标界256，不称Lean的60、最优界或欧氏半径256；不是速度/弧长/物理实现、环境同胚或所有实时间无条件空间界。 |
| C-319 | NativeMotionEvidence的12字段在同一未改动motion/closedMotion和原域上装配联合连续、每片实际像同胚、内点一致、原n/m全初末图、端部相遇时间、完整纤维及开闭参数界。另对该固定末态参数化定义WeakFinalCoverage=∀w∈原Weak去点圆,∃u∈原开区间,motion(1,u)=w的平面点；证明它↔原Circle Lift↔RealNonzeroApartness。给定Lift，显式返回原参数及命中原点的等式。 | `FORMAL_CHECKED_WITH_SCOPE / SAME_MAP_RECORD_AND_EXACT_WEAK_COVERAGE_CRITERION` | `WeakFinalCoverage/ChosenWeakFinalOutput/liftGivesChosenWeakFinalOutput/weakFinalCoverageGivesLift/weakFinalCoverageIffLift/weakFinalCoverageIffRealPrinciple/NativeMotionEvidence/nativeMotionEvidence`；同run | 未给无条件Weak覆盖、原则否定/独立性或LEM必要性；必要性仅该固定最终图的覆盖，不是任意同胚必需。记录装配不证明物理/全Lean模型翻译/四层失配或整体Goal完成；旧公设及配置边界保持。 |


## 同一原生几何对象对上的操作合同分离（2026-09-21）

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-ASTRA-NATIVE-TASK-INTEGRATION-001` | `C-320` | `formal/agda-unimath/hott-z/NativeTaskIntegration.agda`及原NativeMotion/Rich/FiniteTrace依赖 | `verification/runs/20260921-MP-ASTRA-NATIVE-TASK-INTEGRATION-001-01/`；固定no-erasure without-K，fresh完整依赖exit0 | `FORMAL_CHECKED_WITH_SCOPE / SAME_PAIR_DISTINCT_OPERATIONS` |

| Claim ID | 精确主张 | 状态 | 证据 | 禁止外推 |
|---|---|---|---|---|
| C-320 | 固定原nRich/mRich。CurveRun(r,s)要求真实连续切片嵌入族、原闭图初末态、内点一致、实际正向切片映射和坐标界256；actualCurveRun以未改动原F给出CurveRun(nRich,mRich)。同一对象对的原有限AmbientStep Success为空，故不存在从该CurveRun成功转为该Ambient成功的函数，不存在对所有Rich对的统一转换，两成功类型不等价。原非平凡ambient交换控制及Rich不相等同时保留。 | `FORMAL_CHECKED_WITH_SCOPE / NO_SUCCESS_PRESERVING_CROSS_CONTRACT_ADAPTER` | `CurveRun/actualCurveRun/samePairDifferentOperations/noCurveToAmbientAtActualPair/noUniformCurveToAmbient/noCurveAmbientEquivalence/nontrivialAmbientControl/samePairStillRichDistinct`；同run | 对象对相同但操作/完成类型不同，不是同一P与非P；未证明HoTT实际承诺被否定转换。不是全部现实复原/生产历史、无条件Weak覆盖、任意操作不可达或完整四弹失配/一致性认证。 |

## 原Weak最终图覆盖的Markov必要后果（2026-09-21）

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-ASTRA-WEAK-COVERAGE-MARKOV-001` | `C-321–C-322` | `formal/agda-unimath/hott-z/WeakCoverageMarkov.agda`、`BinaryWitnessReal.agda`、`BinaryWitnessWeights.agda`及原几何/原则依赖 | `verification/runs/20260921-MP-ASTRA-WEAK-COVERAGE-MARKOV-001-01/`；固定no-erasure without-K，fresh完整依赖exit0 | `FORMAL_CHECKED_WITH_SCOPE / ACTUAL_BINARY_REAL_AND_FIXED_WEAK_COVERAGE_IMPLIES_MARKOV` |

| Claim ID | 精确主张 | 状态 | 证据 | 禁止外推 |
|---|---|---|---|---|
| C-321 | 对任意f:ℕ→Bool，以L_f(q)=(q<0)∨∃n[f(n)=true∧q<1/(n+1)]实际构造ℝ(lzero)中的Dedekind实数；非空、rounded、上界补集及located由有理权重与有限前缀搜索给出。证明非负、SomeTrue(f)↔0<x_f、x_f=0↔¬SomeTrue(f)，以及¬¬SomeTrue(f)→x_f≠0、x_f apart 0→SomeTrue(f)；全false取零和全true严格正的实际控制同时成立。 | `FORMAL_CHECKED_WITH_SCOPE / SMALL_DEDEKIND_BINARY_WITNESS_ENCODING` | `weight/smallWeight/finiteSearch/lowerWitnessCut/locatedWitnessCut/binaryWitnessReal/witnessIffPositive/zeroIffNoWitness/doubleNegWitnessGivesNonzero/apartWitnessGivesSomeTrue/falseSequenceRealIsZero/trueSequenceRealIsPositive`；同run | exists及∨按命题截断，不偷选全无限序列；未给所有序列的零/正判定，不是无限搜索总完成算法；新源未加入LEM/Markov/choice公设，继承基线公设仍显式；非物理完成/全理论声性。 |
| C-322 | 由C321实际编码推出RealNonzeroApartness→BookMarkov，其中BookMarkov=(f:ℕ→Bool)→¬¬(∃n,f n=true)→∃n,f n=true。再经原同一圆周/最终图的已证桥得到RealPairApartness、Circle Lift、UniformRealInverse和固定WeakFinalCoverage各自蕴含BookMarkov；并翻译为库Markov形式。¬BookMarkov→¬WeakFinalCoverage仅为显式条件逆否，其前提未提供。 | `FORMAL_CHECKED_WITH_SCOPE / FORWARD_PRINCIPLE_BRIDGE_ON_ACTUAL_WEAK_MAP` | `realApartnessImpliesBookMarkov/pairApartnessImpliesBookMarkov/circleLiftImpliesBookMarkov/fixedWeakCoverageImpliesBookMarkov/realInverseImpliesBookMarkov/fixedWeakCoverageImpliesLibraryMarkov/noFixedWeakCoverageIfNotMarkov`；同run | 不声称Markov→任意Dedekind RNZA或两者等价；未证基线独立/不可证、LEM或resizing必要性、任意同胚必需、无条件Weak覆盖或其否定；不把已知原典方向和当前实例连接称HoTT独有失败、现实失配或完整四弹成功。 |

## Markov反向的实际表示数据与显式可数选择（2026-09-21）

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-ASTRA-MARKOV-REVERSE-001` | `C-323–C-324` | `formal/agda-unimath/hott-z/MarkovCountableChoice.agda`、`MarkovRationalBounds.agda`及原cut/圆周/前向依赖 | `verification/runs/20260921-MP-ASTRA-MARKOV-REVERSE-001-01/`；固定no-erasure without-K，fresh完整依赖exit0 | `FORMAL_CHECKED_WITH_SCOPE / DATA_SENSITIVE_AND_EXPLICIT_CHOICE_CONVERSES` |

| Claim ID | 精确主张 | 状态 | 证据 | 禁止外推 |
|---|---|---|---|---|
| C-323 | 对x:原ℝ(lzero)及具体RationalBoundSequence(x)，每n给p_n<x<q_n且q_n<p_n+1/(n+1)。实际Bool测试判定0<p_n或q_n<0，证明mere命中存在↔x apart 0，故BookMarkov与x≠0及该界序列给apart；整列界的mere存在亦足够，截断只消去到apart命题。有理实数有显式界序列，零无命中、一有命中控制成立。另对C321实际binaryWitnessReal(f)族，不加可数选择假设即有BinaryRealApartness↔BookMarkov。 | `FORMAL_CHECKED_WITH_SCOPE / SUPPLIED_BOUNDS_AND_BINARY_SUBFAMILY_MARKOV_CHARACTERIZATION` | `BoundAt/RationalBoundSequence/hitBool/apartnessIffDetection/markovWithBoundsGivesApartness/rationalBoundSequence/zeroNoDetection/oneDetection/markovWithMereBoundsGivesApartness/binaryApartnessIffMarkov`；同run | 给定界序列或其整列存在不同于逐精度存在；特定二元编码族不冒充所有Dedekind实数；未给Markov实例、任意实数的无条件反向或无限搜索总完成算法。 |
| C-324 | `pointwiseMereBounds`直接取得每n的截断界存在；显式参数ac:level-ACℕ(lzero)应用于具体的小集合族BoundAt(x,n)，给每x的整列界之mere存在。由此证明ac→(RNZA↔BookMarkov)、ac→(原固定WeakFinalCoverage↔BookMarkov)、ac→(UniformRealInverse↔BookMarkov)。给定ac与BookMarkov还得到原Circle Lift、完整Weak覆盖及命中同一原最终图的ChosenWeakFinalOutput。 | `FORMAL_CHECKED_WITH_SCOPE / COUNTABLE_CHOICE_CONDITIONAL_ORIGINAL_WEAK_RECOVERY` | `boundAtSet/pointwiseMereBounds/countableChoiceGivesMereBounds/suppliedBoundsMarkovGivesRNZA/choiceMarkovGivesRNZA/rnzaIffMarkovWithChoice/choiceMarkovGivesCircleLift/choiceMarkovGivesWeakCoverage/choiceMarkovGivesChosenWeakOutput/weakCoverageIffMarkovWithChoice/inverseIffMarkovWithChoice`；同run | ac为自然数索引小集合族的截断选择，非所有类型的任意全局选择算子；未在新源加入其或Markov的postulate/实例。未证选择必要、最弱、独立或不可证；未去掉假设得到任意Dedekind反向，不等于物理执行、HoTT错误承诺、内部矛盾或完整四弹成功。 |

## 最小 OriginDirectedDiagram 的原生表达与忘却控制（2026-09-21）

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-ASTRA-ORIGIN-DIRECTED-DIAGRAM-001` | `C-325` | `formal/astra-breakpoint-check/OriginDirectedDiagram.agda`，依赖 `GeometricBoundaryObservation`/ `BoundaryIncidence` | `verification/runs/20260921-MP-ASTRA-ORIGIN-DIRECTED-DIAGRAM-001-03/`；Cubical Agda 2.8.0 / cubical-0.9，exit 0；-01/-02 保留为类型错误修复历史 | `FORMAL_CHECKED_WITH_SCOPE / MINIMAL_ORIGIN_STRUCTURE_EXPRESSIBLE` |

| Claim ID | 精确主张 | 状态 | 证据 | 禁止外推 |
|---|---|---|---|---|
| C-325 | 在原生 Cubical Agda 中可定义最小 `OriginDirectedDiagram = Σ static:RichDiagram. ((Bool→Bool)×Bool)`，其字段保留 static boundary/source 图、trace label 和 done label。给定 `originN`/ `originM`，可证明 `bareOrigin originN ≡ bareOrigin originM`，但不存在两完整对象之间的 path，且不存在一个以裸 `Type` 为输入、同时恢复这两个给定对象的函数。另一方面，沿 `swappedDiagramPath` 通过 `liftStatic` 得到完整 `originTransport`，并保持 trace/done label。 | `FORMAL_CHECKED_WITH_SCOPE / MINIMAL_ORIGIN_STRUCTURE_EXPRESSIBLE` | `sameBareCarrier/noOriginPath/noOneBareOriginRecovery/originTransport/transportPreservesTrace/transportPreservesDone`；成功 run -03；失败 run -01（未导入 `∘`）和 -02（错误 Sigma path）保留。 | 这是有限接口控制，不是完整实圆—去点—闭合过程、物理 trace 或一般 `R_origin` 理论；不证明 HoTT 不可表达该结构，不证明实际 K、理论—实现差异、自然误用、HoTT 缺陷或四弹完成。 |
| C-326 | 对 `Bare : RichCurve → UU` 定义 `PresentationFiber A = Σ(r:RichCurve), Bare r = A`。在 `A = OpenRealInterval`，`transportedRich` 与 `nRich` 都给出 fiber 成员；前者满足 `EndCoincidence`，后者不满足，且不存在两成员之间的 path。 | `FORMAL_CHECKED_WITH_SCOPE / SAME_BARE_FIBER_HAS_DISTINCT_PRESENTATIONS` | `PresentationFiber/transportedMInOpenFiber/nInOpenFiber/transportedFiberClosed/nFiberNotClosed/noTransportedRichPath/noOpenFiberPath`；`MP-ASTRA-PRESENTATION-FIBER-001` run。 | 这是 `Bare` 忘却映射的指定 fiber 局部控制，不是完整来源/过程/Done 对象、一般纤维理论、HoTT 缺陷、实际 K、理论—实现差异或现实任务结论。 |

## MO3有限阶段关系与原生直接合成的Acc资格（2026-09-23）

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-MO3-STAGE-COLIMIT-001` | `C-327–C-330` | `formal/mo3/stage-colimit/StageColimit.agda`，真实Cubical0.9 SeqColim/Acc/PT | `verification/runs/20260923-MO3-STAGE-COLIMIT-001-04/`；Agda2.8.0-3d04bac，safe/cubical/guardedness，exit0；原始失败和错误赋值控制保留 | `FORMAL_CHECKED_WITH_SCOPE / LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED` |

| Claim ID | 精确主张 | 状态 | 证据 | 禁止外推 |
|---|---|---|---|---|
| C-327 | 对每个n:ℕ和x:Stage n=Fin(suc n)，其中StageStep n y x=(suc(fst y)≡fst x)，有Acc(StageStep n,x)。 | `FORMAL_CHECKED_WITH_SCOPE` | `natAccessible/liftAccessible/stageWellFounded`；同run | 不声称任意有限关系良基，不等物理遍历全部输入已完成。 |
| C-328 | 对任意n及x,y:Stage n，StageStep n y x推出StageStep(suc n)(fsuc y)(fsuc x)；Stages以这些fsuc作为结构映射。 | `FORMAL_CHECKED_WITH_SCOPE` | `Stages/stepPreserved`；同run | 保边不被加强为保Acc或保终点；未声称任意嵌入的性质。 |
| C-329 | 对原生Total=SeqColim Stages，TotalStep y x为某同一stage从b到a的递归边（StageStep n a b）及incl a=y、incl b=x的mere image。terminal k=incl{k}fzero构成显式后继链；∀k，Acc TotalStep(terminal k)→⊥，因此WellFounded TotalStep→⊥。 | `FORMAL_CHECKED_WITH_SCOPE` | `TotalStep/terminal/terminalStep/terminalNotAccessible/totalNotWellFounded`；同run | 只否定该精确关系的Acc，不证明某次运行永不结束、现实不可完成、HoTT许诺免费保Acc或内部矛盾；不是所有colimit定理。 |
| C-330 | 对任意bound:ℕ，用恒定Stage bound、identity映射的原生SeqColim和同样阶段边mere image定义FrozenStep，则WellFounded FrozenStep。 | `FORMAL_CHECKED_WITH_SCOPE / FROZEN_STAGE_POSITIVE_CONTROL` | `Frozen.Constant/Frozen.rank/Frozen.rankStep/Frozen.frozenAccessible/Frozen.frozenWellFounded`；同run | 正控制改变为不再增长的阶段族，不自动是同一动态任务的解决；不消解所有现实解释或全理论问题。 |

## 既有C-326包的缺失索引定位补全（2026-09-23）

本次只补registry及旧RUN.json已登记的包→claim/source/run导航关系。旧C-326行保留；没有修改旧run、补造其index_status或冻结行，也没有在本轮重新认证旧数学结果。

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-ASTRA-PRESENTATION-FIBER-001` | `C-326` | `formal/agda-unimath/hott-z/PresentationFiber.agda` | `verification/runs/20260922-MP-ASTRA-PRESENTATION-FIBER-001-01/`；proof/claim身份及exit0仅按旧RUN.json转述，index_status缺失和row-manifest缺失仍保留 | `SOURCE_REPORTED_NOT_REPLAYED / LEGACY_PACKAGE_LOCATOR_RESTORED_NOT_RECERTIFIED` |

## MO3双环路的原生运输次序与逆序恢复（2026-09-24）

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-MO3-BOUQUET-ORDER-001` | `C-331–C-334` | `formal/mo3/bouquet-order/BouquetOrder.agda`；原库Bouquet、ua、subst | `verification/runs/20260924-MO3-BOUQUET-ORDER-001-02/`；Agda2.8.0-3d04bac/Cubical0.9，safe/cubical/guardedness，exit0；首run选项失败及WrongOrder拒绝保留 | `FORMAL_CHECKED_WITH_SCOPE / LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED` |

| Claim ID | 精确主张 | 状态 | 证据 | 禁止外推 |
|---|---|---|---|---|
| C-331 | Space=Bouquet Bool，Mark有a/b/c；State base=Mark，loop false沿ua(swapAB)，loop true沿ua(swapBC)，其中swapAB交换a/b且固定c，swapBC交换b/c且固定a。α=loop false，β=loop true，act p=subst State p，则act(α∙β)a≡c及act(β∙α)a≡b。 | `FORMAL_CHECKED_WITH_SCOPE` | `actα/actβ/αβ-a/βα-a`；同run | 固定族/两路径/初标记，不对全部族、路径字或现实仪器外推。 |
| C-332 | 同C331的精确族/路径，act(α∙β)a≡act(β∙α)a→⊥，且(α∙β)≡(β∙α)→⊥。 | `FORMAL_CHECKED_WITH_SCOPE` | `c≢b/outputsDifferent/pathsDifferent`；同run | 只否定这两个相等命题；不称HoTT规则矛盾或所有回路均不可交换。 |
| C-333 | 对同一State，任意p,q:base≡base和x:Mark，act(sym p)(act p x)≡x；并有act(sym q∙sym p)(act(p∙q)x)≡x。 | `FORMAL_CHECKED_WITH_SCOPE / SAME_FAMILY_INVERSE_CONTROL` | `restore/restoreTwo/restoreComposite`；同run | 使用实际路径的逆且次序反转；不把交换原操作当逆操作，不证明物理可逆性或历史圆环复原。 |
| C-334 | 对任意p:base≡base和x:Mark，常值族λ(_:Space)→Mark中的subst沿p保持x。 | `FORMAL_CHECKED_WITH_SCOPE / CONSTANT_FAMILY_CONTROL` | `constantControl`；同run | 常值族改变了依赖结构，只作敏感性对照，不替C331原族的观察。 |

## MO3有理区间的有限原索引交付与一般索引边界（2026-09-24）

本包R是固定CutRealLayer.DedekindReals ℓ-zero；InUnit按Book下截集包含式定义0≤x≤1。Cover F xs要求每个这样的实际cut点merely落在xs中某个原索引的开区间。Book的紧致性定理本身不由本包重新证明；输入mere有限子覆盖与仅有任意逐点覆盖分别保留。

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-MO3-FINITE-COVER-001` | `C-335–C-339` | `formal/mo3/finite-cover/GenericFiniteCover.agda`及manifest中全部本地传递依赖 | `verification/runs/20260924-MO3-FINITE-COVER-001-08/`；Agda2.8.0/Cubical0.9，safe/cubical/guardedness/two-level，exit0；保留索引匹配计算警告、失败与错误证书控制 | `FORMAL_CHECKED_WITH_SCOPE / LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED` |

| Claim ID | 精确主张 | 状态 | 证据 | 禁止外推 |
|---|---|---|---|---|
| C-335 | ∀F:ℕ→ℚ×ℚ及xs:List ℕ，严格重叠Cert F xs→Cover F xs；反向Cover F xs→∥Σys:List ℕ,Cert F ys∥。Cert含首左端<0、相邻严格重叠、末右端>1。反向可重排/另选链，不声称同一xs本身满足链顺序。 | `FORMAL_CHECKED_WITH_SCOPE` | `IntervalCover.chainSound`、`FiniteSubcover.finiteCoverToChain`；实际rationalCut与buildChain；同run | 覆盖全部给定cut区间点，非有限采样；不由此证明任意逐点覆盖具有有限子覆盖。 |
| C-336 | ∀F:ℕ→Interval，∥Σxs:List ℕ,Cover F xs∥→Σxs:List ℕ,Cover F xs；并经双向membership映射得到同一GenericCover合同在I=ℕ处的natSelector。 | `FORMAL_CHECKED_WITH_SCOPE` | `extractFiniteSubcover/toGenericCover/toNatCover/natSelector`；同run | 依赖实际mere有限子覆盖输入及给定Nat索引函数；不恢复某个隐藏的原选表，不从仅有点覆盖无条件取得紧致性。 |
| C-337 | overlapping族0↦(-1,3/4)、1↦(1/4,2)、其余↦(2,2)的给定mere有限覆盖输入，natSelector输出原列表[0,1]（Path等式；较早直接构造输入另有refl计算）。touching族0↦(-1,1/2)、1↦(1/2,2)、其余↦(2,2)在实际rationalCut(1/2)处无索引覆盖，故∀xs，Cover touching xs→⊥。 | `FORMAL_CHECKED_WITH_SCOPE / POSITIVE_AND_GAP_CONTROLS` | `selectedIndices/fromMereChainIndices/extractedOriginalIndices/natSelectorIndices/halfInUnit/touchingMissesHalf/touchingNoFiniteCover`；同run | touching不满足覆盖输入，是错误实例；不由软件有限未命中推出无界失败或物理完成结论。 |
| C-338 | 每个有限Nat列表xs在某有限n的words n(upto n)中出现；若候选集中有Cert，则inspect成功；由mere成功stage可取得唯一最小stage并提取真实列表和Cert。 | `FORMAL_CHECKED_WITH_SCOPE / DECLARED_LIST_GENERATOR_COVERAGE` | `generatorComplete/inspectComplete/certificateStage/leastStage/fromMereChain`；同run | 完备性仅本有限列表生成器，不是全HoTT搜索完备；保留UnsupportedIndexedMatch限制，不称任意transported证明都会定义性归约。 |
| C-339 | 不存在UniformSelector=(I:Type₀)(F:I→Interval)→∥Σxs:List I,GenericCover I F xs∥→Σxs:List I,GenericCover I F xs。归约用恒定(-1,2)区间族、真实非空unit interval及既有univalent无统一无标签选点证明。 | `FORMAL_CHECKED_WITH_SCOPE / UNIFORM_INDEX_INTERFACE_BOUNDARY` | `singleCover/mereConstantCover/coverHead/choiceFromSelector/noUniformSelector`；同run中的NoCanonicalPoint精确依赖 | 不否定每个固定I有某个选择或额外枚举/标签下的算法；不声称Book承诺此强接口，不构成HoTT矛盾或现实相对失配。 |

## MO3整开区间与严格内缩余量的有限覆盖（2026-09-24）

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-MO3-OPEN-COVER-MARGIN-001` | `C-340–C-341` | `formal/mo3/finite-cover/OpenCoverMargins.agda`及manifest中的真实cut/有理数依赖 | `verification/runs/20260924-MO3-OPEN-COVER-MARGIN-001-01/`；safe/cubical/guardedness/two-level，exit0，无warning；WrongWholeCover错误边界控制另存 | `FORMAL_CHECKED_WITH_SCOPE / LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED` |

| Claim ID | 精确主张 | 状态 | 证据 | 禁止外推 |
|---|---|---|---|---|
| C-340 | 固定R=DedekindReals ℓ-zero，Inner=Σl,r:ℚ,(0<l)×(l<r)×(r<1)，OpenUnit x=Lower x 0×Upper x 1。∀x，OpenUnit x→∥Σi:Inner,CoveredBy i x∥；但∀xs:List Inner，FiniteCoversOpen xs→⊥，其中有限覆盖保留原Inner成员与同一pointwise目标。 | `FORMAL_CHECKED_WITH_SCOPE` | `pointwiseInnerCover/smallBound/lookupBound/noFiniteInnerCover`；同run，漏点为实际rationalCut(mid 0 s) | 是此固定族的pointwise性质，未形式化Book inductive-cover HIT或否定其紧致性定理；不由数学稠密性推出物理事实。 |
| C-341 | 对所有有理0<a<b<1，存在给定数据i:Inner，使∀x:R，ClosedBetween a b x→CoveredBy i x；ClosedBetween按下cut包含定义a≤x≤b。给出的i端点是mid 0 a和mid b 1，另有[1/4,3/4]实例。 | `FORMAL_CHECKED_WITH_SCOPE / STRICT_INNER_TARGET_POSITIVE_CONTROL` | `innerChoice/innerClosedSingle/closedExample`；同run | 正控制改变目标为固定严格内缩闭区间，不是原整个OpenUnit任务的完成，也不证明任意族的compactness。 |

## MO3-C的Bool函数编码积与依赖计算接口（2026-09-24）

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-MO3-COVERAGE-ENCODED-PAIR-001` | `C-342–C-343` | `formal/mo3-coverage/encoded-pair/EncodedPair.agda`；本地Bool/Nat/Id，显式ext/ext-id参数 | `verification/runs/20260924-MO3-COVERAGE-ENCODED-PAIR-001-02/`；Agda2.8.0-3d04bac，safe/without-K/exact-split，exit0；NEG02拒绝裸refl为运行控制 | `FORMAL_CHECKED_WITH_SCOPE / LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED` |

| Claim ID | 精确主张 | 状态 | 证据 | 禁止外推 |
|---|---|---|---|---|
| C-342 | 固定本地Bool/Nat/Id及Encoded=Bool→Nat；给定对Bool索引Set族的dependent ext与恒等律ext(λx.refl)=refl，对所有C:Encoded→Set、d:Πa,b:Nat.C(pair a b)、a,b:Nat，指定encoded-elim C d(pair a b)=d a b。η-canonical与delivered-zero为同假设下的中间/实例结果。 | `FORMAL_CHECKED_WITH_SCOPE / EXPLICIT_HYPOTHESES` | `WithExt.η-canonical/encoded-β/delivered-zero`；primary02 | 是原生intensional Id片段的条件命题，不证明假设有模型、不证明整个Book/Cubical翻译、不含UA或HIT；不把命题β提升为判断β，也不推出程序不终止。 |
| C-343 | 对本地PrimitivePair及任意C:PrimitivePair→Set、d:Πa,b.C(pack a b)，primitive-elim C d(pack a b)=d a b由refl成立；且∀a,b:Nat，left(pair a b)=a由refl成立。 | `FORMAL_CHECKED_WITH_SCOPE / POSITIVE_CONTROLS` | `primitive-β/projection-β`；primary02，不依赖WithExt参数 | 控制只说明这些具体定义的计算行为。直接投影可以完成取左分量任务，因此NEG02不是该任务不可完成的证明；未证明任何现实相对HoTT失配。 |

## T1 的 H₀：内容恢复与可观察 append-only audit state（2026-09-25）

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-TERRA-T1-H0-001` | `C-344–C-346` | `formal/terra-t1-h0/H0Audit.agda`；本地 `CLAIM.md`；Cubical v0.9 的 Bool／Sigma／List | `verification/runs/20260925-MP-TERRA-T1-H0-001-01/`；Cubical Agda 2.8.0-3d04bac，`--safe --cubical --guardedness`，exit 0 | `FORMAL_CHECKED_WITH_SCOPE / MACHINE_PROVED_LOCAL_UNCOMMITTED` |

| Claim ID | 精确主张 | 状态 | 证据 | 禁止外推 |
|---|---|---|---|---|
| C-344 | 在固定 `Action={forward,backward}`、`apply forward=apply backward=not`、`undo forward=backward` 的 Cubical Bool 模型中，对任意 `c:Bool` 与 `log:List AuditEvent`，`current(step (undo forward) (step forward (c,log))) ≡ c`。 | `FORMAL_CHECKED_WITH_SCOPE` | `H0Audit.contentUndo/undo-law`；run `20260925-MP-TERRA-T1-H0-001-01` | 只证明固定 Bool content action 的**内容投影**恢复；不证明任意 Content/Action/FHIR update 的 inverse，也不证明完整 state 返回初始值。 |
| C-345 | 在同一模型中，对任意 `c,log`，`audit(step (undo forward) (step forward (c,log))) ≡ log ++ [evForward,evBackward]`；每个 event 由对应的同一 `step` 的 `recordEvent` 产生。 | `FORMAL_CHECKED_WITH_SCOPE` | `H0Audit.auditAppend/++-assoc/step`；同 run | 不证明 FHIR server 自动生成 e1/e2，亦不证明 authorization、query、retention、NIST enforcement、HPT merge/replay 或真实 append-only storage。 |
| C-346 | 对具体 `initial=(true,[])` 与 `afterUndo=step backward (step forward initial)`，有 `current afterUndo ≡ current initial` 且 `¬(afterUndo ≡ initial)`。 | `FORMAL_CHECKED_WITH_SCOPE / COMPLETE_STATE_CONTROL` | `H0Audit.initialContentRestored/initialAuditRecordsBoth/fullStateNotReturn`；同 run | 非相等依赖这个具体 Bool/list/event instance；不证明所有非空 audit log、所有 state space 或任何现实操作都不回原点。 |

## T1 的 H₀ interface：同一 update 的 actor/event、授权 query 与 capability 边界（2026-09-25）

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-TERRA-T1-H0-INTERFACE-001` | `C-347–C-350` | `formal/terra-t1-h0-interface/H0AuditInterface.agda`；本地 `CLAIM.md`；Cubical v0.9 的 Bool／Sigma／List | `verification/runs/20260925-MP-TERRA-T1-H0-INTERFACE-001-01/`；Cubical Agda 2.8.0-3d04bac，`--safe --cubical --guardedness`，exit 0 | `FORMAL_CHECKED_WITH_SCOPE / MACHINE_PROVED_LOCAL_UNCOMMITTED` |

| Claim ID | 精确主张 | 状态 | 证据 | 禁止外推 |
|---|---|---|---|---|
| C-347 | 在固定三 actor／两 action／Bool content 的模型中，`forwardPermit` 可居住，`step updater forward initial forwardPermit` 在**同一个 step** 中 append `event updater forward true false`，该 event 的 actor/action 投影分别为 updater/forward。 | `FORMAL_CHECKED_WITH_SCOPE / SAME_PRIMITIVE_ACTION_CONTROL` | `H0AuditInterface.forwardPermit/forwardEventIsInternal/forwardEventCarriesActor/forwardEventCarriesAction`；run `20260925-MP-TERRA-T1-H0-INTERFACE-001-01` | 不证明任意 production update 自动产生 FHIR AuditEvent；固定 `Permit` 只是本模型 capability 数据。 |
| C-348 | `auditor` 的 `CanReadAudit` 见证可居住，且其 `readAudit` 读取 `afterUndo` 时精确得到由 updater 的 forward/backward 两步产生的两个带 actor/action/前后 Bool 内容的 event。 | `FORMAL_CHECKED_WITH_SCOPE / AUTHORIZED_QUERY_INTERFACE_CONTROL` | `H0AuditInterface.auditReaderPermit/authorizedQuery`；同 run | 不证明真实 authentication、authorization policy、FHIR search、audit backend、retention 或 NIST deployment enforcement。 |
| C-349 | 在固定 capability interface 中，`¬ CanUpdate outsider forward (current initial)` 且 `¬ CanReadAudit outsider afterUndo`。 | `FORMAL_CHECKED_WITH_SCOPE / FIXED_INTERFACE_REJECTION` | `H0AuditInterface.outsiderCannotUpdate/outsiderCannotRead`；同 run | 只否定此有限 datatype interface 的 outsider capabilities；不建模管理员、攻击者、权限提升、网络或密码学。 |
| C-350 | 在同一 actor/capability 模型中，`contentRestored : current afterUndo ≡ current initial` 与 `fullStateNotReturn : ¬ (afterUndo ≡ initial)` 同时成立。 | `FORMAL_CHECKED_WITH_SCOPE / CONTENT_VS_COMPLETE_STATE_SEPARATION` | `H0AuditInterface.contentRestored/fullStateNotReturn`；同 run | 不证明所有 content/action/log 都有该性质；不把完整 audit state 的非回返说成现实物理不可逆定律。 |

## T1 的 H₀ generic metadata：任意 supplied audit payload 的结构正控制（2026-09-26）

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-TERRA-T1-H0-GENERIC-001` | `C-351–C-353` | `formal/terra-t1-h0-generic/H0AuditGeneric.agda`；本地 `CLAIM.md`；Cubical v0.9 的 Sigma／List | `verification/runs/20260926-MP-TERRA-T1-H0-GENERIC-001-01/`；Cubical Agda 2.8.0-3d04bac，`--safe --cubical --guardedness`，exit 0 | `FORMAL_CHECKED_WITH_SCOPE / MACHINE_PROVED_LOCAL_UNCOMMITTED` |

| Claim ID | 精确主张 | 状态 | 证据 | 禁止外推 |
|---|---|---|---|---|
| C-351 | 对任意 `Content`、`Actor`、`Action`、`Metadata`、`apply`、`undo` 和显式 `undo-law`，任意 supplied `u,a,m₁,m₂,c,log` 均有 `contentUndo`：二次同一 `step` 后恢复内容投影。 | `FORMAL_CHECKED_WITH_SCOPE / EXPLICIT_UNDO_LAW` | `H0AuditGeneric.contentUndo`；run `20260926-MP-TERRA-T1-H0-GENERIC-001-01` | `undo-law` 是显式前提，不证明任意现实 update 可撤销或任意 action 系统都有 inverse。 |
| C-352 | 对同一参数和任意 supplied `m₁,m₂`，`auditAppend` 证明两个同一 `step` 产生的 event 保留 actor/action/before/after/metadata，逐项 append 在最终 log 中。 | `FORMAL_CHECKED_WITH_SCOPE / GENERIC_METADATA_CARRIED_BY_SAME_STEP` | `H0AuditGeneric.auditAppend/recordEvent/step`；同 run | 不证明实际 FHIR schema/profile、metadata 真值、timestamp、签名、authorization enforcement、retention 或 HPT merge/replay。 |
| C-353 | 对任意 supplied `u,a,m₁,m₂,c`，空初始 log 下 `contentRestoredAtInitial` 与 `fullStateNotReturn` 同时成立。 | `FORMAL_CHECKED_WITH_SCOPE / GENERIC_CONTENT_VS_COMPLETE_STATE_SEPARATION` | `H0AuditGeneric.contentRestoredAtInitial/fullStateNotReturn`；同 run | 非回返使用初始空 log 和至少两次 step 的结构；不证明一般现实不可逆性、所有 deployment 或任何 HoTT 全局结论。 |

## T2 的一次性授权码：bare 可复制接口与 stateful server 正控制（2026-09-26）

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-TERRA-T2-ONESHOT-001` | `C-354–C-356` | `formal/terra-t2-one-shot/OneShotCapability.agda`；本地 `CLAIM.md`；Cubical v0.9 的 Sigma／List | `verification/runs/20260926-MP-TERRA-T2-ONESHOT-001-01/`；Cubical Agda 2.8.0-3d04bac，`--safe --cubical --guardedness`，exit 0 | `FORMAL_CHECKED_WITH_SCOPE / MACHINE_PROVED_LOCAL_UNCOMMITTED` |

| Claim ID | 精确主张 | 状态 | 证据 | 禁止外推 |
|---|---|---|---|---|
| C-354 | 对任意 `A : Type`，`duplicate : A → A × A` 可定义；对固定 `authorizationCode` 有 `duplicate authorizationCode ≡ (authorizationCode , authorizationCode)`。 | `FORMAL_CHECKED_WITH_SCOPE / BARE_VALUE_DUPLICATION_CONTROL` | `OneShotCapability.duplicate/duplicatedCode/duplicateIsTwoCopies`；run `20260926-MP-TERRA-T2-ONESHOT-001-01` | 只说明普通 Cubical 积接口允许一个**数据值**进入两个使用位置；不证明所有现实资源可复制、Book 的所有上下文规则、任何攻击能力或 HoTT 结论。 |
| C-355 | 在固定 pure interface `pureRedeem : Code → Token` 中，`pureTwice authorizationCode ≡ (accessToken , accessToken)`。 | `FORMAL_CHECKED_WITH_SCOPE / BARE_PURE_INTERFACE_NEGATIVE_CONTROL` | `OneShotCapability.pureRedeem/pureTwice/pureCopiesBothGrant`；同 run | 这是故意选择的非状态 pure interface，不能代表 OAuth 或所有 code→token 函数；不从此推出“HoTT 使一次性任务失败”。 |
| C-356 | 对同一 `duplicatedCode` 的两份分量按序调用固定 stateful `redeem`，第一次 reply 为 `granted accessToken`，第二次为 `denied`，最终 server status 是 `consumed`，event log 是 `[grantAttempt,denialAttempt]`。 | `FORMAL_CHECKED_WITH_SCOPE / SAME_CORE_TASK_STATEFUL_POSITIVE_CONTROL` | `OneShotCapability.firstCopyGrants/secondCopyIsDenied/serverHasConsumedCode/bothAttemptsRecorded`；同 run | 只证明顺序、单 code、固定有限 state model；不证明真实 OAuth 的 client/redirect binding、原子并发、PKCE/TLS、安全性、日志持久化、生产部署或所有 HoTT representations。 |

## Cloud-Opus 审计并补完 GLM：GLM 线最终集成、一般 n（KS 5.9/5.10）与 HIT 名称级证书（2026-09-27）

> 授权：用户委托工作单 `GLM-5.3-Flash/审计请求/20260927-委托工作单-审计修正补完交付最终卷宗.md` §6（"`HoTT/CLAIM_EVIDENCE_MATRIX.md`（仅 D2 最终集成行）"）。写入者：Claude Code 云端会话（Cloud-Opus），分支 `claude/charming-pasteur-mvzlio`。
> 工具链：Agda v2.8.0 **Linux x86-64** release 资产 + cubical v0.9（与 `dedekind-omega-missile/TOOLCHAIN.json` 的 cubical 逐字节一致；Agda 为同一 release 的另一平台资产），记录 `formal/cloud-opus-glm-audit/TOOLCHAIN.linux-x86_64.json`。全部运行 `--safe --cubical --guardedness --ignore-interfaces`。
> 索引状态：运行 `index_status = PENDING_CLAIM_EVIDENCE_MATRIX_UPDATE`；`verification/PROOF_VERSION_CLOSURE.json` 属 integrator，未写。目标内索引 `Cloud-Opus审计并补完GLM/证据索引.md`；核验 `Cloud-Opus审计并补完GLM/tools/verify_copus_run.py`（复用 canonical 检查并逐字节重放）。审计报告与卷宗：`Cloud-Opus审计并补完GLM/`。
> GLM 的原运行 `20260926-GLM-*` 保持原样（哈希锁定）；其 schema 非 canonical（见审计报告 R5），此处以 `20260927-COPUS-REPLAY-GLM-*` 为 canonical 副本。
> 编号约定：本节提到 Opus 的主张时一律写带命名空间的 `CG001-C-NN`（Opus CG-001 目标内索引 `.claude/goals/CG-001-targeted-overview/证据索引.md`）；本矩阵其它节里同号的 `C-63`、`C-71`、`C-75` 等是别的证明包的 claim，与本节无关。

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-GLM-RUSSELL-IOTA-001` | `GLM-R1-C02`、`GLM-R1-C03` | `formal/glm-russell/iota-syntax/ArtificialEquationControl.agda`（+ `RealisticIotaSyntax.agda`） | `verification/runs/20260927-COPUS-REPLAY-GLM-IOTA-SYNTAX-01/`；exit 0 | `FORMAL_CHECKED_WITH_SCOPE`（GLM 证明，本会话 canonical 重放） |
| `MP-GLM-RUSSELL-IOTA-NEG-001` | `GLM-R1-C03` 负控制 | `formal/glm-russell/iota-syntax/WrongArtIsRefl.agda` | `verification/runs/20260927-COPUS-REPLAY-GLM-IOTA-SYNTAX-NEG-01/`；exit 42，`art i != boolTy` | `NEGATIVE_CONTROL_REJECTED`（只测 art ≢ refl，不测 C03 论证） |
| `MP-GLM-RUSSELL-IOTA-002` | `GLM-R1-C01` | `formal/glm-russell/iota-syntax/RealisticIotaSyntaxSet.agda` | `verification/runs/20260927-COPUS-REPLAY-GLM-IOTA-SYNTAX-02/`；exit 0 | `FORMAL_CHECKED_WITH_SCOPE` |
| `MP-GLM-RUSSELL-STALL-001` | `GLM-R2-C01`、`GLM-R2-C02` | `formal/glm-russell/universe-ascent-stall/AscentStallAtSets.agda` | `verification/runs/20260927-COPUS-REPLAY-GLM-ASCENT-STALL-01/`；exit 0 | `FORMAL_CHECKED_WITH_SCOPE / HIT_FREE_NAME_LEVEL (COPUS-R1-C02/C03)` |
| `MP-GLM-RUSSELL-GROUPOID-001` | `GLM-R3-C01` | `formal/glm-russell/groupoid-universe/NoHitGroupoidUniverse.agda` | `verification/runs/20260927-COPUS-REPLAY-GLM-GROUPOID-UNIVERSE-01/`；exit 0 | `FORMAL_CHECKED_WITH_SCOPE / HIT_FREE_NAME_LEVEL (COPUS-R1-C01) / KS_N1_FAITHFUL_REPLAY` |
| `MP-GLM-RUSSELL-GROUPOID-NEG-001` | `GLM-R3-C01` 原负控制 | `formal/glm-russell/groupoid-universe/WrongGroupoidWitness.agda` | `verification/runs/20260927-COPUS-REPLAY-GLM-GROUPOID-UNIVERSE-NEG-01/`；exit 42，`[NotInScope] true` | `REJECTED_BEFORE_TYPE_CHECKING / CONTROL_INVALID`（由 `MP-COPUS-GLM-FIX-NEG-001/002` 取代） |
| `MP-COPUS-KS-TOWER-001` | `COPUS-KS-C01`–`COPUS-KS-C05` | `formal/cloud-opus-glm-audit/ks-universe-tower/KSUniverseTower.agda`；本地 `CLAIM.md` | `verification/runs/20260927-COPUS-KS-UNIVERSE-TOWER-01/`；exit 0（72 s） | `MACHINE_PROVED_WITH_SCOPE / HIT_FREE_NAME_LEVEL (COPUS-R1-C05) / KNOWN_THEOREM_REPLAYED (Kraus–Sattler 2015)` |
| `MP-COPUS-KS-TOWER-NEG-001` | `COPUS-KS-C01` 负控制 | `formal/cloud-opus-glm-audit/ks-universe-tower/KSNegTrivialBase.agda` | `verification/runs/20260927-COPUS-KS-UNIVERSE-TOWER-NEG-01/`；exit 42，`false != true` | `NEGATIVE_CONTROL_REJECTED`（平凡基环） |
| `MP-COPUS-KS-TOWER-NEG-002` | `COPUS-KS-C01` 负控制 | `formal/cloud-opus-glm-audit/ks-universe-tower/KSNegOvershoot.agda` | `verification/runs/20260927-COPUS-KS-UNIVERSE-TOWER-NEG-02/`；exit 42 | `NEGATIVE_CONTROL_REJECTED`（证书层级精确，不越级） |
| `MP-COPUS-HITSCAN-001` | `COPUS-R1-C01`–`COPUS-R1-C03` | `formal/cloud-opus-glm-audit/hitscan/CertGLM.agda`（+ `HITScan.agda`） | `verification/runs/20260927-COPUS-HITSCAN-CERT-GLM-01/`；exit 0；stdout 含全部闭包 | `MACHINE_CHECKED_CERTIFICATE_WITH_SCOPE`（名称级，边界见 hitscan/CLAIM.md） |
| `MP-COPUS-HITSCAN-002` | `COPUS-R1-C04`、`COPUS-R6-C01` | `formal/cloud-opus-glm-audit/hitscan/CertOpus.agda` | `verification/runs/20260927-COPUS-HITSCAN-CERT-OPUS-01/`；exit 0 | `MACHINE_CHECKED_CERTIFICATE_WITH_SCOPE` |
| `MP-COPUS-HITSCAN-003` | `COPUS-R1-C05` | `formal/cloud-opus-glm-audit/hitscan/CertKS.agda` | `verification/runs/20260927-COPUS-HITSCAN-CERT-KS-01/`；exit 0 | `MACHINE_CHECKED_CERTIFICATE_WITH_SCOPE` |
| `MP-COPUS-HITSCAN-004` | `COPUS-R1-C06` | `formal/cloud-opus-glm-audit/hitscan/CertC71.agda` | `verification/runs/20260927-COPUS-HITSCAN-CERT-OPUS-02/`；exit 0 | `MACHINE_CHECKED_CERTIFICATE_WITH_SCOPE` |
| `MP-COPUS-HITSCAN-NEG-001` | `COPUS-R1-C01` 扫描器负控制 | `formal/cloud-opus-glm-audit/hitscan/NegCertIota.agda` | `verification/runs/20260927-COPUS-HITSCAN-NEG-01/`；exit 42，点名 `Tm` | `NEGATIVE_CONTROL_REJECTED` |
| `MP-COPUS-HITSCAN-NEG-002` | `COPUS-R6-C01` 扫描器负控制 | `formal/cloud-opus-glm-audit/hitscan/NegCertC75.agda` | `verification/runs/20260927-COPUS-HITSCAN-NEG-02/`；exit 42，点名 `HubAndSpoke, Susp, S¹, EM₁, EM₁-raw` | `NEGATIVE_CONTROL_REJECTED` |
| `MP-COPUS-HITSCAN-NEG-003` | `COPUS-R1-C01` 扫描器负控制 | `formal/cloud-opus-glm-audit/hitscan/NegCertPT.agda` | `verification/runs/20260927-COPUS-HITSCAN-NEG-03/`；exit 42，点名 `∥_∥₁` | `NEGATIVE_CONTROL_REJECTED` |
| `MP-COPUS-GLM-FIX-001` | `COPUS-GLM-FIX-C02a`、`COPUS-GLM-FIX-C02b` | `formal/cloud-opus-glm-audit/glm-repairs/IotaC02Faithful.agda` | `verification/runs/20260927-COPUS-GLM-REPAIR-01/`；exit 0 | `FORMAL_CHECKED_WITH_SCOPE / DECLARATION_PROOF_REPAIR` |
| `MP-COPUS-GLM-FIX-NEG-001` | `GLM-R3-C01` 修复负控制 | `formal/cloud-opus-glm-audit/glm-repairs/GroupoidNegFixed.agda` | `verification/runs/20260927-COPUS-GLM-REPAIR-NEG-01/`；exit 42，`false != true` | `NEGATIVE_CONTROL_REJECTED` |
| `MP-COPUS-GLM-FIX-NEG-002` | `GLM-R3-C01` 近失控制 | `formal/cloud-opus-glm-audit/glm-repairs/GroupoidNegTrivialLoop.agda` | `verification/runs/20260927-COPUS-GLM-REPAIR-NEG-02/`；exit 42，`true != false` | `NEGATIVE_CONTROL_REJECTED` |
| `MP-COPUS-GLM-FIX-NEG-003` | `GLM-R1-C03` 近失控制 | `formal/cloud-opus-glm-audit/glm-repairs/IotaC03NegTrivialInterp.agda` | `verification/runs/20260927-COPUS-GLM-REPAIR-NEG-03/`；exit 42 | `NEGATIVE_CONTROL_REJECTED` |
| `MP-COPUS-Q7-001` | `COPUS-Q7-C01` | `formal/cloud-opus-glm-audit/glm-repairs/Q7AnnotatedReplay.agda` | `verification/runs/20260927-COPUS-GLM-REPAIR-Q7-01/`；exit 0 | `FORMAL_CHECKED_WITH_SCOPE` |

| Claim ID | 精确主张 | 状态 | 证据 | 禁止外推 |
|---|---|---|---|---|
| GLM-R1-C01 | `realisticIotaSyntaxIsASet : isSet Tm`（Tm：Bool 字面量 + cond + 两条 ι 路径构造子的玩具 HIT，Tm ≃ Bool） | `FORMAL_CHECKED_WITH_SCOPE` | run `20260927-COPUS-REPLAY-GLM-IOTA-SYNTAX-02` | 不是"理论自身的表述完全落定"；无替换/上下文/依赖；完整类型论语法未触及 |
| GLM-R1-C02 | 形式上只有 `valReflT/F : Path (Path Bool (val (cond (lit b) t s)) (val _)) refl refl`（端点定义性相等） | `FORMAL_CHECKED_WITH_SCOPE / DECLARATION_PROOF_RUPTURE` | run `20260927-COPUS-REPLAY-GLM-IOTA-SYNTAX-01` | **不**陈述"ι 路径构造子被解释为 refl"；该内容由 COPUS-GLM-FIX-C02a 陈述 |
| GLM-R1-C03 | `¬isSetTmA : ¬ isSet TmA`（加入一条被解释为 `ua not` 的人工等式后） | `FORMAL_CHECKED_WITH_SCOPE` | runs `20260927-COPUS-REPLAY-GLM-IOTA-SYNTAX-01`、`-NEG-01`、`20260927-COPUS-GLM-REPAIR-NEG-03` | 不证明"非落定必须人工注入" |
| GLM-R2-C01 | `universeLoopSpaceAtSetIsSet : ∀ {ℓ} (X : Type ℓ) (pX : isSet X) → isSet (Path (Type ℓ) X X)` | `FORMAL_CHECKED_WITH_SCOPE / HIT_FREE_NAME_LEVEL` | run `20260927-COPUS-REPLAY-GLM-ASCENT-STALL-01`；COPUS-R1-C02 | — |
| GLM-R2-C02 | `noLevel2AscentAtSets : ∀ {ℓ} (X : Type ℓ) (pX : isSet X) → isContr (Path (Path (Type ℓ) X X) refl refl)` | `FORMAL_CHECKED_WITH_SCOPE / HIT_FREE_NAME_LEVEL` | 同上；COPUS-R1-C03 | 不推出"HIT 对上升必要"（宇宙塔无 HIT 也上升：COPUS-KS-C01） |
| GLM-R3-C01 | `¬universeIsGroupoid : ¬ isOfHLevel 3 (Type (ℓ-suc ℓ-zero))` | `FORMAL_CHECKED_WITH_SCOPE / HIT_FREE_NAME_LEVEL / KS_N1_FAITHFUL_REPLAY` | runs `20260927-COPUS-REPLAY-GLM-GROUPOID-UNIVERSE-01`、`20260927-COPUS-GLM-REPAIR-NEG-01/02`、`20260927-COPUS-GLM-REPAIR-Q7-01`；COPUS-R1-C01 | 原负控制 `-NEG-01` 无效（作用域错误） |
| COPUS-KS-C01 | `KS-Theorem-5-9 : (n : ℕ) → ¬ isOfHLevel (2 + n) (Type (lvl n))`，`lvl zero = ℓ-zero`，`lvl (suc n) = ℓ-suc (lvl n)` | `MACHINE_PROVED_WITH_SCOPE / HIT_FREE_NAME_LEVEL` | run `20260927-COPUS-KS-UNIVERSE-TOWER-01`；负控制 `-NEG-01/02`；COPUS-R1-C05 | Kraus–Sattler 2015 的已知定理（重放，非新数学）；不证明任何固定宇宙无层 |
| COPUS-KS-C02 | `workOrderForm : (n : ℕ) → ¬ isOfHLevel (n + 2) (Type (iterSuc n ℓ-zero))`，`iterSuc zero ℓ = ℓ`，`iterSuc (suc n) ℓ = iterSuc n (ℓ-suc ℓ)` | `MACHINE_PROVED_WITH_SCOPE / HIT_FREE_NAME_LEVEL` | 同上 | 同上 |
| COPUS-KS-C03 | `KS-Theorem-5-10-U≤ : (n : ℕ) → isOfHLevel (3 + n) (T (lvl n) n) × ¬ isOfHLevel (2 + n) (T (lvl n) n)`，`T L k = TypeOfHLevel L (2 + k)` | `MACHINE_PROVED_WITH_SCOPE / HIT_FREE_NAME_LEVEL` | 同上 | — |
| COPUS-KS-C04 | `KS-Theorem-5-10-Loop : (n : ℕ) → isOfHLevel (3 + n) (Loop (lvl n) n) × ¬ isOfHLevel (2 + n) (Loop (lvl n) n)` | `MACHINE_PROVED_WITH_SCOPE / HIT_FREE_NAME_LEVEL` | 同上 | — |
| COPUS-KS-C05 | `step : (L : Level) (k : ℕ) → NT L k → NT (ℓ-suc L) (suc k)`（U_L^{≤k} 的非平凡 (k+1)-环 ⇒ U_{L+1}^{≤k+1} 的非平凡 (k+2)-环） | `MACHINE_PROVED_WITH_SCOPE` | 同上 | — |
| COPUS-R1-C01 | `Path (List Name) (hitsOf ¬universeIsGroupoid) []`、`Path Nat (sizeOf ¬universeIsGroupoid) 251` | `MACHINE_CHECKED_CERTIFICATE_WITH_SCOPE` | run `20260927-COPUS-HITSCAN-CERT-GLM-01`；负控制 `20260927-COPUS-HITSCAN-NEG-01/03` | 名称级闭包（反射所见）；不是"可在无 HIT 元理论中证明"的元定理 |
| COPUS-R1-C02 | `hitsOf universeLoopSpaceAtSetIsSet ≡ []`，`sizeOf ≡ 189` | `MACHINE_CHECKED_CERTIFICATE_WITH_SCOPE` | run `20260927-COPUS-HITSCAN-CERT-GLM-01` | 同上 |
| COPUS-R1-C03 | `hitsOf noLevel2AscentAtSets ≡ []`，`sizeOf ≡ 190` | `MACHINE_CHECKED_CERTIFICATE_WITH_SCOPE` | 同上 | 同上 |
| COPUS-R1-C04 | `hitsOf typeIsNotASet ≡ []`（Opus `CG001-C-63`），`sizeOf ≡ 101` | `MACHINE_CHECKED_CERTIFICATE_WITH_SCOPE` | run `20260927-COPUS-HITSCAN-CERT-OPUS-01` | 同上 |
| COPUS-R1-C05 | `hitsOf` 对 `KS-Theorem-5-9`、`workOrderForm`、`KS-Theorem-5-10-U≤`、`KS-Theorem-5-10-Loop` 均为 `[]`（363/364/363/364 名） | `MACHINE_CHECKED_CERTIFICATE_WITH_SCOPE` | run `20260927-COPUS-HITSCAN-CERT-KS-01` | 同上 |
| COPUS-R1-C06 | `hitsOf hSetNotSet ≡ []`（Opus `CG001-C-71`），`sizeOf ≡ 149` | `MACHINE_CHECKED_CERTIFICATE_WITH_SCOPE` | run `20260927-COPUS-HITSCAN-CERT-OPUS-02` | 同上 |
| COPUS-R6-C01 | `hitsOf localGlobal ≡ []`（Opus `CG001-C-75` 包的 local-global 桥），`sizeOf ≡ 201` | `MACHINE_CHECKED_CERTIFICATE_WITH_SCOPE` | run `20260927-COPUS-HITSCAN-CERT-OPUS-01`；负控制 `20260927-COPUS-HITSCAN-NEG-02`（`CG001-C-75` 主定理依赖 HIT） | 同上 |
| COPUS-GLM-FIX-C02a | `valBetaT-refl : (t s : Tm) → cong val (betaT t s) ≡ refl`、`valBetaF-refl`（证明为 refl） | `FORMAL_CHECKED_WITH_SCOPE` | run `20260927-COPUS-GLM-REPAIR-01` | 一阶 ι 玩具片段 |
| COPUS-GLM-FIX-C02b | `glmFormHoldsAtArt : Path (Path Type (f boolTy) (f boolTy)) refl refl` 且 `faithfulFormFailsAtArt : ¬ (cong f art ≡ refl)` | `FORMAL_CHECKED_WITH_SCOPE / RUPTURE_EXHIBIT` | 同上 | 只说明 GLM 原陈述形式不能区分真实与人工等式 |
| COPUS-Q7-C01 | GLM-R3-C01 各中间步骤的显式类型重述（`hlevel3≡isGroupoid`、`a-moves`、`fst-τ`、`τ≠refl-annotated`、`fst-FAM`、`eval-loopE`、`setOfSelfEquivs`、`Q7-theorem`） | `FORMAL_CHECKED_WITH_SCOPE` | run `20260927-COPUS-GLM-REPAIR-Q7-01` | 审计者读法的内核确认；不加新数学 |

### 终局轮追加（2026-09-27）

> 写终局判词（`Cloud-Opus审计并补完GLM/14-罗素面终局判词.md`）之后追加。原为暂存区的一行类型检查，按用户"全部代码入库"的要求入库并按 F-011 捕获。同一授权（委托工作单 §6，D2 最终集成行）。

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-COPUS-KS-TOWER-002` | `COPUS-KS-C06` | `formal/cloud-opus-glm-audit/ks-universe-tower/CatalogOfSetsTwoSteps.agda` | `verification/runs/20260927-COPUS-KS-CATALOG-OF-SETS-01/`；exit 0（73 s） | `MACHINE_PROVED_WITH_SCOPE`（KS 5.10 在 n = 0 的实例；无 HIT 见 COPUS-R1-C05） |
| `MP-COPUS-KS-TOWER-NEG-003` | `COPUS-KS-C06` 负控制 | `formal/cloud-opus-glm-audit/ks-universe-tower/KSNegCatalogOfSetsIsSet.agda` | `verification/runs/20260927-COPUS-KS-CATALOG-OF-SETS-NEG-01/`；exit 42，`[UnequalTerms]` | `NEGATIVE_CONTROL_REJECTED`（3 层读不成 2 层） |

| Claim ID | 精确主张 | 状态 | 证据 | 禁止外推 |
|---|---|---|---|---|
| COPUS-KS-C06 | `catalogOfSetsTwoSteps : isOfHLevel 3 (hSet ℓ-zero) × (¬ isSet (hSet ℓ-zero))` | `MACHINE_PROVED_WITH_SCOPE` | run `20260927-COPUS-KS-CATALOG-OF-SETS-01`；负控制 `-NEG-01` | 只关于装集合的目录 `hSet ℓ-zero`；"追问两步就停"是对两个分量的读法 |

#### Lean 对照 `CG001-C-72` 的 Linux 重放（2026-09-27）

> Opus 的 UIP 世界对照（`CG001-C-72`，原运行在 macOS）。本会话用 Lean 4.34.0 的 Linux release 资产重放；它与 Opus 的工具链同一源码 commit `293d5d0c0c3f3dded4688b3ccd6a33939ac5102b`，`Init.olean`、`Init/Prelude.olean` 两平台逐字节相同。工具链记录 `formal/cloud-opus-glm-audit/LEAN_TOOLCHAIN.linux-x86_64.json`；驱动沿用 CG-001 的 `lean_check.py`，未改动。首次捕获因漏解 `Init.olean.server` 失败，已整体留档于 `Cloud-Opus审计并补完GLM/附件/失败捕获-20260927-Lean缺Init配套文件/`。

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-CG001-UNIVERSE-SET-LEAN-001` | `CG001-C-72` | `formal/claude-cg001/universe-set-lean/UniverseIsSet.lean` | `verification/runs/20260927-COPUS-REPLAY-CG001-UNIVERSE-SET-LEAN-01/`；exit 0；stdout 与原运行逐字节相同 | `KERNEL_ACCEPTED_WITH_SCOPE / CROSS_PLATFORM_BYTE_IDENTICAL_REPLAY`（Lean 4，UIP；不是 HoTT 命题） |
| `MP-CG001-UNIVERSE-SET-LEAN-NEG-001` | `CG001-C-72` 负控制 | `formal/claude-cg001/universe-set-lean/WrongCastFlips.lean` | `verification/runs/20260927-COPUS-REPLAY-CG001-UNIVERSE-SET-LEAN-NEG-01/`；exit 1，拒绝在目标文件第 11 行 | `NEGATIVE_CONTROL_REJECTED`（细化阶段：`cast p true` 不定义性等于 `false`） |

| Claim ID | 精确主张 | 状态 | 证据 | 禁止外推 |
|---|---|---|---|---|
| CG001-C-72 | `theorem universeIsSet {A B : Type} (p q : A = B) : p = q := rfl`；`castIsId`、`noFlip`（均不依赖公理） | `MACHINE_PROVED_WITH_SCOPE`（Opus；本会话 Linux 重放） | runs `20260926-CG001-UNIVERSE-SET-LEAN-01`、`20260927-COPUS-REPLAY-CG001-UNIVERSE-SET-LEAN-01`；负控制 `-NEG-01` 两份 | UIP 类型论中的命题，不是 HoTT 命题；在终局判词中只作粗粒度对照（同时压平了高阶结构） |

#### 芝诺线（Opus 的 A7：无穷相干）的 Linux 重放（2026-09-27）

> 为 `docs/社区审计提交/01-芝诺悖论的幽灵.md` 捕获。Agda v2.8.0 Linux 资产 + cubical v0.9（逐字节一致）；Lean 4.34.0 Linux 资产（与原工具链同一源码 commit）。Opus 的原运行 `20260926-CG001-*` 保持原样。

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-CG001-SST-FINITE-LEVELS-001` | `CG001-C-62` | `formal/claude-cg001/sst-finite-levels/SSTLevels.agda` | `verification/runs/20260927-COPUS-REPLAY-CG001-SST-FINITE-LEVELS-01/`；exit 0 | `KERNEL_ACCEPTED_WITH_SCOPE / CROSS_PLATFORM_REPLAY`（Opus 原证，Linux 重放） |
| `MP-CG001-SST-FINITE-LEVELS-NEG-001` | `CG001-C-62` 负控制 | `formal/claude-cg001/sst-finite-levels/WrongFace.agda` | `verification/runs/20260927-COPUS-REPLAY-CG001-SST-FINITE-LEVELS-NEG-01/`；exit 42，`UnequalTerms` | `NEGATIVE_CONTROL_REJECTED` |
| `MP-CG001-WILD-SST-001` | `CG001-C-64` | `formal/claude-cg001/wild-sst/WildSST.agda` | `verification/runs/20260927-COPUS-REPLAY-CG001-WILD-SST-01/`；exit 0 | `KERNEL_ACCEPTED_WITH_SCOPE / CROSS_PLATFORM_REPLAY`（Opus 原证，Linux 重放） |
| `MP-CG001-WILD-SST-NEG-001` | `CG001-C-64` 负控制 | `formal/claude-cg001/wild-sst/WrongSpinCoherent.agda` | `verification/runs/20260927-COPUS-REPLAY-CG001-WILD-SST-NEG-01/`；exit 42，`UnequalTerms` | `NEGATIVE_CONTROL_REJECTED` |
| `MP-CG001-WILD-SST-LEAN-001` | `CG001-C-65` | `formal/claude-cg001/wild-sst-lean/WildSSTUIP.lean` | `verification/runs/20260927-COPUS-REPLAY-CG001-WILD-SST-LEAN-01/`；exit 0 | `KERNEL_ACCEPTED_WITH_SCOPE / CROSS_PLATFORM_REPLAY`（Opus 原证，Linux 重放） |
| `MP-CG001-WILD-SST-LEAN-NEG-001` | `CG001-C-65` 负控制 | `formal/claude-cg001/wild-sst-lean/WrongRoute.lean` | `verification/runs/20260927-COPUS-REPLAY-CG001-WILD-SST-LEAN-NEG-01/`；exit 1，`ELABORATION_ERROR_IN_TARGET` | `NEGATIVE_CONTROL_REJECTED` |
| `MP-CG001-WILD-SST2-001` | `CG001-C-66` | `formal/claude-cg001/wild-sst/WildSST2.agda` | `verification/runs/20260927-COPUS-REPLAY-CG001-WILD-SST2-01/`；exit 0 | `KERNEL_ACCEPTED_WITH_SCOPE / CROSS_PLATFORM_REPLAY`（Opus 原证，Linux 重放） |
| `MP-CG001-WILD-SST2-NEG-001` | `CG001-C-66` 负控制 | `formal/claude-cg001/wild-sst/WrongSurfTrivial.agda` | `verification/runs/20260927-COPUS-REPLAY-CG001-WILD-SST2-NEG-01/`；exit 42，`UnequalTerms` | `NEGATIVE_CONTROL_REJECTED` |
| `MP-CG001-SELF-INTERPRETATION-001` | `CG001-C-67` | `formal/claude-cg001/self-interpretation/SelfInterpretation.agda` | `verification/runs/20260927-COPUS-REPLAY-CG001-SELF-INTERPRETATION-01/`；exit 0 | `KERNEL_ACCEPTED_WITH_SCOPE / CROSS_PLATFORM_REPLAY`（Opus 原证，Linux 重放） |
| `MP-CG001-SELF-INTERPRETATION-NEG-001` | `CG001-C-67` 负控制 | `formal/claude-cg001/self-interpretation/WrongFlipIsIdentity.agda` | `verification/runs/20260927-COPUS-REPLAY-CG001-SELF-INTERPRETATION-NEG-01/`；exit 42，`UnequalTerms` | `NEGATIVE_CONTROL_REJECTED` |
| `MP-CG001-WILD-SST-P4-001` | `CG001-C-68` | `formal/claude-cg001/wild-sst/WildSSTP4Flat.agda` | `verification/runs/20260927-COPUS-REPLAY-CG001-WILD-SST-P4-01/`；exit 0 | `KERNEL_ACCEPTED_WITH_SCOPE / CROSS_PLATFORM_REPLAY`（Opus 原证，Linux 重放） |
| `MP-CG001-WILD-SST-P4-NEG-001` | `CG001-C-68` 负控制 | `formal/claude-cg001/wild-sst/WrongSurfMoveTrivial.agda` | `verification/runs/20260927-COPUS-REPLAY-CG001-WILD-SST-P4-NEG-01/`；exit 42，`UnequalTerms` | `NEGATIVE_CONTROL_REJECTED` |
| `MP-CG001-WINDING-COCYCLE-001` | `CG001-C-69` | `formal/claude-cg001/wild-sst/WindingCocycle.agda` | `verification/runs/20260927-COPUS-REPLAY-CG001-WINDING-COCYCLE-01/`；exit 0 | `KERNEL_ACCEPTED_WITH_SCOPE / CROSS_PLATFORM_REPLAY`（Opus 原证，Linux 重放） |
| `MP-CG001-WINDING-COCYCLE-NEG-001` | `CG001-C-69` 负控制 | `formal/claude-cg001/wild-sst/WrongSpinWCocycle.agda` | `verification/runs/20260927-COPUS-REPLAY-CG001-WINDING-COCYCLE-NEG-01/`；exit 42，`UnequalTerms` | `NEGATIVE_CONTROL_REJECTED` |
| `MP-CG001-WILD-SST-LEVELS-001` | `CG001-C-70` | `formal/claude-cg001/wild-sst/WildSSTP4Levels.agda` | `verification/runs/20260927-COPUS-REPLAY-CG001-WILD-SST-LEVELS-01/`；exit 0 | `KERNEL_ACCEPTED_WITH_SCOPE / CROSS_PLATFORM_REPLAY`（Opus 原证，Linux 重放） |
| `MP-CG001-WILD-SST-LEVELS-NEG-001` | `CG001-C-70` 负控制 | `formal/claude-cg001/wild-sst/WrongS2Groupoid.agda` | `verification/runs/20260927-COPUS-REPLAY-CG001-WILD-SST-LEVELS-NEG-01/`；exit 42，`UnequalTerms` | `NEGATIVE_CONTROL_REJECTED` |

| Claim ID | 精确主张 | 状态 | 证据 | 禁止外推 |
|---|---|---|---|---|
| CG001-C-62 | `SST≤0 … SST≤5 : Type₁` 与平凡居民（外部生成器逐层打印） | `MACHINE_PROVED_WITH_SCOPE`（Opus；本会话 Linux 重放） | runs `20260926-CG001-SST-FINITE-LEVELS-01`、`20260927-COPUS-REPLAY-CG001-SST-FINITE-LEVELS-01`；负控制两份 | 见 Opus 证据索引对应行的禁止外推；不证明半单纯类型不可定义 |
| CG001-C-64 | `WildSST`、`Coh₂`、`setsCohere`；`spin`：两条路线绕 1 圈与 2 圈，`spinIncoherent : ¬ Coh₂ spin` | `MACHINE_PROVED_WITH_SCOPE`（Opus；本会话 Linux 重放） | runs `20260926-CG001-WILD-SST-01`、`20260927-COPUS-REPLAY-CG001-WILD-SST-01`；负控制两份 | 见 Opus 证据索引对应行的禁止外推；不证明半单纯类型不可定义 |
| CG001-C-65 | Lean 4（UIP）：`theorem coh2 (S : WildSST) : Coh2 S := fun _ _ _ _ _ _ _ => rfl` | `MACHINE_PROVED_WITH_SCOPE`（Opus；本会话 Linux 重放） | runs `20260926-CG001-WILD-SST-LEAN-01`、`20260927-COPUS-REPLAY-CG001-WILD-SST-LEAN-01`；负控制两份 | 见 Opus 证据索引对应行的禁止外推；不证明半单纯类型不可定义 |
| CG001-C-66 | `surf≢refl`；`flat` 上两个不同的六边形填充；`Deg₃` 对一个成立、对另一个不成立 | `MACHINE_PROVED_WITH_SCOPE`（Opus；本会话 Linux 重放） | runs `20260926-CG001-WILD-SST2-01`、`20260927-COPUS-REPLAY-CG001-WILD-SST2-01`；负控制两份 | 见 Opus 证据索引对应行的禁止外推；不证明半单纯类型不可定义 |
| CG001-C-67 | 玩具语法自解释两难：`faithful∞`、`syntax∞IsNotASet`、`noFaithfulForFacts` | `MACHINE_PROVED_WITH_SCOPE`（Opus；本会话 Linux 重放） | runs `20260926-CG001-SELF-INTERPRETATION-01`、`20260927-COPUS-REPLAY-CG001-SELF-INTERPRETATION-01`；负控制两份 | 见 Opus 证据索引对应行的禁止外推；不证明半单纯类型不可定义 |
| CG001-C-68 | 一般第二级相干 `Coh₃`（P₄）：`notCoh₃ : ¬ Coh₃ flatSurfᵢ`、`coh₃Trivial : Coh₃ flatTrivialᵢ` | `MACHINE_PROVED_WITH_SCOPE`（Opus；本会话 Linux 重放） | runs `20260926-CG001-WILD-SST-P4-01`、`20260927-COPUS-REPLAY-CG001-WILD-SST-P4-01`；负控制两份 | 见 Opus 证据索引对应行的禁止外推；不证明半单纯类型不可定义 |
| CG001-C-69 | 圆周值结构上 `Coh₂` ⇔ 绕数上闭链方程；`spinW` 不相干、`uniformW` 相干 | `MACHINE_PROVED_WITH_SCOPE`（Opus；本会话 Linux 重放） | runs `20260926-CG001-WINDING-COCYCLE-01`、`20260927-COPUS-REPLAY-CG001-WINDING-COCYCLE-01`；负控制两份 | 见 Opus 证据索引对应行的禁止外推；不证明半单纯类型不可定义 |
| CG001-C-70 | 集合 ⇒ `Coh₂ᵢ`；群胚 ⇒ `Coh₂ᵢ` 为命题且 `Coh₃` 成立；`flatS¹` 数据唯一 | `MACHINE_PROVED_WITH_SCOPE`（Opus；本会话 Linux 重放） | runs `20260926-CG001-WILD-SST-LEVELS-01`、`20260927-COPUS-REPLAY-CG001-WILD-SST-LEVELS-01`；负控制两份 | 见 Opus 证据索引对应行的禁止外推；不证明半单纯类型不可定义 |

#### 自查轮追加：Lean 对照的补充控制（2026-09-27）

> 用户要求对本会话后来的工作做声明层与证明层的自查。查出 Opus 的 `CG001-C-65` 负控制 `WrongRoute.lean` 注释声称检验"首尾记账、内核拒绝"，实际报错落在一步的参数上、由细化器报出；`CG001-C-72` 负控制的注释也把细化器拒绝写成 "KERNEL_REJECTED"。两个主定理不受影响。补上的控制见 `formal/cloud-opus-glm-audit/lean-controls/CLAIM.md`；原包只增不改的说明 `formal/claude-cg001/wild-sst-lean/REVISIONS.md`、`formal/claude-cg001/universe-set-lean/REVISIONS.md`。工具链记录 `formal/cloud-opus-glm-audit/LEAN_TOOLCHAIN_META.linux-x86_64.json`。

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-COPUS-LEAN-C65-ENDPOINT-NEG-001` | `CG001-C-65` 首尾负控制 | `formal/cloud-opus-glm-audit/lean-controls/WrongRouteEndpoint.lean` | `verification/runs/20260927-COPUS-LEAN-C65-ENDPOINT-NEG-01/`；exit 1，`ELABORATION_ERROR_IN_TARGET` | `NEGATIVE_CONTROL_REJECTED`（细化器在第二、三步的接口处拒绝） |
| `MP-COPUS-LEAN-C65-KERNEL-001` | `COPUS-LEAN-C01` | `formal/cloud-opus-glm-audit/lean-controls/KernelRoute.lean` | `verification/runs/20260927-COPUS-LEAN-C65-KERNEL-01/`；exit 0（含 `leanchecker --fresh`） | `KERNEL_ACCEPTED_WITH_SCOPE`（经 `Lean.addDecl` 由内核接受；Lean 4，UIP） |
| `MP-COPUS-LEAN-C65-KERNEL-NEG-001` | `COPUS-LEAN-C01` 负控制 | `formal/cloud-opus-glm-audit/lean-controls/KernelRouteEndpoint.lean` | `verification/runs/20260927-COPUS-LEAN-C65-KERNEL-NEG-01/`；exit 1，`KERNEL_ERROR_IN_TARGET` | `NEGATIVE_CONTROL_REJECTED`（内核本身：`(kernel) application type mismatch`） |
| `MP-COPUS-LEAN-C72-KERNEL-001` | `COPUS-LEAN-C02` | `formal/cloud-opus-glm-audit/lean-controls/KernelCast.lean` | `verification/runs/20260927-COPUS-LEAN-C72-KERNEL-01/`；exit 0（含 `leanchecker --fresh`） | `KERNEL_ACCEPTED_WITH_SCOPE`（经 `Lean.addDecl` 由内核接受；Lean 4，UIP） |
| `MP-COPUS-LEAN-C72-KERNEL-NEG-001` | `COPUS-LEAN-C02` 负控制 | `formal/cloud-opus-glm-audit/lean-controls/KernelCastFlips.lean` | `verification/runs/20260927-COPUS-LEAN-C72-KERNEL-NEG-01/`；exit 1，`KERNEL_ERROR_IN_TARGET` | `NEGATIVE_CONTROL_REJECTED`（内核本身：`(kernel) declaration type mismatch`） |

| Claim ID | 精确主张 | 状态 | 证据 | 禁止外推 |
|---|---|---|---|---|
| COPUS-LEAN-C01 | `kernelRouteA`：陈述取自 `routeA`、证明项为显式首尾的 `Eq.trans stepOne (Eq.trans stepTwo stepThree)`，经 `Lean.addDecl` 交给内核而被接受；`kernelRouteA_states_routeA : @kernelRouteA = @routeA := rfl`；均不依赖公理 | `MACHINE_PROVED_WITH_SCOPE` | run `20260927-COPUS-LEAN-C65-KERNEL-01`；负控制 `20260927-COPUS-LEAN-C65-KERNEL-NEG-01`、`20260927-COPUS-LEAN-C65-ENDPOINT-NEG-01` | UIP 类型论中的命题；不给 `CG001-C-65` 增加新数学；负控制不证明 Lean 内核一般可靠 |
| COPUS-LEAN-C02 | `kernelCastIsId : ∀ (p : Bool = Bool), cast p true = true`（证明项 `fun p => Eq.refl true`，经 `Lean.addDecl` 交给内核）被接受；`kernelCastIsId_states_castIsId : @kernelCastIsId = fun p => castIsId p true := rfl` | `MACHINE_PROVED_WITH_SCOPE` | run `20260927-COPUS-LEAN-C72-KERNEL-01`；负控制 `20260927-COPUS-LEAN-C72-KERNEL-NEG-01` | UIP 类型论中的命题，不是 HoTT 命题 |

## Claude CG-001 线：罗素线与 UR 的机器证据（追问程序、邻近对照、截断对照；2026-09-30）

> 授权：研究发起人 2026-09-30 在本机 Claude Code 会话中说“把所有该做的，全部做完，我认为我们要阶段性地收尾HoTT悖论查找工作了，因为我们很可能已经找到了。”写入者：Claude Code 本机会话 `eadb3381`（macOS，分支 main）。本节只追加，不改动其它各节。
> 工具链：Agda 2.8.0 + cubical 0.9，`--safe --cubical --guardedness`；macOS 记录 `formal/dedekind-omega-missile/TOOLCHAIN.json`，Linux 记录 `formal/cloud-opus-glm-audit/TOOLCHAIN.linux-x86_64.json`（C-77 至 C-80 的原运行）；Lean 4.34.0（C-80：Linux 记录 `formal/cloud-opus-glm-audit/LEAN_TOOLCHAIN.linux-x86_64.json`，macOS 记录 `formal/claude-cg001/pedometer-ablation-lean/LEAN_TOOLCHAIN.json`）。
> 索引状态：各运行的 `index_status` 保持捕获时的值（`PENDING_CLAIM_EVIDENCE_MATRIX_UPDATE`），`verification/PROOF_VERSION_CLOSURE.json` 属 integrator，本节未写；canonical 的 register→mark→freeze 待 integrator。目标内索引与精确重放：`.claude/goals/CG-001-targeted-overview/证据索引.md` §18–§23，核验 `.claude/goals/CG-001-targeted-overview/tools/verify_cg001_run.py --rerun`（复用 canonical 检查，只把矩阵索引检查换成目标内索引）。
> 编号约定：同上节，Opus 线的主张一律写带命名空间的 `CG001-C-NN`；`CG001-C-72` 已登记在上一节（Cloud-Opus 的 Linux 重放），本节不重复。本矩阵其它节里同号的 `C-71`、`C-75` 等是别的证明包的 claim，与本节无关。
> 读法：这批命题支撑两份社区审计稿（`docs/社区审计提交/02-罗素悖论的幽灵.md` 与 `03-HoTT的芝诺.md`）。研究发起人的判定与 UR 定义是判定，不是定理；本节不宣称 HoTT 不一致。

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-CG001-HSET-UNIVERSE-001` | `CG001-C-71` | `formal/claude-cg001/hset-universe/HSetNotSet.agda` | `verification/runs/20260926-CG001-HSET-UNIVERSE-01/`；exit 0，stderr 0 B；目标内精确重放一致 | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEX_ONLY`（待登记） |
| `MP-CG001-HSET-UNIVERSE-NEG-001` | `CG001-C-71`（负控制） | `formal/claude-cg001/hset-universe/WrongFlipSetTrivial.agda` | `verification/runs/20260926-CG001-HSET-UNIVERSE-NEG-01/`；exit 42，`false != true of type Bool` | `NEGATIVE_CONTROL_REJECTED` |
| `MP-CG001-TOTALITY-ESCALATION-001` | `CG001-C-73` | `formal/claude-cg001/totality-escalation/TotalityEscalates.agda` | `verification/runs/20260926-CG001-TOTALITY-ESCALATION-01/`；exit 0，stderr 0 B；目标内精确重放一致 | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEX_ONLY`（精确上升只证 n = 0、1，一般 n 为来源 Kraus–Sattler 2015，见同包 `REVISIONS.md`；上界为库定理） |
| `MP-CG001-TOTALITY-ESCALATION-NEG-001` | `CG001-C-73`（负控制） | `formal/claude-cg001/totality-escalation/WrongRotateTrivial.agda` | `verification/runs/20260926-CG001-TOTALITY-ESCALATION-NEG-01/`；exit 42，`1 != 0 of type Nat` | `NEGATIVE_CONTROL_REJECTED` |
| `MP-CG001-COPIES-OF-BOOL-001` | `CG001-C-74` | `formal/claude-cg001/totality-escalation/CopiesOfBool.agda`（命题全文 `CLAIM-C74.md`） | `verification/runs/20260926-CG001-COPIES-OF-BOOL-01/`；exit 0，stderr 0 B；目标内精确重放一致 | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEX_ONLY`（只涉及 Bool） |
| `MP-CG001-COPIES-OF-BOOL-NEG-001` | `CG001-C-74`（负控制） | `formal/claude-cg001/totality-escalation/WrongSwapStays.agda` | `verification/runs/20260926-CG001-COPIES-OF-BOOL-NEG-01/`；exit 42，`false != true of type Bool` | `NEGATIVE_CONTROL_REJECTED` |
| `MP-CG001-UNIVERSE-QUESTIONING-001` | `CG001-C-75`、`CG001-C-76` | `formal/claude-cg001/universe-questioning/UniverseHasNoLevel.agda`（命题全文 `CLAIM.md`，范围修订 `REVISIONS.md`） | `verification/runs/20260926-CG001-UNIVERSE-QUESTIONING-01/`；exit 0，stderr 0 B；目标内精确重放一致（2026-09-30 补登入本草稿） | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEX_ONLY`（主定理经 Eilenberg–MacLane 空间用了高阶归纳类型，名称级证书见证据索引 §19 补注） |
| `MP-CG001-UNIVERSE-QUESTIONING-NEG-001` | `CG001-C-75`（负控制） | `formal/claude-cg001/universe-questioning/WrongSectionReadsZero.agda` | `verification/runs/20260926-CG001-UNIVERSE-QUESTIONING-NEG-01/`；exit 42，`1 != 0` | `NEGATIVE_CONTROL_REJECTED` |
| `MP-CG001-QUESTIONING-DELAY-001` | `CG001-C-77`、`CG001-C-78`、`CG001-C-79` | `formal/claude-cg001/questioning-delay/QuestioningDelay.agda`（命题全文 `CLAIM.md`；导入 `pedometer-semantics` 与 `universe-questioning`） | `verification/runs/20260930-CG001-QUESTIONING-DELAY-01/`（Linux 工具链记录 `formal/cloud-opus-glm-audit/TOOLCHAIN.linux-x86_64.json`）；exit 0，stderr 0 B；目标内精确重放一致；macOS 跨平台重放 `verification/runs/20260930-CG001-QUESTIONING-DELAY-MACOS-01/`，归一化 stdout 与 Linux 逐行一致 | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEX_ONLY`（罗素线 S6 的内部定理：对任意判定器，宇宙上的追问程序等于 never；读到现实执行仍需一致性，对任意判定器另需典范性） |
| `MP-CG001-QUESTIONING-DELAY-NEG-001` | `CG001-C-78`（负控制） | `formal/claude-cg001/questioning-delay/WrongUniverseAnswersEarly.agda` | `verification/runs/20260930-CG001-QUESTIONING-DELAY-NEG-01/`；exit 42，`nothing != just 1`；macOS 跨平台重放 `verification/runs/20260930-CG001-QUESTIONING-DELAY-MACOS-NEG-01/`，归一化 stdout 与 Linux 逐行一致 | `NEGATIVE_CONTROL_REJECTED` |
| `MP-CG001-QUESTIONING-DELAY-NEG-002` | `CG001-C-79`（负控制） | `formal/claude-cg001/questioning-delay/WrongNaturalsSilent.agda` | `verification/runs/20260930-CG001-QUESTIONING-DELAY-NEG-02/`；exit 42，`just 1 != nothing`；macOS 跨平台重放 `verification/runs/20260930-CG001-QUESTIONING-DELAY-MACOS-NEG-02/`，归一化 stdout 与 Linux 逐行一致 | `NEGATIVE_CONTROL_REJECTED` |
| `MP-CG001-QUESTIONING-DELAY-NEG-003` | `CG001-C-79`（负控制） | `formal/claude-cg001/questioning-delay/WrongSetsStopAtOne.agda` | `verification/runs/20260930-CG001-QUESTIONING-DELAY-NEG-03/`；exit 42，`nothing != just 1`；macOS 跨平台重放 `verification/runs/20260930-CG001-QUESTIONING-DELAY-MACOS-NEG-03/`，归一化 stdout 与 Linux 逐行一致 | `NEGATIVE_CONTROL_REJECTED` |
| `MP-CG001-QUESTIONING-DELAY-NEG-004` | `CG001-C-78`（负控制） | `formal/claude-cg001/questioning-delay/WrongNeverByRefl.agda` | `verification/runs/20260930-CG001-QUESTIONING-DELAY-NEG-04/`；exit 42，`askFrom Type judgeU 1 != never`；macOS 跨平台重放 `verification/runs/20260930-CG001-QUESTIONING-DELAY-MACOS-NEG-04/`，归一化 stdout 与 Linux 逐行一致 | `NEGATIVE_CONTROL_REJECTED` |
| `MP-CG001-QUESTIONING-DELAY-LEAN-001` | `CG001-C-80` | `formal/claude-cg001/questioning-delay-lean/QuestioningLean.lean`（**Lean 4.34.0**，Linux 记录 `formal/cloud-opus-glm-audit/LEAN_TOOLCHAIN.linux-x86_64.json`） | `verification/runs/20260930-CG001-QUESTIONING-DELAY-LEAN-01/`；exit 0，九条定理零公理，`leanchecker --fresh` 通过；目标内精确重放一致；macOS 跨平台重放 `verification/runs/20260930-CG001-QUESTIONING-DELAY-LEAN-MACOS-01/`，归一化 stdout 与 Linux 逐行一致 | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEX_ONLY`（Lean 行，事实世界中同一过程第 1 问停） |
| `MP-CG001-QUESTIONING-DELAY-LEAN-NEG-001` | `CG001-C-80`（负控制） | `formal/claude-cg001/questioning-delay-lean/WrongLeanUniverseSilent.lean` | `verification/runs/20260930-CG001-QUESTIONING-DELAY-LEAN-NEG-01/`；exit 1，`Not a definitional equality`（细化器拒绝）；macOS 跨平台重放 `verification/runs/20260930-CG001-QUESTIONING-DELAY-LEAN-MACOS-NEG-01/`，归一化 stdout 与 Linux 逐行一致 | `NEGATIVE_CONTROL_REJECTED` |
| `MP-CG001-PRODUCT-QUESTIONING-001` | `CG001-C-81`、`CG001-C-82` | `formal/claude-cg001/product-questioning/ProductQuestioning.agda`（命题全文 `CLAIM.md`；导入 `questioning-delay`、`pedometer-semantics`、`universe-questioning`） | `verification/runs/20260930-CG001-PRODUCT-QUESTIONING-01/`（**macOS** 工具链记录 `formal/dedekind-omega-missile/TOOLCHAIN.json`）；exit 0，stderr 0 B；目标内精确重放一致 | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEX_ONLY`（C-78 的邻近对照：HoTT Book 例 8.8.6 的非宇宙乘积上，追问程序对任意判定器等于 never；同一乘积成员高度有上限时恰好第 2+b 问停；只在 macOS 捕获与重放） |
| `MP-CG001-PRODUCT-QUESTIONING-NEG-001` | `CG001-C-81`（负控制） | `formal/claude-cg001/product-questioning/WrongProductAnswersEarly.agda` | `verification/runs/20260930-CG001-PRODUCT-QUESTIONING-NEG-01/`；exit 42，`nothing != just 1` | `NEGATIVE_CONTROL_REJECTED` |
| `MP-CG001-PRODUCT-QUESTIONING-NEG-002` | `CG001-C-81`（负控制） | `formal/claude-cg001/product-questioning/WrongProductNeverByRefl.agda` | `verification/runs/20260930-CG001-PRODUCT-QUESTIONING-NEG-02/`；exit 42，`askFrom Prod judgeProd 1 != never` | `NEGATIVE_CONTROL_REJECTED` |
| `MP-CG001-PRODUCT-QUESTIONING-NEG-003` | `CG001-C-82`（负控制） | `formal/claude-cg001/product-questioning/WrongBoundedSilent.agda` | `verification/runs/20260930-CG001-PRODUCT-QUESTIONING-NEG-03/`；exit 42，`just 2 != nothing` | `NEGATIVE_CONTROL_REJECTED` |
| `MP-CG001-PRODUCT-QUESTIONING-NEG-004` | `CG001-C-82`（负控制） | `formal/claude-cg001/product-questioning/WrongBoundedStopsEarly.agda` | `verification/runs/20260930-CG001-PRODUCT-QUESTIONING-NEG-04/`；exit 42，`nothing != just 1` | `NEGATIVE_CONTROL_REJECTED` |
| `MP-CG001-TRUNCATION-QUESTIONING-001` | `CG001-C-83` | `formal/claude-cg001/truncation-questioning/TruncationQuestioning.agda`（命题全文 `CLAIM.md`；导入 `product-questioning`、`questioning-delay`、`pedometer-semantics`，经其导入 `universe-questioning`） | `verification/runs/20260930-CG001-TRUNCATION-QUESTIONING-01/`（**macOS** 工具链记录 `formal/dedekind-omega-missile/TOOLCHAIN.json`）；exit 0，stderr 0 B；目标内精确重放一致 | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEX_ONLY`（教科书消解的对照：对任意类型与判定器，追问程序在集合截断上第 1 问停，与 C-78、C-81 的 `never` 并列；代价：截断把宇宙里不同的自我认同合一，且不能解码回宇宙；只在 macOS 捕获与重放） |
| `MP-CG001-TRUNCATION-QUESTIONING-NEG-001` | `CG001-C-83`（负控制） | `formal/claude-cg001/truncation-questioning/WrongTruncSilent.agda` | `verification/runs/20260930-CG001-TRUNCATION-QUESTIONING-NEG-01/`；exit 42，`just 1 != nothing` | `NEGATIVE_CONTROL_REJECTED` |
| `MP-CG001-TRUNCATION-QUESTIONING-NEG-002` | `CG001-C-83`（负控制） | `formal/claude-cg001/truncation-questioning/WrongNotEqTrivial.agda` | `verification/runs/20260930-CG001-TRUNCATION-QUESTIONING-NEG-02/`；exit 42，`false != true` | `NEGATIVE_CONTROL_REJECTED` |
| `MP-ZFC-HOTT-OBSERVATION-BRIDGE-001` | `C-357` | `formal/claude-cg001/observation-completion-bridge/ObservationCompletionBridge.agda`（命题全文 `CLAIM.md`；复用C-78/C-83的固定Cubical Agda依赖） | `verification/runs/20261003-CG001-ZFC-HOTT-OBSERVATION-BRIDGE-02/`；macOS Agda 2.8.0 + cubical 0.9；exit 0，stderr 0 B；由统一捕获器记录全部本地导入根和12个固定源码文件 | `KERNEL_ACCEPTED_WITH_SCOPE`：原universe Q为`never`、截断Q第一步停、且无统一section三项的联合控制；不构成ZFC模型／验收定理。 |
| `MP-ZFC-HOTT-OBSERVATION-BRIDGE-NEG-001` | `C-357`（负控制） | `formal/claude-cg001/observation-completion-bridge/WrongObservationCompletionBridge.agda` | `verification/runs/20261003-CG001-ZFC-HOTT-OBSERVATION-BRIDGE-NEG-02/`；exit 42，`Bool != A` | `NEGATIVE_CONTROL_REJECTED`：同层常值Bool不能承担每个原universe元素的统一恢复。 |
| `MP-ZFC-HOTT-COMPLETION-REFLECTION-001` | `C-358` | `formal/claude-cg001/completion-reflection-failure/CompletionReflectionFailure.agda`（命题全文 `CLAIM.md`；复用固定C-78/C-83过程） | `verification/runs/20261003-CG001-ZFC-HOTT-COMPLETION-REFLECTION-04/`；macOS Agda 2.8.0 + cubical 0.9；exit 0，stderr 0 B；统一捕获器固定6个本地导入根和11个源码文件 | `KERNEL_ACCEPTED_WITH_SCOPE`：截断Q在第一步完成，不能推出原universe Q存在有限halt witness；不构成ZFC模型／验收定理。 |
| `MP-ZFC-HOTT-COMPLETION-REFLECTION-NEG-001` | `C-358`（负控制） | `formal/claude-cg001/completion-reflection-failure/WrongCompletionReflection.agda` | `verification/runs/20261003-CG001-ZFC-HOTT-COMPLETION-REFLECTION-NEG-03/`；exit 42，`nothing != just 1` | `NEGATIVE_CONTROL_REJECTED`：伪造的原Q fuel-0 halt不由截断完成推出。 |

| Claim ID | 精确主张 | 状态 | 证据 | 禁止外推 |
|---|---|---|---|---|
| CG001-C-71 | `flipSet` 的第一分量为 `ua notEquiv`，`ua notEquiv ≢ refl`；`hSetNotSet : ¬ isSet (hSet ℓ-zero)` | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEXED` | run `20260926-CG001-HSET-UNIVERSE-01`、`-NEG-01` | 只陈述集合宇宙这一层；不证明更高层 |
| CG001-C-73 | n 层落定者的总体在 n+1 层落定（库定理）；集合的总体不是集合、群胚的总体不是群胚（n = 0、1 精确）；集合总体的截断不能解码回去 | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEXED` | run `20260926-CG001-TOTALITY-ESCALATION-01`、`-NEG-01` | 一般 n 由 CG001-C-76 与 Kraus–Sattler 重放（上节）给出，不在本行 |
| CG001-C-74 | 所有与 Bool 相同的类型的收集：按相同计数恰好一个，收集本身不是集合 | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEXED` | run `20260926-CG001-COPIES-OF-BOOL-01`、`-NEG-01` | 有限实例；不涉及大小问题 |
| CG001-C-75 | 局部—整体环路原理；对 `K n = EM ℤ (1+n)` 有非平凡截面；`universeHasNoLevel : (m : ℕ) → ¬ isOfHLevel m (Type ℓ-zero)` | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEXED` | run `20260926-CG001-UNIVERSE-QUESTIONING-01`、`-NEG-01` | 用了高阶归纳类型（名称级证书见上节 COPUS-R6-C01）；不证明没有高阶归纳类型时同样成立 |
| CG001-C-76 | 对一切 k，(1+k) 层落定者的总体不在 1+k 层落定（`gatheringNeverSettled`），配合库的上界恰好高一层；第 0 层的总体可缩 | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEXED` | run `20260926-CG001-UNIVERSE-QUESTIONING-01` | CG001-C-73 一般 n 的机器证明；不陈述单个宇宙 |
| CG001-C-77 | 追问过程 Q 写成 C-55 的 Delay 程序并带判定器 `Judge C = (k : ℕ) → Dec (isOfHLevel (suc k) C)`：燃料方程只取决于事实；返回值可靠；停机当且仅当有某个有限层；`Q ≡ never` 当且仅当一层都没有；精确停机时刻（`exactHalt`、`silentUpTo`） | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEXED` | runs `20260930-CG001-QUESTIONING-DELAY-01`（Linux）、`-MACOS-01`（macOS） | `≡ never` 只经有限燃料的运行来读；读成现实执行需要理论一致性与对闭判定器的典范性 |
| CG001-C-78 | `universeQuestioningIsNever : (judge : Judge (Type ℓ-zero)) → question (Type ℓ-zero) judge ≡ never`；判定器存在且唯一；`kernelRuns1000`（`refl`）；问“有没有一层落定”的程序燃料 0 答否 | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEXED` | runs `20260930-CG001-QUESTIONING-DELAY-01`、`-MACOS-01`；负控制 `-NEG-01`、`-NEG-04` 及其 `-MACOS-` 重放 | 不证明 HoTT 不一致；经 CG001-C-75 用了高阶归纳类型 |
| CG001-C-79 | 同一程序：ℕ、Bool 第 1 问停；h-层 1+n 的类型的目录（`Gathering n`）恰好第 1+n 问停，更少燃料得 `nothing`；各有判定器 | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEXED` | runs `20260930-CG001-QUESTIONING-DELAY-01`、`-MACOS-01`；负控制 `-NEG-02`、`-NEG-03` 及其 `-MACOS-` 重放 | “第 k 问”指问数与燃料，不是时间 |
| CG001-C-80 | Lean 4（UIP）：同一组燃料方程写成有限燃料运行；对任意判定器，宇宙 `Type` 第 1 问停并返回 1；九条定理零公理 | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEXED` | runs `20260930-CG001-QUESTIONING-DELAY-LEAN-01`（Linux）、`-LEAN-MACOS-01`（macOS）；负控制 `-LEAN-NEG-01`、`-LEAN-MACOS-NEG-01` | 集合层命题（Lean 相等有 UIP）；与 Agda 定义是按同一组方程的转写，不是跨系统的同一对象 |
| CG001-C-81 | `productHasNoLevel : (m : ℕ) → ¬ isOfHLevel m Prod`（`Prod = (n : ℕ) → K n`，HoTT Book 例 8.8.6）；对任意判定器 `question Prod judge ≡ never`；判定器存在且唯一；`productKernelRuns1000`（`refl`）；问“有没有一层”燃料 0 答否 | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEXED` | run `20260930-CG001-PRODUCT-QUESTIONING-01`；负控制 `-NEG-01`、`-NEG-02` | 书中已知例子，不主张原创；只在 macOS 上捕获与重放；宇宙只作类型族的值域 |
| CG001-C-82 | `Bounded b = (n : ℕ) → K b` 在 h-层 3+b 落定、2+b 不落定；对任意判定器 `runFor (suc b) (question (Bounded b) judge) ≡ just (suc (suc b))`，更少燃料得 `nothing` | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEXED` | run `20260930-CG001-PRODUCT-QUESTIONING-01`；负控制 `-NEG-03`、`-NEG-04` | 负控制只跑 b = 0；只在 macOS 上捕获与重放 |
| CG001-C-83 | 对任意类型与判定器，追问程序在集合截断 `∥ X ∥₂` 上燃料 0 返回 1；截断宇宙的判定器存在且唯一（`refl` 实跑）；与宇宙、乘积本身的 `never` 并列；`notEqNotRefl`、`truncCollapses : cong ∣_∣₂ notEq ≡ refl`、`noDecoding` | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEXED` | run `20260930-CG001-TRUNCATION-QUESTIONING-01`；负控制 `-NEG-01`、`-NEG-02` | 不说截断错了；不裁定对截断发问与对宇宙发问是不是同一任务；只在 macOS 上捕获与重放 |
| C-357 | 固定原universe的逐层Q满足`question (Type ℓ-zero) judgeU ≡ never`；其集合截断`TU`上的同一Q满足`runFor 0 (question TU judgeTU) ≡ just 1`；并且不存在统一`g : TU → Type ℓ-zero`使所有`A`满足`g ∣A∣₂ ≡ A`。三项由`coarseCompletionCreatesNoRestoration`同一Cubical Agda命题联结。 | `KERNEL_ACCEPTED_WITH_SCOPE` | `MP-ZFC-HOTT-OBSERVATION-BRIDGE-001` / `20261003-CG001-ZFC-HOTT-OBSERVATION-BRIDGE-02`；负控制 `MP-ZFC-HOTT-OBSERVATION-BRIDGE-NEG-001` / `-NEG-02` | 证明固定HoTT Q上的粗完成观察与无统一恢复控制；不形式化ZFC、单纯集模型、模型验收或AcceptanceContract，不说截断错误，也不证明ZFC时间观察力不完备、HoTT不一致或UR现实判词。 |
| C-358 | 定义`CompletionReflectsOriginalHalting = (runFor 0 (question TU judgeTU) ≡ just 1) → Questioning.Halts (Type ℓ-zero) judgeU`。`coarseCompletionDoesNotReflectOriginalHalting`证明其否定：截断版阶段一完成不能推出原Q有有限halt witness。 | `KERNEL_ACCEPTED_WITH_SCOPE` | `MP-ZFC-HOTT-COMPLETION-REFLECTION-001` / `20261003-CG001-ZFC-HOTT-COMPLETION-REFLECTION-04`；负控制 `MP-ZFC-HOTT-COMPLETION-REFLECTION-NEG-001` / `-NEG-03` | 证明固定HoTT Q上的完成反射失败；不裁定两个问题是否同一任务，不形式化ZFC／模型／AcceptanceContract，也不证明ZFC时间观察力不完备、HoTT不一致或UR现实判词。 |

## ZFC 实际 Q、数学幻觉 P、A/B 与 ZFC-1 的第一轮形式化（2026-10-04）

> 用户原文：`sources/prompts/Codex-ZFC-Q-P-A-B-ZFC1-用户原文-20261004.md`。此节机器检查三条相互分层的命题：Lean 中用户 A/P/B/ZFC-1 推理的条件政策 consequence；Cubical Agda 中固定 HoTT Q 对具体 coarse-completion P 的反例；Mathlib 中一个严格 finite-stage P control 与闭连续时间端点正控制。它们不共同构成 bare ZFC 的形式矛盾，也不证明历史来源已经填入全部实际 Q 前提。

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-ZFC-ACTUAL-Q-POLICY-001` | `C-359` | `formal/zfc-actual-q-policy/ZFC1IllusionPolicy.lean` | `verification/runs/20261004-MP-ZFC-ACTUAL-Q-POLICY-001-07/`；Lean 4.34.1 core；pinned core binary、exit 0、stderr 0 B、10条打印定理无公理 | `KERNEL_ACCEPTED_WITH_SCOPE`：若同一完整 Q 将 Zeno-side P 许可运输到 HoTT，且 HoTT-side B 给出 formal completion 与非-origin completion，则显式 `ZFCOneUse` policy model 导出 `False`；B 同时成为`QObservesPromotionFailure`并反驳模型记录的`QMissing`。Q gap本身不推出P，`ZFC+A ↔ ZFC+P`另需 `A↔P`。 |
| `MP-ZFC-ACTUAL-Q-POLICY-NEG-001` | `C-359`（负控制） | `formal/zfc-actual-q-policy/WrongQGapForcesP.lean` | `verification/runs/20261004-MP-ZFC-ACTUAL-Q-POLICY-NEG-06/`；exit 1，`gap : qGap`不能作为任意`P`的证明 | `NEGATIVE_CONTROL_REJECTED`：缺失Q不自动推出P；source/policy premise必须显式提供。此前`-03`止于import布局错误，保留为setup failure而不作控制证据。 |
| `MP-ZFC-ACTUAL-Q-HOTT-COUNTEREXAMPLE-001` | `C-360` | `formal/zfc-actual-q-policy/HoTTCounterexample.agda` | `verification/runs/20261004-MP-ZFC-ACTUAL-Q-HOTT-COUNTEREXAMPLE-001-07/`；Cubical Agda 2.8.0 + cubical 0.9；exit 0、stderr 0 B、全部8个实际本地模块与外部依赖 manifest | `KERNEL_ACCEPTED_WITH_SCOPE`：固定截断Q的stage-one completion与原universe Q无有限halt witness一起，否定具体`MathematicalIllusionP = coarse completion → original finite halting`。 |
| `MP-ZFC-ACTUAL-Q-HOTT-COUNTEREXAMPLE-NEG-001` | `C-360`（负控制） | `formal/zfc-actual-q-policy/WrongHoTTCounterexample.agda` | `verification/runs/20261004-MP-ZFC-ACTUAL-Q-HOTT-COUNTEREXAMPLE-NEG-04/`；exit 42，`nothing != just 1` | `NEGATIVE_CONTROL_REJECTED`：伪造original universe halt不由coarse completion推出；同样固定8个实际本地模块。 |
| `MP-ZFC-ACTUAL-Q-ZENO-LIMIT-CONTROL-001` | `C-361` | `formal/zfc-actual-q-policy/ZenoLimitControl.lean` | `verification/runs/20261004-MP-ZFC-ACTUAL-Q-ZENO-LIMIT-CONTROL-001-08/`；Lean 4.34.0 + pinned Mathlib；exit 0、stderr 0 B；`propext`、`Classical.choice`、`Quot.sound`明示 | `KERNEL_ACCEPTED_WITH_SCOPE / DECLARED_CLASSICAL_AXIOMS`：固定几何数列的FormalA不蕴含严格有限阶段Done，且闭连续时间有端点到达；不将严格Done归给Standard Solution。 |
| `MP-ZFC-ACTUAL-Q-SOURCE-CONTRACT-001` | `C-362` | `formal/zfc-actual-q-policy/ZenoSourceCompletionContract.lean` | `verification/runs/20261004-MP-ZFC-ACTUAL-Q-SOURCE-CONTRACT-001-01/`；Lean 4.34.1 core；pinned core binary；exit 0、stderr 0 B、6条打印定理无公理 | `KERNEL_ACCEPTED_WITH_SCOPE / SOURCE_CERTIFIED_PREMISES`：固定 Norton/IEP 来源卡所分类的 revised completion（每个编号动作完成、无最后动作要求）不提供 strict original completion bridge；来源分类本身不由Lean证明。 |
| `MP-ZFC-ACTUAL-Q-SOURCE-CONTRACT-NEG-001` | `C-362`（负控制） | `formal/zfc-actual-q-policy/WrongZenoLastAction.lean` | `verification/runs/20261004-MP-ZFC-ACTUAL-Q-SOURCE-CONTRACT-NEG-001/`；exit 1，`0 ≤ action`不能作为`action ≤ 0` | `NEGATIVE_CONTROL_REJECTED`：不得伪造最大的自然动作编号来支付严格完成。 |
| `MP-ZFC-ACTUAL-Q-HOTT-CONTRACT-001` | `C-363` | `formal/zfc-actual-q-policy/HoTTCompletionContract.agda` | `verification/runs/20261004-MP-ZFC-ACTUAL-Q-HOTT-CONTRACT-001-01/`；Cubical Agda 2.8.0 + cubical 0.9；exit 0、stderr 0 B、完整本地依赖 manifest | `KERNEL_ACCEPTED_WITH_SCOPE`：固定 HoTT B 被封装为 generic completion gap：有 revised witness、无 original finite-halt witness、无 bridge。 |
| `MP-ZFC-ACTUAL-Q-HOTT-CONTRACT-NEG-001` | `C-363`（负控制） | `formal/zfc-actual-q-policy/WrongHoTTCompletionBridge.agda` | `verification/runs/20261004-MP-ZFC-ACTUAL-Q-HOTT-CONTRACT-NEG-001/`；exit 42，`nothing != just 1` | `NEGATIVE_CONTROL_REJECTED`：generic bridge 不能掩盖固定 HoTT 原过程未完成。 |
| `MP-BARE-ZFC-Q-PRECISION-001` | `C-364` | `formal/bare-zfc-q-precision/BareZFCPrecision.lean`（精确范围见目录`CLAIM.md`） | `verification/runs/20261004-MP-BARE-ZFC-Q-PRECISION-001-03/`；Lean 4.34.1 core；pinned core binary、exit 0、stderr 0 B、10条打印定理无公理；negative control `...NEG-004` 在 `False ↔ True` 处拒绝，`...NEG-001`保留为 output-stream setup failure | `KERNEL_ACCEPTED_WITH_SCOPE / SOURCE_BOUND_APPLICATION_VIEW`：固定两 completion-contract worlds 在同一 coarse standard-resolution view 下的 OriginDone 不能被该 view 决定，且该 view 不支付 universal FormalDone→OriginDone bridge；rich contract view 与有限 process code 是正控制。 |

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-ZFC-H0-TRACE-001` | `C-365` | `formal/zfc-h0-final-closure/H0TraceObservation.agda` | `verification/runs/20261004-MP-ZFC-H0-TRACE-001-07/`；Cubical Agda 2.8.0-3d04bac + cubical v0.9、`--ignore-interfaces`、exit 0、stderr 0 B；negative control `...TRACE-NEG-001-07` 在 `nothing != just 1` 处拒绝 | `KERNEL_ACCEPTED_WITH_SCOPE / H0_OPERATIONAL_FRAGMENT_TRACE_MACHINE_PROVED`：fixed `Delay ℕ/runFor` 的 H0 输出进入 h-set finite trace，universe question 对每一 Judge 的 trace 均为 all-`nothing`；不构成 full H0Map。 |
| `MP-ZFC-H0-PROCESS-REPRESENTATION-001` | `C-366` | `formal/zfc-h0-final-closure/H0ProcessRepresentation.lean` | `verification/runs/20261004-MP-ZFC-H0-PROCESS-REPRESENTATION-001-05/`；冻结 `Foundation@f3972f4204fc` 的 Lean 4.34.0 Zermelo-model interface，exit 0；五个声明均列出 `propext`、`Classical.choice`、`Quot.sound`；negative control `...NEG-001-05` 在同一 stage 的 `value ≠ value` 义务处拒绝 | `KERNEL_ACCEPTED_WITH_SCOPE / ZFC_PROCESS_REPRESENTABILITY_POSITIVE_CONTROL_MACHINE_PROVED_WITH_SCOPE`：外部形式化的 Zermelo model 可表示 ordinal-indexed sequence graph、唯一 stage value、`Seq`/`lh` 定义性；不支付 completion bridge 或任何 bare-ZFC acceptance policy。 |
| `MP-T-PRECISION-TOBS-001` | `C-367` | `formal/t-precision-observation/ObservationPrecision.lean` | `verification/runs/20261004-MP-T-PRECISION-TOBS-001-06/`；Lean 4.34.1 core，exit 0，五个 selected theorem 的 axiom report 均无公理；negative control `MP-T-PRECISION-TOBS-NEG-001` / `20261004-MP-T-PRECISION-TOBS-NEG-001-02/` 在 `False ↔ True` 义务处拒绝 | `KERNEL_ACCEPTED_WITH_SCOPE / ABSTRACT_OBSERVATION_BOUNDARY_MACHINE_PROVED_WITH_SCOPE`：碰撞的 chosen observation 不能决定 chosen predicate；identity/rich observation 是正控制。 |
| `MP-T-PRECISION-TDIAG-001` | `C-368` | `formal/t-precision-diagonal/AcceptanceDiagonal.lean` | `verification/runs/20261004-MP-T-PRECISION-TDIAG-001-02/`；Lean 4.34.1 core，exit 0，五个 selected theorem 的 axiom report 均无公理；negative control `MP-T-PRECISION-TDIAG-NEG-001` / `20261004-MP-T-PRECISION-TDIAG-NEG-001-01/` 在伪造 bridge 的 `accepted : True` 与目标 `originDone : False` 类型不匹配处拒绝 | `KERNEL_ACCEPTED_WITH_SCOPE / CONDITIONAL_SELF_CODE_ACCEPTANCE_BRIDGE_BOUNDARY`：显式 self-code、diagonal completion contract 与 paid `Accept → OriginDone` bridge 联合迫使该 code 不被接受；bridge-missing control 表明 self-coding 与 diagonal contract 本身不制造矛盾。 |

| Claim ID | 精确主张 | 状态 | 证据 | 禁止外推 |
|---|---|---|---|---|
| C-359 | `zfc1_q_missing_with_same_Q_P_and_B_is_inconsistent`与`zfc1_same_Q_P_with_B_is_inconsistent`：在显式`ZFCOneUse`中，若`SameFullQ`、Q gap对Zeno的P许可与`B = formalDone_hott ∧ ¬originDone_hott`都成立，则 B 既见证`QObservesPromotionFailure`又导出`False`；另有`q_gap_does_not_logically_force_P`、`zfc_plus_A_iff_zfc_plus_P`、evidence-status/revised/different-Q controls。 | `KERNEL_ACCEPTED_WITH_SCOPE` | `MP-ZFC-ACTUAL-Q-POLICY-001` / `20261004-MP-ZFC-ACTUAL-Q-POLICY-001-07`；负控制 `MP-ZFC-ACTUAL-Q-POLICY-NEG-001` / `-NEG-06` | 不形式化bare ZFC、IEP、数学共同体、实际同Q映射或物理芝诺完成；这是来源前提明确的政策 use-model consequence。 |
| C-360 | `hottCounterexampleToMathematicalIllusionP : ¬ ((runFor 0 (question TU judgeTU) ≡ just 1) → Questioning.Halts (Type ℓ-zero) judgeU)`，并给出coarse completion与original halt failure的独立分量。 | `KERNEL_ACCEPTED_WITH_SCOPE` | `MP-ZFC-ACTUAL-Q-HOTT-COUNTEREXAMPLE-001` / `20261004-MP-ZFC-ACTUAL-Q-HOTT-COUNTEREXAMPLE-001-07`；负控制 `...NEG-001` / `-NEG-04` | 固定Cubical Agda Q的P反例；不裁定截断与原问题同一性，不将其作为ZFC模型／验收事实。 |
| C-361 | `FormalA = Tendsto s_n (𝓝 1)`且`¬(FormalA → ∃n, s_n=1)`，其中`s_n=1-(1/2)^n`；另有闭连续时间端点到达正控制。 | `KERNEL_ACCEPTED_WITH_SCOPE / DECLARED_CLASSICAL_AXIOMS` | `MP-ZFC-ACTUAL-Q-ZENO-LIMIT-CONTROL-001` / `20261004-MP-ZFC-ACTUAL-Q-ZENO-LIMIT-CONTROL-001-08` | 不证明Standard Solution要求有限阶段、不证明连续运动无端点、不证明ZFC矛盾或实际同Q。 |
| C-362 | `norton_modeled_contract_diverges`：`RevisedAllActionsCompletion`成立、`StrictLastActionCompletion`不成立、`bridgePaid=False`且判词为`revisedResolved`；因此不存在`RevisedDone → OriginalDone`。 | `KERNEL_ACCEPTED_WITH_SCOPE / SOURCE_CERTIFIED_PREMISES` | `MP-ZFC-ACTUAL-Q-SOURCE-CONTRACT-001` / `20261004-MP-ZFC-ACTUAL-Q-SOURCE-CONTRACT-001-01`；负控制 `...NEG-001` | 不证明 Norton／IEP 历史文字、所有标准解法或 ZFC 政策；只形式化来源卡指定合同的逻辑后果。 |
| C-363 | `hottCompletionGap`：固定 Cubical Agda Q 具有 `RevisedDone` witness、`¬ OriginalDone`和`¬(RevisedDone → OriginalDone)`。 | `KERNEL_ACCEPTED_WITH_SCOPE` | `MP-ZFC-ACTUAL-Q-HOTT-CONTRACT-001` / `20261004-MP-ZFC-ACTUAL-Q-HOTT-CONTRACT-001-01`；负控制 `...NEG-001` | 证明共享 completion-gap schema；不证明SameFullQ、跨kernel同一性、来源政策或 ZFC 矛盾。 |
| C-364 | 在固定的有限 source-contract control 中，`standardResolutionView` 对 `OriginDone` 不存在仅依其输出的 decoder，且不存在全域 `FormalDone → OriginDone` completion bridge；显式 rich completion view 与 finite process code 都可决定 `OriginDone`。 | `KERNEL_ACCEPTED_WITH_SCOPE / SOURCE_BOUND_APPLICATION_VIEW` | `MP-BARE-ZFC-Q-PRECISION-001` / `20261004-MP-BARE-ZFC-Q-PRECISION-001-03`；来源绑定见 `audit/20261004-BARE-ZFC-Q-PRECISION-P0-P3-来源接口与完成合同.md`；negative control `...NEG-004` | 只证明该 fixed application-interface control 的观察精度边界；不形式化 bare ZFC、ZFC 模型、ZFC 一致性、不可能的 set encoding、所有标准解法、实际同Q或现实完成。 |
| C-365 | `Trace = ℕ → Maybe ℕ` 为 h-set；`trace d n = runFor n d` 保持 Delay path；对任意 H0 Judge，`trace (question (Type ℓ-zero) judge) = λ _ → nothing`，故每个 finite fuel 都不等于任意 `just answer`。 | `KERNEL_ACCEPTED_WITH_SCOPE / H0_OPERATIONAL_FRAGMENT_TRACE_MACHINE_PROVED` | `MP-ZFC-H0-TRACE-001` / `20261004-MP-ZFC-H0-TRACE-001-07`；负控制 `MP-ZFC-H0-TRACE-NEG-001` / `20261004-MP-ZFC-H0-TRACE-NEG-001-07` | exact native `Delay ℕ`／finite observation fragment；不构造 CCHM/ZFC full model，不支付 H0Map、C_accept、AdequacyLift、SameFullQ、P/Q 或 bare ZFC 归因。 |
| C-366 | 对任意 frozen Foundation Zermelo-model interface 的 `Seq trace`，`domain trace` 为 ordinal；每个 `stage ∈ lh trace` 有唯一 graph value，规范 `nth` 属于 graph；`Seq` 与 `lh` 都有一阶集合论 definability instance。 | `KERNEL_ACCEPTED_WITH_SCOPE / ZFC_PROCESS_REPRESENTABILITY_POSITIVE_CONTROL_MACHINE_PROVED_WITH_SCOPE` | `MP-ZFC-H0-PROCESS-REPRESENTATION-001` / `20261004-MP-ZFC-H0-PROCESS-REPRESENTATION-001-05`；negative control `MP-ZFC-H0-PROCESS-REPRESENTATION-NEG-001` / `20261004-MP-ZFC-H0-PROCESS-REPRESENTATION-NEG-001-05` | 只是在冻结外部 source 的 Zermelo model interface 中证明过程图可表示；不构造 model、不证明 bare ZFC object-language theorem、ZFC consistency、H0Map、C_accept、AdequacyLift、SameFullQ 或 bare-ZFC Q 归因。 |
| C-367 | 对任意 World、View、project 与 observe，若存在 x,y 使 project x = project y、observe x 且 ¬ observe y，则不存在通过 project 全域决定 observe 的 Prop-valued decoder；identity observation 是一般正控制，TinyWorld 的 coarse-to-one-view 是有限具体控制。 | `KERNEL_ACCEPTED_WITH_SCOPE / ABSTRACT_OBSERVATION_BOUNDARY_MACHINE_PROVED_WITH_SCOPE` | `MP-T-PRECISION-TOBS-001` / `20261004-MP-T-PRECISION-TOBS-001-06`；negative control `MP-T-PRECISION-TOBS-NEG-001` / `20261004-MP-T-PRECISION-TOBS-NEG-001-02`；来源背景见 T0 source denominator | 只证明指定函数／命题接口的因子化边界；不证明所有理论、bare ZFC、HoTT、现实过程、时间维度缺失、哥德尔对角化或理论抽象必然导致悖论。 |
| C-368 | 对任意 `Code` 与显式 `step,d,Accept,OriginDone`，若 `step d = d`、`OriginDone (step d) ↔ ¬ Accept d`，且 paid bridge `Accept d → OriginDone (step d)` 成立，则 `¬ Accept d`。另有 bridge-missing 与 bridge-paid controls，分离 self-coding、diagonal contract 与 bridge。 | `KERNEL_ACCEPTED_WITH_SCOPE / CONDITIONAL_SELF_CODE_ACCEPTANCE_BRIDGE_BOUNDARY` | `MP-T-PRECISION-TDIAG-001` / `20261004-MP-T-PRECISION-TDIAG-001-02`；negative control `MP-T-PRECISION-TDIAG-NEG-001` / `20261004-MP-T-PRECISION-TDIAG-NEG-001-01`；来源边界见 `audit/20261005-T-PRECISION-TDIAG-001-SOURCE-DENOMINATOR.md` | 不构造 actual Gödelization，不证明 set.mm/bare ZFC 满足前提，不把 proof acceptance 等同芝诺／圆环／H0 完成，不推出 ZFC 不一致或想法 T 已得证。 |

## GODEL-Q：`set.mm` Appendix-C 变量扩张的 M 层源绑定控制（2026-10-05）

> 该追加节只冻结 actual raw `set.mm@160ebb…` 的有限 vocabulary 与 Appendix-C
> variable-extension 子义务。它不声称实际数据库已经在 ZF 内构造成 `mFS` object；这个差别是本研究
> 当前最重要的 G2 boundary。

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-GODEL-Q-SETMM-APPENDIX-C-VAR-EXTENSION-001` | `C-369` | `formal/godel-q-reflection/SetMMAppendixCVarExtension.lean`（machine-managed vocabulary input：`SetMMAppendixCGenerated.lean`） | `verification/runs/20261005-MP-GODEL-Q-SETMM-APPENDIX-C-VAR-EXTENSION-004/`；Lean 4.34.1 core，stable runner 使生成器对 exact raw `set.mm@160ebb…` 的重生逐字匹配并能独立 replay，exit 0，五条 selected theorem 均无公理；negative control `MP-GODEL-Q-SETMM-APPENDIX-C-VAR-EXTENSION-NEG-001` / `...-NEG-005/` 在 `rawEmbedding v000 = fresh wff 0` 处拒绝 | `KERNEL_ACCEPTED_WITH_SCOPE / M_LEVEL_SOURCE_BOUND_VOCABULARY_EXTENSION`：actual `$v/$f` vocabulary 可单射嵌入对每种 source type 都含可数无限 fresh family 的扩张；这是 `mFS` infinite-variable requirement 的一个 M-level precondition control。 |

| Claim ID | 精确主张 | 状态 | 证据 | 禁止外推 |
|---|---|---|---|---|
| C-369 | 对由 exact raw `set.mm@160ebb…` 的 `$v/$f` declarations 生成的 355 个 `RawVar`，`rawEmbedding` 保持 source type 且为单射；对每个 source `RawType`，`freshFamily : Nat → ExtendedVar` 为单射并始终落在该 type；任意 raw variable 与 fresh variable 可区分。因此该有限 source vocabulary 有一个显式、按 type 的可数无限 fresh extension。 | `KERNEL_ACCEPTED_WITH_SCOPE / M_LEVEL_SOURCE_BOUND_VOCABULARY_EXTENSION` | `MP-GODEL-Q-SETMM-APPENDIX-C-VAR-EXTENSION-001` / `20261005-MP-GODEL-Q-SETMM-APPENDIX-C-VAR-EXTENSION-004`；negative control `...-NEG-005`；精确 scope 见 `formal/godel-q-reflection/SetMMAppendixCVarExtension-CLAIM.md` | 不构造 raw database 的 frame→`mAx` map、ZF 内 `T ∈ mFS` witness、proof trace→`mPPSt/mThm` adequacy、`Prv`、diag、completion bridge或任何 bare-ZFC／现实过程结论。 |

## `ZFC+Q_norm` 的规范性过程完成审计（2026-10-05）

> 这个 package 机器检查研究发起人明确加入的过程完成审计规范：将模型的
> `FormalDone` 说成原任务已经完成前，必须支付 `FormalDone → OriginDone` bridge；
> 明确改题只能得到 revised verdict。它不是 bare ZFC 的对象语言形式化，也不声称
> 既有数学共同体已经采纳这一规范。

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-ZFC-NORMATIVE-PROCESS-AUDIT-001` | `C-370..C-374` | `formal/zfc-normative-process-audit/ProcessCompletionAudit.lean` | `verification/runs/20261005-MP-ZFC-NORMATIVE-PROCESS-AUDIT-001-03/`；Lean 4.34.1 core，固定源码／toolchain／source cards及Lean binary digest，exit 0，十二条 selected theorem 的 axiom report 均无公理 | `KERNEL_ACCEPTED_WITH_SCOPE / NORMATIVE_FORMAL_SPECIFICATION`：对显式 `CompletionContract`，paid bridge 才能给出 original resolution；explicit task switch 只能给 revised resolution；missing bridge 必须给 bridge-required，并且后二者都不能静默成为 original resolution。 |

| Claim ID | 精确主张 | 状态 | 证据 | 禁止外推 |
|---|---|---|---|---|
| C-370 | 对任意明确的 `CompletionContract`，若 `audit contract formal = originalResolved`，则 `contract.originDone`；该结论只经 `.paid (formalDone → originDone)` 分支取得。 | `KERNEL_ACCEPTED_WITH_SCOPE / NORMATIVE_FORMAL_SPECIFICATION` | `MP-ZFC-NORMATIVE-PROCESS-AUDIT-001` / `20261005-MP-ZFC-NORMATIVE-PROCESS-AUDIT-001-03` | 不证明 bare ZFC 已包含此 audit，不证明任何历史模型实际已有 bridge。 |
| C-371 | 对任意 contract，明确 `explicitTaskSwitch` 时 `audit = revisedResolved` 且 `audit ≠ originalResolved`；冻结的 Norton strict/revised control 满足这一判词。 | `KERNEL_ACCEPTED_WITH_SCOPE / NORMATIVE_FORMAL_SPECIFICATION / SOURCE_BOUND_CONTROL` | `MP-ZFC-NORMATIVE-PROCESS-AUDIT-001` / `20261005-MP-ZFC-NORMATIVE-PROCESS-AUDIT-001-03` | Norton 分类是 source-card input，不由 Lean 证明其历史文本，也不推广到所有 Standard Solution。 |
| C-372 | 对任意 contract，bridge 为 `missing` 时 `audit = bridgeRequired` 且 `audit ≠ originalResolved`。 | `KERNEL_ACCEPTED_WITH_SCOPE / NORMATIVE_FORMAL_SPECIFICATION` | `MP-ZFC-NORMATIVE-PROCESS-AUDIT-001` / `20261005-MP-ZFC-NORMATIVE-PROCESS-AUDIT-001-03` | 不推出任意实际理论缺少 bridge，也不把“没有发现”当作 source absence。 |
| C-373 | paid positive control 同时得到 `originalResolved` 与 `originDone`。 | `KERNEL_ACCEPTED_WITH_SCOPE / NORMATIVE_FORMAL_SPECIFICATION / POSITIVE_CONTROL` | `MP-ZFC-NORMATIVE-PROCESS-AUDIT-001` / `20261005-MP-ZFC-NORMATIVE-PROCESS-AUDIT-001-03` | 控制只证明规范不会一概拒绝模型、极限或连续统；不支付现实应用 bridge。 |
| C-374 | missing-bridge negative control 有 `formalDone`，却得到 `bridgeRequired` 且不等于 `originalResolved`。 | `KERNEL_ACCEPTED_WITH_SCOPE / NORMATIVE_FORMAL_SPECIFICATION / NEGATIVE_CONTROL` | `MP-ZFC-NORMATIVE-PROCESS-AUDIT-001` / `20261005-MP-ZFC-NORMATIVE-PROCESS-AUDIT-001-03` | 只否定此规范中的 silent promotion；不构成 bare ZFC、HoTT 或数学共同体矛盾。 |

## ZFC MSS 中 time primitive 消去的定义域恢复／无定义域控制（2026-10-05）

> 来源：Sant'Anna--Bueno 2014；source snapshot、原页范围和翻译边界见
> `audit/20261005-ZFC-META-SUBTHEORY-ADEQUACY-C0R8-DOMAIN-ELIMINATION-SOURCE-TO-SPEC-CONTROL.md`。
> 该包把来源所明说的 domain-bearing ZFC MSS 与 domainless N-MSS 非完全等价作为
> representation-control 动机；它不重放 MSS、Padoa 或 N 的完整理论，也不对 bare ZFC 作结论。

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-ZFC-MSS-DOMAIN-TIME-CONTROL-001` | `C-375`、`C-376` | `formal/zfc-mss-domain-time-control/MSSDomainTimeControl.lean` | `verification/runs/20261005-MP-ZFC-MSS-DOMAIN-TIME-CONTROL-001-04/`；Lean 4.34.1 core；7份固定 source/document inputs、pinned Lean binary、exit 0、stderr 0 B；7条 selected theorem 的 axiom report 均无公理 | `KERNEL_ACCEPTED_WITH_SCOPE / SOURCE_MOTIVATED_REPRESENTATION_CONTROL`：graph/domain view 可恢复固定 endpoint membership；function-only view 在一对固定实例上不能决定该 observation。 |

| Claim ID | 精确主张 | 状态 | 证据 | 禁止外推 |
|---|---|---|---|---|
| C-375 | 对任意 `GraphTrace`，若 `∀t, (∃x, graph t x) ↔ time t`，则对于每个 endpoint，`graphOnly` 有一个仅由 graph domain 构造的 decoder，恰好决定 `EndpointAvailable trace endpoint`。 | `KERNEL_ACCEPTED_WITH_SCOPE / SOURCE_MOTIVATED_POSITIVE_CONTROL` | `MP-ZFC-MSS-DOMAIN-TIME-CONTROL-001` / `20261005-MP-ZFC-MSS-DOMAIN-TIME-CONTROL-001-04`；命题全文：`formal/zfc-mss-domain-time-control/CLAIM.md` | 不形式化 ZFC/MSS/Padoa/Theorem 8；不证明实际物理完成、所有时间观察或 bare-ZFC adequacy。 |
| C-376 | 在固定 `shortCandidate.time={0}` 与 `longCandidate.time={0,1}`、二者有同一 `sharedFunction` 的两实例中，不存在只由 `FunctionView` 决定 `endpoint=1` membership 的全域 decoder。 | `KERNEL_ACCEPTED_WITH_SCOPE / SOURCE_MOTIVATED_NEGATIVE_CONTROL` | `MP-ZFC-MSS-DOMAIN-TIME-CONTROL-001` / `20261005-MP-ZFC-MSS-DOMAIN-TIME-CONTROL-001-04`；命题全文：`formal/zfc-mss-domain-time-control/CLAIM.md` | 不证明这些实例是 N/N-MSS 模型、N 有物理错误、endpoint 是完整 OriginDone，或 ZFC/HoTT/数学共同体矛盾。 |

## MSS phase-space 状态范围与参数顺序控制（2026-10-05）

> 来源：da Costa--Sant'Anna 2001 `gr-qc/0102107v2` 把 prediction/future/time 与
> phase-space state description并列；精确 source-to-spec 边界见
> `audit/20261005-ZFC-META-SUBTHEORY-ADEQUACY-C0R8-MSS-PHASE-ORDER-SOURCE-TO-SPEC-CONTROL.md`。
> 包只检查一个有限 range projection，不将 source 的 phase-space curve 自动等同于该 projection。

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-ZFC-MSS-PHASE-ORDER-CONTROL-001` | `C-377`、`C-378` | `formal/zfc-mss-phase-order-control/MSSPhaseOrderControl.lean` | `verification/runs/20261005-MP-ZFC-MSS-PHASE-ORDER-CONTROL-002/`；Lean 4.34.1 core；7份固定 source/document inputs、pinned Lean binary、exit 0、stderr 0 B；6条 selected theorem 的 axiom report 均无公理 | `KERNEL_ACCEPTED_WITH_SCOPE / SOURCE_MOTIVATED_PARAMETER_ORDER_CONTROL`：参数化 trace 保留固定 start/end order observation；visited-state range在一对 forward/reverse controls 上不能决定它。 |

| Claim ID | 精确主张 | 状态 | 证据 | 禁止外推 |
|---|---|---|---|---|
| C-377 | 对 `TemporalTrace := Bool → Bool` 与 `OrderedForward`，identity `temporalView` 存在 decoder，故决定该 order-sensitive observation。 | `KERNEL_ACCEPTED_WITH_SCOPE / SOURCE_MOTIVATED_POSITIVE_CONTROL` | `MP-ZFC-MSS-PHASE-ORDER-CONTROL-001` / `20261005-MP-ZFC-MSS-PHASE-ORDER-CONTROL-002`；命题全文：`formal/zfc-mss-phase-order-control/CLAIM.md` | 不形式化实际 phase space、MSS、预测、物理时序或完整 OriginDone。 |
| C-378 | 对固定 `forwardTrace` 与 `reverseTrace`，两者 `rangeView` 相同而 `OrderedForward` 真假不同；因此不存在只由该 `RangeView` 决定 `OrderedForward` 的全域 decoder。 | `KERNEL_ACCEPTED_WITH_SCOPE / SOURCE_MOTIVATED_NEGATIVE_CONTROL` | `MP-ZFC-MSS-PHASE-ORDER-CONTROL-001` / `20261005-MP-ZFC-MSS-PHASE-ORDER-CONTROL-002`；命题全文：`formal/zfc-mss-phase-order-control/CLAIM.md` | 不把 source 的 curve等同 rangeView，不证明任何实际物理失败、bare ZFC缺陷、Zeno/圆环问题或HoTT同Q。 |

## Claude CG-005、CG-006 线：哥德尔式 Q——过程完成的观察力及其不完备，落在真实的 𝗭𝗙𝗖 上（2026-10-07 至 10-08）

> 授权：研究发起人 2026-10-07【原话】“审计、综合、融合8个git worktree的工作成果，最终完成哥德尔启发性的‘完全的形式化与机器证明’。”以及“这个repo全部的分支和git worktree，现在由你全面接手了，你就是‘最后的AI’，所以你认为应该做的，都可以做，我全面授权你。”“你要综合所有之前的AI的所有工作，推进到完全的形式化和机器证明的完成。”写入者：Claude Code 本机会话 `d58e0c0d`（Opus 5.5，macOS），经 worktree `.claude/worktrees/cg006-dev` 写 `dev`。本节只追加，不改动其它各节。
> 工具链：Lean 4.34.0（固定路径调用，`sandbox-exec` 禁网）+ 本项目 Mathlib `5ed29652…`（Astra 缓存）；CG-006 另加 FormalizedFormalLogic/Foundation `1fb01b72`（本机禁网编译）。记录：`formal/claude-cg001/godel-q/LEAN_TOOLCHAIN.json`、`MATHLIB_CLOSURE.json`（1,692 个模块的编译产物哈希）；`formal/claude-cg001/godel-q-zfc/LEAN_TOOLCHAIN.json`、`MATHLIB_CLOSURE.json`（1,889 个模块，聚合 `21197b0b…29c7`）。
> 索引状态：九个运行都经 `verify_cg001_run.py --rerun` 精确重放（CG-001 `verification/20261007-CG001-GODEL-Q-*.json`、`20261008-CG001-GODEL-Q-ZFC-*.json`）；`verification/PROOF_VERSION_CLOSURE.json` 本节未写。目标内索引：`.claude/goals/CG-001-targeted-overview/证据索引.md` §24、§25。
> 编号约定：Claude 线的命题一律写带命名空间的 `CG001-C-NN`。共享编号在各分支之间的命名空间见 `HoTT/CLAIM_NAMESPACE_LEDGER.md`。
> 读法：不推出 `ZFC ⊢ ⊥`。CG-005 的 ZFC 读法以其 `CLAIM.md` §3 的标准元定理与 Con(ZFC) 为条件；CG-006 把其中的 R、Σ1C、Δ0C 做成了 Foundation 中真实 𝗭𝗙𝗖 上的定理，Con 与 Σ1 可靠是 Lean 元层定理（`Universe` 模型），不是 𝗭𝗙𝗖 内部可证；哥德尔第二不完备定理对 𝗭𝗙𝗖 本身没有形式化（godel-q-zfc `CLAIM.md` §3、§8）。“时间维度 = 过程的逐步运行”是按研究发起人框架（KC-000010、KC-000024）所作的解释桥。

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-CG001-GODEL-Q-001` | `CG001-C-84`–`CG001-C-94` | `formal/claude-cg001/godel-q/GodelQ/`：`ProcessObservation`、`EffectiveTheory`、`GodelZenoRunner`、`ProvabilityLogic`、`OmegaQuestion`、`Qualification`（按序编译；命题全文 `CLAIM.md`） | `verification/runs/20261007-CG001-GODEL-Q-01/`；exit 0，stderr 0 B；公理只有 propext、Classical.choice、Quot.sound（C-92 无公理）；精确重放一致 | `KERNEL_ACCEPTED_WITH_SCOPE / GOAL_LOCAL_INDEXED` |
| `MP-CG001-GODEL-Q-NEG-SOUNDNESS-001` | `CG001-C-85`（负控制） | `formal/claude-cg001/godel-q/GodelQ/Negative/WrongEscapeWithoutSoundness.lean` | `verification/runs/20261007-CG001-GODEL-Q-NEG-SOUNDNESS-01/`；exit 1，`sound` 字段的目标 `¬ Done e` 无法关闭 | `NEGATIVE_CONTROL_REJECTED` |
| `MP-CG001-GODEL-Q-NEG-CONSISTENCY-001` | `CG001-C-90`（负控制） | `formal/claude-cg001/godel-q/GodelQ/Negative/WrongTheoryWithoutConsistency.lean` | `verification/runs/20261007-CG001-GODEL-Q-NEG-CONSISTENCY-01/`；exit 1，`consistent` 字段的目标 `False` 无法关闭 | `NEGATIVE_CONTROL_REJECTED` |
| `MP-CG001-GODEL-Q-NEG-EFFECTIVENESS-001` | `CG001-C-90`（负控制） | `formal/claude-cg001/godel-q/GodelQ/Negative/WrongBargainWithoutEffectiveness.lean` | `verification/runs/20261007-CG001-GODEL-Q-NEG-EFFECTIVENESS-01/`；exit 1，`re_never` 无法关闭 | `NEGATIVE_CONTROL_REJECTED` |
| `MP-CG001-GODEL-Q-NEG-GODEL-II-001` | `CG001-C-92`（负控制） | `formal/claude-cg001/godel-q/GodelQ/Negative/WrongConsistencyProvable.lean` | `verification/runs/20261007-CG001-GODEL-Q-NEG-GODEL-II-01/`；exit 1，目标化简为 `False` | `NEGATIVE_CONTROL_REJECTED` |
| `MP-CG001-GODEL-Q-ZFC-001` | `CG001-C-95`–`CG001-C-102` | `formal/claude-cg001/godel-q-zfc/GodelQ/`：CG-005 的三个模块（逐字节复制）、`FoundationArith.lean`、`ZFC/` 下 14 个模块与 `ZFC/Qualification.lean`（按序编译；命题全文 `CLAIM.md`） | `verification/runs/20261008-CG001-GODEL-Q-ZFC-01/`；exit 0，stderr 0 B，约 41 秒；85 条公理报告全为三条标准公理；精确重放一致 | `KERNEL_ACCEPTED_WITH_SCOPE / GOAL_LOCAL_INDEXED` |
| `MP-CG001-GODEL-Q-ZFC-NEG-SOUNDNESS-001` | `CG001-C-100`（负控制） | `formal/claude-cg001/godel-q-zfc/GodelQ/Negative/WrongSoundnessWithoutModel.lean` | `verification/runs/20261008-CG001-GODEL-Q-ZFC-NEG-SOUNDNESS-01/`；exit 1，模型实例 `Universe↓[ℒₛₑₜ] ⊧* insert (haltsS ΦH a) 𝗭𝗙𝗖` 找不到 | `NEGATIVE_CONTROL_REJECTED` |
| `MP-CG001-GODEL-Q-ZFC-NEG-DELTA1-001` | `CG001-C-97`（负控制） | `formal/claude-cg001/godel-q-zfc/GodelQ/Negative/WrongREWithoutDelta1.lean` | `verification/runs/20261008-CG001-GODEL-Q-ZFC-NEG-DELTA1-01/`；exit 1，`Theory.Δ₁ trueInUniverse` 找不到 | `NEGATIVE_CONTROL_REJECTED` |
| `MP-CG001-GODEL-Q-ZFC-NEG-CONSISTENCY-001` | `CG001-C-99`（负控制） | `formal/claude-cg001/godel-q-zfc/GodelQ/Negative/WrongConsistencyWithBot.lean` | `verification/runs/20261008-CG001-GODEL-Q-ZFC-NEG-CONSISTENCY-01/`；exit 1，`Entailment.Consistent (insert ⊥ 𝗭𝗙𝗖)` 找不到 | `NEGATIVE_CONTROL_REJECTED` |

| Claim ID | 精确主张 | 状态 | 证据 | 禁止外推 |
|---|---|---|---|---|
| CG001-C-84 | `Done e ↔ ∃ k, DoneBy e k`（`Done e := (Code.eval e 0).Dom`，`DoneBy e k := (Code.evaln k e 0).isSome`）；`DoneBy` 单调；`DoneBy` 作为二元谓词可计算 | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEXED` | run `20261007-CG001-GODEL-Q-01`（`qual_C84`） | 只关于部分递归程序在输入 0 上的停机 |
| CG001-C-85 | 对任一可枚举 `accepts` 存在 `d` 使 `Done d ↔ accepts d`（`d` 由 `Code.fixed_point₂` 构造，不是假设）；对任一 `NeverObserver O` 存在 `d`：`¬ Done d ∧ ¬ O.accepts d ∧ (Done d ↔ O.accepts d)` | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEXED` | run `20261007-CG001-GODEL-Q-01`；负控制 `-NEG-SOUNDNESS-01` | 经典结果（Kleene 递归定理），新的是读法 |
| CG001-C-86 | 不存在完备的 `NeverObserver`；可靠且完备的接受集不可枚举；`¬ REPred (fun e => ¬ Done e)`（另有 Mathlib 经 Rice 定理的独立证明） | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEXED` | run `20261007-CG001-GODEL-Q-01` | 不推出任何具体理论不一致 |
| CG001-C-87 | 任一观察者 `O` 有严格更大的 `O'`（多接受一个 `O` 漏掉的真永不完成者），`O'` 仍有漏点 | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEXED` | run `20261007-CG001-GODEL-Q-01` | 没有证明观察者塔的极限可枚举 |
| CG001-C-88 | 有效理论（R、Σ1C、Δ0C、Con）：`provesNever e → ¬ Done e`；每次完成都被证明；永不完成者的每个有限时刻都被证明“尚未完成” | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEXED` | run `20261007-CG001-GODEL-Q-01` | ZFC 读法以 CG-005 `CLAIM.md` §3 为条件；对真实 𝗭𝗙𝗖 见 CG001-C-99 |
| CG001-C-89 | 存在 `d`：`¬ Done d`，`¬ provesNever d`，`∀ k, provesNotYet d k`，且 `Done d ↔ provesNever d`；`¬ CompleteForNever` | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEXED` | run `20261007-CG001-GODEL-Q-01` | 不推出 `ZFC ⊢ ⊥` |
| CG001-C-90 | 有效理论 `¬ OmegaClosed`；封闭于 ω 完成规则 P 的一致 Σ1C/Δ0C 理论 `¬ REPred provesNever`；有效 + Σ1C + Δ0C + P（不预设一致）⟹ 存在 `e` 同时被证明停机与永不停机；控制 `toyTheory`、`truthTheory`、`consistency_needed`、`soundness_needed` | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEXED` | run `20261007-CG001-GODEL-Q-01`；负控制 `-NEG-CONSISTENCY-01`、`-NEG-EFFECTIVENESS-01` | “魔鬼交易”是解读；矛盾属于加了 P 的理论，不属于 bare ZFC |
| CG001-C-91 | 对任一可枚举可靠的到达接受者 `O` 存在 `d`：`Arrives d`，`¬ O.accepts d`，`∀ n, position d n < 1`，极限存在，`Arrives d ↔ ¬ O.accepts d`；`Arrives d ↔ ¬ Done d`；`Restores d ↔ Arrives d`；`rfind' succ` 驱动的跑者恰是经典芝诺序列，到达，且 `toyTheory` 确认它 | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEXED` | run `20261007-CG001-GODEL-Q-01` | 圆环读法只承接“逼近而复原确认不了”一面；经典芝诺本身的到达看得见 |
| CG001-C-92 | HBL 理论：Löb；`Pr con → Pr bot`；一致 ⟹ `¬ Pr con`；扩张若证明 `con` 则严格更强；`trivialBoxModel` 一致且 `¬ Pr con` | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEXED` | run `20261007-CG001-GODEL-Q-01`；负控制 `-NEG-GODEL-II-01` | ZFC 满足 HBL 与对角引理是来源中的标准元定理，未在本仓库形式化 |
| CG001-C-93 | 任一永不完成的 ω 追问上，“形式上完成的整体 ⟹ 有限阶段完成”（P_fin）被否定；芝诺序列永不在有限阶段到达而极限为 1；H0（参数形式）在“每一问都答否”之下 P_fin 被否定；`(processQ d).Never ↔ Arrives d` | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEXED` | run `20261007-CG001-GODEL-Q-01` | H0 的 HoTT 内容在 Agda（C-78），跨内核对应不是单一内核的证明 |
| CG001-C-94 | `AGeneral ↔ CompleteForNever`；`OmegaClosed → AGeneral`；有效 `RunnerTheory` 没有 `AGeneral`；具有 `AGeneral` 的 Σ1C/Δ0C 理论要么 `¬ REPred provesNever`，要么不一致 | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEXED` | run `20261007-CG001-GODEL-Q-01` | `AGeneral` 是“极限理论解决芝诺式问题”作为一般方法的读法；经典芝诺这一个实例不在其中 |
| CG001-C-95 | `𝗭𝗙𝗖` 有 Foundation 意义下的 Δ1 公理表示（`Theory.Δ₁`：Δ1 定义在 𝗜𝚺₁ 中可证地恰当）；`𝗦𝗘𝗣`、`𝗥𝗘𝗣𝗟` 各有 Δ1 识别（仿 Foundation 对归纳模式的 `InductionR`）；`𝗕𝗦𝗧` 有限 | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEXED` | run `20261008-CG001-GODEL-Q-ZFC-01`（`qual_C95`） | Δ1 指 Foundation 的内部定义，不是 Mathlib 的 `Primrec` |
| CG001-C-96 | `numCode`（经 `PR.Blueprint` 的内部原始递归，Σ1）在 ℕ 中等于 `⌜Num_n⌝`；在 `𝗭` 的每个模型中 `Num_n(z) ↔ z = ofNat n` | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEXED` | run `20261008-CG001-GODEL-Q-ZFC-01` | 只关于本包的数字公式写法 |
| CG001-C-97 | 对任意 ℒₛₑₜ 公式 `Φ`，`{n ∣ 𝗭𝗙𝗖 ⊢ neverS Φ n}` 可枚举（经 `𝗭𝗙𝗖.Δ₁`、内部可证性、`provable_iff_provable`、`rePred_iff_sigma1`） | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEXED` | run `20261008-CG001-GODEL-Q-ZFC-01`；负控制 `-NEG-DELTA1-01` | 可枚举指 Mathlib 的 `REPred` |
| CG001-C-98 | `𝗭𝗙𝗖 ⊳ 𝗥₀`（直接解释）；每个真实 r.e. 事实 `p a` 的数字句 `haltsS (arithTrln.translate (codeOfREPred p)) a` 被 𝗭𝗙𝗖 证明（𝗥₀ 的 Σ1 完全性，不需要可靠性） | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEXED` | run `20261008-CG001-GODEL-Q-ZFC-01` | 只解释 𝗥₀，未解释 𝗜𝚺₁ 或 𝗣𝗔 |
| CG001-C-99 | `zfcEffective : EffectiveTheory`，四条元性质全为定理；存在 `d`：`¬ Done d`，对每个 k `𝗭𝗙𝗖 ⊢ haltsS ΨN ⌜(d,k)⌝`，`𝗭𝗙𝗖 ⊬ neverS ΦH ⌜d⌝`，且 `Done d ↔ 𝗭𝗙𝗖 ⊢ neverS ΦH ⌜d⌝`；`¬ zfcEffective.OmegaClosed` | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEXED` | run `20261008-CG001-GODEL-Q-ZFC-01`；负控制 `-NEG-CONSISTENCY-01` | 一致性来自 Lean 元层模型（Foundation `zfc_consistent`）；不推出 `ZFC ⊢ ⊥` |
| CG001-C-100 | 数字句 Σ1 可靠：`𝗭𝗙𝗖 ⊢ haltsS (…codeOfREPred p…) a → p a`；`provesHalts e ↔ Done e`；对角过程的两句都独立（`𝗭𝗙𝗖 ⊬ neverS`、`𝗭𝗙𝗖 ⊬ haltsS`）；`Entailment.Incomplete 𝗭𝗙𝗖`（前提：无（可靠性经 `Universe`，见 §8 第 2 条）） | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEXED` | run `20261008-CG001-GODEL-Q-ZFC-01`；负控制 `-NEG-SOUNDNESS-01` | 可靠性是 Lean 元层定理，不是 𝗭𝗙𝗖 内部可证 |
| CG001-C-101 | 对任意一族 ℒₛₑₜ 句 `arr`，若 `∀ a, 𝗭𝗙𝗖 ⊢ arr a 🡘 neverS ΦH a`：存在确实到达的跑者，𝗭𝗙𝗖 每一刻确认它尚未停、位置 < 1、有极限，却证明不了 `arr ⌜d⌝`；`AGeneral ↔ CompleteForNever`；`OmegaClosed → AGeneral`；`¬ AGeneral`。参数可满足（取 `arr := neverS ΦH`）（前提：参数 `harr`） | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEXED` | run `20261008-CG001-GODEL-Q-ZFC-01` | 实分析的“到达”句在 ℒₛₑₜ 中的写法与等价的 𝗭𝗙𝗖 内部证明不在本包 |
| CG001-C-102 | S1：对任意 `[T.Δ₁] [𝗥₀ ⪯ T] [T.SoundOnHierarchy 𝚺 1]` 的算术理论 T，哥德尔 I 过程形式（含独立性）与魔鬼交易；交叉核对：Foundation 自带的 `incomplete_of_halting_problem` 对同一 T（另加 `𝗜𝚺₁ ⪯ T`）给出 `Entailment.Incomplete T`（前提：所列类型类实例） | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEXED` | run `20261008-CG001-GODEL-Q-ZFC-01` | 只对满足所列实例的算术理论 |


## 并入 `dev` 的 GPT 分支命题：dev-01 的稠密与量子化、应用充分性，dev-09 的 Cubical 哥德尔片段（2026-10-08）

> 来源：`origin/dev-01`（`f10899cb`）与 `origin/dev-09`（`ac6391b6`）。包与运行原样并入（`dev` 提交 `4a3535d9`），文件逐字节同分支。写入者：Claude Code 本机会话 `d58e0c0d`（CG-006 S7-c），研究发起人 2026-10-07 全面授权。本节只追加。
> 编号：这些命题在分支上的编号与本矩阵前文同号异义，这里一律改写为带分支前缀的 `D01-C-NNN`、`D09-C-NNN`；映射与理由见 `HoTT/CLAIM_NAMESPACE_LEDGER.md`。各行的主张、状态、证据与禁止外推照录分支矩阵的原行，只换编号，并在证据列末尾加本机重放结果（报告 `.claude/goals/CG-006-zfc-complete-formalization/verification/20261008-S7C-IMPORT-REPLAY.json`）。
> 读法：D01 是研究发起人“稠密性—运动”原合同（KC-000003、004、019）的有限机器控制，不证明物理时空离散，也不证明 ZFC 不能表示稠密或离散运动。D09 只到编码、引用与自实例的语法形状，没有对象层的可表示性定理，不是第一不完备定理；真实的第一不完备定理在 Foundation 的 𝗭𝗙𝗖 上由 CG001-C-99、C-100 给出。

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-ZFC-META-SUBTHEORY-ADEQUACY-001` | `D01-C-369` | `formal/zfc-meta-subtheory-adequacy/ApplicationAdequacy.lean` | `verification/runs/20261005-MP-ZFC-META-SUBTHEORY-ADEQUACY-001-04/`；Lean 4.34.1 core；fixed binary、exit 0、九个 selected theorem均报告无公理；negative control `MP-ZFC-META-SUBTHEORY-ADEQUACY-NEG-001` / `...-NEG-001/` 在 paid bridge伪造 failure处拒绝。；2026-10-08 20261005-MP-ZFC-META-SUBTHEORY-ADEQUACY-001-04 本机重放逐字节一致 | `KERNEL_ACCEPTED_WITH_SCOPE / SOURCE_CERTIFIED_APPLICATION_ADEQUACY_CONTRACT`：显式 application claim、original-resolution claim、RequiresBridge、无 bridge和无 explicit task switch共同构成 failure；paid bridge、task switch、model-only 和未付 SameQ_H0 均不被误判。 |
| `MP-ZFC-META-SUBTHEORY-ADEQUACY-NEG-002` | `D01-C-369` 负控制 | `formal/zfc-meta-subtheory-adequacy/WrongPaidBridgeFailure.lean` | `verification/runs/20261005-MP-ZFC-META-SUBTHEORY-ADEQUACY-NEG-002/`；exit 1，`ApplicationAdequacyFailure bridgePaidControl`无可用证明。`-001`保留为旧CLAIM/capture pin历史收据。；2026-10-08 20261005-MP-ZFC-META-SUBTHEORY-ADEQUACY-NEG-002 本机重放逐字节一致 | `NEGATIVE_CONTROL_REJECTED`：已支付 bridge的 case不能由 failure label伪造为 failure。 |
| `MP-ZFC-DENSE-QUANTIZED-MOTION-001` | `D01-C-370` | `formal/zfc-dense-quantized-motion/QuantizedHalfControl.lean` | `verification/runs/20261005-MP-ZFC-DENSE-QUANTIZED-MOTION-001-02/`；Lean 4.34.1 core；exit 0、四条 selected theorem无公理；negative control `MP-ZFC-DENSE-QUANTIZED-MOTION-NEG-001` / `...NEG-001/` 在 stage-3 premature completion处拒绝。；2026-10-08 20261005-MP-ZFC-DENSE-QUANTIZED-MOTION-001-02 本机重放逐字节一致 | `KERNEL_ACCEPTED_WITH_SCOPE / FINITE_QUANTIZED_CONTROL`：固定八单位量化 half-step过程在第4步到零、在第3步未到零。 |
| `MP-ZFC-DENSE-QUANTIZED-MOTION-NEG-002` | `D01-C-370` 负控制 | `formal/zfc-dense-quantized-motion/WrongPrematureQuantizedCompletion.lean` | `verification/runs/20261005-MP-ZFC-DENSE-QUANTIZED-MOTION-NEG-002/`；exit 1，`quantizedRun 3 = 0` 不能由refl交付。`-001`保留为旧CLAIM pin历史收据。；2026-10-08 20261005-MP-ZFC-DENSE-QUANTIZED-MOTION-NEG-002 本机重放逐字节一致 | `NEGATIVE_CONTROL_REJECTED`。 |
| `MP-ZFC-DENSE-QUANTIZED-CONTRACT-001` | `D01-C-371` | `formal/zfc-dense-quantized-contract/NormalizedCompletionContract.lean` | `verification/runs/20261005-MP-ZFC-DENSE-QUANTIZED-CONTRACT-001-02/`；Lean 4.34.1 core；exit 0、五条 selected theorem均无公理；negative control `MP-ZFC-DENSE-QUANTIZED-CONTRACT-NEG-001` / `...NEG-001/` 在 dense stage-four Done伪造处拒绝。`-01`保留为旧documentation-pin收据，见REVISIONS。；2026-10-08 20261005-MP-ZFC-DENSE-QUANTIZED-CONTRACT-001-02 本机重放逐字节一致 | `KERNEL_ACCEPTED_WITH_SCOPE / SYMBOLIC_COMPLETION_CONTRACT_CONTROL`：固定 normalized dense/quantized controls从相同初态开始、前三阶段一致，但 finite-stage completion predicates不逐点等价。 |
| `MP-ZFC-DENSE-QUANTIZED-CONTRACT-NEG-001` | `D01-C-371` 负控制 | `formal/zfc-dense-quantized-contract/WrongUniformFiniteStageDone.lean` | `verification/runs/20261005-MP-ZFC-DENSE-QUANTIZED-CONTRACT-NEG-001/`；exit 1，`dyadic 4 = zero`不能由refl交付。；2026-10-08 20261005-MP-ZFC-DENSE-QUANTIZED-CONTRACT-NEG-001 本机重放逐字节一致 | `NEGATIVE_CONTROL_REJECTED`。 |

| Claim ID | 精确主张 | 状态 | 证据 | 禁止外推 |
|---|---|---|---|---|
| D01-C-369（分支原编号 C-369） | 对 `ApplicationCase`，若 `applicationClaim ∧ claimsOriginalResolution ∧ requiresBridge ∧ ¬bridgePaid ∧ ¬explicitTaskSwitch`，则 `ApplicationAdequacyFailure`；`bridgePaidControl`、`taskSwitchControl`、`modelOnlyControl`分别不满足 failure，且 `h0MissingSameQ` 不能进入 `H0Eligible`。 | `KERNEL_ACCEPTED_WITH_SCOPE / SOURCE_CERTIFIED_APPLICATION_ADEQUACY_CONTRACT` | `MP-ZFC-META-SUBTHEORY-ADEQUACY-001` / `20261005-MP-ZFC-META-SUBTHEORY-ADEQUACY-001-04`；source-to-spec fields及边界见 `formal/zfc-meta-subtheory-adequacy/CLAIM.md` 和 C4A/C5A audit cards。 | 不证明 bare ZFC 的对象语言矛盾、ZFC 无法表示时间、所有数学模型或标准解法失败、IEP/Norton事实由内核证明、HoTT/芝诺 SameQ，或本 SOP 已完成。 |
| D01-C-370（分支原编号 C-370） | 对固定 `quantizedRun`，`run 0=8`、`run 1=4`、`run 2=2`、`run 3=1`、`run 4=0`；故第4步完成且第3步未完成。 | `KERNEL_ACCEPTED_WITH_SCOPE / FINITE_QUANTIZED_CONTROL` | `MP-ZFC-DENSE-QUANTIZED-MOTION-001` / `20261005-MP-ZFC-DENSE-QUANTIZED-MOTION-001-02`；用户/source-to-spec边界见 C2C contract。 | 不证明物理时空离散、普朗克尺度、任何一般量化规则终止、ZFC错误或极限理论错误。 |
| D01-C-371（分支原编号 C-371） | 对固定 symbolic normalized controls，dense和quantized在 0–3 阶段共享同一个非零dyadic余量；dense无任何finite-stage Done、quantized在4步Done，因此不存在二者finite-stage Done的逐点等价。 | `KERNEL_ACCEPTED_WITH_SCOPE / SYMBOLIC_COMPLETION_CONTRACT_CONTROL` | `MP-ZFC-DENSE-QUANTIZED-CONTRACT-001` / `20261005-MP-ZFC-DENSE-QUANTIZED-CONTRACT-001-02`；C4D task/source-to-spec见 `formal/zfc-dense-quantized-contract/CLAIM.md`。 | 不证明C-361 real-analysis theorem、C-370的源代码同一性、物理时空、IEP来源事实、user Q与IEP Q同一或bare ZFC判词。 |

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-CUBICAL-GODEL-FRAGMENT-001` | `D09-C-370`–`D09-C-374` | `formal/cubical-godel-fragment/CCTTmini.agda`；`CLAIM.md`；`--safe --cubical` | `verification/runs/20261005-MP-CUBICAL-GODEL-FRAGMENT-001-02/`；Cubical Agda 2.8.0-3d04bac，exit 0、stderr 0；负控制 `MP-CUBICAL-GODEL-FRAGMENT-NEG-001` / `...NEG-001-02` 在 `true != false` 处拒绝；2026-10-08 20261005-MP-CUBICAL-GODEL-FRAGMENT-001-02 本机重放在替换原工作树路径后一致 | `KERNEL_ACCEPTED_WITH_SCOPE / SOURCE_CORRESPONDING_FRAGMENT_ONLY`：finite RawCert、structural checker 与 explicit Deriv witness 已 machine-checked；不含 Nat-valued Gödel编码、representability、fixed point、完整 cubical semantics、H0或ZFC归因。 |
| `MP-CUBICAL-GODEL-FRAGMENT-NEG-001` | `D09-C-370`–`D09-C-374`（负控制） | `formal/cubical-godel-fragment/WrongCCTTmini.agda` | `verification/runs/20261005-MP-CUBICAL-GODEL-FRAGMENT-NEG-001-02/`；exit 42，`true != false`；2026-10-08 20261005-MP-CUBICAL-GODEL-FRAGMENT-NEG-001-02 本机重放在替换原工作树路径后一致 | `NEGATIVE_CONTROL_REJECTED`：已接受正例不能被伪造为拒绝。 |
| `MP-CUBICAL-GODEL-NAT-CODING-001` | `D09-C-375`–`D09-C-378` | `formal/cubical-godel-fragment/CCTTminiNat.agda`；`NAT_CODING_CLAIM.md`；`--safe --cubical` | `verification/runs/20261005-MP-CUBICAL-GODEL-NAT-CODING-001-01/`；Cubical Agda 2.8.0-3d04bac，exit 0，stdout 保留 `UnsupportedIndexedMatch` warning；negative `...NEG-001-01` 在 `reflC (sucC (varC zero)) != zeroC` 处拒绝；2026-10-08 20261005-MP-CUBICAL-GODEL-NAT-CODING-001-01 本机重放在替换原工作树路径后一致 | `KERNEL_ACCEPTED_WITH_SCOPE / SOURCE_CORRESPONDING_NAT_CODING_FRAGMENT_ONLY`：finite RawCert 的 parser、Nat code、total image decoder 和 injectivity 已检查；不含 formula/proof predicate、representability、fixed point、full cubical semantics、H0 或 ZFC归因。 |
| `MP-CUBICAL-GODEL-NAT-CODING-NEG-001` | `D09-C-375`–`D09-C-378`（负控制） | `formal/cubical-godel-fragment/WrongCCTTminiNat.agda` | `verification/runs/20261005-MP-CUBICAL-GODEL-NAT-CODING-NEG-001-01/`；exit 42；2026-10-08 20261005-MP-CUBICAL-GODEL-NAT-CODING-NEG-001-01 本机重放在替换原工作树路径后一致 | `NEGATIVE_CONTROL_REJECTED`：编码像中的正例不能被伪称为 `zeroC`。 |
| `MP-CUBICAL-GODEL-FORMULA-PREDICATE-001` | `D09-C-379`–`D09-C-382` | `formal/cubical-godel-fragment/CCTTminiFormula.agda`；`FORMULA_PREDICATE_CLAIM.md`；`--safe --cubical` | `verification/runs/20261005-MP-CUBICAL-GODEL-FORMULA-PREDICATE-001-01/`；Cubical Agda 2.8.0-3d04bac，exit 0、preserved inherited warning；negative `...NEG-001-01` 在 `provF (code closedC) != botF` 处拒绝；2026-10-08 20261005-MP-CUBICAL-GODEL-FORMULA-PREDICATE-001-01 本机重放在替换原工作树路径后一致 | `KERNEL_ACCEPTED_WITH_SCOPE / META_OBJECT_BOUNDARY_EXPLICIT`：closed certificate code、formula quotation 与 meta witness interface 已检查；没有 arithmetic representability、formula coding/substitution 或 fixed point。 |
| `MP-CUBICAL-GODEL-FORMULA-PREDICATE-NEG-001` | `D09-C-379`–`D09-C-382`（负控制） | `formal/cubical-godel-fragment/WrongCCTTminiFormula.agda` | `verification/runs/20261005-MP-CUBICAL-GODEL-FORMULA-PREDICATE-NEG-001-01/`；exit 42；2026-10-08 20261005-MP-CUBICAL-GODEL-FORMULA-PREDICATE-NEG-001-01 本机重放在替换原工作树路径后一致 | `NEGATIVE_CONTROL_REJECTED`：quoted certificate formula 不是 `botF`。 |
| `MP-CUBICAL-GODEL-FORMULA-CODING-001` | `D09-C-383`–`D09-C-386` | `formal/cubical-godel-fragment/CCTTminiFormulaCode.agda`；`FORMULA_CODING_CLAIM.md`；`--safe --cubical` | `verification/runs/20261005-MP-CUBICAL-GODEL-FORMULA-CODING-001-01/`；Cubical Agda 2.8.0-3d04bac，exit 0、preserved inherited warning；negative `...NEG-001-01` 在 self instance ≠ `bot₁` 处拒绝；2026-10-08 20261005-MP-CUBICAL-GODEL-FORMULA-CODING-001-01 本机重放在替换原工作树路径后一致 | `KERNEL_ACCEPTED_WITH_SCOPE / SYNTAX_LEVEL_DIAGONAL_SHAPE_ONLY`：formula code/decoder/injectivity和模板的 self-code numeral substitution 已检查；无 representability、fixed-point equivalence或incompleteness。 |
| `MP-CUBICAL-GODEL-FORMULA-CODING-NEG-001` | `D09-C-383`–`D09-C-386`（负控制） | `formal/cubical-godel-fragment/WrongCCTTminiFormulaCode.agda` | `verification/runs/20261005-MP-CUBICAL-GODEL-FORMULA-CODING-NEG-001-01/`；exit 42；2026-10-08 20261005-MP-CUBICAL-GODEL-FORMULA-CODING-NEG-001-01 本机重放在替换原工作树路径后一致 | `NEGATIVE_CONTROL_REJECTED`：self instance 不被伪造为 bottom。 |

| Claim ID | 精确主张 | 状态 | 证据 | 禁止外推 |
|---|---|---|---|---|
| D09-C-370（分支原编号 C-370） | 固定 `Γ₁ = Nat ∷ []` 中，`positiveC = reflC (sucC (varC 0))` 满足 `accepts Γ₁ positiveC ≡ true`。 | `KERNEL_ACCEPTED_WITH_SCOPE` | `CCTTmini.positiveAccepted`；主 run。 | 只是一项固定正例；不证明 full cctt/redtt 或一般 HoTT checker。 |
| D09-C-371（分支原编号 C-371） | `positiveWitness` 给出 `Checked Γ₁ positiveC`，其内容是 `Deriv Γ₁ (erase positiveC) (Path Nat (suc (var 0)) (suc (var 0)))`。 | `KERNEL_ACCEPTED_WITH_SCOPE` | `CCTTmini.positiveWitness`；主 run。 | 不构造完整 derivation calculus、上游 proof certificate 或 universe/path semantics。 |
| D09-C-372（分支原编号 C-372） | 空 context 的 `varC 0` 满足 `accepts [] (varC 0) ≡ false`。 | `KERNEL_ACCEPTED_WITH_SCOPE` | `CCTTmini.illScopedRejected`；主 run。 | 只覆盖该 fragment 的一条 ill-scoped input。 |
| D09-C-373（分支原编号 C-373） | `accepts [] (sucC (reflC zeroC)) ≡ false`；路径 certificate 不被当成 Nat certificate。 | `KERNEL_ACCEPTED_WITH_SCOPE` | `CCTTmini.wrongSucRejected`；主 run。 | 不涵盖完整 definitional equality 或所有类型错配。 |
| D09-C-374（分支原编号 C-374） | 每一个 `Checked Γ c` 携带 `Deriv Γ (erase c) A`；`checkedSound` 与 `checkSound` 公开该证书到 derivation 的消去。 | `KERNEL_ACCEPTED_WITH_SCOPE` | `CCTTmini.checkedSound/checkSound`；主 run。 | 这不是对任意 Raw term 的 complete checker，更不是 `Proof_T` 的算术表示性。 |
| D09-C-375（分支原编号 C-375） | `unbits-code : (bs : List Bool) → unbits (LEN bs) (codeBits bs) ≡ bs`。 | `KERNEL_ACCEPTED_WITH_SCOPE` | `CCTTminiNat.unbits-code`；主 run。 | 不证明任意 Nat 是某个有效 bit/certificate code。 |
| D09-C-376（分支原编号 C-376） | `parse-run`：对任意 `RawCert c`、stack/rest/fuel，prefix bit grammar `bits c ++ rest` 被 finite-fuel parser 精确还原为 `close c stack` 与原 rest。 | `KERNEL_ACCEPTED_WITH_SCOPE` | `CCTTminiNat.parse-run`；主 run。 | 不验证 cctt/redtt 的完整 parser 或 conversion semantics。 |
| D09-C-377（分支原编号 C-377） | `decode-code : (c : RawCert) → decode (code c) ≡ c`。 | `KERNEL_ACCEPTED_WITH_SCOPE / WARNING_SCOPED` | `CCTTminiNat.decode-code`；主 run的 preserved warning。 | 只对编码像 roundtrip；不说明 malformed Nat codes、任意 transports 或 full object syntax。 |
| D09-C-378（分支原编号 C-378） | `code-injective : code c ≡ code d → c ≡ d`。 | `KERNEL_ACCEPTED_WITH_SCOPE / WARNING_SCOPED` | `CCTTminiNat.code-injective`；主 run。 | 不构成 arithmetic provability predicate、formula quotation或 diagonal fixed point。 |
| D09-C-379（分支原编号 C-379） | `validCode (code closedC) ≡ true`。 | `KERNEL_ACCEPTED_WITH_SCOPE / WARNING_SCOPED` | `CCTTminiFormula.closedAccepted`；主 run。 | `validCode` 是 meta-level checker，不是对象公式。 |
| D09-C-380（分支原编号 C-380） | `closedProvWitness : ProvWitness (code closedC)`。 | `KERNEL_ACCEPTED_WITH_SCOPE / WARNING_SCOPED` | `CCTTminiFormula.closedProvWitness`；主 run。 | 一个 closed certificate witness，不是 full proof predicate or enumeration theorem。 |
| D09-C-381（分支原编号 C-381） | `quoteCert closedC ≡ provF (code closedC)`。 | `KERNEL_ACCEPTED_WITH_SCOPE` | `CCTTminiFormula.quoteClosed`；主 run。 | formula syntax 引用 code，不等于 code of formula / self-reference。 |
| D09-C-382（分支原编号 C-382） | `ProvHolds (quoteCert closedC)` 由同一 `ProvWitness` 证明。 | `KERNEL_ACCEPTED_WITH_SCOPE / WARNING_SCOPED` | `CCTTminiFormula.quoteClosedHolds`；主 run。 | `ProvHolds` 只定义了 `provF` clause；没有 implication/falsum semantics、representability或reflection。 |
| D09-C-383（分支原编号 C-383） | `decodeExprCode : decodeExpr (codeExpr e) ≡ e`。 | `KERNEL_ACCEPTED_WITH_SCOPE / WARNING_SCOPED` | `CCTTminiFormulaCode.decodeExprCode`；主 run。 | 只覆盖 `lit/fvar` expression fragment。 |
| D09-C-384（分支原编号 C-384） | `decodeFormulaCode` 与 `formulaCodeInjective`：Fmini formula code roundtrip 且单射。 | `KERNEL_ACCEPTED_WITH_SCOPE / WARNING_SCOPED` | 相应 declarations；主 run。 | 不含 implication/binders或任意上游 formula syntax。 |
| D09-C-385（分支原编号 C-385） | `selfInstance template ≡ prov₁ (lit (codeFormula template))`，其中 `template = prov₁ (fvar 0)`。 | `KERNEL_ACCEPTED_WITH_SCOPE` | `CCTTminiFormulaCode.selfInstanceShape`；主 run。 | syntax substitution shape，不是 Gödel fixed point。 |
| D09-C-386（分支原编号 C-386） | `selfInstance template ≡ prov₁ (quoteFormula template)`。 | `KERNEL_ACCEPTED_WITH_SCOPE` | `CCTTminiFormulaCode.selfInstanceQuotesFormula`；主 run。 | quotation syntax不代表 `ProvWitness` 的 arithmetic representation。 |

## Claude CG-006 S6：Z0 的条件形式——𝗭𝗙𝗖 的算术影子与哥德尔第二不完备定理（2026-10-08）

> 授权同上一 Claude 节（研究发起人 2026-10-07 全面授权；会话 `d58e0c0d`）。本节只追加。
> 工具链同 CG-006：Lean 4.34.0 + Mathlib `5ed29652…` + Foundation `1fb01b72`，禁网编译；记录 `formal/claude-cg001/godel-q-zfc-z0/LEAN_TOOLCHAIN.json`、`MATHLIB_CLOSURE.json`（1,893 个模块，聚合 `02b0e80f…5161`）。两个运行都经 `verify_cg001_run.py --rerun` 精确重放；目标内索引 `.claude/goals/CG-001-targeted-overview/证据索引.md` §26。
> 读法：条件定理。两条前提 `Sh.RE`、`𝗜𝚺₁ ⪯ Sh` 是 S6 的卡点，没有证明；“Sh 一致 ⟺ 𝗭𝗙𝗖 一致”的 𝗜𝚺₁ 内部化也没有做。所以本节不推出 Z0 对 𝗭𝗙𝗖 成立，只把它化成精确的引理。

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-CG001-GODEL-Q-ZFC-Z0-001` | `CG001-C-103` | `formal/claude-cg001/godel-q-zfc-z0/GodelQ/ZFC/Z0Shadow.lean`（加 15 个与 `godel-q-zfc` 逐字节相同的依赖模块；命题全文 `CLAIM.md`） | `verification/runs/20261008-CG001-GODEL-Q-ZFC-Z0-01/`；exit 0，stderr 0 B；五条定理只依赖三条标准公理；精确重放一致 | `KERNEL_ACCEPTED_WITH_SCOPE / GOAL_LOCAL_INDEXED / CONDITIONAL_ON_TWO_EXPLICIT_HYPOTHESES` |
| `MP-CG001-GODEL-Q-ZFC-Z0-NEG-ISIGMA1-001` | `CG001-C-103`（负控制） | `formal/claude-cg001/godel-q-zfc-z0/GodelQ/Negative/WrongZ0WithoutISigma1.lean` | `verification/runs/20261008-CG001-GODEL-Q-ZFC-Z0-NEG-ISIGMA1-01/`；exit 1，实例 `𝗜𝚺₁ ⪯ Sh` 找不到 | `NEGATIVE_CONTROL_REJECTED`：已证的 `𝗥₀ ⪯ Sh` 不能代替 `𝗜𝚺₁ ⪯ Sh` |

| Claim ID | 精确主张 | 状态 | 证据 | 禁止外推 |
|---|---|---|---|---|
| CG001-C-103 | `Sh := {σ ∣ 𝗭𝗙𝗖 ⊢ σᵗ}`（`σᵗ := arithTrln.translate σ`）：`Sh ⊢ σ ↔ 𝗭𝗙𝗖 ⊢ σᵗ`；`Sh` 一致；`𝗥₀ ⪯ Sh`；若 `[Sh.RE] [𝗜𝚺₁ ⪯ Sh]`，则 `𝗭𝗙𝗖 ⊬ arithTrln.translate (Sh.craig.consistent.val)` 且 `Sh ⊬ Sh.craig.consistent.val` | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEXED / CONDITIONAL` | run `20261008-CG001-GODEL-Q-ZFC-Z0-01`（`zfc_z0_conditional`）；负控制 `-NEG-ISIGMA1-01` | 两条前提未证；不推出 Z0 对 𝗭𝗙𝗖 成立；`Sh` 的一致性来自 Lean 元层 `Universe` 模型；不推出 `ZFC ⊢ ⊥` |

## Claude CG-007 W1：图灵路线——不对 𝗭𝗙𝗖 做自指的观察力不完备（无哥德尔路线 (a)，2026-10-08）

> 授权同上一 Claude 节（研究发起人 2026-10-07 全面授权；2026-10-08：“按照你的想法进行优先级安排，完成后续所有“形式化和机器证明”工作。”；会话 `d58e0c0d`）。本节只追加。
> 工具链同 CG-006；记录 `formal/claude-cg001/godel-q-zfc-turing/LEAN_TOOLCHAIN.json`、`MATHLIB_CLOSURE.json`（1,889 个模块，聚合 `21197b0b…29c7`）。两个运行都经 `verify_cg001_run.py --rerun` 精确重放；目标内索引 `.claude/goals/CG-001-targeted-overview/证据索引.md` §27。
> 读法：机器证明（有范围）。源码末尾的 `run_cmd` 依赖检查核对：这些定理不依赖本项目的对角声明（含 C-99/C-100），依赖 Mathlib 的停机定理；停机定理本身经 Rice 定理用到递归定理。所以“无哥德尔”只指不对 𝗭𝗙𝗖 及其可证性做自指。

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-CG001-GODEL-Q-ZFC-TURING-001` | `CG001-C-104`、`CG001-C-105` | `formal/claude-cg001/godel-q-zfc-turing/GodelQ/Turing.lean`、`ZFC/TuringZFC.lean`、`ZFC/QualificationTuring.lean`（加 16 个与 `godel-q-zfc` 逐字节相同的依赖模块；命题全文 `CLAIM.md`） | `verification/runs/20261008-CG001-GODEL-Q-ZFC-TURING-01/`；exit 0，stderr 0 B；87 条公理报告只有三条标准公理；依赖检查两行通过；精确重放一致 | `KERNEL_ACCEPTED_WITH_SCOPE / GOAL_LOCAL_INDEXED` |
| `MP-CG001-GODEL-Q-ZFC-TURING-NEG-TRUTH-001` | `CG001-C-104`（负控制） | `formal/claude-cg001/godel-q-zfc-turing/GodelQ/Negative/WrongTuringWithTruthObserver.lean` | `verification/runs/20261008-CG001-GODEL-Q-ZFC-TURING-NEG-TRUTH-01/`；exit 1，`re` 字段处被拒 | `NEGATIVE_CONTROL_REJECTED`：可靠但不可枚举的真理观察者没有漏点，“可枚举”这一前提确实被用到 |

| Claim ID | 精确主张 | 状态 | 证据 | 禁止外推 |
|---|---|---|---|---|
| CG001-C-104 | 任一可靠、可枚举的永不完成观察者 `O`：`¬ REPred (· ∈ O.Misses)`，`O.Misses.Infinite`，任意有限补丁之后同样成立；任一 `EffectiveTheory`：`¬ CompleteForNever`（证明不经过对角点），漏点不可枚举且无穷，漏点的每个有限时刻都被确认“尚未完成” | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEXED` | run `20261008-CG001-GODEL-Q-ZFC-TURING-01`（`qual_C104`）；负控制 `-NEG-TRUTH-01` | 停机问题的证明本身是对角论证；不推出任何理论不一致 |
| CG001-C-105 | 对 Foundation 的 `𝗭𝗙𝗖`：`zfcMisses = {e ∣ 𝗭𝗙𝗖 ⊬ neverS ΦH ⌜e⌝ ∧ 𝗭𝗙𝗖 ⊬ haltsS ΦH ⌜e⌝}`；它不可枚举且无穷；对其中每个 e 与每个 k，`𝗭𝗙𝗖 ⊢ haltsS ΨN ⌜(e,k)⌝`；`¬ zfcEffective.CompleteForNever`；`Entailment.Incomplete 𝗭𝗙𝗖`；有限补丁之后漏点仍不可枚举、仍无穷 | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEXED` | run `20261008-CG001-GODEL-Q-ZFC-TURING-01`（`qual_C105`） | 一致与 Σ1 可靠来自 Lean 元层 `Universe` 模型；补丁定理针对观察者，不是 𝗭𝗙𝗖 加公理后的演绎闭包；不推出 `ZFC ⊢ ⊥` |

## Claude CG-007 W2：取到与贴近——稠密性恰是芝诺缺口的前提（无哥德尔路线 (b)，时空结构一面，2026-10-08）

> 授权同上节。本节只追加。
> 工具链：Lean 4.34.0 + Mathlib `5ed29652…`（不用 Foundation 的对象理论）；记录 `formal/claude-cg001/zeno-density-attainment/LEAN_TOOLCHAIN.json`、`MATHLIB_CLOSURE.json`（1,681 个模块，聚合 `9deac388…630a`）。两个运行都经 `verify_cg001_run.py --rerun` 精确重放；目标内索引 `.claude/goals/CG-001-targeted-overview/证据索引.md` §28。
> 读法：机器证明（有范围）。这些是 Mathlib 实分析与拓扑中的定理（子理论一侧），不是 Foundation 𝗭𝗙𝗖 中的推导；不证明现实时空量子化，不裁定哪一个“到达”是原任务的，只定位二者分开的确切前提。

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-CG001-ZENO-DENSITY-ATTAINMENT-001` | `CG001-C-106`、`CG001-C-107`、`CG001-C-108` | `formal/claude-cg001/zeno-density-attainment/GodelQ/Zeno/Attainment.lean`、`Runners.lean`、`QualificationZeno.lean`（命题全文 `CLAIM.md`） | `verification/runs/20261008-CG001-ZENO-DENSITY-ATTAINMENT-01/`；exit 0，stderr 0 B；22 条公理报告只有三条标准公理；精确重放一致 | `KERNEL_ACCEPTED_WITH_SCOPE / GOAL_LOCAL_INDEXED` |
| `MP-CG001-ZENO-DENSITY-ATTAINMENT-NEG-DENSE-001` | `CG001-C-106`（负控制） | `formal/claude-cg001/zeno-density-attainment/GodelQ/Negative/WrongDenseAttains.lean` | `verification/runs/20261008-CG001-ZENO-DENSITY-ATTAINMENT-NEG-DENSE-01/`；exit 1，`Isolated (1 : ℝ)` 无法证明 | `NEGATIVE_CONTROL_REJECTED`：“终点孤立”这一前提确实被用到 |

| Claim ID | 精确主张 | 状态 | 证据 | 禁止外推 |
|---|---|---|---|---|
| CG001-C-106 | 第一可数空间中 `(∀ s, ArrivesAt s x → AttainsAt s x) ↔ Isolated x`；ℝ 中每一点不孤立（`zenoSeq x`）；格点值收敛序列最终等于极限；离散空间同样 | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEXED` | run `20261008-CG001-ZENO-DENSITY-ATTAINMENT-01`（`qual_C106`）；负控制 `-NEG-DENSE-01` | 不证明现实时空量子化；不裁定哪一个“到达”是原任务的 |
| CG001-C-107 | 量子化半步跑者（`quantStep m r = ⌊r/2·2ᵐ⌋/2ᵐ`）的闭式、格点性、恰在第 m+1 步完成、第 0 至 m 步与稠密跑者相同；`¬ ∃ g, ∀ s L, ArrivesAt s L → (g L ↔ AttainsAt s L)`，带粒度的判据存在；完成在 m → ∞ 的逐步极限里丢失，位置的累次极限都是 1 | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEXED` | 同上（`qual_C107`） | 量子化只用等距格点模型；推广而不替代 D01-C-370、C-371 |
| CG001-C-108 | 稠密时间：阶段时刻严格递增、都 < 1、以 1 为极限；连续运动在 t = 1 ∈ [0,1] 取到 1（正控制）；t = 1 不是任何阶段；格点时间中严格递增序列无上界 | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEXED` | 同上（`qual_C108`） | 闭区间端点只作标准解完成的正控制，不替代原过程完成 |

## Claude CG-007 W3：𝗭𝗙𝗖 解释 𝗣𝗔；Z0 只剩一条前提（2026-10-08）

> 授权同上节。本节只追加。
> 工具链同 CG-006；记录 `formal/claude-cg001/godel-q-zfc-z0-pa/LEAN_TOOLCHAIN.json`、`MATHLIB_CLOSURE.json`（1,893 个模块，聚合 `02b0e80f…5161`）。两个运行都经 `verify_cg001_run.py --rerun` 精确重放；目标内索引 `.claude/goals/CG-001-targeted-overview/证据索引.md` §29。
> 读法：机器证明（有范围）。C-103 的第二条前提 `𝗜𝚺₁ ⪯ Sh` 成为定理；Z0 只剩 `Sh.RE` 与内部化，本节不推出 Z0 对 𝗭𝗙𝗖 已成立。

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-CG001-GODEL-Q-ZFC-Z0-PA-001` | `CG001-C-109`、`CG001-C-110` | `formal/claude-cg001/godel-q-zfc-z0-pa/GodelQ/ZFC/OmegaLaws.lean`、`PAModel.lean`、`Z0PA.lean`、`QualificationZ0PA.lean`（加 17 个逐字节复制的依赖模块；命题全文 `CLAIM.md`） | `verification/runs/20261008-CG001-GODEL-Q-ZFC-Z0-PA-01/`；exit 0，stderr 0 B；94 条公理报告只有三条标准公理；精确重放一致 | `KERNEL_ACCEPTED_WITH_SCOPE / GOAL_LOCAL_INDEXED` |
| `MP-CG001-GODEL-Q-ZFC-Z0-PA-NEG-RE-001` | `CG001-C-110`（负控制） | `formal/claude-cg001/godel-q-zfc-z0-pa/GodelQ/Negative/WrongZ0WithoutRE.lean` | `verification/runs/20261008-CG001-GODEL-Q-ZFC-Z0-PA-NEG-RE-01/`；exit 1，实例 `Theory.RE Sh` 找不到 | `NEGATIVE_CONTROL_REJECTED`：`Sh.RE` 仍是前提，没有被偷偷证明 |

| Claim ID | 精确主张 | 状态 | 证据 | 禁止外推 |
|---|---|---|---|---|
| CG001-C-109 | 对每个 `M ⊧ 𝗭𝗙𝗖`，`(arithTrln.Model M) ⊧* 𝗣𝗔`；`paInterp : 𝗭𝗙𝗖 ⊳ 𝗣𝗔`；`𝗣𝗔 ⊢ σ → 𝗭𝗙𝗖 ⊢ arithTrln.translate σ` | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEXED` | run `20261008-CG001-GODEL-Q-ZFC-Z0-PA-01`（`qual_C109`） | 经典事实的形式化；完备性定理与模型在 Lean 元层 |
| CG001-C-110 | `𝗣𝗔 ⪯ Sh`；`𝗜𝚺₁ ⪯ Sh`；在 `[Sh.RE]` 下 `𝗭𝗙𝗖 ⊬ arithTrln.translate (Sh.craig.consistent.val)` 且 `Sh ⊬ Sh.craig.consistent.val` | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEXED / CONDITIONAL_ON_ONE_EXPLICIT_HYPOTHESIS` | 同上（`qual_C110`）；负控制 `-NEG-RE-01` | `Sh.RE` 与内部化未证；不推出 Z0 对 𝗭𝗙𝗖 已成立；不推出 `ZFC ⊢ ⊥` |

## Claude CG-007 W4a：𝗭𝗙𝗖 的定理集可枚举；Z0 归结为一条纯语法引理（2026-10-09）

> 授权同上节。本节只追加。工具链与闭包同上节；目标内索引 §30。读法：机器证明（有范围）；Z0 的条件收窄为“`arithTrln.translate` 可计算”，该引理未证。

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-CG001-GODEL-Q-ZFC-Z0-RE-001` | `CG001-C-111` | `formal/claude-cg001/godel-q-zfc-z0-re/GodelQ/ZFC/ShRE.lean`、`QualificationShRE.lean`（加 20 个逐字节复制的依赖模块；命题全文 `CLAIM.md`） | `verification/runs/20261009-CG001-GODEL-Q-ZFC-Z0-RE-01/`；exit 0，stderr 0 B；97 条公理报告只有三条标准公理；精确重放一致 | `KERNEL_ACCEPTED_WITH_SCOPE / GOAL_LOCAL_INDEXED` |
| `MP-CG001-GODEL-Q-ZFC-Z0-RE-NEG-COMP-001` | `CG001-C-111`（负控制） | `formal/claude-cg001/godel-q-zfc-z0-re/GodelQ/Negative/WrongShREWithoutComputability.lean` | `verification/runs/20261009-CG001-GODEL-Q-ZFC-Z0-RE-NEG-COMP-01/`；exit 1 | `NEGATIVE_CONTROL_REJECTED`：可计算性没有被偷偷证明 |

| Claim ID | 精确主张 | 状态 | 证据 | 禁止外推 |
|---|---|---|---|---|
| CG001-C-111 | `REPred (fun φ : Sentence ℒₛₑₜ ↦ 𝗭𝗙𝗖 ⊢ φ)`；可计算且在 𝗭𝗙𝗖 中与 `arithTrln.translate` 可证性相同的 τ 给出 `Sh.RE`；`Computable arithTrln.translate → 𝗭𝗙𝗖 ⊬ (Sh.craig.consistent)ᵗ` | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEXED / CONDITIONAL_ON_ONE_SYNTACTIC_LEMMA` | run `20261009-CG001-GODEL-Q-ZFC-Z0-RE-01`（`qual_C111`）；负控制 `-NEG-COMP-01` | 翻译的可计算性未证；内部化未做；不推出 Z0 已成立 |

## Claude CG-007 W6：同一个 ω 追问，在一个有单价性的内核里（2026-10-09）

> 授权同上节。本节只追加。工具链：Cubical Agda 2.8.0 + cubical 0.9（macOS 记录 `formal/dedekind-omega-missile/TOOLCHAIN.json`），`--safe`，无公设。四个运行都经 `verify_cg001_run.py --rerun` 精确重放；目标内索引 §31。
> 读法：机器证明（有范围）。同一内核中的同一类型、同一程序与同一跑者；不证明芝诺、H0、Z0 的数学内容相同；Z0 以参数接入，“𝗭𝗙𝗖 证明不了”在 Lean 一侧。

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-CG001-SAME-Q-UNIVALENT-001` | `CG001-C-112`、`CG001-C-113` | `formal/claude-cg001/same-q-univalent/SameQ.agda`（导入 `pedometer-semantics`、`questioning-delay`、`truncation-questioning`、`product-questioning`、`universe-questioning`；命题全文 `CLAIM.md`） | `verification/runs/20261009-CG001-SAME-Q-UNIVALENT-01/`；exit 0；精确重放一致 | `KERNEL_ACCEPTED_WITH_SCOPE / GOAL_LOCAL_INDEXED` |
| `MP-CG001-SAME-Q-UNIVALENT-NEG-001` | `CG001-C-113`（负控制） | `formal/claude-cg001/same-q-univalent/WrongH0Settles.agda` | `verification/runs/20261009-CG001-SAME-Q-UNIVALENT-NEG-01/`；exit 42，`nothing != just 1` | `NEGATIVE_CONTROL_REJECTED` |
| `MP-CG001-SAME-Q-UNIVALENT-NEG-002` | `CG001-C-113`（负控制） | `formal/claude-cg001/same-q-univalent/WrongTruncUnsettled.agda` | `verification/runs/20261009-CG001-SAME-Q-UNIVALENT-NEG-02/`；exit 42，`true != false` | `NEGATIVE_CONTROL_REJECTED` |
| `MP-CG001-SAME-Q-UNIVALENT-NEG-003` | `CG001-C-112`（负控制） | `formal/claude-cg001/same-q-univalent/WrongRunnerWithoutMonotone.agda` | `verification/runs/20261009-CG001-SAME-Q-UNIVALENT-NEG-03/`；exit 42，`alt k != not (alt k)` | `NEGATIVE_CONTROL_REJECTED`：单调前提确实被用到 |

| Claim ID | 精确主张 | 状态 | 证据 | 禁止外推 |
|---|---|---|---|---|
| CG001-C-112 | `OmegaQ = ℕ → Bool` 与找到即停的 `Delay` 搜索 `askQ`：`NeverFrom q s ↔ askQ q s ≡ never`；落定则燃料 k 内有输出；`¬ PFin`；单调追问的减半跑者 `Arrives ↔ Never`，单调前提不可去（`monotoneNeeded`）；`question C judge ≡ askQ (FromJudge.answers C judge) 1` | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEXED` | run `20261009-CG001-SAME-Q-UNIVALENT-01`（`qual-C112`）；负控制 `-NEG-03` | 跑者到达是算术写法（减半次数无界），不用实数 |
| CG001-C-113 | 芝诺：`askQ constFalse 0 ≡ never`、减半次数 = n、到达；H0：单价宇宙上 `question ≡ askQ answers 1`、从第 1 阶段起永不落定、跑者到达、`runFor 100 … ≡ nothing` 由 `refl`；截断宇宙 `TU`：第 1 阶段停、此后每阶段落定、跑者不到达；Z0：任一单调流满足同样的等价 | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEXED` | run `20261009-CG001-SAME-Q-UNIVALENT-01`（`qual-C113`）；负控制 `-NEG-01`、`-NEG-02` | 三者共用类型与程序，各自的“落定”意义来自解释桥；Z0 是参数 |

## Claude CG-007 W7：想法 T 的两种形式与脚手架；C6 审查力（AI 提案）；P 的两侧（2026-10-09）

> 授权同上节。本节只追加。工具链同 W4a 节；导入闭包 1,889 个模块。四个运行都经 `verify_cg001_run.py --rerun` 精确重放；目标内索引 §32。
> 读法：机器证明（有范围）。想法 T 的形式（观察者、接口、维度）与 C6 的“审查”定义是 AI 提案，待研究发起人裁定。依赖检查核对 21 个定理不经本项目的对角声明。

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-CG001-IDEA-T-C6-P-001` | `CG001-C-114`、`CG001-C-115`、`CG001-C-116` | `formal/claude-cg001/idea-t-c6-p/GodelQ/IdeaT.lean`、`C6Review.lean`、`PTwoSides.lean`、`QualificationW7.lean`（加 20 个逐字节复制的依赖模块；命题全文 `CLAIM.md`） | `verification/runs/20261009-CG001-IDEA-T-C6-P-01/`；exit 0，stderr 0 B；144 条公理报告只有三条标准公理；精确重放一致 | `KERNEL_ACCEPTED_WITH_SCOPE / GOAL_LOCAL_INDEXED` |
| `MP-CG001-IDEA-T-C6-P-NEG-001` | `CG001-C-114`（负控制） | `formal/claude-cg001/idea-t-c6-p/GodelQ/Negative/WrongLimitDecoder.lean` | `verification/runs/20261009-CG001-IDEA-T-C6-P-NEG-01/`；exit 1 | `NEGATIVE_CONTROL_REJECTED`：接口上的碰撞确实被用到 |
| `MP-CG001-IDEA-T-C6-P-NEG-002` | `CG001-C-115`（负控制） | `formal/claude-cg001/idea-t-c6-p/GodelQ/Negative/WrongCompleteReview.lean` | `verification/runs/20261009-CG001-IDEA-T-C6-P-NEG-02/`；exit 1 | `NEGATIVE_CONTROL_REJECTED`：有效性确实被用到 |
| `MP-CG001-IDEA-T-C6-P-NEG-003` | `CG001-C-116`（负控制） | `formal/claude-cg001/idea-t-c6-p/GodelQ/Negative/WrongRealP1.lean` | `verification/runs/20261009-CG001-IDEA-T-C6-P-NEG-03/`；exit 1 | `NEGATIVE_CONTROL_REJECTED`：语义 P₁ 的成立确实依赖量子化 |

| Claim ID | 精确主张 | 状态 | 证据 | 禁止外推 |
|---|---|---|---|---|
| CG001-C-114 | 经接口 π 确认维度 D：π 压平 D ⟹ 无可靠完备观察者；D 不可枚举 ⟹ 每个可靠可枚举观察者漏点不可枚举、无穷，可严格加细而仍漏；可靠完备可枚举的观察者存在 ⟺ `FiberConstant π D ∧ REPred D`；停机维度纤维恒定而无此观察者；𝗭𝗙𝗖 的“永不停机”漏点不可枚举、无穷；`limUnder` 接口判不了“有限阶段取到” | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEXED / AI_PROPOSED_FORMAL_SHAPE` | run `20261009-CG001-IDEA-T-C6-P-01`（`qual_C114`）；负控制 `-NEG-01` | 不是“一切不完备都是维度缺失”；只在“接口 + 维度”的形状下 |
| CG001-C-115 | `Adequate d := Arrives d ↔ ∃ n, position d n = 1`；`¬ Adequate d ↔ ¬ Done d`；每个有效、可靠的 `Review` 都不完备；𝗭𝗙𝗖 有一个 `¬ Adequate` 的跑者，其停机句与永不停机句都不可证；对任一 ℒₛₑₜ 公式 Φ，若 `𝗭𝗙𝗖 ⊢ neverS Φ ⌜d⌝ → ¬ Adequate d`，则 `{d ∣ ¬ Adequate d ∧ 𝗭𝗙𝗖 ⊬ neverS Φ ⌜d⌝}` 无穷且不可枚举 | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEXED / AI_PROPOSED_DEFINITION` | run `20261009-CG001-IDEA-T-C6-P-01`（`qual_C115`）；负控制 `-NEG-02` | 审查定义待裁定；𝗭𝗙𝗖 的审查句经 Lean 元层等价取作停机句；ℒₛₑₜ 到达句是 W5 |
| CG001-C-116 | 有 `F x ∧ ¬ O x` 则无 `P1Rule Acc F ∧ OriginSound Acc O`；`P1Rule ∧ FormalSound ∧ ¬ REPred F ⟹ ¬ REPred Acc`；ℝ 每点 `¬ SemanticP1`，格点上成立；跑者族上二者都成立；`LooseRunnerTheory` 上 `A ↔ P ↔ CompletionSubstitution`；有效理论 `¬ A`（一条经 C-94，一条不经对角点）；真值理论有 A 与 P 而不可枚举 | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEXED` | run `20261009-CG001-IDEA-T-C6-P-01`（`qual_C116`）；负控制 `-NEG-03` | “现实是量子化的”未证；“社区实际采用 P₁”是来源层；A ⟺ P 对 𝗭𝗙𝗖 本身两边都假 |

## Claude CG-007 W5：跑者的到达句——𝗭𝗙𝗖 逐个证明它与永不停机句等价（2026-10-09）

> 授权同上节。本节只追加。工具链同 W4a 节；导入闭包 1,889 个模块。三个运行都经 `verify_cg001_run.py --rerun` 精确重放；目标内索引 §33。
> 读法：机器证明（有范围）。支付 CG001-C-101 的参数 `harr`，对象是新的停机公式 ΦS；对旧的不透明公式 ΦH 不声称。到达句是算术写法，实数的读法在 Lean 元层。

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-CG001-GODEL-Q-ZFC-RUNNER-ARRIVAL-001` | `CG001-C-117`、`CG001-C-118` | `formal/claude-cg001/godel-q-zfc-runner-arrival/GodelQ/ZFC/ArrivalArith.lean`、`ArrivalZFC.lean`、`QualificationArrival.lean`（加 21 个逐字节复制的依赖模块；命题全文 `CLAIM.md`） | `verification/runs/20261009-CG001-GODEL-Q-ZFC-RUNNER-ARRIVAL-01/`；exit 0，stderr 0 B；139 条公理报告只有三条标准公理；精确重放一致 | `KERNEL_ACCEPTED_WITH_SCOPE / GOAL_LOCAL_INDEXED` |
| `MP-CG001-GODEL-Q-ZFC-RUNNER-ARRIVAL-NEG-001` | `CG001-C-118`（负控制） | `formal/claude-cg001/godel-q-zfc-runner-arrival/GodelQ/Negative/WrongArrivalOldPhi.lean` | `verification/runs/20261009-CG001-GODEL-Q-ZFC-RUNNER-ARRIVAL-NEG-01/`；exit 1 | `NEGATIVE_CONTROL_REJECTED`：等价依赖到达句与停机公式来自同一个 `stopF` |
| `MP-CG001-GODEL-Q-ZFC-RUNNER-ARRIVAL-NEG-002` | `CG001-C-118`（负控制） | `formal/claude-cg001/godel-q-zfc-runner-arrival/GodelQ/Negative/WrongHaltingRunnerArrives.lean` | `verification/runs/20261009-CG001-GODEL-Q-ZFC-RUNNER-ARRIVAL-NEG-02/`；exit 1 | `NEGATIVE_CONTROL_REJECTED`：到达句区分停与不停 |

| Claim ID | 精确主张 | 状态 | 证据 | 禁止外推 |
|---|---|---|---|---|
| CG001-C-117 | θ := `(codeOfPartrec' stopFun)/[‘1’, #0, #1]` 是 Σ1 的，ℕ 里恰是 `stopB`；`stopF e k := ∃ i ≤ k, θ e i` 在每个 𝗣𝗔⁻ 模型里单调；每个 𝗣𝗔⁻ 模型里 `arrF e ↔ ¬ haltsF e`；`remaining d n ≤ (1/2)^K ↔ K ≤ n ∧ ∀ i < K, ¬ DoneBy d i`；`Arrives d ↔ ∀ K ∃ N ∀ n ≥ N, remaining d n ≤ (1/2)^K`；ℕ 里 `arrF ⌜d⌝ ↔ Arrives d` | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEXED` | run `20261009-CG001-GODEL-Q-ZFC-RUNNER-ARRIVAL-01`（`qual_C117`） | 𝗭𝗙𝗖 内部没有构造实数 |
| CG001-C-118 | ∀ a，`arrS a ≠ neverS ΦS a ∧ 𝗭𝗙𝗖 ⊢ arrS a 🡘 neverS ΦS a`；`Universe ⊧ arrS ⌜d⌝ ↔ Arrives d`；`𝗭𝗙𝗖 ⊢ haltsS ΦS ⌜e⌝ ↔ Done e`；存在到达的跑者，𝗭𝗙𝗖 每一刻确认尚未停而 `𝗭𝗙𝗖 ⊬ arrS ⌜d⌝`；`¬ AGeneral`、`¬ OmegaClosed`；对角过程三句都不可证；`{d ∣ ¬ Adequate d ∧ 𝗭𝗙𝗖 ⊬ arrS ⌜d⌝}` 无穷且不可枚举 | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEXED` | run `20261009-CG001-GODEL-Q-ZFC-RUNNER-ARRIVAL-01`（`qual_C118`）；负控制 `-NEG-01`、`-NEG-02` | 对旧的 ΦH 不声称；一致与可靠经 `Universe` |

## Claude CG-007 W4b：翻译可计算；Z0 的影子形式不再带前提（2026-10-09）

> 授权同上节。本节只追加。工具链同 W4a 节；导入闭包 1,893 个模块。三个运行都经 `verify_cg001_run.py --rerun` 精确重放；目标内索引 §34。
> 读法：机器证明（有范围）。支付 CG001-C-111 的阻塞引理；CG001-C-103 的两条前提都成为定理。结论是“𝗭𝗙𝗖 证明不了它的算术影子（经 Craig 公理化）一致性句的翻译”；读成“𝗭𝗙𝗖 证明不了 Con(𝗭𝗙𝗖)”还差证明的内部翻译（W8）。

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-CG001-GODEL-Q-ZFC-Z0-TRANSLATE-001` | `CG001-C-119`、`CG001-C-120` | `formal/claude-cg001/godel-q-zfc-z0-translate/GodelQ/ZFC/InternalTranslate.lean`、`TranslateRE.lean`、`QualificationTranslate.lean`（加 21 个逐字节复制的依赖模块；命题全文 `CLAIM.md`） | `verification/runs/20261009-CG001-GODEL-Q-ZFC-Z0-TRANSLATE-01/`；exit 0，stderr 0 B；106 条公理报告只有三条标准公理；精确重放一致 | `KERNEL_ACCEPTED_WITH_SCOPE / GOAL_LOCAL_INDEXED` |
| `MP-CG001-GODEL-Q-ZFC-Z0-TRANSLATE-NEG-RE-001` | `CG001-C-120`（负控制） | `formal/claude-cg001/godel-q-zfc-z0-translate/GodelQ/Negative/WrongZ0WithoutRE.lean` | `verification/runs/20261009-CG001-GODEL-Q-ZFC-Z0-TRANSLATE-NEG-RE-01/`；exit 1 | `NEGATIVE_CONTROL_REJECTED`：没有内部翻译就没有 `Sh.RE`，C-110 一条不够 |
| `MP-CG001-GODEL-Q-ZFC-Z0-TRANSLATE-NEG-DOMAIN-001` | `CG001-C-119`（负控制） | `formal/claude-cg001/godel-q-zfc-z0-translate/GodelQ/Negative/WrongTranslateNoDomain.lean` | `verification/runs/20261009-CG001-GODEL-Q-ZFC-Z0-TRANSLATE-NEG-DOMAIN-01/`；exit 1 | `NEGATIVE_CONTROL_REJECTED`：量词情形核对了 ω 限制 |

| Claim ID | 精确主张 | 状态 | 证据 | 禁止外推 |
|---|---|---|---|---|
| CG001-C-119 | 在 𝗜𝚺₁ 的每个模型 V 中，`iVE`、`iT` 是 𝚺₁ 可定义的函数（`iVEDef`、`iTDef`），且对每个闭项 t、每个算术公式 φ：`iVE n ⌜t⌝ = ⌜varEqual t⌝`、`iT n ⌜φ⌝ = ⌜arithTrln.translate φ⌝`；ℕ 里 `iT 0 (encode σ) = encode σᵗ`；`Computable (fun σ : ArithmeticSentence ↦ arithTrln.translate σ)` | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEXED` | run `20261009-CG001-GODEL-Q-ZFC-Z0-TRANSLATE-01`（`qual_C119`）；负控制 `-NEG-DOMAIN-01` | `iT_quote` 是对具体公式的元层定理，不是 𝗜𝚺₁ 内部的一句断言 |
| CG001-C-120 | `REPred (fun σ ↦ 𝗭𝗙𝗖 ⊢ σᵗ)`；`Sh.RE`；`𝗜𝚺₁ ⪯ Sh`；`𝗭𝗙𝗖 ⊬ (Sh.craig.consistent)ᵗ`；`Sh ⊬ Sh.craig.consistent`：都不带前提 | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEXED` | run `20261009-CG001-GODEL-Q-ZFC-Z0-TRANSLATE-01`（`qual_C120`）；负控制 `-NEG-RE-01` | 不是“𝗭𝗙𝗖 ⊬ Con(𝗭𝗙𝗖)”的内部形式（还差 𝗜𝚺₁ ⊢ Con(𝗭𝗙𝗖) → Con(Sh.craig)）；`Sh` 一致经 `Universe` |

## Claude CG-007 W8：Z0 的内部化只差一条引理；其余前提全部成为定理（2026-10-09）

> 授权同上节。本节只追加。工具链同 W4a 节；导入闭包 1,893 个模块。一个主运行经 `verify_cg001_run.py --rerun` 精确重放；目标内索引 §35。**接手说明**：本单元原由 Claude Opus 5.5 会话 d58e0c0d 推进，停在 `godel-q-zfc-z0-full` 包的开发构建（两处编译错误：`modus_ponens_sentence` 的理论参数、`FFL.Semantics.Iff.models_iff` 这个不存在的常数名）。Codex 会话修复这两处机械错误后完成本单元，未改动其数学设计。
>
> 读法：机器证明（有范围）。显式可证性谓词 `𝔅Z(x) := Provable 𝗭𝗙𝗼 (iT 0 x)` 成为 `Provability 𝗜𝚺₁ Sh`，D1、D2、一致性句等价、Σ1 层级与 D3 在 ℕ 中的正对照都是定理。把 C-120 读成“𝗭𝗙𝗼 证明不了 Con(𝗭𝗙𝗼)”所差的最后一步被固定成**一条** Lean 命题（`zfcTr_D3_internalize`，带未证标记，不是收据源）；它一旦成立，完整形式立即随之成立。本包没有负控制运行，理由见包 `CLAIM.md` §3。

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-CG001-GODEL-Q-ZFC-Z0-FULL-001` | `CG001-C-121`、`CG001-C-122` | `formal/claude-cg001/godel-q-zfc-z0-full/GodelQ/ZFC/Z0Full.lean`（加 21 个逐字节复制的依赖模块；命题全文 `CLAIM.md`；阻塞引理在 `GodelQ/ZFC/Z0Blocked.lean`，**不在**本运行源清单） | `verification/runs/20261009-CG001-GODEL-Q-ZFC-Z0-FULL-01/`；exit 0，stderr 0 B，71.7 秒；112 条公理报告只有三条标准公理；30 个源文件哈希固定 | `KERNEL_ACCEPTED_WITH_SCOPE / GOAL_LOCAL_INDEXED` |

| Claim ID | 精确主张 | 状态 | 证据 | 禁止外推 |
|---|---|---|---|---|
| CG001-C-121 | `TrProvable x := Provable 𝗭𝗙𝗼 (iT 0 x)`，其 Σ1 公式 `trProv`；`zfcTr : Provability 𝗜𝚺₁ Sh` 且 `V ⊧ zfcTr σ ↔ Provable 𝗭𝗙𝗼 ⌜σᵗ⌝`；D1（`iT_quote` + `internalize_provability`）；D2 = HBL2（`modus_ponens_sentence`）；`𝗜𝚺₁ ⊢ zfcTr.con 🡘 𝗭𝗙𝗼.consistent`；`zfcTr σ` 是 𝚺₁ 句；正对照：ℕ 中 D3 成立 | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEXED` | run `20261009-CG001-GODEL-Q-ZFC-Z0-FULL-01`（`zfcTr`、`zfcTr_HBL2`、`zfcTr_con_iff`、`zfcTr_sigma1`、`zfcTr_D3_standard`） | 谓词是“𝗭𝗙𝗼 证明 x 的翻译”，不是 `Sh.craig` 那个经选择得到的 Σ1 句；D3 的正对照不覆盖非标准模型 |
| CG001-C-122 | 给定阻塞引理 `zfcTr_D3_internalize`（𝗜𝚺₁ 的每个模型 V 中 `Provable 𝗭𝗙𝗸 ⌜σᵗ⌝ → Provable 𝗭𝗙𝗸 ⌜(zfcTr σ)ᵗ⌝`），则 `𝗭𝗙𝗸 ⊬ arithTrln.translate (𝗭𝗙𝗸.consistent)`，且 `Sh ⊬ 𝗭𝗙𝗸.consistent` | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEXED / CONDITIONAL_ON_BLOCKING_LEMMA` | run `20261009-CG001-GODEL-Q-ZFC-Z0-FULL-01`（`zfc_z0_full_of_D3_internalize`，无未证标记，只以待证引理为显式前提） | 阻塞引理本身未证；不声称“𝗭𝗙𝗸 ⊬ Con(𝗭𝗙𝗸)”已证；不带前提的仍是 C-120 的影子形式 |

## Claude CG-007 W9：八个 git worktree 的形式化资产在 `dev` 上全部有可重放收据（2026-10-09）

> 授权：研究发起人 2026-10-08“按照你的想法进行优先级安排，完成后续所有‘形式化和机器证明’工作”，以及本轮“必须 Cover 所有值得保留的 8 个当初的 git worktree 留下的工作方向”。本节只追加。
> 工具链：Lean 4 core v4.34.1（二进制与版本行按字节与 SHA-256 固定），**无 Mathlib、无项目库**；禁网沙盒内按绝对路径调用 pinned 二进制，不经过 elan 代理。18 个源逐个与 `origin/dev-02`、`origin/dev-03`、`origin/dev-04` 原件比对 SHA-256 后复制。
> **身份**：本机重放与来源固定，不是新数学。所有定理在各自分支上已由 GPT 各线证明。逐线覆盖判定见包 `CLAIM.md` §1。

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-CG001-BRANCH-FORMALIZATION-COVERAGE-001` | `CG001-C-123`、`CG001-C-125`、`CG001-C-126` | `formal/branch-formalization-coverage/GodelQ/`：16 个正源（`ObservationBoundary`、`MetaObservationConsistency`、`MetaSubtheoryAudit`、`CompletionPromotionTension`、`CompletionSubstitutionProfile`、`CommunityObservationPolicy`、`ActualPolicyWitness`、`ActualPolicyEvidenceFrontier`、`SepCompletionPromotion`、`SequentialCompletionContracts`、`UouCompletionPromotion`、`ActualQPolicy`、`ZFCObservationLanguage`、`ZFCCompletionPolicyUniformity`、`ZFCUnpaidCompletionPromotion`、`ZFCMembershipLanguageBoundary`；命题全文 `CLAIM.md`） | `verification/runs/20261009-CG001-BRANCH-FORMALIZATION-COVERAGE-06/`；exit 0；165 条公理报告全部无公理 | `KERNEL_ACCEPTED_WITH_SCOPE / GOAL_LOCAL_INDEXED / LOCAL_REPLAY_NOT_NEW_MATHEMATICS` |
| `MP-CG001-BRANCH-FORMALIZATION-COVERAGE-NEG-001` | `CG001-C-124`（负控制） | `formal/branch-formalization-coverage/GodelQ/WrongMetaSubtheoryAudit.lean`、`WrongCompletionPromotionTension.lean` | `verification/runs/20261009-CG001-BRANCH-FORMALIZATION-COVERAGE-NEG-02/`；exit 1，`assumption` 失败 | `NEGATIVE_CONTROL_REJECTED`：受控反例确实在预定点被拒 |

| Claim ID | 精确主张 | 状态 | 证据 | 禁止外推 |
|---|---|---|---|---|
| CG001-C-123 | dev-02/03/04 三条线留在分支上的 16 个 Lean-core 正源，在 pinned Lean 4.34.1、禁网沙盒下全部编译通过，且每个文件与其分支原件逐字节相同 | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEXED / LOCAL_REPLAY` | run `-04` | 不读成“这些命题被独立复核”；数学内容与范围仍以各分支 `CLAIM.md` 为准 |
| CG001-C-124 | 同一环境下 2 个负控制源都在预定点被内核拒绝（`WrongMetaSubtheoryAudit` 的 `assumption` 失败） | `NEGATIVE_CONTROL_REJECTED / GOAL_LOCAL_INDEXED` | run `NEG-01` | 不证明 ZFC 或 HoTT 的任何性质 |
| CG001-C-125 | 16 个正源 165 条公理报告全部为“does not depend on any axioms”；stdout/stderr/exit 与源码哈希、二进制哈希一起固定 | `EVIDENCE_INTEGRITY_PINNED / GOAL_LOCAL_INDEXED` | run `-04` | 无公理不等于命题为真，只等于这些 Lean core 定理不依赖额外公理 |
| CG001-C-126 | 八个工作树方向的形式化覆盖完整：dev-01 与 dev-09 的已并入包沿用既有 `dev` 收据（`4a3535d9`、`20261008-S7C-IMPORT-REPLAY.json`）；dev-02/03/04 由本包补齐；dev-06/07/08 无形式包判为不适用；dev-09 的 `external-foundation-incompleteness`（D09-C-369）判为本机不可重放，保持 `SOURCE_REPORTED_NOT_REPLAYED` | `COVERAGE_COMPLETE_WITH_SCOPE / GOAL_LOCAL_INDEXED` | run `-04` + `dev` 既有收据 | dev-09 外部 Foundation 包的运行依赖一个已不存在的 `/tmp` 检出，缺的是本机 toolchain，不是它的正确性；不读成八条线的研究已完成；`GeometricCompletion.lean` 依赖 Mathlib，本包未含其构建树，其分支收据保持原样 |

## CG-007 W9b：分支实分析控制在本机 Mathlib 上重放（2026-10-09，Codex 会话）

Package 表：

| Package ID | Claim IDs | 源码 | 证据 | 判词 |
|---|---|---|---|---|
| `MP-CG001-GODEL-Q-GEOMETRIC-COMPLETION-001` | `CG001-C-127` | `formal/claude-cg001/godel-q-geometric-completion/GodelQ/GeometricCompletion.lean`（逐字节复制自 `origin/dev-03`，与 `origin/dev-04` 同路径文件逐字节相同）；命题全文与分支禁止外推见该包 `CLAIM.md` | `verification/runs/20261009-CG001-GODEL-Q-GEOMETRIC-COMPLETION-01/`；exit 0，stderr 0 B；8 条公理报告全为 propext、Classical.choice、Quot.sound；`--rerun` `EXACT_EXIT_STDOUT_STDERR_MATCH` | `KERNEL_ACCEPTED_WITH_SCOPE / GOAL_LOCAL_INDEXED / LOCAL_REPLAY_NOT_NEW_MATHEMATICS` |

Claim 表：

| Claim ID | 精确主张 | 状态 | 证据 | 禁止外推 |
|---|---|---|---|---|
| CG001-C-127 | 分支的实分析控制 `GeometricCompletion.lean` 在本机 Mathlib `5ed29652` 与 pinned Lean 4.34.0、禁网沙盒下编译通过：几何部分和 `1-(1/2)^n` 在每个自然数阶段严格小于 1、永不到达 1、在实数拓扑中趋于 1；`hasLimitOutcome` 与 `hasFiniteStageEndpoint` 两个形式谓词对该具体序列不等价；闭区间 `[0,1]` 时间域中有终端参数 | `FORMAL_CHECKED_WITH_SCOPE / GOAL_LOCAL_INDEXED / LOCAL_REPLAY` | run `20261009-CG001-GODEL-Q-GEOMETRIC-COMPLETION-01` | 不读成“这些命题被独立复核”，数学内容与范围仍以分支自己的 `CLAIM.md` 为准；不读成几何完成性或芝诺问题被解决；不声称 Mathlib 本体进入 CG-007 其它包的 pin（仅本包含它，且本包不用 Foundation）；不是 HoTT 路径证明，也不是 ZFC 元理论陈述 |

**这一节对 §36 的修正**：上一轮把 `GeometricCompletion.lean` 记为“本机 toolchain pin 未含 Mathlib 构建树，故不在覆盖包内”。本机 `/Volumes/D/HoTT-toolchain-cache/` 下有完整的 Mathlib `5ed29652` 构建（2329 个 olean，含 `Mathlib/Analysis/SpecificLimits/Normed.olean`）；CG-007 既有 pin 只列 8 个依赖包而不列 Mathlib 本体根，是 pin 覆盖面的选择，不是能力缺失。因此 §36 的该条保留意见被本节取代。
