# GZ-004：R4 cubicaltt checker 资格化

> **身份：** `ROUTE_UNIT_RECORD / GODEL-ZFC-CONVERGENCE-SOP / G1-R4`。
>
> **状态：** `LOCAL_CLOSED_WITH_SCOPE / CUBICALTT_TOOLCHAIN_GAP / CCTT_SUCCESSOR_REQUIRED`。

## 1. Parent gap

cooltt 已确认具 Nat/Path/NbE/conversion 的 source 结构，但当前没有 OCaml/Dune/Nix/opam toolchain。
本单位改用不同的 Haskell implementation，检验它是否能给 R4 一个独立的 executable Nat/Path cubical calculus target。

## 2. 自身构造与反证条件

合格 target 必须同时给 source identity、raw syntax/checker、Nat、Path/cubical transport、univalence/HIT（若声称）、
以及能够判定闭合输入的 checker入口。若 Haskell implementation 只有示例文本或没有编译／运行工具链，不能将 feature list
写成 proof acceptance；若 source 将 `undefined` 等输入纳入可处理语法，仍需实际 exit/diagnostic 决定其是否在 closed proof domain 外。

## 3. 冻结来源与实际审读

```text
mortberg/cubicaltt@9baa6f2491cc61dbd4fd81d58323c04100381451
license: MIT
commit source: exact shallow fetch; clean detached checkout
```

| Gate | 证据 | 范围结论 |
|---|---|---|
| `Q-SOURCE` | `README.md`、`LICENSE`、`cubicaltt.cabal`、`stack.yaml` | 冻结的是一个 experimental Haskell cubical implementation，非纯论文描述。 |
| `Q-RAW-SYNTAX` | `Exp.cf`、`CTT.hs`、`TypeChecker.hs`、`Main.hs` | 有 grammar、checker和 typechecker source。 |
| `Q-NAT` | `examples/nat.ctt`、`CTT.hs`/`Eval.hs` 的 Nat forms | Nat example 与 evaluation source 同时存在。 |
| `Q-PATH` | README 的 Path abstraction/application、composition/transport、`examples/idtypes.ctt` | Path、transport、identity 进入该 implementation 的公开语言层。 |
| `Q-UNIVALENCE/HIT` | README + `examples/univalence.ctt`、`circle.ctt`、`integer.ctt` | source package声明可证明 univalence且有部分 HIT examples；这尚非一项已重放 theorem。 |
| `Q-INCOMPLETE-INPUT` | README reserved words 包含 `undefined`；需 checker run 决定其实际接受／拒绝语义 | 不能仅由保留词把它判为 proof-domain failure。 |

## 4. 工具链资格化

README 指定 Cabal/Make/Stack build；`cubicaltt.cabal` 要求 Haskell packages，`stack.yaml` 固定 `lts-21.12` 与 BNFC。当前本机检测：`ghc=ABSENT`、`cabal=ABSENT`、`stack=ABSENT`。因此未执行 build、Nat 正向样例、Path/transport 正向样例、错误输入、undefined 或 recursion controls。

```text
CUBICALTT_SOURCE_QUALIFIED_FOR_R4_NAT_PATH_CUBICAL_FEATURES_WITH_SCOPE
CUBICALTT_CHECKER_ACCEPTANCE_NOT_RUN
CUBICALTT_HASKELL_TOOLCHAIN_GAP_WITH_SCOPE
```

这条结论不表示 cubicaltt calculus 无法提供 R4 target；它只拒绝“当前 host 已验证它提供这样的 target”。

## 5. Required successor

`GZ-005 / R4-CCTT-INPUT-DOMAIN-001`：冻结 `AndrasKovacs/cctt@3695c69efbd5e4cbb4b92a8980f5cdae9874072a`。重点不再仅列 Nat/Path，而是审查该 implementation 对 holes、未解目标和 unrestricted top-level recursion 的实际输入／完成语义；若同样缺 Haskell toolchain，仍可对其 source-level closed-proof-domain 设计形成不同判别结论，不能重复 cubicaltt 的 feature inventory。
