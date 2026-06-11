# Étape 4 — Test et validation

## 4.1 Vérifications préalables

Avant de lancer le programme, assurez-vous que :

- [ ] Le Raspberry Pi est allumé et le bureau est visible
- [ ] Un terminal est ouvert
- [ ] La bibliothèque RPLCD est installée (voir [01_preparation.md](01_preparation.md))
- [ ] Vous êtes dans le bon dossier :

```bash
cd ~/mon_lab_iot
ls
```

Vous devriez voir le fichier `compteur.py` dans la liste.

---

## 4.2 Lancer le programme

```bash
python3 compteur.py
```

---

## 4.3 Résultats attendus

### Au démarrage

| Quoi | Ce que vous devez voir |
|------|----------------------|
| Terminal | `Programme démarré. Appuyez sur le bouton.` |
| LCD ligne 1 | `Lab IoT` |
| LCD ligne 2 | `Compteur: 0` |
| LED | Éteinte |

```
LCD après démarrage :
┌────────────────┐
│Lab IoT         │
│Compteur: 0     │
└────────────────┘
```

---

### À chaque appui sur le bouton

| Quoi | Ce que vous devez voir |
|------|----------------------|
| LED | S'allume pendant 0,5 seconde, puis s'éteint |
| LCD ligne 2 | `Compteur: 1` (puis 2, 3, ...) |
| Terminal | `Bouton pressé ! Compteur = 1` |

```
LCD après 3 appuis :
┌────────────────┐
│Lab IoT         │
│Compteur: 3     │
└────────────────┘
```

---

### À l'arrêt (Ctrl + C)

| Quoi | Ce que vous devez voir |
|------|----------------------|
| LCD | `Au revoir !` pendant 1 seconde, puis s'efface |
| Terminal | `GPIO nettoyés. Programme terminé.` |

---

## 4.4 Problèmes courants et solutions

### La LED ne s'allume pas

```
Diagnostic :
  1. Vérifier le sens de la LED (patte longue = anode vers GPIO27)
  2. Vérifier que la résistance 220 Ω est bien placée
  3. Tester la LED en la branchant directement entre 3,3V et GND avec la résistance
```

### Le LCD ne s'affiche pas (rien sur l'écran)

```
Diagnostic :
  1. Vérifier que le 5V est bien connecté à VDD (broche 2 du LCD)
  2. Vérifier la résistance de contraste 1,2 kΩ sur V0 (broche 3)
     → Essayez de remplacer la résistance par un fil direct vers GND
       pour avoir le contraste maximum et voir si des caractères apparaissent
  3. Vérifier toutes les connexions D4-D7, RS, E, RW
  4. Vérifier que RW est bien connecté à GND (pas à 3,3V)
```

### Le compteur s'incrémente plusieurs fois par appui

```
Diagnostic :
  → C'est un problème de "rebond" (bouncing) du bouton
  → Le délai de 50ms devrait suffire, mais si le problème persiste :
     Augmentez le délai dans le code :
       time.sleep(0.05)  →  time.sleep(0.1)
```

### Erreur Python : "RuntimeError: No access to /dev/mem"

```
Solution :
  Lancez le programme avec sudo :
    sudo python3 compteur.py
```

### Erreur Python : "ModuleNotFoundError: No module named 'RPLCD'"

```
Solution :
  pip3 install RPLCD
  (ou sudo pip3 install RPLCD si nécessaire)
```

### Le bouton ne réagit pas

```
Diagnostic :
  1. Vérifier que GPIO17 est bien connecté à un côté du bouton
  2. Vérifier que l'autre côté du bouton est bien connecté au 3,3V
  3. Vérifier la résistance pull-down 10 kΩ entre GPIO17 et GND
  4. Tester le bouton en ajoutant ce code de diagnostic :

     import RPi.GPIO as GPIO
     GPIO.setmode(GPIO.BCM)
     GPIO.setup(17, GPIO.IN)
     while True:
         print(GPIO.input(17))
         import time; time.sleep(0.1)
```

---

## 4.5 Questions de réflexion

Répondez à ces questions dans votre rapport de laboratoire :

1. **Pourquoi utilise-t-on une résistance pull-down (10 kΩ) avec le bouton ?**  
   Que se passerait-il si on ne l'utilisait pas ?

2. **Pourquoi utilise-t-on une résistance de 220 Ω avec la LED ?**  
   Que risque-t-il d'arriver à la LED sans résistance ?

3. **Qu'est-ce que le "debounce" (anti-rebond) et pourquoi est-il nécessaire ?**

4. **Pourquoi le LCD est-il alimenté en 5V alors que les signaux GPIO sont en 3,3V ?**

5. **Modifiez le programme pour que le LCD affiche aussi le nombre d'appuis sur la première ligne.**

---

## 4.6 Pour aller plus loin (optionnel)

Si vous terminez en avance, voici des défis supplémentaires :

- **Défi 1 :** Ajouter un deuxième bouton qui **remet le compteur à zéro**.
- **Défi 2 :** Faire **clignoter** la LED 3 fois rapidement au lieu de rester allumée 0,5s.
- **Défi 3 :** Afficher sur la première ligne du LCD un message différent selon si le compteur est pair ou impair.
- **Défi 4 :** Sauvegarder la valeur du compteur dans un fichier texte pour qu'elle persiste après redémarrage.

---

## Félicitations !

Vous avez réalisé votre premier montage IoT avec un Raspberry Pi.  
Vous avez appris à :

- Connecter des composants électroniques sur une breadboard
- Utiliser les broches GPIO en entrée et en sortie
- Contrôler une LED et lire un bouton en Python
- Afficher des informations sur un écran LCD

---

> Retour au début : [README.md](lab/README.md)
