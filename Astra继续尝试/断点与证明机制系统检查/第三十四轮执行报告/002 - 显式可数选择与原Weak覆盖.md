<!-- governance-shard:v2
logical_id: ASTRA-MARKOV-REVERSE-34
shard_id: 002
index: ../第三十四轮执行报告.md
-->

# 显式可数选择与原Weak覆盖

C324把所需数据的供给单独证明并暴露假设，然后接回原圆周和原最终映射。所有结论都在固定ℝ(lzero)与原Weak类型上，没有移动目标点或改为另一个参数化。

## 1. 三层信息逐项对照

| 输入层 | 精确含义 | 本轮证据 |
|---|---|---|
| 具体整列 | `(n:ℕ) → BoundAt x n` | C323直接消费；有理数有实际实例 |
| 整列mere存在 | `∥(n:ℕ) → BoundAt x n∥` | 足以消去到apartness命题 |
| 逐精度mere存在 | `(n:ℕ) → ∥BoundAt x n∥` | 原库`is-arithmetically-located-ℝ`直接提供 |

不能把第三行直接读成第一行。`boundAtSet`证明每个BoundAt是小集合；`countableChoiceGivesMereBounds`把显式`ac : level-ACℕ lzero`应用于这个具体自然数索引的集合族，得到第二行。

这不是一个对所有任意类型返回选定元素的全局算子；它是固定库的集合族、截断选择形式。本轮没有给ac填入一个postulate或原则实例。

## 2. 反向及条件等价

给定ac后，C323的恢复可逐实数使用，得到：

~~~text
ac : level-ACℕ lzero
----------------------------------------
RNZA ↔ BookMarkov
原固定WeakFinalCoverage ↔ BookMarkov
UniformRealInverse ↔ BookMarkov
~~~

前向复用C322；反向由实际界序列路线构成。`choiceMarkovGivesCircleLift`返回保持同一点的Strong证据；`choiceMarkovGivesWeakCoverage`返回原`motion(1,u)`覆盖同一点的mere存在；`choiceMarkovGivesChosenWeakOutput`进一步复用已核的原同胚返回指定参数和原图命中等式。

因而，这组显式假设下的恢复是同一个任务接口的条件正构造，不能写成“原接口在所有HoTT变体下不可能”。同时，条件构造的核接受不认证传入原则的全局实例或实际程序归约/物理执行。

## 3. 哪些必要性仍未证明

本证明使用ac，并不证明ac必需或最弱；没有证明去掉ac后Markov不能推出RNZA，也没有建立相称模型或基线独立性。此前的排中律充分路线仍有自己的精确范围，未被本轮删除。

不能把“有一组充分假设”改写为“HoTT必须支付这组假设”，更不能将它接回旧的“任何实数对象都要Ω塌缩”说法。这里处理的是弱否定信息与apartness及同点输出，不是普遍宇宙小型化必要性。
