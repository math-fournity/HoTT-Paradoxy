# GZ-005：R4 cctt 的受限证明输入域资格化

> **身份：** `ROUTE_UNIT_RECORD / GODEL-ZFC-CONVERGENCE-SOP / G1-R4`。
>
> **状态：** `LOCAL_CLOSED_WITH_SCOPE / GZ-006_SUCCESSOR_REQUIRED`。
>
> **运行收据：** [20261005-CCTT-R4-INPUT-DOMAIN-002](../HoTT/verification/runs/20261005-CCTT-R4-INPUT-DOMAIN-002/RUN.json)。

## 1. Parent gap

cooltt 与 cubicaltt 都因当前 target toolchain不可重放而只给 source-level R4 evidence。cctt 是一个不同的 Haskell cartesian cubical implementation，当前 host 实际具有 GHC 与 Stack，因而可以检验其真实 checker behavior。

但 cctt 的 tutorial 直接声明两个可能破坏“checker接受 = closed proof”的默认推论：

```text
Holes are checkable only. Holes are convertible to any value.
Any top-level definition can be recursive.
There's no termination checking.
```

因此本单位的对象不是“cctt 是否能检查文件”这个弱问题，而是：能否定义一个透明的、受限的 `ClosedProofAccept` 输入域，使 cctt checker 的成功对 R4 有有限价值。

## 2. 冻结 target 与自身构造

| 字段 | 值 |
|---|---|
| implementation | `AndrasKovacs/cctt@3695c69efbd5e4cbb4b92a8980f5cdae9874072a` |
| toolchain | `stack` / GHC；source `stack.yaml` 固定 `lts-21.25` 与两个 exact Git extra-deps |
| object features | `Presyntax.Tm` 的 `Nat`、`Path`、`Coe/HCom/Com`、`Glue`、`Hole`；tutorial的 inductive Nat/HIT/Glue/path examples |
| candidate formal completion | `ClosedProofAccept_cctt(source)`：source 通过本项目受限 profile，cctt进程完成、输出无上游 `ERROR` diagnostic 且含 `checked N definitions` marker；profile 拒绝 holes、`undefined`、imports与 top-level recursion cycle。它是项目受限输入合同，不是 cctt 的一般 proof relation。 |

### 正向样例预期

冻结一个小 cctt corpus，至少让同一文件含：Nat/zero/suc/case、一个 Path/refl 或 transport、一个 Glue/coe/hcom 片段。它应在 profile 通过后，以无 `ERROR` diagnostic 和 checked marker 的方式通过 checker。

### 负向控制预期

1. `?` hole：无论 checker exit 是否为零，profile 必须拒绝；
2. top-level self recursion：无论 checker exit 是否为零，profile 必须拒绝；
3. 类型错误：checker diagnostics 本身必须拒绝；process exit 单独不构成 oracle；
4. profile 不能只关键词匹配注释；它至少应去除注释／字符串后识别可执行 token。

### Falsifier

- exact source 或 Stack build 无法获得；
- 不能在 cctt source 中定位 Nat/Path/Glue/hole/recursion 的实际语义；
- 正向 corpus 不通过 checker；
- error corpus 被 checker接受且 profile也无法区分；
- 任何结论把受限 source profile升级为 cctt 全部程序、完整 HoTT 或 object-level provability。

## 3. 已知 source anchors（build 前）

- `README.md`：NbE、conversion、quotation与 closed/open cubical evaluation；
- `src/Presyntax.hs`：`Hole`、`Nat`、`Path`、`Coe/HCom/Com`、`GlueTy/GlueTm/Unglue`；
- `src/Conversion.hs`：`VHole` 与任意值 convertible；
- `tutorial.cctt`：holes可检查、任意 top-level recursion、无 termination checking、Nat、Path、Glue、HIT examples；
- `stack.yaml` / `package.yaml`：Haskell build source。

这些是 source-level facts，尚不等于实际 checker run。

## 4. 实际 build 与 controls

冻结 source 的 tracked tree 有 185 个文件。`stack --system-ghc build` 在 GHC 9.4.8、Stack
3.11.1 上 exit 0；run receipt 同时固定 `stack.yaml`、`package.yaml`、`stack.yaml.lock`、
GHC、Stack 和生成 checker 的 SHA-256。它允许 hpack 生成 `cctt.cabal`，但拒绝任意其它
upstream worktree delta。

| 输入 | project profile | cctt 诊断性验收 | process exit | 观察范围 |
|---|---|---|---:|---|
| `Positive.cctt` | 接受；10 个 acyclic top-level definitions | 无 `ERROR`，有 `checked 11 definitions` | 0 | 同一输入含 Nat、Path、Glue、`coe`、`hcom`。这说明这些 forms 进入 parser/elaborator；不说明 `hcom` 已被归约。 |
| `Hole.cctt` | 拒绝：`HOLE_TOKEN` | 无 `ERROR`，有 `HOLE` 诊断和 checked marker | 0 | diagnostic acceptance 不能单独充当 closed proof certificate。 |
| `Recursive.cctt` | 拒绝：`TOP_LEVEL_RECURSION_CYCLE:loop` | 无 `ERROR`，有 checked marker | 0 | 默认 checker 接纳此 self recursion；受限接口必须把它排除。 |
| `Recursive.cctt nf loop` | 不适用 | 两秒内结束，报告 `<<loop>>` | 1 | 仅是这条 command 的有限观察，不证明任何全称不可终止性。 |
| `TypeError.cctt` | 接受（profile 不是 typechecker） | 有 `ERROR`，无 checked marker | **0** | 关键反控制：当前 CLI 对类型错误仍 exit 0；shell status 不可当作 acceptance oracle。 |

`Positive.cctt` 的注释故意带有 `?`、`undefined`、`import`、`loop`。profile 去除注释后仍接受它，排除了简单关键词搜索将注释误报为输入缺陷的假阳性。

## 5. 局部判词

```text
CCTT_R4_RESTRICTED_CHECKER_INPUT_DOMAIN_QUALIFIED_WITH_SCOPE
CCTT_CLI_EXIT_CODE_IS_NOT_AN_ACCEPTANCE_ORACLE
CCTT_DEFAULT_HOLE_AND_RECURSION_ADMISSION_IS_NOT_A_CLOSED_PROOF_RELATION
CCTT_OBJECT_LEVEL_PROOF_CODE_REPRESENTABILITY_DIAGONALIZATION_UNPAID
```

GZ-005 支付的是一个受限 R4 **输入／checker contract**，并未支付 `H-PROOF-CODE`、
`H-SUBSTITUTION`、`H-ARITH-INTERP`、`H-REPRESENTABILITY`、`H-FIXPOINT` 或
`H-INDEPENDENCE`。项目 profile 不是数学共同体、HoTT 社区或 bare ZFC 的实际
acceptance interface；本单位也没有产生 HoTT 不完备性或 bare-ZFC 理论精度结论。

## 6. Required successor

`GZ-006 / R4-CCTT-PROOF-CODE-EFFECTIVITY-001` 必须改变判别面：固定同一 cctt
source，逐项审计它是否拥有或能保真导出 finite derivation/proof-code domain、total finite
proof checker/enumerator、syntax coding/decoding、substitution/quotation discipline，以及足以支持
diagonalization 的 arithmetic interpretation。

它必须先写自己的候选 relation 与反控制，再审读 parser/elaboration/core source。若 source 只有
executable elaboration、没有这样的 derivation relation，只能形成
`CCTT_PROOF_CODE_GAP_WITH_SCOPE`，随后切换到另一个 exact calculus 或既有 proof-code route；不得用
GZ-005 的 restricted profile 填补缺失的 proof relation。

## 7. Reopen conditions

重开条件是：冻结 commit/build input/CLI diagnostics 改变；profile 漏掉可执行 hole、import 或 recursion route；或 GZ-006 找到 cctt 自己已有更强、可编码的 closed derivation contract。
