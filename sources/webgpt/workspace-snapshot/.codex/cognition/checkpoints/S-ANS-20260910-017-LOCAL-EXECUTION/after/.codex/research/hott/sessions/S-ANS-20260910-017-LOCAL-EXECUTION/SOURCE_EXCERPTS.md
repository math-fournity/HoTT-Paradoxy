# R017实际所用规则摘录

仅局部读取，不冒称本轮审查完整HoTT元理论。

## HoTT/theory-schema/upstream/book-578b85cc/formal.tex lines 198–219

198 | and use infix notation $x\circ y$ for $\circ(x,y)$. This of course is just composition of functions.
199 | 
200 | The second kind of defined constant is used to specify a (parameterized) mapping
201 | $f(x_1,\dots,x_n,x)$, where $x$ ranges over a type whose elements are generated
202 | by zero or more primitive constants.  For each such primitive constant $c$ there
203 | is a defining equation of the form
204 | \[
205 |   f(x_1,\dots,x_n,c(y_1,\dots,y_m)) \defeq t,
206 | \]
207 | where $f$ may occur in $t$, but only in such a way that it is clear that the
208 | equations determine a totally defined function. The paradigm examples of such
209 | defined functions are the functions defined by primitive recursion on the
210 | natural numbers. We may call this kind of definition of a function a \emph{total
211 |   recursive definition}.
212 | \index{total!recursive definition}%
213 | In computer science and logic this kind of definition
214 | of a function on a recursive data type has been called a \define{definition by
215 |   structural recursion}.
216 | \index{definition!by structural recursion}%
217 | \index{structural!recursion}%
218 | \index{recursion!structural}%
219 | 

## HoTT/theory-schema/upstream/book-578b85cc/formal.tex lines 383–409

383 | \subsection{Natural numbers}
384 | 
385 | The type of natural numbers is obtained by introducing primitive constants
386 | $\N$, $0$, and $\suc$ with the following rules:
387 | %
388 | \begin{itemize}
389 |   \item $\N : \UU_0$,
390 |   \item $0:\N$,
391 |   \item $\suc:\N\rightarrow \N$.
392 | \end{itemize}
393 | %
394 | Furthermore, we can define functions by primitive recursion. If we have
395 | $C : \N \rightarrow \UU_k $ we can introduce a defined constant $f:\tprd{x:\N}C(x)$ whenever we have
396 | %
397 | \begin{align*}
398 |   d & : C(0) \\
399 |   e & : \tprd{x:\N}(C(x)\rightarrow C(\suc (x)))
400 | \end{align*}
401 | %
402 | with the defining equations
403 | %
404 | \begin{equation*}
405 |   f(0) \defeq d
406 |   \qquad\text{and}\qquad
407 |   f(\suc (x)) \defeq e(x,f(x)).
408 | \end{equation*}
409 | 

## HoTT/theory-schema/upstream/book-578b85cc/formal.tex lines 1143–1178

1143 |   If $A$ is in normal form then the 
1144 |   judgment $A : \UU$ is decidable. If $A : \UU$ and $t$ is in normal form then the judgment
1145 |   $t:A$ is decidable.
1146 | \end{thm}
1147 | 
1148 | Logical consistency\index{consistency} (of the system in \cref{sec:syntax-informally}) follows
1149 | immediately: if we had $a:\emptyt$ in the empty context, then by
1150 | \cref{thm:conversion-preserves-typing,thm:strong-normalization}, $a$
1151 | simplifies to a normal term $a':\emptyt$. But by
1152 | \cref{lem:normal-forms} no such term exists.
1153 | 
1154 | \begin{cor}
1155 |  The system in \cref{sec:syntax-informally} is logically consistent.
1156 | \end{cor}
1157 | 
1158 | Similarly, we have the \emph{canonicity}\indexdef{canonicity} property that if $a:\N$ in the empty
1159 | context, then $a$ simplifies to a normal term $\suc^k(0)$ for some numeral $k$.
1160 | 
1161 | \begin{cor}
1162 |  The system in \cref{sec:syntax-informally} has the canonicity property.
1163 | \end{cor}
1164 | 
1165 | Finally, if $a,A$ are in normal form, it is \emph{decidable} whether $a:A$; in
1166 | other words, because type-checking amounts to verifying the correctness of a
1167 | proof, this means we can always ``recognize a correct proof when we see one''.
1168 | 
1169 | \begin{cor}
1170 | The property of being a proof in the system in \cref{sec:syntax-informally} is decidable.
1171 | \end{cor}
1172 | 
1173 | \mentalpause
1174 | 
1175 | The above results do not apply to the extended system of homotopy type
1176 | theory (i.e., the above system extended by \cref{sec:hott-features}), since
1177 | occurrences of the univalence axiom and constructors of higher inductive types
1178 | never simplify, breaking \cref{lem:normal-forms}. It is an open question\index{open!problem}

## HoTT/theory-schema/upstream/book-578b85cc/logic.tex lines 801–838

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

## HoTT/theory-schema/CORE_RULES.md lines 103–161

103 | ## C05 · Π：依赖函数类型
104 | 
105 | **依据**：A.2 Dependent function types，646 行起。
106 | 
107 | ```text
108 | Formation:
109 | Γ ⊢ A:Uᵢ    Γ,x:A ⊢ B:Uᵢ
110 | ──────────────────────────
111 | Γ ⊢ Π(x:A).B : Uᵢ
112 | 
113 | Introduction:
114 | Γ,x:A ⊢ b:B
115 | ─────────────────────
116 | Γ ⊢ λx.b : Π(x:A).B
117 | 
118 | Elimination:
119 | Γ ⊢ f:Π(x:A).B    Γ ⊢ a:A
120 | ──────────────────────────
121 | Γ ⊢ f(a):B[a/x]
122 | 
123 | Computation (β):
124 | (λx.b)(a) ≡ b[a/x] : B[a/x]
125 | 
126 | Uniqueness (η, A.2):
127 | f ≡ λx.f(x) : Π(x:A).B
128 | ```
129 | 
130 | 非依赖情形定义 `A→B := Π(x:A).B`。β/η 是判断相等；函数外延性是另外一项内部 identity 原则，不是把这两个规则改名。
131 | 
132 | **呈现差异**：A.1 明确不加入这里的 judgmental η，A.2 加入。谈归约和正规化时必须标明采用哪一呈现。
133 | 
134 | **时间切口**：函数项具有计算行为，但其 identity 不自动记录代码、执行轨迹和运行成本。具体丢失何物需要指定 Program→Function 语义，而非由 Π 类型名称决定。
135 | 
136 | ## C06 · Σ：依赖对类型
137 | 
138 | **依据**：A.2 Dependent pair types，713 行起；§2.7。
139 | 
140 | ```text
141 | Formation:
142 | A:Uᵢ, x:A ⊢ B:Uᵢ    ⇒    Σ(x:A).B : Uᵢ
143 | 
144 | Introduction:
145 | a:A, b:B(a)           ⇒    (a,b):Σ(x:A).B
146 | 
147 | Elimination:
148 | C:(Σ(x:A).B)→Uⱼ
149 | d:Π(x:A).Π(y:B(x)).C(x,y)
150 | ⇒ indΣ(C,d):Π(p:Σ(x:A).B).C(p)
151 | 
152 | Computation:
153 | indΣ(C,d,(a,b)) ≡ d(a,b)
154 | ```
155 | 
156 | 这里使用函数式记法转述消去器；严格 A.2 绑定写法及宇宙条件见来源。投影 `pr₁(p):A`、`pr₂(p):B(pr₁(p))` 可由消去器定义。非依赖情形为积 A×B。
157 | 
158 | Σ 的 judgmental η **未在此基线假定**；`(pr₁ p,pr₂ p)=p` 的命题性唯一性可以证明。
159 | 
160 | **现实切口**：Σ 正是把来源、成本或证明附在对象上的直接方法。忘掉第二分量可能损失信息；“用了 HoTT”本身不要求把第二分量忘掉。
161 | 

## HoTT/theory-schema/CORE_RULES.md lines 186–206

186 | ## C09 · 自然数、递归与归纳
187 | 
188 | **依据**：A.2 Natural number type，860 行起；§1.9–1.10。
189 | 
190 | ```text
191 | N:Uᵢ
192 | zero:N
193 | suc:N→N
194 | 
195 | C:N→U
196 | c₀:C(zero)
197 | cₛ:Π(n:N).C(n)→C(suc n)
198 | ──────────────────────────
199 | indN(C,c₀,cₛ):Π(n:N).C(n)
200 | 
201 | indN(C,c₀,cₛ,zero) ≡ c₀
202 | indN(C,c₀,cₛ,suc n) ≡ cₛ(n,indN(C,c₀,cₛ,n))
203 | ```
204 | 
205 | 这是合法结构递归；不是任意自调用/循环算子。依赖归纳比只指定函数输入输出更有约束。一个定义使用递归，不代表它违反用户要求的因果准入。
206 | 

## HoTT/theory-schema/CORE_RULES.md lines 353–365

353 | ## C17 · 定义、精化、检查与证明搜索
354 | 
355 | **依据**：A.2 Definitions；A.1 已定义常量；§1.10。
356 | 
357 | - 定义名、隐式参数和典型歧义需要展开/精化到规则能检查的形式；
358 | - 精化（elaboration）不等于类型核心本身；
359 | - 检查给定候选项，不等于搜索任意问题的证明；
360 | - 书中结构递归不能替代任意求值器的终止保证；
361 | - 公理常量是有类型的假设，不是被归约计算出来的见证。
362 | 
363 | 因此“证明检查器接受”还必须追问：接受了哪个项、哪些公理、什么 universe 设定、什么编译/内核选项。Schema 不把特定 Agda/Lean 行为自动等同于 book 核心。
364 | 
365 | ## C18 · 元理论：结论与适用系统一起记录
