from pybricks.pupdevices import UltrasonicSensor
from pybricks.parameters import Port
from pybricks.tools import wait, StopWatch

from umath import pi, sin

# Initialiser le capteur.
eyes = UltrasonicSensor(Port.A)

# Initialiser un chronomètre.
watch = StopWatch()

# Nous voulons qu'un cycle complet de lumière dure trois secondes.
PERIOD = 3000

while True:
    # La phase est où nous en sommes dans le cercle unité maintenant.
    phase = watch.time() / PERIOD * 2 * pi

    # Chaque lumière suit une onde sinusoïdale avec une moyenne de 50, avec une amplitude de 50.
    # Nous décalons cette onde sinusoïdale de 90 degrés pour chaque lumière, afin que toutes les
    # lumières fassent quelque chose de différent.
    brightness = [sin(phase + offset * pi / 2) * 50 + 50 for offset in range(4)]

    # Régler les valeurs de luminosité pour toutes les lumières.
    eyes.lights.on(brightness)

    # Attendre un certain temps.
    wait(50)
