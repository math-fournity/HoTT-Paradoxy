# ERCF-3 T3 脉冲链（含十个 claim-bearing package）

> 判词只覆盖本目录的编码层义务；**ERCF-3 本体保持 `GATED`**（C8 §9 的 P1–P8 与停止条件不变）。
> 快速索引：`HoTT/CLAIM_EVIDENCE_MATRIX.md` 的追加节；版本登记：`HoTT/verification/PROOF_VERSION_CLOSURE.json` 的 `later_packages`。

| package | claims | 源码 | run | 判词 |
|---|---|---|---|---|
| `MP-ERCF3-T3-JOINT-001` | `C-157`–`C-159` | `JointRecursion.agda` | `20260913-MP-ERCF3-T3-JOINT-001-02` | `MACHINE_PROVED_LOCAL_UNCOMMITTED / ERCF3_T3_SHARED_DECISION_JOINT_RECURSION` |
| `MP-ERCF3-T3-DECODING-001` | `C-160`–`C-162` | `DecodingFence.agda` | `20260913-MP-ERCF3-T3-DECODING-001-01` | `MACHINE_PROVED_LOCAL_UNCOMMITTED / ERCF3_T3_DECODABILITY_FENCE` |
| `MP-ERCF3-T3-REPAIR-SPEC-001` | `C-163`–`C-165` | `CodingRepair.agda` | `20260913-MP-ERCF3-T3-REPAIR-SPEC-001-01` | `MACHINE_PROVED_LOCAL_UNCOMMITTED / ERCF3_T3_REPAIR_SPECIFICATION` |
| `MP-ERCF3-T3-ARITH-TAGS-001` | `C-166`–`C-168` | `ArithmeticTags.agda` | `20260913-MP-ERCF3-T3-ARITH-TAGS-001-01` | `MACHINE_PROVED_LOCAL_UNCOMMITTED / ERCF3_T3_ARITHMETIC_TAGS_FRAGMENT` |
| `MP-ERCF3-T3-BIT-CODING-001` | `C-169`–`C-172` | `BitCoding.agda` | `20260913-MP-ERCF3-T3-BIT-CODING-001-01` | `MACHINE_PROVED_LOCAL_UNCOMMITTED / ERCF3_T3_BIT_SUBSTRATE` |
| `MP-ERCF3-T3-STREAMING-PARSER-001` | `C-173`–`C-176` | `StreamingParser.agda` | `20260913-MP-ERCF3-T3-STREAMING-PARSER-001-01` | `MACHINE_PROVED_LOCAL_UNCOMMITTED / ERCF3_T3_REPAIRED_NAT_CODING` |
| `MP-ERCF3-T3-FORMULA-CODING-001` | `C-177`–`C-180` | `FormulaCoding.agda` | `20260913-MP-ERCF3-T3-FORMULA-CODING-001-01` | `MACHINE_PROVED_LOCAL_UNCOMMITTED / ERCF3_T3_REPAIRED_FORMULA_CODING` |
| `MP-ERCF3-T3-REPAIRED-SYNTAX-001` | `C-181`–`C-183` | `RepairedSyntax.agda` | `20260913-MP-ERCF3-T3-REPAIRED-SYNTAX-001-01` | `MACHINE_PROVED_LOCAL_UNCOMMITTED / ERCF3_T3_REPAIRED_SUBSTITUTION_AND_QUOTATION` |
| `MP-ERCF3-T3-C168-COUNTERCHECK-001` | `C-184`–`C-185` | `C168Countercheck.agda` | `20260913-MP-ERCF3-T3-C168-COUNTERCHECK-001-01` | `MACHINE_PROVED_LOCAL_UNCOMMITTED / ERCF3_T3_C168_NARRATIVE_CORRECTED_BY_COUNTERCHECK` |
| `MP-ERCF3-T3-CODING-IMAGE-001` | `C-186`–`C-187` | `CodingImage.agda` | `20260913-MP-ERCF3-T3-CODING-IMAGE-001-01` | `MACHINE_PROVED_LOCAL_UNCOMMITTED / ERCF3_T3_REPAIRED_CODING_MISSES_ONE` |

其余 `ObjectSyntax.agda`–`DecisionParam.agda` 与 `TermIdentityFinal.agda` 是 S067–S080 的脉冲谱系（`PULSE_EVIDENCE_ONLY`，无 claim 行）。

---

## 1. `MP-ERCF3-T3-JOINT-001`：共享判定联合递归

### 1.1 精确命题

固定工具链与语法（`ObjectSyntax.agda` 的 `Tm`/`Fml`、`DiagonalCore.agda` 的 `codeT`/`codeF`、`CodeStoreFix.agda` 的 `substFixT`、`DecisionParam.agda` 的 `substFixTd`）。本包机器检查三条：

| claim | 精确命题 | 源码标识 |
|---|---|---|
| `C-157` | `(d : Bool) (k i : Nat) (t : Tm) → substFixTd d k i t ≡ codeT (substTd d k i t)`（显式共享判定下码级修正替换与语法级替换一致） | `JointRecursion.substFixTd-agrees` |
| `C-158` | `(k i : Nat) (t : Tm) → substFixT k i t ≡ codeT (substT k i t)`（**原始逐出现判定**的项层恒等式——N34 记录的剩余义务） | `JointRecursion.fixT-agrees` |
| `C-159` | `(k i : Nat) (φ : Fml) → substFixFc k i φ ≡ codeF (substF k i φ)`（修正后的公式层码替换与语法替换一致） | `JointRecursion.substFixFc`、`JointRecursion.fixF-agrees`（见 §3） |

### 1.2 来源与脉冲谱系

- S067–S080 的 13 个脉冲把该义务逐步逼到"两侧必须共享同一判定 → 联合递归"（`TermIdentityFinal.agda` 的注释与 `S-RES-20260913-080` 的记载）；
- S079 的修法 (b) 把**码级**替换改成判定值显式参数（`substFixTd`）；
- 本包在同一步把**语法级**替换也改成显式判定（`substTd`），于是三项都成为普通归纳；
- `C-158` 不需要显式共享判定：只有 `var` 分支做判定分叉，因此**逐出现判定**的项层恒等式可以单 `with` 收口（`fixT-agrees`）。

### 1.3 修正记录（不重写历史文件）

`CodeStoreFixF.agda`（S075 脉冲）的公式层码替换在 `all` 的**影子分支**（`i =n m` 为真）写的是
`1+1+1+1+1 + (m + codeF (all m φ))`，即对整条量化公式**双重编码**；语法层 `substF k i (all m φ)` 在该分支保持
`all m φ` 不代入，其码应为 `1+1+1+1+1 + (m + codeF φ)`。本包在新模块中给出修正函数 `substFixFc` 并机器检查 `C-159`。
历史脉冲文件与其会话证据**逐字节未改**；本修正以新模块 + 本 README + 矩阵追加节的形式登记。

### 1.4 运行与证据

| 类型 | 位置 |
|---|---|
| 主源码 | `HoTT/formal/ercf3-t3/JointRecursion.agda` |
| 依赖模块（按哈希固定） | `ObjectSyntax.agda`、`DiagonalCore.agda`、`DiagonalLemma.agda`、`CodeStoreFix.agda`、`MutualInduction2.agda`、`DecisionParam.agda` |
| 固定工具链 | `HoTT/formal/ercf3-t3/TOOLCHAIN.json` + `AGDA_LIBRARIES`（Agda 2.8.0-3d04bac、Cubical v0.9 库声明；证明本身只用 Agda builtins） |
| canonical run | `HoTT/verification/runs/20260913-MP-ERCF3-T3-JOINT-001-02/`（`KERNEL_ACCEPTED_WITH_SCOPE`、exit 0、stderr 0、`INDEXED_IN_CLAIM_EVIDENCE_MATRIX`） |
| 行冻结收据 | `HoTT/verification/runs/20260913-MP-ERCF3-T3-JOINT-001-02/index-row-manifest.json`（`freeze_proof_index_rows.py`；冻结包行 + `C-157`–`C-159` 三行；后续矩阵只追加，故为 row-stable） |
| 失败尝试（保留） | `HoTT/verification/runs/20260913-MP-ERCF3-T3-JOINT-001-01/`：在源码里加 `{-# OPTIONS --safe #-}` 后，早期脉冲模块未声明 `--safe` 触发 `CoInfectiveImport`（exit 42）；canonical 命令因此与 S067–S080 脉冲一致（不含 `--safe`），命令行 `--safe` 的手工检查同样 exit 0 |

**校验入口范围**：本包是 builtins-only 的 T3 脉冲链（与 S067–S080 同族），源码不声明 `--safe --cubical`，因此
`verify_formal_proof_run.py` 对它会报 `AGDA_SAFE_CUBICAL_OPTIONS_REQUIRED`——那是该 verifier 的适用域（cubical 包），
不是本包的失败。本包的 canonical 校验入口是 `verify_proof_version_closure.py`（`later_packages` 分支，要求源码/工具链/
`RUN.json` Git-tracked、`exit_code = 0`、`index_status = INDEXED_IN_CLAIM_EVIDENCE_MATRIX`）与 run 自身的
`RUN.json` + `index-row-manifest.json`。

### 1.5 禁止外推

- **不是** ERCF-3 本体：不构造对角线不动点，不涉及证明谓词 `P` 的表示性、反射或自应用；不改变 ERCF-3 的 `GATED` 状态；
- **不是** HoTT 悖论或 HoTT 内部不一致；本包不使用 univalence、cubical Path、HIT 或 truncation；
- 不把编码层一致升级成"对角引理已形式化"或"对象层替换算术化已完成"；
- 只覆盖上述三条精确命题与固定工具链；不覆盖 `substF` 的其它性质或其它编码方案。

---

## 2. `MP-ERCF3-T3-DECODING-001`：编码的可解码性/单射性围栏

`ObjectSyntax.agda` 第 11 行把 "Goedel coding with decodability/injectivity" 列为 T3 义务并**故意不形式化**；
`DiagonalCore.agda` 的 `⌜-injective` 实际是"沿码相等的替换同余"（`cong-here`），不是单射性。本包把这条义务的**下界**机器化：

| claim | 精确命题 | 源码标识 |
|---|---|---|
| `C-160` | 具体编码在项层不是单射：`codeT (var 2) ≡ codeT (num 0)`（`refl`）而 `var 2 ≢ num 0`，故不存在 `(t u : Tm) → codeT t ≡ codeT u → t ≡ u` 的单射解码器 | `var2-num0-collide`、`var≢num`、`no-injective-codeT` |
| `C-161` | 同一碰撞提升到公式层：`codeF (var 2 =f var 2) ≡ codeF (num 0 =f num 0)` 而两条公式不同，故 `codeF` 也不单射 | `eqVar2-collides-eqNum0`、`varEq≢numEq`、`no-injective-codeF` |
| `C-162` | 正控制：数字片段在码上单射——`(n m : Nat) → codeT (num n) ≡ codeT (num m) → n ≡ m` | `num-code-injective` |

**修复要求（已记录、未证明）**：可解码编码需要**标签值域不相交**（例如 `var n ↦ 3 * n`、`num n ↦ 3 * n + 1`、
`_+t_ ↦ 3 * ⟨pair⟩ + 2`，或列表编码）。任何修复都会改变具体码值，从而改变对角实例——那是下一个有界脉冲。

**运行**：`HoTT/verification/runs/20260913-MP-ERCF3-T3-DECODING-001-01/`（`KERNEL_ACCEPTED_WITH_SCOPE`、exit 0、stderr 0、
`INDEXED_IN_CLAIM_EVIDENCE_MATRIX`）+ `index-row-manifest.json`（4 行冻结）。

**校验入口**：与 §1.4 同——本目录两个包都在 builtins-only 脉冲链上，`verify_formal_proof_run.py` 会报
`AGDA_SAFE_CUBICAL_OPTIONS_REQUIRED`（那是 cubical 包的适用域）；canonical 校验入口是
`verify_proof_version_closure.py` 的 `later_packages` 分支与 run 自身的 `RUN.json` + `index-row-manifest.json`。

**禁止外推**：不给出修复后的编码或其单射性证明；不声称对角引理不可形式化（只说明**当前编码**不可解码）；
不涉及证明谓词表示性、反射或对角不动点；不改写 `DiagonalCore.agda` 的 `⌜-injective` 命名或任何历史脉冲文件；
ERCF-3 保持 `GATED`。

---

## 3. `MP-ERCF3-T3-REPAIR-SPEC-001`：编码修复规格

把"修复编码"从口号变成可机器检查的规格，并给出精确的剩余义务：

| claim | 精确命题 | 源码标识 |
|---|---|---|
| `C-163` | 结构化（树）编码可解码：`encT : Tm → CodeT`、`decT : CodeT → Tm` 满足 `∀ t → decT (encT t) ≡ t`，故 `encT` 单射 | `encT-roundtrip`、`encT-injective`（正控制） |
| `C-164` | 通用规格引理：任意目标类型 `A` 上，若 `c : Tm → A` 有往返解码器 `dec`，则 `c` 单射 | `roundtrip-implies-injective` |
| `C-165` | 当前 Nat 编码 `codeT` **不存在解码器**：`Σ (dec : Nat → Tm), (∀ t → dec (codeT t) ≡ t)` 蕴含 `Empty` | `no-decoder-for-codeT`（C-164 + `DecodingFence.no-injective-codeT`） |

**修复义务（下一有界脉冲）**：给出 `codeT' : Tm → Nat` 与 `dec' : Nat → Tm` 并证明往返；由 C-164 该对自动单射。
结构半已完成（C-163）；**算术半**（标签值域不相交如 `3n`/`3n+1`/`3*⟨pair⟩+2`，或列表编码）尚未完成——
它需要 Nat 算术/配对引理，是明确的下一步。

**运行**：`HoTT/verification/runs/20260913-MP-ERCF3-T3-REPAIR-SPEC-001-01/`（`KERNEL_ACCEPTED_WITH_SCOPE`、exit 0、
stderr 0、`INDEXED_IN_CLAIM_EVIDENCE_MATRIX`）+ `index-row-manifest.json`（4 行冻结）。

**校验入口与禁止外推**：与 §1.4/§2 同（builtins-only ⇒ 适用 closure verifier）；不给 Nat 值修复编码本身，
不涉及 P 表示性/反射/对角不动点，ERCF-3 保持 `GATED`，历史脉冲文件不改写。

---

## 4. `MP-ERCF3-T3-ARITH-TAGS-001`：修复编码的算术半第一片

| claim | 精确命题 | 源码标识 |
|---|---|---|
| `C-166` | 偶/奇标签算术：`double` 单射（`double n ≡ double m → n ≡ m`）、`double n ≢ odd m`、`odd` 单射（`double n = 2n`、`odd n = 2n+1`） | `double-injective`、`double≠odd`、`odd-injective` |
| `C-167` | var/num 片段的 Nat 值编码 `codeAtom`（`avar n ↦ 2n`、`anum n ↦ 2n+1`）**单射**——链条中第一个 Nat 值单射编码 | `codeAtom-injective` |
| `C-168` | **`double`** 非满射：`1` 无原像（`¬ Σ m, double m ≡ 1`），故 **`avar`-only 片段**非满射 | `one-has-no-preimage` |

> **2026-09-13 独立审计更正（F1）**：本行原先写作"该编码（`codeAtom`）非满射，故任何全解码器必须带缺省分支"——
> 这是**对象错配**：`one-has-no-preimage` 的类型是 `Not (Σ' Nat (λ m → double m ≡ suc zero))`，谈的是函数 `double`，
> 与 `codeAtom` 无关。外部独立审计机器证明 `codeAtom` **满射**（`MP-AUD-C168-20260913`，`audit/imports/audit-c168-20260913/`）；
> 本 repo 以**完整传递闭包**重放该反证（`MP-ERCF3-T3-C168-COUNTERCHECK-001` / `C-184`–`C-185`，见 §9）。
> "全解码器需要缺省分支"这一点对**修复后的** `codeT'`/`codeF'` 仍然成立，但依据是它们自身的像不含 `1`
> （`MP-ERCF3-T3-CODING-IMAGE-001` / `C-186`–`C-187`），而不是本条。

**剩余算术义务（下一有界脉冲）**：把标签不相交形状扩到应用结点（`_+t_` 需要配对函数），写出带缺省分支的
**全解码器**，并证明像上的往返（由 C-164 自动得到单射）。

**运行**：`HoTT/verification/runs/20260913-MP-ERCF3-T3-ARITH-TAGS-001-01/`（`KERNEL_ACCEPTED_WITH_SCOPE`、exit 0、
stderr 0、`INDEXED_IN_CLAIM_EVIDENCE_MATRIX`）+ `index-row-manifest.json`（4 行冻结）。

**禁止外推**：只覆盖 var/num 片段；应用结点与全解码器未做；不涉及 P 表示性/反射/对角不动点；
ERCF-3 保持 `GATED`；历史脉冲文件不改写。

---

## 5. `MP-ERCF3-T3-BIT-CODING-001`：修复编码的算术半第二片（位级底座与燃料界）

标签不相交的算术核心（§4）只覆盖 var/num 片段；应用结点需要一位一位可读的编码底座。本包把它机器化：

| claim | 精确命题 | 源码标识 |
|---|---|---|
| `C-169` | 数字算术：`parity (twice n) ≡ false`、`parity (suc (twice n)) ≡ true`、`half (twice n) ≡ n`、`half (suc (twice n)) ≡ n`（`parity` 取最低位、`half` 折半） | `parity-twice`、`parity-suc-twice`、`half-twice`、`half-suc-twice` |
| `C-170` | 捆绑/抽取两侧引理：`parity (pack b c) ≡ b`、`half (pack b c) ≡ c`（`codeBits [] ≡ 1`，`codeBits (b ∷ bs) ≡ pack b (codeBits bs)`） | `parity-code`、`half-code` |
| `C-171` | 已知长度的往返：`unbits (LEN bs) (codeBits bs) ≡ bs` | `unbits-code` |
| `C-172` | 码支配自身长度：`suc (LEN bs) ≤ codeBits bs`，故未来解析器的**燃料可直接取自码本身** | `codeBits-dominates`（辅助 `≤-refl`/`≤-suc`/`≤-trans`/`n≤twice`/`suc≤pack`） |

**为什么先做位级底座**：`unbits` 只能按外部给定的长度抽取（C-171），而解析器必须只拿到码就能工作；
C-172 正是"码里自带够用的位数"这一步，它使"燃料=码"的写法有机器检查的依据，而不是一句设计口号。

**后续（已由 §6 收口）**：符号层（`var n`/`num n` 的**自定界**索引位 + 构造子标签）与带缺省分支（C-168）的解析器、
像上往返与 Nat 值编码单射已在 `MP-ERCF3-T3-STREAMING-PARSER-001`（C-173–C-176）中机器化。

**运行**：`HoTT/verification/runs/20260913-MP-ERCF3-T3-BIT-CODING-001-01/`（`KERNEL_ACCEPTED_WITH_SCOPE`、exit 0、
stderr 0、`INDEXED_IN_CLAIM_EVIDENCE_MATRIX`）+ `index-row-manifest.json`（5 行冻结）。

**校验入口**：与 §1.4 同——本目录全部包都在 builtins-only 脉冲链上，`verify_formal_proof_run.py` 对它们会报
`AGDA_SAFE_CUBICAL_OPTIONS_REQUIRED`（那是 cubical 包的适用域）；canonical 校验入口是
`verify_proof_version_closure.py` 的 `later_packages` 分支与 run 自身的 `RUN.json` + `index-row-manifest.json`。

**禁止外推**：不给出符号层、解析器或全解码器；不声称完整 `Tm` 已有 Nat 值单射编码；往返只在**已知长度/自身码**上成立；
不涉及 P 表示性/反射/对角不动点；ERCF-3 保持 `GATED`；历史脉冲文件不改写。

---

## 6. `MP-ERCF3-T3-STREAMING-PARSER-001`：符号层、流式解析器与修复后的 Nat 值编码

§4/§5 把算术半推进到"标签不相交 + 位级底座 + 燃料界"，并把**符号层与解析器**记为下一义务。本包闭合它，并因此
在**编码层**完结 §3 记录的修复义务（C-163/C-164/C-165）：

| claim | 精确命题 | 源码标识 |
|---|---|---|
| `C-173` | 自定界索引层：`unary n`（`n` 个 `true` 后随一个 `false`）可读，且读取后剩余燃料恰为 `f`：`run (suc (m + f)) (unary m ++ rest) (readIndex b k stk) ≡ resume (close (leafTerm b (k + m)) stk) rest f` | `unary-run` |
| `C-174` | 符号层 `bits`/`BLEN` 与**流式解析器** `run` 的精确往返：`run (BLEN t + f) (bits t ++ rest) (startSub stk) ≡ resume (close t stk) rest f`——消耗 `BLEN t` 个单位后剩余燃料恰为 `f`；顺序消费（左子解析后仍需右子）由显式框架栈在**同一个**燃料递减递归内解决 | `parse-run`、`parse-run-app` |
| `C-175` | 长度对账与燃料分解：`LEN (bits t) ≡ BLEN t`；`n ≤ m → Σ' Nat (λ k → m ≡ n + k)`；`unbits (i + j) c ≡ unbits i c ++ unbits j (halfs i c)` | `bits-length`、`≤-split`、`unbits-split` |
| `C-176` | **修复后的 Nat 值编码** `codeT'`（`t ↦ codeBits (bits t)`）带全解码器 `dec : Nat → Tm`（含缺省分支，符合 C-168）满足 `dec (codeT' t) ≡ t`，故由 C-164 **单射** | `codeT'`、`dec`、`codeT'-roundtrip`、`codeT'-injective` |

**为什么解析器写成"流式循环"而不是嵌套递归**：`(t +t u)` 的自然解析是"先解析 t 再解析 u"，第二次调用要用第一次
调用**返回剩余**的燃料，这在 Agda 里既不能结构递归也不能由终止检查器接受。本包把待解析的右子做成显式框架栈
（`Slot`/`Stack`/`close`），于是每一步只做一次 `run f rest …`：一次迭代恰好消费一位、消耗一个燃料单位，
结构递归直接成立，而往返定理仍是**精确**的（剩余燃料即 `f`）。

**修复义务的现状**：C-165 证明旧 `codeT` 不存在解码器；C-176 给出一个**存在**的 Nat 值编码，其解码器是全函数、
往返在像上成立。于是"编码不可解码"这一前置缺口在**编码层**被补齐。仍未做：公式层 `codeF` 的对应修复实现、
把 `codeT'`/`dec` 与对象层替换（`substFix` 系列）对齐、以及证明谓词 `P` 的表示性、反射与对角不动点。

**运行**：`HoTT/verification/runs/20260913-MP-ERCF3-T3-STREAMING-PARSER-001-01/`（`KERNEL_ACCEPTED_WITH_SCOPE`、
exit 0、stderr 0、`INDEXED_IN_CLAIM_EVIDENCE_MATRIX`）+ `index-row-manifest.json`（5 行冻结）。

**校验入口**：与 §1.4 同（builtins-only 脉冲链 ⇒ canonical 入口是 `verify_proof_version_closure.py` 的
`later_packages` 分支与 run 自身的 `RUN.json` + `index-row-manifest.json`）。

**禁止外推**：只覆盖 **Tm** 的编码/解码与单射性；不修复 `codeF` 的实现、不重做 `codeT`/`codeF` 的对象层替换一致义务、
不涉及 P 表示性/反射/对角不动点；新编码属新模块，历史脉冲文件与 `DiagonalCore` 的既有编码逐字节未改；ERCF-3 保持 `GATED`。

---

## 7. `MP-ERCF3-T3-FORMULA-CODING-001`：修复编码的公式层（复用项层解码器）

对角化真正引用的是**公式**（`⌜ φ ⌝`），所以 C-176 的修复必须再上一层。本包不重写项层解析器，而是把它当**黑箱**：

| claim | 精确命题 | 源码标识 |
|---|---|---|
| `C-177` | 公式符号层 `bitsF`（`=f`/`bot`/`=>f` 两位标签；`all` 两位标签 + 一元索引）与流式 `run` 的往返：`run (wantFml stk) (STEPS φ + f) (bitsF φ ++ rest) ≡ resume (close φ stk) rest f`；`all` 的索引读取（`index-run`）单独收口 | `parse-run`、`index-run` |
| `C-178` | 项层解析器复用：`tmFrom bs = SP.run (LEN bs) bs (SP.startSub SP.ε)` 满足 `tmFrom (bits t ++ rest) ≡ res t rest`——`=f` 的 `Tm` 子项燃料直接取自**剩余位数** | `tmFrom-run`、`eq-node`、`eqRight-step` |
| `C-179` | 长度对账：`STEPS φ ≤ LEN (bitsF φ)`，故公式码本身仍可充当燃料 | `STEPS≤LEN`（辅助 `≤-add-right`/`+-right-mono`/`+-left-mono`/`≤-add`/`BLEN-nonzero`/`one≤bits`） |
| `C-180` | 修复后的公式编码 `codeF'`（`φ ↦ codeBits (bitsF φ)`）带全解码器 `decF` 与往返 `decF (codeF' φ) ≡ φ`，故**单射** | `codeF'`、`decF`、`codeF'-roundtrip`、`codeF'-injective` |

**两个新教训（已写入 `LESSONS` #96）**：

1. **模式参数要放最前**：`run` 的第一个参数是 `Mode`（永远是构造子）。若把位串放前面，`eqRight` 那一步的位串是**卡住的**
   `bits u ++ rest`，Agda 就无法在不知道位串构造子的情况下选择子句，于是"定义上相等"的等式也证不出来——改写顺序一次解决。
2. **命题步骤要写成引理**：`tmFrom` 与 `res` 的等同是**命题**而非定义上的等同，直接 `refl` 必然失败；把带 `tmFrom …` 的
   目标写成独立引理（`tmFrom-run`、`eq-node`、`eqRight-step`），让 `rewrite` 有确定的可改写位置，再用 `SP.subst'` 显式搬运燃料/位串。

**修复义务的现状**：C-176（`Tm`）+ C-180（`Fml`）合起来给出**可解码、故单射**的 Nat 值编码；C-165 的否定结论因此被"存在性修复"正面回答。
仍未做：公式层与对象层替换（`substF`/`substFix` 系列）的对齐、`⌜·⌝` 的算术化表示、以及证明谓词 `P` 的表示性、反射与对角不动点。

**运行**：`HoTT/verification/runs/20260913-MP-ERCF3-T3-FORMULA-CODING-001-01/`（`KERNEL_ACCEPTED_WITH_SCOPE`、
exit 0、stderr 0、`INDEXED_IN_CLAIM_EVIDENCE_MATRIX`）+ `index-row-manifest.json`（5 行冻结）。

**校验入口**：与 §1.4 同（builtins-only 脉冲链 ⇒ canonical 入口是 `verify_proof_version_closure.py` 的
`later_packages` 分支与 run 自身的 `RUN.json` + `index-row-manifest.json`）。

**禁止外推**：只覆盖 `Fml` 的编码/解码与单射性；不宣称公式层替换一致、不构造 `P` 或对角不动点；
`BitCoding`/`StreamingParser` 与全部历史脉冲文件逐字节未改（两次 run 的 `source-manifest.json` 可交叉核对）；ERCF-3 保持 `GATED`。

---

## 8. `MP-ERCF3-T3-REPAIRED-SYNTAX-001`：修复编码之上的替换一致与引用

旧编码要在"码级替换"与"语法级替换"之间补一条联合递归工程（C-157–C-159）。修复编码有了解码器之后，这件事变成**推论**：
码级替换直接定义为"解码—替换—编码"。

| claim | 精确命题 | 源码标识 |
|---|---|---|
| `C-181` | 项层：`substCodeT k n c = codeT' (substT k n (dec c))` 满足 `substCodeT k n (codeT' t) ≡ codeT' (substT k n t)` | `substCodeT`、`substCodeT-agrees` |
| `C-182` | 公式层：`substCodeF k n c = codeF' (substF k n (decF c))` 满足 `substCodeF k n (codeF' φ) ≡ codeF' (substF k n φ)` | `substCodeF`、`substCodeF-agrees` |
| `C-183` | 引用 `⌜ φ ⌝' = num (codeF' φ)` **单射**；对角实例 `diagonalize' φ = substF (codeF' φ) 0 φ` 是替换实例，且 `codeF' (diagonalize' φ) ≡ substCodeF (codeF' φ) 0 (codeF' φ)` | `⌜_⌝'`、`⌜-injective'`、`diagonalize'`、`diagonalize'-is-subst`、`diagonalize'-code` |

**诚实边界**：`substCodeT`/`substCodeF` 是**经由解码器**定义的（解码—替换—编码），所以"一致"是精确的，但本包**不**主张对象理论
（`ObjectSyntax` 的 `⊢_` 系统）能表示这个替换或引用函数。那条义务（表示性）需要把算术/表示层真正建起来，仍归**门 B**。
本包交付的是对角引理所需的**形状**：引用单射 + 对角实例 + 码级替换可算出对角实例的码。

**运行**：`HoTT/verification/runs/20260913-MP-ERCF3-T3-REPAIRED-SYNTAX-001-01/`（`KERNEL_ACCEPTED_WITH_SCOPE`、
exit 0、stderr 0、`INDEXED_IN_CLAIM_EVIDENCE_MATRIX`）+ `index-row-manifest.json`（4 行冻结）。

**校验入口**：与 §1.4 同（builtins-only 脉冲链 ⇒ canonical 入口是 `verify_proof_version_closure.py` 的
`later_packages` 分支与 run 自身的 `RUN.json` + `index-row-manifest.json`）。

**禁止外推**：不构造证明谓词 `P`、不证明表示性/反射/对角不动点；不重做旧 `codeT`/`codeF` 的 `substFix` 义务；
`BitCoding`/`StreamingParser`/`FormulaCoding` 与全部历史脉冲文件逐字节未改（三次 run 的 `source-manifest.json` 可交叉核对）；ERCF-3 保持 `GATED`。

---

## 9. `MP-ERCF3-T3-C168-COUNTERCHECK-001` 与 `MP-ERCF3-T3-CODING-IMAGE-001`：独立审计吸收（F1）

外部独立审计（`audit/imports/audit-c168-20260913/`，发现 F1）指出 §4 的 C-168 叙述把 **`double` 的性质**
误写成 **`codeAtom` 的性质**，并用机器反证证明 `codeAtom` 满射。本 repo 的处理分两步：

| package | claim | 精确命题 | 源码 |
|---|---|---|---|
| `MP-ERCF3-T3-C168-COUNTERCHECK-001` | `C-184` | `codeAtom (anum zero) ≡ suc zero`——`1` 有显式原像 | `C168Countercheck.agda`（`one-has-codeAtom-preimage`） |
| （同上） | `C-185` | `(n : Nat) → Σ' Atom (λ a → codeAtom a ≡ n)`——`codeAtom` **满射** | `codeAtom-surjective` |
| `MP-ERCF3-T3-CODING-IMAGE-001` | `C-186` | `(t : Tm) → codeT' t ≢ suc zero`——修复后的项编码不含 `1` | `CodingImage.agda`（`codeT'-misses-one`） |
| （同上） | `C-187` | `(φ : Fml) → codeF' φ ≢ suc zero`——修复后的公式编码不含 `1` | `codeF'-misses-one` |

**两条纪律**（本包的意义不只在数学）：

1. **原行与原 run 收据保持原样**：`HoTT/CLAIM_EVIDENCE_MATRIX.md` 的 C-168 行与 `20260913-MP-ERCF3-T3-ARITH-TAGS-001-01/`
   的冻结行哈希逐字节未改；更正以**新的追加节 + 新 claim**登记（矩阵 append-only 要求）。
2. **撤回后必须补上真正成立的依据**：`codeT'`/`codeF'` 的全解码器需要缺省分支这一点**仍然成立**，
   但它由 C-186/C-187（它们自身的像不含 `1`）证明，而不是由被撤回的 C-168 叙述。

**运行**：`HoTT/verification/runs/20260913-MP-ERCF3-T3-C168-COUNTERCHECK-001-01/`、
`HoTT/verification/runs/20260913-MP-ERCF3-T3-CODING-IMAGE-001-01/`（均 `KERNEL_ACCEPTED_WITH_SCOPE`、exit 0、stderr 0、
`INDEXED_IN_CLAIM_EVIDENCE_MATRIX`；各自的 `source-manifest.json` 固定**完整传递闭包**，共 9 / 11 个文件）。

**旁注（审计发现 F6）**：`ARITH-TAGS`、`BIT-CODING`、`STREAMING-PARSER`、`FORMULA-CODING`、`REPAIRED-SYNTAX` 五个**历史** run
只固定了直接导入的模块，未列入编译器实际检查的传递依赖（`DiagonalLemma.agda`；`REPAIRED-SYNTAX` 另缺 `DecodingFence.agda`）。
该缺口登记在 `HoTT/verification/PROOF_VERSION_CLOSURE.json` 的 `later_package_dependency_gap_allowlist`（6 条，注明"不回填历史 manifest"），
`verify_proof_version_closure.py` 会拒绝任何**新增**的未登记缺口。
