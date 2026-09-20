<!-- governance-shard:v2
logical_id: ASTRA-GOLD-CUT-17
shard_id: 002
index: ../第十七轮执行报告.md
-->

# 实际GOLD装配与精确查询恢复

C-298/C-299直接消费原CutGoldForm的Lₚ/Uₚ、inhabL/inhabU、disjoint、rounded双向及located，未换谓词。导入的旧源码哈希仍与先前主收据一致。

## 1. 完整装配

~~~text
goldStd        : dcutStd G.Lₚ G.Uₚ
goldBook       : dcutBook G.Lₚ G.Uₚ
goldLegacy     : CutRealLayer.dcut G.Lₚ G.Uₚ
goldReal       : StandardReals 0
goldLegacyReal : CutRealLayer.DedekindReals 0
~~~

前两份实数载体元素实际在Type1；其L/U投影与原谓词是refl。声明和证明体都没有LEM、resizing或SingleOmega输入，标准装配并不调用旧sufficiency的付费前提。

这关闭了“GOLD只是几个分散字段，尚未进入标准载体”的具体装配缺口。没有在此新增实数环运算、环内x²=2或完备性定理；本包交付的是固定L/U的切割元素及其规格。

在1<2这一实际输入，L1与U2都成立，所以未截断的`L1⊎U2`有两个不同分支。`untruncatedLocatedValueNotProp`证明这个输出类型不是Prop。这说明携带分支数据的强locatedness与标准截断locatedness需要区分；它不证明整个强结构不可能，也不否定GOLD提供这种额外数据的合法性。

## 2. 精确查询及负三对照

`classify`对每个有理q产生真实Lq或Uq，使用有理符号、平方比较及旧M2无理性排除等号支。`lowerQuery/upperQuery`返回Dec，并通过goldReal的实际投影提供`packedLowerQuery/packedUpperQuery`。

机器还检查了闭项归约：

~~~text
GOLD lower-query tag (-3) = true
actual old M3 square table (-3) = false
~~~

旧表判断q²<2，GOLD下切割还包含所有负有理数。这个反例证明旧表不能保持相同q与真假含义而原样改名为完整下切割表。

这里没有宣称“两个正确查询规格的类型本身不等价”。比较的是相同输入下的谓词含义和答案，类型等价与保持查询语义的转换仍需分开。

## 3. 最强恢复进入同包

`squareFromTable`直接消费旧Spec_A的实际(f,正确性表)，得到平方条件的Dec。`lowerViaTable`再加入有理数符号判断，产生正确Lq的Dec；`recoveryAgrees`对任意正确旧Spec_A与任意q证明它等于直接lowerQuery。实际旧表在−3经恢复后归约为true。

因此，旧表的不同不意味着无法转换。本轮明确给出了转换及同输入正确性，不能只报道负三差异，把已有恢复隐去。

## 4. 不同完成任务

| 任务 | 当前证据 |
|---|---|
| SQ-REP：交付这份标准切割 | C298实际元素与规格，已构造 |
| SQ-QUERY：每个q的L/U精确判断 | C299实际Dec函数、正确性类型和闭项控制，已构造 |
| SQ-RATIONAL-ROOT：交付q:ℚ及q²=2 | 本包调用原M2给出空性，不能交付此类输出 |
| SQ-APPROX(n)：给定精度交付有理夹逼与宽度证明 | 下一单元，尚未完成全精度证明 |

不能因为精确有理根任务为空，就断言其余任务都无法完成；也不能用切割表示完成替代任意物理过程或一次算完无穷多个查询。
