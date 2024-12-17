from pybricks.pupdevices import Light
from pybricks.parameters import Port
from pybricks.tools import wait, StopWatch

from umath import pi, cos

# Initialiser la lumière et un chronomètre.
light = Light(Port.A)
watch = StopWatch()

# Propriétés du motif cosinus.
PERIOD = 2000
MAX = 100

# Faire varier la luminosité.
while True:
    # Obtenir la phase du cosinus.
    phase = watch.time() / PERIOD * 2 * pi

    # Évaluer la luminosité.
    brightness = (0.5 - 0.5 * cos(phase)) * MAX

    # Régler la luminosité de la lumière et attendre un peu.
    light.on(brightness)
    wait(10)
