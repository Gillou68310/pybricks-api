:mod:`messaging <pybricks.messaging>` -- Messagerie
===================================================

.. module:: pybricks.messaging

.. currentmodule:: pybricks.messaging

Un EV3 Brick peut envoyer des informations à un autre EV3 Brick en utilisant
Bluetooth. Cette page vous montre comment connecter plusieurs briques et
comment écrire des scripts pour envoyer des messages entre elles.

Appairage de deux EV3 Bricks
----------------------------

Avant que deux EV3 Bricks puissent échanger des messages, elles doivent être
*appairées*. Vous n'aurez besoin de le faire que la première fois. Tout
d'abord, activez le Bluetooth sur toutes les EV3 Bricks comme indiqué dans
:numref:`fig_bluetooth_on`.

.. _fig_bluetooth_on:

.. figure:: ../main/diagrams/bluetooth_on.png
   :width: 100 %
   :alt: bluetooth_on
   :align: center

   Activez le Bluetooth et rendez le Bluetooth visible.

Maintenant, vous pouvez faire en sorte qu'une EV3 Brick recherche l'autre et
s'appaire avec elle, comme indiqué dans :numref:`fig_bluetooth_pair`.

Une fois qu'elles sont appairées, ne cliquez *pas* sur *connecter* dans le
menu qui apparaît. La connexion sera établie lorsque vous exécuterez vos
programmes, comme décrit ci-dessous.

.. _fig_bluetooth_pair:

.. figure:: ../main/diagrams/bluetooth_pair.png
   :width: 100 %
   :alt: bluetooth_pair
   :align: center

   Appairage d'une EV3 Brick à une autre EV3 Brick.

Lorsque vous scannez les appareils Bluetooth, vous verrez une liste de noms
d'appareils. Par défaut, toutes les EV3 Bricks sont nommées *ev3dev*. Cliquez
`here`_ pour apprendre comment changer ce nom. Cela facilite leur distinction.

Répétez les étapes dans :numref:`fig_bluetooth_pair` si vous souhaitez
appairer plus de deux EV3 Bricks.

Serveur et Client
-----------------

Un réseau sans fil se compose de EV3 Bricks agissant comme serveurs ou
clients. Un exemple avec un serveur et un client est montré dans
:numref:`fig_messaging`. Les messages peuvent être envoyés dans les deux sens
: le serveur peut envoyer un message au client, et le client peut envoyer un
message au serveur.

.. _fig_messaging:

.. figure:: ../main/diagrams/messaging.png
   :width: 90 %
   :alt: messaging
   :align: center

   Un exemple de réseau avec un serveur et un client.

La seule différence entre le client et le serveur est lequel initie la
connexion au début du programme :

    - Le **serveur** doit toujours être démarré en premier. Il utilise la
      classe ``BluetoothMailboxServer``. Ensuite, il attend les clients en
      utilisant la méthode ``wait_for_connection``.
    - Le **client** utilise la classe ``BluetoothMailboxClient``. Il se
      connecte au serveur en utilisant la méthode ``connect``.
    - Après cela, l'envoi et la réception de messages se font de la même
      manière sur les deux EV3 Bricks.

.. autoclass:: BluetoothMailboxServer

.. autoclass:: BluetoothMailboxClient

Boîtes aux lettres
------------------

Les boîtes aux lettres sont utilisées pour envoyer des données vers et depuis
d'autres EV3 Bricks.

Une boîte aux lettres a un ``nom``, similaire au "sujet" d'un email. Si deux
EV3 Bricks ont une boîte aux lettres avec le même nom, elles peuvent s'envoyer
des messages. Chaque EV3 Brick peut lire sa propre boîte aux lettres et
envoyer des messages à la boîte aux lettres de l'autre EV3 Brick.

En fonction du type de messages que vous souhaitez échanger (octets, booléens,
nombres ou texte), vous pouvez choisir l'une des boîtes aux lettres
ci-dessous.

.. autoclass:: Mailbox

.. autoclass:: LogicMailbox
    :no-members:

.. autoclass:: NumericMailbox
    :no-members:

.. autoclass:: TextMailbox
    :no-members:

Exemples
--------

**Serveur Bluetooth EV3**

Voici la version complète de l'extrait montré dans :numref:`fig_messaging`.

.. literalinclude:: ../../examples/ev3/bluetooth_server/server.py

**Client Bluetooth EV3**

Voici la version complète de l'extrait montré dans :numref:`fig_messaging`.

.. literalinclude:: ../../examples/ev3/bluetooth_client/client.py

Créer des réseaux plus grands
-----------------------------

Les classes de ce module ne sont pas limitées à seulement deux EV3 Bricks. Par
exemple, vous pouvez ajouter plus de clients à votre réseau. Un exemple avec
du pseudo-code est montré dans :numref:`fig_messaging_network`.

.. _fig_messaging_network:

.. figure:: ../main/diagrams/messaging_network.png
   :width: 90 %
   :alt: messaging
   :align: center

   Un exemple de réseau avec un serveur et deux clients.

.. _here: https://pybricks.com/install/mindstorms-ev3/beyond-micropython
