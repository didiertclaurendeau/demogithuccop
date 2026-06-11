
```prompt
Crée moi un fichier MD qui avec une procédure pour résoudre une équation quadratique. Mets moi tous les étapers pour m'aider à faire la démontration à des étudiants.
```

[[equation_quadratique]]

```prompt
Cree moi un fichiel html avec du javascript permettant d'explique comment la résolution de cette équation est en lien avec une fonction x/y
```

https://cegep.fdtt.space/demo/equation_quadratique.html

```prompt
Je donne un cours de physique et je veux faire une page intéractive pour démontrer le concept de friction statique vers dynamique. Je veux donc être en mesure de montrer un objet sur une pente ou on voit les fictiions représentés à l'aide d'une flèches et je peux changer la pente pour changer les conditions.
```

![[Pasted image 20260602090014.png]]

```prompt
Crée moi un fichier md avec un tableau historique des grands philosophes pour permettre de donner une idée a mes étudiants de l'évolution . Mets les années, le nom et le type de doctrine que ces philosophe ont apportés
```


­https://cegep.fdtt.space/demo/friction.html 


[[philosophes_historique]]

```prompt
Je veux créer un laboratoire pour les étudiants pour les base de l'utilisation d'un IOT. Je veux que durant ce laboratoire ils effectuent le montage sur une plaquette avec un Raspberry PI ou un bouton augumente un compteur sur un LCD.  C'est une première expérience et donc le laboratoire doit guider les étudiants pas a pas pour le réaliser. Utilise des fichiers markdown .MD pour créer la procédure. Pour faire les directives de montage utilise du ASCII art. Lorsque l'étudiant presse le bouton un LED doit s'afficher pour une demi seconde et le compteur sur le LCD doit incrémenter. 

Le LCD est le LCD1602 et pour les résistances les étudiants on accès a des 220 Ohms, 1.2 KOhms et 10 kOhms. 

Cree l'expérience dans un répertoire lab
```

[[lab/README]]

```prompt
Dans  le répertoire devoirs il y a plusieurs répertoires avec des travaux d'étudiants. Je voudrais que tu évalues la réponses des étudiants pour la section 3.1 dans la zone OBSERVATIONS. Qu'elle étudiant a le mieux répondu?
```

## Étudiants n'ayant pas répondu (OBSERVATIONS vide)

`0e19f65`, `1be7aec`, `21613c6`, `2732cea`, `2b53634`, `4e60e09`, `52de27c`, `5c8a40e`, `68cf22e`, `8b8b59e`, `b0a6c1c`, `b13342c`, `b786863`, `b8fed5c`, `d40d187`, `dfbfffe` — **16 étudiants sur 25 n'ont rien écrit.**

---

## Étudiants ayant répondu — classement

| Rang | Étudiant    | Qualité                                                                                                                                            |
| ---- | ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| 🥇 1 | **656fb86** | Répond aux 3 étapes avec détails techniques (noms de tables, champs), explique clairement le double-spend, la balance négative et l'incohérence BD |
| 🥈 2 | **42470f2** | Réponse structurée en 3 points clairs, couvre toutes les questions, explique bien le phénomène de concurrent read/write                            |
| 🥉 3 | **d4aeca6** | Réponse structurée dans les questions ET dans OBSERVATIONS, nomme TOCTOU, explique bien la balance négative                                        |
| 4    | **3343f74** | Bonne réponse couvrant les 3 étapes et les conséquences, bien rédigée                                                                              |
| 5    | **1ddf397** | Structure en 3 étapes claires, correct, mais moins développé                                                                                       |
| 6    | **78b3405** | L'essentiel de la réponse est écrit _dans_ le bloc question (pas dans OBSERVATIONS) — très bien compris mais mal placé                             |
| 7    | **b10e6e3** | Correct mais formulation imprécise à l'étape 3 ("les 10 autres requêtes")                                                                          |
| 8    | **67aa12a** | Très minimal, cite les étapes sans développer les conséquences                                                                                     |

---

## Meilleur étudiant : **656fb86**

Sa réponse dans OBSERVATIONS est la plus complète et la mieux rédigée :

> _"Étape 1 — Lecture : on récupère les infos de l'acheteur dans la table `users` (notamment sa balance) ainsi que les infos de l'annonce dans `listings` (comme le prix). Étape 2 — Vérification : on vérifie que l'acheteur a assez d'argent [...] Le problème arrive avec les requêtes concurrentes. Si 10 requêtes passent l'étape 2 avant que l'étape 3 soit faite, chacune va quand même continuer. Résultat : la balance est déduite 10 fois (double-spend), elle peut devenir négative, plusieurs achats sont enregistrés pour la même annonce, et la base de données devient incohérente."_

Il identifie clairement les 3 étapes, le mécanisme de la race condition, le terme "double-spend", et les 3 conséquences possibles.

```prompt
Je veux donner une bonne rétroaction à l'étudiant pour le travail 656fb86. Crée moi un fichier retro.md qui donne une rétroaction à tout les réponses de l'étudiant
```

[[retro]]

```prompt
Je veux créer un cours pour un programme diététique ou je veux expliquer la production des graisses versus l'alimentation et l'exercices. Donc ici je veux créer trois cours sur les différent concepts pour comprendre l'importance de ces concept. Crée un répertoire cours avec un proposition pour ces trois cours. Chaque cours doivent avoir une durée de 3 heures et inclure une partie pratique ou laboratoire d'une heure et demi pour les étudiants. 
```

[[cours/README]]

```prompt
Crée moi une évaluation les trois cours contenus dans le répertoire cours. Je veux 5 choix multiples et 2 questions à dévelopement
```

[[evaluation]]

# Quota

Depuis le premier juin un système de quota fut mis en place et il est donc possible qu'il y ait maintenant une limite d'utilisation mensuel. Dans le passé des limites étaient affichées mais pas prise en compte donc il est aussi possible que ce nouveau système n'ait pas d'impact.

![[Pasted image 20260603070838.png]]