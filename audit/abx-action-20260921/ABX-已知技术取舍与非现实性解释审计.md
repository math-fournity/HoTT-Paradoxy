# ABX：已知技术取舍、非现实性解释与剩余问题审计

> 状态：`SOURCE_INSPECTED_WITH_SCOPE / INTERPRETIVE_CLAIMS_NOT_MACHINE_PROVED`  
> 机械来源核对：[ABX-KNOWN-TRADEOFF-VERIFICATION.json](ABX-KNOWN-TRADEOFF-VERIFICATION.json)  
> 外部实现文献：Simon Huber, “Canonicity for Cubical Type Theory,” Journal of Automated Reasoning 63 (2019), DOI [10.1007/s10817-018-9469-1](https://link.springer.com/article/10.1007/s10817-018-9469-1)。

## 1. Book §11.2 知道的是什么

Book 确实明确讨论了 Dedekind real 的宇宙层级问题：若用一个特定 universe 的命题来定义 cut，实数会升到下一 universe。它把“避免繁琐的 universe bookkeeping”说成文本中的 simplifying assumption，并列出四种处理方式：逐层跟踪、propositional resizing、仅对 mere propositions 的 LEM、以及 initial σ-frame 的构造路线。

这支持的结论是：作者知道这里存在**形式化表达、大小和公理选择的技术取舍**。它不支持三个更强断言：

1. 作者把该取舍称为“非现实”；
2. 任何路线都会导致悖论；
3. 社区在不知情或未披露的状态下使用了某条路线。

Book 自己给出无需 LEM 或 resizing 的 initial σ-frame 路线，因而“必须接受 LEM 或 resizing”的反向命题已经被原书的选项结构排除。

## 2. SingleOmega、B1a 和必要性的实际状态

`SingleOmega` 是本项目为一个低层命题分类结构引入的形式化名称，并非 Book 的“非现实元素”术语。现有 B1a 证明的是条件充分性：给定 `SingleOmega`，可构造项目定义的 `ℝLayerAt` 代理。它没有证明 `ℝLayerAt → SingleOmega`，更没有证明某种原则“必付费”、所有实数使用都依赖它、或这构成 HoTT 的缺陷。

该反向 `Necessity` 在现有 claim package 中被明确标作 `CONJECTURE`。因此，把“给出支付条件后可以完成构造”改说成“理论必须以非现实元素完成构造”，是从充分性跳到了未证必要性。

## 3. LEM∞ 与 LEM 不能混为一谈

Book 在 univalence 下否定的是对**所有类型**的朴素原则

```text
∀ A : U, A + ¬A
```

即项目中写作 LEM∞ 的版本。它随后定义仅作用于 mere propositions 的 LEM，并明确说明后者可以一致地作为公理假定。故“Book 发现 LEM∞ 不相容”说明的是一个坏的全类型提升被理论排除；它不能作为“HoTT 已采用 LEM∞ 这种非现实元素”的证据。

## 4. Cubical 与 Huber 的精确意义

普通类型理论中把 univalence 单纯作为不可计算公理加入，确实会产生关于闭项规范化的技术问题。Cubical type theory 的研究方向正是给 univalence 提供计算规则。Huber 的论文证明一个 cubical type theory 的 canonicity：在规定的 name-variable context 中自然数项判断等于某个 numeral。

这不是“社区承认非现实性后把它修好”的证据；它也不是所有 cubical 系统、所有扩展或所有外部应用的完备安全证明。它说明原先 AI 的说法“Huber 证明 cubical 的 univalence 破坏 canonicity”方向颠倒了：Huber 的该论文证明的是一个 cubical 演算的 canonicity。

## 5. 对 GLM 最后几轮与 ABX 的结论

原始 ZCode raw trajectory 中，GLM 后段实际报告过 agda-unimath 保留宇宙层级、使用命题截断的“卫生”负结果；这不是圆环陷阱已被发现，反而是一个在固定语料内没有命中的控制。它还把 Book surreal 的大小/小索引讨论解释为“共同体书面自证”，但该 Book 段直接讲的是 universe、严格正性和大小约束，不能单独推出“非现实”或“危机”。

因此，ABX 并非没有意义，但其有意义的版本已经比 GLM 的叙述更窄：

- 若用户要研究一个带来源、端点、闭图和操作合同的对象理论，ABX 可以把它定义为独立的 `R_origin` 任务，并研究何时可由 `U` 恢复；
- 若用户要指控 HoTT 的实际使用，需要一个外部、版本固定的 K 调用链，显示 H_top/U 被当作 Done_strong；
- 若没有这两者，继续 ABX 只能重复 Book 已知的技术取舍或产生新的表示边界，不能构成对 HoTT 的击落。

“理论抽象必然导致非现实性悖论”仍是一个哲学或元数学假说，不是本项目、Book、Agda 或 Huber 已经证明的定理。把技术取舍称为非现实，需要另行定义现实对应、被保留的任务、失败条件和可反驳观察。
