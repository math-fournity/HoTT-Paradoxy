# GZ-003：R4-HOTT-NAT-EFFECTIVITY-001 的 cooltt 资格化

> **身份：** `ROUTE_UNIT_RECORD / GODEL-ZFC-CONVERGENCE-SOP / G1-R4`。
>
> **状态：** `LOCAL_CLOSED_WITH_SCOPE / COOLTT_TOOLCHAIN_GAP / CUBICALTT_SUCCESSOR_REQUIRED`。
>
> **前提：** `GZ-002` 已在版本闭合范围内重放 Foundation 的一阶算术第一不完备性基准；这不使 R3 自动实例化到 HoTT。

## 1. Parent gap

R4 需要回答：G0 中的 code、provability、diagonal 和 independent-sentence结构能否落入一个**同一、精确、可执行的 HoTT/cubical calculus**，而不是只存在于元语言 Coq/Lean/Agda。

现有 `akaposi/cohtt@5babc385` groupoid syntax 已机器重放 `Con/Sub/Ty/Tm` 与 typed substitution，但义务矩阵显示：`H-NAT`、`H-ID/PATH`、`H-UNIVALENCE/HIT` 均为 `ABSENT_BY_DEFINITION`，`H-CONVERSION` 与 `H-EFFECTIVITY` 仍开放。因此它只能做 R4 的语法控制，不能作为 R4 的终点。

## 2. 冻结 target

| 字段 | 值 |
|---|---|
| 候选实现 | `RedPRL/cooltt@b39bf29900451cb43ae6fbd9af5aa33d59e18935` |
| 要资格化的层 | concrete raw syntax、Nat/NatElim、Path/Glue/universe、conversion/NbE、闭合输入的 checker acceptance |
| 本单位仅支付 | `Q-SOURCE`、`Q-RAW-SYNTAX`、`Q-NAT`、`Q-PATH`、`Q-CONVERSION`，若可能再支付有限范围的 `Q-EFFECTIVITY` |
| 不支付 | proof-code enumerator、arithmetic interpretation、representability、fixed point、independent sentence、HoTT essentiality、ZFC acceptance 或 OriginDone bridge |

## 3. 自身构造与可证伪预期（先于 candidate source 审读）

### 候选构造

一个合格 R4 target 应能把下列对象同时放在同一 object calculus 的可检查输入域中：

```text
Nat / zero / suc / Nat elimination
Path or identity / at least one transport or composition form
Universe and a cubical Glue or equivalent feature if advertised
closed term/type checker or conversion entry point
```

本单位将把 `ClosedProofAccept(source)` 收紧为有限 checker-input contract：输入不得含 holes、未解 metavariables、`undefined`、admit/postulate shortcut 或未经 termination/guardedness 限定的一般 recursion。主正向样例应至少包含 Nat eliminator 与 Path/transport；反向样例应尝试错误 Nat branch、错误 Path endpoint、不完备项及直接 recursion。

### Falsifier

以下任一项会拒绝此 exact target 作为 `R4_EXECUTABLE_NAT_PATH_SLICE`：

1. 不能固定 URL、commit、license 与 source tree；
2. source 不同时出现 raw syntax、Nat/NatElim 与 path/cubical constructs；
3. 没有可运行 conversion/checker，或其本身的输入域无法把 holes/recursion 同闭合证明区分；
4. 构建环境缺失且无法获得可复现 target toolchain；
5. 任一主张只能来自 host OCaml function 而不能定位到 object syntax/checker contract。

### 对照与后继

- 若 cooltt source/build 足够，进入其 bounded Nat/Path positive/negative corpus；
- 若 source 有 feature 但 toolchain 不可运行，记录 `COOLTT_TOOLCHAIN_GAP_WITH_SCOPE`，切换 `cubicaltt` 的 Haskell checker target；
- 若 cooltt 的 syntactic admission 允许 holes/recursion 进入同一 accepted domain，转为 `CCTT`/cooltt 的 closed-input exclusion control，不把它称为 proof relation；
- 无论哪一项，都不得重新调用 G0 或把一般 Foundation theorem 当作 HoTT theorem。

## 4. 实际 source qualification

### 4.1 来源、license 与树身份

通过 Git exact fetch 得到：

```text
RedPRL/cooltt@b39bf29900451cb43ae6fbd9af5aa33d59e18935
commit date: 2023-10-21T12:26:16-05:00
license: Apache-2.0
source files outside .git: 162
```

README 将其明确描述为 Cartesian cubical type theory 的 NbE 与 elaboration 实现；`cooltt.opam` 固定
OCaml `>= 5.0`、Dune、`bantorra`、`kado`等依赖，并给出 opam 与 Nix 两条 build route。

### 4.2 已直接支付的静态 gates

| Gate | 直接 source anchor | 结论 |
|---|---|---|
| `Q-RAW-SYNTAX` | `src/frontend/Grammar.mly` 与 `src/core/SyntaxData.ml` | 有 concrete grammar 与 raw term/type data；不是只给论文规则表。 |
| `Q-NAT` | grammar 的 `NAT`、`src/core/Domain.ml` 的 `Nat`/`KNatElim`、`src/core/Refiner.mli` 的 `Nat.formation/literal/suc/elim`、`test/nat.cooltt` | Nat、数值、后继与 eliminator 实际存在，test corpus 含 `#normalize`。 |
| `Q-PATH` | `test/prelude.cooltt` 的 `path`、`test/path-types.cooltt`、grammar 的 cubical term forms | source 含 path/extension/coercion/transport surface，并非只有 host equality。 |
| `Q-CONVERSION` | `src/core/Conversion.ml/.mli` 和 NbE/Semantics modules | 有明确 conversion engine / normalization source。 |
| `Q-INCOMPLETE-INPUT` | grammar 的 `Hole`/`BoundaryHole`、`RefineErrorData.UnsolvedHoles` 和 `HoleNotPermitted` | source 显式区分 hole 与 closed acceptance；仍需真实 checker run 测试其实际入口行为。 |

### 4.3 当前工具链 verdict

本机检测结果：`ocaml=ABSENT`、`dune=ABSENT`、`nix=ABSENT`；`opam` 存在但未初始化，因而没有可用 switch 或 pinned dependency closure。没有调用全局 `opam init`、没有猜测 compiler 版本，也没有把静态 source 读出写成 checker acceptance。

```text
COOLTT_SOURCE_QUALIFIED_FOR_R4_NAT_PATH_CONVERSION_WITH_SCOPE
COOLTT_BUILD_AND_CLOSED_INPUT_ACCEPTANCE_NOT_RUN
COOLTT_TOOLCHAIN_GAP_WITH_SCOPE
```

这不是 cooltt calculus 的失败，也不是 R4 被否定。它只拒绝“本机已重放 cooltt checker”这一主张。

## 5. Required successor

`GZ-004 / R4-CUBICALTT-BUILD-QUALIFICATION-001`：冻结 `mortberg/cubicaltt@9baa6f2491cc61dbd4fd81d58323c04100381451`，先检查 Haskell toolchain、raw syntax、Nat/Path/Glue/univalence/HIT、checker input boundary与可重放 sample corpus。它必须改变 implementation/toolchain/acceptance interface，而不是重复 cooltt 的 OCaml 环境诊断。
