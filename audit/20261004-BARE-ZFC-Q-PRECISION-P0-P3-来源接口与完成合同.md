# bare ZFC 的 Q 理论精度：P0／P1／P3 来源接口与完成合同

> **身份：** F049_SOURCE_INTERFACE_CARD / BARE_LANGUAGE_AND_APPLICATION_CONTRACT / NOT_A_BARE_ZFC_INCONSISTENCY。
>
> **执行方案：** [BARE-ZFC-Q-PRECISION-SOP](../dev-docs/BareZFC理论精度Q形式化SOP.md) 的 P0、P1、P3。
>
> **来源分母：** SEP *Set Theory*、IEP *Zeno’s Paradoxes*、John D. Norton *Zeno’s Paradoxes of Motion*；冻结读取日期为 2026-10-04。

## 1. 这张卡冻结什么，不冻结什么

研究发起人要检验的不是“ZFC 能否给时间取一个集合编码”。SEP 明确把 ZFC 描述为仅有 equality 和 membership 的一阶公理系统，同时说明数学对象、关系与函数能够被当作集合表示；这使“没有时间 primitive，因此 ZFC 完全不能表达步骤或程序”的推断不成立。[SEP：*Set Theory*](https://plato.stanford.edu/entries/set-theory/index.html) 的语言说明在 §2，表示能力说明在 §5。

当前要冻结的是一个更窄、可以真正审计的接口问题：

    bare ZFC language / set representation
        + a source that deploys ZFC-supported real analysis as a Zeno resolution
        + a process contract that says which completion was used
        -> does that application interface itself retain OriginDone or pay a bridge?

这张卡不把上面三层合并成“bare ZFC 已作出一个物理完成判词”。它只检查一份来源所声明的基础性应用是否在声明解答时保留了原过程的 completion contract。

## 2. P0：语言／基础位置

| ID | 一手来源事实 | 可用含义 | 不能推出 |
|---|---|---|---|
| SEP-SET-20261004-LANG | ZFC 是具有 equality 和唯一非逻辑二元 relation symbol ∈ 的一阶公理系统。 | 这固定了 bare ZFC 的语言层。 | 没有时间 primitive 即不能编码时间、轨迹或计算。 |
| SEP-SET-20261004-FOUNDATION | 数学对象可被看作集合，数学陈述可在集合论语言中形式化；这正是其作为数学基础的意义。 | 过程、数列和 relations 可以由额外集合数据表示。 | 任意 set representation 自动保留来源、操作、观察或完成条件。 |
| IEP-ZENO-20261004-APPLICATION | IEP 把带 Choice 的 ZF、标准实分析与 Standard Solution 放进“间接解决芝诺”的基础语境。 | 存在一个可考察的 ZFC-supported standard-solution application。 | 这是 bare ZFC 的对象语言关于物理运动的定理。 |

**P0 判词：**

    P0_LANGUAGE_FIXED
    P0_SEMANTIC_BARE_ZFC_COMPLETION_INTERFACE = SOURCE_UNDERDETERMINED_WITH_SCOPE

bare ZFC 的语言和基础位置已经固定；“bare ZFC 原生完成接口”没有被任何来源定义。这个负结果不是普通的“没有搜到”，而是由语义层的区分得出：语言／表示能力与来源中实际承担原过程完成判词的 interface 不是同一个对象。

## 3. P1：过程合同与 application-level C/I/O/Done

IEP 把 Standard Solution 描述为使用标准实分析和 calculus 的解答路线，并指出抽象连续性是否真正描述时间、空间与具体物理现实仍受争论。[IEP：*Zeno’s Paradoxes*](https://iep.utm.edu/zenos-paradoxes/) 同时给出了“基础支持”与“现实适切性另需审查”两层。

Norton 将这个过程合同写得更直接：

- 完成无限 actions 的严格读法包含“做完全部 actions，包括最后／第一 action”；
- 对没有最后／第一 action 的无限序列，改用“做完全部 actions”的 revised reading；
- 删除那项要求后，原来的矛盾不再推出。

该文本直接区分 completion 读法，而不是把它们当作同一个谓词。[Norton：*Zeno’s Paradoxes of Motion*](https://sites.pitt.edu/~jdnorton/teaching/paradox/chapters/Zeno/Zeno.html)

| P1 字段 | 冻结值 | 来源等级 |
|---|---|---|
| T_application | ZFC-with-Choice-supported standard real analysis / calculus | SOURCE_ESTABLISHED |
| u | Norton 的无限正向或反向编号 action sequence | SOURCE_ESTABLISHED |
| FormalDone | revised completion：每一个可编号 action 都完成，不要求不存在的 first／last action | SOURCE_ESTABLISHED |
| OriginDone | 当前严格控制：原任务包含 first／last action 条件 | SOURCE_ESTABLISHED_AS_NORTON_STRICT_READING |
| C | IEP 的 standard-solution application / resolution policy | SOURCE_APPLICATION_OWNER_ONLY |
| Bridge | FormalDone -> OriginDone | SOURCE_UNPAID；Norton 明说删去 strict 条件而非证明它 |

**P1 判词：**

    P1_APPLICATION_CONTRACT_FIXED_WITH_SCOPE
    P1_BARE_ZFC_CONSUMER = NOT_ESTABLISHED

这里有一个实际的 application-level source owner，但没有一个“bare ZFC 自己消费并断言 OriginDone”的 source-defined consumer。

## 4. P3：合同改写、bridge 与归因

Norton 的文字是此卡最强的 P3 证据。它不是从无穷级数的形式结果偷偷推导严格 completion，而是将 strict condition 叫作在无限情形不适用，并建议删除它。于是：

    P3_EXPLICIT_TASK_SWITCH
    FormalDone -> OriginDone = NOT_PAID_BY_THIS_SOURCE

这支持一项精确的应用层审计要求：**若一个 source owner 用 FormalDone 交付“原过程已解决”，它必须给出 bridge 的域、保持方式或明确说明 task 已变。**它不支持把这个要求直接归为 bare ZFC 中的一条被违反的公理。

## 5. H095 独立来源映射与运行边界

[H095 NodeCard](20261004-P-DAG-SOURCE-095-BARE-ZFC-Q-PRECISION-NODECARD.md) 把上述三份来源及有限逻辑控制封进只读 source-match payload。隔离 App Server 的公开终态满足：

| 项 | 结果 |
|---|---|
| 模型／推理 | gpt-5.6-terra / max |
| 输入预检 | PASS；项目路径、旧答案和 P-DAG skill 名称不在模型输入中，冻结 source card 在输入中 |
| 运行权限 | readOnly、networkAccess=false、approvalPolicy=never |
| 行为 | 正常终态；0 command、0 file change、0 approval request |
| 公开输出 | E0–E7 完整，776 words，SHA-256 d0665ad1486dcb5c8a9c6a387207f7c4b214eab1dba8196233cdbc3adea9743d |
| trajectory | 私有双向 App Server wire 记录 1302 个 events。raw reader 确认 0 tool calls/results；direct wire 没有完整 AGENTS 正文，故 L1 为 NOT_FULLY_CERTIFIED，不把运行结果冒充为完整 context injection 证据。 |

worker 的公开 MatchTrace 与 Master 的直接来源复核一致，给出的 scoped verdict 是：

    P0_LANGUAGE_FIXED
    P1_APPLICATION_CONTRACT_FIXED
    P3_EXPLICIT_TASK_SWITCH
    SOURCE_APPLICATION_OWNER_ONLY
    SOURCE_INTERFACE_UNDERDETERMINED

运行细节与不确定性见 [H095 运行与 MatchTrace 报告](20261004-P-DAG-SOURCE-095-BARE-ZFC-Q-PRECISION-Terra-Max.md)。私有 wire、认证和 prompt-input 收据不进入 Git。

## 6. 对 M2／M3 的允许归因

后续 Lean package 可构造一个有限 CompletionWorld control：

    same coarse StandardResolutionView
    different OriginDone
    => the coarse view cannot decode OriginDone

它必须使用下面的名字：

    INTERFACE_RELATIVE_FORMAL_CONTROL
    SOURCE_BOUND_APPLICATION_VIEW

它不得使用下面的名字：

    bare-ZFC semantic interface theorem
    ZFC cannot encode time theorem
    ZFC inconsistency theorem

富接口／显式 process code 的正控制是必须项，因为 SEP 的 representation 事实正好要求我们不能将“某个 coarse application view 忽略 contract”误说成“ZFC 无法表达 contract”。

## 7. P0–P3 总结与停止条件

| 层 | 当前结论 | 对 F-049 的影响 |
|---|---|---|
| P0 | language 固定；bare semantic completion interface 未由来源定义 | 禁止将任何自造 projection 归因给 ZFC 本身 |
| P1 | application contract 固定 | 允许针对该 application view 作 interface-relative 形式化 |
| P2 | 由 C-364 的同投影／异 OriginDone 机器 control 检验 | 只能是模型控制，不替代来源 owner |
| P3 | Norton 明示 task switch；strict bridge 未支付 | 支持 completion-bridge obligation，不支持 bare-ZFC defect verdict |

若找到一份版本固定的基础来源，将 bare-ZFC formal acceptance 自身提升为原过程／物理任务的充分完成判词，并且拒绝或遗漏上述 bridge，它才会改变 SOURCE_INTERFACE_UNDERDETERMINED。当前来源分母已经足以完成本轮的 P0/P1/P3，不允许用不断追加相似来源把这个 scoped result 误写成全域结果。
