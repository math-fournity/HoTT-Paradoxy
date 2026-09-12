# R023 circle source excerpts

Local pinned upstream snapshot; not recompiled.

## HoTT/theory-schema/upstream/book-578b85cc/homotopy.tex:323-349

```tex
323: It is not too hard to define functions in both directions between $\Omega(\Sn^1)$ and \Z.
324: By specializing \cref{thm:looptothe} to $\lloop:\base=\base$, we have a function $\lloop^{\blank} : \Z \rightarrow (\id{\base}{\base})$ defined (loosely speaking) by
325: \[
326:   \lloop^n =
327:   \begin{cases}
328:     \underbrace{\lloop \ct \lloop \ct \cdots \ct \lloop}_{n}  & \text{if $n > 0$,} \\
329:     \underbrace{\opp \lloop \ct \opp \lloop \ct \cdots \ct \opp \lloop}_{-n} & \text{if $n < 0$,} \\
330:     \refl{\base} & \text{if $n = 0$.}
331: \end{cases}
332: \]
333: %
334: Defining a function $g:\Omega(\Sn^1)\to\Z$ in the other direction is a bit trickier.
335: Note that the successor function $\Zsuc:\Z\to\Z$ is an equivalence,
336: \index{successor!isomorphism on Z@isomorphism on $\Z$}%
337: and hence induces a path $\ua(\Zsuc):\Z=\Z$ in the universe \type.
338: Thus, the recursion principle of $\Sn^1$ induces a map $c:\Sn^1\to\type$ by $c(\base)\defeq \Z$ and $\apfunc c (\lloop) \defid \ua(\Zsuc)$.
339: Then we have $\apfunc{c} : (\base=\base) \to (\Z=\Z)$, and we can define $g(p)\defeq \transfib{X\mapsto X}{\apfunc{c}(p)}{0}$.
340: 
341: With these definitions, we can even prove that $g(\lloop^n)=n$ for any $n:\Z$, using the induction principle \cref{thm:sign-induction} for $n$.
342: (We will prove something more general a little later on.)
343: However, the other equality $\lloop^{g(p)}=p$ is significantly harder.
344: The obvious thing to try is path induction, but path induction does not apply to loops such as $p:(\base=\base)$ that have \emph{both} endpoints fixed!
345: A new idea is required, one which can be explained both in terms of classical homotopy theory and in terms of type theory.
346: We begin with the former.
347: 
348: 
349: \subsection{The classical proof}
```

## HoTT/theory-schema/upstream/book-578b85cc/homotopy.tex:423-456

```tex
423:   \begin{align*}
424:     \code(\base) &\defeq \Z \\
425:     \apfunc{\code}({\lloop}) &\defid \ua(\Zsuc).
426:   \end{align*}
427: \end{defn}
428: 
429: We emphasize briefly the definition of this family, since it is so different from how one usually defines covering spaces in classical homotopy theory.
430: To define a function by circle recursion, we need to find a point and a
431: loop in the codomain.  In this case, the codomain is $\type$, and the point
432: we choose is $\Z$, corresponding to our expectation that the
433: fiber of the universal cover should be the integers.  The loop we choose
434: is the successor/predecessor
435: \index{successor!isomorphism on Z@isomorphism on $\Z$}%
436: \index{predecessor!isomorphism on Z@isomorphism on $\Z$}%
437: isomorphism on $\Z$, which
438: corresponds to the fact that going around the loop in the base goes up
439: one level on the helix.  Univalence is necessary for this part of the
440: proof, because we need to convert a \emph{non-trivial} equivalence on $\Z$ into an identity.
441: 
442: We call this the fibration of ``codes'', because its elements are combinatorial data that act as codes for paths on the circle: the integer $n$ codes for the path which loops around the circle $n$ times.
443: 
444: From this definition, it is simple to calculate that transporting with
445: $\code$ takes $\lloop$ to the successor function, and
446: $\opp{\lloop}$ to the predecessor function:
447: \begin{lem} \label{lem:transport-s1-code}
448: \id{\transfib \code \lloop x} {x + 1} and
449: \id{\transfib \code {\opp \lloop} x} {x - 1}.
450: \end{lem}
451: \begin{proof}
452: For the first equation, we calculate as follows:
453: \begin{align}
454: {\transfib \code \lloop x}
455: &= \transfib {A \mapsto A} {(\ap{\code}{\lloop})} x \tag{by \cref{thm:transport-compose}}\\
456: &= \transfib {A \mapsto A} {\ua (\Zsuc)} x \tag{by computation for $\rec{\Sn^1}$}\\
```

## HoTT/theory-schema/upstream/book-578b85cc/homotopy.tex:497-538

```tex
497: We begin with the function~\eqref{eq:pi1s1-encode} that maps paths to codes:
498: \begin{defn}
499: Define $\encode : \prd{x : \Sn ^1} (\base=x) \rightarrow  \code(x)$ by
500: \[
501: \encode \: p \defeq \transfib{\code} p 0
502: \]
503: (we leave the argument $x$ implicit).
504: \end{defn}
505: Encode is defined by lifting a path into the universal cover, which
506: determines an equivalence, and then applying the resulting equivalence
507: to $0$.
508: The interesting thing about this function is that it computes a concrete
509: number from a loop on the circle, when this loop is represented using
510: the abstract groupoidal framework of homotopy type theory.  To gain an
511: intuition for how it does this, observe that by the above lemmas,
512: $\transfib \code \lloop x$ is the successor map and $\transfib \code {\opp
513:   \lloop} x$ is the predecessor map.
514: Further, $\mathsf{transport}$ is functorial (\cref{cha:basics}), so
515: $\transfib{\code} {\lloop \ct \lloop}{\blank}$ is
516: \[(\transfib \code \lloop-) \circ (\transfib \code \lloop-)\]
517: and so on.
518: Thus, when $p$ is a composition like
519: \[
520: \lloop \ct \opp \lloop \ct \lloop \ct \cdots
521: \]
522: $\transfib{\code}{p}{\blank}$ will compute a composition of functions like
523: \[
524: \Zsuc \circ \Zpred \circ \Zsuc \circ \cdots
525: \]
526: Applying this composition of functions to 0 will compute the
527: \index{winding!number}%
528: \emph{winding number} of the path --- how many times it goes around the
529: circle, with orientation marked by whether it is positive or negative,
530: after inverses have been canceled.  Thus, the computational behavior of
531: $\encode$ follows from the reduction rules for higher-inductive types and
532: univalence, and the action of $\mathsf{transport}$ on compositions and inverses.
533: 
534: Note that the instance $\encode' \defeq \encode_{\base}$ has type
535: $(\id \base \base) \rightarrow \Z$.
536: This will be one half of our desired equivalence; indeed, it is exactly the function $g$ defined in \cref{sec:pi1s1-initial-thoughts}.
537: 
538: Similarly, the function~\eqref{eq:pi1s1-decode} is a generalization of the function $\lloop^{\blank}$ from \cref{sec:pi1s1-initial-thoughts}.
```

## HoTT/theory-schema/upstream/book-578b85cc/homotopy.tex:576-645

```tex
576: \begin{lem} \label{lem:s1-decode-encode}
577: For all $x: \Sn ^1$ and $p : \id \base x$, $\id
578: {\decode_x({{\encode_x(p)}})} p$.
579: \end{lem}
580: 
581: \begin{proof}
582: By path induction, it suffices to show that
583: \narrowequation{\id {\decode_{\base}({{\encode_{\base}(\refl{\base})}})} {\refl{\base}}.}
584: But
585: \narrowequation{\encode_{\base}(\refl{\base}) \jdeq \transfib{\code}{\refl{\base}} 0 \jdeq 0,}
586: and $\decode_{\base}(0) \jdeq \lloop^ 0 \jdeq \refl{\base}$.
587: \end{proof}
588: 
589: The other direction is not much harder.
590: 
591: \begin{lem} \label{lem:s1-encode-decode} For all
592: $x: \Sn ^1$ and $c : \code(x)$, we have $\id
593: {\encode_x({{\decode_x(c)}})} c$.
594: \end{lem}
595: 
596: \begin{proof}
597: The proof is by circle induction.  It suffices to show the case for
598: \base, because the case for \lloop is a path between paths in
599: $\Z$, which is immediate because $\Z$ is a set.
600: 
601: Thus, it suffices to show, for all $n : \Z$, that
602: \[
603: \id {\encode'(\lloop^n)} {n}.
604: \]
605: The proof is by induction, using \cref{thm:sign-induction}.
606: %
607: \begin{itemize}
608: 
609: \item In the case for $0$, the result is true by definition.
610: 
611: \item In the case for $n+1$,
612: \begin{align}
613:  {\encode'(\lloop^{n+1})}
614: &= {\encode'(\lloop^{n} \ct \lloop)} \tag{by definition of $\lloop^{\blank}$} \\
615: &= \transfib{\code}{(\lloop^{n} \ct \lloop)}{0} \tag{by definition of $\encode$}\\
616: &= \transfib{\code}{\lloop}{(\transfib{\code}{\lloop^n}{0})} \tag{by functoriality}\\
617: &= {(\transfib{\code}{\lloop^n}{0})} + 1 \tag{by \cref{lem:transport-s1-code}}\\
618: &= n + 1. \tag{by the inductive hypothesis}
619: \end{align}
620: 
621: \item The case for negatives is analogous.  \qedhere
622: \end{itemize}
623: \end{proof}
624: 
625: Finally, we conclude the theorem.
626: 
627: \begin{thm}
628: There is a family of equivalences $\prd{x : \Sn ^1} (\eqv {(\base=x)} {\code(x)})$.
629: \end{thm}
630: \begin{proof}
631: The maps $\encode$ and $\decode$ are quasi-inverses by
632: \cref{lem:s1-decode-encode,lem:s1-encode-decode}.
633: \end{proof}
634: 
635: Instantiating at {\base} gives
636: \begin{cor}\label{cor:omega-s1}
637: $\eqv {\Omega(\Sn^1,\base)} {\Z}$.
638: \end{cor}
639: 
640: A simple induction shows that this equivalence takes addition to
641: composition, so that $\Omega(\Sn ^1) = \Z$ as groups.
642: 
643: \begin{cor} \label{cor:pi1s1}
644: $\id{\pi_1(\Sn ^1)} {\Z}$, while $\id{\pi_n(\Sn ^1)}0$ for $n>1$.
645: \end{cor}
```
