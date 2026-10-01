# HoTT-Paradoxy: Paradoxa der Nichtrealität in der Homotopietypentheorie – Ergebnisse und Belege

[中文](README-ZH.md) · [Русский](README-RU.md) · **Deutsch** · [Français](README-FR.md) · [English](README-EN.md)

**Zusammenfassung.** Aus Gründen der Ökonomie und der Allgemeinheit macht die Homotopietypentheorie (HoTT) aus „dasselbe sein“ statt einer Tatsache, die eine einzige Prüfung entscheidet, eine Struktur, die sich Stufe für Stufe befragen lässt („auf welche Weisen sind diese dasselbe?“): Isomorphe Dinge sind identisch (Univalenz), und Formen jeder Dimension stehen im Universum auf einmal zur Verfügung (höhere induktive Typen). Wir schreiben „entscheiden, ob zwei Dinge dasselbe sind“ als ein Programm, das Stufe für Stufe fragt: Die k-te Frage lautet, ob diese Gleichheit auf Stufe k erledigt ist (das heißt, ob der Typ das h-Level k+1 hat); ein Entscheider beantwortet jede Frage mit einem Beweis für „ja“ oder für „nein“; bei „ja“ hält das Programm an und meldet die Stufe. Wir beweisen in Cubical Agda, dass dieses Programm für jeden Entscheider auf dem Universum (mit höheren induktiven Typen) und auf dem Produkt ∏ₙ K(ℤ,n+1) gleich dem nie terminierenden Programm `never` ist; ist die Höhe der Elemente beschränkt, hält es genau bei der Frage an, die die Schranke bestimmt; nach denselben Gleichungen in Lean 4 übertragen, wo Gleichheit eine bloße Tatsache ist, hält es bei der ersten Frage an; auf die Mengentrunkierung angesetzt, hält es ebenfalls bei der ersten Frage an, doch die Trunkierung fasst die verschiedenen Weisen, dasselbe zu sein, zu einer einzigen zusammen und lässt sich nicht in das Universum zurückdecodieren. Die Person, die das Projekt initiiert hat, definiert ein Paradoxon der Nichtrealität als „etwas, das sehr einfach sein sollte, aber selbst in Theorie X nicht zu leisten ist“ (UR); sie liest dieses Ergebnis als Paradoxon von derselben Gestalt wie das des Zenon und hält es für sehr wahrscheinlich, dass es das ist, wonach das Projekt gesucht hat. Die Mathematik ist größtenteils nicht neu: Das Produkt ist Beispiel 8.8.6 des HoTT Book; für das Universum schrieb das Book (2013), das Ergebnis sei vermutlich beweisbar, aber noch nicht bewiesen, und dieses Repository liefert einen maschinengeprüften Beweis. Neu ist vor allem die Lesart und die Prämisse, auf die sie zeigt, allen voran die Univalenz. Eine zweite Linie: Eine einheitliche Definition semi-simplizialer Typen in Buch-HoTT ist bis heute unbekannt, ein bekanntes offenes Problem; die Person, die das Projekt initiiert hat, urteilte, diese Linie habe „das Gespenst von Zenons Paradoxon wiederbelebt“. Alle positiven Aussagen sind vom Kern geprüft (Cubical Agda 2.8.0 mit cubical 0.9; Lean 4.34.0), mit Negativkontrollen und 107 wiederholbaren Laufbelegen. Wir behaupten nicht, dass HoTT widersprüchlich ist; „sehr wahrscheinlich gefunden“ ist ein Urteil der Person, die das Projekt initiiert hat, kein Theorem.

**Schlüsselwörter.** Homotopietypentheorie; Univalenz; höhere induktive Typen; Trunkierungsstufen; Delay-Monade; unendliche Kohärenz; Zenons Paradoxon; Paradoxon der Nichtrealität

> **Zu diesem Branch.** `main` enthält nur, was die Ergebnisse stützt: die Ergebnisdokumente, präzise Aussagen, Beweisquellen, Laufbelege und die Möglichkeit, sie zu wiederholen. Der gesamte Forschungsprozess liegt im [Branch `dev`](https://github.com/math-fournity/HoTT-Paradoxy/tree/dev): das Verzeichnis der Originalaussagen der Person, die das Projekt initiiert hat, die Projektionen der Richtungen und Ergebnisse, die Arbeitsbereiche der KI-Systeme, Audits und Korrespondenz, Governance und Status. Dieser Branch wird aus dem Commit [`24950d5d`](https://github.com/math-fournity/HoTT-Paradoxy/commit/24950d5d19ee6d0e7edc6c2d6ff93f1c18a2c2e1) von `dev` nach einem Manifest erzeugt ([`RELEASE-MANIFEST.json`](RELEASE-MANIFEST.json)) und nicht direkt bearbeitet. Dieses README gibt es inhaltsgleich auch auf Chinesisch, Russisch, Französisch und Englisch. Die Ergebnisdokumente, der Abschlussbericht und `CLAIMS.md` sind auf Chinesisch verfasst; die Dokumente 01 und 02 beginnen mit einer englischen Zusammenfassung.

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
- Laufbelege: `HoTT/verification/runs/`, insgesamt 107: 49 vom Kern akzeptiert und 58 Negativkontrollen, die wie erwartet abgelehnt wurden (sie prüfen genaue Grenzen; sie sind keine Geschichte von Fehlschlägen). Für einige Aussagen gibt es Läufe unter macOS und unter Linux.
- [`RELEASE-MANIFEST.json`](RELEASE-MANIFEST.json): SHA-256 und Rolle jeder der 699 Dateien dieses Branches sowie der `dev`-Commit, aus dem sie stammen.

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

| Pfad | In `dev` |
|---|---|
| `.claude/goals/CG-001-targeted-overview` | [öffnen](https://github.com/math-fournity/HoTT-Paradoxy/tree/dev/.claude/goals/CG-001-targeted-overview) |
| `.claude/goals/CG-001-targeted-overview/证据索引.md` | [öffnen](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/.claude/goals/CG-001-targeted-overview/%E8%AF%81%E6%8D%AE%E7%B4%A2%E5%BC%95.md) |
| `.claude/goals/CG-002-a7-infinite-coherence` | [öffnen](https://github.com/math-fournity/HoTT-Paradoxy/tree/dev/.claude/goals/CG-002-a7-infinite-coherence) |
| `.claude/goals/CG-003-a7-self-audit` | [öffnen](https://github.com/math-fournity/HoTT-Paradoxy/tree/dev/.claude/goals/CG-003-a7-self-audit) |
| `.claude/思考与发现` | [öffnen](https://github.com/math-fournity/HoTT-Paradoxy/tree/dev/.claude/%E6%80%9D%E8%80%83%E4%B8%8E%E5%8F%91%E7%8E%B0) |
| `.claude/总索引.md` | [öffnen](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/.claude/%E6%80%BB%E7%B4%A2%E5%BC%95.md) |
| `.claude/调研请求/20260930-相同永远了结不了-社区先例调研请求.md` | [öffnen](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/.claude/%E8%B0%83%E7%A0%94%E8%AF%B7%E6%B1%82/20260930-%E7%9B%B8%E5%90%8C%E6%B0%B8%E8%BF%9C%E4%BA%86%E7%BB%93%E4%B8%8D%E4%BA%86-%E7%A4%BE%E5%8C%BA%E5%85%88%E4%BE%8B%E8%B0%83%E7%A0%94%E8%AF%B7%E6%B1%82.md) |
| `Cloud-Opus审计并补完GLM` | [öffnen](https://github.com/math-fournity/HoTT-Paradoxy/tree/dev/Cloud-Opus%E5%AE%A1%E8%AE%A1%E5%B9%B6%E8%A1%A5%E5%AE%8CGLM) |
| `Cloud-Opus审计并补完GLM/01-工具链与复现.md` | [öffnen](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/Cloud-Opus%E5%AE%A1%E8%AE%A1%E5%B9%B6%E8%A1%A5%E5%AE%8CGLM/01-%E5%B7%A5%E5%85%B7%E9%93%BE%E4%B8%8E%E5%A4%8D%E7%8E%B0.md) |
| `Cloud-Opus审计并补完GLM/02-断裂审计-逐命题（D1）.md` | [öffnen](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/Cloud-Opus%E5%AE%A1%E8%AE%A1%E5%B9%B6%E8%A1%A5%E5%AE%8CGLM/02-%E6%96%AD%E8%A3%82%E5%AE%A1%E8%AE%A1-%E9%80%90%E5%91%BD%E9%A2%98%EF%BC%88D1%EF%BC%89.md) |
| `Cloud-Opus审计并补完GLM/11-收据核验结果.json` | [öffnen](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/Cloud-Opus%E5%AE%A1%E8%AE%A1%E5%B9%B6%E8%A1%A5%E5%AE%8CGLM/11-%E6%94%B6%E6%8D%AE%E6%A0%B8%E9%AA%8C%E7%BB%93%E6%9E%9C.json) |
| `Cloud-Opus审计并补完GLM/13-外部复核请求.md` | [öffnen](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/Cloud-Opus%E5%AE%A1%E8%AE%A1%E5%B9%B6%E8%A1%A5%E5%AE%8CGLM/13-%E5%A4%96%E9%83%A8%E5%A4%8D%E6%A0%B8%E8%AF%B7%E6%B1%82.md) |
| `Cloud-Opus审计并补完GLM/14-罗素面终局判词.md` | [öffnen](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/Cloud-Opus%E5%AE%A1%E8%AE%A1%E5%B9%B6%E8%A1%A5%E5%AE%8CGLM/14-%E7%BD%97%E7%B4%A0%E9%9D%A2%E7%BB%88%E5%B1%80%E5%88%A4%E8%AF%8D.md) |
| `Cloud-Opus审计并补完GLM/README.md` | [öffnen](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/Cloud-Opus%E5%AE%A1%E8%AE%A1%E5%B9%B6%E8%A1%A5%E5%AE%8CGLM/README.md) |
| `Cloud-Opus审计并补完GLM/tools` | [öffnen](https://github.com/math-fournity/HoTT-Paradoxy/tree/dev/Cloud-Opus%E5%AE%A1%E8%AE%A1%E5%B9%B6%E8%A1%A5%E5%AE%8CGLM/tools) |
| `Cloud-Opus审计并补完GLM/tools/capture_zeno_line_replays.sh` | [öffnen](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/Cloud-Opus%E5%AE%A1%E8%AE%A1%E5%B9%B6%E8%A1%A5%E5%AE%8CGLM/tools/capture_zeno_line_replays.sh) |
| `Cloud-Opus审计并补完GLM/附件/20260926-Session问答原文存档（用户上传，GLM-Auditor会话）.md` | [öffnen](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/Cloud-Opus%E5%AE%A1%E8%AE%A1%E5%B9%B6%E8%A1%A5%E5%AE%8CGLM/%E9%99%84%E4%BB%B6/20260926-Session%E9%97%AE%E7%AD%94%E5%8E%9F%E6%96%87%E5%AD%98%E6%A1%A3%EF%BC%88%E7%94%A8%E6%88%B7%E4%B8%8A%E4%BC%A0%EF%BC%8CGLM-Auditor%E4%BC%9A%E8%AF%9D%EF%BC%89.md) |
| `Cloud-Opus审计并补完GLM/附件/工作过程文件/自查轮/verify-all-rerun-46个运行.json` | [öffnen](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/Cloud-Opus%E5%AE%A1%E8%AE%A1%E5%B9%B6%E8%A1%A5%E5%AE%8CGLM/%E9%99%84%E4%BB%B6/%E5%B7%A5%E4%BD%9C%E8%BF%87%E7%A8%8B%E6%96%87%E4%BB%B6/%E8%87%AA%E6%9F%A5%E8%BD%AE/verify-all-rerun-46%E4%B8%AA%E8%BF%90%E8%A1%8C.json) |
| `GLM-5.3-Flash/README.md` | [öffnen](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/GLM-5.3-Flash/README.md) |
| `GLM-5.3-Flash/审计请求` | [öffnen](https://github.com/math-fournity/HoTT-Paradoxy/tree/dev/GLM-5.3-Flash/%E5%AE%A1%E8%AE%A1%E8%AF%B7%E6%B1%82) |
| `GLM-5.3-Flash/思考与发现` | [öffnen](https://github.com/math-fournity/HoTT-Paradoxy/tree/dev/GLM-5.3-Flash/%E6%80%9D%E8%80%83%E4%B8%8E%E5%8F%91%E7%8E%B0) |
| `GLM-5.3-Flash/策略快照/20260926-D2后罗素线策略-大白话快照.md` | [öffnen](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/GLM-5.3-Flash/%E7%AD%96%E7%95%A5%E5%BF%AB%E7%85%A7/20260926-D2%E5%90%8E%E7%BD%97%E7%B4%A0%E7%BA%BF%E7%AD%96%E7%95%A5-%E5%A4%A7%E7%99%BD%E8%AF%9D%E5%BF%AB%E7%85%A7.md) |
| `GLM-5.3-Flash/裁定问题/20260926-M2-形成规则是回答还是回避-两面陈词.md` | [öffnen](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/GLM-5.3-Flash/%E8%A3%81%E5%AE%9A%E9%97%AE%E9%A2%98/20260926-M2-%E5%BD%A2%E6%88%90%E8%A7%84%E5%88%99%E6%98%AF%E5%9B%9E%E7%AD%94%E8%BF%98%E6%98%AF%E5%9B%9E%E9%81%BF-%E4%B8%A4%E9%9D%A2%E9%99%88%E8%AF%8D.md) |
| `HoTT/CLAIM_EVIDENCE_MATRIX.md` | [öffnen](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/HoTT/CLAIM_EVIDENCE_MATRIX.md) |
| `HoTT/verification/PROOF_VERSION_CLOSURE.json` | [öffnen](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/HoTT/verification/PROOF_VERSION_CLOSURE.json) |
| `README.md` | [öffnen](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/README.md) |
| `Terra对Opus的审计` | [öffnen](https://github.com/math-fournity/HoTT-Paradoxy/tree/dev/Terra%E5%AF%B9Opus%E7%9A%84%E5%AE%A1%E8%AE%A1) |
| `Terra对Opus的审计/Opus给GPT的回应` | [öffnen](https://github.com/math-fournity/HoTT-Paradoxy/tree/dev/Terra%E5%AF%B9Opus%E7%9A%84%E5%AE%A1%E8%AE%A1/Opus%E7%BB%99GPT%E7%9A%84%E5%9B%9E%E5%BA%94) |
| `rulings.md` | [öffnen](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/rulings.md) |
| `scripts/audit/verify_math_proof_delivery_governance.py` | [öffnen](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/scripts/audit/verify_math_proof_delivery_governance.py) |
| `scripts/audit/verify_proof_version_closure.py` | [öffnen](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/scripts/audit/verify_proof_version_closure.py) |
| `sources/prompts/Claude-UR与芝诺的模式匹配-用户原文-20260930.md` | [öffnen](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/sources/prompts/Claude-UR%E4%B8%8E%E8%8A%9D%E8%AF%BA%E7%9A%84%E6%A8%A1%E5%BC%8F%E5%8C%B9%E9%85%8D-%E7%94%A8%E6%88%B7%E5%8E%9F%E6%96%87-20260930.md) |
| `sources/prompts/Claude-归因是正题-用户原文-20260924.md` | [öffnen](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/sources/prompts/Claude-%E5%BD%92%E5%9B%A0%E6%98%AF%E6%AD%A3%E9%A2%98-%E7%94%A8%E6%88%B7%E5%8E%9F%E6%96%87-20260924.md) |
| `sources/prompts/Claude-罗素原则P1至P3-用户原文-20260926.md` | [öffnen](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/sources/prompts/Claude-%E7%BD%97%E7%B4%A0%E5%8E%9F%E5%88%99P1%E8%87%B3P3-%E7%94%A8%E6%88%B7%E5%8E%9F%E6%96%87-20260926.md) |
| `sources/prompts/Codex-非现实性悖论的目标与A向读法-用户原文-20260930.md` | [öffnen](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/sources/prompts/Codex-%E9%9D%9E%E7%8E%B0%E5%AE%9E%E6%80%A7%E6%82%96%E8%AE%BA%E7%9A%84%E7%9B%AE%E6%A0%87%E4%B8%8EA%E5%90%91%E8%AF%BB%E6%B3%95-%E7%94%A8%E6%88%B7%E5%8E%9F%E6%96%87-20260930.md) |
| `sources/prompts/GLM-算符先行于存在性落定-用户原文-20260926.md` | [öffnen](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/sources/prompts/GLM-%E7%AE%97%E7%AC%A6%E5%85%88%E8%A1%8C%E4%BA%8E%E5%AD%98%E5%9C%A8%E6%80%A7%E8%90%BD%E5%AE%9A-%E7%94%A8%E6%88%B7%E5%8E%9F%E6%96%87-20260926.md) |
| `全景视野.md` | [öffnen](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/%E5%85%A8%E6%99%AF%E8%A7%86%E9%87%8E.md) |
| `扩展认知.md` | [öffnen](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/%E6%89%A9%E5%B1%95%E8%AE%A4%E7%9F%A5.md) |
| `扩展认知/011 - 本来应该很简单的事：UR 与芝诺的模式匹配.md` | [öffnen](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/%E6%89%A9%E5%B1%95%E8%AE%A4%E7%9F%A5/011%20-%20%E6%9C%AC%E6%9D%A5%E5%BA%94%E8%AF%A5%E5%BE%88%E7%AE%80%E5%8D%95%E7%9A%84%E4%BA%8B%EF%BC%9AUR%20%E4%B8%8E%E8%8A%9D%E8%AF%BA%E7%9A%84%E6%A8%A1%E5%BC%8F%E5%8C%B9%E9%85%8D.md) |
| `方向追踪.md` | [öffnen](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/%E6%96%B9%E5%90%91%E8%BF%BD%E8%B8%AA.md) |
| `核心认知.md` | [öffnen](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/%E6%A0%B8%E5%BF%83%E8%AE%A4%E7%9F%A5.md) |

## 7. Branches

- `main` (dieser Branch): Ergebnisse und Belege. Er wird von `scripts/release/build_main_release.py` in `dev` nach `scripts/release/main-release-spec.json` erzeugt. Zum Aktualisieren ändert man das Manifest oder die Ergebnisdokumente in `dev` und erzeugt ihn neu; direkt in diesen Branch wird nichts committet.
- `dev`: der gesamte Forschungsprozess; dort findet alle Arbeit statt.
