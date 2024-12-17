Appareil I2C générique
^^^^^^^^^^^^^^^^^^^^^^

.. note::

   Cette classe est **seulement supportée sur l'EV3** pour le moment. Elle
   pourrait être ajoutée aux hubs Powered Up dans une future version. Si vous
   souhaitez que cela se produise, assurez-vous de nous le demander sur notre
   `support page`_.

.. _support page: https://github.com/pybricks/support/issues/

.. figure:: ../../main/cad/output/iodevice-rj12cyan.png
   :width: 25 %

.. autoclass:: pybricks.iodevices.I2CDevice

**Exemple : Lire et écrire sur un appareil I2C**

.. literalinclude:: ../../../examples/ev3/i2c_basics/main.py

.. _i2caddress:

Adresses I2C
------------

Les adresses I2C sont des valeurs sur 7 bits. Cependant, la plupart des
vendeurs qui fabriquent des capteurs compatibles LEGO fournissent une adresse
sur 8 bits dans leur documentation. Pour utiliser ces adresses, vous devez les
décaler de 1 bit. Par exemple, si l'adresse documentée est ``0xD2``, vous
pouvez faire ``address = 0xD2 >> 1``.

Commandes I2C avancées
----------------------

Certains appareils I2C rudimentaires ne nécessitent pas d'argument de registre
ni même de données. Vous pouvez obtenir ce comportement comme montré dans les
exemples ci-dessous.

**Exemple : Techniques avancées de lecture et d'écriture I2C**

.. literalinclude:: ../../../examples/ev3/i2c_extra/main.py

**Ressources techniques supplémentaires**

Les méthodes de la classe ``I2CDevice`` appellent des fonctions du pilote
Linux SMBus. Pour savoir quelles commandes sont appelées en coulisses,
consultez le `Pybricks source code`_. Plus de détails sur l'utilisation de
l'I2C sans MicroPython peuvent être trouvés sur la page `ev3dev I2C`_.

.. _ev3dev I2C: http://docs.ev3dev.org/projects/lego-linux-drivers/en/ev3dev-stretch/i2c.html
.. _Pybricks source code: https://github.com/pybricks/pybricks-micropython
