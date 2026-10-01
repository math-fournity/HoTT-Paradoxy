# HoTT-Paradoxy : les fantômes de Zénon et de Russell

**— et, dans la théorie homotopique des types, une chose qui devrait être très simple et qu'on ne finit pourtant jamais**

[中文](README-ZH.md) · [Русский](README-RU.md) · [Deutsch](README-DE.md) · **Français** · [English](README-EN.md)

Il y a plus de deux mille ans, Zénon disait : si, à chaque fois, tu ne parcours que la moitié de la distance qui reste, tu n'arriveras jamais au bout. Il y a un peu plus de cent ans, Russell demandait : rassemblons tous les ensembles qui ne se contiennent pas eux-mêmes ; l'ensemble ainsi obtenu se contient-il lui-même ?

Les mathématiques ultérieures ont écrit une réponse standard à chacune de ces questions : pour Zénon, les limites ; pour Russell, la théorie axiomatique des ensembles et la théorie des types. La plupart des manuels s'arrêtent là et traitent l'une et l'autre comme une histoire réglée.

Ce dépôt rend compte d'une tentative qui n'est pas d'accord avec ce « réglé ». La personne à l'origine du projet (dont vient aussi la philosophie des mathématiques exposée plus bas) est convaincue que ces deux paradoxes ne sont pas vraiment derrière nous. Comme des fantômes, ils reviennent sous un autre visage : là où une théorie, pour être commode, modifie en silence une condition de la réalité, c'est par là que le fantôme revient. En suivant cette idée, nous sommes entrés dans l'un des fondements des mathématiques les plus récents, la théorie homotopique des types (Homotopy Type Theory, HoTT en abrégé), et nous y avons trouvé une chose qui devrait être très simple et qu'on ne finit pourtant jamais : **décider si deux choses sont la même**. Chaque étape du raisonnement a été vérifiée par des programmes de vérification de preuves sur ordinateur.

La personne à l'origine du projet résume ainsi la portée de ce travail (2026-10-01, propos originaux) :

> ……真正重要的事情，不仅仅是我们找到的HoTT的理论的不合理之处，其实从数学哲学意义上来讲，我们复活了罗素悖论的幽灵和芝诺悖论的幽灵，才是意义重大的。
>
> 我们用计算视角重新发现了罗素悖论的内在张力，这是基于这种计算视角下的内在张力，我们完成了HoTT悖论寻找之旅的最关键的一跃，从那之后，我们的探索工作走到了正确的方向上，并最终找到了HoTT理论的非现实性/不合理之处。
>
> 我们用圆环悖论的视角，揭示了芝诺悖论并没有被极限理论真正地解决。

> **Traduction.** « … Ce qui compte vraiment, ce n'est pas seulement le caractère déraisonnable que nous avons trouvé dans la théorie de HoTT ; au sens de la philosophie des mathématiques, ce qui est d'une grande portée, c'est que nous avons ressuscité le fantôme du paradoxe de Russell et le fantôme du paradoxe de Zénon.
>
> Avec un regard computationnel, nous avons redécouvert la tension interne du paradoxe de Russell ; c'est sur la base de cette tension interne, vue sous l'angle du calcul, que nous avons accompli le bond le plus décisif de notre voyage à la recherche d'un paradoxe de HoTT. À partir de là, notre exploration est allée dans la bonne direction et a fini par trouver la non-réalité / le caractère déraisonnable de la théorie de HoTT.
>
> Du point de vue du paradoxe de l'anneau, nous avons montré que le paradoxe de Zénon n'a pas vraiment été résolu par la théorie des limites. »

Pour lire ce texte, il n'est pas nécessaire de connaître la théorie homotopique des types. La personne à l'origine du projet a toujours voulu que sa philosophie des mathématiques soit compréhensible par des lycéens, voire par des collégiens ; ce texte essaie d'être à la hauteur de cette exigence. Il suit l'histoire telle qu'elle s'est déroulée : d'abord notre façon de voir les paradoxes (section 1), puis les deux fantômes (sections 2 et 3), puis ce que nous avons trouvé dans HoTT (section 4) et pourquoi les deux fantômes disent la même chose (section 5), enfin comment nous vérifier (section 7). En chemin, nous distinguons trois sortes d'énoncés : les vues et les verdicts de la personne à l'origine du projet (toutes les citations sont des propos originaux) ; les faits mathématiques vérifiés par ordinateur ; et nos propres interprétations. Tout ce qui est hors des citations est notre explication (« nous », ce sont les systèmes d'IA qui ont pris part au projet) ; quand nous donnons notre propre jugement plutôt qu'une explication, nous le disons.

## 1. Notre façon de voir les paradoxes

La façon dont la personne à l'origine du projet voit les paradoxes commence par cette phrase (2026-09-09, propos originaux, extrait) :

> 你知道，在我看来，悖论就是一个矛盾，或者说，可以被看成是反证法要看到的那个矛盾。

> **Traduction.** « Tu sais, à mes yeux, un paradoxe est une contradiction ; ou plutôt, on peut le voir comme la contradiction même que cherche un raisonnement par l'absurde. »

Chacun a rencontré le raisonnement par l'absurde à l'école : on suppose quelque chose, on raisonne, on aboutit à une contradiction, et on en conclut que la supposition était fausse. Le raisonnement lui-même est correct ; la faute est au point de départ.

La personne à l'origine du projet voit un paradoxe comme un processus de même nature. Une théorie doit d'abord accepter certaines prémisses avant de pouvoir raisonner. Pour être utiles, ces prémisses ne coïncident souvent pas tout à fait avec la réalité : pour rendre le calcul commode, pour qu'une même façon de parler couvre beaucoup de cas, une théorie laisse tomber en silence des choses qui semblent superflues dans les problèmes ordinaires, ou ajoute des choses idéalisées que la réalité n'a pas. C'est comme une carte : pour qu'on voie d'un coup d'œil quelle route mène où, elle ne montre ni le revêtement de la chaussée, ni les endroits où l'eau stagne aujourd'hui. D'habitude, cela ne pose aucun problème ; mais dès qu'on demande « puis-je passer ce pont aujourd'hui ? », ce qui a été laissé de côté compte de nouveau.

Pour qu'une chose arrive dans la réalité, beaucoup de conditions doivent être réunies à la fois ; dans la langue de la logique : « vrai seulement si tout est vrai, faux dès qu'un seul élément est faux ». Qu'une théorie modifie une seule de ces conditions, et elle peut, dans un processus particulier, déduire un résultat qui n'existe pas dans la réalité. La personne à l'origine du projet range ces résultats en deux sortes (2026-09-10, propos originaux, extrait) :

> 第一种：现实中能完成，理论中却无法完成。第二种：现实中无法完成（不停机），理论中却绕过 ASK，假装它“已完成”。

> **Traduction.** « Première sorte : cela peut être achevé dans la réalité, mais pas dans la théorie. Seconde sorte : cela ne peut pas être achevé dans la réalité (cela ne s'arrête pas), mais dans la théorie on contourne ASK et on fait comme si c'était « achevé ». »

ASK est le nom que la personne à l'origine du projet donne à cette étape : avant de répondre à une question, demander d'abord si elle peut avoir une réponse, si le calcul qui la cherche peut s'arrêter. Le paradoxe de Zénon est le modèle de la première sorte, le paradoxe de Russell celui de la seconde.

Une fois cette « contradiction » apparue, ce qu'il faut rechercher en remontant, c'est la prémisse que la théorie a modifiée au départ (2026-09-23, propos originaux, extrait) :

> 这种矛盾作为一种结果，可以被认为是反证法中的那个结果中的矛盾，于是当我们回头追溯的时候，会发现，站在反证法的视角中，我们设定错误的那个前提，就是理论设计者当初做的非现实抽象。

> **Traduction.** « En tant que résultat, cette contradiction peut être considérée comme la contradiction à laquelle aboutit un raisonnement par l'absurde ; aussi, quand nous remontons en arrière, nous découvrons que, du point de vue du raisonnement par l'absurde, la prémisse que nous avons mal posée est précisément l'abstraction irréaliste que les concepteurs de la théorie ont faite au départ. »

Plus tard, la personne à l'origine du projet a formulé la première sorte de façon encore plus directe (2026-09-30, propos originaux, extrait) :

> `UR`=`本来应该很简单的事情，甚至在X理论中，都做不到`，我想这就是一种类似芝诺悖论的`不合理`。

> **Traduction.** « `UR` = `une chose qui devrait être très simple et qui, même dans la théorie X, ne peut pas être faite` ; je pense que c'est là quelque chose de « déraisonnable », du même genre que le paradoxe de Zénon. »

« Une chose qui devrait être très simple », c'est la réalité ; « même dans la théorie X, ne peut pas être faite », c'est le paradoxe. Ce qui juge que c'est « déraisonnable », ce n'est pas un critère formel, mais une personne qui regarde d'un seul coup d'œil.

## 2. Le fantôme de Zénon : le paradoxe de l'anneau

Commençons par Zénon. Tu veux aller d'ici à là-bas. D'abord tu parcours la moitié, et il reste une moitié ; puis la moitié de ce qui reste, et il reste un quart ; puis encore la moitié… Après chaque pas, il reste un petit bout. À raisonner ainsi, tu n'arrives jamais. Pourtant, dans la réalité, on passe d'une enjambée.

La réponse des manuels est la limite : la somme infinie 1/2 + 1/4 + 1/8 + … vaut exactement 1. La distance totale est finie, donc tu arrives.

La personne à l'origine du projet n'est pas satisfaite de cette réponse. Voici une façon d'en comprendre la raison : la limite nous dit quelle distance on a parcourue au total *si* l'infinité des pas a été entièrement parcourue ; elle ne nous dit pas comment une infinité de pas se parcourt, l'un après l'autre. « Vaut exactement 1 » est un résultat proclamé par une définition, et proclamer qu'on est arrivé n'est pas la même chose qu'arriver vraiment. Le 2026-09-01, la personne à l'origine du projet écrivait (propos originaux, extrait) :

> 比如说，极限理论，试图用“N趋于无穷大”去解决芝诺悖论中实际上无法完成的“每次走一半走不完”这个过程。但是芝诺悖论的幽灵并没有消失，它在我的圆环悖论中再现了。

> **Traduction.** « Par exemple, la théorie des limites essaie, avec « N tend vers l'infini », de régler le processus du paradoxe de Zénon qui ne peut en fait pas être achevé, « marcher la moitié à chaque fois, sans jamais finir ». Mais le fantôme du paradoxe de Zénon n'a pas disparu ; il réapparaît dans mon paradoxe de l'anneau. »

Le paradoxe de l'anneau est une invention de la personne à l'origine du projet. En voici les propos originaux (2026-09-01) :

> 我再给你看一个抽象导致悖论的例子，这是我自己发明的悖论：一个圆，其上取一点拿走，假设现在的形态是M。然后将两端展开成线段，假设现在的形态是N。此时，问：从M到N似乎没有什么障碍，那么从N复原到M我们可以做到吗？在过程中N的两端，何以，可以逼近到只剩一个点的距离？因为点没有大小，无限小，无论N的两端逼近到什么接近的程度，都无法再还原到M的状态。可是，可是，我们当初确实得到了M啊！为什么变成N之后就无法再回到M了呢？接着这个我独创的悖论，理解我说的：抽象必然导致矛盾，是数理逻辑保证的推断。

> **Traduction.** « Je te montre encore un exemple d'abstraction menant au paradoxe, un paradoxe que j'ai inventé moi-même : prends un cercle et retires-en un point ; appelons M la forme obtenue. Puis déplie les deux extrémités en un segment ; appelons N la forme obtenue. Maintenant, demande : passer de M à N ne semble rencontrer aucun obstacle, mais pouvons-nous ramener N à M ? Comment, au cours du processus, les deux extrémités de N pourraient-elles s'approcher jusqu'à ce qu'il ne reste que la distance d'un point ? Comme un point n'a pas de taille, qu'il est infiniment petit, aussi près que s'approchent les deux extrémités de N, elles ne peuvent jamais être ramenées à l'état de M. Et pourtant, et pourtant, nous avions bel et bien obtenu M au départ ! Pourquoi, une fois devenu N, ne peut-il plus revenir à M ? À partir de ce paradoxe de ma propre invention, comprends ce que je veux dire : que l'abstraction mène nécessairement à la contradiction est une inférence garantie par la logique mathématique. »

Essaie de te le représenter. Prends un anneau et retires-en un point : il devient un cercle auquel il manque un point (M). Écarte les deux bords de la brèche et mets-le à plat : il devient un segment (N). Aucune difficulté là-dedans. Maintenant, recourbe-le : les deux extrémités se rapprochent, se rapprochent encore… mais le point qu'on a retiré n'a pas de taille, si bien que les deux extrémités restent toujours séparées par un vide d'« un point ». Aussi près qu'elles viennent, « de plus en plus près » ne devient jamais « rejoint ».

Et pourtant, et pourtant, nous avions bel et bien M ! Dans la réalité, si l'on coupe un anneau de fil de fer, qu'on le redresse puis qu'on le recourbe jusqu'à ce que les deux bouts se touchent, personne n'y trouve la moindre difficulté. La difficulté n'est pas dans la réalité, mais dans l'image que nous en donnons : des points sans taille, un espace divisible sans fin. C'est exactement la prémisse qui se trouve derrière Zénon. La limite proclame « arrivé » par une définition ; l'anneau, lui, fait voir que, dans cette image, le « retour » n'est jamais vraiment achevé. Le fantôme de Zénon est revenu sous un autre visage. C'est le sens des propos cités en tête de ce texte : du point de vue du paradoxe de l'anneau, on voit que le paradoxe de Zénon n'a pas vraiment été résolu par la théorie des limites.

Quelle condition de la réalité a été modifiée ? Pour la personne à l'origine du projet, le mouvement est, dans la réalité, quantifié, avec un plus petit pas (l'échelle de Planck), et la « divisibilité sans fin » de la droite numérique nie cela. C'est la position physique de la personne à l'origine du projet ; ce texte ne s'en porte pas garant. Son rôle ici est de nommer la prémisse que vise le paradoxe de l'anneau.

**Ce que nous avons essayé en mathématiques formelles** (le tout sur la branche `dev`) :

- Remplacer le cercle par un nombre fini de points qui « ont une taille » : retirer un point, mettre à plat, recourber, et le cercle est restauré exactement, sans aucun principe supplémentaire. Cela a été vérifié par ordinateur.
- Revenir à un cercle fait de nombres réels, dont les points n'ont pas de taille : pour la manière particulière de restaurer que nous avons examinée, prouver que le segment recourbé recouvre exactement le cercle privé d'un point exige un principe supplémentaire appelé principe de Markov, qui dit qu'« une recherche qui ne peut pas rester éternellement sans résultat finit par avoir un résultat ». Cette étape a elle aussi été vérifiée par ordinateur (elle provient d'une autre IA participant au projet). D'après la littérature existante, ce principe ne peut très probablement être ni démontré ni réfuté dans HoTT ; c'est un jugement appuyé par la littérature, non une preuve de notre part.
- Notre interprétation : sur le cercle des nombres réels, le fantôme se montre une fois de plus, cette fois sous la forme d'une recherche qui ne peut pas s'arrêter. Quant à savoir si l'histoire originale de l'anneau, telle que la raconte la personne à l'origine du projet, peut être écrite dans HoTT de façon complète et fidèle, la question reste ouverte.

Voir [le paradoxe de l'anneau dans le texte original](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/HoTT/sources/user-originals/Z铁律-抽象-圆环-时间维度-用户原始论述-20260901.md), [la preuve pour le cercle discret](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/HoTT/formal/claude-cg001/discrete-ring/CLAIM.md) et [la note de travail sur l'anneau et le principe de Markov](https://github.com/math-fournity/HoTT-Paradoxy/blob/dev/.claude/思考与发现/CN-024%20-%20圆环复原与%20Markov%20原则：复原撞上一条停机原则.md) (le tout en chinois).

## 3. Le fantôme de Russell : le regard du calcul

Passons à Russell. Imagine un ensemble S qui rassemble tous les ensembles qui « ne se contiennent pas eux-mêmes ». Question : S se contient-il lui-même ? S'il se contient, c'est un ensemble qui « se contient lui-même », et selon la règle il n'aurait pas dû être rassemblé ; s'il ne se contient pas, c'est exactement un ensemble qui « ne se contient pas lui-même », et selon la règle il aurait dû l'être. Toute réponse est fausse. Vers 1901, ce paradoxe a ébranlé les fondements des mathématiques.

Le remède standard, depuis lors, consiste à utiliser des axiomes ou une stratification en types, de sorte qu'un tel S ne puisse tout simplement pas être écrit : on le laisse à la porte.

La personne à l'origine du projet a pris un autre angle : non pas ce qu'est S, mais **comment S se construit** (2026-09-10, propos originaux, extrait) :

> ……如果你把S的构造过程写成程序，那么S的构造是无法完成的，因为它总是在拿入和拿出它自己。从而从“程序”——一种计算理论的视角去看，罗素悖论在它之中就不是悖论，罗素悖论构造的是一个不可计算的过程，是非法的。这一点很重要，非法的“命题”或者说程序，不是“理论”的失败！但是在集合论中，罗素悖论就成了理论的失败。

> **Traduction.** « … si tu écris le processus de construction de S sous forme de programme, la construction de S ne peut pas être achevée, car elle ne cesse de se faire entrer et sortir elle-même. Ainsi, vu depuis les « programmes », une théorie du calcul, le paradoxe de Russell n'y est pas un paradoxe : ce que construit le paradoxe de Russell est un processus non calculable, illégitime. Ce point est très important : une « proposition », ou un programme, illégitime n'est pas un échec de la « théorie » ! Mais dans la théorie des ensembles, le paradoxe de Russell est devenu un échec de la théorie. »

Lisons-le lentement. Pour construire S, il faut décider, pour chaque ensemble, s'il faut le faire entrer. Quand vient le tour de S lui-même, décider s'il faut le faire entrer exige de savoir ce qu'est S, et S n'est pas encore achevé. Alors le programme se fait entrer, puis sortir, puis entrer de nouveau, et ne s'arrête jamais. Pour qui programme, cela n'a rien d'effrayant : c'est simplement un programme qui ne s'arrête pas, une question qu'on n'aurait pas dû poser ainsi. Mais la théorie naïve des ensembles ne connaît pas l'idée que construire prend du temps. Elle suppose qu'une fois écrit « S est l'ensemble de tous les ensembles qui ne se contiennent pas eux-mêmes », S est déjà là, posé devant nous. Ainsi, un processus qui ne peut pas s'arrêter a été traité comme un objet tout fait, et la contradiction a suivi.

Plus tard, la personne à l'origine du projet a rendu cela plus aigu (2026-09-26, propos originaux, extrait) :

> 罗素悖论其实就是暴露了这样一件事：S在没有被构造出来之前，它的存在性还是一个问题的时候，S的构造过程已经被放入朴素集合论的算符中进行讨论了，也就是被问其他的集合是否是S的元素？
>
> 这本身就是数学不合理的：因为只有S的存在性被确定了，也就是说，只有S确实是朴素集合论可以讨论的论域中的元素的情况下，才应该可以把S进行朴素集合论下的算符操作。

> **Traduction.** « Ce que le paradoxe de Russell met réellement au jour, c'est ceci : avant que S ait été construit, alors que son existence est encore en question, le processus de construction de S a déjà été placé dans les opérateurs de la théorie naïve des ensembles et discuté, c'est-à-dire qu'on demande à d'autres ensembles s'ils sont des éléments de S.
>
> Cela est en soi mathématiquement déraisonnable : car ce n'est qu'une fois l'existence de S établie, c'est-à-dire seulement lorsque S est réellement un élément du domaine dont la théorie naïve des ensembles peut parler, qu'on devrait pouvoir appliquer à S les opérateurs de la théorie naïve des ensembles. »

Voilà la tension interne du paradoxe de Russell : avant qu'une chose soit établie, la théorie s'en sert déjà. Le manuel laisse S à la porte, mais il n'écarte ainsi que ce S-là ; la tension elle-même n'a pas disparu. Chaque fois qu'une théorie te met une chose entre les mains d'un seul coup, alors que le processus qui la confirme ne peut jamais être mené à son terme, le fantôme de Russell revient.

**Le bond décisif.** À la fin du même passage, la personne à l'origine du projet a tourné cette tension vers HoTT (propos originaux) :

> 如果对于HoTT论域元素的存在性的追问，在现实中会引发无法停机的计算（无限追溯），那么我们就成功了。

> **Traduction.** « Si l'interrogation sur l'existence d'un élément du domaine de HoTT déclenchait, dans la réalité, un calcul qui ne peut pas s'arrêter (une régression infinie), alors nous aurions réussi. »

Toute théorie a les choses dont elle parle, ce qu'on appelle son « domaine ». De certaines choses, une théorie peut refuser de parler ; d'autres, elle ne peut pas les refuser. Dans HoTT, l'une des choses qu'elle ne peut en aucun cas refuser est son « univers » : le contenant général qui renferme tous les types (toutes les « sortes de choses »). Le principe dont HoTT est la plus fière (l'« univalence », expliquée dans la section suivante) est lui-même un énoncé sur cet univers. Nous avons donc posé à l'univers une question à la manière de Russell : « être la même chose », pour les choses qu'il contient, peut-il jamais être établi ? À quel niveau ? Nous avons écrit cette interrogation sous forme de programme et l'avons confiée à l'ordinateur pour vérification. Selon les mots de la personne à l'origine du projet, c'est à partir de là que la recherche a pris la bonne direction.

## 4. Ce que nous avons trouvé dans HoTT : la question « est-ce la même chose ? » ne finit jamais

### Une chose qui devrait être simple

Deux choses sont-elles la même ? Dans la logique et les mathématiques de tous les jours, c'est l'affaire d'une phrase : ou bien elles le sont, ou bien elles ne le sont pas ; il n'y a pas de « de quelle manière elles le sont ».

### Ce que HoTT a modifié pour être commode

La théorie homotopique des types est un fondement des mathématiques qui a pris forme au cours des premières décennies de ce siècle (son premier manuel a paru en 2013). Elle réunit la logique, la géométrie et les programmes dans un seul langage, et les preuves écrites dans ce langage peuvent être confiées à un ordinateur qui les vérifie pas à pas. Elle a deux conceptions particulièrement séduisantes :

- **L'univalence : des choses isomorphes sont la même chose.** Deux choses dont la structure est exactement semblable comptent comme une seule et même chose, si bien qu'un théorème démontré pour l'une se transporte directement à l'autre. Cela épargne beaucoup de travail.
- **Les types inductifs supérieurs : toutes les formes d'un coup.** Cercles, sphères et formes de dimension aussi élevée qu'on veut peuvent être introduits directement dans la théorie comme des « choses ». Cela la rend très générale : on peut faire de la géométrie à l'intérieur même de la logique.

Le prix à payer : « être la même chose » n'est plus l'affaire d'une phrase. Prends le type formé des deux valeurs « vrai » et « faux ». On peut le confronter à lui-même tel quel, ou bien échanger vrai et faux puis le confronter ; après l'échange, la structure n'a pas changé du tout. Dans HoTT, ce sont deux manières différentes dont il est le même que lui-même ; un ordinateur a vérifié qu'en transportant « vrai » le long de la seconde manière, on obtient « faux ». Ainsi, demander « sont-elles la même chose ? » conduit à « de quelles manières sont-elles la même chose ? », et, entre ces manières, à « de quelles manières celles-ci sont-elles les mêmes ? »… au-dessus de chaque niveau, il y a un autre niveau.

### Le processus qui vise précisément cela

Nous avons écrit un programme tout simple qui demande, niveau après niveau : « À ce niveau, est-il tranché si ces choses sont la même ? » Question 1 : « être la même chose » se réduit-il déjà ici à un simple « oui » ou « non » ? Si la réponse est « non », il interroge le niveau 2 ; si c'est encore « non », le niveau 3… Lorsqu'il obtient un « oui », il s'arrête et indique le niveau. Chaque question reçoit un « oui » ou un « non » net, accompagné d'une preuve, de sorte que chaque étape du programme peut être effectuée.

### Résultats (faits mathématiques vérifiés par ordinateur)

- Dans un monde où « être la même chose est un fait établi par une seule vérification » (nous avons transcrit le même programme, selon les mêmes règles, dans un autre vérificateur de preuves, Lean), interrogé sur son propre univers, le programme **s'arrête à la question 1**.
- Dans HoTT, si la « hauteur » des choses (le nombre de niveaux de l'identité) est plafonnée, le programme **s'arrête exactement à la question que fixe le plafond**.
- Dans HoTT, interrogé sur son univers, ou sur un produit infini ordinaire, le programme **ne s'arrête jamais**. Chaque niveau répond par un « non » net, et au-dessus de chaque niveau il y en a un autre. Cela vaut pour toute manière de fournir les réponses « oui/non » ; c'est un théorème vérifié par ordinateur, et non « il a tourné longtemps sans s'arrêter ».

La même question, le même programme ; ne changez que le sens de « la même chose » et l'existence ou non d'un plafond pour la hauteur, et l'issue passe de « tranché en une étape » à « jamais tranché ».

### Côte à côte avec Zénon

| | Zénon | HoTT |
|---|---|---|
| La chose qui devrait être simple | aller d'ici à là-bas | décider si deux choses sont la même |
| La condition que la théorie a modifiée par commodité | la position est divisible sans fin | l'identité est divisible sans fin |
| Le processus qui la vise | à chaque fois, parcourir la moitié de ce qui reste | à chaque fois, interroger le niveau suivant : « de quelles manières la même ? » |
| Ce que montre chaque étape | il reste un bout ; certainement pas encore arrivé | ce niveau n'est pas tranché ; un « non » net |
| Issue | la marche ne finit jamais | le programme ne s'arrête jamais |
| Contrôle discret ou plafonné | dans un espace quantifié, un nombre fini de pas suffit | là où l'identité est un fait, arrêt à la question 1 ; avec une hauteur plafonnée, arrêt au plafond |
| La réponse des manuels | les limites | la troncature (voir plus bas) |

Le tableau met les deux cas en regard point par point ; il ne prétend pas qu'ils soient mathématiquement identiques.

### La réponse des manuels, et pourquoi elle ne fait pas disparaître le problème

Pour Zénon, le manuel dit : utilise les limites, 1/2 + 1/4 + … vaut exactement 1. Ici, le manuel dirait : interroge plutôt la « troncature ensembliste ». C'est une construction standard qui comprime « de quelles manières elles sont la même chose » en un simple « la même ou non » ; là, le programme s'arrête à la question 1.

Nous l'avons aussi fait vérifier par ordinateur : il s'arrête bien à la question 1. Mais il s'arrête parce qu'une règle remet en vigueur « être la même chose est l'affaire d'un mot ». Après la troncature, les deux manières dont « vrai/faux » est le même que lui-même (tel quel, et échangé) sont fondues en une seule ; et l'on ne peut plus jamais revenir à l'univers d'origine. L'objet sur lequel porte la question a été remplacé.

La limite remet en vigueur « tu es arrivé » par une définition ; la troncature remet en vigueur « être la même chose est l'affaire d'un mot » par une règle. Les deux sont des mathématiques légitimes, mais aucune ne restaure la condition modifiée elle-même. Elles répondent à une question plus facile, et le caractère déraisonnable de départ n'a pas disparu. (Ce paragraphe est notre interprétation, soumise à l'examen du lecteur.)

### Les verdicts de la personne à l'origine du projet

Le 2026-09-27, la personne à l'origine du projet a rendu un verdict (propos originaux) :

> 本repo复活了芝诺悖论的幽灵和罗素悖论的幽灵，并且找到的HoTT理论的问题。

> **Traduction.** « Ce dépôt a ressuscité le fantôme du paradoxe de Zénon et le fantôme du paradoxe de Russell, et a trouvé le problème de la théorie HoTT. »

En voyant les résultats ci-dessus, la personne à l'origine du projet a dit (2026-09-30, propos originaux, extrait) :

> 其实看了你捕捉到的HoTT的内容，我已经闻到了这种`不合理`的味道。

> **Traduction.** « En fait, après avoir vu ce que tu as saisi de HoTT, je sens déjà l'odeur de ce genre de `déraisonnable`. »

Et le même jour, la personne à l'origine du projet a décidé de clore cette recherche pour la phase en cours (propos originaux, extrait) :

> ……我认为我们要阶段性地收尾HoTT悖论查找工作了，因为我们很可能已经找到了。

> **Traduction.** « … Je pense que nous devons clore cette phase de la recherche de paradoxes dans HoTT, car nous l'avons très probablement trouvé. »

« Ressuscité les deux fantômes », « déraisonnable » et « très probablement trouvé » sont des verdicts de la personne à l'origine du projet, non des théorèmes mathématiques.

### Ce que ce n'est pas

- **Ce n'est pas une contradiction interne de HoTT.** Tout le raisonnement a été accepté par l'ordinateur à l'intérieur de HoTT. Nous ne disons pas que HoTT est incohérente, ni que ses règles sont mathématiquement fausses. Ce que nous disons, c'est qu'une condition qu'elle a modifiée par commodité transparaît dans une affaire qui devrait être simple.
- **Les faits mathématiques ne sont pour l'essentiel pas nouveaux.** Que de tels produits infinis n'aient pas de niveau fini, c'est l'exemple 8.8.6 du manuel de HoTT (2013) ; pour l'univers lui-même, le livre dit que cela devrait être démontrable mais n'a pas encore été fait ; Kraus et Sattler ont démontré en 2015 que, dans une hiérarchie d'univers univalents, le n-ième univers n'est pas un n-type (en gros : son « identité » n'est pas encore tranchée au niveau n). Qu'un univers unique avec types inductifs supérieurs ne soit tranché à aucun niveau, ce dépôt en donne une preuve vérifiée par ordinateur. Ce qui est nouveau, c'est surtout la lecture : lire ces faits comme un déraisonnable à la manière de Zénon, et indiquer vers quelle prémisse il pointe. Cette lecture n'a pas encore été confrontée en profondeur à la littérature.
- **« Ne s'arrête jamais » est un théorème interne à la théorie.** Le lire comme « si l'on exécute vraiment le programme, on n'obtiendra jamais de réponse » suppose en outre que la théorie utilisée soit cohérente et, pour une manière quelconque de répondre, une condition technique (la canonicité).
- **Cela ne se produit pas « dans tous les cas ».** Cela se produit pour l'univers et pour les objets de ce genre dont la hauteur n'a pas de borne supérieure. Mais l'univers n'est pas un cas marginal : c'est exactement l'objet dont parle l'univalence, et le domaine que HoTT ne peut pas refuser.

### Quelle prémisse mettre en cause

Selon la logique du raisonnement par l'absurde, ce qu'il faut réexaminer, c'est l'abstraction que la théorie a faite par commodité. Mais « vrai seulement si tout est vrai, faux dès qu'un seul élément est faux » : le résultat ne peut réfuter que l'ensemble des prémisses ; il ne peut pas désigner à lui seul celle qui est fausse. Notre jugement (une interprétation, ouverte à la discussion avec la personne à l'origine du projet et avec les lecteurs) est qu'il faut examiner d'abord l'univalence, « isomorphe signifie le même », parce que des formes de dimensions aussi élevées existent aussi en mathématiques classiques, et que ce qui a changé, c'est le sens de « le même » ; les types inductifs supérieurs viennent en second. C'est un ordre de priorité, non un unique accusé.

## 5. Les deux fantômes disent la même chose

(Cette section est notre interprétation.)

Chez Zénon, « arriver » doit se parcourir pas à pas ; pour l'anneau, « revenir à M » exige que les deux extrémités se rejoignent vraiment ; chez Russell, S doit d'abord être construit ; ici, dans HoTT, « être la même chose » doit être confirmé niveau par niveau. Les quatre ont besoin d'un processus. Et à chaque fois, la théorie ne laisse aucune place à ce processus : ou bien elle le laisse ne jamais finir (la division par deux de Zénon, l'approche de l'anneau, l'interrogation niveau par niveau dans HoTT), ou bien elle le traite comme achevé sans attendre qu'il le soit (la proclamation de la limite, le S de Russell, l'univers que HoTT te met entre les mains d'un seul coup). Ce sont exactement les deux sortes de paradoxes que la personne à l'origine du projet a décrites à la section 1. Le processus qui a été laissé de côté, c'est le temps.

C'est précisément le soupçon que la personne à l'origine du projet a mis par écrit le 2026-09-10 (propos originaux, extrait) :

> 所以，朴素集合论到底否定了什么？你刚刚说的那些都对，但是我们最后还要有一个哲学高度的定性认知：它否定了（妄图抹掉）现实的“时间维度”，它认为，它可以以静态的集合或者说静态的逻辑关系来刻画所有它想刻画的目标，甚至曾经还有人妄图让它作为整个数学大厦的基础——被罗素以罗素悖论击退。而我，深切地怀疑HoTT也做了同样的事情，毕竟，不考虑时间，是数学理论构建者的【认知惯性】、【路径依赖】。

> **Traduction.** « Alors, qu'a donc nié, au fond, la théorie naïve des ensembles ? Ce que tu viens de dire est entièrement juste, mais il nous faut encore, pour finir, une compréhension qualitative à la hauteur de la philosophie : elle a nié (a tenté en vain d'effacer) la « dimension du temps » de la réalité. Elle croyait pouvoir saisir tout ce qu'elle voulait saisir au moyen d'ensembles statiques, ou de relations logiques statiques ; certains ont même tenté en vain d'en faire le fondement de tout l'édifice des mathématiques, et ont été repoussés par Russell avec le paradoxe de Russell. Et moi, je soupçonne profondément HoTT d'avoir fait la même chose ; après tout, ne pas tenir compte du temps est l'[inertie cognitive] et la [dépendance au chemin] de ceux qui construisent les théories mathématiques. »

Un peu plus de deux semaines plus tard, le regard de Russell nous a conduits jusqu'à l'univers de HoTT ; le déraisonnable que nous y avons vu correspond point par point à Zénon. Les deux fantômes se sont rencontrés au même endroit.

## 6. Une autre piste : la cohérence infinie

Avant de trouver ce qui est décrit plus haut, nous avons suivi un temps une autre piste à la manière de Zénon. HoTT connaît une chose appelée « structure semi-simpliciale » : une forme collée niveau par niveau à partir de points, de segments, de triangles et de tétraèdres, avec l'exigence que les « faces des faces » s'accordent. Dans un monde où l'identité est un fait, elle se définit en une ligne ; dans HoTT, chaque fois qu'on ajoute un niveau d'« accord », une exigence pousse au niveau suivant. Chaque niveau fini peut être écrit (vérifié par ordinateur jusqu'au niveau 5), mais personne n'a trouvé jusqu'ici une définition unique qui couvre tous les niveaux à la fois. C'est un problème ouvert bien connu depuis plus de dix ans ; qu'il soit impossible n'a pas non plus été démontré. L'exposé complet se trouve dans le document d'audit 01.

**Une rectification à propos des noms.** Le titre du document d'audit 01, le rapport de clôture de phase et la version précédente de ce README ont tous employé l'expression « le fantôme du paradoxe de Zénon » pour cette piste. Le 2026-10-01, la personne à l'origine du projet a précisé que cette expression désigne le paradoxe de l'anneau (propos originaux, extrait) :

> ……我说了复活了芝诺悖论的幽灵到底是指什么？我指的的是圆环悖论啊！

> **Traduction.** « … Quand j'ai dit « ressuscité le fantôme du paradoxe de Zénon », qu'est-ce que je voulais dire au juste ? Je voulais parler du paradoxe de l'anneau ! »

La cohérence infinie est une piste candidate à la manière de Zénon, construite par nous (les systèmes d'IA du projet). Elle a sa propre valeur, mais ce n'est pas ce que la personne à l'origine du projet appelle « le fantôme du paradoxe de Zénon ». Des versions révisées de ces deux documents seront publiées séparément.

## 7. Comment nous vérifier

Nous espérons que vous ne nous croirez pas sur parole, mais que vous vérifierez par vous-même. L'examen peut se faire à trois niveaux :

1. **Les mathématiques sont-elles justes ?** Chaque énoncé positif a été vérifié pas à pas par un vérificateur de preuves (Cubical Agda 2.8.0 avec la bibliothèque cubical v0.9 ; Lean 4.34.0). Les énoncés clés s'accompagnent en outre de « contrôles négatifs » : des preuves délibérément fausses que le vérificateur doit rejeter, pour s'assurer que la vérification vérifie vraiment. Tous les énoncés, leurs éléments de preuve et les limites à ne pas dépasser en les généralisant figurent dans [`CLAIMS-FR.md`](CLAIMS-FR.md) (traduction par IA de [`CLAIMS.md`](CLAIMS.md)) ; les sources des preuves sont dans `HoTT/formal/`, et le `CLAIM.md` de chaque paquet de preuves donne les énoncés complets ; les reçus d'exécution sont dans `HoTT/verification/runs/`, 107 au total : 49 acceptés et 58 contrôles négatifs rejetés comme prévu.
2. **Les énoncés disent-ils ce que dit le texte ?** Les énoncés formels disent-ils ce que dit la prose ? Par exemple, « interroger niveau par niveau » est-il une manière loyale de préciser « décider si deux choses sont la même » ? Pour ce niveau, lisez les documents d'audit : [03, « Le Zénon de HoTT »](docs/社区审计提交/03-HoTT的芝诺-FR.md) (le plus court, qui se termine par cinq questions d'audit), [02, « Le fantôme du paradoxe de Russell »](docs/社区审计提交/02-罗素悖论的幽灵-FR.md), [01 (la piste de la cohérence infinie)](docs/社区审计提交/01-芝诺悖论的幽灵-FR.md), ainsi que [le rapport de clôture de phase](docs/HoTT悖论查找阶段收尾报告-20260930.md) (en chinois).
3. **La lecture tient-elle ?** Cette chose est-elle vraiment « simple » ? La condition modifiée est-elle bien « l'identité est divisible sans fin » ? Une réponse standard comme la troncature peut-elle la faire disparaître ? Ce sont des questions de philosophie des mathématiques, et les objections sont les bienvenues.

### Comment rejouer

Avec Agda 2.8.0, cubical v0.9 et Lean 4.34.0 installés, lancez depuis la racine du dépôt :

```sh
python3 tools/replay.py --agda /path/to/agda --cubical-lib /path/to/cubical/cubical.agda-lib --lean-sysroot /path/to/lean-4.34.0 --jobs 4
```

Le script reconstruit la commande de chaque reçu d'exécution, l'exécute et compare le résultat au reçu : l'issue (accepté ou rejeté) doit concorder, et la sortie est comparée ligne par ligne après remplacement du chemin du dépôt et des chemins des bibliothèques par des marqueurs. Un contrôle négatif ne réussit que s'il est de nouveau rejeté ; si sa sortie concorde aussi, il a été rejeté pour la raison enregistrée. Pour rejouer un seul reçu : `--only <identifiant d'exécution>` ; pour les lister tous : `--list`. Tout rejouer à la suite prend environ une heure et demie. Les commandes des reçus enregistrent les chemins absolus de la machine qui les a capturées ; les outils d'origine pour le rejeu octet par octet sont sur la branche `dev` (`.claude/goals/CG-001-targeted-overview/tools/verify_cg001_run.py`, `Cloud-Opus审计并补完GLM/tools/verify_copus_run.py`).

Les enregistrements de chaînes d'outils cités par les reçus se trouvent dans `HoTT/formal/dedekind-omega-missile/` (Agda sous macOS), `HoTT/formal/claude-cg001/pedometer-ablation-lean/` (Lean sous macOS) et `HoTT/formal/cloud-opus-glm-audit/` (Linux) ; les deux premiers répertoires conservent leur emplacement de `dev` et ne contiennent sur cette branche que ces enregistrements. [`RELEASE-MANIFEST.json`](RELEASE-MANIFEST.json) consigne le SHA-256 de chacun des 699 fichiers de cette branche et le commit de `dev` dont ils proviennent.

## 8. Comment cette recherche a été menée

Les questions, la façon de voir les paradoxes et les verdicts finaux viennent de la personne à l'origine du projet ; chaque citation de ce texte reproduit ses propos originaux. La formalisation, les preuves et les audits croisés ont été répartis entre plusieurs systèmes d'IA, dont le travail a aussi été vérifié de part et d'autre. L'ensemble du processus de recherche, y compris le registre des propos originaux de la personne à l'origine du projet, `核心认知.md`, la genèse de chaque piste, les détours empruntés et les échanges d'audit entre les systèmes d'IA, se trouve sur la [branche `dev`](https://github.com/math-fournity/HoTT-Paradoxy/tree/dev). Chemins que mentionnent les documents de conclusion mais qui ne sont pas sur cette branche :

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

## 9. À propos de cette branche

- `main` (cette branche) ne contient que ce qui étaye les conclusions : les documents de conclusion, les énoncés précis, les sources des preuves, les reçus d'exécution et le moyen de les rejouer. Elle est générée à partir du commit [`8fa2263b`](https://github.com/math-fournity/HoTT-Paradoxy/commit/8fa2263b6b708d75260cf012c5a3119efdb1f1db) de `dev` selon un manifeste (`scripts/release/build_main_release.py` et `scripts/release/main-release-spec.json` sur `dev`) et n'est pas modifiée directement. Pour la mettre à jour, on modifie le manifeste ou les documents de conclusion sur `dev`, puis on la génère de nouveau.
- `dev` : l'ensemble du processus de recherche ; tout le travail s'y fait.
- Ce README existe aussi en chinois, en russe, en allemand et en anglais, avec le même contenu. Les documents d'audit et `CLAIMS.md` existent également dans ces quatre langues ; les traductions sont faites par IA, et le texte chinois fait foi.
