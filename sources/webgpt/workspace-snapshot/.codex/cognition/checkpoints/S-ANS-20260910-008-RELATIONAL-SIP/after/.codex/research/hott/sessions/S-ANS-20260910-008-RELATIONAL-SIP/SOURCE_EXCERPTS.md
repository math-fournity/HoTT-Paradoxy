# Revision8 实际源区间（完整区间保留，不冒充全书审查）

原Book commit：578b85cc8d586b1677ec4335148adeb443057d24。
源文件：HoTT/theory-schema/upstream/book-578b85cc/categories.tex；SHA256：141332f0b27d5ab055419e02bada9664561758d129ebe4d52e43bb8e290b275f。
这些区间来自用户提供的固定版本项目源；此处是编号逐行证据副本，不改原文件。
范围：同构定义、标准结构定义及关系同态/同构的实际原文。

## §9.1 同构、idtoiso与有关运输：88—177行
```tex
88: \begin{defn}\label{ct:isomorphism}
89:   A morphism $f:\hom_A(a,b)$ is an \define{isomorphism}
90:   \indexdef{isomorphism!in a (pre)category}%
91:   if there is a morphism $g:\hom_A(b,a)$ such that $\id{g\circ f}{1_a}$ and $\id{f\circ g}{1_b}$.
92:   We write $a\cong b$ for the type of such isomorphisms.
93: \end{defn}
94: 
95: \begin{lem}\label{ct:isoprop}
96:   For any $f:\hom_A(a,b)$, the type ``$f$ is an isomorphism'' is a mere proposition.
97:   Therefore, for any $a,b:A$ the type $a\cong b$ is a set.
98: \end{lem}
99: \begin{proof}
100:   Suppose given $g:\hom_A(b,a)$ and $\eta:(\id{1_a}{g\circ f})$ and $\epsilon:(\id{f\circ g}{1_b})$, and similarly $g'$, $\eta'$, and $\epsilon'$.
101: We must show $\id{(g,\eta,\epsilon)}{(g',\eta',\epsilon')}$.
102:   But since all hom-sets are sets, their identity types are mere propositions, so it suffices to show $\id g {g'}$.
103:   For this we have
104:   \[g' = 1_a\circ g' = (g\circ f)\circ g' = g\circ (f\circ g') = g\circ 1_b = g\]
105:   using $\eta$ and $\epsilon'$.
106: \end{proof}
107: 
108: \symlabel{ct:inv}
109: \index{inverse!in a (pre)category}%
110: If $f:a\cong b$, then we write $\inv f$ for its inverse, which by \cref{ct:isoprop} is uniquely determined.
111: 
112: The only relationship between these two notions of sameness that we have in a precategory is the following.
113: 
114: \begin{lem}[\textsf{idtoiso}]\label{ct:idtoiso}
115:   If $A$ is a precategory and $a,b:A$, then
116:   \[(\id a b)\to (a \cong b).\]
117: \end{lem}
118: \begin{proof}
119:   By induction on identity, we may assume $a$ and $b$ are the same.
120:   But then we have $1_a:\hom_A(a,a)$, which is clearly an isomorphism.
121: \end{proof}
122: 
123: Evidently, this situation is analogous to the issue that motivated us to introduce the univalence axiom.
124: In fact, we have the following:
125: 
126: \begin{eg}\label{ct:precatset}
127:   \index{set}%
128:   There is a precategory \uset, whose type of objects is \set, and with $\hom_{\uset}(A,B) \defeq (A\to B)$.
129:   The identity morphisms are identity functions and the composition is function composition.
130:   For this precategory, \cref{ct:idtoiso} is equal to (the restriction to sets of) the map $\idtoeqv$ from \cref{sec:compute-universe}.
131: 
132:   Of course, to be more precise we should call this category $\uset_\UU$, since its objects are only the \emph{small sets}
133:   \index{small!set}%
134:   relative to a universe \UU.
135: \end{eg}
136: 
137: Thus, it is natural to make the following definition.
138: 
139: \begin{defn}\label{ct:category}
140:   A \define{category}
141:   \indexdef{category}
142:   is a precategory such that for all $a,b:A$, the function $\idtoiso_{a,b}$ from \cref{ct:idtoiso} is an equivalence.
143: \end{defn}
144: 
145: In particular, in a category, if $a\cong b$, then $a=b$.
146: 
147: \begin{eg}\label{ct:eg:set}
148:   \index{univalence axiom}%
149:   The univalence axiom implies immediately that \uset is a category.
150:   One can also show, using univalence, that any precategory of set-level structures such as groups, rings, topological spaces, etc.\ is a category; see \cref{sec:sip}.
151: \end{eg}
152: 
153: We also note the following.
154: 
155: \begin{lem}\label{ct:obj-1type}
156:   In a category, the type of objects is a 1-type.
157: \end{lem}
158: \begin{proof}
159:   It suffices to show that for any $a,b:A$, the type $\id a b$ is a set.
160:   But $\id a b$ is equivalent to $a \cong b$, which is a set.
161: \end{proof}
162: 
163: \symlabel{isotoid}
164: We write $\isotoid$ for the inverse $(a\cong b) \to (\id a b)$ of the map $\idtoiso$ from \cref{ct:idtoiso}.
165: The following relationship between the two is important.
166: 
167: \begin{lem}\label{ct:idtoiso-trans}
168:   For $p:\id a a'$ and $q:\id b b'$ and $f:\hom_A(a,b)$, we have
169:   \begin{equation}\label{ct:idtoisocompute}
170:     \id{\trans{(p,q)}{f}}
171:     {\idtoiso(q)\circ f \circ \inv{\idtoiso(p)}}.
172:   \end{equation}
173: \end{lem}
174: \begin{proof}
175:   By induction, we may assume $p$ and $q$ are $\refl a$ and $\refl b$ respectively.
176: Then the left-hand side of~\eqref{ct:idtoisocompute} is simply $f$.
177:   But by definition, $\idtoiso(\refl a)$ is $1_a$, and $\idtoiso(\refl b)$ is $1_b$, so the right-hand side of~\eqref{ct:idtoisocompute} is $1_b\circ f\circ 1_a$, which is equal to $f$.
```

## §9.8 The structure identity principle：1205—1363行（完整该节）
```tex
1205: \section{The structure identity principle}
1206: \label{sec:sip}
1207:  \index{structure!identity principle|(}
1208: 
1209: The \emph{structure identity principle} is an informal principle
1210: that expresses that isomorphic structures are identical.  We aim to
1211: prove a general abstract result which can be applied to a wide family
1212: of notions of structure, where structures may be many-sorted or even
1213: dependently-sorted, infinitary, or even higher order.
1214: 
1215: The simplest kind of single-sorted structure consists of a type with
1216: no additional structure.  The univalence axiom expresses the structure identity principle for that
1217: notion of structure in a strong form: for types $A,B$, the
1218: canonical function $(A=B)\to (\eqv A B)$ is an equivalence.
1219: 
1220: We start with a precategory $X$.  In our application to
1221: single-sorted first order structures, $X$ will be the category %\uset%
1222: of $\bbU$-small sets, where $\bbU$ is a univalent type universe.
1223: 
1224: \begin{defn}\label{ct:sig}
1225:   A \define{notion of structure}
1226:   \indexdef{structure!notion of}%
1227:   $(P,H)$ over $X$ consists of the following.
1228:   \begin{enumerate}
1229:   \item A type family $P:X_0 \to \type$.
1230:     For each $x:X_0$ the elements of $Px$ are called \define{$(P,H)$-structures}
1231:     \indexsee{PH-structure@$(P,H)$-structure}{structure}%
1232:     \indexdef{structure!PH@$(P,H)$-}%
1233:     on $x$.
1234:   \item For $x,y:X_0$, $f:\hom_X(x,y)$ and $\alpha:Px$, $\;\beta:Py$, a mere proposition
1235:   \[ H_{\alpha\beta}(f).\]
1236:     If $H_{\alpha\beta}(f)$ is true, we say that $f$ is a \define{$(P,H)$-homomorphism}
1237:     \indexdef{homomorphism!of structures}%
1238:     \indexdef{structure!homomorphism of}%
1239:     from $\alpha$ to $\beta$.
1240:   \item For $x:X_0$ and $\alpha:Px$, we have $H_{\alpha\alpha}(1_x)$.\label{item:sigid}
1241:   \item For $x,y,z:X_0$ and $\alpha:Px$, $\;\beta:Py$, $\;\gamma:Pz$,
1242: if $f:\hom_X(x,y)$ and $g:\hom_X(y,z)$, we have\label{item:sigcmp}
1243:   \[ H_{\alpha\beta}(f)\to H_{\beta\gamma}(g)\to H_{\alpha\gamma}(g\circ   f).\]
1244:    \end{enumerate}
1245:   When $(P,H)$ is a notion of structure, for $\alpha,\beta:Px$ we define
1246:   \[ (\alpha\leq_x\beta) \defeq H_{\alpha\beta}(1_x).\]
1247:   By~\ref{item:sigid} and~\ref{item:sigcmp}, this is a preorder (\cref{ct:orders}) with $Px$ its type of objects.
1248:   We say that $(P,H)$ is a \define{standard notion of structure}
1249:   \indexdef{structure!standard notion of}%
1250:   if this preorder is in fact a partial order, for all $x:X$.
1251: \end{defn}
1252: 
1253: Note that for a standard notion of structure, each type $Px$ must actually be a set.
1254: We now define, for any notion of structure $(P,H)$, a \define{precategory of $(P,H)$-structures},
1255: \indexdef{precategory!of PH-structures@of $(P,H)$-structures}%
1256: \indexdef{structure!precategory of PH@precategory of $(P,H)$-}%
1257: $A = \mathsf{Str}_{(P,H)}(X)$.
1258: \begin{itemize}
1259: \item The type of objects of $A$ is the type $A_0 \defeq \sm{x:X_0} Px$.
1260:   If $a\jdeq (x,\alpha):A_0$, we may write $|a| \defeq x$.
1261: \item For $(x,\alpha):A_0$ and $(y,\beta):A_0$, we define
1262:   \[\hom_A((x,\alpha),(y,\beta)) \defeq \setof{ f:x \to y | H_{\alpha\beta}(f)}.\]
1263: \end{itemize}
1264: The composition and identities are inherited from $X$; conditions~\ref{item:sigid} and \ref{item:sigcmp} ensure that these lift to $A$.
1265: 
1266: \begin{thm}[Structure identity principle]\label{thm:sip}
1267:   \indexdef{structure!identity principle}%
1268:   If $X$ is a category and $(P,H)$ is a standard notion of structure over $X$, then the precategory $\mathsf{Str}_{(P,H)}(X)$ is a category.
1269: \end{thm}
1270: \begin{proof}
1271:   By the definition of equality in dependent pair types, to give an equality $(x,\alpha)=(y,\beta)$ consists of
1272:   \begin{itemize}
1273:   \item An equality $p:x=y$, and
1274:   \item An equality $\trans{p}{\alpha}=\beta$.
1275:   \end{itemize}
1276:   Since $P$ is set-valued, the latter is a mere proposition.
1277:   On the other hand, it is easy to see that an isomorphism $(x,\alpha)\cong (y,\beta)$ in $\mathsf{Str}_{(P,H)}(X)$ consists of
1278:   \begin{itemize}
1279:   \item An isomorphism $f:x\cong y$ in $X$, such that
1280:   \item $H_{\alpha\beta}(f)$ and $H_{\beta\alpha}(\inv f)$.
1281:   \end{itemize}
1282:   Of course, the second of these is also a mere proposition.
1283:   And since $X$ is a category, the function $(x=y) \to (x\cong y)$ is an equivalence.
1284:   Thus, it will suffice to show that for any $p:x=y$ and for any $(\alpha:Px)$, $(\beta:Py)$, we have $\trans{p}{\alpha}=\beta$ if and only if both  $H_{\alpha\beta}(\idtoiso (p))$ and $H_{\beta\alpha}(\inv{\idtoiso(p)})$.
1285: 
1286:   The ``only if'' direction is just the existence of the function $\idtoiso$ for the category $\mathsf{Str}_{(P,H)}(X)$.
1287:   For the ``if'' direction, by induction on $p$ we may assume that $y\jdeq x$ and $p\jdeq\refl x$.
1288:   However, in this case $\idtoiso (p)\jdeq 1_x$ and therefore $\inv{\idtoiso(p)}=1_x$.
1289:   Thus, $\alpha\leq_x \beta$ and $\beta\leq_x \alpha$, which implies $\alpha=\beta$ since $(P,H)$ is a standard notion of structure.
1290: \end{proof}
1291: 
1292: As an example, this methodology gives an alternative way to express the proof of \cref{ct:functor-cat}.
1293: 
1294: \begin{eg}\label{ct:sip-functor-cat}
1295:   Let $A$ be a precategory and $B$ a category.
1296:   There is a precategory $B^{A_0}$ whose objects are functions $A_0 \to B_0$, and whose set of morphisms from $F_0:A_0 \to B_0$ to $G_0:A_0 \to B_0$ is $\prd{a:A_0} \hom_B(F_0 a, G_0 a)$.
1297:   Composition and identities are inherited directly from those in $B$.
1298:   It is easy to show that $\gamma:\hom_{B^{A_0}}(F_0, G_0)$ is an isomorphism exactly when each component $\gamma_a$ is an isomorphism, so that we have $\eqv{(F_0 \cong G_0)}{\prd{a:A_0} (F_0 a \cong G_0 a)}$.
1299:   Moreover, the map $\idtoiso : (F_0 = G_0) \to (F_0 \cong G_0)$ of $B^{A_0}$ is equal to the composite
1300:   \[ (F_0 = G_0) \longrightarrow \prd{a:A_0} (F_0 a  = G_0 a) \longrightarrow \prd{a:A_0} (F_0 a \cong G_0 a) \longrightarrow (F_0 \cong G_0) \]
1301:   in which the first map is an equivalence by function extensionality, the second because it is a dependent product of equivalences (since $B$ is a category), and the third as remarked above.
1302:   Thus, $B^{A_0}$ is a category.
1303: 
1304:   Now we define a notion of structure on $B^{A_0}$ for which $P(F_0)$ is the type of operations $F:\prd{a,a':A_0} \hom_A(a,a') \to \hom_B(F_0 a,F_0 a')$ which extend $F_0$ to a functor (i.e.\ preserve composition and identities).
1305:   This is a set since each $\hom_B(\blank,\blank)$ is so.
1306:   Given such $F$ and $G$, we define $\gamma:\hom_{B^{A_0}}(F_0, G_0)$ to be a homomorphism if it forms a natural transformation.\index{natural!transformation}
1307:   In \cref{ct:functor-precat} we essentially verified that this is a notion of structure.
1308:   Moreover, if $F$ and $F'$ are both structures on $F_0$ and the identity is a natural transformation from $F$ to $F'$, then for any $f:\hom_A(a,a')$ we have $F'f = F'f \circ 1_{F_0 a} = 1_{F_0 a}\circ F f = F f$.
1309:   Applying function extensionality, we conclude $F = F'$.
1310:   Thus, we have a \emph{standard} notion of structure, and so by \cref{thm:sip}, the precategory $B^A$ is a category.
1311: \end{eg}
1312: 
1313: As another example, we consider categories of structures for a first-order signature.
1314: We define a \define{first-order signature},
1315: \indexdef{first-order!signature}%
1316: \indexdef{signature!first-order}%
1317: $\Omega$, to consist of sets $\Omega_0$ and $\Omega_1$ of function symbols, $\omega:\Omega_0$, and relation symbols, $\omega:\Omega_1$, each having an arity\index{arity} $|\omega|$ that is a set.
1318: An \define{$\Omega$-structure}
1319: \indexdef{structure!Omega@$\Omega$-}%
1320: \indexsee{omega-structure@$\Omega$-structure}{structure}%
1321: $a$ consists of a set $|a|$ together with an assignment of an $|\omega|$-ary function $\omega^a:|a|^{|\omega|}\to |a|$ on $|a|$ to each function symbol, $\omega$, and an assignment of an $|\omega|$-ary relation $\omega^a$ on $|a|$, assigning a mere proposition $\omega^ax$ to each $x:|a|^{|\omega|}$, to each relation symbol.
1322: And given $\Omega$-structures $a,b$, a function $f:|a|\to |b|$ is a \define{homomorphism $a\to b$}
1323: \indexdef{homomorphism!of Omega-structures@of $\Omega$-structures}%
1324: \indexdef{structure!homomorphism of Omega@homomorphism of $\Omega$-}%
1325: if it preserves the structure; i.e.\ if for each symbol $\omega$ of the signature and each $x:|a|^{|\omega|}$,
1326: \begin{enumerate}
1327: \item $f(\omega^ax) = \omega^b(f\circ x)$ if $\omega:\Omega_0$, and
1328: \item $\omega^ax\to\omega^b(f\circ x)$ if $\omega:\Omega_1$.
1329: \end{enumerate}
1330: Note that each $x:|a|^{|\omega|}$ is a function $x:|\omega|\to |a|$ so that $f\circ x : b^\omega$.
1331: 
1332: Now we assume given a (univalent) universe $\bbU$ and a $\bbU$-small signature $\Omega$; i.e. $|\Omega|$ is a $\bbU$-small set and, for each $\omega:|\Omega|$, the set $|\omega|$ is $\bbU$-small.
1333: Then we have the category $\uset_\bbU$ of $\bbU$-small sets.  We want to define the precategory of $\bbU$-small $\Omega$-structures over $\uset_\bbU$ and use \cref{thm:sip} to show that it is a category.
1334: 
1335: We use the first order signature $\Omega$ to give us a standard notion of structure $(P,H)$ over $\uset_\bbU$.
1336: 
1337: \begin{defn}\label{defn:fo-notion-of-structure}
1338: \mbox{}
1339: \begin{enumerate}
1340: \item For each $\bbU$-small set $x$ define
1341:   \[ Px \defeq P_0x\times P_1x.\]
1342:   Here
1343:   %
1344:   \begin{align*}
1345:     P_0x &\defeq \prd{\omega:\Omega_0} x^{|\omega|}\to x, \mbox{ and } \\
1346:     P_1x &\defeq \prd{\omega:\Omega_1} x^{|\omega|}\to \propU,
1347:   \end{align*}
1348: \item For $\bbU$-small sets $x,y$ and
1349:   $\alpha:P^\omega x,\;\beta:P^\omega y,\; f:x\to y$, define
1350:   \[ H_{\alpha\beta}(f) \defeq H_{0,\alpha\beta}(f)\wedge H_{1,\alpha\beta}(f).\]
1351:   Here
1352:   \begin{align*}
1353:     H_{0,\alpha\beta}(f) &\defeq
1354:     \fall{\omega:\Omega_0}{u:x^{|\omega|}} f(\alpha u)=\;\beta(f\circ u),
1355:     \mbox{ and }\\
1356:     H_{1,\alpha\beta}(f) &\defeq
1357:     \fall{\omega:\Omega_1}{u:x^{|\omega|}} \alpha u\to\beta(f\circ u).
1358:   \end{align*}
1359: \end{enumerate}
1360: \end{defn}
1361: 
1362: It is now routine to check that $(P,H)$ is a standard notion of structure over $\uset_\bbU$ and hence we may use \cref{thm:sip} to get that the precategory $Str_{(P,H)}(\uset_\bbU)$ is a category.  It only remains to observe that this is essentially the same as the precategory of $\bbU$-small $\Omega$-structures over $\uset_\bbU$.
1363:  \index{structure!identity principle|)}
```

## 阅读与证明的边界
这两段支持结构同构必须有逆同态，而关系同态单向保持。
新文件PROOF_NOTE中的带时刻观察族、两个Bool³协议以及查询恢复定理是本轮纸笔推导；不把它们冒称书中已存在的同名定理。
