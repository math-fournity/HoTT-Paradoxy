# ZFC-H0 总证明闭环：F1-D GCTT clocked Delay 翻译卡

> **身份：** `RESEARCH_COGNITION_CLOSURE / M1_H0MAP_TARGET_ANALYSIS / SOURCE_AND_CHECKER_ATTEMPT / NOT_H0MAP`。
>
> **冻结 target：** `hansbugge/cubicaltt` branch `gcubical`，commit
> `c2c5262b6637c09e37d3add55babd3400c839b93`。
>
> **结论状态：** `CLOCKED_DELAY_ENCODING_SOURCE_SUPPORTED / PROTOTYPE_TYPECHECKER_BUILD_DEPENDENCY_GAP_WITH_SCOPE / NATIVE_H0_TO_CLOCKED_TRANSLATION_UNPAID`。

## 1. 在查来源前固定的翻译义务

fixed H0 不是泛称的“一个 infinite object”。它来自 Cubical Agda 2.8.0 + cubical 0.9 的
native `--guardedness` coinductive record：

```text
Delay A
force  : Delay A → A ⊎ Delay A
never  : Delay A
runFor : ℕ → Delay A → Maybe A
```

而 `QuestioningDelay` 的 H0 还依赖 universe、h-level 判定、`EM₁`、suspension、truncation，
并以 `runFor n (question Type judge) ≡ nothing` 给出每个有限 fuel 的实际观察。

在读取 GCTT 资料前，本项目的最小候选不是“两个理论都有 coinduction”，而是下列 card：

| H0 字段 | 必须在 target 中给出的东西 | 反证/失败条件 |
|---|---|---|
| native `Delay A` | 一种 clocked guarded carrier，最终能形成没有显式 clock 参数的 coinductive target | 只能表示带额外 clock 的对象，不能形成 clock-quantified type |
| `force` | `A + Delay A` 的一次观察，且 delayed branch 能回到同一 target | 只给 `▷κ A`，没有 force 或没有 delayed branch 的回收 |
| `never` | guarded fixed point 的无限 silent object | fixed point 不能定义该 object，或只能改写行为 |
| `runFor` | 对每个 natural fuel 的有限观察器及 preserve theorem | 只有 streams/CoNat 的类比而无 finite observation |
| exact H0 closure | universe、h-level、EM1、suspension、truncation 与 `QuestioningDelay` 同一版本的 map | 仅有 Delay 类比或不同 library feature |

这个表的目的不是预设 GCTT 会失败；它使“clocked calculus”必须真正支付 `H0Map` 的哪些字段可审计。

## 2. 一手论文、原型代码与实际构建尝试

### 2.1 学术来源给出的 calculus 边界

[Guarded Cubical Type Theory](https://arxiv.org/abs/1611.09263) 将 cubical type theory 与
guarded recursion 合并，并以 cube category × ω 的 presheaf 语义说明单 clock 的 guarded model。
论文明确将 clock quantification 留给后续工作；因此它不能被直接当作 fixed H0 的无 clock
coinductive record semantics。

[Clocked Cubical Type Theory / Greatest HITs](https://arxiv.org/abs/2102.01969) 才把 multiple clocks、
clock quantification 与 HIT 放进同一方向。这解释了为什么本 card 必须检查 `forall k` 与 `prev`，
而不能只看 `▷`／`next`。

### 2.2 固定 GitHub 原型实际有什么

我将 `gcubical` branch 检出到独立目录并直接审读其 README、grammar、checker 与 examples。
以下是源码事实，不是对 fixed H0 的翻译结论：

| 原型输入 | 直接可读事实 | 对 card 的作用 |
|---|---|---|
| `README.md` | 明示 later modality、`next`、delayed substitutions、`dfix`；README 将其称为 Guarded Cubical Type Theory type checker。 | 支持 guarded fragment 不是只存在于论文文字。 |
| `Exp.cf` | grammar 有 `forall` clocks、clock abstraction/application、`prev`、`next`、`dfix`、`fix`、`|>`。 | 支持 clock quantification 与 `prev` 进入该特定 prototype 的 syntax。 |
| `gctt-examples/streams.ctt` | `data Str = Cons (n : nat) (ns : |> Str)`。 | 单 clock guarded coinductive-style data 的源码实例。 |
| `examples/dataclocks.ctt` | `data gCoNat k` 后定义 `CoNat = forall k, gCoNat $ k`；`comCoNat` 把 clock-quantified guarded data 用 `prev` 和一个 coproduct-like `Plus` 观察成 `Maybe CoNat`。 | 这是 `Delay` 的 `force` 所需 “clocked branch → clock-quantified continuation” 形状的直接源码类比。 |
| `gctt-experiments/gctt.ctt` | 有 `coprod A B`、`dfix/fix`、later code，以及 guarded data。 | 给 generic `A + Delay A` carrier 的可用构件。 |

因此一个 **尚未机器验收的**候选定义可以精确写成：

```text
gDelay A κ = now A | later (▷κ (gDelay A κ))
DelayClocked A = ∀ κ. gDelay A κ
forceClocked : DelayClocked A → A + DelayClocked A
```

其中 `forceClocked` 不能凭空声明。它必须仿照 `comCoNat`，先将 clock-indexed sum
通过 `comPlus` 移到量化外，再在 delayed branch 用 `prev` 返回 `∀κ. gDelay A κ`。这是一条
有代码依据的**翻译路线**，不是已经得到的 `Delay A ≅ DelayClocked A`，更不是 H0Map。

### 2.3 checker 实跑的边界

为避免只读 source 后把 prototype 当作已实际 type-check 的 target，我在另一份同 commit 的新 checkout
运行 `make`。构建在第一个 Haskell 依赖处停止：

```text
Connections.hs:15:1: error:
    Could not find module ‘Test.QuickCheck’
```

本机有 `ghc`，但没有 `cabal` 或已注册的 `QuickCheck` package。没有安装、替换或删去该依赖，
因为那会改变这次对固定原型的运行条件。因而当前没有把任何 `.ctt` example 的成功执行写成证据。

```text
GCTT_PROTOTYPE_BUILD_ATTEMPTED
GCTT_PROTOTYPE_CHECKER_UNAVAILABLE_DUE_TO_MISSING_QUICKCHECK_WITH_SCOPE
```

这是本机的依赖缺口，不是 GCTT 的语义反例，也不是论文或 checker 永远不能运行的结论。

## 3. 对 fixed H0 的逐字段差分裁决

| H0 map 字段 | 当前 source 支持 | 仍缺的支付 |
|---|---|---|
| `Delay` carrier | guarded `data`、later、clock quantification 的源码形状可写；`CoNat` 实例真实存在。 | generic `gDelay A` 和 `DelayClocked A` 的实际 checker acceptance。 |
| `force` | `comCoNat` 给出同形的 clock-quantified force 模式。 | 对 generic sum `A + DelayClocked A` 的具体定义与 typecheck。 |
| `never` | `fix/dfix`、`omega`／guarded recursive streams 存在。 | 对 H0 silent `never` 的 definition 与 force equation。 |
| `runFor` | `nat` 和 guarded observation ingredients 存在。 | exact finite observer、每个 fuel 的 `nothing` preservation theorem。 |
| native→clocked translation | source supports a possible target calculus. | 从 Cubical Agda native `--guardedness` record 到 this calculus 的 translation/adequacy theorem。 |
| H0 universe/HIT closure | target has `U`、cubical primitives、一些 data/HIT examples。 | H0 依赖的 exact `EM₁`、suspension、truncation、h-level library 与 QuestioningDelay 的同一 variant map。 |

故当前不能把 card 写成 `H0MAP_CANDIDATE`。最准确的状态是：

```text
CLOCKED_CUBICAL_DELAY_ENCODING_SOURCE_SUPPORTED
EXACT_NATIVE_H0_TO_CLOCKED_TRANSLATION_UNPAID
EXACT_H0_UNIVERSE_EM1_HIT_CLOSURE_UNPAID
M1_FULL_H0MAP_UNPAID
```

## 4. 下一项最小判别动作与停止条件

下一项不是再找一篇也提到 clocks 的论文。它必须选择下列任一路线，并冻结其版本：

1. **原型运行路线：** 在不替换 target semantics 的条件下提供原型的缺失 build dependency，
   typecheck 一个最小 `ClockedDelay.ctt`，其中有 `gDelay/DelayClocked/forceClocked/never/runFor` 和
   H0 finite trace 的正负控制；
2. **成熟 CCTT 路线：** 找到 exact CCTT implementation 或 mechanization，逐项确认其 grammar、
   clocks、coinductive encoding、HIT/universe library 与 H0 native source 的翻译；
3. **有界拒绝路线：** 若固定 target 的 clock parameter、available library 或 checker semantics 使
   上述 `force/runFor` card 无法成型，记录 `CLOCKED_VARIANT_GAP_WITH_SCOPE`，只关闭该 target。

三者都不能把 source analogue 升格为 H0Map。只有 generic clocked `Delay` 已真实 typecheck、其
finite trace 证明已核验、并且 exact H0 dependency closure 被同一 map 支付后，M1 才可前进到
`H0MAP_CANDIDATE`。

## 5. 可复核入口

- [fixed `gcubical` branch](https://github.com/hansbugge/cubicaltt/tree/gcubical)
- [README at fixed commit](https://github.com/hansbugge/cubicaltt/blob/c2c5262b6637c09e37d3add55babd3400c839b93/README.md)
- [grammar at fixed commit](https://github.com/hansbugge/cubicaltt/blob/c2c5262b6637c09e37d3add55babd3400c839b93/Exp.cf)
- [clocked CoNat/force example](https://github.com/hansbugge/cubicaltt/blob/c2c5262b6637c09e37d3add55babd3400c839b93/examples/dataclocks.ctt)
- [guarded stream example](https://github.com/hansbugge/cubicaltt/blob/c2c5262b6637c09e37d3add55babd3400c839b93/gctt-examples/streams.ctt)
