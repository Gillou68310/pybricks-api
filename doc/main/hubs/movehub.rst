.. pybricks-requirements:: movehub

Move Hub
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. _fig_movehub:

.. figure:: ../../main/diagrams/movehub.png
    :width: 100%

.. blockimg:: pybricks_variables_set_move_hub_option0

.. blockimg:: pybricks_variables_set_move_hub_option4
    :stack:

.. autoclass:: pybricks.hubs.MoveHub
    :no-members:

    .. rubric:: Utilisation de la lumière d'état du hub

    .. blockimg:: pybricks_blockLightOnColor_movehub_on

    .. automethod:: pybricks.hubs::MoveHub.light.on

    .. blockimg:: pybricks_blockLightOnColor_movehub_off

    .. automethod:: pybricks.hubs::MoveHub.light.off

    .. automethod:: pybricks.hubs::MoveHub.light.blink

    .. automethod:: pybricks.hubs::MoveHub.light.animate

    .. rubric:: Utilisation de l'IMU

    .. blockimg:: pybricks_blockImuUp_MoveHub

    .. automethod:: pybricks.hubs::MoveHub.imu.up

    .. blockimg:: pybricks_blockTilt_MoveHub_imu.tilt.pitch

    .. blockimg:: pybricks_blockTilt_MoveHub_imu.tilt.roll
        :stack:

    .. automethod:: pybricks.hubs::MoveHub.imu.tilt

    .. blockimg:: pybricks_blockImuAcceleration_MoveHub

    .. automethod:: pybricks.hubs::MoveHub.imu.acceleration

        .. versionchanged:: 3.2

            Changement des unités d'accélération de m/s² à mm/s².

    .. rubric:: Utilisation de la messagerie Bluetooth sans connexion

    .. blockimg:: pybricks_blockBleBroadcast_PrimeHub

    .. automethod:: pybricks.hubs::PrimeHub.ble.broadcast

    .. blockimg:: pybricks_blockBleObserve_PrimeHub

    .. automethod:: pybricks.hubs::PrimeHub.ble.observe

    .. automethod:: pybricks.hubs::MoveHub.ble.signal_strength

    .. automethod:: pybricks.hubs::MoveHub.ble.version

    .. rubric:: Utilisation de la batterie

    .. blockimg:: pybricks_blockBatteryMeasure_MoveHub_battery.voltage

    .. automethod:: pybricks.hubs::MoveHub.battery.voltage

    .. blockimg:: pybricks_blockBatteryMeasure_MoveHub_battery.current

    .. automethod:: pybricks.hubs::MoveHub.battery.current

    .. rubric:: Bouton et contrôle du système

    .. blockimg:: pybricks_blockButtonIsPressed_PrimeHub

    .. automethod:: pybricks.hubs::MoveHub.buttons.pressed

    .. blockimg:: pybricks_blockHubStopButton_MoveHub

    .. blockimg:: pybricks_blockHubStopButton_MoveHub_none
        :stack:

    .. automethod:: pybricks.hubs::MoveHub.system.set_stop_button

    .. automethod:: pybricks.hubs::MoveHub.system.name

    .. automethod:: pybricks.hubs::MoveHub.system.storage

        Vous pouvez stocker jusqu'à 128 octets de données sur ce hub. Les
        données sont effacées lorsque vous mettez à jour le firmware Pybricks
        ou si vous restaurez le firmware d'origine.

    .. blockimg:: pybricks_blockHubShutdown_MoveHub

    .. automethod:: pybricks.hubs::MoveHub.system.shutdown

    .. automethod:: pybricks.hubs::MoveHub.system.reset_reason

Exemples de lumière d'état
--------------------------

Allumer et éteindre la lumière
******************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/light_off_movehub.py

Faire clignoter la lumière
**************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/light_blink_movehub.py

Exemples d'IMU
---------------

Tester quelle direction est vers le haut
****************************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/imu_up_movehub.py

Lire l'accélération
*******************

.. literalinclude::
    ../../../examples/pup/hub_movehub/imu_read_acceleration.py


Exemples de Bluetooth
---------------------

Diffuser des données vers d'autres hubs
***************************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/ble_broadcast_movehub.py

Observer les données d'autres hubs
**********************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/ble_observe_movehub.py


Exemples de bouton et de système
--------------------------------

Utiliser le bouton d'arrêt pendant votre programme
**************************************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/button_single_movehub.py

Éteindre le hub
***************

.. literalinclude::
    ../../../examples/pup/hub_common/build/system_shutdown_movehub.py

Générer des nombres aléatoires
******************************

Le Move Hub n'inclut pas le module :mod:`urandom`. Si vous avez besoin de
nombres aléatoires dans votre application, vous pouvez essayer une variation
de l'exemple suivant.

Pour que cela fonctionne mieux, changez la valeur initiale de ``_rand`` en
quelque chose qui est vraiment aléatoire dans votre application. Vous pourriez
utiliser l'accélération de l'IMU ou une valeur de capteur, par exemple.

.. literalinclude::
    ../../../examples/pup/hub_movehub/randint_implementation.py
