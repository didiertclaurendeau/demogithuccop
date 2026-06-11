# Résolution d'une Équation Quadratique

## Définition

Une **équation quadratique** (ou du second degré) est une équation de la forme :

$$ax^2 + bx + c = 0$$

où $a$, $b$ et $c$ sont des nombres réels, avec $a \neq 0$.

---

## Étape 1 — Identifier les coefficients

À partir de l'équation, repérer :

| Coefficient | Rôle | Exemple : $2x^2 - 4x - 6 = 0$ |
|-------------|------|-------------------------------|
| $a$ | Coefficient du terme en $x^2$ | $a = 2$ |
| $b$ | Coefficient du terme en $x$ | $b = -4$ |
| $c$ | Terme constant | $c = -6$ |

> **Important :** S'assurer que l'équation est bien mise sous la forme standard $ax^2 + bx + c = 0$ avant de commencer.

---

## Étape 2 — Calculer le discriminant $\Delta$

Le **discriminant** permet de déterminer le nombre de solutions. Il se calcule ainsi :

$$\Delta = b^2 - 4ac$$

**Avec notre exemple :**

$$\Delta = (-4)^2 - 4 \times 2 \times (-6) = 16 + 48 = 64$$

---

## Étape 3 — Analyser le discriminant

| Cas | Condition | Nombre de solutions |
|-----|-----------|---------------------|
| $\Delta > 0$ | Discriminant positif | **2 solutions réelles distinctes** |
| $\Delta = 0$ | Discriminant nul | **1 solution réelle double** |
| $\Delta < 0$ | Discriminant négatif | **Pas de solution réelle** (solutions complexes) |

**Dans notre exemple :** $\Delta = 64 > 0$ → il y a **deux solutions réelles distinctes**.

---

## Étape 4 — Calculer les solutions

### Cas 1 : $\Delta > 0$ — Deux solutions

$$x_1 = \frac{-b - \sqrt{\Delta}}{2a} \qquad \text{et} \qquad x_2 = \frac{-b + \sqrt{\Delta}}{2a}$$

**Avec notre exemple :**

$$x_1 = \frac{-(-4) - \sqrt{64}}{2 \times 2} = \frac{4 - 8}{4} = \frac{-4}{4} = -1$$

$$x_2 = \frac{-(-4) + \sqrt{64}}{2 \times 2} = \frac{4 + 8}{4} = \frac{12}{4} = 3$$

**Les solutions sont donc $x_1 = -1$ et $x_2 = 3$.**

---

### Cas 2 : $\Delta = 0$ — Une solution double

$$x_0 = \frac{-b}{2a}$$

> Il n'y a qu'une seule valeur de $x$ qui annule l'équation (racine double).

---

### Cas 3 : $\Delta < 0$ — Pas de solution réelle

L'équation n'a pas de solution dans $\mathbb{R}$.  
*(En terminale ou en supérieur, on peut parler de solutions complexes.)*

---

## Étape 5 — Vérification

Substituer chaque solution dans l'équation d'origine pour vérifier :

**Vérification pour $x_1 = -1$ :**

$$2(-1)^2 - 4(-1) - 6 = 2(1) + 4 - 6 = 2 + 4 - 6 = 0 \checkmark$$

**Vérification pour $x_2 = 3$ :**

$$2(3)^2 - 4(3) - 6 = 2(9) - 12 - 6 = 18 - 12 - 6 = 0 \checkmark$$

---

## Récapitulatif — Méthode en 5 étapes

```
1. Mettre l'équation sous la forme ax² + bx + c = 0
2. Identifier a, b et c
3. Calculer Δ = b² - 4ac
4. Analyser Δ et calculer les solutions avec la formule
5. Vérifier les solutions dans l'équation d'origine
```

---

## Astuce pédagogique

> Pour aider les étudiants à mémoriser la formule, on peut retenir la phrase :
> **"moins b, plus ou moins racine de delta, le tout divisé par deux a"**
>
> $$x = \frac{-b \pm \sqrt{\Delta}}{2a}$$

---

## Exercice d'application

Résoudre l'équation : $x^2 - 5x + 6 = 0$

<details>
<summary>Voir la solution</summary>

**Étape 1 :** $a = 1$, $b = -5$, $c = 6$

**Étape 2 :** $\Delta = (-5)^2 - 4(1)(6) = 25 - 24 = 1$

**Étape 3 :** $\Delta > 0$ → deux solutions

**Étape 4 :**
$$x_1 = \frac{5 - 1}{2} = 2 \qquad x_2 = \frac{5 + 1}{2} = 3$$

**Les solutions sont $x_1 = 2$ et $x_2 = 3$.**

</details>
