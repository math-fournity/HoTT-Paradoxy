# C04：双环路运输次序及真实逆序恢复

本包在Cubical Agda原生Bouquet Bool上定义三个标签的类型族，检验两个同基点回路的有序合成对纤维的作用。源码与primary run `20260924-MO3-BOUQUET-ORDER-001-02`对应；精确结论及量词见唯一矩阵C331–334，proof ID `MP-MO3-BOUQUET-ORDER-001`。Git身份由所选包版本检查另核，不改写at-run状态。

`BouquetOrder.agda`的`--safe --cubical --guardedness`与固定库一致。Mark/两个置换/逆律是本地定义；State的loop分支使用ua，act使用原生subst，合成使用库substComposite。没有本地postulate、primitive、未填洞或coinductive定义。`--guardedness`是固定Prelude的导入选项要求，不把本题改称clocked或guarded calculus研究。

形式结果限这个族：α后β把a送c，β后α把a送b；原生终态及路径不同；真实逆序的逆路径恢复原标签；常值族对loop不敏感。两回路的端点都是base，端点描述不等于纤维作用描述。完整理论可以表达差别，不构成它忽略顺序的实例；现实桥仅本候选的理想离散校准。

依赖固定于复用的`../stage-colimit/BUILTIN-SOURCES.json`及`../../dedekind-omega-missile/TOOLCHAIN.json`（repo路径以正式manifest为准）。前者是全部36个安装builtin源的保守清单，不声称全被本次用到；本次运行前后核相同hash。`DEPENDENCY-AUDIT.json`从本run实际stdout提取58个检查模块并按canonical lexical scanner审查postulate/primitive，零声明命中；这不否定builtin边界，也不是独立最小公理集证明。外部Cubical全树、binary和archive由run source-manifest固定。审计JSON是run后导出的证据，不是kernel输入或新公理。

失败原件：run01因缺guardedness导入资格退出42，原源码副本在`第三轮机器统观/Session-A/证据/W3-C04/attempt-001/`。修正选项后run02退出0。`WrongOrder.agda`以refl声称两输出相等，control01应因UnequalTerms拒绝；该控制不证明一般校验器正确性。

不支持物理仪器、空间连续性、零大小点/逼近圆环、任意族/路径分类、全理论完备或全球原创性。过程卡/现实对应与父级G2判断由Session-A过程002拥有。
