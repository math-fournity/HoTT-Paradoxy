# ZFC-COFORGE-004：L7 obligation-mode 独立复核

> **身份：** `EXTERNAL_CLI_BEHAVIOR_PROBE / MATCHTRACE_REVIEW / NOT_A_ZFC_RESULT`。
>
> **结论：** `ANSWERABLE_FALSE_BRANCH`。代理对前一张 P1 理由卡作独立、结构化的 E0–E7 审查，确认非反身的 membership 真值条件仍不是 source-supplied consumer 的正完成义务。

## 运行身份

| 字段 | 记录 |
|---|---|
| CLI | `codex-cli 0.157.0` |
| 工作根 | `/tmp/pattern-p-zfc-coforge-004-l7-review` |
| 模型请求 / effort | `gpt-5.6-terra` / `max` |
| sandbox / approval | `read-only` / `never` |
| session | `01a0fcfa-5379-7842-8643-560af9a32ef5` |
| 输入 | 中性 ZFC source card、COFORGE-003 的公开理由卡、L7 定义；禁止项目历史、网络、命令和写入 |

## 独立代理的 E0–E7 理由链

### E0：范围

审查只判断 `Q(a)=∀x(x∈a→∀y(y∈x→y∈a))` 是否有 L7 所要求的 obligation mode；不判断它是否有趣、是否为 ZFC 定理、某个 a 是否满足它，或是否存在更广泛的 ZFC 问题。

### E1：实际使用的 source facts

代理明确依赖：对象为集合且 membership 是 relation；幂集见证可从 a、再从 p₁ 形成 p₁/p₂；card 没有肯定 membership 才算完成的规则；它也没有 formula coding、satisfaction、construction machine、由 Q 条件化的后续 formation。Bounded separation、Replacement、Foundation 均不为 Q 提供正完成前提。

### E2：两个竞争读法

1. **有利读法：** 把 membership 当成 `(a,p₂)` 的原生 consumer。Q 区分 affirmative 与 negative branch，但 negative branch 仍是完成的成员关系判断。
2. **严格读法：** card 只给 relation，没有 evaluator、certificate 或 completion protocol；甚至未建立 operational consumer，因此可能是 `SOURCE_CONSUMER_GAP`。

代理采用第一个、对候选最有利的读法，并指出：即便在该读法下，L7 仍不通过。

### E3：字段映射

| 字段 | source 支持的角色 | L7 结果 |
|---|---|---|
| `a` | 已给集合输入 | 起始对象 |
| `p₁` | a 的幂集见证 | formation 不以 Q 为条件 |
| `p₂` | p₁ 的幂集见证 | formation 不以 Q 为条件 |
| `a∈p₂` | membership query | 唯一可能的 consumer |
| `Q(a)` | 报告所给 affirmative condition | 只刻画 true branch |
| `¬Q(a)` | negative branch | 可以是完成的 query result |
| unpaid formation obligation | 未识别 | card 中没有由 Q 条件化的后续对象 |

### E4：选中／拒绝的读法及理由

代理选有利的 membership-query 读法，拒绝“只有 affirmative answer 才算完成”的隐含读法。理由是 card 没有指明 false 是未完成、错误或 formation failure。`T4` 的非反身性只能说明 affirmative branch 非自动获得，不能使它变为成功前提；`T5/T6` 只给出与反身性邻近项的比较，不能补出 affirmative-only Done。

### E5：最小推演与三种完成后果

报告的链是 `a → p₁ → p₂ → membership query a∈p₂ → Q(a) as positive-branch condition`。

- **true：** 可以获得 affirmative answer；这是答案结果，未表明形成之前必须支付 Q。
- **false：** 可以获得 negative answer；在有利读法中，这仍是完成的 relation judgment。
- **blocked：** card 缺评价器／构造机，但该缺失不选择性阻断 false 或 true，也不令 p₁/p₂ 的形成等候 Q。

### E6：反事实

如果 source 另行规定：给定 `(a,p₂)` 的某项明确 consumer task 只有产出 `a∈p₂` 的 affirmative certificate 才算 Done，并且 false 被视为 non-completion，那么 Q 才可成为正完成前提。实际 card 没有该事实。

### E7：判词

```text
ANSWERABLE_FALSE_BRANCH
```

该结论是在赋予候选最宽松、最有利的 membership-consumer 解释后得到；因此它不能借收紧为“无 consumer”来逃避 L7。

## 主研究者判词与范围

这个外部复核支持将 L7 加入 P1：它表明 COFORGE-003 的理由链并非仅因主研究者偏好而被否决。它只证明两份独立、prompt-bounded 报告在同一中性卡上给出了相容的公开理由。它不证明 ZFC 的关系判断在一般情况下总是这样运行，也不排除未来固定的真实 consumer 带来一个不能以 false 分支正常完成的不同 Q。
