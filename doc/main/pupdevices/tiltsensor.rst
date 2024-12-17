.. pybricks-requirements::

Capteur d'inclinaison
^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../main/cad/output/pupdevice-tilt.png
   :width: 35 %

.. blockimg:: pybricks_variables_set_tilt_sensor

.. autoclass:: pybricks.pupdevices.TiltSensor
    :no-members:

    .. blockimg:: pybricks_blockTilt_TiltSensor_imu.tilt.pitch

    .. blockimg:: pybricks_blockTilt_TiltSensor_imu.tilt.roll
        :stack:

    .. automethod:: tilt

Exemples
--------

Mesurer le tangage et le roulis
*******************************

.. literalinclude::
    ../../../examples/pup/sensor_tilt/basics.py
