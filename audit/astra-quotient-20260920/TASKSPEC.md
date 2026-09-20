# 同GOLD有理数商与截断数据消费

状态：候选合同，原生核验前不交付为数学结论。任务BP-QUOTIENT-CONSUMER-01，计划proof MP-ASTRA-QUOTIENT-CONSUMER-001，claims C305/C306。

固定Cubical0.9的Rationals.Base.ℚ及原GOLD，不用QuoQ。原代表Frac=ℤ×ℕ₊₁；pack为真实商映射；Rep(q)=Σr:Frac,pack(r)=q。SquareTask(q)=Σout:ℚ,out=q·q。原始分子任务要求对全部r返回fst(r)，不能改为某个规范代表的分子。

五项：原商关系下实际加乘/平方及GOLD谓词保持；两个等价分数的原分子差异和精确不存在命题；[]surjective→mere Rep(q)→rec→Set（显式常值性）→真实平方值与Done；两项错误关系/常值证据的固定项控制；明确给定原代表时的观察及裸输入边界。

必须分开：数学不存在证明、固定项被拒、正确函数值可恢复、原历史代表信息未由裸商类给出。目标ℚ为Set数据且证明它不是Prop；不能以“截断只能消去到命题”的粗略口号替代实际接口审查。全部假设显式；无LEM、resizing或新postulate。

母构造先过核，再运行RawNumeratorQuotient与RawNumeratorTruncation两个错误项。类型诊断要落在实际代表兼容/常值性义务；缺库/解析/超时不计成功拒绝。正构造的correctness/Done与给定数据来源一起保留。完成五项及原生证据后返回原广义几何和整体策略；不扩成全商/全HoTT完备。
