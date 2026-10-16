# 原Weak域与Markov方向的来源审查

本单元要核对固定Dedekind实数基线中，RNZA能否推出Book的二元Markov形式，并把结果接到已有实际Weak最终图覆盖。本文记录来源与方法选择；数学证据等级由正式run和claim/index资格另行决定。

## 原典

固定Book commit `578b85cc8d586b1677ec4335148adeb443057d24`，`HoTT/theory-schema/upstream/book-578b85cc/reals.tex`，原行3204–3222的`ex:reals-apart-neq-MP`。其明确请求为：所有Dedekind实数x≠y推出x apart y这一原则蕴含二元Markov；随后询问反方向。这是来源报告，不是把练习本身当本repo已证明。

小宇宙、mere存在和Bool真假形式由现有`MarkovBookForms.agda`拥有；`RealPrincipleBookScope.agda`已将零点RNZA与任意实数对表述连接。旧文件结尾说“本模块未断言实数—Markov桥”，保留其原模块范围；本轮新模块承担该连接，不追改旧收据。

## 固定库的决定性实物

| 来源 | 本轮消费 |
|---|---|
| logic/markovs-principle，logic/markovian-types | 库原则的精确类型；没有实例化该原则 |
| elementary-number-theory/unit-fractions-rational-numbers | 1/(n+1)正性、单调性、对每个正有理界取得更小权重 |
| elementary-number-theory/strict-inequality-rational-numbers，inequality-natural-numbers | 有理比较/中介数、有限前缀与尾部的全域划分 |
| real-numbers/lower-dedekind-real-numbers | 下cut非空与双向roundedness合同 |
| real-numbers/real-numbers-from-lower-dedekind-real-numbers | 从有上界且located的下cut构造实际Dedekind实数，而非假设一个“编码实数”存在 |
| real-numbers/strict-inequality-real-numbers，inequality-real-numbers，apartness-real-numbers | 正性与cut成员转换、非负、相等、apartness的具体接口 |

固定库为no-erasure派生树`3787fb34df15515246da11b90b609d3a2063f15e234f19c1e7f64553c4990f57`，父commit7b81411d；其基础公设/工具限制沿既有配置，不借本单元认证全库声性。

## 检索与方法选择

zvec语义查询返回`Transport closed`，随后在固定real-numbers/real-analysis/metric-spaces执行Markov/binary相关精确检索，并查看上述具体定义。在该检索范围没有找到现成实数—Markov连接，不声称全库或其他库不存在。

曾查看Cauchy近似、级数及supremum接口用于选择实现。最终采用更小的直接cut路线：L_f(q)由q<0或某个f(n)=true且q<1/(n+1)给出。located性仅检查有限前缀；尾部由有理权重界处理。避免为一个方向引入完整级数/收敛工程或额外可数选择假设。

现有圆环入口是`NativeMotionComplete.WeakFinalCoverage`与`weakFinalCoverageGivesLift`，继续使用原motion(1,u)和同一平面点；未把它换为另一个抽象覆盖谓词。

## 证据边界

即使该前向蕴含过核，也只给精确必要后果；没有自动给BookMarkov→所有Dedekind RNZA、原则独立性/不可证性、LEM必要性、无条件Weak覆盖或HoTT错误承诺。若研究反方向，必须先固定实数的可用表示数据，不能从mere存在偷偷选择全序列近似。
