# GZ-006：R4 cctt 的 proof-code 与有效性资格化

> **身份：** `ROUTE_UNIT_RECORD / GODEL-ZFC-CONVERGENCE-SOP / G1-R4`。
>
> **状态：** `LOCAL_CLOSED_WITH_SCOPE / GZ-007_SUCCESSOR_REQUIRED`。
>
> **冻结 target：** `AndrasKovacs/cctt@3695c69efbd5e4cbb4b92a8980f5cdae9874072a`。

## 1. Parent gap

GZ-005 已经建立 cctt 的受限 checker-input contract，但没有建立哥德尔式
`Proof_T(p,q)`。本单位考察的是更强的问题：在这个 exact cubical calculus 的
source 中，是否已经存在一条可审计的路径，把有限 code 连接到一个 derivation／proof
certificate、可验证 judgement、substitution/quotation 和算术化所需的接口。

这一区分是必要的。一个 Haskell elaborator 可以接收一份 source file，仍然不等于存在：

```text
Code × Judgment → Bool
```

形式的、总的、对象层 proof checker；更不等于该 relation 在同一 calculus 中可表示，能
支持 Gödel fixed point。

## 2. 先于本次 source 审读的构造与反控制

本单位采用如下 payment matrix：

| 义务 | 最低所需实物 | 不能拿来替代它的东西 |
|---|---|---|
| `PC-1 SyntaxCode` | 有限 syntax/code domain 与 encoder/decoder 或明确外部编码 | 单有 `Show`、source text 或 parser 名称 |
| `PC-2 Derivation` | judgement-labelled derivation/certificate data | 已 elaborated term 或 runtime value |
| `PC-3 Checker` | 对有限 certificate/code 的明确 checker/enumerator | 只打印 diagnostics 的 CLI |
| `PC-4 Effectivity` | totality/termination argument，或至少冻结的适用界 | 一次快速运行、性能或 timeout |
| `PC-5 SubQuote` | 同一 code relation 上的 substitution/quotation contract | NbE 的 meta-level `quote` 函数 |
| `PC-6 Arithmetic` | 在 target calculus 中解释自然数编码与所需递归函数 | 语言含 `Nat` construct |
| `PC-7 FixedPoint` | 对上述 relation 的 diagonal/fixed-point theorem | 自递归 top-level definition |

反控制是：即使 cctt 有 raw syntax、parser、`check`、`infer`、NbE、quotation 和 Nat，也不能在
没有 PC-1--PC-7 明确 payment 时，把它称为 R3 的 HoTT object-level instantiation。

**过程自审：** 这张 matrix 在查 source 前已于本轮公开工作说明中形成，但没有在执行 source
search 前先写入 repo。这是 `PERSISTENCE_ORDER_DEVIATION`：思想顺序满足“先构造、后审读”，
持久记录顺序晚于 source command。它不把事后文档伪装成事前盲测；本 unit 以此记录修复，并要求
后续 GZ-007 在任何新外部 source search 前先落盘自己的 matrix。

## 3. 冻结分母与直接 source evidence

分母是上游 Git remote `https://github.com/AndrasKovacs/cctt.git` 的冻结 commit 全部 20 个
`src/**/*.hs` 文件，以及 root `README.md`、`rules.txt`、`tutorial.cctt` 和 package metadata。
对全部 source 执行了关于 `Deriv`、`Proof`、`Judg`、`proofCode`、`checkDeriv`、
`verifyProof`、encoding/decoding 的符号搜索，并逐项回读负责 core syntax、elaboration、state、
errors、parser、quotation 与 rules 的文件。

| Matrix 行 | 当前 source 中的事实 | 对 GZ-006 的结论 |
|---|---|---|
| `PC-1 SyntaxCode` | `Presyntax.hs` 与 `CoreTypes.hs` 有 concrete/pre-core term data；但 search 未发现 `Tm`/judgement 的 encode/decode 或 serialization contract。`Data.Flat` 在 source 中只直接用于 `Lvl`。 | raw syntax source 存在；可重用的 proof-code contract 未找到。 |
| `PC-2 Derivation` | 全 20 个 Haskell source 文件中未找到 `data Deriv`、`data Proof`、`data Judg` 或同类 derivation certificate；`Elaboration.check` 的签名是 `P.Tm -> GTy -> IO Tm`，`infer` 返回 `IO Infer`。 | checker produces elaborated terms or diagnostics, not explicit proof objects. |
| `PC-3 Checker` | `check`/`infer`、`elabTop` 与 `elaborate` 是 Haskell IO pipeline；GZ-005 实测 type error 会打印 `ERROR` 但 process exit 仍为 0。 | 有 executable elaboration，不是一个由 exit status 给出的 Bool proof checker，也没有 source-paid certificate verifier。 |
| `PC-4 Effectivity` | tutorial 与 talk material 明说没有 termination checking；`Core.hs` TODO 仍写“have native fixpoints + case trees, drop top-level recursion”。 | 不可由 source/一次运行把整个 acceptance path 支付为 total finite checker。此处没有断言 Haskell program 必然在所有输入上不终止。 |
| `PC-5 SubQuote` | README 和 `Quotation.hs` 确实有 NbE quotation、interval substitution 与 closures；README 同时说明 CTT evaluation 需要作用于 values 的 interval substitution。 | 这是 meta-implementation 的 substitution/quotation resource；没有把它与 finite proof codes 的 relation 连接。 |
| `PC-6 Arithmetic` | `Nat` 与 case/elaboration forms 存在，GZ-005 positive corpus 已运行。 | `Nat` feature 不等价于 numeral coding、representability 或 arithmetic interpretation。 |
| `PC-7 FixedPoint` | source denominator 内未找到 diagonal/fixed-point / Gödel construction。top-level recursion 是 implementation feature，不能替换 syntax quotation + substitution + proof predicate 的对角化。 | 未支付。 |

两个额外边界尤其重要：

1. `CoreTypes.hs` 的 `Tm` 带有 `DefInfo`、`TyConInfo`、constructor tables 和 `IORef` 等运行时关联；
   它不能仅凭“有一个 Haskell `data Tm`”被当成已经给出独立的、封闭的自然数编码域。
2. `rules.txt` 的确写了形如 `Γ ⊢ t : A` 的规则，但文件首行就是 “THIS IS ALSO PRETTY OLD NOW”，
   并列出与 implementation harmonize 的 TODO。它是历史规则草稿，既不与当前 source 同步冻结，也不提供
   derivation codes/checker/totality证明。

## 4. 可重放检查与反控制

- 用 GZ-005 固定 binary 运行 `Positive.cctt elab`，实际得到 elaborated terms（Nat、Path、Glue、
  `coe`、`hcom`），没有输出 derivation certificate；
- `CoreTypes.hs` 给出 internally elaborated `Tm`、runtime `Val`、closures 和 `Recurse`，而不是
  `Derivation` data；
- `Elaboration.hs` 的 `check` 成功返回 `Tm`，错误通过 `err` 的 IO control flow 报告；
- `rules.txt` 作为不同任务控制：它说明作者有 judgemental notation，但它的 old/TODO 标记和缺少 code
  relation 排除了“规则文本 = 当前 executable proof predicate”的偷换；
- Foundation Lean GZ-002 是正对照：该 source 明确导出 `Provable`、`codeOfREPred`、substitution、
  quotation 和 first incompleteness theorem。cctt target 缺失的是该种 payment，并非本项目把标准设到无法满足。

## 5. 局部判词

```text
CCTT_RAW_SYNTAX_AND_EXECUTABLE_ELABORATION_PRESENT_WITH_SCOPE
CCTT_FINITE_DERIVATION_PROOF_CODE_CONTRACT_NOT_SOURCE_PAID_WITH_SCOPE
CCTT_EFFECTIVITY_REPRESENTABILITY_AND_FIXED_POINT_UNPAID_WITH_SCOPE
NOT_A_NEGATIVE_RESULT_ABOUT_ALL_CUBICAL_TYPE_THEORIES
NOT_A_GÖDEL_THEOREM_ABOUT_CCTT
```

这关闭的是 **这个 source version 作为 G0→R4 object-level proof-code bridge 的 target**。它不说明
cctt 的数学理论错误，也不说明不存在另一种针对同一 calculus 的外部 formalization；更不说明 HoTT 或
bare ZFC 的理论精度问题已经得到正面或负面的结论。

## 6. Required successor

`GZ-007 / R4-EXACT-CUBICAL-DERIVATION-SOURCE-TRIAGE-001`：切换到不同的 source denominator，优先寻找
版本固定的 cubical/HoTT formalization，其中有 explicit raw syntax、derivation relation、effective
checker/enumerator，并至少覆盖 Nat 与 Path/identity；univalence/HIT 必须另列。它需要先冻结候选池和
排除理由，再逐个资格化，不能再次以 cctt 的 CLI 或 project profile 充当 evidence。

若所有声明候选都在各自固定分母中缺 proof-code bridge，才可以在 R4 这一分母上形成有界负结论；在此之前，
G1-R4 保持 active。

## 7. Reopen conditions

若发现该 commit 的未读 source、作者维护的 derivation formalization、可验证 serialization/checker 或
同 source 的 exact metatheory，其内容满足 PC-1--PC-7 中的一项，则重开 GZ-006。任何这种材料仍须先判定
它是同一 calculus、可翻译 fragment，还是只共享“cubical”标签。
