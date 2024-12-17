.. pybricks-requirements::

Power Functions
^^^^^^^^^^^^^^^^^^^^^^^^^

La :class:`ColorDistanceSensor <pybricks.pupdevices.ColorDistanceSensor>` peut
envoyer des signaux infrarouges pour contrôler les récepteurs infrarouges
Power Functions. Vous pouvez utiliser cette technique pour contrôler les
moteurs moyens, grands, extra grands et de train. La portée infrarouge est
limitée à environ 30 cm, selon l'angle et les conditions ambiantes.

.. figure:: ../../main/cad/output/pupdevice-pfmotor.png
   :width: 95 %

   Powered Up
   :class:`ColorDistanceSensor <pybricks.pupdevices.ColorDistanceSensor>`
   (left), récepteur infrarouge Power Functions (middle), et un moteur Power
   Functions (right). Ici, le récepteur utilise le canal 1 avec un moteur sur le
   port rouge.

.. blockimg:: pybricks_variables_set_pf_motor

.. autoclass:: pybricks.pupdevices.PFMotor
    :noindex:
    :no-members:

    .. blockimg:: pybricks_blockMotorDuty_PFMotor

    .. automethod:: pybricks.pupdevices.PFMotor.dc
        :noindex:

    .. blockimg:: pybricks_blockMotorStop_PFMotor_coast

    .. automethod:: pybricks.pupdevices.PFMotor.stop
        :noindex:

    .. blockimg:: pybricks_blockMotorStop_PFMotor_brake

    .. automethod:: pybricks.pupdevices.PFMotor.brake
        :noindex:

Exemples
--------

Contrôler un moteur Power Functions
***********************************

.. literalinclude::
    ../../../examples/pup/motor_pf/motor_pf_basics.py

Contrôler plusieurs moteurs Power Functions
*******************************************

.. literalinclude::
    ../../../examples/pup/motor_pf/motor_pf_pwm.py
