# C02：有理区间覆盖到有限原索引列表

本包使用实际Dedekind cuts、有理端点和原生命题截断，连接有限覆盖、可检查重叠链、有限列表枚举及最小见证。proof为`MP-MO3-FINITE-COVER-001`，唯一矩阵C335–339，primary为`20260924-MO3-FINITE-COVER-001-08`。本地证据与Git闭合分别检查，不将at-run状态回写成事后状态。

正结果不是泛P模型：R复用CutRealLayer的`DedekindReals ℓ-zero`；`InUnit`为下截集定义的0≤x≤1；覆盖量化全部这些cut点。`IntervalCover`给严格有理重叠证书及真实点覆盖证明；`RationalCuts`实际构造有理数嵌入、密度、0和1/2等点；`FiniteSubcover`从任意有限逐点子覆盖递归取一条链，消除了只接受较强链输入的缺口。

`FiniteCoverSearch`枚举长度及原索引均≤n的全部有限列表，证明每个有限列表在某有限stage出现，并将mere成功信息消去到唯一最小stage，最终返回原索引列表和覆盖。`GenericFiniteCover.natSelector`把结果接到与一般索引相同的GenericCover合同。列表允许重复，这是Book的List I接口；算法不承诺最短或无重复。

相反，若要求对每个I:Type₀同时给统一提取器，即使区间恒为(-1,2)，也会从无标签二元素类型统一选点；本包实际构造该归约并复用原生noUniformChoice。它不否定固定已给I的所有选择，也不否定保留枚举/标签后的正结果。

**输入边界必须保留。** 正定理输入为mere有限子覆盖，不能删除成只有任意点覆盖。Book §11.5对取得这一输入分别有LEM下的点覆盖定理及归纳覆盖定理；本包不重新形式化它们，不把来源身份升成当前机器证明。具体overlapping族的输入则由本包自己的覆盖证明提供。没有新增物理期限、神谕或恢复原隐藏选表的任务。

工具配置为safe/cubical/guardedness/two-level，沿固定Agda2.8.0/Cubical0.9。`CutRealLayer.agda`、`CutInfra.agda`、`NoCanonicalPoint.agda`都是精确依赖副本，三个snapshot JSON连接原件hash；未修改原件，不采纳其所有历史说明。所有本地传递依赖在source-manifest中，外部树/binary/archive均锁定；共36个builtin源的保守清单复用并重核。

`DEPENDENCY-AUDIT.json`从primary真实stdout提取143个检查模块，lexical扫描未命中显式postulate/primitive声明；这不否定builtin边界，不是最小公理依赖或kernel正确性证明。审计是运行后派生证据。

原始stdout保留三处不同定义的`UnsupportedIndexedMatch`警告（部分重复打印）：inspectComplete、removeLength、splitMember。它们的任意transported索引证明输入未必有定义性计算；不得据本包宣称此类统一归约能力。已核具体`refl`目标、路径等式和软件执行分别计量。官方2.8.0说明与本次范围见Session-A证据W3-C02/indexed-match-boundary.md；没有关警告或修改全局选项。

失败/控制：01保留overlap保留词解析失败；02保留有理数值写法错误；03保留不存在的concat导入；04为较早链/搜索子模块接受；BRIDGE-01为有理cut辅助接受；05保留局部extend名称冲突；06为较早完整接口接受；07保留具体输出桥的未解meta；08为最终源接受。修改过的失败/早期接受源在Session-A/证据/W3-C02/attempt-*保全；未变依赖仍按原hash可查。WrongTouching单独拒绝不代替C337的实际缺口证明。

四个软件fixture使用Fraction精确端点与固定stage前缀，保独立product重算、真实stdout/stderr与重放收据。它们不代替原生全称命题；touching的软件有限未命中也没有被拿来推出数学无界结论。

无HoTT内部矛盾、一般物理完成或全理论完备结论。该候选的原意/现实桥和父级影响由Session-A过程003持有，B尚未独立审计。
