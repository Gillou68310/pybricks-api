Appareil UART générique
^^^^^^^^^^^^^^^^^^^^^^^

.. note::

   Cette classe est **seulement supportée sur l'EV3** pour le moment. Elle
   pourrait être ajoutée aux hubs Powered Up dans une future version. Si vous
   souhaitez que cela se produise, assurez-vous de nous le demander sur notre
   `support page`_.

.. _support page: https://github.com/pybricks/support/issues/

.. figure:: ../../main/cad/output/iodevice-rj12grey.png
   :width: 25 %

.. autoclass:: pybricks.iodevices.UARTDevice

**Exemple : Lire et écrire sur un appareil UART**

.. literalinclude::
   ../../../examples/ev3/uart_basics/main.py
