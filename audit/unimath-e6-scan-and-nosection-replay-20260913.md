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

## 3. E6 外部源码扫描（固定语料：agda-unimath@7b81411d）

本节现在严格定级为 `SOURCE_INSPECTED_BOUNDED_NEGATIVE`。它回答的是：**在固定源码中，哪些相关接口、反例和正控制可精确定位；S088 保存的 C-05 kernel run 实际检查了哪些模块与公设边界？** 它不是全库语义证明，也不把没有进入 run 的模块称为“本轮机器反证”。可复现机器收据为 `audit/agda-unimath-e6-source-scan-20260913.json`，canonical manager 为 `scripts/audit/scan_agda_unimath_e6.py`。

1. **源码中显式命名提升接口**：`src/foundation/hilberts-epsilon-operators.lagda.md:35–36` 定义 `ε-operator-Hilbert A = type-trunc-Prop A → A`。这证明固定源码含该定义；不证明存在任意 `A` 的该算子。
2. **`no-global-choice` 仅为本轮 source-inspected**：`src/foundation/global-choice.lagda.md:35–50` 定义 `Global-Choice` 与 `no-global-choice`，后者源码直接调用 `no-section-type-2-Element-Type`。但 S088 的保存命令只检查 `hott-z.NoCanonicalPoint` 及其 485 个外部依赖模块；`foundation.global-choice` 不在 stdout 闭包。因此当前身份是 `SOURCE_INSPECTED_NOT_REPLAYED_BY_THIS_RUN`，不能写成 S088 已由 kernel 检查的“最强反证”。
3. **显式前提下的正控制为 source-inspected**：固定源码中可定位 `ε-operator-count`、`ε-operator-is-decidable` 与 `ε-operator-Hilbert-has-double-negation-elim`。它们说明提升接口在携带 `count`、可判定性或 double-negation elimination 时有定义；本轮没有把这些模块全部提升为新的项目数学 claim。
4. **literate-aware 公设口径**：脚本只统计 `.lagda.md` 的 fenced `agda` 代码块与 `.agda` 正文中行首 `postulate`/`primitive` 声明。结果是 **20 个 postulate 文件、9 个 primitive 文件、并集 22 个文件**。此前“32 个文件”没有可复现规则，撤回。普通行首 grep 会得到 24/26，但其中多出的 4 个 `postulate` 命中位于 Markdown prose（`foundation/propositional-truncations` 与三个 modal 文档），不是代码声明。
5. **实际 C-05 run 的公设/primitive 闭包**：486 条 `Checking` 中 1 条是项目目标、485 条来自固定外部树；其中 7 个文件含真实声明：`foundation/function-extensionality`、`foundation/univalence`、`foundation/truncations`、`foundation/replacement`、`synthetic-homotopy-theory/circle`、`synthetic-homotopy-theory/pushouts`、`reflection/erasing-equality`。最后一项含 `primitive`，其余含 `postulate`。所以该结果是相对于 agda-unimath 显式基础的 kernel replay，不是无公设证明。
6. **不安全选项的精确清点**：脚本确认仅 `src/type-theories/simple-type-theories.lagda.md` 与 `src/type-theories/unityped-type-theories.lagda.md` 含 `--allow-unsolved-metas`；它们不在 C-05 保存 run 的相关 E6 论证中。该 lexical 事实不等于完整语义安全认证。
7. **有界结论**：在上述固定源码锚点和命名接口范围内，没有取得一个未声明额外前提的下游 E6 使用链；源码反而展示了拒绝和带前提正控制。继续搜索应转向真实下游应用/派生开发，而不是把基础库中被正确围栏的接口重复计为 E6。

**判词**：`SOURCE_INSPECTED_BOUNDED_NEGATIVE`。E6 仍开放；不证明全库或所有下游开发不存在 E6，也不证明 `foundation.global-choice` 已由 S088 run 重放。

## 4. 工程与治理注记

- 为让"外部库重放"进入统一证据契约，本轮做了两处**原则化扩项**（不是为本次求绿而放宽）：
  1. `verify_formal_proof_run.py` 的 Agda 变体检查改为按 `theory_variant` 分支：cubical 变体仍要求 `--safe --cubical`；without-K 变体要求 `--without-K --exact-split`；其余变体 fail closed。分支按 without-K 优先匹配，避免"no cubical features"这类描述性文字误触发 cubical 要求（该误报在本轮实际发生并已修正；回归确认 MP-NOCANONICAL-001-02、MP-TRUNC-NORECOVERY-001-03、MP-ERCF-001-02 仍 PASS_WITH_SCOPE）。
  2. 外部树依赖标签扩展为 `{cubical-extracted-tree, agda-unimath-extracted-tree}`，两者的确定性树校验相同。
- `-02` 的 `index-row-manifest.json` 在矩阵行文本修正为指向 final run 后被重生成一次；旧 manifest（sha256 `25ac098c…`）与新 manifest（`45d025fb…`）的替换已在此显式记录，RUN.json 的原始运行证据未被改写（仅索引绑定字段按 mark/freeze 流程更新）。
- 本轮下载遵循 `external-large-download` Skill：确认外置盘与容量、Range/ETag 探针、单连接降级、`gzip -t`/tar 结构校验、原始归档保留、失败现场保留。
- 后续独立审计补入 literate-aware 扫描 manager、单元测试和 JSON 收据；它不改写 S088 的 kernel stdout，而是把源码审读、导入闭包与公设边界分开定级。

## 5. 不能推出

- 不主张定理原创性：`no-section-type-2-Element-Type` 是 agda-unimath 的定理，本轮只重放派生文件的导入链。
- 不把结论外推到其它提交、其它库版本、其它开发或"不存在任何消费者"；负结论限定在被固定的这一份语料（3,166 文件）与该提交。
- 不证明 HoTT 内部矛盾；不把 global-choice 的被反证读作 HoTT 的缺陷——那是库对不安全提升的正确拒绝（与被拒绝对象一致的资格分离）。
- E6 未被本次扫描证伪为"任何地方都不存在"；它仍是开放搜索目标。
