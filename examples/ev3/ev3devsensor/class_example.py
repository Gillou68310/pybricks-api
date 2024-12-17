#!/usr/bin/env pybricks-micropython
from pybricks.parameters import Port
from pybricks.iodevices import Ev3devSensor


class MySensor(Ev3devSensor):
    """Exemple d'extension de la classe Ev3devSensor."""

    def __init__(self, port):
        """Initialiser le capteur."""

        # Initialiser la classe parente.
        super().__init__(port)

        # Obtenir le chemin sysfs.
        self.path = "/sys/class/lego-sensor/sensor" + str(self.sensor_index)

    def get_modes(self):
        """Obtenir une liste de chaînes de modes pour ne pas avoir à les chercher."""

        # Le chemin du fichier des modes.
        modes_path = self.path + "/modes"

        # Ouvrir le fichier des modes.
        with open(modes_path, "r") as m:

            # Lire le contenu.
            contents = m.read()

            # Supprimer le symbole de nouvelle ligne et diviser à chaque symbole d'espace.
            return contents.strip().split(" ")


# Initialiser le capteur
sensor = MySensor(Port.S3)

# Montrer où ce capteur peut être trouvé
print(sensor.path)

# Imprimer les modes disponibles
modes = sensor.get_modes()
print(modes)

# Lire le mode 0 de ce capteur
val = sensor.read(modes[0])
print(val)
