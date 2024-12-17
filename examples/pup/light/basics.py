from pybricks.pupdevices import Light
from pybricks.parameters import Port
from pybricks.tools import wait

# Initialiser la lumière.
light = Light(Port.A)

# Faire clignoter la lumière indéfiniment.
while True:
    # Allumer la lumière à 100% de luminosité.
    light.on(100)
    wait(500)

    # Éteindre la lumière.
    light.off()
    wait(500)
