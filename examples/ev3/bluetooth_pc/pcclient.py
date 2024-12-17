#!/usr/bin/env python3
from pybricks.messaging import BluetoothMailboxClient, TextMailbox

# Cette démo permet à votre PC de communiquer avec un EV3 via Bluetooth.
#
# Ceci est identique à l'exemple de client EV3 dans ../bluetooth_client
#
# La seule différence est qu'il s'exécute en Python3 sur votre ordinateur, grâce à
# l'implémentation Python3 du module de messagerie qui est incluse ici.
# En ce qui concerne l'EV3, il pense qu'il parle simplement à un client EV3.
#
# Ainsi, l'exemple de serveur EV3 ne nécessite aucune modification supplémentaire. La procédure de connexion
# est également la même que celle documentée dans les docs du module de messagerie :
# https://docs.pybricks.com/en/latest/messaging.html
#
# Alors, activez le Bluetooth sur votre PC et l'EV3. Vous devrez peut-être rendre le Bluetooth
# visible sur l'EV3. Vous pouvez ignorer l'appariement si vous connaissez déjà l'adresse de l'EV3.

# Ceci est l'adresse du serveur EV3 auquel nous nous connectons.
SERVER = "CC:78:AB:D8:4E:F6"

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
