<!-- governance-shard:v2
logical_id: ASTRA-BREAKPOINT-EXECUTION-7
shard_id: 004
index: ../第七轮执行报告.md
-->

# Agda与Lean的命题对照

本片回应用户对“四弹Agda发现”与本轮Lean曲线构造是否冲突的追问。方法为原始类型/递推/操作合同对照、三份旧Agda命令实际重放，以及在Lean中按原M1递推证明同一算术结论并与曲线命题合取。证据等级分别为原证书重放、精确源码审查和C-274的新机器命题；不是一般跨内核保真或一致性证明。

用户本轮原话：

> 难道这没有什么问题吗？这和我们曾经在Agda那边在四弹一体击落HoTT工程中的发现难道不冲突吗？Lean为什么直接通过了？为什么那个时候Agda不给通过呢？

## 1. 最先纠正“不给通过”的对象

四弹M1/M2/M3-UNC的当前源码包含的是**被Agda接受的否定证明**。不是Agda曾收到本次F的同一声明后拒绝了它。本轮没有把完整F和相同的实数拓扑/公理合同移植到原生Agda，所以不能声称“同题Agda拒绝而Lean接受”。

“Agda拒签”是历史叙事；其实际数学对象必须回到代码。当前重放M1和M3-UNC均通过，后者消费M2。第三个EndpointMaps控制也通过。三份输出与原收据均`EXACT_EXIT_STDOUT_STDERR_MATCH`，见`audit/astra-endpoint-closure-20260920/agda-comparison/REPLAY.json`及逐run原输出。

## 2. 四弹主链实际检查什么

| 项 | 原精确类型/定义 | 与当前F的区别 |
|---|---|---|
| M1 | 初值(p,q)=(1,1)，递推(p+2q,p+q)，整数D(n)=p²−2q²恒为±1，因此∀n:ℕ,D(n)≠0 | D是这条离散递推的整数判别式；源码未把它定义为当前平面端点距离，也未给同任务保持翻译 |
| M2 | `¬ Σ q:ℚ, q·q=2` | 不存在满足该规格的有理数，与存在实际实数曲线F是不同目标；F没有交付该q |
| M3-UNC | `Spec_A`是判定`q²<2`的布尔比较表，`Spec_B=Σq:ℚ,q²=2`，证明`¬(Spec_A≃Spec_B)` | 没有在M/N上定义本次曲线过程、边界图或可达性；把表与有理根规格称为同任务还需要桥梁 |
| REAL-LAYER | 当前代码证明`SingleOmega ℓ → ℝLayerAt ℓ`的充分性，必要方向只定义命题 | 涉及特定宇宙层级的实数表示，不是“任何实数连续曲线都不存在/不能到达”的证明 |

代码锚点：`HoTT/formal/dedekind-omega-missile/MissileOneProcessLayer.agda`的pellP/pellQ/D/gap-never-zero；`MissileTwoUniversalIrrationality.agda`的noRootℚ/spec-B-empty；`MissileThreeVerdictCollision.agda`的Spec_A/Spec_B；`MissileThreeUnconditional.agda`的M3-L1-unc；`CutRealLayer.agda`的Sufficiency/Necessity/sufficiency。

其中M1的“gap”命名不能替代几何距离定义，M3的“同一任务”注释不能替代输入、操作、观察和Done的保持证明。本轮对REAL-LAYER只作类型定位，没有把它计入三份新增重放分母。

## 3. 已做同一算术结论的Lean对照

`HoTT/formal/astra-real-geometry/PellCurveComparison.lean`按相同初值和递推定义`pellPair`；不改变D=p²−2q²的含义。C-274正式证明：

~~~text
∀n, D(n)=1 ∨ D(n)=−1
∀n, D(n)≠0
(∀n, D(n)≠0) ∧ (∃F, 联合连续 ∧ 逐时嵌入 ∧ 初像N ∧ 末像M)
~~~

最后的合取调用已经验证的C-269，实际过Lean核，run=`20260920-MP-ASTRA-PELL-CURVE-COMPARISON-001-01`。Pell部分公理输出仅propext；合取再出现实数几何使用的Classical.choice/Quot.sound。源码、运行、索引与关系检查由`lean-comparison/DELIVERY.json`持有。

因此本轮有直接证据表明：Lean没有把旧Pell不变量改判为“可为零”；它同时接受旧算术否定与新曲线存在。这个同题对照只覆盖上述递推，不冒充所有Agda/Lean语义相同或两内核元层一致性证明。

## 4. 若用户指后来圆环侧的Agda控制

`EndpointMaps.agda`的Reach只允许内部Bool坐标变化、两个边界坐标保持；其relativeNonreach是该受限语法的结论。同文件还给出扩充构造操作后的extendedReachable。当前F允许边界像移动，且闭参数末态非单射；它没有满足原控制中全边界等价/单射的前提。Lean自身的C-267/C-273也分别给出环境不可达和闭域末态非单射。

`PathExclusion.agda`和`HomotopyRestorationControl.agda`则使用HIT S¹上的`Σx, ¬(x≡base)`内部路径排除，代码明确区别于点集圆删去一个坐标点。它们没有成为本次实数几何的保真翻译，不能把其noSplit解释为本次F不存在。本段是当前源码对照，未另计这两包重放。

## 5. Lean究竟为什么通过，以及仍须审查什么

Lean检查的是明确连续函数、嵌入、初末像和所用公理下的证明项。它没有检查“所有原现实条件均保持”。本次采用经典实数点集几何、闭实数时间、开曲线参数及允许端部移动的合同；原生Agda完整版F尚未重放，构造性/公理差异也不能据此宣布无影响。

主要差异不能仅用“ℚ换成ℝ”概括：同时改变的还有递推/曲线对象、离散n/连续t、整数判别式/几何距离、输出一个有理根/交付一条连续族，以及固定端部/允许端部移动。哪项改变符合原用户任务，仍须逐项审查。

对上一答复应补足的范围是：**“同一个M/N”目前只指同一个底层几何点集，尚未认证同一完整现实任务。N→M已在所声明的允许端部移动模型中完成；没有证明它保持用户原任务的全部固定端部、环境或构造来源条件。** 若把这个新模型当成原固定端部任务的完整解答，就发生了任务替换；当前正构造不能升级为该任务的完整正恢复。这个范围修正与四弹现有定理继续有效可以同时保留。

下一任务仍为真实Rich/Bare/Forget与结构消费者；本轮质疑促成同题对照和更清楚的范围说明，不改变父Goal，也不以新Pell控制替代主几何与HoTT连接。
