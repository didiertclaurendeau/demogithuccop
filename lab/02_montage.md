# Étape 2 — Montage des composants

> **Important :** Le Raspberry Pi doit être **hors tension** (débranché) pendant tout le montage.

---

## 2.1 Comprendre la breadboard

Une breadboard (plaquette de prototypage) permet de connecter des composants **sans soudure**.

```
Structure interne d'une breadboard (vue de dessus)
╔══════════════════════════════════════════════════════╗
║  +  ─────────────────────────────────────────  rail + ║
║  -  ─────────────────────────────────────────  rail - ║
║                                                       ║
║  a  b  c  d  e     f  g  h  i  j   ← colonnes        ║
║  ┌──┬──┬──┬──┬──┐ ┌──┬──┬──┬──┬──┐                  ║
║1 │  │  │  │  │  │ │  │  │  │  │  │  ← rangée 1       ║
║2 │  │  │  │  │  │ │  │  │  │  │  │  ← rangée 2       ║
║3 │  │  │  │  │  │ │  │  │  │  │  │                   ║
║  └──┴──┴──┴──┴──┘ └──┴──┴──┴──┴──┘                  ║
║  +  ─────────────────────────────────────────  rail + ║
║  -  ─────────────────────────────────────────  rail - ║
╚══════════════════════════════════════════════════════╝

Les trous d'une même RANGÉE (1a–1e) sont connectés ensemble.
Les RAILS (+/-) sont connectés sur toute la longueur.
```

---

## 2.2 Montage de la LED avec résistance 220 Ω

La résistance **220 Ω** protège la LED contre un courant trop élevé.

### Identifier la LED

```
LED vue de côté :

      Anode (+)    Cathode (-)
         |              |
         |    _____     |
         |   /     \    |
         +--| (LED) |---+
              \_____/
         
  La patte LONGUE = Anode (+)
  La patte COURTE = Cathode (-)
```

### Schéma de connexion de la LED

```
GPIO27 (broche 13) ──── [R 220Ω] ──── Anode(+) LED ──── Cathode(-) ──── GND
```

### Sur la breadboard :

```
Breadboard — Section LED (rangées 1 à 5)

Colonne :  a    b    c    d    e        f    g    h    i    j
         ┌────┬────┬────┬────┬────┐  ┌────┬────┬────┬────┬────┐
  1      │GPIO│    │    │    │    │  │    │    │    │    │    │
         │ 27 │    │    │    │    │  │    │    │    │    │    │
  2      │[fil]────────────[R220Ω-début]│    │    │    │    │
         │    │    │    │    │    │  │    │    │    │    │    │
  3      │    │    │[R220Ω-fin]──[Anode LED+] │    │    │    │
         │    │    │    │    │    │  │    │    │    │    │    │
  4      │    │    │    │[Cathode LED-]──[fil GND]  │    │    │
         │    │    │    │    │    │  │    │    │    │    │    │
  5      │    │    │    │    │    │  │    │    │    │    │    │
         └────┴────┴────┴────┴────┘  └────┴────┴────┴────┴────┘
```

**Instructions pas à pas :**

1. Placez la résistance **220 Ω** entre les colonnes **a2** et **d2** (en pont sur le milieu).
2. Insérez la **LED** : anode (patte longue) en **d3**, cathode (patte courte) en **d4**.
3. Connectez un fil de **a2** vers la broche **GPIO27** (broche physique 13) du Raspberry Pi.
4. Connectez un fil de **d4** vers le rail **GND (-)** de la breadboard.
5. Connectez le rail **GND (-)** de la breadboard à une broche **GND** du Raspberry Pi (broche physique 6 ou 9).

---

## 2.3 Montage du bouton avec résistance pull-down 10 kΩ

La résistance **10 kΩ** en pull-down garantit que l'entrée GPIO lit **0** (LOW) quand le bouton n'est pas pressé.

### Identifier le bouton-poussoir

```
Bouton-poussoir vu de dessus :

    A ──┬── B
        │  (contact interne)
    C ──┴── D

  A et B sont connectés ensemble (côté 1)
  C et D sont connectés ensemble (côté 2)
  Appuyer sur le bouton connecte A/B avec C/D
```

### Schéma de connexion du bouton

```
3,3V ──── Broche A du bouton
           Broche C du bouton ──── [R 10kΩ] ──── GND
           Broche C du bouton ──── GPIO17
```

### Sur la breadboard :

```
Breadboard — Section Bouton (rangées 10 à 17)

Colonne :  a    b    c    d    e        f    g    h    i    j
         ┌────┬────┬────┬────┬────┐  ┌────┬────┬────┬────┬────┐
 10      │3.3V│    │[Broche A bouton]│ │[Broche B bouton]     │
         │[fil│    │    │    │    │  │    │    │    │    │    │
 11      │    │    │    │    │    │  │    │    │    │    │    │
         │    │    │    │    │    │  │    │    │    │    │    │
 12      │    │    │    │    │    │  │[Broche C bouton]       │
         │    │    │    │    │    │  │    │    │    │    │    │
 13      │    │    │    │    │    │  │[GPIO17][R10k─────GND]  │
         └────┴────┴────┴────┴────┘  └────┴────┴────┴────┴────┘
```

**Instructions pas à pas :**

1. Placez le bouton-poussoir **à cheval sur le milieu** de la breadboard, entre les colonnes e et f (rangées 11–12 par exemple).
2. Connectez un fil du **rail 3,3 V (+)** vers la **broche A** du bouton (côté haut, ex : e11).
3. Connectez un fil de la **broche C** du bouton (côté bas, ex : f12) vers la broche **GPIO17** (broche physique 11).
4. Connectez la résistance **10 kΩ** entre la **broche C** (ex : g12) et le **rail GND (-)**.
5. Connectez le **rail 3,3 V (+)** à la broche **3,3 V** du Raspberry Pi (broche physique 1).

---

## 2.4 Montage du LCD 1602

Le LCD 1602 possède **16 broches**. On l'utilise en mode **4 bits** pour réduire le nombre de fils.

### Brochage du LCD 1602

```
LCD 1602 — Vue de face (broches en bas)

 ┌────────────────────────────────────────────┐
 │  ████████████████████████████████████████  │ ← ligne 1
 │  ████████████████████████████████████████  │ ← ligne 2
 └────────────────────────────────────────────┘
   │  │  │  │  │  │  │  │  │  │  │  │  │  │  │  │
   1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16

  1 : VSS  → GND
  2 : VDD  → 5V
  3 : V0   → Curseur de contraste (via résistance 1,2 kΩ vers GND)
  4 : RS   → GPIO26
  5 : RW   → GND (on écrit seulement)
  6 : E    → GPIO19
  7 : D0   → (non connecté en mode 4 bits)
  8 : D1   → (non connecté en mode 4 bits)
  9 : D2   → (non connecté en mode 4 bits)
 10 : D3   → (non connecté en mode 4 bits)
 11 : D4   → GPIO13
 12 : D5   → GPIO6
 13 : D6   → GPIO5
 14 : D7   → GPIO0
 15 : A    → 3,3V (rétroéclairage +)
 16 : K    → GND  (rétroéclairage -)
```

### Schéma de connexion complet du LCD

```
Raspberry Pi            LCD 1602
─────────────           ─────────────────────────────
GND            ──────── VSS  (broche 1)
5V             ──────── VDD  (broche 2)
GND ──[1,2kΩ]─────────  V0   (broche 3)   ← contraste
GPIO26 (pin37) ──────── RS   (broche 4)
GND            ──────── RW   (broche 5)
GPIO19 (pin35) ──────── E    (broche 6)
                        D0 à D3 non connectés
GPIO13 (pin33) ──────── D4   (broche 11)
GPIO6  (pin31) ──────── D5   (broche 12)
GPIO5  (pin29) ──────── D6   (broche 13)
GPIO0  (pin27) ──────── D7   (broche 14)
3,3V           ──────── A    (broche 15)
GND            ──────── K    (broche 16)
```

**Instructions pas à pas pour le LCD :**

1. Insérez le LCD sur la breadboard (il s'insère sur les deux moitiés).
2. Connectez la broche **VSS (1)** au rail **GND (-)**.
3. Connectez la broche **VDD (2)** au rail **5V (+)** — utilisez la broche **5V** physique 2 ou 4 du Raspberry Pi.
4. Pour le **contraste (V0, broche 3)** : placez la résistance **1,2 kΩ** entre V0 et GND. Cela donne un contraste fixe correct pour débuter.
5. Connectez **RS (broche 4)** à **GPIO26**.
6. Connectez **RW (broche 5)** à **GND**.
7. Connectez **E (broche 6)** à **GPIO19**.
8. Laissez D0, D1, D2, D3 (broches 7–10) non connectées.
9. Connectez **D4 (broche 11)** à **GPIO13**.
10. Connectez **D5 (broche 12)** à **GPIO6**.
11. Connectez **D6 (broche 13)** à **GPIO5**.
12. Connectez **D7 (broche 14)** à **GPIO0**.
13. Connectez **A (broche 15)** à **3,3V**.
14. Connectez **K (broche 16)** à **GND**.

---

## 2.5 Vue d'ensemble du circuit complet

```
╔══════════════════════════════════════════════════════════════════╗
║                    CIRCUIT COMPLET — VUE ASCII                  ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║   Raspberry Pi                                                   ║
║   ┌──────────┐                                                   ║
║   │ [1] 3.3V │──────────────────────────── Rail (+) breadboard  ║
║   │ [2]  5V  │──────────────────────────── Rail (5V) breadboard ║
║   │ [6]  GND │──────────────────────────── Rail (-) breadboard  ║
║   │          │                                                   ║
║   │[11]GPIO17│──────┬─────[10kΩ]──── GND   ← Bouton            ║
║   │          │    Bouton                                         ║
║   │          │      └────────────────────── 3,3V                ║
║   │          │                                                   ║
║   │[13]GPIO27│───[220Ω]───[Anode+]LED[Cathode-]─── GND         ║
║   │          │                                                   ║
║   │[27]GPIO0 │──── D7  LCD (broche 14)                          ║
║   │[29]GPIO5 │──── D6  LCD (broche 13)                          ║
║   │[31]GPIO6 │──── D5  LCD (broche 12)                          ║
║   │[33]GPIO13│──── D4  LCD (broche 11)                          ║
║   │[35]GPIO19│──── E   LCD (broche 6)                           ║
║   │[37]GPIO26│──── RS  LCD (broche 4)                           ║
║   │          │                                                   ║
║   └──────────┘    LCD 1602                                       ║
║                   ┌─────────────────────┐                       ║
║   GND ────────────┤VSS (1)              │                       ║
║   5V  ────────────┤VDD (2)              │                       ║
║   GND──[1,2kΩ]───┤V0  (3)  ┌─────────┐│                       ║
║   GPIO26 ─────────┤RS  (4)  │ Ligne 1 ││                       ║
║   GND ────────────┤RW  (5)  │ Ligne 2 ││                       ║
║   GPIO19 ─────────┤E   (6)  └─────────┘│                       ║
║   GPIO13 ─────────┤D4  (11)             │                       ║
║   GPIO6  ─────────┤D5  (12)             │                       ║
║   GPIO5  ─────────┤D6  (13)             │                       ║
║   GPIO0  ─────────┤D7  (14)             │                       ║
║   3,3V ───────────┤A   (15)             │                       ║
║   GND ────────────┤K   (16)             │                       ║
║                   └─────────────────────┘                       ║
╚══════════════════════════════════════════════════════════════════╝
```

---

## 2.6 Vérification avant mise sous tension

Avant de brancher le Raspberry Pi, cochez chaque point :

- [ ] La LED est dans le bon sens (patte longue = anode vers la résistance 220 Ω)
- [ ] La résistance 220 Ω est entre GPIO27 et l'anode de la LED
- [ ] La résistance 10 kΩ est entre GPIO17 et GND (pull-down bouton)
- [ ] La résistance 1,2 kΩ est entre V0 (broche 3 LCD) et GND (contraste)
- [ ] Les broches VDD (2) du LCD sont connectées au **5V** (pas au 3,3V)
- [ ] RW (broche 5) du LCD est connecté à **GND**
- [ ] Tous les GND sont connectés au rail GND de la breadboard
- [ ] Le rail GND de la breadboard est connecté à une broche GND du Raspberry Pi

> Si tout est correct, vous pouvez brancher l'alimentation du Raspberry Pi.

---

## Prêt ?

Passez à l'étape suivante : [03_programmation.md](03_programmation.md)
