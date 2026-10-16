# 数学机器证明运行收据

<!-- math-proof-run-contract:v1
authoritative_run_root: HoTT/verification/runs
required_files: RUN.json,stdout.txt,stderr.txt,environment.txt,source-manifest.json
-->

本目录保存从 `MATH_PROOF_BEFORE_DELIVERY_V1` 生效后，实际被用于数学结论交付的 proof assistant/kernel 运行。每个 run 使用不可复用、不可覆盖的子目录：

```text
HoTT/verification/runs/<run-id>/
```

`run-id` 应包含日期、稳定 proof/claim 身份和必要的短序号，例如：

```text
20260912-MP-ERCF-001-01
```

## 每个 run 的必需文件

| 文件 | 最小内容 |
|---|---|
| `RUN.json` | schema/version、run/proof/claim IDs、工具/版本、完整 argv、cwd、时间、exit code、状态、支持范围、禁止外推 |
| `stdout.txt` | 原始 stdout；为空时仍保留空文件 |
| `stderr.txt` | 原始 stderr；warning/失败不得删除 |
| `environment.txt` | OS、arch、proof assistant/kernel、关键依赖的非敏感身份 |
| `source-manifest.json` | 本次实际读取的证明源码、配置、锁定依赖 path/bytes/SHA-256 |

`RUN.json` 的成功状态只有在 exit code 与工具语义确实表示 kernel 接受、所有必需文件存在且哈希已核时才可写 `KERNEL_ACCEPTED_WITH_SCOPE`。脚本启动、文件存在、测试数量或 stdout 中出现 `PASS` 不能替代这一判断。

## 失败与重放

- 影响结论、揭示前提/版本/工具边界或被最终 Gate 使用过的失败 run 必须保留；
- 修改证明源码、依赖、理论变体或命题后生成新 run，不覆盖旧目录；
- 重放记录新的 run ID，并在 `HoTT/CLAIM_EVIDENCE_MATRIX.md` 中更新当前指针；
- secret、token、个人凭据和无关环境变量不得进入收据；
- `/tmp` 只可保存可删除缓存/中间文件，不能成为任何必需文件的唯一位置。

## 索引和交付

run 只有被 `HoTT/CLAIM_EVIDENCE_MATRIX.md` 的精确 claim/proof 行引用后，才完成 `INDEXED` 状态。未索引的成功运行最多是 `RUN_OBSERVED_NOT_DELIVERABLE_AS_CONCLUSION`。

## 当前 run 索引

| run ID | proof/claims | 状态 | 用途 |
|---|---|---|---|
| `20260912-MP-ERCF-001-01` | `MP-ERCF-001` / `C-59`–`C-66` | `KERNEL_ACCEPTED_WITH_SCOPE / PENDING_CLAIM_EVIDENCE_MATRIX_UPDATE` | 第一次 captured 成功；绑定中间 README，保留为不可覆盖 pre-index 谱系，不作为当前交付 run |
| `20260912-MP-ERCF-001-02` | `MP-ERCF-001` / `C-59`–`C-66` | `KERNEL_ACCEPTED_WITH_SCOPE / INDEXED_IN_CLAIM_EVIDENCE_MATRIX` | 当前 final indexed run；Lean 4.33.1；`verify_formal_proof_run.py --rerun` 得到 `EXACT_EXIT_STDOUT_STDERR_MATCH` |
| `20260912-MP-ERCF-TRUNC-001-01` | `MP-ERCF-TRUNC-001` / `C-67`–`C-70` | `KERNEL_ACCEPTED_WITH_SCOPE / INDEXED_IN_CLAIM_EVIDENCE_MATRIX` | Cubical Agda 2.8.0 + library v0.9 原生 squash-HIT；外部依赖与 source tree 哈希已核；exact replay；判词 `DEFENSE_WORKS` |
| `20260912-MP-RACE-TIMEOUT-001-01` | `MP-RACE-TIMEOUT-001` / `C-71`–`C-76` | `KERNEL_ACCEPTED_WITH_SCOPE / INDEXED_IN_CLAIM_EVIDENCE_MATRIX` | Cubical Agda 2.8.0 + library v0.9；R041 delay 模型的操作闭包：bind 同余与商下降、race/deadline 非同余、商上无 race 选择子；判词 `REPRESENTATION_BOUNDARY` |
| `20260912-MP-CONTEXTUAL-EQUIV-001-01` | `MP-CONTEXTUAL-EQUIV-001` / `C-77`–`C-83` | `KERNEL_ACCEPTED_WITH_SCOPE / INDEXED_IN_CLAIM_EVIDENCE_MATRIX` | 同一工具链；上下文等价层次：`≡c` 精化 `≈` 且严格更细（时序/发散/值分离）；判词 `REPRESENTATION_BOUNDARY` |
| `20260912-MP-QUOTIENT-MONAD-001-01` | `MP-QUOTIENT-MONAD-001` / `C-84`–`C-88` | `KERNEL_ACCEPTED_WITH_SCOPE / INDEXED_IN_CLAIM_EVIDENCE_MATRIX` | 同一工具链；结果商的 canonical section 与商值 continuation 单子（单位律 + 代表层/商层关联律）；正面结构结果 |
| `20260912-MP-CONTEXT-CHARACTERIZATION-001-01` | `MP-CONTEXT-CHARACTERIZATION-001` / `C-89`–`C-91` | `KERNEL_ACCEPTED_WITH_SCOPE / INDEXED_IN_CLAIM_EVIDENCE_MATRIX` | 同一工具链；Bool 片段上下文等价完整刻画（trichotomy + 一般时间分离 + `≡c ⟺ ≡`）；代表相等即最细 |
| `20260912-MP-GUARD-ERASURE-001-01` | `MP-GUARD-ERASURE-001` / `C-92`–`C-95` | `KERNEL_ACCEPTED_WITH_SCOPE / INDEXED_IN_CLAIM_EVIDENCE_MATRIX` | 同一工具链；阶段擦除 ⇔ 不动点存在（必要性/充分性 + 否定律反例 + 具体振荡轨道） |
| `20260912-MP-COST-FACTORIZATION-001-01` | `MP-COST-FACTORIZATION-001` / `C-96`–`C-99` | `KERNEL_ACCEPTED_WITH_SCOPE / INDEXED_IN_CLAIM_EVIDENCE_MATRIX` | 同一工具链；同函数异时实例 + 裸函数不可区分性 + 成本恢复 no-go + 成本细化正控制 |
| `20260912-MP-PATH-CERTIFICATE-001-01` | `MP-PATH-CERTIFICATE-001` / `C-100`–`C-105` | `KERNEL_ACCEPTED_WITH_SCOPE / INDEXED_IN_CLAIM_EVIDENCE_MATRIX` | 同一工具链；R034 原生核查：ua 计算 + 截断命题性 + MereMove 非栖居（Σ回路 + 依赖运输）+ 路径版迁移正例 |
| `20260912-MP-ONLINE-CAUSALITY-001-01` | `MP-ONLINE-CAUSALITY-001` / `C-106`–`C-109` | `KERNEL_ACCEPTED_WITH_SCOPE / INDEXED_IN_CLAIM_EVIDENCE_MATRIX` | 同一工具链；在线因果：时刻 0 无前视 + 两个正例 + 完整知识 ≠ 在线资格 |
| `20260912-MP-TRANSITION-LIFT-001-01` | `MP-TRANSITION-LIFT-001` / `C-110`–`C-117` | `KERNEL_ACCEPTED_WITH_SCOPE / INDEXED_IN_CLAIM_EVIDENCE_MATRIX` | 同一工具链；R036/R038 核心边界：终止正控制 + 存在像自环 + 无两步提升 + 无当前态提升函数 + 精确极限空/截断极限有元素/无逆 + 无纤维恒定下降等级；零 warning |
| `20260912-MP-PARTIAL-DECISION-001-01` | `MP-PARTIAL-DECISION-001` / `C-118`–`C-123` | `KERNEL_ACCEPTED_WITH_SCOPE / INDEXED_IN_CLAIM_EVIDENCE_MATRIX` | 同一工具链；strict vs partial classifier：代表层 strict 分类器 + strict 区分 now/later + 无 strict 商扩展 + up-to-≈ partial classifier 正控制 + 无 strict Bool 消费者；零 warning |
| `20260912-MP-SIP-REPRESENTATION-001-01` | `MP-SIP-REPRESENTATION-001` / `C-124`–`C-128` | `KERNEL_ACCEPTED_WITH_SCOPE / INDEXED_IN_CLAIM_EVIDENCE_MATRIX` | 同一工具链；SIP/UA 替换许可：ua 识别 (Bool,true)/(Bool,false) + 签名外观察量不同 + 任意 Str→Bool 常数化 + 无统一恢复 + 细化签名正控制；零 warning |
| `20260912-MP-CAUCHY-MODULUS-001-01` | `MP-CAUCHY-MODULUS-001` / `C-129`–`C-133` | `KERNEL_ACCEPTED_WITH_SCOPE / INDEXED_IN_CLAIM_EVIDENCE_MATRIX` | 同一工具链；Cauchy modulus 边界：按极限值取商保留 limit + 两个 modulus 不同的表示被识别 + 无统一 modulus 恢复 + 细化同一性后 modulus 下降（正控制）；零 warning；外部 Real 库接口审计同步记录 |
| `20260913-MP-TRUNC-NORECOVERY-001-01` / `-02` / `-03` | `MP-TRUNC-NORECOVERY-001` / `C-134`–`C-141` | `KERNEL_ACCEPTED_WITH_SCOPE / INDEXED_IN_CLAIM_EVIDENCE_MATRIX`（`-03` 为当前指针） | 同一工具链；集合值截断不可恢复族、完成/区段候选的内部否定形式与 `isFinSet` 形状接口边界；`-01`/`-02` 保留为同源前次运行 |
| `20260913-MP-NOCANONICAL-001-01` / `-02` | `MP-NOCANONICAL-001` / `C-142`–`C-148` | `KERNEL_ACCEPTED_WITH_SCOPE / INDEXED_IN_CLAIM_EVIDENCE_MATRIX`（`-02` 为当前指针） | 同一工具链；unlabeled 二元素呈现无统一选点（swap 自识别 ⇒ `not` 不动点）+ 标签保留正控制 |
| `20260913-MP-UNIMATH-NOSECTION-REPLAY-01` / `-02` | `MP-UNIMATH-NOSECTION-REPLAY-001` / `C-05` | `REPLAYED / INDEXED_IN_CLAIM_EVIDENCE_MATRIX`（`-02` 为当前指针） | 固定 agda-unimath@`7b81411d` 的派生文件重放（486 条检查、exit 0）；`-01` 为 include 根配置失败尝试 |
| `20260913-MP-VERIFICATION-EVENT-001-01` | `MP-VERIFICATION-EVENT-001` / `C-149`–`C-156` | `KERNEL_ACCEPTED_WITH_SCOPE / INDEXED_IN_CLAIM_EVIDENCE_MATRIX` | 外部独立来源包的项目内 canonical 重放；负向校准在 `audit/imports/verification-event-20260913-01a099e9/project-negative-probe/` |
| `20260913-MP-ERCF3-T3-JOINT-001-01` / `-02` | `MP-ERCF3-T3-JOINT-001` / `C-157`–`C-159` | `KERNEL_ACCEPTED_WITH_SCOPE / INDEXED_IN_CLAIM_EVIDENCE_MATRIX`（`-02` 为当前指针） | builtins-only T3 脉冲链；共享判定联合递归 + 原始逐出现判定的项层恒等式 + 修正后的公式层恒等式；`-01` 为 `--safe` pragma 触发 `CoInfectiveImport` 的失败尝试 |
| `20260913-MP-ERCF3-T3-DECODING-001-01` | `MP-ERCF3-T3-DECODING-001` / `C-160`–`C-162` | `KERNEL_ACCEPTED_WITH_SCOPE / INDEXED_IN_CLAIM_EVIDENCE_MATRIX` | builtins-only T3 脉冲链；编码可解码性/单射性围栏（`var 2` 与 `num 0` 碰撞 ⇒ 无单射解码器；公式层同碰撞；数字片段正控制） |
| `20260913-MP-ERCF3-T3-REPAIR-SPEC-001-01` | `MP-ERCF3-T3-REPAIR-SPEC-001` / `C-163`–`C-165` | `KERNEL_ACCEPTED_WITH_SCOPE / INDEXED_IN_CLAIM_EVIDENCE_MATRIX` | builtins-only T3 脉冲链；编码修复规格（往返 ⇒ 单射的通用引理；结构化树编码正控制；当前 `codeT` 无解码器的精确否证） |
| `20260913-MP-ERCF3-T3-ARITH-TAGS-001-01` | `MP-ERCF3-T3-ARITH-TAGS-001` / `C-166`–`C-168` | `KERNEL_ACCEPTED_WITH_SCOPE / INDEXED_IN_CLAIM_EVIDENCE_MATRIX` | builtins-only T3 脉冲链；算术半第一片（偶/奇标签互斥与单射；`codeAtom` 单射；`C-168` 仅证明 `double` 下 `1` 无原像；`codeAtom` 满射的更正见 C-184–C-185） |
| `20260913-MP-ERCF3-T3-BIT-CODING-001-01` | `MP-ERCF3-T3-BIT-CODING-001` / `C-169`–`C-172` | `KERNEL_ACCEPTED_WITH_SCOPE / INDEXED_IN_CLAIM_EVIDENCE_MATRIX` | builtins-only T3 脉冲链；算术半第二片=位级底座（最低位/折半数字算术；`codeBits`/`unbits` 两侧引理与已知长度往返；码支配自身长度 ⇒ 解析器燃料可取自码本身） |
| `20260913-MP-ERCF3-T3-STREAMING-PARSER-001-01` | `MP-ERCF3-T3-STREAMING-PARSER-001` / `C-173`–`C-176` | `KERNEL_ACCEPTED_WITH_SCOPE / INDEXED_IN_CLAIM_EVIDENCE_MATRIX` | builtins-only T3 脉冲链；符号层 + 流式解析器 + 修复后的 Nat 值编码（一元索引自定界；燃料精确的 `run`；长度/界/多余燃料分解；`codeT'` 带全解码器与往返 ⇒ 单射，闭合编码层修复义务） |
| `20260913-MP-ERCF3-T3-FORMULA-CODING-001-01` | `MP-ERCF3-T3-FORMULA-CODING-001` / `C-177`–`C-180` | `KERNEL_ACCEPTED_WITH_SCOPE / INDEXED_IN_CLAIM_EVIDENCE_MATRIX` | builtins-only T3 脉冲链；修复编码的公式层（公式符号层与迭代数精确的 `run`；`=f` 的 Tm 子项复用项层解析器；长度界；`codeF'` 带全解码器与往返 ⇒ 单射） |
| `20260913-MP-ERCF3-T3-REPAIRED-SYNTAX-001-01` | `MP-ERCF3-T3-REPAIRED-SYNTAX-001` / `C-181`–`C-183` | `KERNEL_ACCEPTED_WITH_SCOPE / INDEXED_IN_CLAIM_EVIDENCE_MATRIX` | builtins-only T3 脉冲链；修复编码之上的替换一致（码级替换=解码—替换—编码，`Tm`/`Fml` 两层）与引用（`⌜φ⌝'` 单射、对角实例及其码） |
| `20260913-MP-ERCF3-T3-C168-COUNTERCHECK-001-01` | `MP-ERCF3-T3-C168-COUNTERCHECK-001` / `C-184`–`C-185` | `KERNEL_ACCEPTED_WITH_SCOPE / INDEXED_IN_CLAIM_EVIDENCE_MATRIX` | 独立审计吸收（F1）；完整传递闭包；`codeAtom (anum zero) ≡ 1`（1 有原像）与 `codeAtom` 满射——纠正 C-168 的中文叙述对象错配 |
| `20260913-MP-ERCF3-T3-CODING-IMAGE-001-01` | `MP-ERCF3-T3-CODING-IMAGE-001` / `C-186`–`C-187` | `KERNEL_ACCEPTED_WITH_SCOPE / INDEXED_IN_CLAIM_EVIDENCE_MATRIX` | 独立审计吸收（F1 替换依据）；完整传递闭包；`codeT'`/`codeF'` 的像不含 `1`，所以全 `Nat` 解码规格须定义像外行为；当前缺省分支在 `1` 上可达 |
| `20260914-MP-CUBICAL-MACHINE-HALTING-001-01` | `MP-CUBICAL-MACHINE-HALTING-001` / `C-188`–`C-190` | `KERNEL_ACCEPTED_WITH_SCOPE / INDEXED_IN_CLAIM_EVIDENCE_MATRIX` | R1 固定机器校准；停机正控制 + 固定循环程序逐有限步不终止 + 无截断有限停机见证；Agda 检查过程自身正常结束；不外推通用不可判定性、Gödel 或最终悖论 |
| `20260914-MP-CUBICAL-PROGRAM-CODE-001-01` | `MP-CUBICAL-PROGRAM-CODE-001` / `C-191`–`C-194` | `KERNEL_ACCEPTED_WITH_SCOPE / INDEXED_IN_CLAIM_EVIDENCE_MATRIX` | R2 第一薄层；有限 ProgramCode + 总 decoder + universal bounded evaluator 与 R1 语义一致 + halt/loop controls；不外推数值编码、公平枚举、通用性或不可判定性 |
| `20260914-MP-CUBICAL-NAT-PROGRAM-CODE-001-01` | `MP-CUBICAL-NAT-PROGRAM-CODE-001` / `C-195`–`C-198` | `KERNEL_ACCEPTED_WITH_SCOPE / INDEXED_IN_CLAIM_EVIDENCE_MATRIX` | `R2-NATCODE-001`；Instr/ProgramCode 自然数编码 + 总 decoder + 非法码策略 + 往返／单射／覆盖 + 数值 bounded evaluator 像上语义保持 + controls；不外推公平枚举、通用性或不可判定性 |
| `20260914-MP-CUBICAL-FAIR-ENUMERATION-001-01` | `MP-CUBICAL-FAIR-ENUMERATION-001` / `C-199`–`C-202` | `KERNEL_ACCEPTED_WITH_SCOPE / INDEXED_IN_CLAIM_EVIDENCE_MATRIX` | `R2-FAIR-001`；Triple/Config 往返 + program/input/fuel 的显式有限 caseIndex/AppearsBy/noStarvation + scheduled observation 保持 + controls；不外推 semi-halting、通用性或不可判定性 |
| `20260914-MP-CUBICAL-SEMI-HALTING-001-01` | `MP-CUBICAL-SEMI-HALTING-001` / `C-203`–`C-207` | `KERNEL_ACCEPTED_WITH_SCOPE / INDEXED_IN_CLAIM_EVIDENCE_MATRIX` | `R2-SEMIHALT-001`；有限 stage partial answer + 正答案持续 + `CodeHalts ↔ SemiReturns` + 公平正见证枚举 + controls；不外推 universality、总停机不可判定或 HoTT 悖论 |
| `20260914-MP-COQ-MM2-UNDECIDABILITY-REPLAY-001-01` | `MP-COQ-MM2-UNDECIDABILITY-REPLAY-001` / `C-208` | `KERNEL_ACCEPTED_WITH_SCOPE / INDEXED_IN_CLAIM_EVIDENCE_MATRIX` | `coq-8.15@c486697` 777 文件干净树；Coq 8.15.2 重放 `MM2_HALTING_undec`；assumptions closed；结论严格是 synthetic implication；两条目标闭包外 coqdep 告警原样保留 |
| `20260914-MP-CUBICAL-MM2-BRIDGE-001-01` | `MP-CUBICAL-MM2-BRIDGE-001` / `C-209`–`C-213` | `KERNEL_ACCEPTED_WITH_SCOPE / INDEXED_IN_CLAIM_EVIDENCE_MATRIX` | Agda 内 label-1 MM2→ProgramCode 查表/final/step/run/halting 双向保持与 controls；跨语言 theorem transport 不冒充 kernel 内同一性 |
| `20260914-MP-COQ-MM2-PROGRAMCODE-BRIDGE-001-01` | `MP-COQ-MM2-PROGRAMCODE-BRIDGE-001` / `C-214`–`C-218` | `KERNEL_ACCEPTED_WITH_SCOPE / INDEXED_IN_CLAIM_EVIDENCE_MATRIX` | Coq 同核显式 target；关系终止↔有限函数观察；`MM2_HALTING ⪯ PC_HALTING`；target synthetic undecidability；assumptions closed；exact replay |
| `20260914-MP-COQ-PARAMETRIC-CT-INTERNAL-UNDEC-001-01` | `MP-COQ-PARAMETRIC-CT-INTERNAL-UNDEC-001` / `C-219`–`C-222` | `KERNEL_ACCEPTED_WITH_SCOPE / INDEXED_IN_CLAIM_EVIDENCE_MATRIX` | `coq-synthetic-computability@b9523cb` 的 20 文件目标闭包；Coq 8.13.2 重放显式 `EPF_bool + SCT` 前提下的三个内部不可判定性定理；三个 assumptions closed；exact replay；不外推 ambient HoTT 无条件 no-decider |
| `20260914-MP-CUBICAL-GROUPOID-SYNTAX-REPLAY-001-01` | `MP-CUBICAL-GROUPOID-SYNTAX-REPLAY-001` / `C-223`–`C-226` | `KERNEL_ACCEPTED_WITH_SCOPE / INDEXED_IN_CLAIM_EVIDENCE_MATRIX` | `akaposi/cohtt@5babc385` 的 20 个 `TT` 模块两阶段 full-source replay；项目探针检查 `isSetTy` 与 `Con/Sub/Ty/Tm` 四类同构；首个 exact G-HOTT-SYNTAX slice，不外推完整 HoTT calculus 或 R4 不完备性 |
| `20260915-MP-CUBICAL-2LTT-FIBRANT-REPLACEMENT-UIP-001-01` | `MP-CUBICAL-2LTT-FIBRANT-REPLACEMENT-UIP-001` / `C-227`–`C-232` | `KERNEL_ACCEPTED_WITH_SCOPE / INDEXED_IN_CLAIM_EVIDENCE_MATRIX` | 两层 boundary-preserving interface 证明 context-uniform `R` + outer UIP ⇒ inner UIP；原生 `S¹.loop ≠ refl` 与 native identity-R 消融；exact replay；不外推 basic HoTT/2LTT 矛盾、自然 consumer 或现实桥梁 |
| `20260915-MP-AGDA-FLAT-INTERNAL-UNIVERSES-REPLAY-001-01` | `MP-AGDA-FLAT-INTERNAL-UNIVERSES-REPLAY-001` / `C-233`–`C-238` | `KERNEL_ACCEPTED_WITH_SCOPE / INDEXED_IN_CLAIM_EVIDENCE_MATRIX` | LOPS 官方 13-source Agda-flat 全包：internal classifier no-go + crisp/tiny recovery + relative universe；crisp positive/local negative；exact replay |
| `20260915-MP-COQ-INTERVAL-REPLACEMENT-BOUNDARY-001-01` | `MP-COQ-INTERVAL-REPLACEMENT-BOUNDARY-001` / `C-239`–`C-243` | `KERNEL_ACCEPTED_WITH_SCOPE / INDEXED_IN_CLAIM_EVIDENCE_MATRIX` | ITT regular replacement→False、degenerate QIT replacement、DFib+Trans→RFib、motive/emptyctx assumptions；Coq 8.13.2 exact replay；完整 Model_structure 不在范围 |
| `20260915-MP-COQ-SYNTHETIC-INCOMPLETENESS-R3-001-01` | `MP-COQ-SYNTHETIC-INCOMPLETENESS-R3-001` / `C-244`–`C-249` | `KERNEL_ACCEPTED_WITH_SCOPE / INDEXED_IN_CLAIM_EVIDENCE_MATRIX` | `csl@cd7d849` 807-file archive fresh build；一般 formal-system essential incompleteness、EPFμ→CTQ 与 Robinson Q 条件独立句；1,284 stable artifacts + theorem/assumption probe exact replay；first-order R3，不外推 exact HoTT R4 |

| `20261003-CG001-ZFC-HOTT-OBSERVATION-BRIDGE-02` | `MP-ZFC-HOTT-OBSERVATION-BRIDGE-001` / `C-357` | `KERNEL_ACCEPTED_WITH_SCOPE / INDEXED_IN_CLAIM_EVIDENCE_MATRIX` | Cubical Agda 2.8.0 + cubical 0.9；统一捕获器固定6个本地导入根和12个源码文件。原universe Q为`never`、集合截断Q第一步停和无统一section的联合桥控制；negative run `-NEG-02`在`Bool != A`处拒绝。它不形式化ZFC模型／验收或时间观察完备性。 |
| `20261003-CG001-ZFC-HOTT-COMPLETION-REFLECTION-04` | `MP-ZFC-HOTT-COMPLETION-REFLECTION-001` / `C-358` | `KERNEL_ACCEPTED_WITH_SCOPE / INDEXED_IN_CLAIM_EVIDENCE_MATRIX` | Cubical Agda 2.8.0 + cubical 0.9；统一捕获器固定6个本地导入根和11个源码文件。固定截断Q的stage-one completion不能推出原Q有限停机；negative run `-NEG-03`在`nothing != just 1`处拒绝。它不裁定任务同一性或形式化ZFC模型／验收。 |
| `20261004-MP-ZFC-ACTUAL-Q-POLICY-001-07` | `MP-ZFC-ACTUAL-Q-POLICY-001` / `C-359` | `KERNEL_ACCEPTED_WITH_SCOPE / INDEXED_IN_CLAIM_EVIDENCE_MATRIX` | Lean 4.34.1 core；pinned core binary、Q观察失败、P、A/B、ZFC-1使用模型与SameFullQ的条件性政策 consequence；negative run `-NEG-06`在`gap : qGap`不能作为任意`P`处拒绝。 |
| `20261004-MP-ZFC-ACTUAL-Q-HOTT-COUNTEREXAMPLE-001-07` | `MP-ZFC-ACTUAL-Q-HOTT-COUNTEREXAMPLE-001` / `C-360` | `KERNEL_ACCEPTED_WITH_SCOPE / INDEXED_IN_CLAIM_EVIDENCE_MATRIX` | Cubical Agda 2.8.0 + cubical 0.9；固定HoTT Q中coarse completion不能提升为original finite halting；8个实际本地依赖均已固定；negative run `-NEG-04`在`nothing != just 1`处拒绝。 |
| `20261004-MP-ZFC-ACTUAL-Q-ZENO-LIMIT-CONTROL-001-08` | `MP-ZFC-ACTUAL-Q-ZENO-LIMIT-CONTROL-001` / `C-361` | `KERNEL_ACCEPTED_WITH_SCOPE / DECLARED_CLASSICAL_AXIOMS / INDEXED_IN_CLAIM_EVIDENCE_MATRIX` | Lean 4.34.0 + pinned Mathlib；固定几何极限不推出有限自然阶段终点，闭连续时间端点到达为正控制。 |
| `20261004-MP-ZFC-ACTUAL-Q-SOURCE-CONTRACT-001-01` | `MP-ZFC-ACTUAL-Q-SOURCE-CONTRACT-001` / `C-362` | `KERNEL_ACCEPTED_WITH_SCOPE / SOURCE_CERTIFIED_PREMISES / INDEXED_IN_CLAIM_EVIDENCE_MATRIX` | Lean 4.34.1 core；固定 Norton/IEP 来源合同中 revised completion 不支付 strict original completion bridge；negative run `-NEG-001`拒绝伪造最大自然动作。 |
| `20261004-MP-ZFC-ACTUAL-Q-HOTT-CONTRACT-001-01` | `MP-ZFC-ACTUAL-Q-HOTT-CONTRACT-001` / `C-363` | `KERNEL_ACCEPTED_WITH_SCOPE / INDEXED_IN_CLAIM_EVIDENCE_MATRIX` | Cubical Agda 2.8.0 + cubical 0.9；固定 HoTT B 的 generic completion-gap schema；negative run `-NEG-001`在`nothing != just 1`处拒绝。 |
| `20261004-MP-BARE-ZFC-Q-PRECISION-001-03` | `MP-BARE-ZFC-Q-PRECISION-001` / `C-364` | `KERNEL_ACCEPTED_WITH_SCOPE / INDEXED_IN_CLAIM_EVIDENCE_MATRIX` | Lean 4.34.1 core；固定的 coarse standard-resolution view 不能决定 OriginDone 或支付 universal completion bridge；rich contract view 与 finite code view 为正控制。negative run `-NEG-004`在`False ↔ True`分支拒绝；`-NEG-001`保留为诊断检查了错误输出流的 setup failure。 |
| `20261005-MP-GODEL-Q-SETMM-APPENDIX-C-VAR-EXTENSION-004` | `MP-GODEL-Q-SETMM-APPENDIX-C-VAR-EXTENSION-001` / `C-369` | `KERNEL_ACCEPTED_WITH_SCOPE / INDEXED_IN_CLAIM_EVIDENCE_MATRIX` | Lean 4.34.1 core；stable runner 显式重建 generated import，exact raw `set.mm@160ebb…` vocabulary generator byte-identical control；有限 source vocabulary 的 source-type-preserving embedding 与按类型可数无限 fresh extension。 |
| `20261005-MP-GODEL-Q-SETMM-APPENDIX-C-VAR-EXTENSION-NEG-005` | `MP-GODEL-Q-SETMM-APPENDIX-C-VAR-EXTENSION-NEG-001` / `C-369` negative control | `EXPECTED_REJECTION_CONFIRMED / REPLAYABLE_NEGATIVE_CONTROL` | Lean 拒绝把 `rawEmbedding v000` 伪装为 `freshFamily wff 0`；`-NEG-001` 保留为 diagnostics-stream classification failure，`-NEG-003`保留为隐式 import 环境之前的确认谱系。 |

**依赖闭包登记缺口（独立审计发现 F6，2026-09-13）**：`ARITH-TAGS`、`BIT-CODING`、`STREAMING-PARSER`、`FORMULA-CODING`、
`REPAIRED-SYNTAX` 五个历史 run 的 `source-manifest.json` 只固定了直接导入模块，未列入编译器实际检查的传递依赖
（各缺 `DiagonalLemma.agda`；`REPAIRED-SYNTAX` 另缺 `DecodingFence.agda`）。缺口登记在
`HoTT/verification/PROOF_VERSION_CLOSURE.json` 的 `later_package_dependency_gap_allowlist`（6 条，每条绑定精确 proof/run、
source-manifest/stdout 哈希与缺失源码哈希；历史 manifest 不回填）；上表两个新 run 与所有后续 run 必须固定完整闭包，
同一 proof 的新 run 不继承历史例外，`verify_proof_version_closure.py` 会拒绝。

**重放登记**：已有 proof/claim 的新 run 不覆盖矩阵中的 primary run。先确保 v2 registry 已登记该 proof；
`mark_proof_run_indexed.py` 会把非 primary run 原子加入 `replay_runs`，再标记 RUN；`freeze_proof_index_rows.py`
只接受 primary 或该精确 replay 关系。仅凭矩阵中存在相同 proof/claim ID，不能把新 run 标为已索引。

**claim 计数更正（独立审计发现 F7）**：`later_machine_proved_claim_count` 曾按每次增量口算而漏计（曾写 34，实为 35；
现含 LOPS/ITT/R3 Coq 三包为 101）。`verify_proof_version_closure.py` 现在**重算**该字段，登记值与重算值不一致即 fail closed。

`index-row-manifest.json` 冻结 proof row 与各 claim row 的精确行哈希。claim matrix 后续只追加新 proof 时，旧 run 不再要求整个不断增长的索引文件保持同 SHA，而是要求自己的原行逐字不变；若任一旧行被改写，verifier fail closed。

当前数学状态均为 `MACHINE_PROVED_LOCAL_UNCOMMITTED`。`MP-ERCF-001` 是一般 Lean 因子化骨架；`MP-ERCF-TRUNC-001` 是截断防御结果；`MP-RACE-TIMEOUT-001` 是 partiality 商竞争边界结果；`MP-CONTEXTUAL-EQUIV-001` 是上下文等价层次结果；`MP-QUOTIENT-MONAD-001` 是商值 continuation 单子结构；`MP-CONTEXT-CHARACTERIZATION-001` 是上下文等价完整刻画；`MP-GUARD-ERASURE-001` 是阶段擦除与不动点存在的等价；`MP-COST-FACTORIZATION-001` 是同函数异时的表示限制与细化正控制；`MP-PATH-CERTIFICATE-001` 是 R034 路径证书边界的原生核查；`MP-ONLINE-CAUSALITY-001` 是在线因果资格边界；`MP-TRANSITION-LIFT-001` 是过渡抽象/极限边界；`MP-PARTIAL-DECISION-001` 是 strict vs partial classifier 边界；`MP-SIP-REPRESENTATION-001` 是 SIP/UA 替换许可边界；`MP-CAUCHY-MODULUS-001` 是 Cauchy modulus 表示边界。十四者都不是 HoTT 悖论。完整证据见 `../../../audit/` 下对应的实施证据文档。

历史 aggregate 结果仍在 `../VERIFICATION_REPORT.md`，不伪造为本规范生效后的逐 run 包。
