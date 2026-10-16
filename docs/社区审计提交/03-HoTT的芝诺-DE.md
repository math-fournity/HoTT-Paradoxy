<!-- translation:v1
source: docs/社区审计提交/03-HoTT的芝诺.md
source_sha256: bea7f03052d2e242a97b0a51e5dd22dc5371119668042a96f3181eba22b26c53
language: de
translator: Claude Opus 5.5 (AI), 2026-10-01; version 2 changes 2026-10-15
authority: the Chinese original is authoritative
-->
# Der Zenon der HoTT

[中文](03-HoTT的芝诺.md) · [Русский](03-HoTT的芝诺-RU.md) · **Deutsch** · [Français](03-HoTT的芝诺-FR.md) · [English](03-HoTT的芝诺-EN.md)

> *KI-Übersetzung (Claude Opus 5.5, 2026-10-01; die Änderungen der Version 2: 2026-10-15) des chinesischen Originals [`03-HoTT的芝诺.md`](03-HoTT的芝诺.md); maßgeblich ist das chinesische Original. Die Worte der Person, die das Projekt initiiert hat (im Folgenden: die initiierende Person), werden im chinesischen Original zitiert, jeweils gefolgt von einer gekennzeichneten Übersetzung; Code, Dateipfade und Kennungen sind unverändert.*

**Warum „dasselbe sein“ in ihrem Universum nie zur Ruhe kommt**

Auditdokument für die Gemeinschaft · Version 2 · 2026-10-15 · Repository `math-fournity/HoTT-Paradoxy`

Version 1 entstand am 2026-09-30. Version 2 ändert nur, was die Entscheidung der initiierenden Person vom 2026-10-15 verlangt: „welche Prämisse zu beschuldigen ist“ und die beiden damit verbundenen Stellen (die ersten zwei Punkte von „Was das zeigt“ und Auditfrage 3); unter „Belege“ kommt ein Theorem hinzu, das die Kontrollen zusammenfasst.

> **Für wen**: für Leserinnen und Leser außerhalb der Mathematik, die bereit sind mitzudenken, und für Mathematikerinnen und Mathematiker, die bereit sind zu prüfen.
>
> **Status**: Das Urteil, dass etwas „ungereimt“ ist, gehört der initiierenden Person; die Schlussfolgerungen sind innerhalb eines angegebenen Rahmens maschinell bewiesen (siehe „Belege“ am Ende); der Rest ist Deutung. Dieses Dokument behauptet **nicht**, dass die HoTT widersprüchlich ist, und auch nicht, dass ihre Regeln mathematisch falsch sind.
>
> **Verhältnis zum Schwesterdokument**: [02 Das Gespenst von Russells Paradoxon](02-罗素悖论的幽灵-DE.md) zeigt ein anderes Gesicht derselben Maschinenbelege, nämlich das russellsche Muster „die Theorie behandelt etwas noch nicht Festgelegtes als bereits geliefert“ (Richtung B). Dieses Dokument stellt die Lesart der initiierenden Person vom 2026-09-30 dar: in der Realität vollendbar, in der Theorie nicht (Richtung A). Die beiden teilen sich die Arbeit: Das Phänomen in der Buch-HoTT gehört zu Richtung A; das „Vollendung per Definition erklären“ in den Reparaturen gehört zu Richtung B.

## Zuerst Zenon

Von hier nach dort gehen: Man geht hinüber und ist da. Denkt man sich die Strecke aber als unendlich teilbar, kommt das „Ankommen“ nie zur Ruhe: Erst geht man die Hälfte, eine Hälfte bleibt; wieder die Hälfte, wieder bleibt eine Hälfte. Bei jedem Schritt ist man ganz sicher noch nicht da, und der Weg wird nie zu Ende gegangen. Die Schlussfolgerung ist nicht falsch, und doch sieht man auf einen Blick, dass das ungereimt ist. Der Fehler steckt in der Prämisse.

Die initiierende Person nennt diese Art von Ungereimtheit UR:

> 本来应该很简单的事情，甚至在X理论中，都做不到。

Übersetzung: „Etwas, das sehr einfach sein sollte, aber selbst in Theorie X nicht zu leisten ist.“

„Realität“ meint die erste Satzhälfte, also das, was sehr einfach sein sollte; „Paradoxon“ meint den ganzen Satz.

## Etwas, das sehr einfach sein sollte

Ob zwei Dinge dasselbe sind: In der alltäglichen Logik und Mathematik ist das eine Sache eines einzigen Satzes. Entweder sind sie es oder nicht; ein „auf welche Weise sie es sind“ gibt es nicht.

## Was die Homotopietypentheorie geändert hat, um bequem zu sein

Die Homotopietypentheorie (HoTT) hat zwei sehr verlockende Konstruktionsmerkmale.

- **Univalenz**: Isomorphe Dinge sind dasselbe Ding. Das spart viel Arbeit: Zwei Dinge mit derselben Struktur muss man nicht mehr unterscheiden, und Sätze lassen sich direkt übertragen.
- **Höhere induktive Typen**: Alle möglichen Formen (Kreise, Sphären und Formen beliebig hoher Dimension) stehen im Universum der Typen auf einmal bereit. Das ist sehr allgemein: Geometrie lässt sich direkt in der Logik betreiben.

Zusammen machen sie „dasselbe sein“ von der Sache eines Satzes zu einer geschichteten Struktur: Auf welche Weisen sind diese Dinge dasselbe? Auf welche Weisen sind diese Weisen dasselbe? Über jeder Schicht liegt eine weitere.

## Der Prozess, der genau darauf zielt

Wir haben ein ganz schlichtes Programm geschrieben, das Stufe für Stufe fragt: „Ist für die Dinge in diesem Katalog die Frage, ob sie dasselbe sind, auf dieser Stufe erledigt?“ Stufe 1 fragt „ist es die Sache eines Satzes?“; lautet die Antwort „nein“, fragt es Stufe 2; und so weiter. Bei „ja“ hält es an und meldet die Stufe. Auf jeder Stufe gibt jemand (ein Entscheider) ein „ja“ oder ein „nein“ samt Beweis, sodass das Programm jeden nächsten Schritt tun kann.

## Ergebnisse

- In einer Welt, in der „Gleichheit eine Tatsache ist, die eine einzige Prüfung entscheidet“ (ein anderer Beweisassistent, Lean, mit demselben Programm, nach denselben Gleichungen übertragen), hält das Programm, nach dem eigenen Universum gefragt, auf Stufe 1.
- In der HoTT hält das Programm, wenn die „Höhe“ der Dinge im Katalog gedeckelt ist, genau auf der Stufe, die der Deckel bestimmt.
- In der HoTT hält das Programm, nach ihrem Universum oder nach einem gewöhnlichen unendlichen Produkt gefragt, **nie an**: Jede Stufe antwortet mit einem sicheren „nein“, und über jeder Stufe liegt eine weitere. Das gilt für jeden Entscheider; es ist ein maschinell bewiesenes Theorem, nicht „es lief lange und hielt nicht an“.

Dieselbe Frage, dasselbe Programm: Ändert man nur, „was Gleichheit ist“ und „ob die Höhe eine Decke hat“, wird aus „in einem Schritt erledigt“ ein „nie erledigt“. Das ist der Zenon der HoTT: Auf jeder Stufe ist es ganz sicher noch nicht erledigt, und die Bestätigung kann nie vollendet werden.

## Die Lehrbuchantwort, und warum sie das Problem nicht beseitigt

Zenon antwortet das Lehrbuch: Nimm Grenzwerte; 1/2 + 1/4 + … ist genau 1. Hier würde das Lehrbuch sagen: Frag stattdessen nach der „Mengentrunkierung“; dort wird „Gleichheit“ zur Sache eines Satzes erklärt, und das Programm hält auf Stufe 1.

Auch das haben wir maschinell geprüft: Es hält tatsächlich auf Stufe 1. Aber es hält, weil eine Regel „Gleichheit ist die Sache eines Satzes“ erneut verkündet. Nach der Trunkierung sind die beiden Weisen, auf die Bool dasselbe ist wie es selbst (alles lassen, wie es ist, und wahr und falsch vertauschen), zu einer einzigen verschmolzen; und das Ergebnis lässt sich nie wieder in das ursprüngliche Universum zurückdecodieren. Der befragte Gegenstand ist ausgetauscht.

Der Grenzwert erklärt „angekommen“ per Definition; die Trunkierung erklärt „Gleichheit ist eine Tatsache“ per Konstruktor. Beides ist legitime Mathematik, aber keines stellt die veränderte Bedingung selbst wieder her. Sie beantworten also eine leichtere Frage und beseitigen die ursprüngliche Ungereimtheit nicht.

## Was das zeigt

- Bei Zenon ist der Angeklagte „die Position lässt sich ohne Ende unterteilen“; sein Gegenstück hier ist „**Gleichheit lässt sich ohne Ende unterteilen**“. Es setzt sich aus zwei Dingen zusammen: Gleichheit ist eine Struktur (Univalenz), und das Universum übergibt Dinge jeder Höhe auf einmal (höhere induktive Typen liefern diese Höhen).
- Die Kontrollen trennen beides: Ersetzt man „Gleichheit ist eine Struktur“ durch „Gleichheit ist eine Tatsache“ (Lean), hält das Programm auf Stufe 1; behält man „Gleichheit ist eine Struktur“ und deckelt nur die Höhe, hält es am Deckel; nur wenn beides da ist, hält es nie an. Die Lean-Kontrolle ersetzt das ganze „Gleichheit ist eine Struktur“, nicht nur die Univalenz. Später wurde diese Gruppe von Kontrollen als ein einziges Theorem für jede Sammlung geschrieben (C-430): Ist beides da, hält das Programm nie an; deckelt man die Höhe der Elemente, hält es am Deckel; lässt man die Elemente genau wie im Beispiel des Universums, mit allen Höhen, und macht nur die „Gleichheit“ der Nummerierung des Katalogs zu einer Tatsache, hält es auf Stufe 1.
- Nach dem Beweis durch Widerspruch ist die Abstraktion neu zu prüfen, die die Theorie vorgenommen hat, um bequem zu sein. Das Theorem ist in beiden Dingen symmetrisch; es sagt nur, dass keines wegfallen darf. Welches davon die unrealistische Abstraktion ist, ist die Entscheidung der initiierenden Person vom 2026-10-15: Es gibt nur einen Angeklagten, die „**fertig vorliegende Sammlung**“: Das Universum übergibt auf einmal, als etwas bereits Daliegendes, ein Ganzes, dessen Bestätigung unendlich viele Stufen bräuchte. Die Univalenz ist eine der Ursachen und bleibt erhalten.
  - Auf der Seite der Mengenlehre (ZFC) nennt die initiierende Person diese Handlung A (2026-10-14, Originalwortlaut): “A就是一个无限的步骤才能到达，从而存在的结果，当作已经存在的结果，参与运算。” Übersetzung: „A ist dies: Ein Ergebnis, das erst durch unendlich viele Schritte erreicht wird und nur dadurch existiert, wird als bereits existierendes Ergebnis behandelt und geht in Rechnungen ein.“
  - Mit der „Richtung A“ am Anfang dieses Dokuments teilt es nur den Buchstaben; es ist nicht dasselbe. Das Phänomen dieses Dokuments gehört zur Richtung A (in der Realität vollendbar, in der Theorie nicht), der Angeklagte dagegen ist eine Handlung der Richtung B wie im Schwesterdokument 02 (noch nicht Festgelegtes als bereits geliefert behandeln).
  - Version 1 dieses Dokuments gab hier unsere eigene Rangfolge an (zuerst die Univalenz prüfen, höhere induktive Typen an zweiter Stelle); sie ist gemäß der Entscheidung korrigiert.

## Was es nicht ist

- Es ist kein innerer Widerspruch der HoTT. Alle Schlussfolgerungen werden in der HoTT von der Maschine akzeptiert.
- Die mathematischen Tatsachen sind größtenteils nicht neu: Dass solche Produkte keine endliche Stufe haben, ist Beispiel 8.8.6 des HoTT Book. Für das Universum selbst schreibt das Buch (Ende von §8.8), man erwarte, auch beweisen zu können, dass es für kein n ein n-Typ ist, das sei aber noch nicht geschehen; Kraus–Sattler 2015 haben bewiesen, dass das n-te Universum einer univalenten Hierarchie kein n-Typ ist, ohne höhere induktive Typen. Dass ein einzelnes Universum mit höheren induktiven Typen für kein n ein n-Typ ist, hat in diesem Repository einen Maschinenbeweis (C-75, siehe 02); ob seither ein veröffentlichter Beweis in der Literatur erschienen ist, haben wir noch nicht geprüft. Die geometrische Reihe kann man längst summieren; Zenons Neuheit liegt in der Lesart, und so ist es auch hier. Auch diese Lesart ist noch nicht mit der Literatur abgeglichen.
- Es ist nicht „in jedem Fall“ so: Es zeigt sich am Universum und an Gegenständen dieser Art, deren Höhe unbeschränkt ist. Aber das Universum ist kein Randfall: Es ist genau der Gegenstand, von dem die Univalenz spricht, und ein Element des Gegenstandsbereichs, das die HoTT nicht zurückweisen kann.

## Belege

- Das Frageprogramm und das Nie-Anhalten auf dem Universum: `HoTT/formal/claude-cg001/questioning-delay/CLAIM.md` (C-77 bis C-79); die Lean-Kontrolle in der Welt der Tatsachen: C-80 in derselben `CLAIM.md`.
- Das Nie-Anhalten auf einem gewöhnlichen Produkt und die gedeckelte Kontrolle: `HoTT/formal/claude-cg001/product-questioning/CLAIM.md` (C-81, C-82).
- Die Trunkierungskontrolle: `HoTT/formal/claude-cg001/truncation-questioning/CLAIM.md` (C-83).
- Die beiden Ursachen als ein Theorem für jede Sammlung, mit der Univalenz für sich isoliert: `HoTT/formal/claude-cg001/a-univalence-b/CLAIM.md` (C-430, 2026-10-15). Es fasst die obigen Kontrollen zusammen; es ist kein neues Phänomen.
- Läufe und exakte Wiederholungen: `.claude/goals/CG-001-targeted-overview/证据索引.md` §20–§23; der letzte Abschnitt der gemeinsamen Belegmatrix des Projekts, `HoTT/CLAIM_EVIDENCE_MATRIX.md`, registriert dieselbe Gruppe von Aussagen. Rahmen: Cubical Agda 2.8.0 mit cubical 0.9 (C-80 in Lean 4.34.0); C-77 bis C-80 auf zwei Plattformen, Linux und macOS, übereinstimmend wiederholt; C-81 bis C-83 nur auf macOS wiederholt.
- Der Originalwortlaut der initiierenden Person und die vollständige Lesart der KI: KC-000052 bis KC-000054 in `核心认知.md`; `扩展认知/011 - 本来应该很简单的事：UR 与芝诺的模式匹配.md`.

## Fragen an das Community-Audit

1. **Mathematik**: Gelten die am Ende aufgeführten formalen Aussagen? Sagen sie, was der Text sagt? Insbesondere: die genaue Bedeutung von „das Frageprogramm ist gleich `never`“ (keine endliche Menge an Treibstoff liefert eine Antwort) und ihr Verhältnis zu „jede Stufe antwortet nein“.
2. **Die Aufgabe**: „Ob zwei Dinge dasselbe sind, ist gewöhnlich die Sache eines einzigen Satzes“ – ist das eine faire Beschreibung der alltäglichen Logik und Mathematik? Ist es dasselbe, wenn man es als „Stufe für Stufe fragen, bis zu welcher Stufe die Gleichheit erledigt ist“ umsetzt?
3. **Zuschreibung**: Ist die veränderte Bedingung „Gleichheit lässt sich ohne Ende unterteilen“? Die initiierende Person hat die „fertig vorliegende Sammlung“ als Angeklagten benannt und die Univalenz als Ursache eingeordnet: Hält diese Zuschreibung stand? Gibt es konkurrierende Zuschreibungen, an die wir nicht gedacht haben?
4. **Standardantworten**: Können die Trunkierung, Mathematik nur auf Mengenebene oder die Schichtung der Universen die Ungereimtheit hier beseitigen? Was kostet jede dieser Antworten?
5. **Vorläufer**: Hat jemand diese mathematischen Tatsachen schon so gelesen? Außerdem: Dass ein einzelnes Universum mit höheren induktiven Typen für kein n ein n-Typ ist, war bei Abfassung des HoTT Book (2013) nicht bewiesen; ist es seither in der Literatur bewiesen worden?
