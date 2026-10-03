# HMZ-003：存在、命名与可交付的有界判词

## 1. 真正找到的接口

原始 ZF 公理可以只断言存在；实际 Isabelle/ZF 使用为了可写、可推理、可复用而把对象以 constants、syntax
translations、single-valuedness、unique-description premises 和 derived rules 显式交付给使用者。`Inf` 的非唯一性
尤其清楚地显示：系统不是声称“从存在命题算出了唯一对象”，而是在理论签名中公开选择一个受公理约束的常量。

这是一条与 `R-CONSTRUCT` / `R-MACHINE` 有关的真实来源界面，但它的当前身份是：

```text
EXPLICIT_FORMATION_PAYMENT
≠ unformed object used secretly
≠ P2/P3 reentry
≠ ZFC Q
```

## 2. 为什么不能把非有效性直接写成理论失败

Grayson 将归约计算与不带有效决定方法的 axiom 分开；Rijke/Spitters 将 type discipline 和 proof-assistant
computation描述为实践优势。它们均没有推出“每一条非有效 ZFC 公理造成非法构造”。反过来，HoTT Library 也明确
报告 univalence/function extensionality 的 axiom 使用会在某些证明中阻断 computation。于是机器可用性是一条
带具体实现条件的设计轴，不是单向评判 ZFC 的捷径。

## 3. 对模式 P 的结果

本轮最接近 P 的对象是 `Inf`，但完整卡片显示：

- 理论对象、axiom 和 consumer 都可定位；
- formation/payment 是显式的常量加约束；
- 没有对 `Inf` 合法性的同对象再入；
- 没有 pending-admission、negative bridge 或无限完成追问；
- 把任务改成“从任意存在证明计算出规范 Inf”会改变输入与 Done。

所以它是一个有价值的 **P 反控制**：它说明未来若发现 ZFC 的存在—使用张力，必须比“存在性被名字化”更强。

## 4. 后续入口

新的 successor 只能由以下来源触发：

1. 真实 ZFC consumer 在同一 Done 下省略了已经需要的 witness/formation payment；
2. 一个系统内 universal evaluator/choice operation 将对象形成与其自身合法性追问交错；
3. 一手文献将 Power Set、Replacement 或 class formation 与这类同一任务明确连接；
4. 已有 H0 在 ZFC 中找到 T0–T5 保真的正向对象。

本 run 未发现任何一项，因此不创建 P-DAG NodeCard，也不改写 Power Set station。
