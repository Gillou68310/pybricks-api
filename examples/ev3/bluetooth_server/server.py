#!/usr/bin/env pybricks-micropython

# Avant d'exécuter ce programme, assurez-vous que les briques EV3 client et serveur
# sont appariées via Bluetooth, mais ne les connectez PAS. Le programme se chargera
# d'établir la connexion.

# Le serveur doit être démarré avant le client !

from pybricks.messaging import BluetoothMailboxServer, TextMailbox

server = BluetoothMailboxServer()
mbox = TextMailbox("greeting", server)

# Le serveur doit être démarré avant le client !
print("waiting for connection...")
server.wait_for_connection()
print("connected!")

# Dans ce programme, le serveur attend que le client envoie le premier message
# puis envoie une réponse.
mbox.wait()
print(mbox.read())
mbox.send("hello to you!")
