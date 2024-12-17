.. pybricks-requirements::

Capteur de force
^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../main/cad/output/pupdevice-force.png
   :width: 35 %

.. blockimg:: pybricks_variables_set_force_sensor

.. autoclass:: pybricks.pupdevices.ForceSensor
    :no-members:

    .. blockimg:: pybricks_blockForce_ForceSensor

    .. automethod:: pybricks.pupdevices.ForceSensor.force

    .. blockimg:: pybricks_blockDistance_ForceSensor

    .. automethod:: pybricks.pupdevices.ForceSensor.distance

    .. automethod:: pybricks.pupdevices.ForceSensor.pressed

    .. automethod:: pybricks.pupdevices.ForceSensor.touched

Exemples
--------

Mesurer la force et le mouvement
********************************

.. literalinclude::
    ../../../examples/pup/sensor_force/basics.py

Mesurer la force maximale
*************************

.. literalinclude::
    ../../../examples/pup/sensor_force/peak.py
