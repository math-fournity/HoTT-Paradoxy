# P9-SHOTT-DIRUNIV-CORPUS-DENOMINATOR-001：directed-univalence 形式化语料审计

**状态：** `NOT_A_CONSUMER / DEFENSE_EXPLICIT_COVARIANT_MODAL_STRUCTURE / P10_SECOND_SUCCESSOR_DISCOVERY_NEXT / NO_NEW_HOTT_DEFECT_CLAIM`  
**日期：** 2026-09-21  
**固定分母：** `LIshy2/sHoTT@e76c196293dc402de945d3bcf9873ce84635ff76`，`diruniv` branch。  
**任务：** 检查 Rzk 所指向的 directed-univalence formalisation corpus 是否从裸输入推到原圆环 `Done_s`，或是否显式保留协变/模态/定向结构。

## 1. 语料身份与本地重复检查

sHoTT README 说明它是使用 Rzk 的 simplicial HoTT / synthetic ∞-category formalization library；Rzk 的 modalities 文档把 `LIshy2/sHoTT` 的 `diruniv` branch 指为 directed-univalence/modalities formalisations。因此它是 P8 Rzk runtime 之外的、具实际 proof corpus 的新分母。

本地历史资料早已登记 directed interval 与 directed univalence 的论文和 discovery candidate，但未对 `diruniv` branch 的实际 `05-diruniv.rzk.md` 做 P7 五项检查。P9 的来源冻结保存 branch、commit、七个 source blob/SHA、raw URL、assumptions/postulates 与限域负检索，见 [`P9-SHOTT-DIRUNIV-SOURCE-FREEZE.json`](P9-SHOTT-DIRUNIV-SOURCE-FREEZE.json)。

## 2. 实际代码所做的事情

`05-diruniv.rzk.md` 明确声明 `funext`、`weakfunext`、`extext`。它定义：

```text
S := Σ (A : U), is-a-cov A
morphism := f : 𝕀 → S
mor2fun(f) := (f 0₂, f 1₂, covariant transport …)
```

随后 `dirglue` 接受显式 `A,B : S` 和 `f : first A → first B`，并利用协变结构、纤维、transport 和 endpoints 构造其结果。`06-simpliciality.rzk.md` 还显式声明 `simp-monad`、其 simpliciality 及 pure map 的 postulates。故该语料不是“无结构的普通等价自动完成任务”；它把方向、协变资格、端点、函数和额外假设/公设留在可见输入与依赖层。

## 3. P7 五项 K 判别

| 条件 | P9 直接证据 | 判定 |
|---|---|---|
| `K-version` | branch、commit、七个 blob/SHA、raw URL 固定。 | `PASS_VERSION_IDENTITY` |
| `K-input` | `S` 的元素携带 `is-a-cov`，morphism 是 `𝕀→S`，`dirglue` 显式接收 A/B/f。 | `FAIL_AS_K / EXPLICIT_COVARIANT_STRUCTURE` |
| `K-output` | `mor2fun` 返回 endpoints 与函数；`dirglue` 形式化协变函数/transport 关系。 | `NO_ORIGIN_DONE_OUTPUT_WITHIN_DECLARED_SCOPE` |
| `K-claim` | README 的目标是 synthetic ∞-category theorem formalisation；选择的源码没有将圆去点—闭合—复原宣称为 `Done_s`。 | `NO_SAME_TASK_DONE_CLAIM_WITHIN_DECLARED_SCOPE` |
| `K-forgetting` | 代码把 `is-a-cov`、directed interval、modal/transport 前提显式带入；`#assume` 与 `#postulate` 也没有被隐藏。 | `FAIL_AS_K / EXPLICIT_ASSUMPTION_AND_STRUCTURE_DEFENSE` |

P9 中的精确负检索只覆盖固定 triangulated/simplicial-hott 文件与原圆环术语；它不证明整个 branch 或所有 sHoTT formalization 没有其他相关例子。

## 4. 对研究主线的实际意义

P9 比 P8 更强，因为它不只是检查语言层 primitive，而是检查 directed-univalence 的实际 formalization：该 corpus 仍然把对象的协变证明、定向区间、端点、函数、transport 和部分公设显式写在输入/依赖中。这是 P7 所要求的 `DEFENSE_PRESERVES_TASK` 形态。

该结果不能被误读为“只要加模态就解决现实问题”。它只表明这份固定语料没有把 `U_bare` 当作用户的 `Done_s`。它也不能被误读为基础 HoTT 已经具有这些额外结构；P9 反而证明了该 corpus 工作在扩展/富化层，且必须对假设和 postulate 保持可见。

## 5. 波次反思与 P10

1. **最终目标连接：** P9 使用实际 formalization corpus 复核 P7 的 K gate，而非从论文标题推断。
2. **新增事实：** `diruniv` 的中心对象 `S` 明确是带 `is-a-cov` 证明的 Σ-type，morphism 与 `dirglue` 明确要求定向/协变/endpoint/function 数据，且部分邻近原则明列为 postulates。
3. **为何停止 P9：** 这个具体 `diruniv` 分母的 K-input/K-claim 已被直接源代码否定；继续同一文件的关键词扩展不会产生 P7 K。
4. **反解释：** branch 中还可能有未审专题；P9 的结论不外推到整库。但 P10 不应机械把所有 sHoTT 文件逐一读完，而应重新比较剩余候选空间，优先寻找真正可能 `U_bare → Done_s` 的实际消费者或独立更强 R。

P10 是一次**第二 successor discovery**：它必须先检查 P1–P9 的禁止重复表、当前社区实现和本地历史资产，再在规则、消费者、对象理论和实现差异之间选择一个新的、不同的有界分母。只有这样，连续 Goal 才不是把同一条防御链无限拉长。

## 6. 结论

P9 的范围结论是 `NOT_A_CONSUMER / DEFENSE_EXPLICIT_COVARIANT_MODAL_STRUCTURE`。它没有提供实际 K，也没有构成 HoTT 缺陷。它把下一步严格限为 `P10-SECOND-SUCCESSOR-DISCOVERY-001`。
