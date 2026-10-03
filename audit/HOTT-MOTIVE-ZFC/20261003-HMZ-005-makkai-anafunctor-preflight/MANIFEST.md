# HMZ-005：Makkai anafunctor 消费者预检

> **身份：** `SOURCE_PREFLIGHT / ACTUAL-CONSUMER-CONTROL / NOT_A_FULL_DENOMINATOR_RUN / ADMISSION_REJECTED_WITH_SCOPE`。

> **触发依据：** 第一阶段来源综合的 successor-admission 条件 1：寻找一个真实消费者，看它是否在同一 `Done` 下省略了 choice、marking、formation 或其它必要支付。本预检不把“Choice”“isomorphism”或“canonical”这些词直接提升为 ZFC 候选。

## 预检问题

Makkai 是否给出了一个集合论侧的真实消费者：它把“每对对象有某个积”无支付地提升为“有一个可用的普通 product functor”，从而形成同一任务的未付完成性，或者对应地给出一个明确的支付／换任务控制？

## 冻结来源

| ID | 身份 | 原件与版本 | 已读范围 | 存档完整性 |
|---|---|---|---|---|
| `HMZ-S-020` | M. Makkai, *Avoiding the Axiom of Choice in General Category Theory*, *Journal of Pure and Applied Algebra* 108(2), 1996, 109–173, DOI `10.1016/0022-4049(95)00029-1`；作者主页保留的 7 段 PostScript 预印本。 | 作者目录 <http://www.math.mcgill.ca/makkai/anafun/>；取得日 2026-10-03。`originals/` 保留七段 `.ps.gz`；`derived/` 保留由这些原件重建的 91 页 PDF 和全文文本。 | 导言 pp. 1–5；product-anafunctor 例子 p. 10；弱 Choice 讨论 pp. 79–81；并对完整派生文本作关键词定位。 | 7/7 原始分段、重建 PDF、派生文本及哈希都在本目录。 |

这是一份**消费者预检**，没有重新开启 A–E 五类完整文献分母。它没有新 `R`：与 HoTT 创建动机的关系只通过既有的结构同一性／代表选择路线和 HMZ-001／002 的 controls 发生。

## 准入裁定

```text
P1 exact object / formation / consumer: PARTIAL — 有真实范畴论 consumer，
  但基础是无 AC 的 constructive Gödel–Bernays class-set theory，不是 ZFC 的同层对象语言。
P2 formation / reentry: NOT SUPPLIED — 所有 product diagrams 已给出；没有待形成对象回入自身形成。
P3 pending admission / unpaid Done: REJECTED — 普通 product functor 所需的 simultaneous choice 被原文明确写出；
  anafunctor 是不同的交付接口，不是同一 Done 的无成本实现。
H0→Z0: NOT FORMED — 这里的“up to isomorphism”不保持 HoTT 高阶相同的 subject/process/observation/Done。
SUCCESSOR RUN: ADMISSION_REJECTED_WITH_SCOPE.
```

详细来源卡、控制和可重开条件见 [SOURCE-CATALOG](SOURCE-CATALOG.md)、[CONSUMER-CONTROLS](CONSUMER-CONTROLS.md)、[COVERAGE](COVERAGE.md) 与 [FINDINGS](FINDINGS.md)。
