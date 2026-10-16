<!-- governance-shard:v2
logical_id: ASTRA-WEAK-COVERAGE-MARKOV-33
shard_id: 002
index: ../第三十三轮执行报告.md
-->

# 从原Weak覆盖到Markov的精确连接

C322把C321构造的具体实数接到已经形式化的原圆周和原最终图。研究对象、点、域和返回值沿既有定义保持；没有把“所有Weak点被覆盖”换成另一个容易证明的抽象接口。

## 1. 两端的原类型

`RealNonzeroApartness`（RNZA）为：对任意固定基线实数r，r≠0推出r apart 0。`BookMarkov`保持原典的二元形式：对任意f:ℕ→Bool，从¬¬(∃n,f(n)=true)推出∃n,f(n)=true。

`WeakFinalCoverage`仍是C319的原类型：对于原Weak去点圆中的每个点w，mere存在原开区间参数u，使**同一个**`motion(1,u)`等于w的平面点。它不是任意存在一个同胚，也不是改变目标点后的覆盖。

## 2. 新前向证明

给定RNZA与任意f、¬¬SomeTrue(f)：

1. C321构造x_f，并从双重否定得到x_f≠0。
2. 对这一个实际x_f使用RNZA，取得x_f apart 0。
3. C321的`apartWitnessGivesSomeTrue`给出SomeTrue(f)。

这个组合形成`realApartnessImpliesBookMarkov`，没有将Markov作为证明参数再次输入。

## 3. 与原几何结果组合

现有C307–310、C319的已核连接与本轮C322组合后，得到：

~~~text
固定WeakFinalCoverage → Circle Lift → RNZA → BookMarkov
RealPairApartness → RNZA → BookMarkov
UniformRealInverse → RNZA → BookMarkov
~~~

另用旧`bookToLibrary`把最后输出翻译为固定库的`Markov's-Principle`。零点原则与任意实数对原则、同点Lift及统一逆元之间的既有等价不重新计作本轮突破；本轮新增的是实际布尔cut到原则的前向连接及其原图实例。

`¬BookMarkov → ¬WeakFinalCoverage`也已按显式条件写出。源码没有提供¬BookMarkov，因此这不是无条件否定Weak覆盖的证明。

## 4. 人话解释

“不等于缺点”只给否定相等的证据。当前原图要完整处理所有这样给出的点，其能力足以作用于任意布尔序列编码出的圆周点，并把一类双重否定存在命题变成正面的存在证明。这给了该接口一个精确的逻辑后果。

这个后果比泛称“引擎拒签”“实数收费”更可检查：可以点开同一圆周、同一最终图、实际实数编码和逐步蕴含。但它本身不说明该接口在当前基线不可得，也不说明HoTT曾无条件许诺它；这两项还须分别证明或定位。
