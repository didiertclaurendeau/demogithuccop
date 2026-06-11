# Laboratoire IoT — Compteur avec bouton, LED et LCD

## Objectif

Dans ce laboratoire, vous allez réaliser votre premier montage IoT sur une plaquette de prototypage (*breadboard*) avec un Raspberry Pi.

**À la fin du lab, votre circuit devra :**
- Détecter l'appui sur un bouton-poussoir
- Allumer une LED pendant **0,5 seconde** à chaque appui
- Incrémenter un compteur affiché sur un **écran LCD 1602**

---

## Matériel requis

| Quantité | Composant |
|----------|-----------|
| 1 | Raspberry Pi (modèle 3B+ ou 4) |
| 1 | Plaquette de prototypage (breadboard) |
| 1 | Écran LCD 1602 (interface 4 bits) |
| 1 | LED (couleur au choix) |
| 1 | Bouton-poussoir (tactile) |
| 1 | Résistance **220 Ω** (pour la LED) |
| 1 | Résistance **10 kΩ** (pull-down pour le bouton) |
| 1 | Résistance **1,2 kΩ** (contraste du LCD) |
| — | Fils de connexion (jumpers) |

---

## Structure du laboratoire

| Étape | Fichier | Description |
|-------|---------|-------------|
| 1 | [01_preparation.md](01_preparation.md) | Préparation du Raspberry Pi |
| 2 | [02_montage.md](02_montage.md) | Montage des composants sur la breadboard |
| 3 | [03_programmation.md](03_programmation.md) | Écriture et explication du code Python |
| 4 | [04_test_validation.md](04_test_validation.md) | Test et validation du montage |

---

## Consignes générales

- **Ne jamais brancher ou débrancher des composants** lorsque le Raspberry Pi est sous tension.
- Vérifiez chaque connexion **avant** de mettre sous tension.
- En cas de doute, appelez le chargé de laboratoire.
- Prenez soin du matériel : les composants sont fragiles et partagés entre les groupes.

---

> **Temps estimé :** 2 à 3 heures  
> **Niveau :** Débutant — aucune expérience préalable requise
