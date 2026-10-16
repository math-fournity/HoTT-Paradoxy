<!-- governance-shard:v2
logical_id: ASTRA-MARKOV-REVERSE-34
shard_id: 001
index: ../第三十四轮执行报告.md
-->

# 具体有理界序列上的Markov恢复

C323首先研究一个明确丰富了输入的任务：给定x:原ℝ(lzero)，以及每个自然数n处的具体有理上下界。没有先假定任意Dedekind输入已经携带这份数据。

## 1. 实际输入与测试

`RationalBoundSequence x`逐n返回有理p_n、q_n，及：p_n属于x的下cut、q_n属于上cut、q_n<p_n+1/(n+1)。严格写成p_n<x<q_n只是这些cut成员的简写。

`hitBool n`实际比较两个有理条件：`0<p_n`或`q_n<0`。比较使用原有理数判定，得到布尔值及其与条件的正确性关系；没有要求判定任意实数的零性。

正式证明：

~~~text
x apart 0  ↔  ∃ n, hitBool(n)=true
x ≠ 0     →  ¬¬(∃ n, hitBool(n)=true)
BookMarkov → x ≠ 0 → x apart 0       （给定上述界序列）
~~~

存在保持命题截断。Bool测试是具体函数，未用“存在一个能检测apartness的程序”代替实现。

## 2. 两个方向怎样成立

若某下界严格正，cut向下封闭性给0<x；若某上界严格负，给x<0。因此每次命中都有真实apartness证据。

反向，若0<x，从严格实数序关系得到一个正有理r<x，选n使1/(n+1)<r。足够窄的p_n、q_n夹住x，迫使p_n>0。若x<0，选择负有理上界及相称精度，迫使q_n<0。两支都得到实际测试的mere命中。

若x≠0而假设没有命中，由上述apartness→命中方向得到¬apart；固定库的tightness给x=0，与非零前提冲突。这产生双重否定。仅在随后一步使用传入的BookMarkov，取得正面的命中存在证明，再返回apartness。

## 3. 输入类确有实例

`rationalCloseBounds`为每个有理数q和正精度ε直接构造q−d、q+d，选择2d<ε并证明cut与宽度条件。由此得到每个有理实数的整列界，未使用可数选择。

`zeroNoDetection`证明零实例没有命中；`oneDetection`证明一实例有命中。它们是实际有理数的控制，避免把给定数据的任务仅留为没有实例的接口。

## 4. 截断与完成边界

如果只给整列界数据的mere存在，仍可用`markovWithMereBoundsGivesApartness`：整个输出apartness是命题，故可以合法地把该截断消去到这个目标。这里没有一般地从∥数据∥返回数据本身。

当前结果不提供BookMarkov实例，不证明无限搜索对所有输入终止，也不证明任意裸Dedekind实数无条件带有整列界。逻辑上有恢复构造与一个物理过程已经执行完成，仍是不同证据等级。
