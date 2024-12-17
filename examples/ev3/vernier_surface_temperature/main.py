#!/usr/bin/env pybricks-micropython
from pybricks.parameters import Port
from pybricks.nxtdevices import VernierAdapter

from math import log

# Formule de conversion pour le capteur de température de surface
def convert_raw_to_temperature(voltage):
    # Convertir la tension brute en résistance NTC
    # selon le bloc Vernier Adapter EV3.
    counts = voltage / 5000 * 4096
    ntc = 15000 * (counts) / (4130 - counts)

    # Gérer log(0) en toute sécurité : s'assurer que la valeur ntc est positive.
    if ntc <= 0:
        ntc = 1

    # Appliquer l'équation de Steinhart-Hart comme indiqué dans la documentation du capteur.
    K0 = 1.02119e-3
    K1 = 2.22468e-4
    K2 = 1.33342e-7
    return 1 / (K0 + K1 * log(ntc) + K2 * log(ntc) ** 3)

# Initialiser l'adaptateur sur le port 1
thermometer = VernierAdapter(Port.S1, convert_raw_to_temperature)

# Obtenir la valeur mesurée et l'imprimer
temp = thermometer.value()
print(temp)
