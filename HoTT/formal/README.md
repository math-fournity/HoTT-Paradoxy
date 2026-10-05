# 形式化核心

<!-- math-proof-source-contract:v1
authoritative_source_root: HoTT/formal
run_root: HoTT/verification/runs
claim_index: HoTT/CLAIM_EVIDENCE_MATRIX.md
-->

本目录只机器检查审计报告中明确、窄化后的数学命题；不把解释性标题当成形式定理。

从 `MATH_PROOF_BEFORE_DELIVERY_V1` 生效后，当前 AI 要交付为已成立的数学结论，其精确证明源码必须先进入本目录。新证明优先使用 `formal/<topic-or-claim-id>/`，保存形式命题、证明、项目/构建文件和锁定依赖身份；实际运行原件进入 `../verification/runs/<run-id>/`，唯一快速索引进入 `../CLAIM_EVIDENCE_MATRIX.md`。聊天代码块、内存变量和 `/tmp` 中的唯一副本均不构成证明资产。

当前 **17 个冻结 package** 的 source/run/index 已由 `../verification/PROOF_VERSION_CLOSURE.json` 固定到 commit `d3dfb0e1869f5f05527f23ef4cb05dc95352eb10`；其后 package 走同一 registry 的 `later_packages` **追加登记**。截至 `C-249` 共登记 25 个 later package / 101 条 later claim；最新的 R1/R2/R3/R4、2LTT/LOPS/ITT 程序包仍是 `LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED`。Git closure 不改写历史 RUN.json 或 frozen matrix 行，也不扩大任何命题范围。

## 文件

- `zfc-actual-q-policy/`：`MP-ZFC-ACTUAL-Q-POLICY-001` / C-359 将用户提出的Q缺失、数学幻觉P、A/B和`ZFC-1`写成明确前提的Lean policy use-model；`MP-ZFC-ACTUAL-Q-HOTT-COUNTEREXAMPLE-001` / C-360在原生Cubical Agda中固定HoTT Q对“coarse completion→original finite halting”的P反例；`MP-ZFC-ACTUAL-Q-ZENO-LIMIT-CONTROL-001` / C-361在固定几何级数上证明极限不推出严格有限阶段Done，并保留闭连续时间端点正控制；C-362与C-363将 Norton/IEP 的 revised completion 来源合同和固定HoTT B分别写成相同的 completion-gap schema。它们不形式化bare ZFC或实际来源政策，详见目录`CLAIM.md`。

- `bare-zfc-q-precision/`：`MP-BARE-ZFC-Q-PRECISION-001` / C-364 以一个来源绑定的有限 completion-contract control 区分粗标准解答 view、OriginDone 与 completion bridge：同一粗 resolved view 不能决定 OriginDone 或支付 universal bridge；显式 contract view 与 code view 是正控制。它是 ZFC-supported Standard Solution application interface 的精度控制，**不**形式化 bare ZFC 本身，不主张 ZFC 不能编码过程或 ZFC 不一致，详见目录`CLAIM.md`。

- `external-foundation-incompleteness/`：`MP-FOUNDATION-INCOMPLETENESS-R3-001` / C-369 固定 Foundation Lean 的 first-order arithmetic 第一不完备性源码与 toolchain，重新构建 `Foundation.FirstOrder.Incompleteness.First`，检查含 `codeOfREPred`、quote、substitution 和 `Provable` 的 theorem exports，并通过缺 `Sigma₁` soundness 的负控制。它是 G0/R3 source calibration，不是 exact HoTT、bare ZFC acceptance 或现实过程完成证明。

- `external-cctt-r4/`：GZ-005 的 **非 kernel checker-evidence package**。冻结 `AndrasKovacs/cctt@3695c69e` 并实际重放 Nat/Path/Glue/`coe`/`hcom` 正例、hole、top-level recursion、类型错误和有界 `nf loop` 观察。它将 cctt CLI 的诊断性接受、process exit 和项目定义的 restricted profile 分开：类型错误仍可能 exit 0，hole/recursive input 仍可被诊断性接受，故只有 profile + 无 `ERROR` diagnostic + checked marker 的合取才构成受限 input contract。它不是形式定理、proof kernel、完整 proof relation、R4 的 Gödel实例或 bare ZFC 结论。

- `cubical-godel-fragment/`：`MP-CUBICAL-GODEL-FRAGMENT-001` / C-370–C-374。用 native Cubical Agda 机器检查项目定义的 `CCTTmini₀`：Nat、Path/refl、finite RawCert、structurally recursive checker 与携带 `Deriv` witness 的 `Checked` result；正例和两条拒绝控制均保存。它是对 cctt/redtt 共用 Nat/Path-refl 形状的受限 source-corresponding bridge，不是 full cubical calculus、upstream proof relation、Nat-valued Gödel编码、representability、fixed point 或 bare ZFC 结论。

- `cubical-godel-fragment/CCTTminiNat.agda`：`MP-CUBICAL-GODEL-NAT-CODING-001` / C-375–C-378。在同一个 `RawCert` 上构造 self-delimiting bit grammar、Nat code、total fallback decoder、image roundtrip 和 injectivity。Cubical Agda 接受其 precise declarations，但 run 保留 `UnsupportedIndexedMatch` warning，故只交付固定 coding 命题，不主张辅助 `≤-trans` 的 transport computation，也不交付 formula/proof predicate、representability、fixed point、full HoTT 或 bare ZFC 结论。

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
- `cubical-machine-halting/MachineHalting.agda`：`MP-CUBICAL-MACHINE-HALTING-001`；R1 固定机器校准：停机正控制（`C-188`）、固定循环程序在每个有限步均未终止（`C-189`）、不存在截断有限停机见证（`C-190`）。本次 Agda 检查正常结束；不推出通用不可判定性、Gödel 不完备性或 HoTT 非现实性悖论。
- `cubical-machine-halting/ProgramCode.agda`：`MP-CUBICAL-PROGRAM-CODE-001`；R2 第一薄层：有限指令表与总 decoder（`C-191`）、统一 bounded evaluator 及 R1 语义一致性（`C-192`）、停机正控制（`C-193`）和循环负控制（`C-194`）。本包自身不含数值编码、公平枚举、通用性或不可判定归约；前两项已由后续包补充。
- `cubical-machine-halting/NatProgramCode.agda`：`MP-CUBICAL-NAT-PROGRAM-CODE-001`；`R2-NATCODE-001`：`Instr`/`ProgramCode` 自定界位流到自然数的编码与全域 decoder、非法标签默认语义（`C-195`），合法像往返／单射／decoder 覆盖（`C-196`），数值 bounded evaluator 的像上语义保持（`C-197`）及编码后 halt/loop 控制（`C-198`）。公平调度和正半判定由后续两包补充；仍无计算通用性或停机不可判定归约。
- `cubical-machine-halting/FairEnumeration.agda`：`MP-CUBICAL-FAIR-ENUMERATION-001`；`R2-FAIR-001`：Triple/Config 自然数往返（`C-199`），任意 ProgramCode×Config×fuel case 的显式有限 `caseIndex`、`AppearsBy` 与 `noStarvation`（`C-200`），scheduled observation 保持原 `haltsWithin`（`C-201`），halt/loop controls（`C-202`）。分阶段正半判定由下一条补充；仍无通用性或不可判定归约。
- `cubical-machine-halting/SemiHalting.agda`：`MP-CUBICAL-SEMI-HALTING-001`；`R2-SEMIHALT-001`：有限 stage 的 `Maybe` approximant 与正答案持续性（`C-203`），精确步和 bounded observation 的桥梁（`C-204`），`CodeHalts` 与某阶段返回的双向对应（`C-205`），公平全域正见证枚举及 soundness/completeness（`C-206`），halt/loop controls（`C-207`）。下一项是 universality/reduction；不能把有限阶段 `nothing` 当成无界否定。
- `external-coq-mm2/`：冻结 Coq Undecidability Library 的 `coq-8.15@c486697` 777 文件树及当前 `rocq-9.2@c7257b7` 来源对照。`MP-COQ-MM2-UNDECIDABILITY-REPLAY-001` / C-208 重放上游 `MM2_HALTING_undec`；`MP-COQ-MM2-PROGRAMCODE-BRIDGE-001` / C-214–C-218 在同一 Coq kernel 定义显式 target、证明关系/函数终止等价、total many-one reduction 与 target synthetic undecidability。`undecidable` 精确为 `decidable P → enumerable(complement SBTM_HALT)`，不是无条件 `¬decidable`。
- `external-coq-parametric-ct/`：`MP-COQ-PARAMETRIC-CT-INTERNAL-UNDEC-001` / C-219–C-222；冻结 `coq-synthetic-computability@b9523cb` 的 109 文件树、20 文件目标闭包与 Coq 8.13.2 工具链，机器重放 `EPF_SCT_halting`、`K_nat_bool_undec`、`K_nat_undec`。结果是在显式 `EPF_bool + SCT` 前提下的内部 `~ decidable`，三个 `Print Assumptions` 均为 `Closed under the global context`；本包不证明该前提在 ambient HoTT 中成立，也不使用 HoTT 特有结构。
- `external-cubical-groupoid-syntax/`：`MP-CUBICAL-GROUPOID-SYNTAX-REPLAY-001` / C-223–C-226；冻结并重放 `akaposi/cohtt@5babc385` 的 20 个当前 `TT` 模块，机器检查 groupoid syntax 的四 sort/Π/U/El/相干结构、`isSetTy` α-normalisation 结果及与 set syntax 的 `Con/Sub/Ty/Tm` 同构。它是 `G-HOTT-SYNTAX-001` 首个 exact machine-replayed slice；缺 Nat、一般 identity、对象层 univalence/HIT、proof enumeration 与 arithmetic，因此不是完整 R4 calculus。
- `two-level-fibrant-replacement-uip/`：`MP-CUBICAL-2LTT-FIBRANT-REPLACEMENT-UIP-001` / C-227–C-232；以外层类型、内层 code/`El` 和受限 `Jᵢ` 重构 2LTT Theorem 2.20 的最小核：context-uniform FORM/INTRO/dependent-ELIM for `R` + outer UIP 推出 inner UIP，排除非平凡 inner loop；原生 `S¹.loop ≠ refl` 与删去 strict 两层桥的 identity-replacement 为 controls。它是已发表可选扩展的条件边界，不是 basic HoTT/2LTT 矛盾或最终现实相对悖论。
- `external-agda-flat-internal-universes/`：`MP-AGDA-FLAT-INTERNAL-UNIVERSES-REPLAY-001` / C-233–C-238；官方 LOPS 2018 Agda-flat source整包重放 ordinary internal fibration classifier no-go、CCHM/CCTT 实例、crisp/tiny classifier recovery、relative universe 与 modal typing controls。显式 postulates 保留；不是无前提 HoTT theorem。
- `external-coq-interval-replacement/`：`MP-COQ-INTERVAL-REPLACEMENT-BOUNDARY-001` / C-239–C-243；从 non-vendored `InternalCubical-Coq emptyctx@28a2568` archive重放 regular-family replacement contradiction、degenerate QIT replacement、`RFib ↔ DFib + Trans` 分解及 `emptyctx` 消去边界。完整 model structure 未在当前 Coq 版本重放。
- `external-coq-synthetic-incompleteness/`：`MP-COQ-SYNTHETIC-INCOMPLETENESS-R3-001` / C-244–C-249；repo-contained `csl@cd7d849` 807-file archive（含 CeCILL license）在 Coq 8.15.2 fresh build，重放 conditional classifier divergence、abstract essential incompleteness、`EPFμ → CTQ` 与 Robinson Q 条件独立句；target/1,284 stable artifacts/qualification exact replay。对象理论是一阶算术，universality、separation、Peirce、CTQ、Q containment、enumerability、consistency均显式；不证明 exact HoTT R4。
- `cubical-machine-halting/MM2Bridge.agda`：`MP-CUBICAL-MM2-BRIDGE-001` / C-209–C-213；在 Cubical Agda 内证明 label-1 MM2 到 `ProgramCode` 的查表、finality、单步、任意有限运行和截断停机存在性双向保持。`R2-TASKSPEC.json` 与 `R2-CROSS-KERNEL-CORRESPONDENCE.md` 固定双内核字段对应；机械 receipt 为 `audit/R2-cross-kernel-correspondence-20260914.json`。

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
