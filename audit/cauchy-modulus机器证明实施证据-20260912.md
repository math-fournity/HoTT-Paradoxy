# MP-CAUCHY-MODULUS-001 机器证明实施证据：Cauchy modulus 边界

> 文档身份：`CURRENT PROOF-PACKAGE EVIDENCE`
> 日期：2026-09-12
> 触发：S050 后的 N9 工作包——用同一原生 Cubical 工具链固定 Cauchy 序列/等价的最小模型，判别“按极限值取商”是否保留指定的 modulus，并把可得的外部 Real 库接口作为固定审计子项。
> 结论：**`MACHINE_PROVED_LOCAL_UNCOMMITTED / CAUCHY_MODULUS_BOUNDARY_WITH_POSITIVE_CONTROLS`**——按极限值取商保留 limit 但忘掉表示携带的 modulus，任何从商出发的函数不能统一恢复该 modulus；把 modulus 加入同一性判据后可以下降（正控制）。这是第二级表示边界，不是 HoTT 悖论。

## 0. 判词与范围

| 项 | 内容 |
|---|---|
| proof ID | `MP-CAUCHY-MODULUS-001` |
| claim IDs | `C-129`–`C-133` |
| 判词 | `CAUCHY_MODULUS_BOUNDARY_WITH_POSITIVE_CONTROLS` |
| 判词级别 | 第二级（`REPRESENTATION_BOUNDARY` 类）：限制定理 + 细化表示正控制，不升级为 `NATURAL_USAGE_MISMATCH` 或 `INTERNAL_INCONSISTENCY` |
| 支持语义 | Agda 2.8.0 + Cubical v0.9 原生 `SetQuotients`（`--safe --cubical --guardedness`） |
| 依据 | 精确 source、kernel run、原始 stdout/stderr、外部依赖哈希和逐行索引 manifest 全部在 repo 内 |
| Git 状态 | 未 commit/tag/push；`LOCAL_UNCOMMITTED_NOT_VERSION_CLOSED` |

## 1. 固定模型与工具链

最小模型（全部在 `HoTT/formal/cauchy-modulus/CauchyModulus.agda`）：

```text
Seq    = ℕ → Bool
Cauchy = Σ[ s ∈ Seq ] Σ[ N ∈ ℕ ] (∀ n → le N n → s n ≡ s N)     -- 序列 + 给定 modulus
seq c = fst c；mod c = fst (snd c)；lim c = seq c (mod c)
c0 = (constTrue , 0 , ·)；c1 = (constTrue , 1 , ·)
Q  = Cauchy / _≈_   其中 c ≈ d := lim c ≡ lim d                  -- 只看极限值
Q' = Cauchy / _≈'_  其中 c ≈' d := (mod c ≡ mod d) × (lim c ≡ lim d)
```

工具链身份与其余十三个包一致：Agda 2.8.0-3d04bac（`/Volumes/D/HoTT-toolchain-cache/agda-v2.8.0-macos-arm64/`），Cubical v0.9（tag commit `b150186d2544e7efeddd31e5d14a8b9ecbb100f7`，tree SHA-256 `73ccfbaf960f252800da02dac6a9bbef72d1214e2907940466dc2abef2060a81`）；外部依赖身份记录在 `TOOLCHAIN.json` 与 run 的 `environment.txt`/`source-manifest.json`。

## 2. 冻结命题（`C-129`–`C-133`）

| claim | 形式化结果 | 关键证据（`CauchyModulus.agda`） |
|---|---|---|
| `C-129` | limit 下降到商：存在 `C-129-limit : Q → Bool`。正控制：商保留极限值 | `SQ-rec isSetBool lim (λ c d p → p)` |
| `C-130` | `c0 ≈ c1`（两者极限都是 `true`），但 `mod c0 ≢ mod c1`（`0 ≢ 1`） | `C-130-related = refl`；`C-130-moduli-differ = zero≠suc 0` |
| `C-131` | 不存在 `f : Q → ℕ` 同时满足 `∀ c → f [c] ≡ mod c`（统一 modulus 恢复 no-go） | `C-131-no-modulus-recovery (f , hf) = zero≠suc 0 (sym (hf c0) ∙ cong f (eq/ c0 c1 C-130-related) ∙ hf c1)` |
| `C-132` | 细化商有 `C-132-modulus-refined : Q' → ℕ`（把 modulus 纳入同一性后可以下降；正控制） | `SQ-rec isSetℕ mod (λ c d p → fst p)` |
| `C-133` | 细化关系不识别两个表示：`¬ (c0 ≈' c1)` | `C-133-refined-not-related p = zero≠suc 0 (fst p)` |

`C-131` 的证明是标准对角/同一性论证的原生实例：`c0` 与 `c1` 在 `Q` 中被识别（`eq/`），任何只在商上定义且满足恢复规范的 `f` 必须给出 `0 ≡ 1`；因此该规范不可满足。它与 C5 的 E1–E5 升级链形状一致：信息在取商（同一化）时被合并，恢复函数不存在，而细化表示恢复资格。

## 3. 运行、索引与旧包回归

final run：`HoTT/verification/runs/20260912-MP-CAUCHY-MODULUS-001-01/`

| 项 | 值 |
|---|---|
| kernel | Agda 2.8.0-3d04bac + Cubical v0.9，`--ignore-interfaces` 重编译 |
| exit code | `0` |
| warnings | `0`（stdout 中 `warning` 计数为 0） |
| stdout | 11,347 bytes，SHA-256 `50f36f6253ea5f4a4a7eb919ae1d74cec93abcdedaa863d7bd6b7b0e1a88be83` |
| stderr | 0 bytes，SHA-256 `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`（空文件原样保留） |
| RUN.json | `KERNEL_ACCEPTED_WITH_SCOPE / INDEXED_IN_CLAIM_EVIDENCE_MATRIX`，SHA-256 `4f719370f34c28f27ddf66b9047ae34a439f62552a5db881847948a0cecfab9b` |
| index-row-manifest | `EXACT_INDEX_SNAPSHOT_MATCH`；矩阵 SHA-256 `22e1c54c02d26e76d6b60309d9f4c1c68418fe6890aef6a4a4f7dbfd3dfda0b4`；manifest SHA-256 `437e898ba4af38145535edf58bc166b477f897d46041fd56aa43c786eb0920b7` |
| 独立重放 | `verify_formal_proof_run.py --rerun`：`PASS_WITH_SCOPE / EXACT_EXIT_STDOUT_STDERR_MATCH` |

矩阵第十二次增长（追加 proof 行 + 5 条 claim 行，`C-129`–`C-133`）后，十三个旧包全部重验为 `ROW_STABLE_AFTER_INDEX_EVOLUTION / EXACT_EXIT_STDOUT_STDERR_MATCH`：

`20260912-MP-ERCF-001-02`、`20260912-MP-ERCF-TRUNC-001-01`、`20260912-MP-RACE-TIMEOUT-001-01`、`20260912-MP-CONTEXTUAL-EQUIV-001-01`、`20260912-MP-QUOTIENT-MONAD-001-01`、`20260912-MP-CONTEXT-CHARACTERIZATION-001-01`、`20260912-MP-GUARD-ERASURE-001-01`、`20260912-MP-COST-FACTORIZATION-001-01`、`20260912-MP-PATH-CERTIFICATE-001-01`、`20260912-MP-ONLINE-CAUSALITY-001-01`、`20260912-MP-TRANSITION-LIFT-001-01`、`20260912-MP-PARTIAL-DECISION-001-01`、`20260912-MP-SIP-REPRESENTATION-001-01`。

其中 ERCF-001、ERCF-TRUNC-001、RACE-TIMEOUT-001 三个包在批量会话输出不可完整捕获后按单包重放补证，结果相同；其余十个包的 row-stable 输出在同一批次中取得。

## 4. 构建失败谱系（按责任点记录，未被冒充为数学拒绝）

1. **`_≤_` 命名冲突**：Cubical v0.9 的 `Cubical.Data.Bool.Properties` 已把 `_≤_ : Bool → Bool → Type` 定义为 Bool 上的序（库第 243 行）。本包的常量性界谓词实为自然数上的关系，故命名为 `le : ℕ → ℕ → Type` 并使用显式递归定义，避免与 Bool 序同名造成歧义。
2. **`SQ-rec` 第一参数是目标集合的 set-ness**：库中 `rec : isSet B → (f : A → B) → ((a b : A) (r : R a b) → f a ≡ f b) → A / R → B`。初版按“先给 f”书写导致类型错误；修正为 `SQ-rec isSetBool lim …` / `SQ-rec isSetℕ mod …`，命题未削弱。

两处均属实现/接口责任点，修复后原命题逐字保留；没有为了通过编译改写 claim。

## 5. 外部 Real 库接口审计（N9 固定子项）

本地 Cubical v0.9 只有 `Rationals`，不含 `Real`/Cauchy 实数模块，故主构造使用自包含最小模型。外部固定审计对象为 **UniMath/agda-unimath `master`**，抓取时 `master` 提交为 `6dc2d58a35d256978aeccb987eb92b9b11ed613a`（committer date `2026-09-11T12:51:21Z`）。抓取日期 2026-09-12（本地时间）；原件保存在
`.codex/research/hott/sessions/S-RES-20260912-051-CAUCHY-MODULUS/evidence/sources/`。

| 对象（`src/` 下路径） | git blob | bytes | SHA-256（抓取字节） | 可核层级 |
|---|---:|---:|---|---|
| `real-numbers/cauchy-sequences-real-numbers.lagda.md` | `2974eb40a9cbaf804405588d4650fd2ecb43b65e` | 7,498 | `8990075c99dd7eeaf85d51978bc36260d7b1541111d101c503df79feb1548aab` | 全文 |
| `real-numbers/modulated-cauchy-sequences-real-numbers.lagda.md` | `b9f448dc1f1c5c160f3021607d37bba7fcd47c8d` | 1,128 | `8de0b2136bed53c3f7345e6c59e96bf895c436cf75db8766543f26b89908ee66` | 全文 |
| `metric-spaces/convergent-sequences-metric-spaces.lagda.md` | `474a9c7325f31349eefad2d5a2b16e170377acc4` | 2,848 | `f6ded48c2c57ed10d67e0bb71cf23cb1e123f36f210922b828b7efb6824dcf96` | 全文 |
| `real-numbers/` 目录列表（GitHub contents API） | — | 184,119 | `9bdffd7086a6c030689bad5ee5963f91bd3dab3bb4b953da5cf7ea978fc63392` | 151 个条目 |
| `commits/master` API 响应 | — | 35,441 | `f51ce13f75e5d2d3fce6b5af77fefddab601e1a08ea500217fd89ccc087c0814` | 版本锚 |

读取结果（与 N9 判别直接相关的三点）：

1. `cauchy-sequences-real-numbers.lagda.md` 的 Idea 明确把 modulus 作为**接口结构**：实数序列“has a convergence modulus if and only if it is Cauchy”（收敛由 `metric-spaces.convergent-sequences-metric-spaces` 的 `has-limit` 数据给出）。
2. 同一文件把完备性定理写成 `opaque has-limit-cauchy-sequence-ℝ`：极限存在，但构造被 opaque 封装，不暴露可计算的 limit 构造。
3. 夹逼定理（squeeze theorem）从显式数据 `c-a→0 : is-zero-limit-sequence-ℝ (λ n → c n -ℝ a n)` 中**析出** modulus `(μ , is-mod-μ) ← c-a→0` 才得到 Cauchy 性；`real-numbers/` 目录另设 `modulated-cauchy-sequences-real-numbers.lagda.md` 结构 `modulated-cauchy-sequence-ℝ := cauchy-modulus-sequence-ℝ`，即把 modulus 作为携带数据的细化表示。

有限解释：agda-unimath 把“极限存在”“收敛 modulus”“modulated Cauchy 序列”分层为不同结构；需要 modulus 的消费者必须持有携带 modulus 的表示，这与本包 `C-131`（商层不能统一恢复）与 `C-132`（把 modulus 纳入同一性即可下降）的边界方向一致。它**不**证明该库在任何具体使用中错误消费了 modulus。

审计限制：只核到上述 3 个文件 + 目录列表 + master 提交锚；`master` 是移动引用，后续变化不回溯改写本记录；未做全库检索，也未审计外层导出/打印模块。

## 6. 解释边界与非目标

- “按极限值取商”保留的是极限值，不是给定 modulus；后者属于表示数据。需要 modulus 的消费者必须保留代表或把 modulus 纳入同一性判据（`C-132` 正控制）。
- 这不是 HoTT 内部矛盾；理论在此正确区分“序列的极限值”与“该序列在给定表示中使用的 modulus”，与截断防御、提取接口审计同为资格分离的正向表现。
- 与 N6 partial/strict 边界的区别：此处缺口是 modulus 表示的同一性，不是 partial/total 判定；与 race/timeout 的区别：此处没有完成先后竞争，只有表示/同一性。
- 非目标：不构造完整 Cauchy reals / 外部 Real 库；不形式化十进制展开或数值打印；不主张任何真实库/系统在无 modulus 时错误提取观察量；不主张原创性（Cauchy 表示的 modulus 依赖是标准现象）。

## 7. 工件与哈希清单（本轮交付引用）

| 路径 | SHA-256 |
|---|---|
| `HoTT/formal/cauchy-modulus/CauchyModulus.agda` | `35fa559186b0debb49d1e9e35330239dd8590a64a125677e67ca603723101b5d` |
| `HoTT/formal/cauchy-modulus/README.md` | `a80d7f2bdfe6f34e1b0a00a3e73a21f7fed1bbcccadd9988385c065390a7ae49` |
| `HoTT/formal/cauchy-modulus/TOOLCHAIN.json` | `151df43c3d32f9d4c0ef306a24fd4596c6595a8928ce0169506a5f5097ac89d2` |
| `HoTT/formal/cauchy-modulus/AGDA_LIBRARIES` | `3dc9309430a79c1764bd9a86d29b96a7f7907f8f6f5638207a9cc4f809591c12` |
| `HoTT/verification/runs/20260912-MP-CAUCHY-MODULUS-001-01/RUN.json` | `4f719370f34c28f27ddf66b9047ae34a439f62552a5db881847948a0cecfab9b` |
| `HoTT/verification/runs/20260912-MP-CAUCHY-MODULUS-001-01/stdout.txt` | `50f36f6253ea5f4a4a7eb919ae1d74cec93abcdedaa863d7bd6b7b0e1a88be83` |
| `HoTT/verification/runs/20260912-MP-CAUCHY-MODULUS-001-01/source-manifest.json` | `4ff12c11bd9149b34c8f0f0e1915f19f31e368469401c58c38b8640b2b830972` |
| `HoTT/verification/runs/20260912-MP-CAUCHY-MODULUS-001-01/environment.txt` | `7b64c3d52bb3892a9426306d8bc5ec6d6f9a1bc3df31c695ace24f41f27566a7` |
| `HoTT/verification/runs/20260912-MP-CAUCHY-MODULUS-001-01/index-row-manifest.json` | `437e898ba4af38145535edf58bc166b477f897d46041fd56aa43c786eb0920b7` |
| `HoTT/CLAIM_EVIDENCE_MATRIX.md`（本次快照） | `22e1c54c02d26e76d6b60309d9f4c1c68418fe6890aef6a4a4f7dbfd3dfda0b4` |

外部来源哈希见 §5；`CauchyModulus.agdai` 是编译器缓存，不作为证明资产，其唯一真实来源是 `CauchyModulus.agda` 与 run 收据。

## 8. 结论

`MP-CAUCHY-MODULUS-001` 在匹配语义的原生 Cubical kernel 中证明了：按极限值取商保留 limit（`C-129`），识别两个 modulus 不同的表示（`C-130`），不存在从商统一恢复给定 modulus 的函数（`C-131`），把 modulus 纳入同一性后可以下降（`C-132`），且细化关系不再识别两表示（`C-133`）。外部 Real 库接口审计与之一致：modulus 是显式结构数据。判词为 `CAUCHY_MODULUS_BOUNDARY_WITH_POSITIVE_CONTROLS`，不升级为 HoTT 悖论。
