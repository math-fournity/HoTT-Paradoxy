# MP-ERCF3-T3-JOINT-001：ERCF-3 T3 共享判定联合递归

> 状态：`MACHINE_PROVED_LOCAL_UNCOMMITTED / ERCF3_T3_SHARED_DECISION_JOINT_RECURSION`
> 判词只覆盖本目录的编码层义务；**ERCF-3 本体保持 `GATED`**（C8 §9 的 P1–P8 与停止条件不变）。
> 快速索引：`HoTT/CLAIM_EVIDENCE_MATRIX.md` 的追加节（`C-157`–`C-159`）；版本登记：`HoTT/verification/PROOF_VERSION_CLOSURE.json` 的 `later_packages`。

## 1. 精确命题

固定工具链与语法（`ObjectSyntax.agda` 的 `Tm`/`Fml`、`DiagonalCore.agda` 的 `codeT`/`codeF`、`CodeStoreFix.agda` 的 `substFixT`、`DecisionParam.agda` 的 `substFixTd`）。本包机器检查三条：

| claim | 精确命题 | 源码标识 |
|---|---|---|
| `C-157` | `(d : Bool) (k i : Nat) (t : Tm) → substFixTd d k i t ≡ codeT (substTd d k i t)`（显式共享判定下码级修正替换与语法级替换一致） | `JointRecursion.substFixTd-agrees` |
| `C-158` | `(k i : Nat) (t : Tm) → substFixT k i t ≡ codeT (substT k i t)`（**原始逐出现判定**的项层恒等式——N34 记录的剩余义务） | `JointRecursion.fixT-agrees` |
| `C-159` | `(k i : Nat) (φ : Fml) → substFixFc k i φ ≡ codeF (substF k i φ)`（修正后的公式层码替换与语法替换一致） | `JointRecursion.substFixFc`、`JointRecursion.fixF-agrees`（见 §3） |

## 2. 来源与脉冲谱系

- S067–S080 的 13 个脉冲把该义务逐步逼到"两侧必须共享同一判定 → 联合递归"（`TermIdentityFinal.agda` 的注释与 `S-RES-20260913-080` 的记载）；
- S079 的修法 (b) 把**码级**替换改成判定值显式参数（`substFixTd`）；
- 本包在同一步把**语法级**替换也改成显式判定（`substTd`），于是三项都成为普通归纳；
- `C-158` 不需要显式共享判定：只有 `var` 分支做判定分叉，因此**逐出现判定**的项层恒等式可以单 `with` 收口（`fixT-agrees`）。

## 3. 修正记录（不重写历史文件）

`CodeStoreFixF.agda`（S075 脉冲）的公式层码替换在 `all` 的**影子分支**（`i =n m` 为真）写的是
`1+1+1+1+1 + (m + codeF (all m φ))`，即对整条量化公式**双重编码**；语法层 `substF k i (all m φ)` 在该分支保持
`all m φ` 不代入，其码应为 `1+1+1+1+1 + (m + codeF φ)`。本包在新模块中给出修正函数 `substFixFc` 并机器检查 `C-159`。
历史脉冲文件与其会话证据**逐字节未改**；本修正以新模块 + 本 README + 矩阵追加节的形式登记。

## 4. 运行与证据

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

## 5. 禁止外推

- **不是** ERCF-3 本体：不构造对角线不动点，不涉及证明谓词 `P` 的表示性、反射或自应用；不改变 ERCF-3 的 `GATED` 状态；
- **不是** HoTT 悖论或 HoTT 内部不一致；本包不使用 univalence、cubical Path、HIT 或 truncation；
- 不把编码层一致升级成"对角引理已形式化"或"对象层替换算术化已完成"；
- 只覆盖上述三条精确命题与固定工具链；不覆盖 `substF` 的其它性质或其它编码方案。
