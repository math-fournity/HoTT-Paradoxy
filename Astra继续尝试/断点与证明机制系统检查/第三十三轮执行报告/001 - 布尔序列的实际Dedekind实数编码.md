<!-- governance-shard:v2
logical_id: ASTRA-WEAK-COVERAGE-MARKOV-33
shard_id: 001
index: ../第三十三轮执行报告.md
-->

# 布尔序列的实际Dedekind实数编码

C321为任意`f : ℕ → Bool`给出固定库`ℝ(lzero)`中的实际实数，随后证明其与“存在true下标”的关系。关键是先构造cut并核其条件，没有假设一个自带所需性质的编码实数。

## 1. 精确构造

令`w(n)=1/(n+1)`，取下cut：

~~~text
L_f(q) = (q < 0) ∨ ∃ n : ℕ, (f(n)=true ∧ q<w(n)).
~~~

这里∨和∃保持命题截断含义。`weightedWitness`的每个固定n条件可判定，因为布尔值与有理数严格比较均可判定；这没有给无限存在式一个全局判定器。

`BinaryWitnessWeights`证明权重严格正、反单调、首项为1、每项≤1，以及对任意正有理q可得到一个w(N)<q。`finiteSearch`对任意具逐点判定的谓词，只搜索`n<N`的有限前缀，返回具体有限见证或该前缀不存在见证的证明。

## 2. located性为何只需有限前缀

为了给`p<q`决定`L_f(p) ∨ ¬L_f(q)`：

1. 若p<0，直接有L_f(p)。
2. 若0≤p，则q>0。取得N使w(N)<q，在n<N中检查f(n)=true且p<w(n)。
3. 如果前缀命中，得到L_f(p)。
4. 如果前缀不命中，任一声称q<w(n)且f(n)=true的见证都会矛盾：n<N时由p<q得到被前缀排除的命中；N≤n时由w(n)≤w(N)<q排除q<w(n)。

因此得到¬L_f(q)，没有检查无限尾部的每一个布尔值，也没有使用Markov或可数选择取得一个未知下标。

下cut非空由所有负有理数给出；roundedness由有理中介数给出两个方向；1不在下cut中提供非空上界补集。固定库`real-lower-ℝ`从这些实际证明构造上cut及完整Dedekind实数`binaryWitnessReal f`。

## 3. 与见证、零和正性的关系

令`SomeTrue(f)=∃n,f(n)=true`，`x_f=binaryWitnessReal f`。正式检查的关系包括：

~~~text
0 ≤ x_f
SomeTrue(f) ↔ 0 < x_f
x_f = 0 ↔ ¬SomeTrue(f)
¬¬SomeTrue(f) → x_f ≠ 0
x_f apart 0 → SomeTrue(f)
~~~

正性与见证的转换直接读取零是否属于所构造下cut。apartness给出x_f<0或0<x_f；前一支由非负性排除，后一支给SomeTrue。输出仍是mere存在证明，不冒充已返回某个非截断下标。

两个实际控制为：全false序列的实数等于零；全true序列的实数严格正。它们连同任意f的定理一起过核，不把有限样本替代全称证明。

## 4. 范围

没有证明对任意f可以决定x_f=0或x_f>0，没有给任意无限搜索一个无条件终止算法。实数构造没有新增LEM/Markov/choice公设，库继承的基础公设与no-erasure配置仍保持其明确边界。本文不把cut形成当作物理无限过程已经执行。
