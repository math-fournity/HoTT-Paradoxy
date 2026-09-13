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
| `20260913-MP-ERCF3-T3-ARITH-TAGS-001-01` | `MP-ERCF3-T3-ARITH-TAGS-001` / `C-166`–`C-168` | `KERNEL_ACCEPTED_WITH_SCOPE / INDEXED_IN_CLAIM_EVIDENCE_MATRIX` | builtins-only T3 脉冲链；算术半第一片（偶/奇标签互斥与单射；var/num 片段 Nat 值单射编码；非满射 ⇒ 解码器需缺省分支） |
| `20260913-MP-ERCF3-T3-BIT-CODING-001-01` | `MP-ERCF3-T3-BIT-CODING-001` / `C-169`–`C-172` | `KERNEL_ACCEPTED_WITH_SCOPE / INDEXED_IN_CLAIM_EVIDENCE_MATRIX` | builtins-only T3 脉冲链；算术半第二片=位级底座（最低位/折半数字算术；`codeBits`/`unbits` 两侧引理与已知长度往返；码支配自身长度 ⇒ 解析器燃料可取自码本身） |
| `20260913-MP-ERCF3-T3-STREAMING-PARSER-001-01` | `MP-ERCF3-T3-STREAMING-PARSER-001` / `C-173`–`C-176` | `KERNEL_ACCEPTED_WITH_SCOPE / INDEXED_IN_CLAIM_EVIDENCE_MATRIX` | builtins-only T3 脉冲链；符号层 + 流式解析器 + 修复后的 Nat 值编码（一元索引自定界；燃料精确的 `run`；长度/界/多余燃料分解；`codeT'` 带全解码器与往返 ⇒ 单射，闭合编码层修复义务） |

`index-row-manifest.json` 冻结 proof row 与各 claim row 的精确行哈希。claim matrix 后续只追加新 proof 时，旧 run 不再要求整个不断增长的索引文件保持同 SHA，而是要求自己的原行逐字不变；若任一旧行被改写，verifier fail closed。

当前数学状态均为 `MACHINE_PROVED_LOCAL_UNCOMMITTED`。`MP-ERCF-001` 是一般 Lean 因子化骨架；`MP-ERCF-TRUNC-001` 是截断防御结果；`MP-RACE-TIMEOUT-001` 是 partiality 商竞争边界结果；`MP-CONTEXTUAL-EQUIV-001` 是上下文等价层次结果；`MP-QUOTIENT-MONAD-001` 是商值 continuation 单子结构；`MP-CONTEXT-CHARACTERIZATION-001` 是上下文等价完整刻画；`MP-GUARD-ERASURE-001` 是阶段擦除与不动点存在的等价；`MP-COST-FACTORIZATION-001` 是同函数异时的表示限制与细化正控制；`MP-PATH-CERTIFICATE-001` 是 R034 路径证书边界的原生核查；`MP-ONLINE-CAUSALITY-001` 是在线因果资格边界；`MP-TRANSITION-LIFT-001` 是过渡抽象/极限边界；`MP-PARTIAL-DECISION-001` 是 strict vs partial classifier 边界；`MP-SIP-REPRESENTATION-001` 是 SIP/UA 替换许可边界；`MP-CAUCHY-MODULUS-001` 是 Cauchy modulus 表示边界。十四者都不是 HoTT 悖论。完整证据见 `../../../audit/` 下对应的实施证据文档。

历史 aggregate 结果仍在 `../VERIFICATION_REPORT.md`，不伪造为本规范生效后的逐 run 包。
