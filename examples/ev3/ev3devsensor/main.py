#!/usr/bin/env pybricks-micropython
from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks.iodevices import Ev3devSensor

# Initialiser un Ev3devSensor.
# Dans cet exemple, nous utilisons le
# capteur de couleur LEGO MINDSTORMS EV3.
sensor = Ev3devSensor(Port.S3)

while True:
    # Lire les valeurs brutes RGB
    r, g, b = sensor.read("RGB-RAW")

    # Imprimer les résultats
    print("R: {0}\t G: {1}\t B: {2}".format(r, g, b))

    # Attendre
    wait(200)
