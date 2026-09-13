# SEM-B03：finite decision 的外部有效交付消费者搜索

> 资产身份：`CANDIDATE_NOT_CURRENT / CONTRIBUTOR_RESEARCH_ARTIFACT`
>
> 日期：2026-09-13
>
> 分支：`codex/semantic-overview`
>
> 当前判词：`WEB_SEARCH_WITH_SCOPE / E6B_CONSUMER_SOURCE_GAP / NATURAL_USAGE_MISMATCH_NOT_ESTABLISHED`

## 1. 触发与问题

SEM-B02 已经找到 `has-decidable-equality-is-finite` 的自然理论消费者，并把 E6 候选拆成：

- `E6a`：理论内自然消费；
- `E6b`：有效程序或现实交付承诺；
- `E6c`：同任务承诺与真实完成失配。

本轮只搜索 `E6b`：是否存在公开、可回查的外部应用、教程、插件或下游包，把这个 exact theorem 或同一 agda-unimath finite-decision 链接到可执行 main、服务接口或资源内完成承诺。

## 2. 搜索范围

2026-09-13 使用公开网页搜索，查询包括：

```text
"has-decidable-equality-is-finite" Agda
site:github.com "has-decidable-equality-is-finite"
site:github.com -"UniMath/agda-unimath" "has-decidable-equality-is-finite"
-site:unimath.github.io -site:github.com/UniMath/agda-unimath "has-decidable-equality-is-finite"
"map-universal-property-set-quotient-trunc-Prop"
agda-unimath executable JavaScript backend compile
```

同时读取：

1. [agda-unimath 当前生成页：Equality in finite types](https://unimath.github.io/agda-unimath/univalent-combinatorics.equality-finite-types.html)；
2. [agda-unimath GitHub 项目入口](https://github.com/UniMath/agda-unimath/)；
3. [Agda 2.8.0 编译器文档](https://agda.readthedocs.io/en/v2.8.0/tools/compilers.html)；
4. [Agda 2.8.0 postulate 文档](https://agda.readthedocs.io/en/v2.8.0/language/postulates.html)；
5. [Agda 2.8.0 FFI 文档](https://agda.readthedocs.io/en/v2.8.0/language/foreign-function-interface.html)。

搜索没有使用登录后的 GitHub Code Search，也没有克隆 103 个 forks 或穷举所有依赖仓库；因此结果是公开搜索索引范围内的负结论，不是全网不存在证明。

## 3. exact-name 外部消费者结果

`has-decidable-equality-is-finite` 的公开搜索结果只定位到 agda-unimath 自己的生成文档；未定位到独立第三方仓库、教程 main、服务接口或插件。`map-universal-property-set-quotient-trunc-Prop` 同样没有出现独立外部使用结果。

当前 agda-unimath 页面仍把该接口放在 “Any finite type has decidable equality” 的数学性质章节，并展示经命题截断泛性质构造的证明项。GitHub README 把项目定位为单价数学形式化课程和面向数学家的信息资源；公开入口没有声称该 theorem 是后端可运行的有限等式算法。

所以当前最强结论是：`EXACT_NAME_EXTERNAL_EFFECTIVE_CONSUMER_NOT_FOUND_IN_SEARCH_SCOPE`。这不排除未被索引的代码、fork 内用法、名称被包装后的调用或私有项目。

## 4. 官方 Agda 合同与本地运行的关系

### 4.1 `--js` 的承诺边界

Agda 2.8.0 文档说明 `--js` 把 Agda 模块翻译为 JavaScript，`--js-optimize` 生成优化代码；`--js-verify` 只对 main 之外的生成模块运行 Node 来检查语法错误。它没有把“代码生成 exit 0”定义成“包含任意 postulate 的 main 一定可完成”。

这与 SEM-B01/B02 的观察一致：JavaScript 文件生成成功，实际执行在未实现的 `unit-trunc` 处失败。编译状态是 `SOURCE_GENERATED`，运行状态仍须单独验证。

### 4.2 postulate 与 FFI

Agda 2.8.0 将 postulate 定义为“有类型但没有随附定义的元素”。FFI 文档进一步规定：`COMPILE <Backend>` pragma 才把后端信息关联到一个名称；其中 JavaScript FFI 可为 postulate、构造子或数据类型提供代码。文档还明确区分 type-checking 与 runtime：FFI runtime 定义不改变 type-checking 时把它视为 postulate 的事实。

固定 agda-unimath 的 `type-trunc`、`unit-trunc`、`is-trunc-type-trunc`、`is-truncation-trunc` 没有相应 JS/GHC `COMPILE` pragma。SEM-B01/B02 生成物中的 `undefined` 与 postulate runtime error 因而符合官方机制，不是后端偷偷给出了错误的截断语义。

### 4.3 编译器是不是 E6b？

Agda 编译器是实际交付路径，但其官方合同要求调用者为外部/postulated 运行语义提供 FFI。当前源码没有支付这一义务，Node 也显式失败。把 `--js` exit 0 单独提升为“该 theorem 是可运行决定过程”将是审计者自己的越级，不能据此反向制造 E6b。

## 5. E6 三分状态

| 子项 | 当前状态 | 证据 |
|---|---|---|
| `E6a` 理论内自然消费 | `YES` | SEM-B02：16 文件 exact-name 使用；exclusive-sum 与 orientation 分支链 |
| `E6b` 有效交付承诺 | `CONSUMER_SOURCE_GAP` | 公开 exact-name/同接口搜索只回到上游数学文档；官方 FFI 要求未被该截断实现满足 |
| `E6c` 同任务失配 | `NOT_ESTABLISHED` | 没有固定外部消费者的输入、输出、完成标准和实际失败对照 |

因此仍不能给出 `NATURAL_USAGE_MISMATCH`。SEM-B02 的 Node 失败保留为未来外部消费者出现时可复用的执行反例，不自行承担消费者承诺。

## 6. 搜索停止与重开条件

exact-name 公开搜索到此按收益/成本停止。以下任一材料出现时重开：

1. 一个固定 commit 的第三方仓库实际导入该 theorem 或其 wrapper，并把结果接到 main、API 或编译产物；
2. 教程或文档明确声称 `is-finite → has-decidable-equality` 在 agda-unimath 当前 postulated truncation 下可执行；
3. agda-unimath 为截断 postulate 增加 JS/GHC FFI 或改用具有计算规则的实现；
4. 可用的 authenticated code search、完整 fork/dependency corpus 或用户提供的具体消费者扩大证据范围。

没有这些输入时，继续扩大同义词网页搜索很可能只找到一般 Agda 编程、其它有限集表示或上游镜像，不能闭合 E6b。

## 7. 下一研究方向

这一轮说明，纯库内搜索已经把 B 方向推进到“理论 consumer 有，delivery consumer 缺”。下一项应切换规则/应用域，而不是继续枚举 finite theorem 的内部调用点。可选的下一有界单元是：在真实证明助手插件或反射/代码生成系统中，查找“已证明存在/已分类”被明确接到验证器、生成器或服务完成承诺的接口；这与 machine-overview 的时间/运动线保持互补。

任何新候选仍须先固定外部消费者版本、同一任务规格和实际运行入口，再决定是否进入 F-011。

## 8. 对 canonical integrator 的候选建议

未来 integrator 若接受本轮结果，可以把外部状态登记为 `E6B_CONSUMER_SOURCE_GAP`，并保留上述重开条件。不要把“公开搜索未命中”改写成“外部消费者不存在”，也不要把官方 `--js` 翻译能力改写成对未实现 postulate 的运行保证。
