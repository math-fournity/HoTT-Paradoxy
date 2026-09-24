# R13：整开区间、有限覆盖与严格内缩余量

本包使用与C02相同的真实Dedekind cuts，但检验另一个问题：所有严格内部有理开区间组成的族能否用有限表覆盖整个OpenUnit，以及固定内缩闭区间有何不同。proof为`MP-MO3-OPEN-COVER-MARGIN-001`，精确C340–341及primary01由唯一矩阵/registry登记；Git身份另经版本检查。

`OpenCoverMargins.agda`保Inner的0<l<r<1、原成员和覆盖目标。全部族的pointwise覆盖用cut的rounded/located/disjoint取得同一x附近的有理端点；有限反例对实际有限列表计算一个正公共左界s，再取rationalCut(mid 0 s)作漏点。不是有理采样或有限未命中推全称。

正控制给所有0<a<b<1明确的原Inner索引(mid 0 a,mid b 1)，覆盖每个真实ClosedBetween a b cut点。它改变目标范围，不拿来冒整个开区间已覆盖；余量正是该对照要保留的条件。

本包没有实现Book全inductive-cover HIT及其紧致性证明，不认证或推翻该证明。Book源里的严格内缩条件与传递段落要按来源范围审查；pointwise反对照只能支持这里明确写出的加强边界。原意/现实解释/源简写评价由Session-A过程004拥有。

工具为固定Agda2.8.0/Cubical0.9，safe/cubical/guardedness/two-level。C02共用的IntervalCover、RationalCuts、CutRealLayer、CutInfra均原字节复用，所有本地传递依赖列manifest；新证明不依赖C02列表搜索/GenericSelector模块。OPEN-MARGINS-DEPENDENCY-AUDIT.json从实际stdout核140个模块，显式声明扫描零命中、无warning；36 builtin清单复核不等无primitive边界。

WrongWholeCover尝试用OpenUnit的Lower x 0直接填Lower x(mid 0 quarter)，实际退出42，诊断为检查fst bounds时UnequalTerms。控制只说明这份错误输入被拒；C340无有限表的结论来自独立原生证明。

不声称全球原创、HoTT独有、内部矛盾或现实相对失配；没有把whole-open与closed-inner混为同一Done。该过程是C02 producer侧条件的补审，不计作又一个完全独立的机制家族。
