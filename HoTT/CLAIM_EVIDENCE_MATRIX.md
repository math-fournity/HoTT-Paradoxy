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
