:mod:`ev3devices <pybricks.ev3devices>` -- Dispositifs EV3
==========================================================

.. automodule:: pybricks.ev3devices
    :no-members:

Moteurs
^^^^^^^^^^^^

.. _fig_ev3motors:

.. figure:: ../main/diagrams/ev3motors.png
   :width: 100 %

   Moteurs compatibles EV3. Les flèches indiquent la direction positive par
   défaut.

.. autoclass:: pybricks.ev3devices.Motor
    :noindex:
    :no-members:

    .. rubric:: Mesure

    .. automethod:: pybricks.ev3devices.Motor.angle

    .. automethod:: pybricks.ev3devices.Motor.reset_angle

    .. automethod:: pybricks.ev3devices.Motor.speed

    .. automethod:: pybricks.ev3devices.Motor.load

    .. automethod:: pybricks.ev3devices.Motor.stalled

    .. rubric:: Arrêt

    .. automethod:: pybricks.ev3devices.Motor.stop

    .. automethod:: pybricks.ev3devices.Motor.brake

    .. automethod:: pybricks.ev3devices.Motor.hold

    .. rubric:: Fonctionnement continu

    .. automethod:: pybricks.ev3devices.Motor.run

    .. automethod:: pybricks.ev3devices.Motor.dc

    .. rubric:: Fonctionnement par une quantité fixe

    .. automethod:: pybricks.ev3devices.Motor.run_time

    .. automethod:: pybricks.ev3devices.Motor.run_angle

    .. automethod:: pybricks.ev3devices.Motor.run_target

    .. automethod:: pybricks.ev3devices.Motor.track_target

    .. automethod:: pybricks.ev3devices.Motor.run_until_stalled

    .. automethod:: pybricks.ev3devices.Motor.done

    .. rubric:: Paramètres du moteur

    .. automethod:: pybricks.ev3devices.Motor.settings

    .. rubric:: Paramètres de contrôle

    .. automethod:: pybricks.ev3devices.Motor.control.limits

    .. automethod:: pybricks.ev3devices.Motor.control.pid

    .. automethod:: pybricks.ev3devices.Motor.control.target_tolerances

    .. automethod:: pybricks.ev3devices.Motor.control.stall_tolerances

    .. attribute:: control.scale

        Nombre de degrés que le moteur tourne pour compléter un degré à la
        sortie du train d'engrenages. Il s'agit du rapport de réduction
        déterminé à partir de l'argument ``gears`` lors de l'initialisation du
        moteur.

Capteur tactile
^^^^^^^^^^^^^^^

.. figure:: ../main/cad/output/ev3device-touch.png
   :width: 18 %

.. autoclass:: pybricks.ev3devices.TouchSensor

Capteur de couleur
^^^^^^^^^^^^^^^^^^

.. figure:: ../main/cad/output/ev3device-color.png
   :width: 18 %

.. autoclass:: pybricks.ev3devices.ColorSensor

Capteur infrarouge et balise
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Chaque méthode de cette classe met le capteur dans un mode différent. Le
changement de mode prend environ une seconde sur ce capteur. Pour vous assurer
que votre programme s'exécute rapidement, utilisez uniquement l'une de ces
méthodes dans votre programme.

.. figure:: ../main/cad/output/ev3device-infrared.png
   :width: 60 %

.. autoclass:: pybricks.ev3devices.InfraredSensor

Capteur ultrasonique
^^^^^^^^^^^^^^^^^^^^

.. figure:: ../main/cad/output/ev3device-ultrasonic.png
   :width: 22 %

.. autoclass:: pybricks.ev3devices.UltrasonicSensor

Capteur gyroscopique
^^^^^^^^^^^^^^^^^^^^

.. figure:: ../main/cad/output/ev3device-gyro.png
   :width: 18 %

.. autoclass:: pybricks.ev3devices.GyroSensor
    :no-members:

    .. automethod:: pybricks.ev3devices.GyroSensor.speed

    .. automethod:: pybricks.ev3devices.GyroSensor.angle

         Si vous utilisez la méthode :meth:`.angle`, vous ne pouvez pas
         utiliser la méthode :meth:`.speed` dans le même programme. Cela
         réinitialiserait l'angle du capteur à zéro chaque fois que vous lisez
         la vitesse.

    .. automethod:: pybricks.ev3devices.GyroSensor.reset_angle
