#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.iodevices import I2CDevice
from pybricks.parameters import Port

# Initialiser l'EV3
ev3 = EV3Brick()

# Initialiser le capteur I2C
device = I2CDevice(Port.S2, 0xD2 >> 1)

# Lire un octet de l'appareil.
# Pour cet appareil, nous pouvons lire le registre Who Am I
# (0x0F) pour la valeur attendue : 211.
if 211 not in device.read(0x0F):
    raise ValueError("Unexpected I2C device ID")

# Pour écrire des données, créez un objet bytes d'un ou plusieurs octets. Par exemple :
# data = bytes((1, 2, 3))

# Écrire un octet (valeur 0x08) dans le registre 0x22
device.write(0x22, bytes((0x08,)))
