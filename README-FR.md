# HoTT-Paradoxy : paradoxes de non-réalité en théorie homotopique des types — conclusions et éléments de preuve

[中文](README-ZH.md) · [Русский](README-RU.md) · [Deutsch](README-DE.md) · **Français** · [English](README-EN.md)

**Résumé.** Par souci d'économie et de généralité, la théorie homotopique des types (HoTT) change le statut d'« être la même chose » : ce n'est plus un fait qu'une seule vérification établit, mais une structure que l'on peut interroger niveau par niveau (« de quelles manières ces objets sont-ils les mêmes ? ») ; des objets isomorphes sont identiques (univalence), et des formes de toute dimension sont disponibles d'emblée dans l'univers (types inductifs supérieurs). Nous écrivons « décider si deux choses sont la même » sous la forme d'un programme qui interroge niveau par niveau : la k-ième question demande si cette identité est tranchée au niveau k (c'est-à-dire si le type est de h-niveau k+1) ; un juge répond à chaque question par une preuve de « oui » ou de « non » ; sur « oui », le programme s'arrête et indique le niveau. Nous démontrons en Cubical Agda que, pour tout juge, ce programme est égal au programme `never`, qui ne termine jamais, sur l'univers (avec types inductifs supérieurs) et sur le produit ∏ₙ K(ℤ,n+1) ; lorsque la hauteur des éléments est bornée, il s'arrête exactement à la question que fixe la borne ; transcrit par les mêmes équations en Lean 4, où l'identité est un simple fait, il s'arrête à la première question ; interrogé sur la troncature ensembliste, il s'arrête lui aussi à la première question, mais la troncature fond en une seule les différentes manières d'être le même et ne peut pas être décodée vers l'univers. La personne à l'origine du projet définit un paradoxe de non-réalité comme « une chose qui devrait être très simple et qui, même dans la théorie X, ne peut pas être faite » (UR) ; elle lit ce résultat comme un paradoxe de même forme que celui de Zénon et juge très probable que ce soit celui que le projet cherchait. Les mathématiques ne sont pour l'essentiel pas nouvelles : le produit est l'exemple 8.8.6 du HoTT Book ; pour l'univers, le Book (2013) indiquait que le résultat devait être démontrable mais ne l'avait pas encore été, et ce dépôt en donne une preuve vérifiée par machine. Ce qui est nouveau, c'est surtout la lecture et la prémisse qu'elle désigne, au premier chef l'univalence. Une seconde ligne : une définition uniforme des types semi-simpliciaux en HoTT « du livre » reste inconnue, un problème ouvert bien connu ; la personne à l'origine du projet a jugé que cette ligne « a ressuscité le fantôme du paradoxe de Zénon ». Toutes les affirmations positives sont vérifiées par le noyau (Cubical Agda 2.8.0 avec cubical 0.9 ; Lean 4.34.0), avec des contrôles négatifs et 107 reçus d'exécution rejouables. Nous ne prétendons pas que HoTT soit incohérente ; « très probablement trouvé » est un jugement de la personne à l'origine du projet, non un théorème.

**Mots-clés.** théorie homotopique des types ; univalence ; types inductifs supérieurs ; niveaux de troncature ; monade de délai ; cohérence infinie ; paradoxe de Zénon ; paradoxe de non-réalité

> **À propos de cette branche.** `main` ne contient que ce qui étaye les conclusions : les documents de conclusion, les énoncés précis, les sources des preuves, les reçus d'exécution et le moyen de les rejouer. L'ensemble du processus de recherche se trouve sur la [branche `dev`](https://github.com/math-fournity/HoTT-Paradoxy/tree/dev) : le registre des propos originaux de la personne à l'origine du projet, les projections des directions et des résultats, les espaces de travail des IA, les audits et les échanges, la gouvernance et l'état. Cette branche est générée à partir du commit [`17b4aec9`](https://github.com/math-fournity/HoTT-Paradoxy/commit/17b4aec95f124329d4d5b43dc30611ae8369a358) de `dev` selon un manifeste ([`RELEASE-MANIFEST.json`](RELEASE-MANIFEST.json)) et n'est pas modifiée directement. Ce README existe aussi en chinois, en russe, en allemand et en anglais, avec le même contenu. Les documents de conclusion, le rapport de clôture et `CLAIMS.md` sont rédigés en chinois ; les documents 01 et 02 commencent par un résumé en anglais.

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
- Reçus d'exécution : `HoTT/verification/runs/`, 107 au total : 49 acceptés par le noyau et 58 contrôles négatifs rejetés comme prévu (ils testent des limites précises ; ce n'est pas un historique d'échecs). Certains énoncés ont des exécutions sous macOS et sous Linux.
- [`RELEASE-MANIFEST.json`](RELEASE-MANIFEST.json) : le SHA-256 et le rôle de chacun des 678 fichiers de cette branche, et le commit de `dev` dont ils proviennent.

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

| Chemin | Sur `dev` |
|---|---|
| `.claude/goals/CG-001-targeted-overview` | [ouvrir](https://github.com/math-fournity/HoTT-Paradoxy/tree/dev/.claude/goals/CG-001-targeted-overview) |
| `.claude/goals/CG-001-targeted-overview/证据索引.md` | [ouvrir](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/.claude/goals/CG-001-targeted-overview/%E8%AF%81%E6%8D%AE%E7%B4%A2%E5%BC%95.md) |
| `.claude/goals/CG-002-a7-infinite-coherence` | [ouvrir](https://github.com/math-fournity/HoTT-Paradoxy/tree/dev/.claude/goals/CG-002-a7-infinite-coherence) |
| `.claude/goals/CG-003-a7-self-audit` | [ouvrir](https://github.com/math-fournity/HoTT-Paradoxy/tree/dev/.claude/goals/CG-003-a7-self-audit) |
| `.claude/思考与发现` | [ouvrir](https://github.com/math-fournity/HoTT-Paradoxy/tree/dev/.claude/%E6%80%9D%E8%80%83%E4%B8%8E%E5%8F%91%E7%8E%B0) |
| `.claude/总索引.md` | [ouvrir](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/.claude/%E6%80%BB%E7%B4%A2%E5%BC%95.md) |
| `.claude/调研请求/20260930-相同永远了结不了-社区先例调研请求.md` | [ouvrir](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/.claude/%E8%B0%83%E7%A0%94%E8%AF%B7%E6%B1%82/20260930-%E7%9B%B8%E5%90%8C%E6%B0%B8%E8%BF%9C%E4%BA%86%E7%BB%93%E4%B8%8D%E4%BA%86-%E7%A4%BE%E5%8C%BA%E5%85%88%E4%BE%8B%E8%B0%83%E7%A0%94%E8%AF%B7%E6%B1%82.md) |
| `Cloud-Opus审计并补完GLM` | [ouvrir](https://github.com/math-fournity/HoTT-Paradoxy/tree/dev/Cloud-Opus%E5%AE%A1%E8%AE%A1%E5%B9%B6%E8%A1%A5%E5%AE%8CGLM) |
| `Cloud-Opus审计并补完GLM/01-工具链与复现.md` | [ouvrir](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/Cloud-Opus%E5%AE%A1%E8%AE%A1%E5%B9%B6%E8%A1%A5%E5%AE%8CGLM/01-%E5%B7%A5%E5%85%B7%E9%93%BE%E4%B8%8E%E5%A4%8D%E7%8E%B0.md) |
| `Cloud-Opus审计并补完GLM/02-断裂审计-逐命题（D1）.md` | [ouvrir](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/Cloud-Opus%E5%AE%A1%E8%AE%A1%E5%B9%B6%E8%A1%A5%E5%AE%8CGLM/02-%E6%96%AD%E8%A3%82%E5%AE%A1%E8%AE%A1-%E9%80%90%E5%91%BD%E9%A2%98%EF%BC%88D1%EF%BC%89.md) |
| `Cloud-Opus审计并补完GLM/11-收据核验结果.json` | [ouvrir](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/Cloud-Opus%E5%AE%A1%E8%AE%A1%E5%B9%B6%E8%A1%A5%E5%AE%8CGLM/11-%E6%94%B6%E6%8D%AE%E6%A0%B8%E9%AA%8C%E7%BB%93%E6%9E%9C.json) |
| `Cloud-Opus审计并补完GLM/13-外部复核请求.md` | [ouvrir](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/Cloud-Opus%E5%AE%A1%E8%AE%A1%E5%B9%B6%E8%A1%A5%E5%AE%8CGLM/13-%E5%A4%96%E9%83%A8%E5%A4%8D%E6%A0%B8%E8%AF%B7%E6%B1%82.md) |
| `Cloud-Opus审计并补完GLM/14-罗素面终局判词.md` | [ouvrir](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/Cloud-Opus%E5%AE%A1%E8%AE%A1%E5%B9%B6%E8%A1%A5%E5%AE%8CGLM/14-%E7%BD%97%E7%B4%A0%E9%9D%A2%E7%BB%88%E5%B1%80%E5%88%A4%E8%AF%8D.md) |
| `Cloud-Opus审计并补完GLM/README.md` | [ouvrir](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/Cloud-Opus%E5%AE%A1%E8%AE%A1%E5%B9%B6%E8%A1%A5%E5%AE%8CGLM/README.md) |
| `Cloud-Opus审计并补完GLM/tools` | [ouvrir](https://github.com/math-fournity/HoTT-Paradoxy/tree/dev/Cloud-Opus%E5%AE%A1%E8%AE%A1%E5%B9%B6%E8%A1%A5%E5%AE%8CGLM/tools) |
| `Cloud-Opus审计并补完GLM/tools/capture_zeno_line_replays.sh` | [ouvrir](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/Cloud-Opus%E5%AE%A1%E8%AE%A1%E5%B9%B6%E8%A1%A5%E5%AE%8CGLM/tools/capture_zeno_line_replays.sh) |
| `Cloud-Opus审计并补完GLM/附件/20260926-Session问答原文存档（用户上传，GLM-Auditor会话）.md` | [ouvrir](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/Cloud-Opus%E5%AE%A1%E8%AE%A1%E5%B9%B6%E8%A1%A5%E5%AE%8CGLM/%E9%99%84%E4%BB%B6/20260926-Session%E9%97%AE%E7%AD%94%E5%8E%9F%E6%96%87%E5%AD%98%E6%A1%A3%EF%BC%88%E7%94%A8%E6%88%B7%E4%B8%8A%E4%BC%A0%EF%BC%8CGLM-Auditor%E4%BC%9A%E8%AF%9D%EF%BC%89.md) |
| `Cloud-Opus审计并补完GLM/附件/工作过程文件/自查轮/verify-all-rerun-46个运行.json` | [ouvrir](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/Cloud-Opus%E5%AE%A1%E8%AE%A1%E5%B9%B6%E8%A1%A5%E5%AE%8CGLM/%E9%99%84%E4%BB%B6/%E5%B7%A5%E4%BD%9C%E8%BF%87%E7%A8%8B%E6%96%87%E4%BB%B6/%E8%87%AA%E6%9F%A5%E8%BD%AE/verify-all-rerun-46%E4%B8%AA%E8%BF%90%E8%A1%8C.json) |
| `GLM-5.3-Flash/README.md` | [ouvrir](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/GLM-5.3-Flash/README.md) |
| `GLM-5.3-Flash/审计请求` | [ouvrir](https://github.com/math-fournity/HoTT-Paradoxy/tree/dev/GLM-5.3-Flash/%E5%AE%A1%E8%AE%A1%E8%AF%B7%E6%B1%82) |
| `GLM-5.3-Flash/思考与发现` | [ouvrir](https://github.com/math-fournity/HoTT-Paradoxy/tree/dev/GLM-5.3-Flash/%E6%80%9D%E8%80%83%E4%B8%8E%E5%8F%91%E7%8E%B0) |
| `GLM-5.3-Flash/策略快照/20260926-D2后罗素线策略-大白话快照.md` | [ouvrir](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/GLM-5.3-Flash/%E7%AD%96%E7%95%A5%E5%BF%AB%E7%85%A7/20260926-D2%E5%90%8E%E7%BD%97%E7%B4%A0%E7%BA%BF%E7%AD%96%E7%95%A5-%E5%A4%A7%E7%99%BD%E8%AF%9D%E5%BF%AB%E7%85%A7.md) |
| `GLM-5.3-Flash/裁定问题/20260926-M2-形成规则是回答还是回避-两面陈词.md` | [ouvrir](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/GLM-5.3-Flash/%E8%A3%81%E5%AE%9A%E9%97%AE%E9%A2%98/20260926-M2-%E5%BD%A2%E6%88%90%E8%A7%84%E5%88%99%E6%98%AF%E5%9B%9E%E7%AD%94%E8%BF%98%E6%98%AF%E5%9B%9E%E9%81%BF-%E4%B8%A4%E9%9D%A2%E9%99%88%E8%AF%8D.md) |
| `HoTT/CLAIM_EVIDENCE_MATRIX.md` | [ouvrir](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/HoTT/CLAIM_EVIDENCE_MATRIX.md) |
| `HoTT/verification/PROOF_VERSION_CLOSURE.json` | [ouvrir](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/HoTT/verification/PROOF_VERSION_CLOSURE.json) |
| `README.md` | [ouvrir](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/README.md) |
| `Terra对Opus的审计` | [ouvrir](https://github.com/math-fournity/HoTT-Paradoxy/tree/dev/Terra%E5%AF%B9Opus%E7%9A%84%E5%AE%A1%E8%AE%A1) |
| `Terra对Opus的审计/Opus给GPT的回应` | [ouvrir](https://github.com/math-fournity/HoTT-Paradoxy/tree/dev/Terra%E5%AF%B9Opus%E7%9A%84%E5%AE%A1%E8%AE%A1/Opus%E7%BB%99GPT%E7%9A%84%E5%9B%9E%E5%BA%94) |
| `rulings.md` | [ouvrir](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/rulings.md) |
| `scripts/audit/verify_math_proof_delivery_governance.py` | [ouvrir](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/scripts/audit/verify_math_proof_delivery_governance.py) |
| `scripts/audit/verify_proof_version_closure.py` | [ouvrir](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/scripts/audit/verify_proof_version_closure.py) |
| `sources/prompts/Claude-UR与芝诺的模式匹配-用户原文-20260930.md` | [ouvrir](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/sources/prompts/Claude-UR%E4%B8%8E%E8%8A%9D%E8%AF%BA%E7%9A%84%E6%A8%A1%E5%BC%8F%E5%8C%B9%E9%85%8D-%E7%94%A8%E6%88%B7%E5%8E%9F%E6%96%87-20260930.md) |
| `sources/prompts/Claude-归因是正题-用户原文-20260924.md` | [ouvrir](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/sources/prompts/Claude-%E5%BD%92%E5%9B%A0%E6%98%AF%E6%AD%A3%E9%A2%98-%E7%94%A8%E6%88%B7%E5%8E%9F%E6%96%87-20260924.md) |
| `sources/prompts/Claude-罗素原则P1至P3-用户原文-20260926.md` | [ouvrir](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/sources/prompts/Claude-%E7%BD%97%E7%B4%A0%E5%8E%9F%E5%88%99P1%E8%87%B3P3-%E7%94%A8%E6%88%B7%E5%8E%9F%E6%96%87-20260926.md) |
| `sources/prompts/Codex-非现实性悖论的目标与A向读法-用户原文-20260930.md` | [ouvrir](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/sources/prompts/Codex-%E9%9D%9E%E7%8E%B0%E5%AE%9E%E6%80%A7%E6%82%96%E8%AE%BA%E7%9A%84%E7%9B%AE%E6%A0%87%E4%B8%8EA%E5%90%91%E8%AF%BB%E6%B3%95-%E7%94%A8%E6%88%B7%E5%8E%9F%E6%96%87-20260930.md) |
| `sources/prompts/GLM-算符先行于存在性落定-用户原文-20260926.md` | [ouvrir](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/sources/prompts/GLM-%E7%AE%97%E7%AC%A6%E5%85%88%E8%A1%8C%E4%BA%8E%E5%AD%98%E5%9C%A8%E6%80%A7%E8%90%BD%E5%AE%9A-%E7%94%A8%E6%88%B7%E5%8E%9F%E6%96%87-20260926.md) |
| `全景视野.md` | [ouvrir](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/%E5%85%A8%E6%99%AF%E8%A7%86%E9%87%8E.md) |
| `扩展认知.md` | [ouvrir](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/%E6%89%A9%E5%B1%95%E8%AE%A4%E7%9F%A5.md) |
| `扩展认知/011 - 本来应该很简单的事：UR 与芝诺的模式匹配.md` | [ouvrir](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/%E6%89%A9%E5%B1%95%E8%AE%A4%E7%9F%A5/011%20-%20%E6%9C%AC%E6%9D%A5%E5%BA%94%E8%AF%A5%E5%BE%88%E7%AE%80%E5%8D%95%E7%9A%84%E4%BA%8B%EF%BC%9AUR%20%E4%B8%8E%E8%8A%9D%E8%AF%BA%E7%9A%84%E6%A8%A1%E5%BC%8F%E5%8C%B9%E9%85%8D.md) |
| `方向追踪.md` | [ouvrir](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/%E6%96%B9%E5%90%91%E8%BF%BD%E8%B8%AA.md) |
| `核心认知.md` | [ouvrir](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/%E6%A0%B8%E5%BF%83%E8%AE%A4%E7%9F%A5.md) |

## 7. Branches

- `main` (cette branche) : conclusions et éléments de preuve. Elle est générée par `scripts/release/build_main_release.py` sur `dev` selon `scripts/release/main-release-spec.json`. Pour la mettre à jour, on modifie le manifeste ou les documents de conclusion sur `dev`, puis on la régénère ; aucun commit n'est fait directement sur cette branche.
- `dev` : l'ensemble du processus de recherche ; tout le travail s'y fait.
