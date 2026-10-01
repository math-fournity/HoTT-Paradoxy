# HoTT-Paradoxy : paradoxes de non-réalité en théorie homotopique des types — conclusions et éléments de preuve

[中文](README-ZH.md) · [Русский](README-RU.md) · [Deutsch](README-DE.md) · **Français** · [English](README-EN.md)

**Résumé.** Par souci d'économie et de généralité, la théorie homotopique des types (HoTT) change le statut d'« être la même chose » : ce n'est plus un fait qu'une seule vérification établit, mais une structure que l'on peut interroger niveau par niveau (« de quelles manières ces objets sont-ils les mêmes ? ») ; des objets isomorphes sont identiques (univalence), et des formes de toute dimension sont disponibles d'emblée dans l'univers (types inductifs supérieurs). Nous écrivons « décider si deux choses sont la même » sous la forme d'un programme qui interroge niveau par niveau : la k-ième question demande si cette identité est tranchée au niveau k (c'est-à-dire si le type est de h-niveau k+1) ; un juge répond à chaque question par une preuve de « oui » ou de « non » ; sur « oui », le programme s'arrête et indique le niveau. Nous démontrons en Cubical Agda que, pour tout juge, ce programme est égal au programme `never`, qui ne termine jamais, sur l'univers (avec types inductifs supérieurs) et sur le produit ∏ₙ K(ℤ,n+1) ; lorsque la hauteur des éléments est bornée, il s'arrête exactement à la question que fixe la borne ; transcrit par les mêmes équations en Lean 4, où l'identité est un simple fait, il s'arrête à la première question ; interrogé sur la troncature ensembliste, il s'arrête lui aussi à la première question, mais la troncature fond en une seule les différentes manières d'être le même et ne peut pas être décodée vers l'univers. La personne à l'origine du projet définit un paradoxe de non-réalité comme « une chose qui devrait être très simple et qui, même dans la théorie X, ne peut pas être faite » (UR) ; elle lit ce résultat comme un paradoxe de même forme que celui de Zénon et juge très probable que ce soit celui que le projet cherchait. Les mathématiques ne sont pour l'essentiel pas nouvelles : le produit est l'exemple 8.8.6 du HoTT Book ; pour l'univers, le Book (2013) indiquait que le résultat devait être démontrable mais ne l'avait pas encore été, et ce dépôt en donne une preuve vérifiée par machine. Ce qui est nouveau, c'est surtout la lecture et la prémisse qu'elle désigne, au premier chef l'univalence. Une seconde ligne : une définition uniforme des types semi-simpliciaux en HoTT « du livre » reste inconnue, un problème ouvert bien connu ; la personne à l'origine du projet a jugé que cette ligne « a ressuscité le fantôme du paradoxe de Zénon ». Toutes les affirmations positives sont vérifiées par le noyau (Cubical Agda 2.8.0 avec cubical 0.9 ; Lean 4.34.0), avec des contrôles négatifs et {{RUN_TOTAL}} reçus d'exécution rejouables. Nous ne prétendons pas que HoTT soit incohérente ; « très probablement trouvé » est un jugement de la personne à l'origine du projet, non un théorème.

**Mots-clés.** théorie homotopique des types ; univalence ; types inductifs supérieurs ; niveaux de troncature ; monade de délai ; cohérence infinie ; paradoxe de Zénon ; paradoxe de non-réalité

> **À propos de cette branche.** `main` ne contient que ce qui étaye les conclusions : les documents de conclusion, les énoncés précis, les sources des preuves, les reçus d'exécution et le moyen de les rejouer. L'ensemble du processus de recherche se trouve sur la [branche `dev`]({{REPO}}/tree/dev) : le registre des propos originaux de la personne à l'origine du projet, les projections des directions et des résultats, les espaces de travail des IA, les audits et les échanges, la gouvernance et l'état. Cette branche est générée à partir du commit [`{{SOURCE_SHORT}}`]({{REPO}}/commit/{{SOURCE_COMMIT}}) de `dev` selon un manifeste ([`RELEASE-MANIFEST.json`](RELEASE-MANIFEST.json)) et n'est pas modifiée directement. Ce README existe aussi en chinois, en russe, en allemand et en anglais, avec le même contenu. Les documents de conclusion, le rapport de clôture et `CLAIMS.md` sont rédigés en chinois ; les documents 01 et 02 commencent par un résumé en anglais.

## 1. Définition et verdicts de la personne à l'origine du projet

Définition opérationnelle d'un « paradoxe de non-réalité » (2026-09-30, propos originaux) :

> `UR`=`本来应该很简单的事情，甚至在X理论中，都做不到`，我想这就是一种类似芝诺悖论的`不合理`。

Traduction : « `UR` = `une chose qui devrait être très simple et qui, même dans la théorie X, ne peut pas être faite` ; je pense que c'est là quelque chose de « déraisonnable », du même genre que le paradoxe de Zénon. »

« Réalité » renvoie à la première moitié de UR (« une chose qui devrait être très simple »), « paradoxe » à UR tout entier ; le « déraisonnable » se juge d'un seul coup d'œil, par quiconque regarde. Ce jugement appartient à la personne à l'origine du projet ; ce n'est pas un théorème mathématique. Ses deux verdicts (propos originaux, chacun suivi d'une traduction) :

> 本repo复活了芝诺悖论的幽灵和罗素悖论的幽灵，并且找到的HoTT理论的问题。

Traduction (2026-09-27) : « Ce dépôt a ressuscité le fantôme du paradoxe de Zénon et le fantôme du paradoxe de Russell, et a trouvé le problème de la théorie HoTT. »

> 把所有该做的，全部做完，我认为我们要阶段性地收尾HoTT悖论查找工作了，因为我们很可能已经找到了。

Traduction (2026-09-30) : « Faites tout ce qui doit être fait. Je pense que nous devons clore cette phase de la recherche de paradoxes dans HoTT, car nous l'avons très probablement trouvé. »

## 2. Le Zénon de HoTT : « être la même chose » ne se tranche jamais

**La chose qui devrait être simple :** décider si deux choses sont la même.

**Le processus qui la vise :** un programme Q qui interroge niveau par niveau. Il demande « l'identité dans ce catalogue est-elle tranchée au niveau k ? » (techniquement : est-ce un type de h-niveau k+1 ?) ; un juge répond à chaque question par une preuve de « oui » ou de « non » ; sur « oui », le programme s'arrête et indique le niveau. Q s'arrête si et seulement si l'identité se tranche à un niveau fini (CG001-C-77).

**Résultats** (vérifiés par machine) :

| Cas | Issue du même programme | Énoncé |
|---|---|---|
| L'identité est un fait (mêmes équations transcrites en Lean 4) | l'univers s'arrête à la question 1 | CG001-C-80 |
| HoTT, catalogue des types de h-niveau 1+n | s'arrête exactement à la question 1+n | CG001-C-79 |
| HoTT, le même produit avec la hauteur des éléments bornée par b | s'arrête exactement à la question 2+b | CG001-C-82 |
| HoTT, le produit ∏ₙ K(ℤ,n+1) (HoTT Book, exemple 8.8.6) | égal au programme `never`, qui ne termine jamais, pour tout juge | CG001-C-81 |
| HoTT (avec types inductifs supérieurs), l'univers | égal à `never` pour tout juge | CG001-C-75, CG001-C-78 |
| HoTT, la troncature ensembliste | s'arrête à la question 1 ; mais la troncature fond en une seule les manières d'être le même et ne peut pas être décodée vers l'univers | CG001-C-83 |

**Correspondance avec Zénon** (une mise en correspondance de formes, non un isomorphisme mathématique) :

| | Zénon | HoTT |
|---|---|---|
| La chose qui devrait être simple | aller d'ici à là-bas | décider si deux choses sont la même |
| La condition que la théorie a changée pour être commode | la position peut être divisée sans fin | l'identité peut être divisée sans fin |
| Ce que montre chaque étape | il reste la moitié ; on n'est certainement pas arrivé | ce niveau n'est pas tranché ; un « non » certain |
| Issue | la marche ne finit jamais | le programme est égal à `never` |
| Résolution des manuels | les limites | la troncature |

**L'objection la plus forte :** « Interrogé sur la troncature ensembliste, le programme s'arrête à la question 1 ; la question était donc simplement mal posée. » Réponse : la troncature répond à « combien de branches y a-t-il ? » ; elle fond en une seule les manières d'être le même et ne peut pas revenir à l'univers : l'objet interrogé a changé. C'est comme répondre à Zénon par les limites : une définition déclare que l'on est arrivé, sans que la condition modifiée soit rétablie. Cette réponse est une interprétation, soumise à l'audit.

**Ce que ce n'est pas :**

- Ce n'est pas une contradiction interne de HoTT.
- Les mathématiques ne sont pour l'essentiel pas nouvelles : que de tels produits n'aient aucun niveau fini est l'exemple 8.8.6 du HoTT Book ; pour l'univers lui-même, le Book (2013) indiquait que ce devait être démontrable mais ne l'avait pas encore été ; Kraus et Sattler (2015) ont démontré que le n-ième univers d'une hiérarchie univalente n'est pas un n-type ; pour un univers unique avec types inductifs supérieurs, ce dépôt contient une preuve vérifiée par machine (CG001-C-75). Ce qui est nouveau, c'est surtout la lecture et la prémisse qu'elle désigne, au premier chef l'univalence.
- « Ne s'arrête jamais » est un théorème interne à la théorie. Le lire comme « exécuter le programme dans la réalité ne donne jamais de réponse » exige en outre la cohérence de la théorie et, pour un juge arbitraire, la canonicité.
- « Très probablement trouvé » est un jugement de la personne à l'origine du projet, non un théorème.

Pour aller plus loin (en chinois) : [document d'audit 03, « Le Zénon de HoTT »](docs/社区审计提交/03-HoTT的芝诺.md) (le plus court, qui se termine par cinq questions d'audit) ; [02, « Le fantôme du paradoxe de Russell »](docs/社区审计提交/02-罗素悖论的幽灵.md) ; [le rapport de clôture de la première phase](docs/HoTT悖论查找阶段收尾报告-20260930.md).

## 3. Le fantôme du paradoxe de Zénon : la cohérence infinie

- **Compromis :** l'univalence rend identiques les objets isomorphes ; l'identité devient donc une donnée. Par exemple, Bool est « le même » que lui-même de deux manières réellement différentes, et le transport de `true` le long de la seconde donne `false` (CG001-C-63).
- **Processus :** écrire une structure semi-simpliciale, c'est-à-dire recoller une forme niveau par niveau à partir de points, de segments, de triangles et de tétraèdres, en exigeant que les « faces des faces » s'accordent. En mathématiques classiques, c'est une définition d'une ligne.
- **Observations :** là où l'identité est un fait (Lean 4), cette ligne est toute la définition, et la cohérence hexagonale vaut par `rfl` (CG001-C-65) ; en HoTT, la même ligne accepte des données qui ne s'accordent pas, deux chemins de simplification faisant respectivement un et deux tours du cercle (CG001-C-64) ; une fois l'hexagone ajouté, il peut être rempli de plus d'une manière, et le niveau suivant (P₄) échoue pour l'un des remplissages (CG001-C-66, CG001-C-68) ; le nombre de niveaux à ajouter dépend du nombre de niveaux de l'identité (CG001-C-70) ; chaque niveau fixé peut être écrit (vérifié par machine jusqu'au niveau 5, CG001-C-62).
- **Limite :** une définition interne uniforme en le nombre de niveaux n est un problème ouvert bien connu, et son impossibilité n'a pas été démontrée. Si une définition uniforme des types semi-simpliciaux apparaît en HoTT « du livre », la forme forte de cette ligne est retirée.

Pour aller plus loin (en chinois, avec un résumé initial en anglais) : [document d'audit 01, « Le fantôme du paradoxe de Zénon »](docs/社区审计提交/01-芝诺悖论的幽灵.md).

## 4. Énoncés et éléments de preuve

- [`CLAIMS.md`](CLAIMS.md) (en chinois) : l'énoncé précis, les éléments de preuve et les extrapolations interdites de chaque énoncé ; pour chaque paquet de preuves, les exécutions principales, les contrôles négatifs et les rejeux multiplateformes.
- Sources des preuves : `HoTT/formal/`. Le `CLAIM.md` de chaque paquet donne les énoncés complets et leur portée.
- Reçus d'exécution : `HoTT/verification/runs/`, {{RUN_TOTAL}} au total : {{RUN_ACCEPTED}} acceptés par le noyau et {{RUN_REJECTED}} contrôles négatifs rejetés comme prévu (ils testent des limites précises ; ce n'est pas un historique d'échecs). Certains énoncés ont des exécutions sous macOS et sous Linux.
- [`RELEASE-MANIFEST.json`](RELEASE-MANIFEST.json) : le SHA-256 et le rôle de chacun des {{FILE_TOTAL}} fichiers de cette branche, et le commit de `dev` dont ils proviennent.

Chaîne d'outils : Cubical Agda 2.8.0 avec la bibliothèque cubical v0.9 (les options `--safe --cubical --guardedness` figurent dans chaque fichier source) ; Lean 4.34.0, bibliothèque de base seule (sans Mathlib), pour les contrôles où l'identité est un fait. Les relevés de chaîne d'outils cités par les reçus se trouvent dans `HoTT/formal/dedekind-omega-missile/` (Agda sous macOS), `HoTT/formal/claude-cg001/pedometer-ablation-lean/` (Lean sous macOS) et `HoTT/formal/cloud-opus-glm-audit/` (Linux) ; les deux premiers répertoires conservent leur emplacement sur `dev` et ne contiennent ici que ces relevés.

## 5. Comment rejouer

Une fois Agda 2.8.0, cubical v0.9 et Lean 4.34.0 installés, lancer depuis la racine du dépôt :

```sh
python3 tools/replay.py --agda /chemin/vers/agda --cubical-lib /chemin/vers/cubical/cubical.agda-lib --lean-sysroot /chemin/vers/lean-4.34.0 --jobs 4
```

Le script reconstruit la commande de chaque reçu avec des chemins relatifs, l'exécute et compare le résultat au reçu : l'issue (acceptée ou rejetée) doit concorder, et la sortie est comparée ligne par ligne après remplacement de la racine du dépôt et des chemins de bibliothèques par des marqueurs. Un contrôle négatif ne passe que s'il est de nouveau rejeté ; si sa sortie concorde aussi, il a été rejeté pour la raison enregistrée. Pour rejouer un seul reçu : `--only <identifiant>` ; pour les lister tous : `--list`. Rejouer l'ensemble à la suite prend environ une heure et demie.

Les commandes des reçus enregistrent les chemins absolus de la machine qui les a produits. Les outils d'origine, qui rejouent octet par octet, se trouvent sur la branche `dev` (`.claude/goals/CG-001-targeted-overview/tools/verify_cg001_run.py`, `Cloud-Opus审计并补完GLM/tools/verify_copus_run.py`).

## 6. Chemins cités dans les documents mais absents de cette branche

Les documents de conclusion citent aussi des fichiers du processus de recherche : le registre des propos originaux `核心认知.md`, les projections des directions et des résultats, les espaces de travail des IA, les audits et les échanges, les index propres aux objectifs, etc. Ils se trouvent tous sur la branche `dev` :

{{DEV_PATHS_TABLE}}

## 7. Branches

- `main` (cette branche) : conclusions et éléments de preuve. Elle est générée par `scripts/release/build_main_release.py` sur `dev` selon `scripts/release/main-release-spec.json`. Pour la mettre à jour, on modifie le manifeste ou les documents de conclusion sur `dev`, puis on la régénère ; aucun commit n'est fait directement sur cette branche.
- `dev` : l'ensemble du processus de recherche ; tout le travail s'y fait.
