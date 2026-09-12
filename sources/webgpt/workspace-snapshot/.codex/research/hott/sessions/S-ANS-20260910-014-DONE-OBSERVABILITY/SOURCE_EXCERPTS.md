# 本轮一手规则与前次结果定位

## HoTT Book §3.9：唯一目标的命题截断消去

文件：`HoTT/theory-schema/upstream/book-578b85cc/logic.tex`
固定目录：book-578b85cc。
SHA-256：`76ac2e06ffa133ede0612584fef4b9c81d698d4e0b7a4ec683131448edfed2f2`。
本轮直接读取范围：797—841行；此处逐行保留。
这是类型论T4的规则依据，不证明本轮所有应用已经内核检查。
未联网更新来源，未运行书籍或归档代码。

```tex
797 | 
798 | \index{denial|)}%
799 | \index{axiom!of choice|)}%
800 | 
801 | \section{The principle of unique choice}
802 | \label{sec:unique-choice}
803 | 
804 | \index{unique!choice|(defstyle}%
805 | \indexsee{axiom!of choice!unique}{unique choice}%
806 | 
807 | The following observation is trivial, but very useful.
808 | 
809 | \begin{lem}\label{thm:prop-equiv-trunc}
810 |   If $P$ is a mere proposition, then $\eqv P {\brck P}$.
811 | \end{lem}
812 | \begin{proof}
813 |   Of course, we have $P\to \brck{P}$ by definition.
814 |   And since $P$ is a mere proposition, the universal property of $\brck P$ applied to $\idfunc[P] :P\to P$ yields $\brck P \to P$.
815 |   These functions are quasi-inverses by \cref{lem:equiv-iff-hprop}.
816 | \end{proof}
817 | 
818 | Among its important consequences is the following.
819 | 
820 | \begin{cor}[The principle of unique choice]\label{cor:UC}
821 |   Suppose a type family $P:A\to \type$ such that
822 |   \begin{enumerate}
823 |   \item For each $x$, the type $P(x)$ is a mere proposition, and
824 |   \item For each $x$ we have $\brck {P(x)}$.
825 |   \end{enumerate}
826 |   Then we have $\prd{x:A} P(x)$.
827 | \end{cor}
828 | \begin{proof}
829 |   Immediate from the two assumptions and the previous lemma.
830 | \end{proof}
831 | 
832 | The corollary also encapsulates a very useful technique of reasoning.
833 | Namely, suppose we know that $\brck A$, and we want to use this to construct an element of some other type $B$.
834 | We would like to use an element of $A$ in our construction of an element of $B$, but this is allowed only if $B$ is a mere proposition, so that we can apply the induction principle for the propositional truncation $\brck A$; the most we could hope to do in general is to show $\brck B$.
835 | %
836 | Instead, we can extend $B$ with additional data which characterizes \emph{uniquely} the object we wish to construct.
837 | Specifically, we define a predicate $Q:B\to\type$ such that $\sm{x:B} Q(x)$ is a mere proposition.
838 | Then from an element of $A$ we construct an element $b:B$ such that $Q(b)$, hence from $\brck A$ we can construct $\brck{\sm{x:B} Q(x)}$, and because $\brck{\sm{x:B} Q(x)}$ is equivalent to $\sm{x:B} Q(x)$ an element of $B$ may be projected from it.
839 | An example can be found in \cref{ex:decidable-choice}.
840 | 
841 | A similar issue arises in set-theoretic mathematics, although it manifests slightly
```

## 与上一轮的差量

前次路径：`.codex/research/hott/sessions/S-ANS-20260910-011-COMPLETION-CERTIFICATE/PROOF_NOTE.md`。
SHA-256：`be97fe471500bee7b03ed441e6e4e929e06d77ab18bf7e5b3247b3f2116076f7`。
原论证涉及嵌入、唯一原像、真像vs负像、AMO安全性、停止界限和源码输入范围。

本轮使用List Bool上的Done擦除，原始fib可以不唯一，但q在fib中唯一。
因此不是把前次“fib本身为命题”的引理直接复制到多原像场景，而是先建立命题型唯一答案图Answer(s)，再作合法消去。
新T3是有效oracle模型中的有限回答证据判据，不引用书中一个尚未定位的同名定理。
数学独立复核、新颖性与内核执行均未完成。
