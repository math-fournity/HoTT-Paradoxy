<!-- translation:v1
source: docs/社区审计提交/03-HoTT的芝诺.md
source_sha256: bea7f03052d2e242a97b0a51e5dd22dc5371119668042a96f3181eba22b26c53
language: fr
translator: Claude Opus 5.5 (AI), 2026-10-01; version 2 changes 2026-10-15
authority: the Chinese original is authoritative
-->
# Le Zénon de HoTT

[中文](03-HoTT的芝诺.md) · [Русский](03-HoTT的芝诺-RU.md) · [Deutsch](03-HoTT的芝诺-DE.md) · **Français** · [English](03-HoTT的芝诺-EN.md)

> *Traduction par IA (Claude Opus 5.5, 2026-10-01 ; les changements de la version 2 : 2026-10-15) de l'original chinois [`03-HoTT的芝诺.md`](03-HoTT的芝诺.md), qui fait foi. Les propos de la personne à l'origine du projet sont cités dans l'original chinois, chacun suivi d'une traduction signalée ; le code, les chemins de fichiers et les identifiants sont inchangés.*

**Pourquoi « être la même chose » ne se tranche jamais dans son univers**

Document d'audit pour la communauté · version 2 · 2026-10-15 · dépôt `math-fournity/HoTT-Paradoxy`

La version 1 date du 2026-09-30. La version 2 ne change que ce qu'exige la décision du 2026-10-15 de la personne à l'origine du projet : « quelle prémisse incriminer » et les deux passages qui y sont liés (les deux premiers points de « Ce que cela montre » et la question d'audit 3) ; elle ajoute sous « Preuves » un théorème qui rassemble les contrôles.

> **À qui il s'adresse** : aux lecteurs non mathématiciens prêts à suivre le raisonnement, et aux mathématiciens prêts à l'auditer.
>
> **Statut** : le jugement selon lequel quelque chose est « déraisonnable » appartient à la personne à l'origine de la recherche ; le raisonnement est prouvé par machine dans un périmètre déclaré (voir « Preuves » à la fin) ; le reste est interprétation. Ce document n'affirme **pas** que HoTT est incohérente, ni que ses règles sont mathématiquement fausses.
>
> **Rapport avec le document jumeau** : [02 Le fantôme du paradoxe de Russell](02-罗素悖论的幽灵-FR.md) montre une autre face des mêmes preuves machine, à savoir le schéma russellien « la théorie traite comme déjà livré ce qui n'est pas encore fixé » (direction B). Le présent document expose la lecture du 2026-09-30 de la personne à l'origine du projet : réalisable dans la réalité, irréalisable dans la théorie (direction A). Les deux se partagent le travail : le phénomène dans la HoTT du livre relève de la direction A ; « déclarer l'achèvement par définition » dans les réparations relève de la direction B.

## D'abord, Zénon

Aller d'ici à là-bas : on y va, et l'on y est. Mais si l'on pense la distance comme divisible à l'infini, « arriver » ne se conclut jamais : on parcourt d'abord la moitié, il reste une moitié ; encore la moitié, il reste encore une moitié. À chaque pas, on n'est assurément pas encore arrivé, et le chemin ne s'achève jamais. Le raisonnement n'est pas faux, et pourtant on voit d'un coup d'œil que c'est déraisonnable. Le défaut est dans la prémisse.

La personne à l'origine du projet appelle UR ce genre de déraisonnable :

> 本来应该很简单的事情，甚至在X理论中，都做不到。

Traduction : « Une chose qui devrait être très simple et qui, même dans la théorie X, ne peut pas être faite. »

La « réalité » désigne la première moitié de la phrase, c'est-à-dire la chose qui devrait être très simple ; le « paradoxe » désigne la phrase entière.

## Une chose qui devrait être très simple

Deux choses sont-elles la même ? Dans la logique et les mathématiques ordinaires, c'est l'affaire d'une phrase. Elles le sont ou ne le sont pas ; il n'y a pas de « de quelle manière elles le sont ».

## Ce que la théorie homotopique des types a changé pour être commode

La théorie homotopique des types (HoTT) a deux traits de conception très séduisants.

- **L'univalence** : des choses isomorphes sont la même chose. C'est très économique : deux choses de même structure n'ont plus à être distinguées, et les théorèmes se transportent directement.
- **Les types inductifs supérieurs** : toutes sortes de formes (cercles, sphères et formes de dimension arbitrairement élevée) sont disponibles d'un coup dans l'univers des types. C'est très général : on peut faire de la géométrie directement dans la logique.

Ensemble, ils font qu'« être la même chose » n'est plus l'affaire d'une phrase mais une structure à étages : de quelles manières ces choses sont-elles les mêmes ? De quelles manières ces manières sont-elles les mêmes ? Au-dessus de chaque étage, il y en a un autre.

## Le processus qui la vise

Nous avons écrit un programme très simple qui pose la question niveau par niveau : « pour les choses de ce catalogue, la question de savoir si elles sont les mêmes est-elle tranchée à ce niveau ? » Le niveau 1 demande « est-ce l'affaire d'une phrase ? » ; si la réponse est « non », il demande le niveau 2, et ainsi de suite. Quand la réponse est « oui », il s'arrête et indique le niveau. À chaque niveau, quelqu'un (un juge) donne un « oui » ou un « non » accompagné d'une preuve, de sorte que le programme peut toujours faire son pas suivant.

## Résultats

- Dans un monde où « l'identité est un fait établi par une seule vérification » (un autre assistant de preuve, Lean, avec le même programme transcrit selon les mêmes équations), interrogé sur son propre univers, le programme s'arrête au niveau 1.
- Dans HoTT, si l'on plafonne la « hauteur » des choses du catalogue, le programme s'arrête exactement au niveau que fixe le plafond.
- Dans HoTT, interrogé sur son univers, ou sur un produit infini ordinaire, le programme **ne s'arrête jamais** : chaque niveau répond un « non » certain, et au-dessus de chaque niveau il y en a un autre. Cela vaut pour tout juge ; c'est un théorème prouvé par machine, non pas « il a tourné longtemps sans s'arrêter ».

Même question, même programme : en ne changeant que « ce qu'est l'identité » et « si la hauteur a un plafond », l'issue passe de « tranché en un pas » à « jamais tranché ». Voilà le Zénon de HoTT : à chaque niveau, ce n'est assurément pas encore tranché, et la confirmation ne peut jamais s'achever.

## La réponse des manuels, et pourquoi elle ne fait pas disparaître le problème

À Zénon, le manuel répond : prenez les limites ; 1/2 + 1/4 + … vaut exactement 1. Ici, le manuel répondrait : interrogez plutôt la « troncature ensembliste » ; là, « être le même » est décrété affaire d'une phrase, et le programme s'arrête au niveau 1.

Nous l'avons aussi vérifié par machine : il s'arrête bien au niveau 1. Mais il s'arrête parce qu'une règle déclare à nouveau qu'« être le même est l'affaire d'une phrase ». Après la troncature, les deux manières dont Bool est le même que lui-même (ne rien bouger, et échanger vrai et faux) sont fusionnées en une seule ; et le résultat ne peut plus jamais être décodé dans l'univers d'origine. L'objet interrogé a été remplacé.

La limite déclare « arrivé » par une définition ; la troncature déclare « l'identité est un fait » par un constructeur. Ce sont deux mathématiques légitimes, mais aucune ne rétablit la condition modifiée elle-même. Elles répondent donc à une question plus facile et ne font pas disparaître le déraisonnable d'origine.

## Ce que cela montre

- Chez Zénon, l'accusée est « la position peut être divisée sans fin » ; son pendant ici est « **l'identité peut être divisée sans fin** ». Elle est faite de deux choses ensemble : l'identité est une structure (univalence), et l'univers livre d'un coup des choses de toutes les hauteurs (les types inductifs supérieurs fournissent ces hauteurs).
- Les contrôles séparent les deux : remplacez « l'identité est une structure » par « l'identité est un fait » (Lean), et le programme s'arrête au niveau 1 ; gardez « l'identité est une structure » et plafonnez seulement la hauteur, et il s'arrête au plafond ; ce n'est qu'avec les deux qu'il ne s'arrête jamais. Le contrôle Lean remplace tout « l'identité est une structure », pas seulement l'univalence. Par la suite, ce groupe de contrôles a été écrit comme un seul théorème valable pour toute collection (C-430) : avec les deux, le programme ne s'arrête jamais ; plafonnez la hauteur des membres, et il s'arrête au plafond ; gardez les membres exactement comme dans l'exemple de l'univers, avec toutes les hauteurs, et faites seulement de l'« identité » de la numérotation du catalogue un fait, et il s'arrête au niveau 1.
- Selon le raisonnement par l'absurde, ce qu'il faut réexaminer, c'est l'abstraction que la théorie a faite pour être commode. Le théorème est symétrique en ces deux choses ; il dit seulement qu'on ne peut retirer ni l'une ni l'autre. Laquelle est l'abstraction irréaliste, c'est la décision du 2026-10-15 de la personne à l'origine du projet : il n'y a qu'un seul accusé, la « **collection toute faite** », c'est-à-dire que l'univers livre d'un coup, comme quelque chose de déjà là, un tout dont la confirmation demanderait une infinité de niveaux. L'univalence est l'une des causes et elle est conservée.
  - Du côté de la théorie des ensembles (ZFC), la personne à l'origine du projet appelle cet acte A (2026-10-14, propos originaux) : “A就是一个无限的步骤才能到达，从而存在的结果，当作已经存在的结果，参与运算。” Traduction : « A, c'est ceci : un résultat qu'on n'atteint qu'au bout d'une infinité d'étapes, et qui n'existe qu'à ce titre, est traité comme un résultat déjà existant et entre dans les calculs. »
  - Il ne partage que la lettre avec la « direction A » du début de ce document ; ce n'est pas la même chose. Le phénomène de ce document relève de la direction A (réalisable dans la réalité, pas dans la théorie), tandis que l'accusé est un acte de la direction B, comme dans le document jumeau 02 (traiter comme déjà livré ce qui n'est pas encore fixé).
  - La version 1 de ce document donnait ici notre propre classement (examiner d'abord l'univalence, les types inductifs supérieurs en second) ; il est corrigé conformément à la décision.

## Ce que ce n'est pas

- Ce n'est pas une contradiction interne de HoTT. Tout le raisonnement est accepté par la machine dans HoTT.
- Les faits mathématiques ne sont pour la plupart pas nouveaux : que de tels produits n'aient aucun niveau fini, c'est l'exemple 8.8.6 du HoTT Book. Pour l'univers lui-même, le livre écrit (fin du §8.8) qu'on s'attend à pouvoir prouver aussi qu'il n'est un n-type pour aucun n, mais que cela n'a pas encore été fait ; Kraus–Sattler 2015 ont prouvé que le n-ième univers d'une hiérarchie univalente n'est pas un n-type, sans types inductifs supérieurs. Qu'un univers unique avec types inductifs supérieurs ne soit un n-type pour aucun n a une preuve machine dans ce dépôt (C-75, voir 02) ; si une preuve publiée est parue depuis dans la littérature, nous ne l'avons pas encore vérifié. La série géométrique, tout le monde sait la sommer depuis longtemps ; la nouveauté de Zénon est dans la lecture, et il en va de même ici. Cette lecture n'a pas non plus encore été confrontée à la littérature.
- Ce n'est pas « dans tous les cas » : cela apparaît sur l'univers et sur les objets de ce genre dont la hauteur n'est pas bornée. Mais l'univers n'est pas un cas marginal : c'est exactement l'objet dont parle l'univalence, et un élément du domaine que HoTT ne peut pas refuser.

## Preuves

- Le programme de questionnement, et le non-arrêt sur l'univers : `HoTT/formal/claude-cg001/questioning-delay/CLAIM.md` (C-77 à C-79) ; le contrôle Lean dans le monde des faits : C-80 dans le même `CLAIM.md`.
- Le non-arrêt sur un produit ordinaire, et le contrôle plafonné : `HoTT/formal/claude-cg001/product-questioning/CLAIM.md` (C-81, C-82).
- Le contrôle par troncature : `HoTT/formal/claude-cg001/truncation-questioning/CLAIM.md` (C-83).
- Les deux causes écrites comme un seul théorème pour toute collection, l'univalence étant isolée à part : `HoTT/formal/claude-cg001/a-univalence-b/CLAIM.md` (C-430, 2026-10-15). Il rassemble les contrôles ci-dessus ; ce n'est pas un phénomène nouveau.
- Exécutions et rejeux exacts : `.claude/goals/CG-001-targeted-overview/证据索引.md` §20–§23 ; la dernière section de la matrice de preuves partagée du projet, `HoTT/CLAIM_EVIDENCE_MATRIX.md`, enregistre le même lot d'énoncés. Périmètre : Cubical Agda 2.8.0 avec cubical 0.9 (C-80 dans Lean 4.34.0) ; C-77 à C-80 rejoués de façon concordante sur deux plateformes, Linux et macOS ; C-81 à C-83 rejoués seulement sur macOS.
- Les propos originaux de la personne à l'origine du projet et la lecture complète qu'en fait l'IA : KC-000052 à KC-000054 dans `核心认知.md` ; `扩展认知/011 - 本来应该很简单的事：UR 与芝诺的模式匹配.md`.

## Questions pour l'audit de la communauté

1. **Mathématiques** : les énoncés formels listés à la fin sont-ils vrais ? Disent-ils ce que dit le texte ? En particulier : le sens précis de « le programme de questionnement est égal à `never` » (aucune quantité finie de carburant ne donne de réponse), et son rapport avec « chaque niveau répond non ».
2. **La tâche** : « savoir si deux choses sont la même est, d'ordinaire, l'affaire d'une phrase » — est-ce une description équitable de la logique et des mathématiques ordinaires ? La mettre en œuvre comme « demander niveau par niveau jusqu'à quel niveau l'identité est tranchée », est-ce la même chose ?
3. **Attribution** : la condition modifiée est-elle « l'identité peut être divisée sans fin » ? La personne à l'origine du projet a désigné la « collection toute faite » comme accusé et rangé l'univalence parmi les causes : cette attribution tient-elle ? Y a-t-il des attributions concurrentes auxquelles nous n'avons pas pensé ?
4. **Réponses standard** : la troncature, le fait de ne faire des mathématiques qu'au niveau des ensembles, ou la stratification des univers peuvent-ils supprimer le déraisonnable ici ? Que coûte chacune de ces réponses ?
5. **Précédents** : quelqu'un a-t-il déjà lu ces faits mathématiques de cette manière ? Par ailleurs : qu'un univers unique avec types inductifs supérieurs ne soit un n-type pour aucun n n'était pas démontré quand le HoTT Book a été écrit (2013) ; l'a-t-il été depuis dans la littérature ?
