#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.iodevices import I2CDevice
from pybricks.parameters import Port

# Initialize the EV3
ev3 = EV3Brick()

# Initialize I2C Sensor
device = I2CDevice(Port.S2, 0xD2 >> 1)

# Recommandé pour la lecture
(result,) = device.read(reg=0x0F, length=1)

# Lire 1 octet sans registre particulier :
device.read(reg=None, length=1)

# Lire 0 octet sans registre particulier :
device.read(reg=None, length=0)

# Les opérations d'écriture I2C consistent en un octet de registre suivi
# d'une série d'octets de données. Selon votre appareil, vous
# pouvez choisir de sauter le registre ou les données comme suit :

# Recommandé pour l'écriture :
device.write(reg=0x22, data=b"\x08")

# Écrire 1 octet sans registre particulier :
device.write(reg=None, data=b"\x08")

# Écrire 0 octet à un registre particulier :
device.write(reg=0x08, data=None)

# Écrire 0 octet sans registre particulier :
device.write(reg=None, data=None)
