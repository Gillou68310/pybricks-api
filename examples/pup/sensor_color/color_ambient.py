
from pybricks.pupdevices import ColorSensor
from pybricks.parameters import Port
from pybricks.tools import wait

# Initialiser le capteur.
sensor = ColorSensor(Port.A)

# Répéter indéfiniment.
while True:

    # Obtenez les valeurs de couleur ambiantes. Au lieu de scanner la couleur d'une surface,
    # cela vous permet de scanner la couleur de sources lumineuses comme des lampes ou des écrans.
    hsv = sensor.hsv(surface=False)
    color = sensor.color(surface=False)

    # Obtenez l'intensité de la lumière ambiante.
    ambient = sensor.ambient()

    # Imprimer les mesures.
    print(hsv, color, ambient)

    # Pointez le capteur vers un écran d'ordinateur ou une lumière colorée. Regardez la couleur.
    # Aussi, couvrez le capteur avec vos mains et regardez la valeur ambiante.

    # Attendre pour pouvoir lire la ligne imprimée.
    wait(100)
