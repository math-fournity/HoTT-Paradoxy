# Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I $^{1}$ .

Von Kurt Gödel in Wien.

## 1.

Die Entwicklung der Mathematik in der Richtung zu größerer Exaktheit hat bekanntlich dazu geführt, daß weite Gebiete von ihr formalisiert wurden, in der Art, daß das Beweisen nach einigen wenigen mechanischen Regeln vollzogen werden kann. Die umfassendsten derzeit aufgestellten formalen Systeme sind das System der Principia Mathematica (PM) $^{2}$ einerseits, das Zermelo-Fraenkelsche (von J. v. Neumann weiter ausgebildete) Axiomensystem der Mengenlehre $^{3}$ andererseits. Diese beiden Systeme sind so weit, daß alle heute in der Mathematik angewendeten Beweismethoden in ihnen formalisiert, d. h. auf einige wenige Axiome und Schlußregeln zurückgeführt sind. Es liegt daher die Vermutung nahe, daß diese Axiome und Schlußregeln dazu ausreichen, alle mathematischen Fragen, die sich in den betreffenden Systemen überhaupt formal ausdrücken lassen, auch zu entscheiden. Im folgenden wird gezeigt, daß dies nicht der Fall ist, sondern daß es in den beiden angeführten Systemen sogar relativ einfache Probleme aus der Theorie der gewöhnlichen ganzen Zahlen gibt $^{4}$ , die sich aus den Axiomen nicht entscheiden lassen. Dieser Umstand liegt nicht etwa an der speziellen Natur der aufgestellten Systeme, sondern gilt für eine sehr weite Klasse formaler Systeme, zu denen insbesondere alle gehören, die aus den beiden angeführten durch Hinzufügung endlich vieler Axiome entstehen $^{5}$ , vorausgesetzt, daß durch die hinzugefügten Axiome keine falschen Sätze von der in Fußnote $^{4}$ angegebenen Art beweisbar werden.

Wir skizzieren, bevor wir auf Details eingehen, zunächst den Hauptgedanken des Beweises, natürlich ohne auf Exaktheit Anspruch zu erheben. Die Formeln eines formalen Systems (wir beschränken uns hier auf das System PM) sind äußerlich betrachtet endliche Reihen der Grundzeichen (Variable, logische Konstante und Klammern bzw. Trennungspunkte) und man kann leicht genau präzisieren, welche Reihen von Grundzeichen sinnvolle Formeln sind und welche nicht⁶). Analog sind Beweise vom formalen Standpunkt nichts anderes als endliche Reihen von Formeln (mit bestimmten angebbaren Eigenschaften). Für metamathematische Betrachtungen ist es natürlich gleichgültig, welche Gegenstände man als Grundzeichen nimmt, und wir entschließen uns dazu, natürliche Zahlen⁷) als solche zu verwenden. Dementsprechend ist dann eine Formel eine endliche Folge natürlicher Zahlen⁸) und eine Beweisfigur eine endliche Folge von endlichen Folgen natürlicher Zahlen. Die metamathematischen Begriffe (Sätze) werden dadurch zu Begriffen (Sätzen) über natürliche Zahlen bzw. Folgen von solchen⁹) und daher (wenigstens teilweise) in den Symbolen des Systems PM selbst ausdrückbar. Insbesondere kann man zeigen, daß die Begriffe „Formel“, „Beweisfigur“, „beweisbare Formel“ innerhalb des Systems PM definierbar sind, d. h. man kann z. B. eine Formel F(v) aus PM mit einer freien Variablen v (vom Typus einer Zahlenfolge) angeben¹⁰), so daß F(v) inhaltlich interpretiert besagt: v ist eine beweisbare Formel. Nun stellen wir einen unentscheidbaren Satz des Systems PM, d. h. einen Satz A, für den weder A noch non-A beweisbar ist, folgendermaßen her:

Eine Formel aus PM mit genau einer freien Variablen, u. zw. vom Typus der natürlichen Zahlen (Klasse von Klassen) wollen wir ein Klassenzeichen nennen. Die Klassenzeichen denken wir uns irgendwie in eine Folge geordnet $^{11}$ , bezeichnen das n-te mit $R(n)$ und bemerken, daß sich der Begriff „Klassenzeichen“ sowie die ordnende Relation R im System PM definieren lassen. Sei $\alpha$ ein beliebiges Klassenzeichen; mit $[\alpha;n]$ bezeichnen wir diejenige Formel, welche aus dem Klassenzeichen $\alpha$ dadurch entsteht, daß man die freie Variable durch das Zeichen für die natürliche Zahl n ersetzt. Auch die Tripel-Relation $x=[y;z]$ erweist sich als innerhalb PM definierbar. Nun definieren wir eine Klasse K natürlicher Zahlen folgendermaßen:

$$
n \varepsilon K \equiv \overline {{B e w}} [ R (n); n ] ^ {1 1 a})\tag{1}
$$

(wobei Bew x bedeutet: x ist eine beweisbare Formel). Da die Begriffe, welche im Definiens vorkommen, sämtlich in PM definierbar sind, so auch der daraus zusammengesetzte Begriff K, d. h. es gibt ein Klassenzeichen $S^{12}$ ), so daß die Formel [S; n] inhaltlich gedeutet besagt, daß die natürliche Zahl n zu K gehört. S ist als Klassenzeichen mit einem bestimmten $R(q)$ identisch, d. h. es gilt

$$
S = R (q)
$$

für eine bestimmte natürliche Zahl $q$ . Wir zeigen nun, daß der Satz $[R(q); q]^{13}$ in PM unentscheidbar ist. Denn angenommen der Satz $[R(q); q]$ wäre beweisbar, dann wäre er auch richtig, d. h. aber nach dem obigen $q$ würde zu $K$ gehören, d. h. nach (1) es würde $\overline{Bew}[R(q); q]$ gelten, im Widerspruch mit der Annahme. Wäre dagegen die Negation von $[R(q); q]$ beweisbar, so würde $n \in K$ , d. h. $Bew[R(q); q]$ gelten. $[R(q); q]$ wäre also zugleich mit seiner Negation beweisbar, was wiederum unmöglich ist.

Die Analogie dieses Schlusses mit der Antinomie Richard springt in die Augen; auch mit dem „Lügner“ besteht eine nahe Verwandtschaft $^{14}$ , denn der unentscheidbare Satz $[R(q); q]$ besagt ja, daß q zu K gehört, d. h. nach (1), daß $[R(q); q]$ nicht beweisbar ist. Wir haben also einen Satz vor uns, der seine eigene Unbeweisbarkeit behauptet $^{15}$ . Die eben auseinandergesetzte Beweismethode läßt sich offenbar auf jedes formale System anwenden, das erstens inhaltlich gedeutet über genügend Ausdrucksmittel verfügt, um die in der obigen Überlegung vorkommenden Begriffe (insbesondere den Begriff „beweisbare Formel“) zu definieren, und in dem zweitens jede beweisbare Formel auch inhaltlich richtig ist. Die nun folgende exakte Durchführung des obigen Beweises wird unter anderem die Aufgabe haben, die zweite der eben angeführten Voraussetzungen durch eine rein formale und weit schwächere zu ersetzen.

Aus der Bemerkung, daß $[R(q); q]$ seine eigene Unbeweisbarkeit behauptet, folgt sofort, daß $[R(q); q]$ richtig ist, denn $[R(q); q]$ ist ja unbeweisbar (weil unentscheidbar). Der im System PM unentscheidbare Satz wurde also durch metamathematische Überlegungen doch entschieden. Die genaue Analyse dieses merkwürdigen Umstandes führt zu überraschenden Resultaten, bezüglich der Widerspruchsfreiheitsbeweise formaler Systeme, die in Abschn. 4 (Satz XI) näher behandelt werden.

## 2.

Wir gehen nun an die exakte Durchführung des oben skizzierten Beweises und geben zunächst eine genaue Beschreibung des formalen Systems P, für welches wir die Existenz unentscheidbarer Sätze nachweisen wollen. P ist im wesentlichen das System, welches man erhält, wenn man die Peanoschen Axiome mit der Logik der PM $^{16}$ überbaut (Zahlen als Individuen, Nachfolgerrelation als undefinierten Grundbegriff).

Die Grundzeichen des Systems P sind die folgenden:

I. Konstante: „∞“ (nicht), „V“ (oder), „II“ (für alle), „O“ (Null), „f“ (der Nachfolger von), „(“, „)“ (Klammern).

II. Variable ersten Typs (für Individuen, d. h. natürliche Zahlen inklusive 0): „ $x_{1}$ “, „ $y_{1}$ “, „ $z_{1}$ “, ....

Variable zweiten Typs (für Klassen von Individuen): $x_{2}$ , $y_{2}$ , $z_{2}$ , $\ldots$ .

Variable dritten Typs (für Klassen von Klassen von Individuen): $x_{3}$ , $y_{3}$ , $z_{3}$ , $\cdots$ .

usw. für jede natürliche Zahl als Typus $^{17}$ .

Anm.: Variable für zwei- und mehrstellige Funktionen (Relationen) sind als Grundzeichen überflüssig, da man Relationen als Klassen geordneter Paare definieren kann und geordnete Paare wiederum als Klassen von Klassen, z. B. das geordnete Paar $a$ , $b$ durch $((a), (a, b))$ , wo $(x, y)$ bzw. $(x)$ die Klassen bedeuten, deren einzige Elemente $x, y$ bzw. $x$ sind $^{18}$ .

$^{16}$ Die Hinzufügung der Peanoschen Axiome ebenso wie alle anderen am System PM angebrachten Abänderungen dienen lediglich zur Vereinfachung des Beweises und sind prinzipiell entbehrlich.

$^{17}$ Es wird vorausgesetzt, daß für jeden Variablentypus abzählbar viele Zeichen zur Verfügung stehen.

$^{18}$ Auch inhomogene Relationen können auf diese Weise definiert werden, z. B. eine Relation zwischen Individuen und Klassen als eine Klasse aus Elementen der Form: $((x_{2}), ((x_{1}), x_{2}))$ . Alle in den PM über Relationen beweisbaren Sätze sind, wie eine einfache Überlegung lehrt, auch bei dieser Behandlungsweise beweisbar.

Unter einem Zeichen ersten Typs verstehen wir eine Zeichenkombination der Form:

$$
a, f a, f f a, f f f a \dots \mathbf {u s w}.
$$

wo $a$ entweder 0 oder eine Variable ersten Typs ist. Im ersten Fall nennen wir ein solches Zeichen Zahlzeichen. Für $n>1$ verstehen wir unter einem Zeichen $n$ -ten Typs dasselbe wie Variable $n$ -ten Typs. Zeichenkombinationen der Form $a(b)$ , wo $b$ ein Zeichen $n$ -ten und $a$ ein Zeichen $n+1$ -ten Typs ist, nennen wir Elementarformeln. Die Klasse der Formeln definieren wir als die kleinste Klasse $^{19}$ ), zu welcher sämtliche Elementarformeln gehören und zu welcher zugleich mit $a, b$ stets auch $\sim(a)$ , $(a) \vee (b)$ , $x\Pi(a)$ gehören (wobei $x$ eine beliebige Variable ist) $^{18a}$ . $(a) \vee (b)$ nennen wir die Disjunktion aus $a$ und $b$ , $\sim(a)$ die Negation und $x\Pi(a)$ eine Generalisation von $a$ . Satzformel heißt eine Formel, in der keine freie Variable vorkommt (freie Variable in der bekannten Weise definiert). Eine Formel mit genau $n$ -freien Individuenvariablen (und sonst keinen freien Variablen) nennen wir $n$ -stelliges Relationszeichen, für $n=1$ auch Klassenzeichen.

Unter Subst $a\binom{v}{b}$ (wo $a$ eine Formel, $v$ eine Variable und $b$ ein Zeichen vom selben Typ wie $v$ bedeutet) verstehen wir die Formel, welche aus $a$ entsteht, wenn man darin $v$ überall, wo es frei ist, durch $b$ ersetzt $^{20}$ ). Wir sagen, daß eine Formel $a$ eine Typenerhöhung einer anderen $b$ ist, wenn $a$ aus $b$ dadurch entsteht, daß man den Typus aller in $b$ vorkommenden Variablen um die gleiche Zahl erhöht.

Folgende Formeln (I bis V) heißen Axiome (sie sind mit Hilfe der in bekannter Weise definierten Abkürzungen: ., ∃, ≡, (Ex), = 21) und mit Verwendung der üblichen Konventionen über das Weglassen von Klammern angeschrieben)22):

$$
1. \sim (f x _ {1} = 0) \quad \sim (x ^ {\prime} = 0)
$$

$$
f x _ {1} = f y _ {1} \supset x _ {1} = y _ {1} \quad z _ {i} ^ {\prime} = z _ {i} ^ {\prime}, \quad z _ {i} = z _ {i}
$$

$$
3. x _ {2} (0). x _ {1} \Pi \left(x _ {2} \left(x _ {1}\right) \supset x _ {2} \left(f x _ {1}\right)\right) = x _ {1} \Pi \left(x _ {2} \left(x _ {1}\right)\right). \quad \times_ {v ^ {\prime} (0)} f
$$

II. Jede Formel, die aus den folgenden Schemata durch Einsetzung beliebiger Formeln für p, q, r entsteht.

1. $p \vee p \supseteq p$ 3. $p \vee q \supseteq q \vee p$

2. $p \supset p \vee q$ 4. $(p \supset q) \supset (r \vee p \supset r \vee q)$ .

III. Jede Formel, die aus einem der beiden Schemata

1. $v\Pi (a)\supseteq \mathrm{Subst}a\binom {v}{c}$

$$
2. v \Pi (b \vee a) \supset b \vee v \Pi (a)
$$

dadurch entsteht, daß man für $a, v, b, c$ folgende Einsetzungen vornimmt (und in 1. die durch „Subst“ angezeigte Operation ausführt):

Für $a$ eine beliebige Formel, für $v$ eine beliebige Variable, für $b$ eine Formel, in der $v$ nicht frei vorkommt, für $c$ ein Zeichen vom selben Typ wie $v$ , vorausgesetzt, daß $c$ keine Variable enthält, welche in $a$ an einer Stelle gebunden ist, an der $v$ frei ist $^{23}$ .

IV. Jede Formel, die aus dem Schema

$$
1. (E u) (v \Pi (u (v) \equiv a))
$$

dadurch entsteht, daß man für v bzw. u beliebige Variable vom Typ n bzw. $n+1$ und für a eine Formel, die u nicht frei enthält, einsetzt. Dieses Axiom vertritt das Reduzibilitätsaxiom (Komprehensionsaxiom der Mengenlehre).

V. Jede Formel, die aus der folgenden durch Typenerhöhung entsteht (und diese Formel selbst):

$$
1. x _ {1} \Pi (x _ {2} (x _ {1}) \equiv y _ {2} (x _ {1})) \supset x _ {2} = y _ {2}.
$$

Dieses Axiom besagt, daß eine Klasse durch ihre Elemente vollständig bestimmt ist.

Eine Formel c heißt unmittelbare Folge aus a und b (bzw. aus a), wenn a die Formel $(\infty(b))\vee(c)$ ist (bzw. wenn c die Formel $v\Pi(a)$ ist, wo v eine beliebige Variable bedeutet). Die Klasse der beweisbaren Formeln wird definiert als die kleinste Klasse von Formeln, welche die Axiome enthält und gegen die Relation „unmittelbare Folge“ abgeschlossen ist $^{24}$ .

Wir ordnen nun den Grundzeichen des Systems P in folgender Weise eineindeutig natürliche Zahlen zu:

Über formal unentscheidbare Sätze der Principia Mathematica etc.

$$
\begin{array}{l l} \text {,0"...1} & \text {,V"...7} \\ \text {,f"...3} & \text {,II"...9} \\ \text {,∞"...5} & \end{array} \quad \begin{array}{l l} \text {,("...11} \\ \text {,")"...13} \\ \text {,} \end{array}
$$

ferner den Variablen n-ten Typs die Zahlen der Form $p^{n}$ (wo p eine Primzahl >13 ist). Dadurch entspricht jeder endlichen Reihe von Grundzeichen (also auch jeder Formel) in eineindeutiger Weise eine endliche Reihe natürlicher Zahlen. Die endlichen Reihen natürlicher Zahlen bilden wir nun (wieder eineindeutig) auf natürliche Zahlen ab, indem wir der Reihe $n_{1}, n_{2}, \ldots, n_{k}$ die Zahl $2^{n_{1}}, 3^{n_{2}} \ldots p_{k}^{nk}$ entsprechen lassen, wo $p_{k}$ die k-te Primzahl (der Größe nach) bedeutet. Dadurch ist nicht nur jedem Grundzeichen, sondern auch jeder endlichen Reihe von solchen in eineindeutiger Weise eine natürliche Zahl zugeordnet. Die dem Grundzeichen (bzw. der Grundzeichenreihe) a zugeordnete Zahl bezeichnen wir mit $\Phi(a)$ . Sei nun irgend eine Klasse oder Relation $R(a_{1}, a_{2} \ldots a_{n})$ zwischen Grundzeichen oder Reihen von solchen gegeben. Wir ordnen ihr diejenige Klasse (Relation) $R'(x_{1}, x_{2} \ldots x_{n})$ zwischen natürlichen Zahlen zu, welche dann und nur dann zwischen $x_{1}, x_{2} \ldots x_{n}$ besteht, wenn es solche $a_{1}, a_{2} \ldots a_{n}$ gibt, daß $x_{i} = \Phi(a_{i})$ (i = 1, 2, ... n) und $R(a_{1}, a_{2} \ldots a_{n})$ gilt. Diejenigen Klassen und Relationen natürlicher Zahlen, welche auf diese Weise den bisher definierten metamathematischen Begriffen, z. B. „Variable“, „Formel“, „Satzformel“, „Axiom“, „beweisbare Formel“ usw. zugeordnet sind, bezeichnen wir mit denselben Worten in Kursivschrift. Der Satz, daß es im System P unentscheidbare Probleme gibt, lautet z. B. folgendermaßen: Es gibt Satzformeln a, so daß weder a noch die Negation von a beweisbare Formeln sind.

Wir schalten nun eine Zwischenbetrachtung ein, die mit dem formalen System $P$ vorderhand nichts zu tun hat, und geben zunächst folgende Definition: Eine zahlentheoretische Funktion $^{25)}$ $\varphi(x_1, x_2 \ldots x_n)$ heißt rekursiv definiert aus den zahlentheoretischen Funktionen $\psi(x_1, x_2 \ldots x_{n-1})$ und $\mu(x_1, x_2 \ldots x_{n+1})$ , wenn für alle $x_2 \ldots x_n$ , $k^{26}$ folgendes gilt:

$$
\begin{array}{l} \varphi (0, x _ {2} \dots x _ {n}) = \psi (x _ {2} \dots x _ {n}) \\ \varphi (k + 1, x _ {2} \dots x _ {n}) = \mu (k, \varphi (k, x _ {2} \dots x _ {n}), x _ {2} \dots x _ {n}). \end{array}
$$

[Unreadable]

(2)

Eine zahlentheoretische Funktion $\varphi$ heißt rekursiv, wenn es eine endliche Reihe von zahlentheor. Funktionen $\varphi_{1},\varphi_{2}\ldots\varphi_{n}$ gibt, welche mit $\varphi$ endet und die Eigenschaft hat, daß jede Funktion $\varphi_{k}$ der Reihe entweder aus zwei der vorhergehenden rekursiv definiert ist oder aus irgend welchen der vorhergehenden durch Einsetzung entsteht $^{27}$ oder schließlich eine Konstante oder die Nachfolgerfunktion $x+1$ ist. Die Länge der kürzesten Reihe von $\varphi_{i}$ , welche zu einer rekursiven Funktion $\varphi$ gehört, heißt ihre Stufe. Eine Relation zwischen natürlichen Zahlen $R(x_{1}\ldots x_{n})$ heißt rekursiv $^{28}$ , wenn es eine rekursive Funktion $\varphi(x_{1}\ldots x_{n})$ gibt, so daß für alle $x_{1}, x_{2} \ldots x_{n}$

$$
R \left(x _ {1} \dots x _ {n}\right) \sim [ \varphi (x _ {1} \dots x _ {n}) = 0 ] ^ {2 9}).
$$

Es gelten folgende Sätze:

I. Jede aus rekursiven Funktionen (Relationen) durch Einsetzung rekursiver Funktionen an Stelle der Variablen entstehende Funktion (Relation) ist rekursiv; ebenso jede Funktion, die aus rekursiven Funktionen durch rekursive Definition nach dem Schema (2) entsteht.

II. Wenn R und S rekursive Relationen sind, dann auch $\overline{R}, R \vee S$ (daher auch $R \& S$ ).

III. Wenn die Funktionen $\varphi(x), \psi(y)$ rekursiv sind, dann auch die Relation: $\varphi(x) = \psi(y)^{30}$ .

IV. Wenn die Funktion $\varphi(x)$ und die Relation $R(x, y)$ rekursiv sind, dann auch die Relationen $S, T$

$$
\begin{array}{l}S (\mathfrak {x}, \mathfrak {y}) \sim (E x) [ x \leq \varphi (\mathfrak {x}) \&R (x, \mathfrak {y}) ]\\T (\mathfrak {x}, \mathfrak {y}) \sim (x) [ x \leq \varphi (\mathfrak {x}) \rightarrow R (x, \mathfrak {y}) ]\end{array}
$$

sowie die Funktion $\psi$

$$
\psi (\mathfrak {x}, \mathfrak {y}) = \varepsilon x [ x \leq \varphi (\mathfrak {x}) \& R (x, \mathfrak {y}) ],
$$

wobei $x F(x)$ bedeutet: Die kleinste Zahl $x$ , für welche $F(x)$ gilt und 0, falls es keine solche Zahl gibt.

Satz I folgt unmittelbar aus der Definition von „rekursiv“. Satz II und III beruhen darauf, daß die den logischen Begriffen —, ∨, = entsprechenden zahlentheoretischen Funktionen

$$
\tilde {\alpha} (x), \stackrel {\gamma^ {\prime}} {\beta} (x, y), \stackrel {=} {\gamma} (x, y)
$$

nämlich:

$$
\alpha (0) = 1; \alpha (x) = 0 \text {   für   } x \neq 0
$$

$\beta (0,x) = \beta (x,0) = 0;\beta (x,y) = 1,\text{wenn} x,y\text{beide}\neq 0\text{sind}$

Über formal unentscheidbare Sätze der Principia Mathematica etc.

$$
\gamma (x, y) = 0, \text {   wenn   } x = y; \gamma (x, y) = 1, \text {   wenn   } x \neq y
$$

rekursiv sind, wie man sich leicht überzeugen kann. Der Beweis für Satz IV ist kurz der folgende: Nach der Voraussetzung gibt es ein rekursives $\rho(x,\mathfrak{y})$ , so daß:

$$
R (x, \mathfrak {y}) \sim [ \rho (x, \mathfrak {y}) = 0 ].
$$

Wir definieren nun nach dem Rekursionsschema (2) eine Funktion $\chi(x, y)$ folgendermaßen:

$$
\begin{array}{c} \chi (0, \mathfrak {y}) = 0 \\ \chi (n + 1, \mathfrak {y}) = (n + 1). a + \chi (n, \mathfrak {y}). \alpha (a) ^ {3 1}) \end{array}
$$

$$
a = \alpha [ \alpha (\rho (0, \mathfrak {y})) ]. \alpha [ \rho (n + 1, \mathfrak {y}) ]. \alpha [ \chi (n, \mathfrak {y}) ].
$$

$\chi(n+1,\mathfrak{y})$ ist daher entweder $=n+1$ (wenn $a=1$ ) oder $=\chi(n,\mathfrak{y})$ (wenn $a=0$ ) $^{32}$ ). Der erste Fall tritt offenbar dann und nur dann ein, wenn sämtliche Faktoren von $a$ 1 sind, d. h. wenn gilt:

$$
\overline {{{R}}} (0, \mathfrak {y}) \& R (n + 1, \mathfrak {y}) \& [ \chi (n, \mathfrak {y}) = 0 ].
$$

Daraus folgt, daß die Funktion $\chi(n,\mathfrak{y})$ (als Funktion von $n$ betrachtet) 0 bleibt bis zum kleinsten Wert von $n$ , für den $R(n,\mathfrak{y})$ gilt, und von da ab gleich diesem Wert ist (falls schon $R(0,\mathfrak{y})$ gilt, ist dem entsprechend $\chi(n,\mathfrak{y})$ konstant und $=0$ ). Demnach gilt:

$$
\begin{array}{l} \psi (\mathfrak {x}, \mathfrak {y}) = \chi (\varphi (\mathfrak {x}), \mathfrak {y}) \\ S (\mathfrak {x}, \mathfrak {y}) \sim R [ \psi (\mathfrak {x}, \mathfrak {y}), \mathfrak {y} ] \end{array}
$$

Die Relation T läßt sich durch Negation auf einen zu S analogen Fall zurückführen, womit Satz IV bewiesen ist.

Die Funktionen $x + y$ , $x \cdot y$ , $x^y$ , ferner die Relationen $x < y$ , $x = y$ sind, wie man sich leicht überzeugt, rekursiv und wir definieren nun, von diesen Begriffen ausgehend, eine Reihe von Funktionen (Relationen) 1—45, deren jede aus den vorhergehenden mittels der in den Sätzen I bis IV genannten Verfahren definiert ist. Dabei sind meistens mehrere der nach Satz I bis IV erlaubten Definitionsschritte in einen zusammengefaßt. Jede der Funktionen (Relationen) 1—45, unter denen z. B. die Begriffe „Formel“, „Axiom“, „unmittelbare Folge“ vorkommen, ist daher rekursiv.

1. $x / y \equiv (Ez)[z \leq x \& x = y, z]^{33})$

x ist teilbar durch $y^{34}$ ).

2. Prim $(x) \equiv (\overline{Ez})$ $[z \leq x \& z \neq 1 \& z \neq x \& x/z] \& x > 1$ x ist Primzahl.

3. $0Prx\equiv 0$

$(n + 1)Prx \equiv \mathfrak{e}y[y \leq x \& \operatorname{Prim}(y) \& x / y \& y > nPrx]$ $nPrx$ ist die $n$ -te (der Größe nach) in $x$ enthaltene Primzahl $^{34a}$ ).

4. $0! \equiv 1$

$$
(n + 1)! \equiv (n + 1). n!
$$

$$
P r (n + 1) \equiv \varepsilon y [ y \leq \{P r (n) \}! + 1
$$

$Pr(n)$ ist die $n$ -te Primzahl (der Größe nach).

6. $n Gl x \equiv \varepsilon y$ $[y \leq x \& x / (n Pr x)^y \& x / (n Pr x)^{y+1}]$ $n Gl x$ ist das $n$ -te Glied der der Zahl $x$ zugeordneten Zahlenreihe (für $n > 0$ und $n$ nicht größer als die Länge dieser Reihe).

$$
l (x) \equiv \varepsilon y [ y \leq x \& y P r x > 0 \& (y + 1) P r x = 0 ]
$$

$l(x)$ ist die Länge der x zugeordneten Zahlenreihe.

$$
x * y \equiv \varepsilon z \{z \leq [ P r (l (x) + l (y)) ] ^ {x + y} \&
$$

x \* y entspricht der Operation des „Aneinanderfügens“ zweier endlicher Zahlenreihen.

9. $R(x)\equiv 2^{x}$

$R(x)$ entspricht der nur aus der Zahl x bestehenden Zahlenreihe (für x > 0).

$$
1 0. E (x) \equiv R (1 1) * x * R (1 3)
$$

$E(x)$ entspricht der Operation des „Einklammerns“ [11 und 13 sind den Grundzeichen „(“ und „)“ zugeordnet].

11. $n\operatorname {Var}x\equiv (Ez)[13 <   z\leq x\& \operatorname {Prim}(z)\& x = z^{n}]\& n\neq 0$

x ist eine Variable n-ten Typs.

12. $\operatorname{Var}(x) \equiv (En) [n \leq x \& n \operatorname{Var} x]$

x ist eine Variable.

13. Neg $(x) \equiv R(5) * E(x)$

Neg (x) ist die Negation von x.

Über formal unentscheidbare Sätze der Principia Mathematica etc.

14. $x$ Dis $y \equiv E(x) * R(7) * E(y)$

x Dis y ist die Disjunktion aus x und y.

15. $x$ Gen $y \equiv R(x) * R(9) * E(y)$

x Gen y ist die Generalisation von y mittels der Variablen x (vorausgesetzt, daß x eine Variable ist).

16. $0Nx \equiv x$

$(n + 1)Nx \equiv R(3) * nNx$

n N x entspricht der Operation: „n-maliges Vorsetzen des Zeichens, $f'$ vor $x''$ .

17. $Z(n)\equiv nN[R(1)]$

Z (n) ist das Zahlzeichen für die Zahl n.

18. $\operatorname{Typ}_1'(x) \equiv (Em, n) \{m, n \leq x \& [m = 1 \vee 1 \text{ Var } m] \& x = n N [R(m)]\}^{34b}$

x ist Zeichen ersten Typs.

19. $\operatorname{Typ}_n(x) \equiv [n = 1 \& \operatorname{Typ}_1'(x)] \lor [n > 1 \& (Ev)\{v \leq x \& n \operatorname{Var} v \& x = R(v)\}]$

x ist Zeichen n-ten Typs.

20. $Elf(x) \equiv (E y, z, n) [y, z, n \leq x \& \text{Typ}_n(y) \& \text{Typ}_{n+1}(z) \& x = z * E(y)]$

x ist Elementarformel.

21. $Op(x y z) \equiv x = \text{Neg}(y) \vee x = y \text{ Dis } z \vee (E v) [v \leq x \& \text{Var}(v) \& x = v \text{ Gen } y]$

22. $FR(x) \equiv (n)\{0 < n \leq l(x) \to Elf(nGlx) \vee (Ep,q)[0 < p,q < n\& Op(nGlx,pGlx,qGlx)]\}$ & $l(x) > 0$

x ist eine Reihe von Formeln, deren jede entweder Elementarformel ist oder aus den vorhergehenden durch die Operationen der Negation, Disjunktion, Generalisation hervorgeht.

23. Form $(x) \equiv (En)\{n \leq (Pr[l(x)^2])^{x} [l(x)]^2$

x ist Formel (d. h. letztes Glied einer Formelreihe n).

24. $v\operatorname {Geb}n,x\equiv \operatorname {Var}(v)\& \operatorname {Form}(x)\&$

$$
(E a, b, c) [ a, b, c \leq x \& x = a * (v \text { Gen } b) * c
$$

& Form (b) & l (a) + 1 ≤ n ≤ l (a) + l (v Gen b)]

Die Variable v ist in x an n-ter Stelle gebunden.

25. $v$ Fr $n$ , $x \equiv \operatorname{Var}(v) \& \operatorname{Form}(x) \& v = n G l x \&$

$$
n \leq l (x) \& v \text {   Geb   } n, x
$$

Die Variable v ist in x an n-ter Stelle frei.

26. $vFrx\equiv (En)[n\leq l(x)\& vFrn,x]$

v kommt in x als freie Variable vor.

27. $Su x \binom{n}{y} \equiv \varepsilon z \{z \leq [Pr(l(x) + l(y))]^{x+y} \& [(Eu, v) u, v \leq x \&$

$$
x = u * R (n G l x) \quad v \& z = u * y * v \& n = l (u) + 1 ] \}
$$

$Su x \binom{n}{y}$ entsteht aus $x$ , wenn man an Stelle des $n$ -ten Gliedes von $x y$ einsetzt (vorausgesetzt, daß $0 < n \leq l(x)$ ).

28. 0 St v, x ≡ ε n {n ≤ l (x) & v Fr n, x

$$
\& \overline {{(E p)}} [ n <   p \leq l (x) \& v F r p, x ] \}
$$

$$
(k + 1) S t v, x \equiv \varepsilon n \{n <   k S t v, x \& v F r n, x
$$

$$
\& \overline {{(E p)}} [ n <   p <   k S t v, x \& v F r p, x ] \}
$$

k St v, x ist die $k + 1$ -te Stelle in x (vom Ende der Formel x an gezählt), an der v in x frei ist (und 0, falls es keine solche Stelle gibt).

$$
2 9. A (v, x) \equiv \varepsilon n \{n \leq l (x) \& n S t v, x = 0 \}
$$

A (v, x) ist die Anzahl der Stellen, an denen v in x frei ist.

30. $Sb_{0}(x_{y}^{v})\equiv x$

$$
S b _ {k + 1} \left(x _ {y} ^ {v}\right) \equiv S u \left[ S b _ {k} \left(x _ {y} ^ {v}\right) \right] \binom {k S t v, x} {y}
$$

$$
3 1. S b \left(x _ {y} ^ {v}\right) \equiv S b _ {A (v, x)} \left(x _ {y} ^ {v}\right) ^ {3 6})
$$

$Sb(x_{y}^{v})$ ist der oben definierte Begriff-Subst $a(b)^{37}$ .

32. $x$ Imp $y \equiv [\mathrm{Neg}(x)]$ Dis $y$

$$
x \text {   Con   } y \equiv \text { Neg   } \{[ \text { Neg   } (x) ] \text {   Dis   } [ \text { Neg   } (y) ] \}
$$

$$
x \text { Aeq } y \equiv (x \text { Imp } y) \text { Con } (y \text { Imp } x)
$$

$$
v \mathrm{Ex} y \equiv \operatorname{Neg} \left\{v \operatorname{Gen} [ \operatorname{Neg} (y) ] \right\}
$$

$$
3 3. n T h x \equiv \varepsilon y \{y \leq x ^ {(x ^ {n})} \&(k) [ k \leq l (x) - \rightarrow
$$

$$
(k G l x \leq 1 3 \& k G l y = k G l x) \vee
$$

$$
(k G l x \overline {{>}} 1 3 \& k G l y = k G l x. [ 1 P r (k G l x) ] ^ {n}) ]
$$

n Th x ist die n-te Typenerhöhung von x (falls x und n Th x Formeln sind).

Den Axiomen I, 1 bis 3 entsprechen drei bestimmte Zahlen, die wir mit $z_{1}, z_{2}, z_{3}$ bezeichnen, und wir definieren:

$$
Z - A x (x) \equiv (x = z _ {1} \vee x = z _ {2} \vee x = z _ {3})
$$

Über formal unentscheidbare Sätze der Principia Mathematica etc.

35. $A_{1} - Ax(x)\equiv (Ey)[y\leq x\& \operatorname {Form}(y)\&$ $x = (y\operatorname {Dis}y)\operatorname {Imp}y]$

x ist eine durch Einsetzung in das Axiomenschema II, 1 entstehende Formel. Analog werden $A_{2}-Ax$ , $A_{3}-Ax$ , $A_{4}-Ax$ entsprechend den Axiomen II, 2 bis 4 definiert.

$$
\begin{array}{l} 3 6. A - A x (x) \equiv A _ {1} - A x (x) \vee A _ {2} - A x (x) \vee A _ {3} - A x (x) \vee \\ \quad \bigvee A _ {4} - A x (x) \end{array}
$$

x ist eine durch Einsetzung in ein Aussagenaxiom entstehende Formel.

37. $Q(z,y,v)\equiv \overline{(En,m,w)}$ $[n\leq l(y)\& m\leq l(z)\& w\leq z\&$ $w = mGlz\& w\mathrm{Geb}n,y\& vFrn,y]$

z enthält keine Variable, die in y an einer Stelle gebunden ist, an der v frei ist.

$$
\begin{array}{l} 3 8. L _ {1} \cdot A x (x) \equiv (E v, y, z, n) \{v, y, z, n \leq x \& n \text { Var } v \& \\ \quad \operatorname{Typ} _ {n} (z) \& \text { Form } (y) \& Q (z, y, v) \& \\ \quad x = (v \text { Gen } y) \text { Imp } [ S b (y ^ {v}) ] \} \end{array}
$$

x ist eine aus dem Axiomenschema III, 1 durch Einsetzung entstehende Formel.

$$
\begin{array}{l} 3 9. L _ {2} - A x (x) \equiv (E v, q, p) \{v, q, p \leq x \& \operatorname{Var} (v) \& \operatorname{Form} (p) \\ \& v F r p \& \operatorname{Form} (q) \& \\ x = [ v \operatorname{Gen} (p \operatorname{Dis} q) ] \operatorname{Imp} [ p \operatorname{Dis} (v \operatorname{Gen} q) ] \} \end{array}
$$

x ist eine aus dem Axiomenschema III, 2 durch Einsetzung entstehende Formel.

$$
\begin{array}{l} 4 0. R - A x (x) \equiv (E u, v, y, n) [ u, v, y, n \leq x \& n \operatorname{Var} v \& \\ (n + 1) \operatorname{Var} u \& u F r y \& \operatorname{Form} (y) \& \\ x = u \operatorname{Ex} \left\{v \operatorname{Gen} \left[ [ R (u) * E (R (v)) ] \operatorname{Aeq} y ] \right] \right\} \end{array}
$$

x ist eine aus dem Axiomenschema IV, 1 durch Einsetzung entstehende Formel.

Dem Axiom V, 1 entspricht eine bestimmte Zahl $z_{4}$ und wir definieren:

$$
4 1. M - A x (x) \equiv (E n) [ n \leq x \& x = n T h z _ {4} ].
$$

42. $Ax(x) \equiv Z - Ax(x) \vee A - Ax(x) \vee L_1 - Ax(x) \vee L_2 - Ax(x) \vee R - Ax(x) \vee M - Ax(x)$ $x$ ist ein $Axiom$ .

43. $Fl(x y z) \equiv y = z \operatorname{Imp} x \vee (Ev)[v \leq x \& \operatorname{Var}(v) \& x = v \operatorname{Gen} y]$

x ist unmittelbare Folge aus y und z.

$$
\begin{array}{l}4 4. B w (x) \equiv (n) \left\{0 <   n \leq l (x) \rightarrow A x (n G l x) \vee \right.\\\left. \right. (E p, q) [ 0 <   p, q <   n \&F l (n G l x, p G l x, q G l x) ] \left. \right\}\\\&l (x) > 0\end{array}
$$

x ist eine Beweisfigur (eine endliche Folge von Formeln, deren jede entweder Axiom oder unmittelbare Folge aus zwei der vorhergehenden ist).

45. $x B y \equiv B w(x) \& [l(x)] G l x = y$

x ist ein Beweis für die Formel y.

46. Bew $(x) \equiv (Ey)yBx$

x ist eine beweisbare Formcl. [Bew (x) ist der einzige unter den Begriffen 1—46, von dem nicht behauptet werden kann, er sei rekursiv.]

Die Tatsache, die man vage so formulieren kann: Jede rekursive Relation ist innerhalb des Systems P (dieses inhaltlich gedeutet) definierbar, wird, ohne auf eine inhaltliche Deutung der Formeln aus P Bezug zu nehmen, durch folgenden Satz exakt ausgedrückt:

Satz V: Zu jeder rekursiven Relation $R(x_{1}\ldots x_{n})$ gibt es ein $n$ -stelliges Relationszeichen $r$ (mit den freien Variablen $^{38}$ ) $u_{1}, u_{2} \ldots u_{n}$ ), so daß für alle Zahlen- $n$ -tupel ( $x_{1} \ldots x_{n}$ ) gilt:

$$
R (x _ {1} \dots x _ {n}) \rightarrow \operatorname{Bew} \left[ S b \left(r ^ {u _ {1}} \dots u _ {n} Z (x _ {1}) \dots Z (x _ {n})\right)\right]\tag{3}
$$

$$
\overline {{R}} (x _ {1} \dots x _ {n}) \rightarrow \operatorname{Bew} \left[ \operatorname{Neg} S b \left(r\begin{array}{c c c c}u _ {1}&\dots&\dots&u _ {n}\\Z (x _ {1})&\dots&Z (x _ {n})\end{array}\right)\right]\tag{4}
$$

Wir begnügen uns hier damit, den Beweis dieses Satzes, da er keine prinzipiellen Schwierigkeiten bietet und ziemlich umständlich ist, in Umrissen anzudeuten $^{39}$ . Wir beweisen den Satz für alle Relationen $R(x_{1}\ldots x_{n})$ der Form: $x_{1}=\varphi(x_{2}\ldots x_{n})^{40}$ (wo $\varphi$ eine rekursive Funktion ist) und wenden vollständige Induktion nach der Stufe von $\varphi$ an. Für Funktionen erster Stufe (d.h. Konstante und die Funktion $x+1$ ) ist der Satz trivial. Habe also $\varphi$ die m-te Stufe. Es entsteht aus Funktionen niedrigerer Stufe $\varphi_{1}\ldots\varphi_{k}$ durch die Operationen der Einsetzung oder der rekursiven Definition. Da für $\varphi_{1}\ldots\varphi_{k}$ nach induktiver Annahme bereits alles bewiesen ist, gibt es zugehörige Relationszeichen $r_{1}\ldots r_{k}$ , so daß (3), (4) gilt. Die Definitionsprozesse, durch die $\varphi$ aus $\varphi_{1}\ldots\varphi_{k}$ entsteht (Einsetzung und rekursive Definition), können sämtlich im System P formal nachgebildet werden. Tut man dies, so erhält man aus $r_{1} \ldots r_{k}$ ein neues Relationszeichen $r^{41}$ ), für welches man die Geltung von (3), (4) unter Verwendung der induktiven Annahme ohne Schwierigkeit beweisen kann. Ein Relationszeichen $r$ , welches auf diesem Wege einer rekursiven Relation zugeordnet ist $^{42}$ ), soll rekursiv heißen.

Wir kommen nun ans Ziel unserer Ausführungen. Sei x eine beliebige Klasse von Formeln. Wir bezeichnen mit Flg (x) (Folgerungsmenge von x) die kleinste Menge von Formeln, die alle Formeln aus x und alle Axiome enthält und gegen die Relation „unmittelbare Folge“ abgeschlossen ist. x heißt ω-widerspruchsfrei, wenn es kein Klassenzeichen a gibt, so daß:

$$
(n) \left[ S b \left(a \begin{array}{c} v \\ Z (n) \end{array} \right) \varepsilon \operatorname{Flg} (\varkappa) \right] \& \left[ \operatorname{Neg} (v \text {   Gen   } a) \right] \varepsilon \operatorname{Flg} (\varkappa)
$$

wobei v die freie Variable des Klassenzeichens a ist.

Jedes ω-widerspruchsfreie System ist selbstverständlich auch widerspruchsfrei. Es gilt aber, wie später gezeigt werden wird, nicht das Umgekehrte.

Das allgemeine Resultat über die Existenz unentscheidbarer Sätze lautet:

Satz VI: Zu jeder ω-widerspruchsfreien rekursiven Klasse x von Formeln gibt es rekursive Klassenzeichen r, so daß weder v Gen r noch Neg (v Gen r) zu Flg (x) gehört (wobei v die freie Variable aus r ist).

Beweis: Sei x eine beliebige rekursive ω-widerspruchsfreie Klasse von Formeln. Wir definieren:

$$
B w _ {x} (x) \equiv (n) [ n \leq l (x) \rightarrow A x (n G l x) \vee (n G l x) \varepsilon x \vee\tag{5}
$$

$$
(E p, q) \{0 <   p, q <   n \& F l (n G l x, p G l x, q G l x) \} ] \& l (x) > 0
$$

(vgl. den analogen Begriff 44)

$$
x B _ {x} y \equiv B w _ {x} (x) \& [ l (x) ] G l x = y\tag{6}
$$

$$
\operatorname{Bew} _ {\varkappa} (x) \equiv (E y) y B _ {\varkappa} x\tag{6·1}
$$

(vgl. die analogen Begriffe 45, 46).

Es gilt offenbar:

$$
(x) \left[ \operatorname{Bew} _ {\varkappa} (x) \sim x \in \operatorname{Flg} (\varkappa) \right]\tag{7}
$$

$$
(x) [ \operatorname{Bew} (x) \rightarrow \operatorname{Bew} _ {\varkappa} (x) ]\tag{8}
$$

Nun definieren wir die Relation:

$$
Q (x, y) \equiv x B _ {n} \left[ S b \left(y \frac {1 9}{Z (y)}\right) \right].\tag{8·1}
$$

Da $xB_{\kappa}y$ [nach (6), (5)] und $Sb\left(y\frac{19}{Z(y)}\right)$ (nach Def. 17, 31)

rekursiv sind, so auch $Q(xy)$ . Nach Satz V und (8) gibt es also ein Relationszeichen $q$ (mit den freien Variablen 17, 19), so daß gilt:

$$
\overline {{x B _ {\times} \left[ S b \left(y \frac {1 9}{Z (y)}\right)\right]}} \rightarrow \operatorname{Bew} _ {\times} \left[ S b \left(q \frac {1 7}{Z (x)} \frac {1 9}{Z (y)}\right)\right]\tag{9}
$$

$$
x B _ {n} \left[ S b \left(y _ {Z (y)} ^ {1 9}\right)\right]\rightarrow \operatorname{Bew} _ {n} \left[ \operatorname{Neg} S b \left(q _ {Z (x)} ^ {1 7} Z (y)\right)\right]\tag{10}
$$

Wir setzen:

$$
p = 1 7 \text {   Gen   } q\tag{11}
$$

(p ist ein Klassenzeichen mit der freien Variablen 19) und

$$
r = S b \left(q _ {Z (p)} ^ {1 9}\right)\tag{12}
$$

(r ist ein rekursives Klassenzeichen mit der freien Variablen 17 $^{43}$ ). Dann gilt:

$$
\begin{array}{r l} S b \left(p \frac {1 9}{Z (p)}\right) = & S b \left([ 1 7 \text { Gen } q ] \frac {1 9}{Z (p)}\right) = 1 7 \text { Gen } S b \left(q \frac {1 9}{Z (p)}\right) \\ & = 1 7 \text { Gen } r ^ {4 4}) \end{array}\tag{13}
$$

[ wegen (11) und (12)] ferner:

$$
S b \left(q \begin{array}{c c} 1 7 & 1 9 \\ Z (x) & Z (p) \end{array} \right) = S b \left(r \begin{array}{c} 1 7 \\ Z (x) \end{array} \right)\tag{14}
$$

[nach (12)]. Setzt man nun in (9) und (10) p für y ein, so entsteht unter Berücksichtigung von (13) und (14):

$$
\overline {{x B _ {n} (1 7 \operatorname{Gen} r)}} \rightarrow \operatorname{Bew} _ {n} \left[ S b \left(r \frac {1 7}{Z (x)}\right)\right]\tag{15}
$$

$$
x B _ {n} (1 7 \text {   Gen   } r) \rightarrow \operatorname{Bew} _ {n} \left[ \operatorname{Neg} S b \left(r \frac {1 7}{Z (x)}\right)\right]\tag{16}
$$

Daraus ergibt sich:

1. 17 Gen $r$ ist nicht $x$ -beweisbar $^{45}$ ). Denn wäre dies der Fall, so gäbe es (nach 6·1) ein $n$ , so daß $n B_{x}$ (17 Gen $r$ ). Nach (16) gälte also: Bew $_{x} \left[ \text{Neg } S b \left( r \frac{17}{Z(n)} \right) \right]$ , während andererseits aus der $x$ -Beweisbarkeit von 17 Gen $r$ auch die von $S b \left( r \frac{17}{Z(n)} \right)$ folgt. $x$ wäre

also widerspruchsvoll (umsomehr ω-widerspruchsvoll).

2. Neg (17 Gen r) ist nicht x-beweisbar. Beweis: Wie eben bewiesen wurde, ist 17 Gen r nicht x-beweisbar, d. h. (nach 6·1) es gilt (n) $\overline{n B_{x}(17\text{ Gen }r)}$ . Daraus folgt nach (15) (n) Bew $_{x} \left[ S b \left( r \frac{17}{Z(n)} \right) \right]$ , was zusammen mit Bew $_{x}$ [Neg (17 Gen r)] gegen die ω-Widerspruchsfreiheit von x verstoßen würde.

17 Gen r ist also aus x unentscheidbar, womit Satz VI bewiesen ist.

Man kann sich leicht überzeugen, daß der eben geführte Beweis konstruktiv ist $^{45a}$ , d. h. es ist intuitionistisch einwandfrei folgendes bewiesen: Sei eine beliebige rekursiv definierte Klasse x von Formeln vorgelegt. Wenn dann eine formale Entscheidung (aus x) für die (effektiv aufweisbare) Satzformel 17 Gen r vorgelegt ist, so kann man effektiv angeben:

1. Einen Beweis für Neg (17 Gen r).

2. Für jedes beliebige n einen Beweis für $Sb\left(r\begin{array}{c}17\\ Z(n)\end{array}\right)$ d.h eine

formale Entscheidung von 17 Gen r würde die effektive Aufweisbarkeit eines ω-Widerspruches zur Folge haben.

Wir wollen eine Relation (Klasse) zwischen natürlichen Zahlen $R(x_{1}\ldots x_{n})$ entscheidungsdefinit nennen, wenn es ein $n$ -stelliges Relationszeichen $r$ gibt, so daß (3) und (4) (vgl. Satz V) gilt. Insbesondere ist also nach Satz V jede rekursive Relation entscheidungsdefinit. Analog soll ein Relationszeichen entscheidungsdefinit heißen, wenn es auf diese Weise einer entscheidungsdefiniten Relation zugeordnet ist. Es genügt nun für die Existenz unentscheidbarer Sätze, von der Klasse $\kappa$ vorauszusetzen, daß sie $\omega$ -widerspruchsfrei und entscheidungsdefinit ist. Denn die Entscheidungsdefinitheit überträgt sich von $\kappa$ auf $xB_{\kappa}y$ (vgl. (5), (6)) und auf $Q(x,y)$ (vgl.

(8·1)) und nur dies wurde in obigem Beweise verwendet. Der unentscheidbare Satz hat in diesem Fall die Gestalt v Gen r, wo r ein entscheidungsdefinites Klassenzeichen ist (es genügt übrigens sogar, daß x in dem durch x erweiterten System entscheidungsdefinit ist).

Setzt man von $x$ statt $\omega$ -Widerspruchsfreiheit, bloß Widerspruchsfreiheit voraus, so folgt zwar nicht die Existenz eines unentscheidbaren Satzes, wohl aber die Existenz einer Eigenschaft ( $r$ ), für die weder ein Gegenbeispiel angebbar, noch beweisbar ist, daß sie allen Zahlen zukommt. Denn zum Beweise, daß 17 Gen $r$ nicht $x$ -beweisbar ist, wurde nur die Widerspruchsfreiheit von $x$ verwendet (vgl. S. 189) und aus $\overline{\text{Bew}_x}$ (17 Gen $r$ ) folgt nach (15), daß für jede Zahl $x$ $Sb\left(r\frac{17}{Z(x)}\right)$ , folglich für keine Zahl Neg $Sb\left(r\frac{17}{Z(x)}\right)x$ -beweisbar ist.

Adjungiert man Neg (17 Gen r) zu x, so erhält man eine widerspruchsfreie aber nicht ω-widerspruchsfreie Formelklasse x'. x' ist widerspruchsfrei, denn sonst wäre 17 Gen r x-beweisbar. x' ist aber nicht ω-widerspruchsfrei, denn wegen Bewx (17 Gen r) und

(15) gilt: (x) $\operatorname{Bew}_{\kappa} S b \left(r \begin{array}{c} 17 \\ Z(x) \end{array} \right)$ , umsomehr also: (x) $\operatorname{Bew}_{\kappa'} S b \left(r \begin{array}{c} 17 \\ Z(x) \end{array} \right)$

und anderseits gilt natürlich: Bew $_{x'}$ [Neg (17 Gen r)] $^{46}$ .

Ein Spezialfall von Satz VI ist der, daß die Klasse $\alpha$ aus endlich vielen Formeln (und ev. den daraus durch Typenerhöhung entstehenden) besteht. Jede endliche Klasse $\alpha$ ist natürlich rekursiv. Sei $a$ die größte in $\alpha$ enthaltene Zahl. Dann gilt in diesem Fall für $\alpha$ :

$$
x \in x \sim (E m, n) [ m \leq x \& n \leq a \& n \varepsilon x \& x = m T h n ]
$$

x ist also rekursiv. Das erlaubt z. B. zu schließen, daß auch mit Hilfe des Auswahlaxioms (für alle Typen) oder der verallgemeinerten Kontinuumhypothese nicht alle Sätze entscheidbar sind, vorausgesetzt, daß diese Hypothesen ω-widerspruchsfrei sind.

Beim Beweise von Satz VI wurden keine anderen Eigenschaften des Systems P verwendet als die folgenden:

1. Die Klasse der Axiome und die Schlußregeln (d. h. die Relation „unmittelbare Folge“) sind rekursiv definierbar (sobald man die Grundzeichen in irgend einer Weise durch natürliche Zahlen ersetzt).

2. Jede rekursive Relation ist innerhalb des Systems P definierbar (im Sinn von Satz V).

Daher gibt es in jedem formalen System, das den Voraussetzungen 1, 2 genügt und ω-widerspruchsfrei ist, unentscheidbare Sätze der Form (x) F(x), wo F eine rekursiv definierte Eigenschaft natürlicher Zahlen ist, und ebenso in jeder Erweiterung eines solchen

Systems durch eine rekursiv definierbare ω-widerspruchsfreie Klasse von Axiomen. Zu den Systemen, welche die Voraussetzungen 1,2 erfüllen, gehören, wie man leicht bestätigen kann, das Zermelo-Fraenkelsche und das v.Neumannsche Axiomensystem-der Mengenlehre $^{47}$ ), ferner das Axiomensystem der Zahlentheorie, welches aus den Peanoschen Axiomen, der rekursiven Definition [nach Schema (2)] und den logischen Regeln besteht $^{48}$ ). Die Voraussetzung 1. erfüllt überhaupt jedes System, dessen Schlußregeln die gewöhnlichen sind und dessen Axiome (analog wie in P) durch Einsetzung aus endlich vielen Schemata entstehen $^{48a}$ ).

## 3.

Wir ziehen nun aus Satz VI weitere Folgerungen und geben zu diesem Zweck folgende Definition:

Eine Relation (Klasse) heißt arithmetisch, wenn sie sich allein mittels der Begriffe +, . [Addition und Multiplikation, bezogen auf natürliche Zahlen $^{49}$ ] und den logischen Konstanten V, -, (x), = definieren läßt, wobei (x) und = sich nur auf natürliche Zahlen beziehen dürfen $^{50}$ . Entsprechend wird der Begriff „arithmetischer Satz“ definiert. Insbesondere sind z. B. die Relationen „größer“ und „kongruent nach einem Modul“ arithmetisch, denn es gilt:

$$
\begin{array}{c} x > y \infty (\overline {{E z}}) [ y = x + z ] \\ x \equiv y (\mathrm{mod} n) \infty (E z) [ x = y + z. n \lor y = x + z. n ] \end{array}
$$

Es gilt der

Satz VII: Jede rekursive Relation ist arithmetisch.
Wir beweisen den Satz in der Gestalt: Jede Relation der Form $x_{0}=\varphi(x_{1}\ldots x_{n})$ , wo $\varphi$ rekursiv ist, ist arithmetisch, und wenden vollständige Induktion nach der Stufe von $\varphi$ an. $\varphi$ habe die s-te Stufe (s>1). Dann gilt entweder:

$$
1. \varphi (x _ {1} \dots x _ {n}) = \rho [ \chi_ {1} (x _ {1} \dots x _ {n}), \chi_ {2} (x _ {1} \dots x _ {n}) \dots \chi_ {m} (x _ {1} \dots x _ {n}) ] ^ {5 1)}
$$

(wo ρ und sämtliche $\chi_{i}$ kleinere Stufe haben als s) oder:

$$
\begin{array}{l} 2. \varphi (0, x _ {2} \dots x _ {n}) = \psi (x _ {2} \dots x _ {n}) \\ \varphi (k + 1, x _ {2} \dots x _ {n}) = \mu [ k, \varphi (k, x _ {2} \dots x _ {n}), x _ {2} \dots x _ {n} ] \end{array}
$$

(wo $\psi, \mu$ niedrigere Stufe als $s$ haben).

Im ersten Falle gilt:

$$
\begin{array}{c} x _ {0} = \varphi (x _ {1} \dots x _ {n}) \infty (E y _ {1} \dots y _ {m}) [ R (x _ {0} y _ {1} \dots y _ {m}) \& \\ \& S _ {1} (y _ {1}, x _ {1} \dots x _ {n}) \& \dots \& S _ {m} (y _ {m}, x _ {1} \dots x _ {n}) ], \end{array}
$$

wo R bzw. $S_{i}$ die nach induktiver Annahme existierenden mit $x_{0}=\rho(y_{1}\ldots y_{m})$ bzw. $y=\chi_{i}(x_{1}\ldots x_{n})$ äquivalenten arithmetischen Relationen sind. Daher ist $x_{0}=\varphi(x_{1}\ldots x_{n})$ in diesem Fall arithmetisch.

Im zweiten Fall wenden wir folgendes Verfahren an: Man kann die Relation $x_{0}=\varphi(x_{1}\ldots x_{n})$ mit Hilfe des Begriffes „Folge von Zahlen“ $(f)^{52)}$ folgendermaßen ausdrücken:

$$
\begin{array}{r l}x _ {0} = \varphi (x _ {1} \dots x _ {n}) \sim (E f)&\left\{ \right.f _ {0} = \psi (x _ {2} \dots x _ {n}) \&(k) [ k <   x _ {1} \rightarrow \left. \right.\\&\left. \right. f _ {k + 1} = \mu (k, f _ {k}, x _ {2} \dots x _ {n}) ] \&x _ {0} = f _ {x _ {1}} \left. \right\}\end{array}
$$

Wenn $S(y, x_{2} \ldots x_{n})$ bzw. $T(z, x_{1} \ldots x_{n+1})$ die nach induktiver Annahme existierenden mit $y = \psi(x_{2} \ldots x_{n})$ bzw. $z = \mu(x_{1} \ldots x_{n+1})$ äquivalenten arithmetische Relationen sind, gilt daher:

$$
\begin{array}{r l}x _ {0} = \varphi (x _ {1} \dots x _ {n})&\sim (E f) \left\{ \right.S (f _ {0}, x _ {2} \dots x _ {n}) \&(k) [ k <   x _ {1} \rightarrow \left. \right.\\&\left. \right. T (f _ {k + 1}, k, f _ {k}, x _ {2} \dots x _ {n}) ] \&x _ {0} = f _ {x _ {1}} \left. \right\}\end{array}\tag{17}
$$

Nun ersetzen wir den Begriff „Folge von Zahlen“ durch „Paar von Zahlen“, indem wir dem Zahlenpaar n, d die Zahlenfolge $f^{(n,d)}(f_{k}^{(n,d)}=[n]_{1+(k+1)d})$ zuordnen, wobei $[n]_{p}$ den kleinsten nicht negativen Rest von n modulo p bedeutet.

## Es gilt dann der

Hilfssatz 1: Ist $f$ eine beliebige Folge natürlicher Zahlen und $k$ eine beliebige natürliche Zahl, so gibt es ein Paar von natürlichen Zahlen $n, d$ , so daß $f^{(n, d)}$ und $f$ in den ersten $k$ Gliedern übereinstimmen.

Beweis: Sei $l$ die größte der Zahlen $k, f_{0}, f_{1} \ldots f_{k-1}$ . Man bestimme $n$ so, daß:

$$
n \equiv f _ {i} [ \mathrm{mod} (1 + (i + 1) l!)) ] \text { für } i = 0, 1 \dots k - 1
$$

was möglich ist, da je zwei der Zahlen $1 + (i + 1) l!$ ( $i = 0, 1 \ldots k - 1$ ) relativ prim sind. Denn eine in zwei von diesen Zahlen enthaltene Primzahl müßte auch in der Differenz $(i_{1} - i_{2}) l!$ und daher wegen $|i_{1} - i_{2}| < l$ in $l!$ enthalten sein, was unmöglich ist. Das Zahlen-paar n, $l!$ leistet dann das Verlangte.

Da die Relation $x = [n]_{p}$ durch:

$$
x \equiv n (\mathrm{mod} p) \& x <   p
$$

definiert und daher arithmetisch ist, so ist auch die folgendermaßen definierte Relation $P(x_{0}, x_{1} \ldots x_{n})$ :

$$
\begin{array}{l}P \left(x _ {0} \dots x _ {n}\right) \equiv (E n, d) \left\{ \right.S \left([ n ] _ {d + 1}, x _ {2} \dots x _ {n}\right) ^ {\prime} \&(k) [ k <   x _ {1} \rightarrow \left. \right.\\T \left( \right.[ n ] _ {1 + d (k + 2)}, k, [ n ] _ {1 + d (k + 1)}, x _ {2} \dots x _ {n}) ] \&x _ {0} = [ n ] _ {1 + d (x _ {1} + 1)} \left. \right\}\end{array}
$$

arithmetisch, welche nach (17) und Hilfssatz 1 mit: $x_0 = \varphi(x_1 \ldots x_n)$ äquivalent ist (es kommt bei der Folge $f$ in (17) nur auf ihren Verlauf bis zum $x_1 + 1$ -ten Glied an). Damit ist Satz VII bewiesen.

Gemäß Satz VII gibt es zu jedem Problem der Form $(x) F(x)$ ( $F$ rekursiv) ein äquivalentes arithmetisches Problem und da der ganze Beweis von Satz VII sich (für jedes spezielle $F$ ) innerhalb des Systems $P$ formalisieren läßt, ist diese Äquivalenz in $P$ beweisbar. Daher gilt:

Satz VIII: In jedem der in Satz VI genannten formalen Systeme $^{53}$ gibt es unentscheidbare arithmetische Sätze.

Dasselbe gilt (nach der Bemerkung auf Seite 190) für das Axiomensystem der Mengenlehre und dessen Erweiterungen durch ω-widerspruchsfreie rekursive Klassen von Axiomen.

Wir leiten schließlich noch folgendes Resultat her:

Satz IX: In allen in Satz VI genannten formalen Systemen gibt es unentscheidbare Probleme des engeren Funktionenkalküls $^{54}$ (d. h. Formeln des engeren Funktionenkalküls, für die weder Allgemeingültigkeit noch Existenz eines Gegenbeispiels beweisbar ist) $^{55}$ .

Dies beruht auf:

Satz X: Jedes Problem der Form $(x)F(x)$ (F rekursiv) läßt sich zurückführen auf die Frage nach der Erfüllbarkeit einer Formel des engeren Funktionenkalküls (d. h. zu jedem rekursiven F kann man eine Formel des engeren Funktionenkalküls angeben, deren Erfüllbarkeit mit der Richtigkeit von $(x)F(x)$ äquivalent ist).

Zum engeren Funktionenkalkül (e. F.) rechnen wir diejenigen Formeln, welche sich aus den Grundzeichen: —, ∨, (x), =; x, y . . . (Individuenvariable) $F(x)$ , $G(xy)$ , $H(x,y,z)$ . . . (Eigenschafts- und Relationsvariable) aufbauen $^{56}$ ), wobei (x) und = sich nur auf Individuen beziehen dürfen. Wir fügen zu diesen Zeichen noch eine dritte Art von Variablen $\varphi(x)$ , $\psi(xy)$ , $\chi(xyz)$ etc. hinzu, die Gegenstandsfunktionen vertreten (d. h. $\varphi(x)$ , $\psi(xy)$ etc. bezeichnen eindeutige Funktionen, deren Argumente und Werte Individuen sind $^{57}$ ). Eine Formel, die außer den zuerst angeführten Zeichen des e. F. noch Variable dritter Art ( $\varphi(x)$ , $\psi(xy)$ . . . etc.) enthält, soll eine Formel im weiteren Sinne (i. w. S.) heißen $^{58}$ ). Die Begriffe „erfüllbar“, „allgemeingültig“ übertragen sich ohneweiters auf Formeln i. w. S. und es gilt der Satz, daß man zu jeder Formel i. w. S. A eine gewöhnliche Formel des e. F. B angeben kann, so daß die Erfüllbarkeit von A mit der von B äquivalent ist. B erhält man aus A, indem man die in A vorkommenden Variablen dritter Art $\varphi(x)$ , $\psi(xy)$ . . durch Ausdrücke der Form: (1 z) $F(zx)$ , (1 z) $G(z,xy)$ . . . ersetzt, die „beschreibenden“ Funktionen im Sinne der PM. I \* 14 auflöst und die so erhaltene Formel mit einem Ausdruck logisch multipliziert $^{59}$ ), der besagt, daß sämtliche an Stelle der $\varphi$ , $\psi$ . . gesetzte $F$ , $G$ . . hinsichtlich der ersten Leerstelle genau eindeutig sind.

Wir zeigen nun, daß es zu jedem Problem der Form $(x) F(x)$ ( $F$ rekursiv) ein äquivalentes betreffend die Erfüllbarkeit einer Formel i. w. S. gibt, woraus nach der eben gemachten Bemerkung Satz X folgt.

Da $F$ rekursiv ist, gibt es eine rekursive Funktion $\Phi(x)$ , so daß $F(x) \sim [\Phi(x) = 0]$ , und für $\Phi$ gibt es eine Reihe von Funktionen $\Phi_1, \Phi_2 \ldots \Phi_n$ , so daß: $\Phi_n = \Phi$ , $\Phi_1(x) = x + 1$ und für jedes $\Phi_k (1 < k \leq n)$ entweder:

$$
1. \left(x _ {2} \dots x _ {m}\right) \left[ \Phi_ {k} \left(0, x _ {2} \dots x _ {m}\right) = \Phi_ {p} \left(x _ {2} \dots x _ {m}\right) \right]\tag{18}
$$

$$
\begin{array}{r l} (x, x _ {2} \dots x _ {m} ^ {\prime}) & \left\{\Phi_ {k} \left[ \Phi_ {1} (x), x _ {2} \dots x _ {m} \right] = \Phi_ {q} \left[ x, \Phi_ {k} (x, x _ {2} \dots x _ {m}), x _ {2} \dots x _ {m} \right] \right\} \\ & p, q <   k \end{array}
$$

Über formal unentscheidbare Sätze der Principia Mathematica etc.

oder:

$$
\begin{array}{c} 2. (x _ {1} \dots x _ {m}) [ \Phi_ {k} (x _ {1} \dots x _ {m}) = \Phi_ {r} (\Phi_ {i _ {1}} (\underline {{x}} _ {1}) \dots \Phi_ {i _ {s}} (\underline {{x}} _ {s})) ] ^ {6 0}) \\ r <   k, i _ {v} <   k (\text { für } v = 1, 2 \dots s) \end{array}\tag{19}
$$

oder:

$$
3. \left(x _ {1} \dots x _ {m}\right) \left[ \Phi_ {k} \left(x _ {1} \dots x _ {m}\right) = \Phi_ {1} \left(\Phi_ {1} \dots \Phi_ {1} (0)\right) \right]\tag{20}
$$

Ferner bilden wir die Sätze:

$$
(x) \overline {{{\Phi_ {1} (x) = 0}}} \& (x y) [ \Phi_ {1} (x) = \Phi_ {1} (y) \longrightarrow x = y ]\tag{21}
$$

$$
(x) [ \Phi_ {n} (x) = 0 ]\tag{22}
$$

Wir ersetzen nun in allen Formeln (18), (19), (20) (für $k=2$ , $3\ldots n$ ) und in (21) (22) die Funktionen $\Phi_{i}$ durch Funktionsvariable $\varphi_{i}$ , die Zahl 0 durch eine sonst nicht vorkommende Individuenvariable $x_{0}$ und bilden die Konjunktion $C$ sämtlicher so erhaltener Formeln.

Die Formel $(Ex_{0})$ C hat dann die verlangte Eigenschaft, d. h.

1. Wenn $(x)$ [ $\Phi(x)=0$ ] gilt, ist $(Ex_{0})C$ erfüllbar, denn die Funktionen $\Phi_{1}, \Phi_{2} \ldots \Phi_{n}$ ergeben dann offenbar in $(Ex_{0})C$ für $\varphi_{1}, \varphi_{2} \ldots \varphi_{n}$ eingesetzt einen richtigen Satz.

2. Wenn $(Ex_0)C$ erfüllbar ist, gilt $(x)[\Phi (x) = 0]$ .

Beweis: Seien $\Psi_{1}, \Psi_{2} \ldots \Psi_{n}$ die nach Voraussetzung existierenden Funktionen, welche in $(Ex_{0}) C$ für $\varphi_{1}, \varphi_{2} \ldots \varphi_{n}$ eingesetzt einen richtigen Satz liefern. Ihr Individuenbereich sei $\Im$ . Wegen der Richtigkeit von $(Ex_{0}) C$ für die Funktionen $\Psi_{i}$ gibt es ein Individuum $a$ (aus $\Im$ ), so daß sämtliche Formeln (18) bis (22) bei Ersetzung der $\Phi_{i}$ durch $\Psi_{i}$ und von 0 durch $a$ in richtige Sätze (18') bis (22') übergehen. Wir bilden nun die kleinste Teilklasse von $\Im$ , welche $a$ enthält und gegen die Operation $\Psi_{1}(x)$ abgeschlossen ist. Diese Teilklasse ( $\Im'$ ) hat die Eigenschaft, daß jede der Funktionen $\Psi_{i}$ auf Elemente aus $\Im'$ angewendet wieder Elemente aus $\Im'$ ergibt. Denn für $\Psi_{1}$ gilt dies nach Definition von $\Im'$ und wegen (18'), (19'), (20') überträgt sich diese Eigenschaft von $\Psi_{i}$ mit niedrigerem Index auf solche mit höherem. Die Funktionen, welche aus $\Psi_{i}$ durch Beschränkung auf den Individuenbereich $\Im'$ entstehen, nennen wir $\Psi_{i}'$ . Auch für diese Funktion gelten sämtliche Formeln (18) bis (22) (bei der Ersetzung von 0 durch $a$ und $\Phi_{i}$ durch $\Psi_{i}'$ ).

Wegen der Richtigkeit von (21) für $\Psi_{1}^{\prime}$ und $a$ kann man die Individuen aus $3^{\prime}$ eineindeutig auf die natürlichen Zahlen abbilden u. zw. so, daß $a$ in 0 und die Funktion $\Psi_{1}^{\prime}$ in die Nachfolgerfunktion $\Phi_{1}$ übergeht. Durch diese Abbildung gehen aber sämtliche Funktionen $\Psi_{i}^{\prime}$ in die Funktionen $\Phi_{i}$ über und wegen der Richtigkeit von (22)

für $\Psi_{n}^{\prime}$ und $a$ gilt $(x)[\Phi_n(x) = 0]$ oder $(x)[\Phi (x) = 0]$ , was zu beweisen war $^{61)}$ .

Da man die Überlegungen, welche zu Satz X führen, (für jedes spezielle F) auch innerhalb des Systems P durchführen kann, so ist die Äquivalenz zwischen einem Satz der Form $(x)F(x)$ (F rekursiv) und der Erfüllbarkeit der entsprechenden Formel des e. F. in P beweisbar und daher folgt aus der Unentscheidbarkeit des einen die des anderen, womit Satz IX bewiesen ist. $^{62}$

## 4.

Aus den Ergebnissen von Abschnitt 2 folgt ein merkwürdiges Resultat, bezüglich eines Widerspruchslosigkeitsbeweises des Systems P (und seiner Erweiterungen), das durch folgenden Satz ausgesprochen wird:

Satz XI: Sei x eine beliebige rekursive widerspruchsfreie $^{63}$ ) Klasse von Formeln, dann gilt: Die Satzformel, welche besagt, daß x widerspruchsfrei ist, ist nicht x-beweisbar; insbesondere ist die Widerspruchsfreiheit von P in P unbeweisbar $^{64}$ ), vorausgesetzt, daß P widerspruchsfrei ist (im entgegengesetzten Fall ist natürlich jede Aussage beweisbar).

Der Beweis ist (in Umrissen skizziert) der folgende: Sei x eine beliebige für die folgenden Betrachtungen ein für allemal gewählte rekursive Klasse von Formeln (im einfachsten Falle die leere Klasse). Zum Beweise der Tatsache, daß 17 Gen r nicht x-beweisbar ist $^{65}$ , wurde, wie aus 1. Seite 189 hervorgeht, nur die Widerspruchsfreiheit von x benutzt, d. h. es gilt:

$$
\operatorname{Wid} (x) \longrightarrow \overline {{\operatorname{Bew} _ {x}}} (1 7 \text { Gen } r)\tag{23}
$$

d. h. nach (6·1):

$$
\operatorname{Wid} (x) \longrightarrow (x) \overline {{x B _ {x} (1 7 \text { Gen } r)}}
$$

Nach (13) ist 17 Gen $r = Sb\left(p \frac{19}{Z(p)}\right)$ und daher:

Über formal unentscheidbare Sätze der Principia Mathematica etc.

$$
\operatorname{Wid} (x) \longrightarrow (x) x B _ {x} S b \left(p \frac {1 9}{Z (p)}\right)
$$

d. h. nach (8·1):

$$
\operatorname{Wid} (x) \longrightarrow (x) Q (x, p)\tag{24}
$$

Wir stellen nun folgendes fest: Sämtliche in Abschnitt 2 $^{66}$ und Abschnitt 4 bisher definierte Begriffe (bzw. bewiesene Behauptungen) sind auch in P ausdrückbar (bzw. beweisbar). Denn es wurden überall nur die gewöhnlichen Definitions- und Beweismethoden der klassischen Mathematik verwendet, wie sie im System P formalisiert sind. Insbesondere ist x (wie jede rekursive Klasse) in P definierbar. Sei w die Satzformel, durch welche in P Wid (x) ausgedrückt wird. Die Relation Q(x,y) wird gemäß (8·1), (9), (10) durch das Relations-

zeichen $q$ ausgedrückt, folglich $Q(x,p)$ durch $r$ [da nach (12) $r_{i}^{6} =$ $= S b\left(q \frac{19}{Z(p)}\right)$ ] und der Satz (x) $Q(x,p)$ durch 17 Gen $r$ .

Wegen (24) ist also w Imp (17 Gen r) in P beweisbar ${}^{67}$ (um so mehr x-beweisbar). Wäre nun w x-beweisbar, so wäre auch 17 Gen r x-beweisbar und daraus würde nach (23) folgen, daß x nicht widerspruchsfrei ist.

Es sei bemerkt, daß auch dieser Beweis konstruktiv ist, d. h. er gestattet, falls ein Beweis aus x für w vorgelegt ist, einen Widerspruch aus x effektiv herzuleiten. Der ganze Beweis für Satz XI läßt sich wörtlich auch auf das Axiomensystem der Mengenlehre M und der klassischen Mathematik $^{68}$ ) A übertragen und liefert auch hier das Resultat: Es gibt keinen Widerspruchslosigkeitsbeweis für M bzw. A, der innerhalb von M bzw. A formalisiert werden könnte, vorausgesetzt daß M bzw. A widerspruchsfrei ist. Es sei ausdrücklich bemerkt, daß Satz XI (und die entsprechenden Resultate über M, A) in keinem Widerspruch zum Hilbertschen formalistischen Standpunkt stehen. Denn dieser setzt nur die Existenz eines mit finiten Mitteln geführten Widerspruchsfreiheitsbeweises voraus und es wäre denkbar, daß es finite Beweise gibt, die sich in P (bzw. M, A) nicht darstellen lassen.

Da für jede widerspruchsfreie Klasse x w nicht x-beweisbar ist, so gibt es schon immer dann (aus x) unentscheidbare Sätze (nämlich w), wenn Neg (w) nicht x-beweisbar ist; m. a. W. man kann in Satz VI die Voraussetzung der ω-Widerspruchsfreiheit ersetzen durch die folgende: Die Aussage „x ist widerspruchsvoll“ ist nicht x-beweisbar. (Man beachte, daß es widerspruchsfreie x gibt, für die diese Aussage x-beweisbar ist.)

Wir haben uns in dieser Arbeit im wesentlichen auf das System P beschränkt und die Anwendungen auf andere Systeme nur angedeutet. In voller Allgemeinheit werden die Resultate in einer demnächst erscheinenden Fortsetzung ausgesprochen und bewiesen werden. In dieser Arbeit wird auch der nur skizzenhaft geführte Beweis von Satz XI ausführlich dargestellt werden.

(Eingelangt: 17. XI. 1930.)