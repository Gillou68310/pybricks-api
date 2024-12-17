from pybricks.pupdevices import ColorSensor
from pybricks.parameters import Port
from pybricks.tools import wait

# Initialiser le capteur.
sensor = ColorSensor(Port.A)

# Répéter indéfiniment.
while True:

    # Allumer une lumière à la fois, à moitié de la luminosité.
    # Faites cela pour les 3 lumières et répétez cela 5 fois.
    for i in range(5):
        sensor.lights.on([50, 0, 0])
        wait(100)
        sensor.lights.on([0, 50, 0])
        wait(100)
        sensor.lights.on([0, 0, 50])
        wait(100)

    # Allumer toutes les lumières à pleine luminosité.
    sensor.lights.on(100)
    wait(500)

    # Éteindre toutes les lumières.
    sensor.lights.off()
    wait(500)
