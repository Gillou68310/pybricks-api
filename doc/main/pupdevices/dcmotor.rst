.. pybricks-requirements::

Moteurs sans capteurs de rotation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _fig_pupdcmotors:

.. figure:: ../../main/diagrams/pupdcmotors.png
   :width: 70 %
   :alt: pupmotors
   :align: center

   Moteurs Powered Up sans capteurs de rotation. Les flèches indiquent la
   direction positive par défaut.

.. blockimg:: pybricks_variables_set_dc_motor

.. autoclass:: pybricks.pupdevices.DCMotor
    :no-members:

    .. blockimg:: pybricks_blockMotorDuty_DCMotor

    .. automethod:: pybricks.pupdevices.DCMotor.dc
        :noindex:

    .. blockimg:: pybricks_blockMotorStop_DCMotor_coast

    .. automethod:: pybricks.pupdevices.DCMotor.stop
        :noindex:

    .. blockimg:: pybricks_blockMotorStop_DCMotor_brake

    .. automethod:: pybricks.pupdevices.DCMotor.brake
        :noindex:

    .. automethod:: pybricks.pupdevices.DCMotor.settings
        :noindex:

Exemples
--------

Faire rouler un train indéfiniment
**********************************

.. literalinclude::
    ../../../examples/pup/motor_dc/motor_dc_battery_box.py

Faire bouger le moteur d'avant en arrière
*****************************************

.. literalinclude::
    ../../../examples/pup/motor_dc/motor_dc_init_basic.py

Changer la direction positive
*****************************

.. literalinclude::
    ../../../examples/pup/motor_dc/motor_dc_init_direction.py

Démarrer et arrêter
*******************

.. literalinclude::
    ../../../examples/pup/motor_dc/motor_dc_stop.py
