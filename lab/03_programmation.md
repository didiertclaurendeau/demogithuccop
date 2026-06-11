# Étape 3 — Programmation en Python

## 3.1 Ouvrir un éditeur de texte

Sur le Raspberry Pi, ouvrez un terminal et créez un nouveau fichier Python :

```bash
cd ~
mkdir -p mon_lab_iot
cd mon_lab_iot
nano compteur.py
```

> `nano` est un éditeur de texte simple dans le terminal.  
> Pour sauvegarder : `Ctrl + O` puis `Entrée`.  
> Pour quitter : `Ctrl + X`.

---

## 3.2 Le code complet

Copiez le code suivant **exactement tel quel** dans votre fichier `compteur.py` :

```python
#!/usr/bin/env python3
"""
Laboratoire IoT — Compteur avec bouton, LED et LCD 1602
"""

import RPi.GPIO as GPIO
import time
from RPLCD.gpio import CharLCD

# ─────────────────────────────────────────────
# Configuration des broches GPIO
# ─────────────────────────────────────────────
PIN_BOUTON = 17   # Broche GPIO du bouton-poussoir
PIN_LED    = 27   # Broche GPIO de la LED

# ─────────────────────────────────────────────
# Initialisation de GPIO
# ─────────────────────────────────────────────
GPIO.setmode(GPIO.BCM)          # On utilise les numéros GPIO (BCM)
GPIO.setwarnings(False)

GPIO.setup(PIN_BOUTON, GPIO.IN)           # Bouton = entrée
GPIO.setup(PIN_LED, GPIO.OUT)             # LED = sortie
GPIO.output(PIN_LED, GPIO.LOW)            # LED éteinte au démarrage

# ─────────────────────────────────────────────
# Initialisation du LCD 1602 (mode 4 bits)
# ─────────────────────────────────────────────
lcd = CharLCD(
    pin_rs=26,
    pin_e=19,
    pins_data=[13, 6, 5, 0],   # D4, D5, D6, D7
    numbering_mode=GPIO.BCM,
    cols=16,
    rows=2
)

# ─────────────────────────────────────────────
# Affichage du message de démarrage
# ─────────────────────────────────────────────
lcd.clear()
lcd.write_string("Lab IoT")
lcd.cursor_pos = (1, 0)         # Déplacer le curseur sur la ligne 2
lcd.write_string("Compteur: 0")

# ─────────────────────────────────────────────
# Variables
# ─────────────────────────────────────────────
compteur = 0
bouton_precedent = GPIO.LOW     # État précédent du bouton

print("Programme démarré. Appuyez sur le bouton.")
print("Pour arrêter : Ctrl + C")

# ─────────────────────────────────────────────
# Boucle principale
# ─────────────────────────────────────────────
try:
    while True:
        etat_bouton = GPIO.input(PIN_BOUTON)

        # Détection du front montant (bouton vient d'être pressé)
        if etat_bouton == GPIO.HIGH and bouton_precedent == GPIO.LOW:
            compteur += 1
            print(f"Bouton pressé ! Compteur = {compteur}")

            # Allumer la LED pendant 0,5 seconde
            GPIO.output(PIN_LED, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(PIN_LED, GPIO.LOW)

            # Mettre à jour l'affichage du LCD
            lcd.cursor_pos = (1, 0)
            lcd.write_string(f"Compteur: {compteur}  ")  # espaces pour effacer

        bouton_precedent = etat_bouton
        time.sleep(0.05)    # Petite pause pour éviter les rebonds (debounce)

except KeyboardInterrupt:
    print("\nArrêt du programme.")

finally:
    lcd.clear()
    lcd.write_string("Au revoir !")
    time.sleep(1)
    lcd.clear()
    GPIO.cleanup()
    print("GPIO nettoyés. Programme terminé.")
```

---

## 3.3 Explication du code section par section

### Importation des bibliothèques

```python
import RPi.GPIO as GPIO
import time
from RPLCD.gpio import CharLCD
```

| Bibliothèque | Rôle |
|---|---|
| `RPi.GPIO` | Contrôle des broches GPIO du Raspberry Pi |
| `time` | Permet de faire des pauses (`time.sleep`) |
| `RPLCD.gpio` | Contrôle du LCD 1602 |

---

### Configuration GPIO

```python
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_BOUTON, GPIO.IN)
GPIO.setup(PIN_LED, GPIO.OUT)
```

- `GPIO.BCM` signifie qu'on utilise les **numéros GPIO** (pas les numéros de broches physiques).
- `GPIO.IN` = la broche est une **entrée** (elle lit un signal).
- `GPIO.OUT` = la broche est une **sortie** (elle envoie un signal).

---

### Initialisation du LCD

```python
lcd = CharLCD(
    pin_rs=26,
    pin_e=19,
    pins_data=[13, 6, 5, 0],
    ...
)
```

On indique à la bibliothèque quelles broches GPIO sont connectées aux broches RS, E, D4, D5, D6, D7 du LCD.

---

### Détection du front montant (appui sur le bouton)

```python
if etat_bouton == GPIO.HIGH and bouton_precedent == GPIO.LOW:
```

On ne réagit que quand le bouton **vient d'être pressé** (transition de LOW → HIGH).  
Cela évite de compter plusieurs fois si on maintient le bouton appuyé.

```
État du bouton dans le temps :

Bouton relâché :  ___________
Bouton pressé  :             ‾‾‾‾‾‾‾‾‾

On réagit ici →             ↑ (front montant)
```

---

### Anti-rebond (debounce)

```python
time.sleep(0.05)
```

Quand un bouton est pressé physiquement, le contact électrique n'est pas parfait et oscille rapidement pendant quelques millisecondes. La pause de 50 ms permet d'ignorer ces oscillations parasites.

---

### Nettoyage final

```python
finally:
    GPIO.cleanup()
```

`GPIO.cleanup()` remet toutes les broches dans leur état par défaut. C'est une **bonne pratique** à toujours inclure pour ne pas laisser le GPIO dans un état indéfini.

---

## 3.4 Lancer le programme

Dans le terminal, depuis le dossier `mon_lab_iot` :

```bash
python3 compteur.py
```

Vous devriez voir s'afficher dans le terminal :

```
Programme démarré. Appuyez sur le bouton.
Pour arrêter : Ctrl + C
```

Et sur le LCD :
```
┌────────────────┐
│Lab IoT         │
│Compteur: 0     │
└────────────────┘
```

---

## Prêt ?

Passez à l'étape suivante : [04_test_validation.md](04_test_validation.md)
