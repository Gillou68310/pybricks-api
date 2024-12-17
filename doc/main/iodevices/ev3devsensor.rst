Capteurs Ev3dev
^^^^^^^^^^^^^^^

.. note::

   Cette classe est uniquement disponible sur EV3.

.. figure:: ../../main/cad/output/iodevice-rj12pcbbox.png
   :width: 30 %

EV3 MicroPython est construit sur ev3dev, ce qui signifie qu'un capteur peut
être supporté même s'il n'est pas listé dans cette documentation. Si c'est le
cas, vous pouvez l'utiliser avec la classe ``Ev3devSensor``. C'est plus facile
et plus rapide que d'utiliser les classes d'appareils personnalisés données
ci-dessus.

Pour vérifier si vous pouvez utiliser la classe ``Ev3devSensor`` :

    * Branchez le capteur sur votre brique EV3.
    * Allez dans le menu principal de la brique EV3.
    * Sélectionnez `Device Browser` puis `Sensors`.
    * Si votre capteur apparaît, vous pouvez l'utiliser.

Sélectionnez maintenant votre capteur dans le menu et choisissez `set mode`.
Cela montre tous les modes disponibles pour ce capteur. Vous pouvez utiliser
ces noms de modes comme paramètre ``mode`` ci-dessous.

Pour en savoir plus sur les appareils compatibles et ce que chaque mode fait,
visitez la page `ev3dev sensors`_.

.. autoclass:: pybricks.iodevices.Ev3devSensor
    :no-members:

    .. autoattribute:: pybricks.iodevices.Ev3devSensor.sensor_index
        :annotation:

    .. autoattribute:: pybricks.iodevices.Ev3devSensor.port_index
        :annotation:

    .. automethod:: pybricks.iodevices.Ev3devSensor.read

**Exemple : Lire des valeurs avec la classe Ev3devSensor**

Dans cet exemple, nous utilisons le capteur de couleur LEGO MINDSTORMS EV3
avec le mode RGB brut. Cela donne des valeurs de réflexion rouge, vert et bleu
non calibrées.

.. literalinclude::
   ../../../examples/ev3/ev3devsensor/main.py

**Exemple : Étendre la classe Ev3devSensor**

Cet exemple montre comment étendre la classe ``Ev3devSensor`` en accédant à
des fonctionnalités supplémentaires trouvées dans le dossier système Linux
pour cet appareil.

.. literalinclude::
   ../../../examples/ev3/ev3devsensor/class_example.py

.. _ev3dev sensors: http://docs.ev3dev.org/projects/lego-linux-drivers/en/ev3dev-stretch/sensors.html
.. _Mode name: http://docs.ev3dev.org/projects/lego-linux-drivers/en/ev3dev-stretch/sensor_data.html
.. _lego-sensor: http://docs.ev3dev.org/projects/lego-linux-drivers/en/ev3dev-stretch/sensors.html#the-lego-sensor-subsytem
.. _lego-port: http://docs.ev3dev.org/projects/lego-linux-drivers/en/ev3dev-stretch/ports.html#the-lego-port-subsystem
