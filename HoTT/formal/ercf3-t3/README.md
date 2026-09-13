# ERCF-3 T3 脉冲链（含五个 claim-bearing package）

> 判词只覆盖本目录的编码层义务；**ERCF-3 本体保持 `GATED`**（C8 §9 的 P1–P8 与停止条件不变）。
> 快速索引：`HoTT/CLAIM_EVIDENCE_MATRIX.md` 的追加节；版本登记：`HoTT/verification/PROOF_VERSION_CLOSURE.json` 的 `later_packages`。

| package | claims | 源码 | run | 判词 |
|---|---|---|---|---|
| `MP-ERCF3-T3-JOINT-001` | `C-157`–`C-159` | `JointRecursion.agda` | `20260913-MP-ERCF3-T3-JOINT-001-02` | `MACHINE_PROVED_LOCAL_UNCOMMITTED / ERCF3_T3_SHARED_DECISION_JOINT_RECURSION` |
| `MP-ERCF3-T3-DECODING-001` | `C-160`–`C-162` | `DecodingFence.agda` | `20260913-MP-ERCF3-T3-DECODING-001-01` | `MACHINE_PROVED_LOCAL_UNCOMMITTED / ERCF3_T3_DECODABILITY_FENCE` |
| `MP-ERCF3-T3-REPAIR-SPEC-001` | `C-163`–`C-165` | `CodingRepair.agda` | `20260913-MP-ERCF3-T3-REPAIR-SPEC-001-01` | `MACHINE_PROVED_LOCAL_UNCOMMITTED / ERCF3_T3_REPAIR_SPECIFICATION` |
| `MP-ERCF3-T3-ARITH-TAGS-001` | `C-166`–`C-168` | `ArithmeticTags.agda` | `20260913-MP-ERCF3-T3-ARITH-TAGS-001-01` | `MACHINE_PROVED_LOCAL_UNCOMMITTED / ERCF3_T3_ARITHMETIC_TAGS_FRAGMENT` |
| `MP-ERCF3-T3-BIT-CODING-001` | `C-169`–`C-172` | `BitCoding.agda` | `20260913-MP-ERCF3-T3-BIT-CODING-001-01` | `MACHINE_PROVED_LOCAL_UNCOMMITTED / ERCF3_T3_BIT_SUBSTRATE` |

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
| `C-168` | 该编码**非满射**（`1` 无原像），故任何**全**解码器必须带缺省分支 | `one-has-no-preimage` |

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

**剩余算术义务（下一有界脉冲）**：符号层（`var n`/`num n` 的**自定界**索引位 + 构造子标签）与带缺省分支
（C-168）的解析器，然后证明像上的往返；由 C-164，该往返自动给出完整 Nat 值编码 `t ↦ codeBits (bits t)` 的**单射**。

**运行**：`HoTT/verification/runs/20260913-MP-ERCF3-T3-BIT-CODING-001-01/`（`KERNEL_ACCEPTED_WITH_SCOPE`、exit 0、
stderr 0、`INDEXED_IN_CLAIM_EVIDENCE_MATRIX`）+ `index-row-manifest.json`（5 行冻结）。

**校验入口**：与 §1.4 同——本目录全部包都在 builtins-only 脉冲链上，`verify_formal_proof_run.py` 对它们会报
`AGDA_SAFE_CUBICAL_OPTIONS_REQUIRED`（那是 cubical 包的适用域）；canonical 校验入口是
`verify_proof_version_closure.py` 的 `later_packages` 分支与 run 自身的 `RUN.json` + `index-row-manifest.json`。

**禁止外推**：不给出符号层、解析器或全解码器；不声称完整 `Tm` 已有 Nat 值单射编码；往返只在**已知长度/自身码**上成立；
不涉及 P 表示性/反射/对角不动点；ERCF-3 保持 `GATED`；历史脉冲文件不改写。
