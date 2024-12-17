#!/usr/bin/env pybricks-micropython

# Avant d'exécuter ce programme, assurez-vous que les briques EV3 client et serveur
# sont appariées via Bluetooth, mais ne les connectez PAS. Le programme se chargera
# d'établir la connexion.

# Le serveur doit être démarré avant le client !

from pybricks.messaging import BluetoothMailboxClient, TextMailbox

# Ceci est le nom de l'EV3 ou du PC distant auquel nous nous connectons.
SERVER = "ev3dev"

client = BluetoothMailboxClient()
mbox = TextMailbox("greeting", client)

print("establishing connection...")
client.connect(SERVER)
print("connected!")

# Dans ce programme, le client envoie le premier message puis attend que le
# serveur réponde.
mbox.send("hello!")
mbox.wait()
print(mbox.read())
