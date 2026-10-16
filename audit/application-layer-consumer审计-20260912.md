# N10 审计：应用层/工具链交付消费者（Agda 编译后端与 Lean 求值）

> 文档身份：`CURRENT AUDIT EVIDENCE / DEFENSE_WORKS (SCOPED)`
> 日期：2026-09-12
> 触发：S051 后的第一工作包 N10——在固定集合与版本内审计真实 HoTT/类型论应用代码或工具链插件，检查是否存在把较弱资格（商、截断、等价存在、表示数据缺失）当作交付/计算承诺的 natural consumer。
> 结论：**在被审计的交付后端上判 `DEFENSE_WORKS`（scoped）——Cubical Agda 内容在 Agda 2.8.0 中没有可交付的执行路径：`--cubical` 模块被全部编译后端拒绝，`--erased-cubical` 只允许与计算无关的擦除使用（计算性 cubical 使用被 erasure checker 拒绝，cubical 库函数被声明为 erased），普通模块甚至不能导入 cubical 库；Lean 4.33.1 侧，尊重关系的商消去可执行，代表元依赖消去被类型检查拒绝，`noncomputable` 消费者被求值器拒绝。本次固定集合内没有找到 E6。**

## 0. 审计集合与限制

| 接口 | 版本/入口 | 本轮可核层级 | 结果 |
|---|---|---|---|
| Agda JS 后端 | Agda 2.8.0-3d04bac（`/Volumes/D/HoTT-toolchain-cache/agda-v2.8.0-macos-arm64/agda`，binary SHA-256 `ac285c19…`）；node v26.7.0 实际执行 | type check → JS 生成 → node 运行 | 非 cubical 基线实际运行成功；所有 cubical/erased-cubical 模块被拒绝编译 |
| Agda GHC/MAlonzo 后端 | 同上；`--compile --ghc-dont-call-ghc`（本机无 `ghc`，只生成 Haskell 源码） | type check → Haskell 源码生成与检查 | `--cubical` 模块被拒绝；`--erased-cubical` 模块接受并生成 Haskell 源码；执行 `NOT_RUN_NO_GHC` |
| Cubical v0.9 库导入面 | tag commit `b150186d2544e7efeddd31e5d14a8b9ecbb100f7`；tree SHA-256 `73ccfbaf960f252800da02dac6a9bbef72d1214e2907940466dc2abef2060a81` | 实际编译/类型检查 | 非 cubical 模块导入 `Cubical.Data.Bool` 被 `InfectiveImport` 拒绝 |
| Lean 4 求值器 | Lean 4.33.1（commit `819816b2e0a3bf405af45ae5c7af2491d8f5bee6`），`lean file.lean` | 实际运行 `#eval` | 商消去正例计算成功；代表元依赖消去被类型检查拒绝；`noncomputable` 被求值器拒绝 |
| Coq/Rocq、其它后端 | 不在本机 PATH | NOT_AVAILABLE | 未审计 |

审计限制：本审计只覆盖上述版本与入口；GHC 交付物只做源码检查，未实际链接执行；不证明任何工具链/任何版本都不可能出现 natural consumer；不新增数学 claim。探针源文件与原始输出全部保存在
`.codex/research/hott/sessions/S-RES-20260912-052-APPLICATION-LAYER-AUDIT/evidence/`。

## 1. Agda 交付后端：cubical 内容没有编译路径

固定探针（全部先通过类型检查，再尝试两条编译后端）：

| 探针 | 内容 | type check | `--js` | `--compile --ghc-dont-call-ghc` |
|---|---|---|---|---|
| `JsBaseline.agda` | 无 cubical 的 Hello-world（IO 实际运行） | 0 | 0（node 实际打印 `BASELINE_OK`） | — |
| `JsUaTransport.agda` | `transport (ua notEquiv) true` 的计算 | 0 | 42 `[CubicalCompilationNotSupported]` | 42 `[CubicalCompilationNotSupported]` |
| `JsHit.agda` | 带路径构造子的 HIT 消去（`sq : a ≡ b`） | 0 | 42 `[CubicalCompilationNotSupported]` | 42 `[CubicalCompilationNotSupported]` |
| `JsQuotient.agda` | 集合商消去（`Bool / true~false`，常量消去子） | 0 | 42 `[CubicalCompilationNotSupported]` | 42 `[CubicalCompilationNotSupported]` |
| `PlainCubicalImport.agda` | 无选项模块导入 `Cubical.Data.Bool` | 42 `[InfectiveImport]`（cubical/erased-cubical、guardedness、two-level 三连） | 42 | — |

关键错误原文：

```text
error: [CubicalCompilationNotSupported]
Compilation of code that uses --cubical is not supported.
```

```text
error: [InfectiveImport]
Importing module Cubical.Data.Bool using the
--cubical/--erased-cubical flag from a module which does not.
```

结论：在这套固定工具链里，“理论接受”与“执行交付”是**两层不同的验收面**。凡是使用 `--cubical` 的模块（无论是否真的触发 cubical 计算），两个编译后端都整体拒绝；cubical 选项是 infective 的，普通模块无法导入 cubical 库来绕开该拒绝。这个拒绝发生在“交付”之前，而不是交付出错误结果，因此对“把较弱资格当交付承诺”的消费者而言是防御，而不是失配。

## 2. 唯一部分交付路径（`--erased-cubical`）及其围栏

`--erased-cubical` 的定位是“只允许与计算无关的擦除使用”。实测三组：

| 探针 | 内容 | type check | `--js` | GHC 源码生成 | 关键证据 |
|---|---|---|---|---|---|
| `ErasedCubicalPositive.agda` | `ua` 只出现在 `@0` 擦除定义中，`main` 打印固定串 | 0 | 42 `[CubicalCompilationNotSupported]`（“uses --erased-cubical”） | 0 | 生成的 Haskell 中不含 `transport`/`ua`（擦除内容被丢弃） |
| `ErasedCubicalNegative.agda` | 同一 `ua` 路径被**计算性**使用（`transport (ua e) true : Bool`） | 42 `[DefinitionIsErased]`（`transport` is declared erased） | — | — | 计算性依赖在检查阶段被拒绝，而不是被擦除或静默交付 |
| `ErasedCubicalLibraryFunction.agda` | 使用 cubical 库函数 `not`（Bool → Bool） | 42 `[DefinitionIsErased]`（`not` is declared erased） | — | — | 库函数也按 erased 处理；只有数据构造子仍可用于计算 |
| `ErasedCubicalImport.agda` | 只用库数据 `Bool` 的构造子，本地定义 `myNot` 并计算 | 0 | 42 | 0 | 生成的 Haskell 忠实编译 `myNot`/`main`（源码级检查） |

这条唯一的部分交付路径因此只能承载**与 cubical 内容计算无关**的代码：能编译的模块要么完全不含 cubical 依赖，要么只把 cubical 内容用于擦除位置；任何“用被擦除的表示数据算出结果”的尝试都在类型/擦除检查阶段被拒绝。

## 3. Lean 4.33.1：商类型的执行与围栏

| 探针 | 内容 | 结果 |
|---|---|---|
| `QuotConsumer.lean` | `rel := True`；`g := Quot.lift (fun _ => true) …`；`#eval g (mk true)`、`#eval g (mk false)` | exit 0；输出 `true`、`true`——商消去可执行且尊重识别（正控） |
| `QuotRespect.lean` | 试图用 `Quot.lift (fun b => b)` 做代表元依赖消去 | exit 1：`rfl` 无法证明 `a = b`——类型层拒绝 |
| `QuotNoncomputable.lean` | `noncomputable def pickBool := Classical.choice ⟨true⟩` + `#eval` | exit 1：`dependsOnNoncomputable`——求值层拒绝 |

与 N2 的 Lean 结果一致：执行层面的资格分离由类型检查与求值器共同执行；没有观察到“接受定义但交付较弱结果”的路径。

## 4. 对 E6 的判定与重开条件

判定：`DEFENSE_WORKS (SCOPED)`。在被审计的集合与版本内，没有找到任何真实、固定版本、可回查的接口或使用链，把“商/截断/等价存在/表示数据缺失”的较弱资格当成执行或交付承诺；相反，工具链在编译、导入、擦除和求值四个层面执行资格分离。该结论与此前 N1（核心库/论文层）、N2（提取接口层）、N5（派生开发自述层）的 bounded 结论方向一致，并首次覆盖**编译后端**这一“真正把理论变成可运行产物”的层面。

重开条件（任一成立即重审）：

1. Agda 后续版本出现支持 cubical 内容的编译后端（或本机 GHC 可用后实测 erased-cubical 交付物）；
2. 出现第三方工具/插件从 cubical 定义生成可执行产物（例如 agda2hs、自定义后端）；
3. Cubical 库把更多定义从 erased 处理改为可计算使用；
4. 发现绕过 erasure checker 的已接受程序（即类型检查通过但执行依赖被擦除的 cubical 内容）。

## 5. 证据清单与哈希

探针源（SHA-256）：

| 文件 | SHA-256 |
|---|---|
| `agda-js/JsBaseline.agda` | `54c31f427cd0323b34e2205dca32a63a27b51d5ab49e4f265af92b8a6db24053` |
| `agda-js/JsUaTransport.agda` | `7f1aca133e53fcf76cf1ea2854949b8b6b787fa0b640e8cb3da5c4a787837f95` |
| `agda-js/JsHit.agda` | `a9efd85fa52630d0dd7d5afa4c5c787e5faf6f7dba671d0a8574d3ededcd14ee` |
| `agda-js/JsQuotient.agda` | `7bdc4465c00585ab3accfb4fdaae7755e27c732973d0e594a7c06b8aae4ac7af` |
| `agda-js/ErasedCubicalPositive.agda` | `537d3072ea72cb6d287000117ad60d5a1945bcebb55fe328767a42cec84bdcb3` |
| `agda-js/ErasedCubicalNegative.agda` | `d8e71f4f26193f023018b6329f365ad3a035eea883c01aee3ee9c4147aa5f438` |
| `agda-js/ErasedCubicalImport.agda` | `3601b84e461ed15e68f9ca5ad507e031c9af9403c04a43af83d664893adf8ee0` |
| `agda-js/ErasedCubicalLibraryFunction.agda` | `e786cf36a378c5a0a6f6baf6684480d9da240c64e9956536f5dd1e864738f4cf` |
| `agda-js/PlainCubicalImport.agda` | `4683961faa057118136e660c7da3542e1ed8279596a03961de67b03f693f7042` |
| `lean/QuotConsumer.lean` | `bac1712a920dc2a38f0d6e6ec6360309309f9ca0e91e7f1847cd848b507b50d7` |
| `lean/QuotRespect.lean` | `19be0b50ef97cab8eed3761f561f458c1ec86de50cc51880ef98bfc9c688130c` |
| `lean/QuotNoncomputable.lean` | `7aee6888ca05406f172bb1d4d2e52d9d50cb96cd22b26416872b9333135c469c` |

关键运行输出（SHA-256）：`baseline.node.stdout.txt` `39d42bc9…`（内容 `BASELINE_OK`）；`JsUaTransport.js2.stdout.txt` = `JsHit.js2.stdout.txt` = `JsQuotient.js2.stdout.txt` `7f0bda1d…`（同一 `CubicalCompilationNotSupported` 文本）；`ErasedCubicalNegative.check2.stdout.txt` `8a9ebe54…`；`ErasedCubicalImport.ghc.stdout.txt` `f039866f…`；`PlainCubicalImport.js2.stdout.txt` `7f07cc38…`；`QuotConsumer.stdout.txt` `21d91041…`（`true\ntrue`）；`QuotRespect.stdout.txt` `64ab7466…`；`QuotNoncomputable.stdout.txt` `da376a55…`。

环境：Agda 2.8.0-3d04bac（binary `ac285c19…`）、Cubical v0.9（`b150186d…` / tree `73ccfbaf…`）、node v26.7.0、Lean 4.33.1（`819816b2…`）、GHC `NOT_AVAILABLE`。

## 6. 过程披露（按责任点记录的探针迭代）

1. `--safe` 与 `COMPILE` pragma 冲突（`[PragmaCompiled]`）→ 交付探针不使用 `--safe`（证明包不受影响）；
2. `--library-file=` 需要指向库列表文件（`AGDA_LIBRARIES`）而不是 `.agda-lib` 本身 → 建立探针自己的 `AGDA_LIBRARIES`；
3. cubical 库的 `--guardedness` 是 infective 选项 → 探针显式启用 `--guardedness`（并保留 `[InfectiveImport]` 探针作为反例）；
4. 标准库 `String` 拼接在探针里需自定义 `_++_` 与 `infixr 5`（cubical Prelude 不导出）；
5. `@0` 属性需要 `--erasure`；cubical 库函数在 erased-cubical 导入下报 `DefinitionIsErased`——这一点由 `ErasedCubicalLibraryFunction.agda` 独立固定为证据，而不是被当作探针错误丢弃。

以上修正只改变探针的选项/命名，不改变被检验命题；所有中间错误与最终错误均保留在 evidence 输出中。

## 7. 结论

`DEFENSE_WORKS (SCOPED)`：固定版本集合内，Cubical Agda 的计算内容在 Agda 2.8.0 中不可交付执行（`--cubical` 全后端拒绝；`--erased-cubical` 只允许擦除使用且库函数同样 erased；普通模块无法导入）；Lean 4.33.1 的商消去在类型与求值两层执行资格分离。E6（natural consumer）在本次审计集合内未发现；当前悖论距离保持第二级 `REPRESENTATION_BOUNDARY`，不升级为 `NATURAL_USAGE_MISMATCH`。
