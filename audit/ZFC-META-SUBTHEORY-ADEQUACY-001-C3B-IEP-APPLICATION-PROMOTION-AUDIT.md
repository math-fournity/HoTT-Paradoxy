# C3B：IEP Standard Solution 的 actual application promotion P

> **身份：** `C3_SOURCE_PROMOTION_CARD / PHYSICAL_APPLICATION_PRESENT / BRIDGE_NOT_YET_PAID`。
>
> **TaskCard：** [C3B](ZFC-META-SUBTHEORY-ADEQUACY-001-C3B-TASKCARD.md)。
>
> **判词：** `P_STANDARD_APPLICATION_SOURCE_PRESENT / P_MIZAR_CONSUMER_NOT_CLAIMED / P_STRICT_ORIGINAL_NOT_ESTABLISHED / C3B_LOCAL_LEAF_CLOSED`。

## 1. IEP 实际说了什么

当前 IEP 条目不是只罗列一个级数公式。它把 Standard Solution 描述为：

- runner path 是 physical continuum；以正而有限的速度完成；
- time/space以实数型连续统和 position function / derivative style speed 描述；
- standard real analysis、calculus、classical mechanics被用来应对 motion paradoxes；
- 多数观点把含 Choice 的 ZF 视作该分析的基础，并把这一路线称为对芝诺的间接解答。

因此，存在一份真实的 **application-level P**：标准数学模型被用于说明 physical runner/path 的完成。它不能降格为“IEP只证明一个级数恒等式”。

## 2. P 的三层分解

| promotion | 来源是否实际给出 | 范围 |
|---|---|---|
| `P_model`：continuous-mathematical model 的 endpoint/limit result | `SOURCE_SUPPORTED`。 | `Q_model`；C2B的 MML trajectory仅作为 formal proxy。 |
| `P_physical`：Standard Solution 对 physical runner/course 的 resolution language | `SOURCE_SUPPORTED_AS_APPLICATION_CLAIM`。 | IEP 的 specific Standard Solution，含其选取的 continuum/calculus/physical assumptions。 |
| `P_Mizar`：`SERIES_1` 或 MML theorem 被 IEP 实际消费并推出 physical completion | `NOT_CLAIMED`。 | IEP没有引用 Mizar；MML不是该历史文本的 consumer。 |
| `P_strict_original`：model result保留/证明“含最后动作”的 strict completion | `NOT_ESTABLISHED`; Norton control的相反 reading为显式 task revision。 | 不得从 IEP 的 “resolution” 自动给出。 |

这一区分很关键：C1A–C2B 的 MML assets可作为版本固定的 **source-to-spec formal proxy**，但不能伪造成 IEP 对某个 proof assistant的历史引用。真正可审计的 target是：IEP 的 standard real-analysis model对 physical Q 提出的 application claim。

## 3. 固定到 C4 的 Q/P 字段

```text
Q_physical
  input       = a runner/course modeled on a real-continuum path
  operation   = run along that path at finite positive speed
  observation = time-indexed position / reaching goal
  done        = course/path completed in the Standard-Solution model

FormalDone_model
  = continuous real-parameterized mathematical trajectory reaches endpoint,
    with standard analysis/calculus conditions

P_standard
  = IEP’s use of the Standard Solution as an indirect resolution/application
    to Q_physical.
```

这些字段足以释放 **C4 bridge audit**；它们还没有把 `OriginDone` 固定为 Norton 的 strict last-action reading。Norton因而是一个 `DifferentTaskControl`，不是对 IEP每一句话的替代解释。

## 4. 已知 bridge 边界

IEP显示它知道模型到物理应用存在争议：其第 98 行说 abstract account of continuity是否真正描述 time/space/concrete reality仍受挑战；第 100–104 行又说明历时修订 continuum定义和 series/motion概念。故 `P_standard` 的存在不自动等于一个已展示的 bridge。

本卡的精确结果是：

```text
P_standard exists as an application-level claim.
Whether P_standard has paid all of
  representation / operation / observation / completion bridge
remains C4, not an inference from the word "solution".
```

它既不能宣布 failure，也不能以“IEP承认争议”宣布 defense。两种结论都需要具体 bridge card和adequacy contract。
