# 形式化核心

<!-- math-proof-source-contract:v1
authoritative_source_root: HoTT/formal
run_root: HoTT/verification/runs
claim_index: HoTT/CLAIM_EVIDENCE_MATRIX.md
-->

本目录只机器检查审计报告中明确、窄化后的数学命题；不把解释性标题当成形式定理。

从 `MATH_PROOF_BEFORE_DELIVERY_V1` 生效后，当前 AI 要交付为已成立的数学结论，其精确证明源码必须先进入本目录。新证明优先使用 `formal/<topic-or-claim-id>/`，保存形式命题、证明、项目/构建文件和锁定依赖身份；实际运行原件进入 `../verification/runs/<run-id>/`，唯一快速索引进入 `../CLAIM_EVIDENCE_MATRIX.md`。聊天代码块、内存变量和 `/tmp` 中的唯一副本均不构成证明资产。

## 文件

- `cauchy-modulus/CauchyModulus.agda`：`MP-CAUCHY-MODULUS-001`；Cauchy modulus 边界：按极限值取商保留 limit（`C-129`）；两个 modulus 不同的常量真序列表示被识别而 modulus 不同（`C-130`）；不存在从商统一恢复给定 modulus 的函数（`C-131`）；把 modulus 纳入同一性判据后可以下降（`C-132`，正控制）；细化关系不再识别两表示（`C-133`）。判词 `CAUCHY_MODULUS_BOUNDARY_WITH_POSITIVE_CONTROLS`。
- `sip-representation/SIPRepresentation.agda`：`MP-SIP-REPRESENTATION-001`；SIP/UA 替换许可的最小边界：点结构 `(Bool,true)` 与 `(Bool,false)` 由 `ua notEquiv` 识别（`C-124`）；签名外可观察量不同（`C-125`）；任意 `Str → Bool` 被识别强制为常数（`C-126`）；不存在统一恢复函数（`C-127`）；细化签名后投影恢复/区分两点（`C-128`，正控制）。判词 `SIP_REPRESENTATION_BOUNDARY_WITH_POSITIVE_CONTROL`。
- `partial-decision/PartialDecision.agda`：`MP-PARTIAL-DECISION-001`；strict 与 partial classifier 的最小原生边界：代表层 strict 分类器存在（`C-118`）、strict 区分 `now/later`（`C-119`）、不存在 strict `Q → Delay Bool` 扩展（`C-120`）、存在 up-to-≈ partial classifier `Q → D≈`（`C-121`，正控制）、不存在 strict `Q → Bool` 消费者（`C-122`）、代表层消费者区分 `a,b`（`C-123`）。判词 `PARTIAL_DECISION_BOUNDARY_WITH_POSITIVE_CONTROL`。
- `transition-lift/TransitionLift.agda`：`MP-TRANSITION-LIFT-001`；R036/R038 核心边界的原生 Cubical 升级：三状态过程终止正控制（`C-110`）、存在像自环与抽象无限路径（`C-111`）、`w,w,w` 无具体两步提升（`C-112`）、当前态提升函数不存在（`C-113`）、精确相容极限为空（`C-114`）、截断极限有元素（`C-115`）、比较映射无逆（`C-116`）、无严格下降纤维恒定等级（`C-117`）。判词 `TRANSITION_LIFT_BOUNDARY_WITH_POSITIVE_CONTROLS`，不是 HoTT 悖论。
- `partiality-race-timeout/OnlineCausality.agda`：`MP-ONLINE-CAUSALITY-001`；在线因果资格：时刻 0 无前视（`C-106`）、读第一个输入的正例（`C-107`）、第二个输入自时刻 1 起的正例（`C-108`）、完整知识 ≠ 在线资格的知识缺口（`C-109`）。
- `partiality-race-timeout/PathCertificate.agda`：`MP-PATH-CERTIFICATE-001`；R034 路径证书边界的原生核查：`ua` 路径按 `not` 计算（`C-100`）、截断命题性（`C-101`）、固定端点接口存在（`C-102`）、固定源与全宇宙统一迁移不可栖居（`C-103`、`C-104`）、路径版迁移存在（`C-105`）。真实 Cubical Path，不使用普通 Lean `Eq`。
- `partiality-race-timeout/CostFactorization.agda`：`MP-COST-FACTORIZATION-001`；同函数异时第一机器构造：`fast`/`slow k` 外延相同而成本不同（`C-96`）；裸函数类型上不存在可区分外延相等程序的谓词（`C-97`），故无从裸函数恢复成本的 consumer（`C-98`）；成本细化表示可恢复/可区分（`C-99`）。
- `partiality-race-timeout/GuardErasure.agda`：`MP-GUARD-ERASURE-001`；显式源演算（分阶段流）+ 显式忘却翻译下的阶段擦除判别：保更新律地擦除阶段 ⇔ 该律有不动点（`C-92`/`C-94`）；否定律被拒绝（`C-93`），振荡轨道阶段可观察（`C-95`）。细化 `self-contained/ZCore.agda` 的历史条件引理。
- `partiality-race-timeout/ContextCharacterization.agda`：`MP-CONTEXT-CHARACTERIZATION-001`；Bool 片段上上下文等价的完整刻画：`lt` 三分律（`C-89`）、一般严格时间分离（`C-90`）、`p ≡c q ↔ p ≡ q`（`C-91`）。代表相等即最细，故该片段内任何上下文扩展不能区分更多。
- `partiality-race-timeout/QuotientMonad.agda`：`MP-QUOTIENT-MONAD-001`；结果商 `Q A = Delay A / ≈` 的 canonical section（`C-84`）与商值 continuation 单子 `bindQQ`（`C-85`–`C-88`：代表层相容、单位律、代表层与商层关联律）。正面结构结果：本片段的商可分裂，无需选择公理。
- `partiality-race-timeout/ContextualEquivalence.agda`：`MP-CONTEXTUAL-EQUIV-001`；同一 delay 片段上的上下文等价层次：`≡c` 精化结果等价（`C-77`、`C-78`）并严格分离时序/发散/值（`C-79`–`C-82`）；结果等价严格粗于上下文等价（`C-83`）。判词 `REPRESENTATION_BOUNDARY`。
- `partiality-race-timeout/PartialityRaceTimeout.agda`：`MP-RACE-TIMEOUT-001`；在 Agda 2.8.0/Cubical v0.9 中机器核实 R041 的 partiality 操作闭包：`bind` 尊重结果等价并下降到集合商（`C-71`、`C-72`），`race`/`deadline` 不尊重该等价且商上无 race 选择子（`C-73`–`C-76`）。判词是 `REPRESENTATION_BOUNDARY`，不是 HoTT 悖论。
- `ercf-truncation-defense/TruncationDefense.agda`：`MP-ERCF-TRUNC-001`；在 Agda 2.8.0/Cubical v0.9 的原生 Path + squash-HIT 下证明命题截断的受保护 recursor、二重截断压平、Bool 输出恒定性与 point-preserving extraction 不可能性（`C-67`–`C-70`）。判词是 `DEFENSE_WORKS`，不是 HoTT 悖论。
- `ercf-factorization/ERCF.lean`：`MP-ERCF-001`；通用 `Type` 值因子化必要/充分条件、E₀ 正反控制、分离观察族与 identity 观察控制。Lean 4.33.1 final run 为 `../verification/runs/20260912-MP-ERCF-001-02/`，只证明 `C-59`–`C-66`，不使用 HoTT 特有规则。
- `self-contained/ZCore.agda`：表示因子化的必要条件、无免费富化、来源/方向有限反例、语境欠定和两个条件性固定点引理。
- `agda-unimath/hott-z/NoCanonicalPoint.agda`：对锁定 `agda-unimath` 定理的薄包装；名称刻意写成“无规范点”，不冒充完整时间序定理。
- `lean/TwoEvent.lean`：二元素交换与方向丢失的独立有限模型。
- `build.sh`：校验关键上游文件哈希后运行 Agda，并在 Lean 可用时运行第二实现。

## 锁定环境

- Agda：2.8.0。
- `agda-unimath` commit：`88cfce0ce195ae3b64a9e73e8ec744ae64b4006b`。
- 上游归档 SHA-256：`50ed8718a56820049eebf5ad86b619774ec0c23a9c5b3ca4a4447b3e70a785a6`。
- `2-element-types.lagda.md` SHA-256：`72f9ad29b6c24b84e1e06f10f701895783e7a56cfaedc1dc0d295dba3629c82e`。
- `agda-unimath.agda-lib` SHA-256：`d42bd31babacf7fced8aab84f499d9004a1cac5c3219dc7b360c56c23e9b6221`。

## 运行

```bash
AGDA=/path/to/agda \
AGDA_UNIMATH_ROOT=/path/to/agda-unimath-at-pinned-commit \
bash HoTT/formal/build.sh
```

不得把成功编译解释成以下命题：`HoTT ⊢ ⊥`、HoTT 无法编码时间、所有 HoTT 箭头均可逆，或
HoTT 作为数学基础已被推翻。机器证书的精确边界见 `../CLAIM_EVIDENCE_MATRIX.md`。

HoTT 特定命题必须使用匹配其 Path/univalence/HIT/truncation/judgmental computation 语义的原生 checker，或同时提供已机器证明的保真翻译。普通 Lean `Eq` 和有限程序测试只能证明其精确编码/有限命题，不能冒充原生 HoTT 或无限全称结论。完整交付合同见 `../../docs/quality/数学结论机器证明与证据留存规范.md`。
