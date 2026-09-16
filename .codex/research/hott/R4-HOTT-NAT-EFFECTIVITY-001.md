# R4-HOTT-NAT-EFFECTIVITY-001：选择具 Nat/Path 的可执行 cubical calculus 与闭合证明输入规范

状态：`ACTIVE / TASKSPEC_FROZEN / IMPLEMENTATION_NOT_STARTED`  
父任务：`A-R3-R4-GODEL-RETURN-001`  
前置：R3 C-244–C-249 已机器重放；R3→R4 十二义务矩阵完成，`H-NAT`/`H-ID/PATH`/`H-UNIVALENCE/HIT` 在当前 groupoid-syntax target 中 `ABSENT_BY_DEFINITION`。

## 1. 目标

选择一个 community cubical/HoTT implementation 作为第二个 exact target，使同一个具名 calculus 至少同时具备：

- 可枚举 raw source syntax；
- Nat 或用户定义 inductive Nat；
- Path/identity、universe 与 cubical composition/transport；
- 实际 conversion/type checker；
- 一个把 holes、`undefined`、未解 metavariables 和无终止性证明的递归明确列为证明关系域外构造的闭合证明输入规范。

本任务只推进 `H-NAT`、`H-ID/PATH`、`H-CONVERSION` 与 `H-EFFECTIVITY`。它不假装已经得到 proof-code representability、fixed point 或 HoTT independent sentence。

## 2. 候选来源与冻结 commits（2026-09-15 资格化入口）

| implementation | exact commit | 已直接看到的结构 | 首要风险 |
|---|---|---|---|
| `cubicaltt` | `mortberg/cubicaltt@9baa6f2491cc61dbd4fd81d58323c04100381451` | Path、composition/transport、Glue/univalence、identity types、Nat examples、circle/integer HIT、Haskell type checker | surface keyword 含 `undefined`；旧 Haskell toolchain；需确定递归/未完成项退出语义 |
| `redtt` | `RedPRL/redtt@ae76658873a647eb43d8cf84365a9d68e9a3273c` | extension/path types、univalent universes、user HIT、two-level pretype/kan split、OCaml checker | README 明说 exact equality尚未加入；2022 旧依赖；需核 Nat 与当前 build |
| `cooltt` | `RedPRL/cooltt@b39bf29900451cb43ae6fbd9af5aa33d59e18935` | raw `SyntaxData` 中 Nat/NatElim、Circle、Universe；独立 `Conversion.ml`；NbE/elaboration | holes/metavariables与 proof refinement 的完成判据须核；OCaml 5.0 + pinned deps |
| `cctt` | `AndrasKovacs/cctt@3695c69efbd5e4cbb4b92a8980f5cdae9874072a` | raw `Presyntax.Tm`、Path/Glue、ordinary inductive Nat、HIT、NbE/conversion；2026-09-11 当前实现 | 教程明确 holes checkable且与任意值 convertible，并允许任意 top-level recursion；默认输入域不能作为证明证书 |

四个 repo 都有明确 MIT/Apache-2.0 许可证。它们当前只在外置文献缓存中按 exact commit checkout；进入 main 的 source manifest、build receipt 和测试必须另行生成。

## 3. 资格化 Gates

每个候选逐项输出：

1. `Q-SOURCE`：repo URL、commit、commit date、license、tracked tree hash；
2. `Q-BUILD`：固定工具链/容器下 build 与 smoke tests；
3. `Q-RAW-SYNTAX`：term/type/context/rule AST 的 source anchors；
4. `Q-NAT`：Nat formation/introduction/elimination/computation；
5. `Q-PATH`：Path/identity、composition/transport、universe/univalence/HIT 的确切层级；
6. `Q-CONVERSION`：checker入口、termination依据与错误结果；
7. `Q-INCOMPLETE-INPUT`：hole/undefined/unsolved metavariable 必须被判为证明关系域外，不能形成完成证明项；
8. `Q-RECURSION`：一般递归、recursive top definition、guarded/corecursive forms 的许可和终止检查；
9. `Q-DETERMINISM`：同一正向／反向样例集的重放结果和输出 hash；
10. `Q-CORRESPONDENCE`：implementation AST/acceptance 与声明 calculus rules 的保真边界。

`Q-BUILD` 通过不自动使其它 Gate 通过。

## 4. 闭合证明输入规范 v1

无论选择哪个 implementation，第一版可证明关系必须先定义为：

```text
ClosedProofAccept(source) :=
  source satisfies the frozen syntactic exclusion profile
  ∧ parser/elaborator/type checker exits successfully
  ∧ output contains no unsolved goals/metavariables
  ∧ every imported module satisfies the same profile
```

排除项至少包括：

- hole、`undefined`、admit/postulate/opaque axiom shortcut；
- 未解 metavariable 或仅打印 goal 却 exit 0；
- 没有 termination/guardedness 证明的一般 recursive definition；
- 非冻结 plugin、network import 或运行时加载的额外 rule；
- 将 host Haskell/OCaml function直接记作 object-calculus representable function。

若 implementation 没有内建闭合证明模式，本项目可以实现独立语法资格化器与 import-closure verifier；它只能定义一个受限输入语言，不得声称修复或证明完整上游 calculus sound。

## 5. 正向与反向边界样例集

每个可运行候选至少测试：

- positive Nat：`zero/suc` 与一次 eliminator/case computation；
- positive Path：`refl`、path application 与一项 transport/composition；
- positive cubical：若系统声称，检查 univalence/Glue 或一个 circle constructor；
- 反向 typing 对照：错误 Nat branch、错误 path endpoint；
- 不完备输入边界对照：hole/undefined/unsolved goal；
- 递归边界对照：直接自调用或互递归循环；
- import control：依赖文件含上述排除项时必须整体拒绝。

同一 corpus 运行两次，比较 exit、stdout、stderr 与输入 closure hashes。

## 6. 选择规则

优先选择能以最少新增假设闭合 `Q-SOURCE`–`Q-RECURSION` 的 implementation，而不是构造最多或运行最快者：

1. 若 cooltt 的 primitive Nat/NatElim + Conversion 能在闭合输入规范下把不完备项判为域外，优先作为 proof-checking target；
2. 若 cooltt 工具链不可重建，尝试 cubicaltt 的稳定示例集；
3. cctt 作为 raw syntax/NbE differential target，只有在语法资格化器把 hole 和 unrestricted recursion 列为域外后进入闭合证明关系；
4. redtt 保留为 extension-type/two-level 对照，不因 feature list 自动胜出。

## 7. 完成与后续

本任务在以下条件同时满足时可称 `R4_EXECUTABLE_NAT_PATH_SLICE_COMPLETE_WITH_SCOPE`：

- 至少一个 exact source/toolchain/build 被 main 冻结；
- 闭合输入规范与 import closure 机械执行；
- 三个正向样例与三类反向边界对照给出稳定收据；
- R3→R4 matrix 中 `H-NAT`、`H-ID/PATH`、`H-CONVERSION`、`H-EFFECTIVITY` 按精确 scope更新；
- 保留 `H-PROOF-CODE`、`H-ARITH-INTERP`、`H-REPRESENTABILITY`、`H-FIXPOINT`、`H-INDEPENDENCE` 的开放状态。

下一阶段才是把 accepted derivation 变成自然数 proof code/enumerator，并证明 checker relation 与 implementation acceptance 的对应。本 TaskSpec 不证明 consistency、normalization、完整 R4、HoTT essentiality或现实相对悖论。
