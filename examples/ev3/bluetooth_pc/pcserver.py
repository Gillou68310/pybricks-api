#!/usr/bin/env python3
from pybricks.messaging import BluetoothMailboxServer, TextMailbox

# Cette démo permet à votre PC de communiquer avec un EV3 via Bluetooth.
#
# Ceci est identique à l'exemple de serveur EV3 dans ../bluetooth_server
#
# La seule différence est qu'il s'exécute en Python3 sur votre ordinateur, grâce à
# l'implémentation Python3 du module de messagerie qui est incluse ici.
# En ce qui concerne l'EV3, il pense qu'il parle simplement à un client EV3.
#
# Ainsi, l'exemple de client EV3 ne nécessite aucune modification supplémentaire. La procédure de connexion
# est également la même que celle documentée dans les docs du module de messagerie :
# https://docs.pybricks.com/en/latest/messaging.html

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
