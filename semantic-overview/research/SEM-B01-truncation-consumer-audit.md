# SEM-B01：真实截断消费者的 B 方向资格检查

> 资产身份：`CANDIDATE_NOT_CURRENT / CONTRIBUTOR_RESEARCH_ARTIFACT`
>
> 日期：2026-09-13
>
> 分支：`codex/semantic-overview`
>
> 基线：`a22f41ecf5c3becdd192383ff6cdbc846982813b`
>
> 当前判词：`SOURCE_INSPECTED_WITH_SCOPE / NATURAL_USAGE_MISMATCH_NOT_ESTABLISHED`

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

`ev-degree-bound-formal-power-series-Commutative-Semiring` 在给定具体次数界时定义有限和。随后源码把 `eq-ev-degree-bound-formal-power-series-Commutative-Semiring` 声明为“任意两个次数界所得求值相等”的证明项；其函数体在 `:298-411` 比较两个自然数界，并用较大界新增项均为零来构造等式。本分支目前只核对了源码类型与构造路径，尚未重新运行 kernel。

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

`LEGITIMATE_WEAKLY_CONSTANT_DATA_FACTORING`：源码建立的是 `Q1 + 明示的见证无关性证明 → Q3`。在已检查的调用链中，尚未出现把该数学函数称为具有特定后端、资源界、终止行为或现实交付能力的 `Q4/Q7` 承诺，所以 `NATURAL_USAGE_MISMATCH` 仍为 `NOT_ESTABLISHED`。

这个样本也说明，扫描器的 `has_obligation_token = false` 不能解释为“没有义务”：弱常值义务出现在签名中，但 v1 token 表对连字符形式 `weakly-constant` 没有覆盖。词汇字段只能用于排队，不能承担语义分类。

## 5. 本单元减少了什么未知

1. 两个条目都是真实消费者，原审计 F5 的更正得到源码级复核。
2. “真实消费者”和“资格越级”必须保持分开：真实消费本身不建立 E6。
3. `apply-universal-property-trunc-Set'` 的选定下游链没有离开命题层。
4. `map-universal-property-set-quotient-trunc-Prop` 可以合法产生集合数据，但其关键支付装置是显式弱常值证明；多项式调用者实际提交了该证明。
5. 当前仍缺的不是另一个截断小定理，而是一个自然使用点对 `Q4/Q7` 的真实承诺，以及与该承诺相称的执行或现实证据。

## 6. 下一步与停止条件

下一步只沿调用链 B 继续一层，避免重新做整库词汇扫描：

1. 固定同输入、同输出与完成标准，检查 agda-unimath 的截断实现、构建/提取边界以及多项式求值的闭合样本；
2. 分开记录“类型可定义”“kernel 可检查”“闭合项可归约”“后端可执行”和“现实资源内完成”；
3. 搜索这个具体 API 的文档和自然下游是否明确承诺后两项；没有承诺时只能给出有界负结论；
4. 只有定位到真实 `Q1/Q3 → Q4/Q7` 升级点，才冻结精确命题并决定是否进入 F-011 机器证明门禁。

本切片在以下任一条件达到时停止：

- 找到可回查的有效交付承诺，并形成一个与之严格同任务的可执行反例候选；
- 已检查的自然调用链只承诺数学函数或命题，归类为 `BOUNDED_NEGATIVE`；
- 工具链或依赖身份不足以判断，归类为 `SOURCE_OR_RUNTIME_CHAIN_INCOMPLETE` 并列出唯一缺口。

## 7. 对 canonical integrator 的候选建议

当前不建议修改主线判词、方向投影或 claim matrix。未来集成人若接受本单元，可考虑：

- 把这两个消费者从“队列开放”进一步标为“已语义分类的负控制”；
- 在词汇扫描器的后续版本中把 `weakly-constant` 作为提示 token，但不得让 token 命中自动等同于义务已满足；
- 刷新 repo-formal 扫描时生成新的版本化快照，不覆盖 2026-09-13 的历史 JSON。

这些都是候选更新，尚未成为项目 current truth。
