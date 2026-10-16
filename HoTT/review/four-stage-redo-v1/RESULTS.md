# 可检查结果与未决义务

研究问题是：在声称同一个对象可以替换、复原或有效使用时，实际保持了哪些结构和操作能力？以下五个入口的源码保持原始字节，原证明编号和主run由生成manifest定位。本包重放不创造新的数学claim，也不改变任何定理的量词。

## 1. 同一几何对象对，两个操作合同

入口：`sources/HoTT/formal/agda-unimath/hott-z/NativeTaskIntegration.agda`；C320。

`RichCurve`包括开参数化、平面实现、整个闭参数图、连续性和内部一致性。`nRich`是指定开线段的闭图；`mRich`是指定Strong去点圆的闭图。不是只有名叫M/N的两个任意类型。

`CurveRun r s`要求闭时间×闭参数联合连续、开曲线与闭扩展相容、每个切片为开区间到实际像的同胚，且正向函数正是该曲线；整个初末闭图等于r/s，所有坐标绝对值≤256。`actualCurveRun`给出nRich→mRich的实际证明。

`Success(r,s)`使用有限条全平面同胚，每步保持完整闭参数图相容。对同一nRich/mRich，`noSuccessNtoM`排除该Success。`noCurveToAmbientAtActualPair`排除两种成功之间的转换函数；`noUniformCurveToAmbient`和`noCurveAmbientEquivalence`给统一及等价版本。`nontrivialAmbientControl`给nRich→swappedN的真实成功。

这两个结果对应不同操作谓词，不是同一P与¬P。曲线能变形也不等于带预设闭图的Rich对象相等：`samePairStillRichDistinct`保留其差别。

依赖`NativeMotionComplete`还给原固定最终图完整Weak覆盖↔Lift↔RealNonzeroApartness；给定Lift可以选定原参数。Strong使用apartness，Weak使用不相等。不能把条件Weak覆盖称无条件覆盖，也不能把原则等价刻画称相对整个基线独立或LEM必要。

几何合同没有给物理设备、速度、能量、有限测量或全部创造历史。后者仍需另外的任务对应证明。

## 2. 给定完整源时可以保结构重新表示

入口：`sources/HoTT/formal/agda-unimath/hott-z/NativeSourceContract.agda`；C295/296。

输入携带完整source RichCurve、targetCarrier及载体等价。`reexpressed`沿ua运输整份CurveData；`denotesReexpression`逐闭参数保持原图。`actualRun/actualCheckedOutput`实现mRich在开区间载体上的重新表示。

输出是运输后的结构，不是预先指定的普通nData。`plainNDoesNotDenote`、`actualOutputNotPlainN`及`bareCheckIsInsufficient`明确排除后一偷换。给定源的重新表示不是从被丢弃的来源数据中恢复源，也不是物理形变。

## 3. 同指GOLD并不意味着同一输出请求

入口：`sources/HoTT/formal/dedekind-omega-missile/Sqrt2TaskComparison.agda`；C302/303，依赖C297–301及原M1/M2/M3。

`Request/Output/Done/Response`列九类请求。`dispatch`对六类给成功项：标准GOLD表示、下/上cut查询、给定自然数阶段的近似、原平方比较表、给定表后的正确下cut回答；对有理精确根、指定二分端点相遇、Pell差归零三类给否定。

旧表判断`q²<2`，标准下cut还区分符号；q=-3是明确分离点。`oldAnswerFailsLowerDone`排除直接把旧回答当标准下cut回答；带符号信息的恢复有实际实现。查询结果为false不等于查询任务失败。

`tableResponseEquivOriginal/rootResponseEquivOriginal`把新请求连回原Spec_A/Spec_B，`responseRefusal`保留其不等价。原M3所证明的不是编译器拒绝检查，而是某个否定命题的证明被接受。

`smallnessIfProvided`保留SingleOmega→指定同层实数层的单向充分性，未补必要性。标准GOLD使用显式宇宙层级，没有把升一层伪称同层resizing。此包不证明所有实数任务都可判定、完整实数理论、任意ε收敛或圆环—算术全任务保真桥。

## 4. 原生S1证明机制与固定错误项控制

入口：`sources/HoTT/formal/astra-s1-consumer-check/SC00.agda`；C304。

SC00复用实际Cubical S1/base/loop、整数覆盖及encode/decode/winding的消费者链，检查与上游的对应、逆律及指定组合观察。不是拿点集去点圆冒充HIT圆，也不是由一个构造子数推出整个路径结构。

SC01–SC04为原已冻结的单因素错误项，分别缺Glue构造、loop边界、pred/suc对应或正确J证明。期望的是exit42及具体`UnequalTerms`诊断；重放同时核诊断，不把任意报错当成功。这四次拒绝只证明这四份项未被该检查器接受，不是四个全称不可能性定理。

## 5. 商与截断既丢弃某些信息，也保留合法观察

入口：`sources/HoTT/formal/astra-quotient-consumer/QuotientConsumer.agda`；C305/306。

同一有理数的1/1、2/2呈现有不同原分子；`noOriginalNumerator/noOriginalFraction`排除保存每个原输入的反向观察/恢复。`noRawFromMere`排除从mere代表中恢复每个原分子。

平方与商关系相容；`squareFromMere`实际经截断消去到非命题的集合ℚ，并证明结果正确。`generatedSquare`给实际任务输出；Rich显式保留所选源时分子观察也合法。

否定原输入恢复不等于不存在任意规范代表选择；截断限制不等于任何非命题数据都不可取出。任务所需观察和被遗忘信息必须逐项检查。

## 6. 当前整体判词和反证入口

当前旧“四弹完美闭环”判词未获上述结果支持。要确认HoTT现实相对失配，还须固定同X/操作/信息/观察/Done，定位实际HoTT能力承诺，证明同任务困难及保真连接，检查最强恢复，再统一源码、依赖、解释与现实范围。

审阅者若发现定理声明与自然语言不符、未经披露公设/选项、实际像或初末图偷换、同一被承诺任务的失败、或原文已经给出缺失保真桥，应指出具体文件/符号、输入和反例。普通库修复、核类型错误、哲学异议和形式反例分别处理。

本包未证明无缺陷、全局一致性、原则独立性、原创性、普适可移植或真实物理实施。学术评价仍可改变当前解释；局部真结果与整体未闭合可以同时成立。
