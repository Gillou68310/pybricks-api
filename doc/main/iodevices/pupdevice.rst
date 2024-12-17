.. pybricks-requirements:: pybricks-iodevices

Appareil Powered Up
^^^^^^^^^^^^^^^^^^^

.. figure:: ../cad/output/iodevice-pupdevice.png
   :width: 60 %

.. autoclass:: pybricks.iodevices.PUPDevice
    :no-members:

    .. automethod:: pybricks.iodevices.PUPDevice.info

    .. automethod:: pybricks.iodevices.PUPDevice.read

    .. automethod:: pybricks.iodevices.PUPDevice.write

Exemples
--------

Détection des appareils
************************

.. literalinclude::
    ../../../examples/pup/iodevices_pupdevice/port_info.py
