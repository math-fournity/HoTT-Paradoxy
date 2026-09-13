# 形式化核心

<!-- math-proof-source-contract:v1
authoritative_source_root: HoTT/formal
run_root: HoTT/verification/runs
claim_index: HoTT/CLAIM_EVIDENCE_MATRIX.md
-->

本目录只机器检查审计报告中明确、窄化后的数学命题；不把解释性标题当成形式定理。

从 `MATH_PROOF_BEFORE_DELIVERY_V1` 生效后，当前 AI 要交付为已成立的数学结论，其精确证明源码必须先进入本目录。新证明优先使用 `formal/<topic-or-claim-id>/`，保存形式命题、证明、项目/构建文件和锁定依赖身份；实际运行原件进入 `../verification/runs/<run-id>/`，唯一快速索引进入 `../CLAIM_EVIDENCE_MATRIX.md`。聊天代码块、内存变量和 `/tmp` 中的唯一副本均不构成证明资产。

当前 **17 个冻结 package** 的 source/run/index 已由 `../verification/PROOF_VERSION_CLOSURE.json` 固定到 commit `d3dfb0e1869f5f05527f23ef4cb05dc95352eb10`；其后的两个 package（`MP-VERIFICATION-EVENT-001`、`MP-ERCF3-T3-JOINT-001`）走同一 registry 的 `later_packages` **追加登记**（要求源码/工具链/run 已进 Git、`exit_code = 0`、`index_status = INDEXED_IN_CLAIM_EVIDENCE_MATRIX`）。Git closure 不改写历史 RUN.json 或 frozen matrix 行，也不扩大任何命题范围。

## 文件

- `truncation-no-recovery/NoCanonicalPoint.agda`：`MP-NOCANONICAL-001`；独立 Cubical/Type₀ 证明 unlabeled 二元素呈现不存在统一选点（C-142–C-148）。这是与 agda-unimath no-section 现象的非正式对照，不是两个形式规格的已证等价，也不是外部源码重放；final run 未导入 bridge `NoCanonicalFinite.agda`。
- `truncation-no-recovery/TruncationNoRecovery.agda`：`MP-TRUNC-NORECOVERY-001`；集合值截断不可恢复、完成候选否定形式与 `isFinSet` 形状接口边界（C-134–C-141）。
- `agda-unimath/hott-z/NoCanonicalPoint.agda`：`MP-UNIMATH-NOSECTION-REPLAY-001` / C-05；在固定 agda-unimath@`7b81411d…` 下真实重放该派生文件及 485 个外部依赖模块。`foundation.global-choice` 不在保存 run 闭包；其 `no-global-choice` 当前只是 source-inspected。
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
- `lean/TwoEvent.lean`：二元素交换与方向丢失的独立有限模型。
- `build.sh`：校验关键上游文件哈希后运行 Agda，并在 Lean 可用时运行第二实现。
- `verification-event/VerificationEvent.agda`：`MP-VERIFICATION-EVENT-001`；外部独立来源的有限验证事件模型在项目内重放——保留时标的历史核查可完成（`C-152`）、固定过去→当前改写不存在（`C-153`）、完全阶段擦除不保真（`C-154`）、保阶段正控制（`C-155`）、条件性 Moore/Fitch 核（`C-156`）；判词 `VERIFICATION_EVENT_STAGE_BOUNDARY_WITH_POSITIVE_CONTROL`，**未构成 HoTT 自身非现实性实例**。
- `ercf3-t3/JointRecursion.agda`：`MP-ERCF3-T3-JOINT-001`；ERCF-3 T3 第十四脉冲——显式共享判定下码级修正替换与语法级替换一致（`C-157`）、**原始逐出现判定的项层恒等式** `substFixT ≡ codeT ∘ substT`（`C-158`，N34 记录的剩余义务）、修正后的公式层恒等式（`C-159`，修正 `CodeStoreFixF` 的 `all` 影子分支双重编码）。同目录 `ObjectSyntax.agda`–`DecisionParam.agda` 是 S067–S080 的脉冲谱系（builtins-only，`PULSE_EVIDENCE_ONLY`）。**ERCF-3 本体保持 `GATED`**：无证明谓词表示性、反射或对角不动点。
- `ercf3-t3/DecodingFence.agda`：`MP-ERCF3-T3-DECODING-001`；T3 第十五脉冲——编码的**可解码性/单射性围栏**：`codeT (var 2) ≡ codeT (num 0)` 而两项不同，故不存在单射解码器（`C-160`）；同一碰撞提升到公式层（`C-161`）；数字片段单射为正控制（`C-162`）。结论：`ObjectSyntax` 记录的 decodability/injectivity 义务**不能由当前编码满足**，需要标签不相交或列表/配对编码的修复；修复是下一个有界脉冲。**ERCF-3 保持 `GATED`**。
- `ercf3-t3/CodingRepair.agda`：`MP-ERCF3-T3-REPAIR-SPEC-001`；T3 第十六脉冲——**编码修复规格**：通用引理"有往返解码器 ⇒ 编码单射"（`C-164`）；结构化树编码 `encT/decT` 往返成立故单射（`C-163`，正控制）；当前 `codeT` **不存在解码器**（`C-165`）。修复义务由此固定为"给出 Nat 值编码 + 解码器 + 往返证明"：结构半已完成，算术半（标签不相交或列表编码）是下一有界脉冲。**ERCF-3 保持 `GATED`**。
- `ercf3-t3/ArithmeticTags.agda`：`MP-ERCF3-T3-ARITH-TAGS-001`；T3 第十七脉冲——**修复编码的算术半第一片**：偶/奇标签算术（`double` 单射、`double n ≢ odd m`，`C-166`）；var/num 片段 Nat 值编码 `codeAtom`（`2n`/`2n+1`）**单射**（`C-167`）。`C-168` 的机器命题只是 **`double` 下 `1` 无原像**；`codeAtom` 实际满射（`C-184`–`C-185`）。修复后 `codeT'`/`codeF'` 的像外输入由 `C-186`–`C-187` 单独刻画。**ERCF-3 保持 `GATED`**。
- `ercf3-t3/BitCoding.agda`：`MP-ERCF3-T3-BIT-CODING-001`；T3 第十八脉冲——**修复编码的算术半第二片（位级底座）**：最低位/折半数字算术（`parity`/`half`/`twice`，`C-169`）；捆绑编码 `codeBits` 与抽取 `unbits` 的两侧引理（`C-170`）与**已知长度**的往返 `unbits (LEN bs) (codeBits bs) ≡ bs`（`C-171`）；码支配自身长度 `suc (LEN bs) ≤ codeBits bs`，故解析器燃料可取自码本身（`C-172`）。剩余：符号层（自定界索引位 + 构造子标签）+ 带缺省分支的解析器 + 像上往返。**ERCF-3 保持 `GATED`**。
- `ercf3-t3/StreamingParser.agda`：`MP-ERCF3-T3-STREAMING-PARSER-001`；T3 第十九脉冲——**符号层 + 流式解析器 + 修复后的 Nat 值编码**：自定界一元索引层（`C-173`）；符号层 `bits`/`BLEN` 与燃料精确的流式解析器 `run`（显式框架栈解决顺序消费，`C-174`）；长度对账、界即和分解与 `unbits` 多余燃料分解（`C-175`）；`codeT' = codeBits ∘ bits` 带全解码器 `dec`、往返 `dec (codeT' t) ≡ t`，故由 C-164 单射（`C-176`）——**在编码层闭合 `CodingRepair` 的修复义务（C-163/C-164/C-165）**。仍未做：`codeF` 的对应修复、对象层替换对齐、P 表示性/反射/对角不动点。**ERCF-3 保持 `GATED`**。
- `ercf3-t3/FormulaCoding.agda`：`MP-ERCF3-T3-FORMULA-CODING-001`；T3 第二十脉冲——**修复编码的公式层（复用项层解码器）**：公式符号层 `bitsF`/`STEPS` 与迭代数精确的流式 `run`（`C-177`）；`=f` 的 Tm 子项交给项层解析器，燃料取剩余位数（`C-178`）；长度对账 `STEPS φ ≤ LEN (bitsF φ)`（`C-179`）；`codeF' = codeBits ∘ bitsF` 带全解码器 `decF`、往返 `decF (codeF' φ) ≡ φ`，故单射（`C-180`）。仍未做：公式层与对象层替换对齐、`⌜·⌝` 算术化、P 表示性/反射/对角不动点。**ERCF-3 保持 `GATED`**。
- `ercf3-t3/RepairedSyntax.agda`：`MP-ERCF3-T3-REPAIRED-SYNTAX-001`；T3 第二十一脉冲——**修复编码之上的替换一致与引用**：码级替换定义为解码—替换—编码，于是"码级替换 ≡ 语法级替换"在 `Tm`（`C-181`）与 `Fml`（`C-182`）两层都成为推论（旧编码需要 C-157–C-159 的联合递归）；引用 `⌜φ⌝'` 单射、对角实例及其码可由码级替换算出（`C-183`）。诚实边界：这些码级函数经解码器定义，**不**主张对象理论可表示它们。仍未做：表示性、反射、对角不动点（门 B）。**ERCF-3 保持 `GATED`**。
- `ercf3-t3/C168Countercheck.agda`：`MP-ERCF3-T3-C168-COUNTERCHECK-001`（独立审计吸收）：用完整传递闭包重放外部审计的反证——`codeAtom (anum zero) ≡ suc zero`（`C-184`）与 `codeAtom` **满射**（`C-185`）。它纠正 C-168 的叙述对象错配（该引理谈的是 `double`），不改原行与原 run 收据。
- `ercf3-t3/CodingImage.agda`：`MP-ERCF3-T3-CODING-IMAGE-001`（独立审计吸收）：证明 `codeT'`（`C-186`）与 `codeF'`（`C-187`）的像都不含 `1`。因此以全部 `Nat` 为输入的解码规格必须定义像外行为；当前 `dec`/`decF` 实现中的缺省分支在输入 `1` 时可达。

## 锁定环境

下列 `88cfce0…` 是历史 `build.sh` 路线的锁定身份；S088 的当前外部重放使用另一条显式 package：commit `7b81411d9f60afec359d29ed1e4edf43f4711c8a`、工具链身份 `agda-unimath/UNIMATH_TOOLCHAIN.json`、final run `../verification/runs/20260913-MP-UNIMATH-NOSECTION-REPLAY-02/`。两者不得混写成一个当前版本。

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
