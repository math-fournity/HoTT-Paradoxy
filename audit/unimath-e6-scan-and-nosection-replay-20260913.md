# N42：固定版本 agda-unimath 的 E6 外部扫描与 no-section 派生文件原生重放（S088）

日期：2026-09-13。Session：`S-RES-20260913-088-N42-UNIMATH-REPLAY`。本轮完成 N42(a)：把 S083（N37）遗留的 `SOURCE_REPORTED_NOT_REPLAYED` 收口为可复跑的 kernel 证据，同时把 E6（真实自然使用链的资格越级）搜索面扩大到一份真实的大型 HoTT 开发库。

## 1. 外部来源的固定与完整性边界

| 项 | 记录 |
|---|---|
| 库 | agda-unimath（`https://github.com/UniMath/agda-unimath`） |
| 固定提交 | `7b81411d9f60afec359d29ed1e4edf43f4711c8a`（下载当日默认分支 HEAD） |
| 取得方式 | `https://codeload.github.com/UniMath/agda-unimath/tar.gz/<commit>`；单连接 aria2 1.37.0（`--split=1 --max-connection-per-server=1`） |
| Range 探针 | `Range: bytes=0-0` 返回 **200**（非 206）→ codeload 不支持分片/续传，按 `external-large-download` Skill 降级为单连接并记录边界 |
| 表示约束 | 探针得到的强 ETag `"e34d6865…53ba"` 以 `If-Match` 前置条件发送，未返回 412 |
| 归档 | 11,938,845 bytes；本机 SHA-256 `552bc6102be8ce952226528dbc256c07f2993038dd182e501c877cc096b664b6`；`gzip -t` 通过；tar 成员 3,226 |
| 发布方摘要 | **无**：GitHub 不为 codeload commit tarball 发布 SHA-256；身份 = commit SHA + ETag 前置条件 + 本机哈希 + 结构校验。本机哈希只证明本地字节身份，不是独立发布方证明 |
| 解包树 | 3,166 文件 / 31,596,894 bytes；确定性树哈希 `88460bc7d2e0ffd2bc85d60ca7fa0ea8e0b833bc12e1e6e9cd18ccd517db41c5`（排除 `*.agdai`、`.DS_Store`） |
| 库文件 | `agda-unimath.agda-lib`，191 bytes，SHA-256 `d42bd31b…6221`；flags 与派生文件 OPTIONS 完全一致（`--without-K --exact-split --no-import-sorts --auto-inline --no-require-unique-meta-solutions -WnoWithoutKFlagPrimEraseEquality --no-postfix-projections`） |
| Agda 兼容性 | 该提交的 `flake.nix` 注明其 pinned nixpkgs 携带 Agda 2.8.0；重放使用本 repo 既有固定二进制 Agda 2.8.0-3d04bac（`ac285c19…741e`） |
| 落盘 | 库与下载件位于 `/Volumes/D/HoTT-toolchain-cache/`（外置 D 盘）；repo 内只保存身份文件 `HoTT/formal/agda-unimath/UNIMATH_TOOLCHAIN.json` 与 `AGDA_LIBRARIES` |

## 2. 原生重放收据（C-05）

- 目标：`HoTT/formal/agda-unimath/hott-z/NoCanonicalPoint.agda`（用户侧派生文件，模块 `hott-z.NoCanonicalPoint`；导入 `foundation.negation`、`foundation.universe-levels`、`univalent-combinatorics.2-element-types`）。
- final run：`HoTT/verification/runs/20260913-MP-UNIMATH-NOSECTION-REPLAY-02/`；Agda 2.8.0-3d04bac + agda-unimath@`7b81411d`；`--ignore-interfaces`（全量重检 486 个模块）；exit 0；**stderr 0 bytes**；`EXACT_INDEX_SNAPSHOT_MATCH`、`EXACT_EXIT_STDOUT_STDERR_MATCH`。
- 保留的失败 run：`…-REPLAY-01`（`KERNEL_REJECTED`，exit 42）——`-i` 误用源文件父目录，Agda 报 `ModuleNameDoesntMatchFileName`；失败被原样保留，修正为 `--include-root HoTT/formal/agda-unimath` 后以 `-02` 重跑。这是"配置错误 ≠ 数学拒绝"的又一实例。
- 定理位置：`agda-unimath@7b81411d` 的 `src/univalent-combinatorics/2-element-types.lagda.md:501` 定义 `no-section-type-2-Element-Type`；派生文件把"无统一选点"包装为 `no-canonical-point` 与 `no-canonical-pointed-orientation`。
- 索引：claim matrix 新增 proof 行 `MP-UNIMATH-NOSECTION-REPLAY-001`；`C-05` 行原位更新为 `MACHINE_REPLAYED_EXTERNAL_LIBRARY_WITH_SCOPE`（历史记录中的旧 commit 简写与当时薄封装编译保留在 Git/ledger）；`MP-LEGACY-NO-CANONICAL-POINT` 行的门禁身份更新为已被固定重放取代。

## 3. E6 外部扫描（固定语料：agda-unimath@7b81411d）

本扫描的问题是：**在这份真实库里，有没有模块把较弱的资格（截断/简并存在）当作较强资格（数据/section）来交付，且不声明额外假设？** 结论是：没有；而且库本身把这个"自然消费者"显式命名、给出正控制并整体反证。

1. **提升接口被显式命名并明确不假设**：`foundation/hilberts-epsilon-operators.lagda.md` 定义 `ε-operator-Hilbert A = type-trunc-Prop A → A`，并写明 "Contrary to Hilbert, we will not assume that such an operator exists for each type `A`"。
2. **整体提升被库内反证**：`foundation/global-choice.lagda.md` 定义 `Global-Choice l = (A : UU l) → ε-operator-Hilbert A`，并证明 `no-global-choice : ¬ (Global-Choice l)`：证明**直接调用 `no-section-type-2-Element-Type`**（即本 repo 派生文件所导入的同一定理）。换言之，最自然的 E6 形状（全局提升）在真实库中不是被越级使用，而是被机器反证。
3. **axiom-of-choice 模块记录同一结论**：`foundation/axiom-of-choice.lagda.md` 说明 AC 对任意类型不成立，其反例形式化于 `foundation.global-choice`，并指出该假设与 univalence 及 HIT 不相容（引用 Rij22 Cor 17.5.3）。
4. **带显式数据/假设的提升（正控制）**：`univalent-combinatorics/finite-choice.lagda.md` 给出 `ε-operator-count : count A → ε-operator-Hilbert A`（以及 decidable subtype、嵌入版本）；`foundation/decidable-types.lagda.md` 给出 `is-decidable A → ε-operator-Hilbert A`；`logic/double-negation-elimination.lagda.md` 给出 `has-double-negation-elim A → ε-operator-Hilbert A`；`elementary-number-theory/well-ordering-principle-*` 在有限/可判定假设下使用 ε 算子。这与本 repo 的 C-146 正控制模式一致：**保留资格数据即可选择，遗忘它就不行**。
5. **公设面清点（32 个文件）**：`reflection/*`（4）、`primitives/*`（4）、`modal-type-theory/*`（6）、`synthetic-homotopy-theory/*`+`synthetic-category-theory/*`+`globular-types/*`（5）、`foundation-core/*`+`foundation/*`（11）、`literature/*`（1）、`elementary-number-theory/equality-conatural-numbers`（1）。其中 `foundation/truncations.lagda.md` 的公设只是 HIT 编码（type former + unit + universal property），消去仍只能进入相应截断层类型；`function-extensionality-axiom` 等是显式公理选择；没有"截断→数据"的公设。
6. **不安全选项清点**：仅 `type-theories/simple-type-theories.lagda.md` 与 `type-theories/unityped-type-theories.lagda.md` 使用 `--allow-unsolved-metas`（研究对象是类型论本身的研究性模块，与截断接口无消费者关系）；`reflection/rewriting` 与 `modal-type-theory/sharp-modality` 使用 `REWRITE`（与截断-数据提升无关）。
7. **类型围栏**：截断消去器（`rec-trunc-Prop`/`apply-universal-property-trunc-Prop`）与 set-quotient 消去器在库中均以"目标必须是截断层/集合"的形式给出，编译器层面阻止把命题截断消去到数据。

**判词**：`BOUNDED_NEGATIVE_WITH_STRONGEST_COUNTEREXAMPLE`——在固定提交的 agda-unimath 中，未发现 E6；且最自然的提升消费者（global choice）被真实库用与本项目同源的 no-section 定理反证。E6 仍是唯一升格口，判词阶梯不变。

## 4. 工程与治理注记

- 为让"外部库重放"进入统一证据契约，本轮做了两处**原则化扩项**（不是为本次求绿而放宽）：
  1. `verify_formal_proof_run.py` 的 Agda 变体检查改为按 `theory_variant` 分支：cubical 变体仍要求 `--safe --cubical`；without-K 变体要求 `--without-K --exact-split`；其余变体 fail closed。分支按 without-K 优先匹配，避免"no cubical features"这类描述性文字误触发 cubical 要求（该误报在本轮实际发生并已修正；回归确认 MP-NOCANONICAL-001-02、MP-TRUNC-NORECOVERY-001-03、MP-ERCF-001-02 仍 PASS_WITH_SCOPE）。
  2. 外部树依赖标签扩展为 `{cubical-extracted-tree, agda-unimath-extracted-tree}`，两者的确定性树校验相同。
- `-02` 的 `index-row-manifest.json` 在矩阵行文本修正为指向 final run 后被重生成一次；旧 manifest（sha256 `25ac098c…`）与新 manifest（`45d025fb…`）的替换已在此显式记录，RUN.json 的原始运行证据未被改写（仅索引绑定字段按 mark/freeze 流程更新）。
- 本轮下载遵循 `external-large-download` Skill：确认外置盘与容量、Range/ETag 探针、单连接降级、`gzip -t`/tar 结构校验、原始归档保留、失败现场保留。

## 5. 不能推出

- 不主张定理原创性：`no-section-type-2-Element-Type` 是 agda-unimath 的定理，本轮只重放派生文件的导入链。
- 不把结论外推到其它提交、其它库版本、其它开发或"不存在任何消费者"；负结论限定在被固定的这一份语料（3,166 文件）与该提交。
- 不证明 HoTT 内部矛盾；不把 global-choice 的被反证读作 HoTT 的缺陷——那是库对不安全提升的正确拒绝（与被拒绝对象一致的资格分离）。
- E6 未被本次扫描证伪为"任何地方都不存在"；它仍是开放搜索目标。
