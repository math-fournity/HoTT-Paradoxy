<!-- governance-shard:v2
logical_id: MO3-C-PARENT-COVERAGE
shard_id: 001
index: ../父范围与覆盖.md
-->

# 固定Book正文与附录入口

> HUMAN_EDITED；owner=Session C。初始定位由锁定来源的既有入口清单一次性展开，随后人工维护处置。它没有自动认证任何正文已审。

本页固定书式HoTT的来源边界：The Univalent Foundations Program，Book commit `578b85cc8d586b1677ec4335148adeb443057d24`。main.tex、formal.tex（1259行EOF）及preliminaries.tex（2044行EOF）已全文读取；实际语义处置以本表和004片为准。A.2/A.3是主要形式呈现，A.1差异、A.4及未编号内容均保留，不靠删去它们获得remainder=0。原始来源沿用CC BY-SA 3.0；本页是项目研究导航，不是上游认可。

## 1. 编号正文入口

以下105个入口由原典章节定位而来。初始均UNREVIEWED/QUESTION；后续实际处置原位更新。行号是锁定源码中的开始行；审查范围从该节开始到下一节之前，并继续检查所属章节的未编号内容。仅有条目/标题/Schema转述不升级覆盖；UNASSIGNED项仍待R2补实际处置。

|ID|原典位置|原始节标题|覆盖处置|语义映射|
|---|---|---|---|---|
|B01.01|[preliminaries.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/preliminaries.tex) L4|`\section{Type theory versus set theory}`|REVIEWED|004§2/5，N-BASE-CONTEXT/EVIDENCE|
|B01.02|[preliminaries.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/preliminaries.tex) L175|`\section{Function types}`|REVIEWED|004§2/5，N-BASE-CONTEXT|
|B01.03|[preliminaries.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/preliminaries.tex) L358|`\section{Universes and families}`|REVIEWED|004§2/5，N-BASE-SIZE|
|B01.04|[preliminaries.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/preliminaries.tex) L437|`\section{Dependent function types (\texorpdfstring{$\Pi$}{Π}-types)}`|REVIEWED|004§2/5，N-BASE-CONTEXT/SIZE|
|B01.05|[preliminaries.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/preliminaries.tex) L530|`\section{Product types}`|REVIEWED|004§2/5，N-BASE-ENCODING；编码研究待核|
|B01.06|[preliminaries.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/preliminaries.tex) L728|`\section{Dependent pair types (\texorpdfstring{$\Sigma$}{Σ}-types)}`|REVIEWED|004§2/5，N-BASE-EVIDENCE/CONTEXT|
|B01.07|[preliminaries.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/preliminaries.tex) L870|`\section{Coproduct types}`|REVIEWED|004§2/5，N-BASE-EVIDENCE|
|B01.08|[preliminaries.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/preliminaries.tex) L959|`\section{The type of booleans}`|REVIEWED|004§2/5，C-BASE-02待核，不冒完成|
|B01.09|[preliminaries.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/preliminaries.tex) L1062|`\section{The natural numbers}`|REVIEWED|004§2/3，N-BASE-ENCODING|
|B01.10|[preliminaries.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/preliminaries.tex) L1205|`\section{Pattern matching and recursion}`|REVIEWED|004§2/4，递归资格与精化|
|B01.11|[preliminaries.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/preliminaries.tex) L1266|`\section{Propositions as types}`|REVIEWED|004§2/5，N-BASE-EVIDENCE；Book3仍待审|
|B01.12|[preliminaries.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/preliminaries.tex) L1547|`\section{Identity types}`|REVIEWED|004§2/5，三个subsection及N-BASE-PATH-FAMILY|
|B02.01|[basics.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/basics.tex) L210|`\section{Types are higher groupoids}`|UNREVIEWED|UNASSIGNED|
|B02.02|[basics.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/basics.tex) L683|`\section{Functions are functors}`|UNREVIEWED|UNASSIGNED|
|B02.03|[basics.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/basics.tex) L748|`\section{Type families are fibrations}`|UNREVIEWED|UNASSIGNED|
|B02.04|[basics.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/basics.tex) L969|`\section{Homotopies and equivalences}`|UNREVIEWED|UNASSIGNED|
|B02.05|[basics.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/basics.tex) L1191|`\section{The higher groupoid structure of type formers}`|UNREVIEWED|UNASSIGNED|
|B02.06|[basics.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/basics.tex) L1238|`\section{Cartesian product types}`|UNREVIEWED|UNASSIGNED|
|B02.07|[basics.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/basics.tex) L1393|`\section{\texorpdfstring{$\Sigma$}{Σ}-types}`|UNREVIEWED|UNASSIGNED|
|B02.08|[basics.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/basics.tex) L1534|`\section{The unit type}`|UNREVIEWED|UNASSIGNED|
|B02.09|[basics.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/basics.tex) L1568|`\section{\texorpdfstring{$\Pi$}{Π}-types and the function extensionality axiom}`|UNREVIEWED|UNASSIGNED|
|B02.10|[basics.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/basics.tex) L1706|`\section{Universes and the univalence axiom}`|UNREVIEWED|UNASSIGNED|
|B02.11|[basics.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/basics.tex) L1809|`\section{Identity type}`|UNREVIEWED|UNASSIGNED|
|B02.12|[basics.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/basics.tex) L1931|`\section{Coproducts}`|UNREVIEWED|UNASSIGNED|
|B02.13|[basics.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/basics.tex) L2070|`\section{Natural numbers}`|UNREVIEWED|UNASSIGNED|
|B02.14|[basics.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/basics.tex) L2165|`\section{Example: equality of structures}`|UNREVIEWED|UNASSIGNED|
|B02.15|[basics.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/basics.tex) L2360|`\section{Universal properties}`|UNREVIEWED|UNASSIGNED|
|B03.01|[logic.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/logic.tex) L11|`\section{Sets and \texorpdfstring{$n$}{n}-types}`|UNREVIEWED|UNASSIGNED|
|B03.02|[logic.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/logic.tex) L159|`\section{Propositions as types?}`|UNREVIEWED|UNASSIGNED|
|B03.03|[logic.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/logic.tex) L255|`\section{Mere propositions}`|UNREVIEWED|UNASSIGNED|
|B03.04|[logic.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/logic.tex) L353|`\section{Classical vs.\ intuitionistic logic}`|UNREVIEWED|UNASSIGNED|
|B03.05|[logic.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/logic.tex) L451|`\section{Subsets and propositional resizing}`|UNREVIEWED|UNASSIGNED|
|B03.06|[logic.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/logic.tex) L558|`\section{The logic of mere propositions}`|UNREVIEWED|UNASSIGNED|
|B03.07|[logic.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/logic.tex) L598|`\section{Propositional truncation}`|UNREVIEWED|UNASSIGNED|
|B03.08|[logic.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/logic.tex) L701|`\section{The axiom of choice}`|UNREVIEWED|UNASSIGNED|
|B03.09|[logic.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/logic.tex) L801|`\section{The principle of unique choice}`|UNREVIEWED|UNASSIGNED|
|B03.10|[logic.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/logic.tex) L852|`\section{When are propositions truncated?}`|UNREVIEWED|UNASSIGNED|
|B03.11|[logic.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/logic.tex) L938|`\section{Contractibility}`|UNREVIEWED|UNASSIGNED|
|B04.01|[equivalences.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/equivalences.tex) L34|`\section{Quasi-inverses}`|UNREVIEWED|UNASSIGNED|
|B04.02|[equivalences.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/equivalences.tex) L148|`\section{Half adjoint equivalences}`|UNREVIEWED|UNASSIGNED|
|B04.03|[equivalences.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/equivalences.tex) L376|`\section{Bi-invertible maps}`|UNREVIEWED|UNASSIGNED|
|B04.04|[equivalences.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/equivalences.tex) L417|`\section{Contractible fibers}`|UNREVIEWED|UNASSIGNED|
|B04.05|[equivalences.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/equivalences.tex) L493|`\section{On the definition of equivalences}`|UNREVIEWED|UNASSIGNED|
|B04.06|[equivalences.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/equivalences.tex) L513|`\section{Surjections and embeddings}`|UNREVIEWED|UNASSIGNED|
|B04.07|[equivalences.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/equivalences.tex) L602|`\section{Closure properties of equivalences}`|UNREVIEWED|UNASSIGNED|
|B04.08|[equivalences.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/equivalences.tex) L785|`\section{The object classifier}`|UNREVIEWED|UNASSIGNED|
|B04.09|[equivalences.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/equivalences.tex) L897|`\section{Univalence implies function extensionality}`|UNREVIEWED|UNASSIGNED|
|B05.01|[induction.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/induction.tex) L9|`\section{Introduction to inductive types}`|UNREVIEWED|UNASSIGNED|
|B05.02|[induction.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/induction.tex) L147|`\section{Uniqueness of inductive types}`|UNREVIEWED|UNASSIGNED|
|B05.03|[induction.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/induction.tex) L253|`\section{\texorpdfstring{$\w$}{W}-types}`|REVIEWED：规则/递归消费语义；定理仅SOURCE_REPORTED|[C-W-01 §6](<../过程与结果/001 - W类型的整族构造与执行完成问题.md>)；未证明全消费者性质|
|B05.04|[induction.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/induction.tex) L381|`\section{Inductive types are initial algebras}`|UNREVIEWED|UNASSIGNED|
|B05.05|[induction.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/induction.tex) L566|`\section{Homotopy-inductive types}`|UNREVIEWED|UNASSIGNED|
|B05.06|[induction.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/induction.tex) L752|`\section{The general syntax of inductive definitions}`|UNREVIEWED|UNASSIGNED|
|B05.07|[induction.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/induction.tex) L949|`\section{Generalizations of inductive types}`|UNREVIEWED|UNASSIGNED|
|B05.08|[induction.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/induction.tex) L1071|`\section{Identity types and identity systems}`|UNREVIEWED|UNASSIGNED|
|B06.01|[hits.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/hits.tex) L8|`\section{Introduction}`|UNREVIEWED|UNASSIGNED|
|B06.02|[hits.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/hits.tex) L105|`\section{Induction principles and dependent paths}`|UNREVIEWED|UNASSIGNED|
|B06.03|[hits.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/hits.tex) L353|`\section{The interval}`|UNREVIEWED|UNASSIGNED|
|B06.04|[hits.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/hits.tex) L429|`\section{Circles and spheres}`|UNREVIEWED|UNASSIGNED|
|B06.05|[hits.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/hits.tex) L551|`\section{Suspensions}`|UNREVIEWED|UNASSIGNED|
|B06.06|[hits.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/hits.tex) L718|`\section{Cell complexes}`|UNREVIEWED|UNASSIGNED|
|B06.07|[hits.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/hits.tex) L771|`\section{Hubs and spokes}`|UNREVIEWED|UNASSIGNED|
|B06.08|[hits.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/hits.tex) L883|`\section{Pushouts}`|UNREVIEWED|UNASSIGNED|
|B06.09|[hits.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/hits.tex) L1048|`\section{Truncations}`|UNREVIEWED|UNASSIGNED|
|B06.10|[hits.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/hits.tex) L1183|`\section{Quotients}`|UNREVIEWED|UNASSIGNED|
|B06.11|[hits.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/hits.tex) L1466|`\section{Algebra}`|UNREVIEWED|UNASSIGNED|
|B06.12|[hits.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/hits.tex) L1755|`\section{The flattening lemma}`|UNREVIEWED|UNASSIGNED|
|B06.13|[hits.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/hits.tex) L2041|`\section{The general syntax of higher inductive definitions}`|UNREVIEWED|UNASSIGNED|
|B07.01|[hlevels.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/hlevels.tex) L27|`\section{Definition of \texorpdfstring{$n$}{n}-types}`|UNREVIEWED|UNASSIGNED|
|B07.02|[hlevels.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/hlevels.tex) L236|`\section{Uniqueness of identity proofs and Hedberg's theorem}`|UNREVIEWED|UNASSIGNED|
|B07.03|[hlevels.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/hlevels.tex) L447|`\section{Truncations}`|UNREVIEWED|UNASSIGNED|
|B07.04|[hlevels.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/hlevels.tex) L776|`\section{Colimits of \texorpdfstring{$n$}{n}-types}`|UNREVIEWED|UNASSIGNED|
|B07.05|[hlevels.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/hlevels.tex) L1065|`\section{Connectedness}`|UNREVIEWED|UNASSIGNED|
|B07.06|[hlevels.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/hlevels.tex) L1378|`\section{Orthogonal factorization}`|UNREVIEWED|UNASSIGNED|
|B07.07|[hlevels.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/hlevels.tex) L1665|`\section{Modalities}`|UNREVIEWED|UNASSIGNED|
|B08.01|[homotopy.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/homotopy.tex) L309|`\section{\texorpdfstring{$\pi_1(S^1)$}{π₁(S¹)}}`|UNREVIEWED|UNASSIGNED|
|B08.02|[homotopy.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/homotopy.tex) L795|`\section{Connectedness of suspensions}`|UNREVIEWED|UNASSIGNED|
|B08.03|[homotopy.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/homotopy.tex) L886|`\section{\texorpdfstring{$\pi_{k \le n}$}{π\_(k≤n)} of an \texorpdfstring{$n$}{n}-connected space and \texorpdfstring{$\pi_{k < n}(\Sn ^n)$}{π\_(k<n)(Sⁿ)}}`|UNREVIEWED|UNASSIGNED|
|B08.04|[homotopy.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/homotopy.tex) L938|`\section{Fiber sequences and the long exact sequence}`|UNREVIEWED|UNASSIGNED|
|B08.05|[homotopy.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/homotopy.tex) L1175|`\section{The Hopf fibration}`|UNREVIEWED|UNASSIGNED|
|B08.06|[homotopy.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/homotopy.tex) L1558|`\section{The Freudenthal suspension theorem}`|UNREVIEWED|UNASSIGNED|
|B08.07|[homotopy.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/homotopy.tex) L1879|`\section{The van Kampen theorem}`|UNREVIEWED|UNASSIGNED|
|B08.08|[homotopy.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/homotopy.tex) L2340|`\section{Whitehead's theorem and Whitehead's principle}`|UNREVIEWED|UNASSIGNED|
|B08.09|[homotopy.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/homotopy.tex) L2542|`\section{A general statement of the encode-decode method}`|UNREVIEWED|UNASSIGNED|
|B08.10|[homotopy.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/homotopy.tex) L2647|`\section{Additional Results}`|UNREVIEWED|UNASSIGNED|
|B09.01|[categories.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/categories.tex) L46|`\section{Categories and precategories}`|UNREVIEWED|UNASSIGNED|
|B09.02|[categories.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/categories.tex) L281|`\section{Functors and transformations}`|UNREVIEWED|UNASSIGNED|
|B09.03|[categories.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/categories.tex) L478|`\section{Adjunctions}`|UNREVIEWED|UNASSIGNED|
|B09.04|[categories.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/categories.tex) L539|`\section{Equivalences}`|UNREVIEWED|UNASSIGNED|
|B09.05|[categories.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/categories.tex) L872|`\section{The Yoneda lemma}`|UNREVIEWED|UNASSIGNED|
|B09.06|[categories.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/categories.tex) L1073|`\section{Strict categories}`|UNREVIEWED|UNASSIGNED|
|B09.07|[categories.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/categories.tex) L1128|`\section{\texorpdfstring{$\dagger$}{†}-categories}`|UNREVIEWED|UNASSIGNED|
|B09.08|[categories.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/categories.tex) L1205|`\section{The structure identity principle}`|UNREVIEWED|UNASSIGNED|
|B09.09|[categories.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/categories.tex) L1366|`\section{The Rezk completion}`|UNREVIEWED|UNASSIGNED|
|B10.01|[setmath.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/setmath.tex) L36|`\section{The category of sets}`|UNREVIEWED|UNASSIGNED|
|B10.02|[setmath.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/setmath.tex) L683|`\section{Cardinal numbers}`|UNREVIEWED|UNASSIGNED|
|B10.03|[setmath.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/setmath.tex) L887|`\section{Ordinal numbers}`|UNREVIEWED|UNASSIGNED|
|B10.04|[setmath.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/setmath.tex) L1278|`\section{Classical well-orderings}`|UNREVIEWED|UNASSIGNED|
|B10.05|[setmath.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/setmath.tex) L1445|`\section{The cumulative hierarchy}`|UNREVIEWED|UNASSIGNED|
|B11.01|[reals.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/reals.tex) L37|`\section{The field of rational numbers}`|UNREVIEWED|UNASSIGNED|
|B11.02|[reals.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/reals.tex) L85|`\section{Dedekind reals}`|UNREVIEWED|UNASSIGNED|
|B11.03|[reals.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/reals.tex) L668|`\section{Cauchy reals}`|UNREVIEWED|UNASSIGNED|
|B11.04|[reals.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/reals.tex) L1778|`\section{Comparison of Cauchy and Dedekind reals}`|UNREVIEWED|UNASSIGNED|
|B11.05|[reals.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/reals.tex) L1876|`\section{Compactness of the interval}`|UNREVIEWED|UNASSIGNED|
|B11.06|[reals.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/reals.tex) L2466|`\section{The surreal numbers}`|UNREVIEWED|UNASSIGNED|

## 2. 附录与未编号内容

附录不是105节分母的一部分。以下起始行已从原始formal.tex结构定位；C已阅读全文。A00/A01/A02基础接口的REVIEWED具体依据与差异见[004§4](<004 - Book基础接口的语义处置.md>)，结果为SOURCE_REPORTED；未把A03/A04自动升级。

|ID|formal.tex行/范围|待审职责|覆盖处置|
|---|---|---|---|
|A00|1–158，Preliminaries从49开始|形式系统目的、元语法、绑定与判断说明|REVIEWED：004§4|
|A01|159–453|第一呈现、convertibility及η差异；八个子节全部保留|REVIEWED：004§4与C-W-01|
|A01.U|251|宇宙|REVIEWED：004§4|
|A01.PI|286|Π|REVIEWED：004§4|
|A01.SIGMA|313|Σ|REVIEWED：004§4|
|A01.SUM|349|余积|REVIEWED：004§4|
|A01.FIN|370|有限类型|REVIEWED：004§4|
|A01.NAT|383|自然数|REVIEWED：004§4|
|A01.W|410|W类型|REVIEWED：构造/递归接口，见C-W-01§6；SOURCE_REPORTED|
|A01.ID|433|Identity|REVIEWED：004§4|
|A02|454–974|第二呈现总说明与以下11子节；不能只读规则名|REVIEWED：004§4；非元定理证明|
|A02.CTX|503|上下文|REVIEWED：004§4|
|A02.STRUCT|537|结构规则及未逐条印出的合同性规则|REVIEWED：004§4；保610行排版观察|
|A02.U|620|宇宙|REVIEWED：004§4|
|A02.PI|646|Π|REVIEWED：004§4|
|A02.SIGMA|713|Σ|REVIEWED：004§4|
|A02.SUM|766|余积|REVIEWED：004§4|
|A02.ZERO|808|空类型|REVIEWED：004§4|
|A02.UNIT|826|单位类型|REVIEWED：004§4|
|A02.NAT|860|自然数|REVIEWED：004§4|
|A02.ID|907|Identity|REVIEWED：004§4|
|A02.DEF|943|定义|REVIEWED：004§4；C17其余分支仍待审|
|A03|975–1063|HoTT扩展总说明与两子节|UNREVIEWED|
|A03.UA|982|函数外延性与单价性|UNREVIEWED|
|A03.CIRCLE|1014|圆|UNREVIEWED|
|A04|1064–1196|基础元理论及适用系统|UNREVIEWED|
|A.NOTES|1197–EOF|附录Notes及出处|UNREVIEWED|

所有附录条目定位于[formal.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/formal.tex)。父行与子行有意重叠，是范围包含，不将二者相加称互斥分母。

|ID|额外原典范围|初始处置及必要性|
|---|---|---|
|U.INTRO|[introduction.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/introduction.tex) 全文|UNREVIEWED：理论对象、同伦解释与整体取舍不能由编号正文替代。|
|U.PREFACE|[preface.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/preface.tex) 全文|UNREVIEWED：核作者声明的目的/假设/呈现范围；不预先排除。|
|U.CHAPTERS|上述11章各自未编号引导、Notes、Exercises及所有subsection|UNREVIEWED：逐章EOF阅读时定位会影响规则/前提/关系的内容；练习不要求全部重新证明，但不能以“练习”排除理论信息。|
|U.B01.NOTES|preliminaries1850–1936|REVIEWED：004§2/4的命名配置差异，非今日实现现状。|
|U.B01.EXERCISES|preliminaries1937–2044 EOF；16题|REVIEWED：004§3全标签语义归组；C-BASE-02实际核证仍待办。|
|U.MACROS|[macros.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/macros.tex)、[symbols.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/symbols.tex)|UNREVIEWED：决定符号和规则读法时按依赖展开。|
|U.LABELS|[main.labelnumbers.first-edition](../../../HoTT/theory-schema/upstream/book-578b85cc/main.labelnumbers.first-edition)|UNREVIEWED：定位辅助；计数不承担语义。|
|U.BIB|[references.bib](../../../HoTT/theory-schema/upstream/book-578b85cc/references.bib)|UNREVIEWED：实际主张的来源链与配置比较入口。|
|U.FRONT|[front.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/front.tex)、[README.md](../../../HoTT/theory-schema/upstream/book-578b85cc/README.md)|UNREVIEWED：许可/版本及边界；后续可按实际内容正当归组。|
|U.MAIN|[main.tex](../../../HoTT/theory-schema/upstream/book-578b85cc/main.tex) 全文|REVIEWED（仅导航）：实际读取include顺序，确认11正文及formal；排版命令不承担数学结论。|

U.CHAPTERS是暂未细分的显式待审桶；必须在R1/R2逐章细化，不能以一行“已读完”关闭全部潜在语义。未编号理论内容的重要性尚未定，不自动视为范围外。

## 3. 双向映射剩余

B01.01–12及A00/A01/A02基础规则映射到004的逐项语义处置与N-BASE单元；B05.03/A01.W仍映射C-W-01。反向映射见004§2–5及过程001/002。Book1十二编号节REVIEWED是来源审查进展，C-BASE-02的编码/计算接口尚须实际判别；不与其数学结果混算。其余编号节、A03/A04/Notes及其它未编号范围仍未完成。B05.04/05虽已实际读全文，其更宽内部化/相干处置未完成，保UNREVIEWED。旧A四包精确复用已核，见复用owner，但尚未凭包名批量升级其它来源。剩余是父目标未完成的具体依据，不是OPEN_RESULT成果。
