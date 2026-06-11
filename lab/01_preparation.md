# Étape 1 — Préparation du Raspberry Pi

## 1.1 Vérifier que le Raspberry Pi est opérationnel

1. Branchez un clavier, une souris et un écran (HDMI) au Raspberry Pi.
2. Branchez l'alimentation (câble micro-USB ou USB-C selon le modèle).
3. Attendez que le bureau Raspberry Pi OS s'affiche.

> Si le Raspberry Pi ne démarre pas, appelez le chargé de laboratoire.

---

## 1.2 Ouvrir un terminal

Depuis le bureau, cliquez sur l'icône du terminal en haut à gauche, ou appuyez sur :

```
Ctrl + Alt + T
```

---

## 1.3 Mettre à jour le système (si demandé par le chargé de lab)

Dans le terminal, entrez les commandes suivantes **une par une** et attendez la fin de chaque commande avant de passer à la suivante :

```bash
sudo apt update
sudo apt upgrade -y
```

---

## 1.4 Installer les bibliothèques Python nécessaires

Le code utilise la bibliothèque `RPi.GPIO` (déjà installée par défaut) et `RPLCD` pour le LCD.

Installez `RPLCD` avec la commande suivante :

```bash
pip3 install RPLCD
```

Vérifiez que l'installation s'est bien passée :

```bash
python3 -c "import RPLCD; print('RPLCD OK')"
```

Vous devriez voir s'afficher : `RPLCD OK`

---

## 1.5 Identifier les broches GPIO du Raspberry Pi

Le Raspberry Pi possède **40 broches** sur le côté. Voici le schéma de référence que vous utiliserez tout au long du lab :

```
Raspberry Pi — Connecteur GPIO 40 broches
Vue de dessus (broches vers le haut, port USB à droite)

     3.3V  [ 1][ 2]  5V
    GPIO2  [ 3][ 4]  5V
    GPIO3  [ 5][ 6]  GND
    GPIO4  [ 7][ 8]  GPIO14
      GND  [ 9][10]  GPIO15
   GPIO17  [11][12]  GPIO18
   GPIO27  [13][14]  GND
   GPIO22  [15][16]  GPIO23
     3.3V  [17][18]  GPIO24
   GPIO10  [19][20]  GND
    GPIO9  [21][22]  GPIO25
   GPIO11  [23][24]  GPIO8
      GND  [25][26]  GPIO7
    GPIO0  [27][28]  GPIO1
    GPIO5  [29][30]  GND
    GPIO6  [31][32]  GPIO12
   GPIO13  [33][34]  GND
   GPIO19  [35][36]  GPIO16
   GPIO26  [37][38]  GPIO20
      GND  [39][40]  GPIO21
```

> **Attention :** Le numéro de broche (1 à 40) et le numéro GPIO sont **différents**. Dans ce lab, on utilise toujours les **numéros GPIO** (ex. : GPIO17, GPIO27...).

---

## Broches utilisées dans ce laboratoire

| Signal | Broche GPIO | Broche physique |
|--------|-------------|-----------------|
| Bouton | GPIO17 | 11 |
| LED | GPIO27 | 13 |
| LCD RS | GPIO26 | 37 |
| LCD E  | GPIO19 | 35 |
| LCD D4 | GPIO13 | 33 |
| LCD D5 | GPIO6  | 31 |
| LCD D6 | GPIO5  | 29 |
| LCD D7 | GPIO0  | 27 |
| Alimentation | 3,3 V | 1 |
| Masse (GND) | GND | 6, 9, 14... |

---

## Prêt ?

Passez à l'étape suivante : [02_montage.md](02_montage.md)
