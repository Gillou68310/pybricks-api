.. pybricks-requirements::

Capteur Ultrasonique
^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../main/diagrams/sensor_ultrasonic_lights.png
   :width: 80 %

.. blockimg:: pybricks_variables_set_ultrasonic_sensor

.. autoclass:: pybricks.pupdevices.UltrasonicSensor
    :no-members:

    .. blockimg:: pybricks_blockDistance_UltrasonicSensor

    .. automethod:: pybricks.pupdevices.UltrasonicSensor.distance

    .. automethod:: pybricks.pupdevices.UltrasonicSensor.presence

    .. rubric:: Lumières intégrées

    Ce capteur a 4 lumières intégrées. Vous pouvez ajuster la luminosité de
    chaque lumière.

    .. blockimg:: pybricks_blockLightOn_ultrasonicsensor_on

    .. blockimg:: pybricks_blockLightOn_ultrasonicsensor_on_list
        :stack:

    .. automethod:: pybricks.pupdevices::UltrasonicSensor.lights.on

    .. blockimg:: pybricks_blockLightOn_ultrasonicsensor_off

    .. automethod:: pybricks.pupdevices::UltrasonicSensor.lights.off

Exemples
--------

Mesurer la distance et allumer les lumières
*******************************************

.. literalinclude::
    ../../../examples/pup/sensor_ultrasonic/basics.py

Changer progressivement la luminosité des lumières
**************************************************

.. literalinclude::
    ../../../examples/pup/sensor_ultrasonic/math.py
