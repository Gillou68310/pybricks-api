.. pybricks-requirements::

Moteurs avec capteurs de rotation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _fig_pupmotors:

.. figure:: ../../main/diagrams/pupmotors.png
   :width: 100 %
   :alt: pupmotors

   Moteurs Powered Up avec capteurs de rotation. Les flèches indiquent la
   direction positive par défaut. Voir le module :mod:`hubs <pybricks.hubs>`
   pour les directions par défaut des moteurs intégrés.

.. blockimg:: pybricks_variables_set_motor

.. autoclass:: pybricks.pupdevices.Motor
    :no-members:

    .. rubric:: Mesurer

    .. blockimg:: pybricks_blockMotorMeasure_motor_angle

    .. automethod:: pybricks.pupdevices.Motor.angle

    .. blockimg:: pybricks_blockMotorResetAngle

    .. automethod:: pybricks.pupdevices.Motor.reset_angle

    .. blockimg:: pybricks_blockMotorMeasure_motor_speed

    .. blockimg:: pybricks_blockMotorMeasure_motor_get_speed_average

    .. automethod:: pybricks.pupdevices.Motor.speed

    .. blockimg:: pybricks_blockMotorMeasure_motor_load

    .. automethod:: pybricks.pupdevices.Motor.load

    .. blockimg:: pybricks_blockMotorMeasure_motor_stalled

    .. automethod:: pybricks.pupdevices.Motor.stalled

    .. rubric:: Arrêter

    .. blockimg:: pybricks_blockMotorStop_Motor_coast

    .. automethod:: pybricks.pupdevices.Motor.stop

    .. blockimg:: pybricks_blockMotorStop_Motor_brake

    .. automethod:: pybricks.pupdevices.Motor.brake

    .. blockimg:: pybricks_blockMotorStop_Motor_hold

    .. automethod:: pybricks.pupdevices.Motor.hold

    .. rubric:: Fonctionnement continu

    .. blockimg:: pybricks_blockMotorRun_run

    .. automethod:: pybricks.pupdevices.Motor.run

    .. blockimg:: pybricks_blockMotorDuty_Motor

    .. automethod:: pybricks.pupdevices.Motor.dc

    .. rubric:: Fonctionnement par une quantité fixe

    .. automethod:: pybricks.pupdevices.Motor.run_time

    .. blockimg:: pybricks_blockMotorRun_run_angle

    .. automethod:: pybricks.pupdevices.Motor.run_angle

    .. blockimg:: pybricks_blockMotorRun_run_target

    .. automethod:: pybricks.pupdevices.Motor.run_target

    .. blockimg:: pybricks_blockMotorRun_run_until_stalled

    .. automethod:: pybricks.pupdevices.Motor.run_until_stalled

    .. blockimg:: pybricks_blockMotorTrack

    .. automethod:: pybricks.pupdevices.Motor.track_target

    .. automethod:: pybricks.pupdevices.Motor.done

    .. _settings:

    .. rubric:: Paramètres du moteur

    .. blockimg:: pybricks_blockMotorConfigure_motor_max_voltage

    .. automethod:: pybricks.pupdevices.Motor.settings

    .. automethod:: pybricks.pupdevices.Motor.close

    .. rubric:: Paramètres de contrôle

    .. pybricks-requirements:: pybricks-common-control

    .. blockimg:: pybricks_blockMotorConfigure_motor_max_speed

    .. blockimg:: pybricks_blockMotorConfigure_motor_acceleration
        :stack:

    .. blockimg:: pybricks_blockMotorConfigure_motor_max_torque
        :stack:

    .. automethod:: pybricks.pupdevices.Motor.control.limits

    .. pybricks-requirements:: pybricks-common-control

    .. automethod:: pybricks.pupdevices.Motor.control.pid

    .. pybricks-requirements:: pybricks-common-control

    .. blockimg:: pybricks_blockMotorConfigure_motor_target_tolerances

    .. automethod:: pybricks.pupdevices.Motor.control.target_tolerances

    .. pybricks-requirements:: pybricks-common-control

    .. automethod:: pybricks.pupdevices.Motor.control.stall_tolerances

    .. pybricks-requirements:: pybricks-common-control

    .. attribute:: control.scale

        Nombre de degrés que le moteur tourne pour compléter un degré à la
        sortie de la transmission. Il s'agit du rapport de réduction déterminé
        à partir de l'argument ``gears`` lors de l'initialisation du moteur.

    .. versionchanged:: 3.2

        Les méthodes :meth:`done`, :meth:`stalled` et :meth:`load` ont été
        déplacées.

    .. pybricks-requirements:: pybricks-common-control

    .. automethod:: pybricks.pupdevices.Motor.model.state

    .. pybricks-requirements:: pybricks-common-control

    .. automethod:: pybricks.pupdevices.Motor.model.settings

Exemples d'initialisation
-------------------------

Faire bouger le moteur d'avant en arrière
*****************************************

.. literalinclude::
    ../../../examples/pup/motor/motor_init_basic.py

Initialiser plusieurs moteurs
*****************************

.. literalinclude::
    ../../../examples/pup/motor/motor_init_multiple.py

Définir la direction positive comme antihoraire
***********************************************

.. literalinclude::
    ../../../examples/pup/motor/motor_init_direction.py

Utiliser des engrenages
***********************

.. literalinclude::
    ../../../examples/pup/motor/motor_init_gears.py

Exemples de mesure
------------------

Mesurer l'angle et la vitesse
*****************************

.. literalinclude::
    ../../../examples/pup/motor/motor_measure.py

Réinitialiser l'angle mesuré
****************************

.. literalinclude::
    ../../../examples/pup/motor/motor_reset_angle.py

Obtenir l'angle absolu
**********************

.. literalinclude::
    ../../../examples/pup/motor/motor_absolute.py


Exemples de mouvement
---------------------

Utilisation de base de toutes les méthodes de course
****************************************************

.. literalinclude::
    ../../../examples/pup/motor/motor_action_basic.py

Arrêter les mouvements en cours de différentes manières
*******************************************************

.. literalinclude::
    ../../../examples/pup/motor/motor_stop.py

Utiliser l'argument ``then`` pour changer la façon dont une commande de course s'arrête
***************************************************************************************

.. literalinclude::
    ../../../examples/pup/motor/motor_action_then.py

Exemples de blocage
-------------------

Faire fonctionner un moteur jusqu'à un point de terminaison mécanique
*********************************************************************

.. literalinclude::
    ../../../examples/pup/motor/motor_until_stalled.py

Centrer un mécanisme de direction
*********************************

.. literalinclude::
    ../../../examples/pup/motor/motor_until_stalled_center.py


Exemples de mouvement parallèle
-------------------------------

Utiliser l'argument ``wait`` pour faire fonctionner les moteurs en parallèle
****************************************************************************

.. literalinclude::
    ../../../examples/pup/motor/motor_action_wait.py

Attendre que deux actions parallèles se terminent
*************************************************

.. literalinclude::
    ../../../examples/pup/motor/motor_action_wait_advanced.py
