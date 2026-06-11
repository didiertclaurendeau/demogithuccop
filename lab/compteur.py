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
