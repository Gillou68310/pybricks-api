from pybricks.pupdevices import ColorDistanceSensor
from pybricks.parameters import Port, Color
from pybricks.tools import wait

# Initialiser le capteur.
sensor = ColorDistanceSensor(Port.A)

# Répéter indéfiniment.
while True:

    # Si le capteur voit un objet à proximité.
    if sensor.distance() <= 40:

        # Alors clignotez la lumière rouge/bleu 5 fois.
        for i in range(5):
            sensor.light.on(Color.RED)
            wait(30)
            sensor.light.on(Color.BLUE)
            wait(30)
    else:
        # Si le capteur ne voit rien
        # à proximité, attendez juste un peu.
        wait(10)
