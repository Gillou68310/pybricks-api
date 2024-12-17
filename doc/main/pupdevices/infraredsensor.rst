.. pybricks-requirements::

Capteur infrarouge
^^^^^^^^^^^^^^^^^^

.. figure:: ../../main/cad/output/pupdevice-infrared.png
   :width: 35 %

.. blockimg:: pybricks_variables_set_infrared_sensor

.. autoclass:: pybricks.pupdevices.InfraredSensor
    :no-members:

    .. blockimg:: pybricks_blockDistance_InfraredSensor

    .. automethod:: pybricks.pupdevices.InfraredSensor.distance

    .. blockimg:: pybricks_blockLightReflection_InfraredSensor

    .. automethod:: pybricks.pupdevices.InfraredSensor.reflection

    .. automethod:: pybricks.pupdevices.InfraredSensor.count

Exemples
--------

Mesurer la distance, le nombre d'objets et la réflexion
********************************************************

.. literalinclude::
    ../../../examples/pup/sensor_infrared/basics.py
