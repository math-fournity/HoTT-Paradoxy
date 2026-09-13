# SEM-B01：真实截断消费者的 B 方向资格检查

> 资产身份：`CANDIDATE_NOT_CURRENT / CONTRIBUTOR_RESEARCH_ARTIFACT`
>
> 日期：2026-09-13
>
> 分支：`codex/semantic-overview`
>
> 基线：`a22f41ecf5c3becdd192383ff6cdbc846982813b`
>
> 当前判词：`KERNEL_CHECKED_AND_RUNTIME_OBSERVED_WITH_SCOPE / EXECUTION_GAP_WITHOUT_DELIVERY_PROMISE / E6_BOUNDED_NEGATIVE`

## 1. 问题与边界

本单元检查 B 方向的一个最小真实切片：已有词汇扫描找到的两个 agda-unimath 截断消费者，是否把较弱的数学资格提升成了并未取得的有效完成资格。

C3 对 B 方向的当前定义是：理论只取得 `Q1/Q3`，但解释、接口或使用把它提升成 `Q4/Q7`；要升级到 `NATURAL_USAGE_MISMATCH`，还必须找到自然、明确、可回查的使用点。C11 v2 也要求定位“把尚未完成当作已经取得”发生在哪一步、由哪条规则或接口支持。本单元因此分开检查：

1. 它是不是截断的真实消费者；
2. 它的类型和实现要求了哪些补偿证据；
3. 下游到底得到见证、与见证无关的数据，还是仅仅得到一个命题；
4. 已检查的源码有没有把数学函数进一步承诺成有限完成的程序或现实交付。

本文件是源码审计，不是新的 HoTT 定理，不向 `HoTT/CLAIM_EVIDENCE_MATRIX.md` 增加 claim，也不把外部库源码阅读冒充本分支的 kernel replay。

## 2. 固定输入

| 输入 | 身份 |
|---|---|
| 当前 repo 基线 | `a22f41ecf5c3becdd192383ff6cdbc846982813b` |
| 历史扫描报告 | `audit/coarse-consumer-scan-20260913.json`；SHA-256 `284027e88951986a20398bc025e156ba7cae399a571345fbe3abbf5388cbc258` |
| 扫描器 | `scripts/audit/scan_coarse_consumers.py`；SHA-256 `fa74cf3275a4c23e10148b8b12cf1f01345df2c75d7158d51deb2b2ecf66526d` |
| 外部源码树 | `/Volumes/D/HoTT-toolchain-cache/agda-unimath-7b81411d/src`；扫描树 SHA-256 `ca8fa3a17dc184bcfd494f68dfcc02ad5eeb5fa4a901660f17307634943a3b26` |
| `set-truncations` | `foundation/set-truncations.lagda.md`；SHA-256 `78657b114c2934e99bbb7e91779f54f372eccbb5209cf6fb1c5781374093cfd2` |
| `trunc-Prop` 到集合的泛性质 | `foundation/universal-property-propositional-truncation-into-sets.lagda.md`；SHA-256 `cf8053a8ed20ddccb003b000f5381f9186a542afa4e18436ec9dd1878319b51c` |
| 第一个下游样本 | `foundation/0-connected-types.lagda.md`；SHA-256 `b59f06c845fb9641ebc4d404ccb687ac52e599eb476f3cd964a3462e9c97657a` |
| 第二个下游样本 | `commutative-algebra/polynomials-commutative-semirings.lagda.md`；SHA-256 `b69a55daf595ba8fd57aad80b4300ca9ebf53255e162777ad0ea6386a540a792` |
| 固定工具链 | Agda `2.8.0-3d04bac`；binary SHA-256 `ac285c193c30ed0f5e1073a2623ae312c7165a4d344940b5c504ce6a2fe1741e`；Node `v26.7.0` |
| 第二阶段 run | `semantic-overview/runs/20260913-SEM-B01-TRUNCATION-DELIVERY-001-01/`；12/12 步符合预期 |

历史扫描报告对 agda-unimath 的记录仍与当前树一致：3,056 个文件、50 个命中、30 个无词汇义务 token 的待人工项。2026-09-13 在本分支重跑扫描器时，repo 自身的 formal 文件数已由历史报告的 34 变为 44，树哈希由 `264f7297…` 变为 `e95770ef…`，但命中仍为 6。因而历史 JSON 可以继续固定当时的审计快照，不能被当作当前 repo-formal 全量清单；本分支不回写或覆盖历史报告。

## 3. 调用链 A：集合截断中心只导出“仅仅存在”

### 3.1 消费接口

`foundation/set-truncations.lagda.md:208-212` 的接口为：

```agda
apply-universal-property-trunc-Set' :
  (t : type-trunc-Set A) (B : Set l2) →
  (A → type-Set B) → type-Set B
```

它确实以 `type-trunc-Set A` 中的项为输入，所以“真实截断消费者”这一判断成立。它同时要求一个集合余域 `B` 和一个已经给出的映射 `A → B`；实现只是把该映射经集合截断的泛性质延拓，然后应用到 `t`。

### 3.2 下游实际输出

`foundation/0-connected-types.lagda.md:75-81` 用它证明：

```agda
is-inhabited-is-0-connected : is-0-connected A → is-inhabited A
```

该调用把集合截断的中心传给消费者，余域取 `set-Prop (trunc-Prop A)`，映射取 `unit-trunc-Prop`。而 `foundation/inhabited-types.lagda.md:45-49` 明确定义：

```agda
is-inhabited-Prop X = trunc-Prop X
is-inhabited X = type-Prop (is-inhabited-Prop X)
```

所以这条链的输出仍是命题截断中的“仅仅存在”，不是 `A` 的具体元素，也没有提供统一选点函数。

### 3.3 判词

`LEGITIMATE_CONSUMER_NO_LIFT`：该链从集合截断得到命题级居留，停留在 `Q1`；在已检查的类型和实现中没有 `Q1 → Q2/Q4/Q7` 的升级点。它可作为 B 方向的负控制，不构成 E6。

## 4. 调用链 B：截断的次数界导出与界无关的多项式值

### 4.1 消费接口中的显式义务

`foundation/universal-property-propositional-truncation-into-sets.lagda.md:97-104` 的接口为：

```agda
map-universal-property-set-quotient-trunc-Prop :
  (B : Set l2) (f : A → type-Set B) →
  is-weakly-constant-map f → type-trunc-Prop A → type-Set B
```

它从命题截断输出集合中的数据，但调用者必须同时给出：

- 原见证到输出的函数 `f`；
- `f` 对任意两个见证给出相等结果的证明 `is-weakly-constant-map f`；
- 集合余域 `B`。

实现先构造 `f` 的命题性像，再用命题截断的泛性质消去到该命题，最后投影出 `B` 中的值。这不是从截断中恢复某一个原见证。

### 4.2 多项式求值样本

`commutative-algebra/polynomials-commutative-semirings.lagda.md:101-115` 把多项式定义为一个形式幂级数，外加“存在次数界”的命题截断。具体的次数界类型是：

```agda
Σ ℕ (is-degree-bound-formal-power-series-Commutative-Semiring p)
```

`ev-degree-bound-formal-power-series-Commutative-Semiring` 在给定具体次数界时定义有限和。随后源码把 `eq-ev-degree-bound-formal-power-series-Commutative-Semiring` 声明为“任意两个次数界所得求值相等”的证明项；其函数体在 `:298-411` 比较两个自然数界，并用较大界新增项均为零来构造等式。第二阶段已用 `--ignore-interfaces` 对该多项式模块及实际加载的 622 个模块做 fresh kernel 重放，exit 0。

最终 `:419-427` 定义多项式求值：

```agda
ev-polynomial-Commutative-Semiring (p , deg-bound-p) x =
  map-universal-property-set-quotient-trunc-Prop
    (set-Commutative-Semiring R)
    (ev-degree-bound-formal-power-series-Commutative-Semiring p x)
    (eq-ev-degree-bound-formal-power-series-Commutative-Semiring p x)
    deg-bound-p
```

按这组源码声明，这里从截断的“存在某个次数界”得到半环元素，因此它比命题余域样本更适合检验 B 方向。不过，接口要求调用者提交弱常值证明项，使结果不依赖选择哪个次数界；接口没有返回次数界，也没有把一个未知见证包装成已选见证。

### 4.3 判词

`LEGITIMATE_WEAKLY_CONSTANT_DATA_FACTORING`：固定工具链已检查这条 `Q1 + 明示的见证无关性证明 → Q3` 数学路径。它仍不自动提供特定后端、资源界、终止行为或现实交付能力；第二阶段的运行证据见下一节。

这个样本也说明，扫描器的 `has_obligation_token = false` 不能解释为“没有义务”：弱常值义务出现在签名中，但 v1 token 表对连字符形式 `weakly-constant` 没有覆盖。词汇字段只能用于排队，不能承担语义分类。

## 5. 第二阶段：kernel、判断相等、生成与运行分层

### 5.1 截断实现的实际身份

`foundation/truncations.lagda.md:44-68` 明写 “We postulate the existence of truncations”，并把下列四项声明为 postulate：

```agda
type-trunc
is-trunc-type-trunc
unit-trunc
is-truncation-trunc
```

固定源码的 `truncations`、`propositional-truncations` 和“命题截断到集合的泛性质”三个模块中，没有为这些项提供 JS/GHC `COMPILE` pragma。因而库提供的是可供 kernel 使用的 HoTT 公理化接口；这份实现本身没有给 postulate 提供后端计算定义。

### 5.2 闭合探针与实际结果

探针源码位于 `semantic-overview/formal/sem-b01/`，完整 run 位于 `semantic-overview/runs/20260913-SEM-B01-TRUNCATION-DELIVERY-001-01/`。

| 层 | 探针 | 实际结果 | 支持范围 |
|---|---|---|---|
| 外部数学源码 | 多项式模块 `--ignore-interfaces` | exit 0；622 条 `Checking` | 固定版本的多项式定义与传递加载闭包被 kernel 接受 |
| 闭合数学正例 | `SemB01Kernel.agda` | exit 0 | 从 `unit-trunc-Prop star` 经弱常值消费者所得 Bool 有一个命题等式到 `true` |
| 判断相等负例 | `SemB01DefinitionalNegative.agda` | exit 42；`[UnequalTerms]` | 同一等式不能由 `refl` 建立；该实现没有相应 judgmental reduction |
| 运行正控 | `SemB01DirectRuntime.agda` | typecheck 0；JS 生成 0；Node 0，输出 `TRUE` | 相同 Agda/JS/Node 与库 Bool 的直接路径可运行 |
| 截断运行探针 | `SemB01TruncatedRuntime.agda` | typecheck 0；JS 生成 0；Node 1 | 加载 `unit-trunc-Prop` 时出现 `unit-trunc is not a function`；没有返回错误 Bool |
| GHC 路径 | `SemB01Kernel.agda --compile --ghc-dont-call-ghc` | 源码生成 0；未执行 | 生成源码对四个 postulate 都写入 `MAlonzo Runtime Error: postulate evaluated`；本机无 GHC |

JS 生成物把四项明确导出为 `undefined`；GHC 生成物保留四条明确的 postulate-evaluated 错误。直接正控确认 Node/JS 能执行生成的 main 并调用 Bool FFI；判断相等负例与运行失败共同表明：kernel 中的命题计算律不能被当作本实现的判断相等或后端程序计算律。

**B02 后续校验修正正控边界**：B01 的 `printBool` FFI 使用 JavaScript truthiness，而 agda-unimath 的 Bool 构造子在生成代码中是 Scott 编码函数。B01 的输入固定为 `true`，所以输出 `TRUE` 与该输入一致，但这个正控不能证明 FFI 能区分两个构造子。B02 改用构造子消去式 FFI，并让显式 `false` 分支实际输出 `FALSE`。该限制不影响 B01 截断探针在加载 `unit-trunc-Prop` 时的独立运行错误。

完整多项式值没有被实际执行；运行探针用 `unit`、`bool` 和同一个 `map-universal-property-set-quotient-trunc-Prop` 隔离了截断消费者的执行边界。因此本轮支持的是“这个公理化截断接口在当前后端没有运行实现”，不外推到所有命题截断实现或所有 HoTT 工具链。

### 5.3 自然承诺搜索

固定源码中，这个泛性质函数在定义模块之外只有四个直接调用点：多项式求值、交换幺半群有限乘积、交换半群有限乘积、交换二元运算。四处都显式提交弱常值/同余证明项。

对定义模块、四个直接调用者及多项式的交换环包装层共 6 个文件，搜索 `executable/execution/runtime/compile/compiler/backend/program/algorithm/termination/resource/complexity/extract/effective/real-world` 为 0 个命中。根 README 把项目说明为单价数学形式化与供数学家使用的信息资源；它没有为这些接口声明后端执行或现实资源承诺。

这只是固定提交和固定调用闭包的有界负结论，不证明外部文章、下游项目或未来版本从未作出更强承诺。

### 5.4 第二阶段判词

1. `KERNEL_CHECKED_WITH_SCOPE`：数学接口与多项式调用链在固定 Agda/agda-unimath 组合中通过。
2. `RUNTIME_OBSERVED_WITH_SCOPE`：JS 可生成，但强制使用 postulated truncation 时显式失败；直接 Bool 正控成功。
3. `EXECUTION_GAP_WITHOUT_DELIVERY_PROMISE`：当前实现缺少截断后端语义，但已检查的库接口和文档没有把它承诺为有效程序。
4. `E6_BOUNDED_NEGATIVE`：固定的四个直接消费者中没有发现 `Q1/Q3 → Q4/Q7` 自然资格升级。

这不是 `NATURAL_USAGE_MISMATCH`，也不是 HoTT 内部矛盾。若未来外部消费者把“Agda 接受/JS 生成成功”明确当作“程序可运行”，本 run 可作为重新打开 B 方向的执行反例基础。

## 6. 本单元减少了什么未知

1. 两个原始条目都是真实消费者，原审计 F5 的更正得到源码与 kernel 两层复核。
2. `apply-universal-property-trunc-Set'` 的选定链没有离开命题层。
3. `map-universal-property-set-quotient-trunc-Prop` 的全部四个直接自然调用者都显式提交弱常值/同余证据。
4. 多项式源码通过 fresh kernel 重放；“数学上定义求值”这一层已经固定。
5. 当前 agda-unimath 截断是 postulated，命题计算律不构成 judgmental reduction；JS/GHC 生成成功不构成运行成功。
6. 实际 Node 失败是显式未实现 postulate，不是静默输出错误结果。
7. 固定调用闭包中没有发现有效执行或现实交付承诺，所以当前没有 E6。

## 7. 切片关闭与下一工作单元

本切片已达到预定停止条件中的 `BOUNDED_NEGATIVE`，不再继续打磨同一截断例子。下一单元拟定为 `SEM-B02`：寻找“命题级有限性/可判定性证明”被自然下游用来选择分支或驱动计算的接口，优先检查 codomain 是 decidable sum/Bool 且确有模式匹配消费者的链。它与本轮“见证无关的代数值”是不同消费者类别。

`SEM-B02` 仍使用五层判据：类型可形成、kernel 可检查、闭合项可归约、后端可执行、现实完成。只有出现真实承诺与实际升级点才进入 F-011；否则形成新的有界负控制并返回 B 方向的下一类别。

## 8. 对 canonical integrator 的候选建议

当前不建议升级主线悖论判词或修改 claim matrix。未来集成人若接受本单元，可考虑：

- 把这两个初始消费者以及 `map-universal-property-set-quotient-trunc-Prop` 的四个直接调用点标为已语义分类的负控制；
- 将“postulated truncation：kernel 接受、后端生成、运行不可用”作为 Q3/Q4 分层实例，而不是 HoTT 缺陷；
- 在词汇扫描器后续版本中增加 `weakly-constant` 提示，同时保留“token 命中不证明义务成立”的边界；
- 刷新 repo-formal 扫描时生成新的版本化快照，不覆盖 2026-09-13 的历史 JSON。

这些都是候选更新，尚未成为项目 current truth。
