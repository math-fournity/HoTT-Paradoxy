# HoTT quotation / later 桥接：固定时钟强制展开与时序擦除候选

状态：`NATIVE_EXPLORATION_REPLAYED / GUARDED_FORCE_ERASURE_CONDITIONAL_COLLAPSE_WITH_DEFENSE / HOTT_BUG_NOT_ESTABLISHED / LOCAL_UNCOMMITTED`

本工作单元承接 `L5-CONSUMER-QUALIFICATION-001`。上一单元发现，通用 `Box` 对角式并不够：Agda 的 `TC`、MetaRocq 的 syntax quotation 和 guarded/clocked HoTT 的 later modality 虽然都有“自应用、推迟或再包装”的外形，却承担不同任务。若只按类型外观或关键词把三者合并，会再次制造一个并不存在的消费者。

本轮首先把三种载体分开：

| role | 真实含义 | 典型操作 | 不能自动得到 |
|---|---|---|---|
| `HOST_TC` | 宿主类型检查器中的一次元计算 | `returnTC`、`bindTC`、`quoteTC`、`checkType`、`unify` | 对象层 `TC A → A`、kernel soundness |
| `SYNTAX_QUOTATION` | 对 term 或 typed proof 的语法编码 | `quote`、`cojoin : □A → □□A` | 代码所代表命题的无条件反射 |
| `TEMPORAL_LATER` | 数据在一个 tick 之后才可用 | `next : A → ▷κ A`、`fixκ : (▷κ A → A) → A` | 固定时钟上的无条件 `▷κ A → A` |

三者的分离不是术语修正，而是决定对角/Löb 构造能否忠实连接真实系统的类型责任。

## 1. 冻结、来源与执行身份

- evaluation：`HOTT-QUOTATION-BRIDGE-001`
- freeze：`BRIDGE-FREEZE.json`
- freeze SHA-256：`29131e2d54a316cf72c4d649aac3308e40e89e80f38cd017d7796863a62e4d96`
- scope：`SCOPE.json`
- decisions：`DECISIONS.json`
- run：`runs/20260913-HOTT-QUOTATION-BRIDGE-001/RUN.json`
- deterministic SHA-256：`df5d3c04c53de827b4a1f2d7bc08e50cb4043bd98fb9a405b5bc2f53b60ef308`
- source systems：6
- pinned artifacts：12
- H1–H6 evidence anchors：66，全部回读成功
- native/toolchain probes：10，全部命中预期，全部 byte-exact replay

来源集合包括：Agda 2.8.0 builtin reflection、Cubical v0.9 reflection、Agda 同 commit 的 `LaterPrims`、GCTT v2、CCTT v3 + `agda/guarded` forcing-ticks commit `cf0c438…`、MetaRocq 9.1 quotation。完整 Cubical v0.9 1,111-file tree与 forcing-ticks 6-file source tree均按整树哈希固定。

Freeze 在 `DECISIONS.json` 和 7 个 repo probe 源文件不存在时写入。设计者仍是当前同一个 AI；因此 freeze 证明来源/角色/判据在结果以前固定，不证明盲测、原创性或一般搜索效果。

## 2. 三种角色的真实接口

### 2.1 Agda `TC`：反射程序仍在宿主检查器中

固定 `Agda.Builtin.Reflection` 源码声明：

```text
TC        : Set a → Set a
returnTC  : A → TC A
bindTC    : TC A → (A → TC B) → TC B
quoteTC   : A → TC Term
unquoteTC : Term → TC A
checkType : Term → Type → TC Term
```

`P01-TC-ROUNDTRIP` 实际核验 `quoteTC` 后接 `unquoteTC` 的结果类型是 `TC A`。`returnTC` 的确可以构造 `TC A → TC (TC A)`，但这只是把一个已有 checker computation 放入 monad；它不是 typed proof 的 quotation，也不提供 `TC A → A`。

`P02-BAD-RUN-TC` 尝试把 `TC A` 直接当 `A`，Agda 以 `[UnequalTerms] R.TC A !=< A` 拒绝。这个错误是本轮最直接的 host/object 层级围栏。

Cubical v0.9 的真实 `Cubical.Reflection.StrictEquiv` 在 `P03` 中由同一 Agda 2.8.0 内核完整重检通过。它调用 `quoteTC`、`checkType`、`unify` 来构造一个等价证明的宏结果。它是一个真实消费者，却始终留在 `R.TC`；没有把宏执行升级成 Cubical 理论对自身 kernel 的证明。

完整 Cubical v0.9 tree 的确定性 inventory 为：

| token | files | occurrences |
|---|---:|---:|
| `quoteTC` | 3 | 12 |
| `checkType` | 6 | 8 |
| `inferType` | 7 | 9 |
| `unquoteDecl` | 33 | 50 |
| `unquoteTC` | 0 | 0 |
| `--guarded`（tick modality） | 0 | 0 |
| `@tick/@lock` | 0 | 0 |
| `--guardedness`（constructor corecursion） | 21 | 21 |

因此标准 Cubical v0.9 库大量使用 host reflection，却没有在同一库中连接 ticked later，也没有 `unquoteTC` 型自解释消费者。`--guardedness` 是 constructor-based corecursion，与 `--guarded` 的 tick modality 不是同一机制。

### 2.2 MetaRocq quotation：真正的 `cojoin`，typed quotation 未闭合

MetaRocq 的 `□T := Ast.term` 是语法 quotation，`Raw.quote_term` 实现 `cojoin : □T → □□T`；项目明确把预期结构与 Löb theorem 相连。它不是 Agda `TC` 的 monadic return。与此同时，携带 typing derivation 的 `□T := {t : Ast.term & Σ ;;; [] |- t : T}` 在固定 9.1 源码中仍标为 in progress。

这说明“有 raw self-quotation”与“有 typed provability modality”必须分开。当前没有一条合法桥把 MetaRocq 的 raw code、Agda `TC` 和 guarded `▷` 合并成同一个 HoTT `Box`。

### 2.3 GCTT/CCTT later：Löb induction 是时间规则

GCTT v2 把 `▷A` 定义为只在之后可用的数据，并给出 guarded fixed point：

```text
fix : (▷ A → A) → A
```

论文把由“later P 推出 P”再得到 P 的证明方式明确称为 Löb induction。这里的 Löb 不是语法 quotation 的 provability Löb；它是按计算步骤解释的 guarded recursion 原理。

GCTT 同时明确：`x : ▷A` 的内容不能在 now 访问，只能在一个本身也位于 later 的构造中通过 delayed substitution 使用；一般 `prev` eliminator 在该版本中不存在，带 clock quantification 的受控消去留给后续工作。

CCTT v3 把这件事推进得更精确。其 forcing-tick 章节直接指出：unrestricted elimination of `▷` is unsound，因为任何带 `▷κ A → A` 的类型都能由 fixed point 得到 inhabitant。安全的 `force` 具有全称时钟范围：

```text
force : (∀ κ → ▷κ (A κ)) → ∀ κ → A κ
```

它不是：

```text
forceNowκ : ▷κ A → A
```

这正是用户所关心的时序前提。`∀κ`、tick、fresh-clock condition 和 forcing substitution 不是装饰；它们是防止“未来值现在可用”的支付装置。

## 3. 固定时钟强制展开候选

本轮将 GCTT/CCTT 已声明的风险写成最小原生 target：

```agda
collapse : (G.▹ ⊥ → ⊥) → ⊥
collapse forceNow = G.fix forceNow
```

其过程为：

```text
原任务：递归调用必须延迟一个 tick，保证生产性
  ↓
理论操作：允许 guarded fix : (▷A → A) → A
  ↓
被攻击的抽象：删掉“只能在之后使用”，加入固定时钟 forceNow : ▷A → A
  ↓
对角/反馈：把 forceNow 本身交给 guarded fix
  ↓
A = ⊥ 时得到 collapse
```

`P06-GUARDED-FORCE-COLLAPSE` 在固定 Agda 2.8.0 `LaterPrims` 源码上 exit 0；其结论只相对于该源码显式列出的 `Tick/dfix/pfix` postulates 和额外输入 `forceNow`。它是 `NATIVE_CHECKED_CONDITIONAL_EXPLORATION`，不进入 claim matrix。

`P07-BAD-FIXED-FORCE` 则尝试直接擦掉 tick binder：

```agda
forceNow delayed = delayed
```

Agda 以 `[UnequalTerms] G.Tick → A !=< A` 拒绝。`P05` 的正控制说明，延迟值在 tick binder 内可以正常使用。于是冲突不是 later/fix 自身产生的；它精确依赖被类型系统拒绝的 same-stage force。

这是本项目目前最清楚的“时序擦除悖论形状”：理论若为了经济性把下一时刻的可用性折叠到现在，原本保证生产性的 fixed-point 机制立即变成 bottom 的入口。但固定 HoTT-adjacent 理论恰好知道并阻止了这一步。因此当前判词是：

```text
GUARDED_FORCE_ERASURE_CONDITIONAL_COLLAPSE_WITH_DEFENSE
```

而不是：

```text
HOTT_BUG_FOUND
```

## 4. Clock quantification 不能被一个固定 clock 冒充

`P08-CLOCK-QUANTIFIED-SHAPE` 用纯 safe Agda 固定 CCTT `force` 的量词形状：只有完整的 `(κ : Cl) → Later κ (A κ)` 才能交给 global force。若调用者另给跨 clock reindexing，固定-clock value 可以被扩展成全称族；该额外数据被显式列出。

`P09-BAD-LOCAL-FROM-GLOBAL` 试图把一个 `Later κ (A κ)` 复制为所有 `κ'` 的值，Agda 以 `[UnequalTerms] κ != κ'` 拒绝。它机械排除了“既然 CCTT 有 force，所以某个固定延迟值现在可取”的错误读法。

forcing-ticks tree 的完整 lexical inventory 只有 9 个 `force*` matching lines、分布于 2 个文件：

- `Clocked/Primitives.agda`：global `force` 的签名、定义和两条 law；
- `Clocked/Lift.agda`：唯一消费者显式构造 `λ κ → λ α → ...` 的全时钟族后再调用 `force`。

没有固定-clock `▷κ A → A` 消费者。inventory receipt：`FORCE-CONSUMER-INVENTORY.json`，deterministic SHA-256 `f8d7ad671b037211a593c28eaa85f7d2e15c9754c3cb303fa5249d83b57b8365`。

## 5. 工具链边界

标准 pinned Agda 2.8.0 可以重检同 commit 的 `LaterPrims`，也能核验本轮 tick/force probes。forcing-ticks `Clocked.Primitives.agda` 则来自需要另一条 Agda `forcing-ticks` branch 的实验实现。`P10` 在标准 binary 上产生：

- `@ftick` unknown-attribute warning；
- `[InvalidTypeSort]`；
- exit 42。

该结果被分类为 `EXPECTED_TOOLCHAIN_VERSION_MISMATCH`，不是数学反例，也不说明 CCTT 源码错误。当前机器没有 GHC/cabal/stack/nix，因而本轮没有编译对应 Agda branch，更不能声称已经原生运行完整 CCTT。

## 6. H1–H6 结果

| source | role | H1 | H2 | H3 | H4 | H5 | H6 |
|---|---|---|---|---|---|---|---|
| Agda TC 2.8.0 | host | PASS | PASS | PASS | FAIL | PASS | FAIL |
| Cubical reflection v0.9 | host | PASS | PASS | PASS | FAIL | PASS | FAIL |
| Agda LaterPrims | temporal | PASS | PASS | PARTIAL | FAIL | PASS | FAIL |
| GCTT v2 | temporal | PASS | PASS | PASS | FAIL | PASS | FAIL |
| CCTT + forcing ticks | temporal | PASS | PASS | PASS | PARTIAL | PASS | FAIL |
| MetaRocq quotation 9.1 | syntax | PASS | PASS | PASS | FAIL | PASS | FAIL |

H4 在各系统中失败/部分的原因不同：host TC 没有 object runner；raw quotation 没有 typed reflection；single-clock later 没有 now eliminator；CCTT 只有 all-clock controlled force。H5 全部 PASS，意味着被理论节省或转移的责任仍能被定位。H6 全部 FAIL：没有真实 fixed consumer 擦除这些责任并继续承诺原任务。

## 7. 与核心认知的关系

这个构造直接触及 `KC-000011`–`KC-000013`、`KC-000023`–`KC-000029`：

- “时序”不再只是描述词，而成为 `@tick` context ordering 和 `∀κ` 量词；
- ASK 的问题是：调用者是否真的拥有 tick、全时钟族或 reindexing；
- 理论经济收益是 guarded fix 允许一般而生产性的递归；
- “否定时序”的具体操作是把 `▷κ A` 当作当前 `A`；
- 自馈结构是 `fix` 把这种 force 再喂回自身；
- 冲突的最小终点是 `fix forceNow : ⊥`。

这条线属于时间中的**可用时序**，不是芝诺所攻击的时空/运动连续性。它不能替代 L3 的运动结构线，但它第一次把 HoTT-adjacent 理论对“之后”的原生处理与自指/Löb 线连接到同一个机器构造。

## 8. 与已有 GuardErasure 结果的关系

`MP-GUARD-ERASURE-001` 已在自建阶段流模型中刻画“保更新律地擦除阶段 iff 存在 fixed point”。本轮没有重命名该已知机制为新发现，而是把它特化到三份真实接口：

1. GCTT 的 `▷` 与 Löb induction；
2. CCTT 的 forcing tick / all-clock `force`；
3. Agda 2.8.0 的实际 tick typing restriction。

新增证据不是更强的全称定理，而是“哪个实际规则承担 guard、错误 bridge 的精确类型、当前 kernel 如何拒绝、真实 force 为什么不等价于错误 bridge”。原创性仍应判 `KNOWN_GUARDED_RECURSION_CORE_WITH_NEW_PROJECT_CORRESPONDENCE`。

## 9. 当前效果判断

机器统观在这个切片上达到了预期中的三项效果：

1. 从真实理论规则反向生成候选，而非等待用户提供故事；
2. 让候选、最强反解释和 payment device 在同一证据链中运行；
3. 在找到 conditional collapse 后继续寻找 natural consumer，而不是立即宣布 HoTT BUG。

它尚未达到最终目标，因为 H6 仍为空，完整 forcing-ticks implementation 未在当前工具链运行，现实应用任务也未出现。当前结果是一个具体、可命名、可继续攻击的 HoTT 时间/自指候选位置，而不是最终悖论交付。

## 10. 下一最小可验动作

下一候选应为 `TICK-IRRELEVANCE-OPERATIONAL-GAP-001`。CCTT 同一来源指出：

- fixed points 只在 forcing tick `◇` 上计算展开；
- tick identity 对 normalization 至关重要；
- extensional theory 又用 `tirr` 给任意 ticks 建 Path；
- `force-delay` 因而给 forcing result 与普通 tick application 一条 Path。

下一步要固定同一个 term 在 `◇` 与普通 tick 下的**归约/当前可用性观察**，再检查 tick-irrelevance Path 是否被真实 consumer 用作操作可替换性。若观察量只能存在于外部元层，判 representation boundary；若固定实现/应用把 Path 提升成当前可执行同一，才进入 `NATURAL_USAGE_MISMATCH` 候选。

同时保留一个工程重开条件：若取得 exact forcing-ticks Agda binary 或可构建 Haskell toolchain，就重放 `Clocked.Primitives` 与真实 `force/tirr/pfix` 计算规则；在此之前保持 `SOURCE_INSPECTED_NOT_NATIVE_REPLAYED`。

## 11. 证据边界

- 本报告没有新增 `HoTT/CLAIM_EVIDENCE_MATRIX.md` 行。
- `P06` 依赖 `LaterPrims` 明示 postulates；它不是 safe、无公设 HoTT theorem。
- `P08/P09` 只核全称时钟类型形状，不冒充 CCTT implementation。
- H6 是六个固定来源的直接审查，不是全学术界或所有应用的 nonexistence theorem。
- forcing-ticks toolchain mismatch 是环境/版本事实，不是数学失败。
- 当前全部资产位于独立 worktree，未 commit、merge、tag 或 push。

