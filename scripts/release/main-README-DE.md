# HoTT-Paradoxy: Paradoxa der Nichtrealität in der Homotopietypentheorie – Ergebnisse und Belege

[中文](README-ZH.md) · [English](README-EN.md) · [Français](README-FR.md) · **Deutsch**

**Zusammenfassung.** Aus Gründen der Ökonomie und der Allgemeinheit macht die Homotopietypentheorie (HoTT) aus „dasselbe sein“ statt einer Tatsache, die eine einzige Prüfung entscheidet, eine Struktur, die sich Stufe für Stufe befragen lässt („auf welche Weisen sind diese dasselbe?“): Isomorphe Dinge sind identisch (Univalenz), und Formen jeder Dimension stehen im Universum auf einmal zur Verfügung (höhere induktive Typen). Wir schreiben „entscheiden, ob zwei Dinge dasselbe sind“ als ein Programm, das Stufe für Stufe fragt: Die k-te Frage lautet, ob diese Gleichheit auf Stufe k erledigt ist (das heißt, ob der Typ das h-Level k+1 hat); ein Entscheider beantwortet jede Frage mit einem Beweis für „ja“ oder für „nein“; bei „ja“ hält das Programm an und meldet die Stufe. Wir beweisen in Cubical Agda, dass dieses Programm für jeden Entscheider auf dem Universum (mit höheren induktiven Typen) und auf dem Produkt ∏ₙ K(ℤ,n+1) gleich dem nie terminierenden Programm `never` ist; ist die Höhe der Elemente beschränkt, hält es genau bei der Frage an, die die Schranke bestimmt; nach denselben Gleichungen in Lean 4 übertragen, wo Gleichheit eine bloße Tatsache ist, hält es bei der ersten Frage an; auf die Mengentrunkierung angesetzt, hält es ebenfalls bei der ersten Frage an, doch die Trunkierung fasst die verschiedenen Weisen, dasselbe zu sein, zu einer einzigen zusammen und lässt sich nicht in das Universum zurückdecodieren. Die Person, die das Projekt initiiert hat, definiert ein Paradoxon der Nichtrealität als „etwas, das sehr einfach sein sollte, aber selbst in Theorie X nicht zu leisten ist“ (UR); sie liest dieses Ergebnis als Paradoxon von derselben Gestalt wie das des Zenon und hält es für sehr wahrscheinlich, dass es das ist, wonach das Projekt gesucht hat. Die Mathematik ist größtenteils nicht neu: Das Produkt ist Beispiel 8.8.6 des HoTT Book; für das Universum schrieb das Book (2013), das Ergebnis sei vermutlich beweisbar, aber noch nicht bewiesen, und dieses Repository liefert einen maschinengeprüften Beweis. Neu ist vor allem die Lesart und die Prämisse, auf die sie zeigt, allen voran die Univalenz. Eine zweite Linie: Eine einheitliche Definition semi-simplizialer Typen in Buch-HoTT ist bis heute unbekannt, ein bekanntes offenes Problem; die Person, die das Projekt initiiert hat, urteilte, diese Linie habe „das Gespenst von Zenons Paradoxon wiederbelebt“. Alle positiven Aussagen sind vom Kern geprüft (Cubical Agda 2.8.0 mit cubical 0.9; Lean 4.34.0), mit Negativkontrollen und {{RUN_TOTAL}} wiederholbaren Laufbelegen. Wir behaupten nicht, dass HoTT widersprüchlich ist; „sehr wahrscheinlich gefunden“ ist ein Urteil der Person, die das Projekt initiiert hat, kein Theorem.

**Schlüsselwörter.** Homotopietypentheorie; Univalenz; höhere induktive Typen; Trunkierungsstufen; Delay-Monade; unendliche Kohärenz; Zenons Paradoxon; Paradoxon der Nichtrealität

> **Zu diesem Branch.** `main` enthält nur, was die Ergebnisse stützt: die Ergebnisdokumente, präzise Aussagen, Beweisquellen, Laufbelege und die Möglichkeit, sie zu wiederholen. Der gesamte Forschungsprozess liegt im [Branch `dev`]({{REPO}}/tree/dev): das Verzeichnis der Originalaussagen der Person, die das Projekt initiiert hat, die Projektionen der Richtungen und Ergebnisse, die Arbeitsbereiche der KI-Systeme, Audits und Korrespondenz, Governance und Status. Dieser Branch wird aus dem Commit [`{{SOURCE_SHORT}}`]({{REPO}}/commit/{{SOURCE_COMMIT}}) von `dev` nach einem Manifest erzeugt ([`RELEASE-MANIFEST.json`](RELEASE-MANIFEST.json)) und nicht direkt bearbeitet. Dieses README gibt es inhaltsgleich auch auf Chinesisch, Englisch und Französisch. Die Ergebnisdokumente, der Abschlussbericht und `CLAIMS.md` sind auf Chinesisch verfasst; die Dokumente 01 und 02 beginnen mit einer englischen Zusammenfassung.

## 1. Definition und Urteile der Person, die das Projekt initiiert hat

Operative Definition eines „Paradoxons der Nichtrealität“ (2026-09-30, Originalwortlaut):

> `UR`=`本来应该很简单的事情，甚至在X理论中，都做不到`，我想这就是一种类似芝诺悖论的`不合理`。

Übersetzung: „`UR` = `etwas, das sehr einfach sein sollte, aber selbst in Theorie X nicht zu leisten ist`; ich denke, das ist eine Ungereimtheit von der Art des zenonischen Paradoxons.“

„Realität“ bezieht sich auf die erste Hälfte von UR („etwas, das sehr einfach sein sollte“), „Paradoxon“ auf UR als Ganzes; die „Ungereimtheit“ beurteilt, wer einmal hinschaut. Dieses Urteil gehört der Person, die das Projekt initiiert hat; es ist kein mathematisches Theorem. Ihre beiden Urteile (Originalwortlaut, jeweils mit Übersetzung):

> 本repo复活了芝诺悖论的幽灵和罗素悖论的幽灵，并且找到的HoTT理论的问题。

Übersetzung (2026-09-27): „Dieses Repo hat das Gespenst von Zenons Paradoxon und das Gespenst von Russells Paradoxon wiederbelebt und das Problem der HoTT-Theorie gefunden.“

> 把所有该做的，全部做完，我认为我们要阶段性地收尾HoTT悖论查找工作了，因为我们很可能已经找到了。

Übersetzung (2026-09-30): „Erledigt alles, was zu tun ist. Ich denke, wir sollten diese Phase der Suche nach HoTT-Paradoxa abschließen, denn wir haben es sehr wahrscheinlich gefunden.“

## 2. Der Zenon der HoTT: „dasselbe sein“ wird nie entschieden

**Das, was einfach sein sollte:** entscheiden, ob zwei Dinge dasselbe sind.

**Der Prozess, der darauf zielt:** ein Programm Q, das Stufe für Stufe fragt. Es fragt: „Ist die Gleichheit in diesem Katalog auf Stufe k erledigt?“ (technisch: Ist es ein Typ vom h-Level k+1?); ein Entscheider beantwortet jede Frage mit einem Beweis für „ja“ oder für „nein“; bei „ja“ hält das Programm an und meldet die Stufe. Q hält genau dann an, wenn die Gleichheit auf einer endlichen Stufe erledigt ist (CG001-C-77).

**Ergebnisse** (maschinengeprüft):

| Fall | Ausgang desselben Programms | Aussage |
|---|---|---|
| Gleichheit ist eine Tatsache (dieselben Gleichungen in Lean 4 übertragen) | das Universum hält bei Frage 1 | CG001-C-80 |
| HoTT, Katalog der Typen vom h-Level 1+n | hält genau bei Frage 1+n | CG001-C-79 |
| HoTT, dasselbe Produkt mit durch b beschränkter Höhe der Elemente | hält genau bei Frage 2+b | CG001-C-82 |
| HoTT, das Produkt ∏ₙ K(ℤ,n+1) (HoTT Book, Beispiel 8.8.6) | gleich dem nie terminierenden `never`, für jeden Entscheider | CG001-C-81 |
| HoTT (mit höheren induktiven Typen), das Universum | gleich `never`, für jeden Entscheider | CG001-C-75, CG001-C-78 |
| HoTT, die Mengentrunkierung | hält bei Frage 1; aber die Trunkierung fasst die Weisen, dasselbe zu sein, zu einer zusammen und lässt sich nicht in das Universum zurückdecodieren | CG001-C-83 |

**Entsprechung zu Zenon** (ein Mustervergleich, kein mathematischer Isomorphismus):

| | Zenon | HoTT |
|---|---|---|
| Das, was einfach sein sollte | von hier nach dort gehen | entscheiden, ob zwei Dinge dasselbe sind |
| Die Bedingung, die die Theorie der Bequemlichkeit halber geändert hat | der Ort ist unbegrenzt teilbar | die Gleichheit ist unbegrenzt teilbar |
| Was jeder Schritt zeigt | die Hälfte bleibt; sicher noch nicht angekommen | diese Stufe ist nicht erledigt; ein sicheres „nein“ |
| Ausgang | der Weg endet nie | das Programm ist gleich `never` |
| Lehrbuchauflösung | Grenzwerte | Trunkierung |

**Der stärkste Einwand:** „Auf die Mengentrunkierung angesetzt, hält das Programm bei Frage 1; die Frage war also nur falsch gestellt.“ Antwort: Die Trunkierung beantwortet „Wie viele Zweige gibt es?“; sie fasst die Weisen, dasselbe zu sein, zu einer zusammen und kann nicht in das Universum zurück: Das befragte Objekt ist ein anderes geworden. Das ist, als beantwortete man Zenon mit Grenzwerten: Eine Definition erklärt, man sei angekommen, ohne dass die geänderte Bedingung wiederhergestellt wird. Diese Antwort ist eine Deutung und wird dem Audit vorgelegt.

**Was es nicht ist:**

- Es ist kein innerer Widerspruch der HoTT.
- Die Mathematik ist größtenteils nicht neu: Dass solche Produkte keine endliche Stufe haben, ist Beispiel 8.8.6 des HoTT Book; für das Universum selbst schrieb das Book (2013), es sei vermutlich beweisbar, aber noch nicht bewiesen; Kraus und Sattler (2015) bewiesen, dass das n-te Universum einer univalenten Hierarchie kein n-Typ ist; für ein einzelnes Universum mit höheren induktiven Typen enthält dieses Repository einen maschinengeprüften Beweis (CG001-C-75). Neu ist vor allem die Lesart und die Prämisse, auf die sie zeigt, allen voran die Univalenz.
- „Hält nie an“ ist ein Satz innerhalb der Theorie. Ihn als „das Programm liefert in der Wirklichkeit nie eine Antwort“ zu lesen, erfordert zusätzlich die Widerspruchsfreiheit der Theorie und, für einen beliebigen Entscheider, Kanonizität.
- „Sehr wahrscheinlich gefunden“ ist ein Urteil der Person, die das Projekt initiiert hat, kein Theorem.

Weiterlesen (auf Chinesisch): [Auditdokument 03, „Der Zenon der HoTT“](docs/社区审计提交/03-HoTT的芝诺.md) (das kürzeste, endet mit fünf Auditfragen); [02, „Das Gespenst von Russells Paradoxon“](docs/社区审计提交/02-罗素悖论的幽灵.md); [der Abschlussbericht der ersten Phase](docs/HoTT悖论查找阶段收尾报告-20260930.md).

## 3. Das Gespenst von Zenons Paradoxon: unendliche Kohärenz

- **Abwägung:** Die Univalenz macht isomorphe Dinge identisch, also wird Gleichheit zu Daten. Zum Beispiel ist Bool auf zwei wirklich verschiedene Weisen „dasselbe“ wie es selbst, und der Transport von `true` entlang der zweiten ergibt `false` (CG001-C-63).
- **Prozess:** eine semi-simpliziale Struktur aufschreiben, also eine Form Stufe für Stufe aus Punkten, Strecken, Dreiecken und Tetraedern zusammenkleben und verlangen, dass die „Seiten der Seiten“ übereinstimmen. In der klassischen Mathematik ist das eine einzeilige Definition.
- **Beobachtungen:** Wo Gleichheit eine Tatsache ist (Lean 4), ist diese Zeile die ganze Definition, und die Sechseck-Kohärenz gilt per `rfl` (CG001-C-65); in HoTT akzeptiert dieselbe Zeile Daten, die nicht zusammenpassen: Zwei Vereinfachungswege umrunden den Kreis einmal bzw. zweimal (CG001-C-64); ist das Sechseck ergänzt, lässt es sich auf mehr als eine Weise füllen, und die nächste Stufe (P₄) scheitert für eine der Füllungen (CG001-C-66, CG001-C-68); wie viele Stufen ergänzt werden müssen, hängt davon ab, wie viele Stufen die Gleichheit hat (CG001-C-70); jede feste Stufe lässt sich aufschreiben (maschinengeprüft bis Stufe 5, CG001-C-62).
- **Grenze:** Eine interne Definition, die in der Stufenzahl n einheitlich ist, ist ein bekanntes offenes Problem; ihre Unmöglichkeit ist nicht bewiesen. Taucht in Buch-HoTT eine einheitliche Definition semi-simplizialer Typen auf, wird die starke Form dieser Linie zurückgezogen.

Weiterlesen (auf Chinesisch, mit englischer Zusammenfassung am Anfang): [Auditdokument 01, „Das Gespenst von Zenons Paradoxon“](docs/社区审计提交/01-芝诺悖论的幽灵.md).

## 4. Aussagen und Belege

- [`CLAIMS.md`](CLAIMS.md) (auf Chinesisch): die präzise Formulierung, die Belege und die verbotenen Verallgemeinerungen jeder Aussage; für jedes Beweispaket die Hauptläufe, Negativkontrollen und plattformübergreifenden Wiederholungen.
- Beweisquellen: `HoTT/formal/`. Die `CLAIM.md` jedes Pakets enthält die vollständigen Aussagen und ihren Geltungsbereich.
- Laufbelege: `HoTT/verification/runs/`, insgesamt {{RUN_TOTAL}}: {{RUN_ACCEPTED}} vom Kern akzeptiert und {{RUN_REJECTED}} Negativkontrollen, die wie erwartet abgelehnt wurden (sie prüfen genaue Grenzen; sie sind keine Geschichte von Fehlschlägen). Für einige Aussagen gibt es Läufe unter macOS und unter Linux.
- [`RELEASE-MANIFEST.json`](RELEASE-MANIFEST.json): SHA-256 und Rolle jeder der {{FILE_TOTAL}} Dateien dieses Branches sowie der `dev`-Commit, aus dem sie stammen.

Werkzeuge: Cubical Agda 2.8.0 mit der cubical-Bibliothek v0.9 (die Optionen `--safe --cubical --guardedness` stehen in jeder Quelldatei); Lean 4.34.0, nur die Kernbibliothek (ohne Mathlib), für die Kontrollen, in denen Gleichheit eine Tatsache ist. Die von den Belegen zitierten Werkzeugprotokolle liegen in `HoTT/formal/dedekind-omega-missile/` (Agda unter macOS), `HoTT/formal/claude-cg001/pedometer-ablation-lean/` (Lean unter macOS) und `HoTT/formal/cloud-opus-glm-audit/` (Linux); die ersten beiden Verzeichnisse behalten ihren Ort aus `dev` und enthalten hier nur diese Protokolle.

## 5. Wiederholen

Mit installiertem Agda 2.8.0, cubical v0.9 und Lean 4.34.0 im Wurzelverzeichnis des Repositorys ausführen:

```sh
python3 tools/replay.py --agda /pfad/zu/agda --cubical-lib /pfad/zu/cubical/cubical.agda-lib --lean-sysroot /pfad/zu/lean-4.34.0 --jobs 4
```

Das Skript baut den Befehl jedes Belegs mit relativen Pfaden neu auf, führt ihn aus und vergleicht das Ergebnis mit dem Beleg: Der Ausgang (akzeptiert oder abgelehnt) muss übereinstimmen, und die Ausgabe wird zeilenweise verglichen, nachdem Repository-Wurzel und Bibliothekspfade durch Platzhalter ersetzt wurden. Eine Negativkontrolle besteht nur, wenn sie erneut abgelehnt wird; stimmt auch ihre Ausgabe überein, wurde sie aus dem protokollierten Grund abgelehnt. Einen einzelnen Beleg wiederholen: `--only <Lauf-ID>`; alle auflisten: `--list`. Alles nacheinander zu wiederholen dauert etwa anderthalb Stunden.

Die Befehle in den Belegen verzeichnen absolute Pfade des Rechners, auf dem sie entstanden. Die ursprünglichen bytegenauen Wiederholungswerkzeuge liegen im Branch `dev` (`.claude/goals/CG-001-targeted-overview/tools/verify_cg001_run.py`, `Cloud-Opus审计并补完GLM/tools/verify_copus_run.py`).

## 6. In den Dokumenten erwähnte Pfade, die nicht in diesem Branch liegen

Die Ergebnisdokumente erwähnen auch Dateien aus dem Forschungsprozess: das Verzeichnis der Originalaussagen `核心认知.md`, die Projektionen der Richtungen und Ergebnisse, die Arbeitsbereiche der KI-Systeme, Audits und Korrespondenz, die zielbezogenen Indizes und anderes. Sie alle liegen im Branch `dev`:

{{DEV_PATHS_TABLE}}

## 7. Branches

- `main` (dieser Branch): Ergebnisse und Belege. Er wird von `scripts/release/build_main_release.py` in `dev` nach `scripts/release/main-release-spec.json` erzeugt. Zum Aktualisieren ändert man das Manifest oder die Ergebnisdokumente in `dev` und erzeugt ihn neu; direkt in diesen Branch wird nichts committet.
- `dev`: der gesamte Forschungsprozess; dort findet alle Arbeit statt.
