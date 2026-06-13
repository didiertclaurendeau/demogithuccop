# Le Test du Khi Carré (χ²)

> 💬 *« Le Khi carré, c'est comme votre beau-frère qui vérifie si vos dés sont pipés — sauf que lui, il a une formule. »*

## 1. Introduction

Le **test du Khi carré** (noté **χ²**) est un test statistique utilisé pour déterminer s'il existe une association significative entre deux variables catégorielles, ou si une distribution observée s'écarte significativement d'une distribution théorique attendue.

Autrement dit : est-ce que ce qu'on **observe** dans la vraie vie ressemble à ce qu'on **s'attendait** à voir ? Si la réponse est « pas du tout », les données ont quelque chose à nous dire. 🔍

Il existe deux grandes variantes :

| Variante | Usage |
|---|---|
| **Test d'ajustement** (goodness of fit) | Compare une distribution observée à une distribution théorique |
| **Test d'indépendance** | Vérifie si deux variables catégorielles sont indépendantes |

---

## 2. Conditions d'application

> ⚠️ *Avant de sortir votre χ², assurez-vous que vos données sont invitées au bon party.*

Avant d'appliquer le test du Khi carré, il faut vérifier les conditions suivantes :

- Les données sont des **fréquences** (effectifs), non des pourcentages ou des moyennes.
- Les observations sont **indépendantes** les unes des autres.
- Chaque effectif **théorique** doit être **≥ 5** dans au moins 80 % des cellules.
- Aucun effectif théorique ne doit être **inférieur à 1**.

---

## 3. La statistique du Khi carré

### Formule générale

$$\chi^2 = \sum \frac{(O_i - E_i)^2}{E_i}$$

Où :
- $O_i$ = effectif **observé** dans la catégorie $i$
- $E_i$ = effectif **attendu** (théorique) dans la catégorie $i$
- $\sum$ = somme sur toutes les cellules

> 🤓 *Traduction : on regarde combien la réalité s'éloigne de la théorie, on met ça au carré pour que personne ne se cache derrière un signe négatif, et on additionne le tout.*

---

## 4. Test d'ajustement (Goodness of Fit)

### Objectif
Vérifier si une distribution observée correspond à une distribution théorique connue (ex. : distribution uniforme, distribution normale, etc.).

### Exemple

> 🎲 *Imaginez que vous soupçonnez votre ami de tricher aux jeux de société. Le Khi carré va régler ça scientifiquement — et diplomatiquement.*

Un dé à 6 faces est lancé 120 fois. On observe :

| Face | 1 | 2 | 3 | 4 | 5 | 6 |
|------|---|---|---|---|---|---|
| **Observé** ($O_i$) | 18 | 22 | 17 | 25 | 19 | 19 |
| **Attendu** ($E_i$) | 20 | 20 | 20 | 20 | 20 | 20 |

**Calcul :**

$$\chi^2 = \frac{(18-20)^2}{20} + \frac{(22-20)^2}{20} + \frac{(17-20)^2}{20} + \frac{(25-20)^2}{20} + \frac{(19-20)^2}{20} + \frac{(19-20)^2}{20}$$

$$\chi^2 = \frac{4}{20} + \frac{4}{20} + \frac{9}{20} + \frac{25}{20} + \frac{1}{20} + \frac{1}{20} = \frac{44}{20} = 2{,}2$$

**Degrés de liberté :** $dl = k - 1 = 6 - 1 = 5$

> ✅ *Résultat : 2,2 < 11,070. Le dé est innocent. Votre ami peut dormir tranquille.*

---

## 5. Test d'indépendance

### Objectif
Déterminer si deux variables catégorielles sont **indépendantes** ou **associées**.

### Tableau de contingence

Les données sont organisées dans un **tableau de contingence** à $r$ lignes et $c$ colonnes.

**Effectif attendu pour chaque cellule :**

$$E_{ij} = \frac{(\text{Total ligne } i) \times (\text{Total colonne } j)}{\text{Total général}}$$

**Degrés de liberté :**

$$dl = (r - 1)(c - 1)$$

### Exemple

On veut savoir si le sexe d'un individu est lié à sa préférence pour un sport.

|  | Football | Basketball | Tennis | **Total** |
|--|----------|------------|--------|-----------|
| **Hommes** | 30 | 15 | 5 | **50** |
| **Femmes** | 10 | 25 | 15 | **50** |
| **Total** | **40** | **40** | **20** | **100** |

**Calcul des effectifs attendus :**

$$E_{11} = \frac{50 \times 40}{100} = 20 \quad E_{12} = \frac{50 \times 40}{100} = 20 \quad E_{13} = \frac{50 \times 20}{100} = 10$$

$$E_{21} = 20 \quad E_{22} = 20 \quad E_{23} = 10$$

**Calcul du χ² :**

$$\chi^2 = \frac{(30-20)^2}{20} + \frac{(15-20)^2}{20} + \frac{(5-10)^2}{10} + \frac{(10-20)^2}{20} + \frac{(25-20)^2}{20} + \frac{(15-10)^2}{10}$$

$$\chi^2 = 5 + 1{,}25 + 2{,}5 + 5 + 1{,}25 + 2{,}5 = 17{,}5$$

**Degrés de liberté :** $dl = (2-1)(3-1) = 2$

---

## 6. Prise de décision

> 🧑‍⚖️ *Le statisticien joue les juges : H₀ est présumée innocente jusqu'à preuve du contraire. Votre χ² est l'avocat de l'accusation.*

### Hypothèses

- **H₀** (hypothèse nulle) : Il n'y a **pas** d'association entre les variables (ou la distribution observée suit la distribution théorique).
- **H₁** (hypothèse alternative) : Il **existe** une association entre les variables.

### Règle de décision

On compare la valeur calculée de **χ²** à la **valeur critique** $\chi^2_{\alpha, dl}$ issue de la table du Khi carré pour un seuil de signification $\alpha$ (généralement 0,05).

| Condition | Décision |
|-----------|----------|
| $\chi^2_{calc} > \chi^2_{critique}$ | **Rejeter H₀** → association significative |
| $\chi^2_{calc} \leq \chi^2_{critique}$ | **Ne pas rejeter H₀** → pas d'association significative |

> On peut aussi comparer la **p-valeur** au seuil α : si p-valeur < α, on rejette H₀.

### Table des valeurs critiques (extrait)

| dl | α = 0,10 | α = 0,05 | α = 0,01 |
|----|----------|----------|----------|
| 1  | 2,706    | 3,841    | 6,635    |
| 2  | 4,605    | 5,991    | 9,210    |
| 3  | 6,251    | 7,815    | 11,345   |
| 4  | 7,779    | 9,488    | 13,277   |
| 5  | 9,236    | 11,070   | 15,086   |

### Reprise des exemples

**Exemple 1 (dé) :** χ² = 2,2 ; dl = 5 ; χ²_critique (α=0,05) = 11,070
→ 2,2 < 11,070 → **On ne rejette pas H₀** : le dé semble équitable.

**Exemple 2 (sport/sexe) :** χ² = 17,5 ; dl = 2 ; χ²_critique (α=0,05) = 5,991
→ 17,5 > 5,991 → **On rejette H₀** : il y a une association significative entre le sexe et la préférence sportive.

---

## 7. Résumé — Démarche en 5 étapes

> 📋 *Cinq étapes. Pas six. Pas quatre. Cinq. Vous pouvez le faire.*

```
1. Formuler H₀ et H₁
2. Choisir le seuil de signification α (ex. : 0,05)
3. Calculer χ² et les degrés de liberté
4. Trouver la valeur critique dans la table
5. Prendre la décision et interpréter
```

> 🏆 *Félicitations, vous êtes maintenant capables de débusquer les associations cachées dans n'importe quel tableau. Utilisez ce pouvoir avec sagesse (et avec α = 0,05).*

---

## 8. Limites du test

> 🦸 *Même les super-héros ont des faiblesses. Le Khi carré aussi.*

- Ne s'applique **pas** aux données continues (sauf si regroupées en classes).
- Ne mesure **pas la force** de l'association (pour cela, utiliser le **V de Cramér**).
- Sensible à la **taille de l'échantillon** : un très grand échantillon peut rejeter H₀ même pour une association triviale.

> 😅 *En d'autres mots : avec 10 000 observations, même « les gens qui mangent des céréales au petit-déjeuner sont légèrement plus grands de 0,2 cm » devient statistiquement significatif. Ce n'est pas la même chose qu'être **intéressant**.*

### V de Cramér (mesure d'effet)

$$V = \sqrt{\frac{\chi^2}{n \times \min(r-1, c-1)}}$$

- V proche de 0 → association faible
- V proche de 1 → association forte
