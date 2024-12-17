.. pybricks-requirements:: essentialhub

Essential Hub
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../main/cad/output/hub-essential.png
    :width: 30%

.. blockimg:: pybricks_variables_set_essential_hub_option0

.. blockimg:: pybricks_variables_set_essential_hub_option4
    :stack:

.. autoclass:: pybricks.hubs.EssentialHub
    :no-members:

    .. rubric:: Utilisation de la lumière d'état du hub

    .. blockimg:: pybricks_blockLightOnColor_essentialhub_on

    .. automethod:: pybricks.hubs::EssentialHub.light.on

    .. blockimg:: pybricks_blockLightOnColor_essentialhub_off

    .. automethod:: pybricks.hubs::EssentialHub.light.off

    .. automethod:: pybricks.hubs::EssentialHub.light.blink

    .. automethod:: pybricks.hubs::EssentialHub.light.animate

    .. rubric:: Utilisation du bouton

    .. blockimg:: pybricks_blockButtonIsPressed_EssentialHub

    .. automethod:: pybricks.hubs::EssentialHub.buttons.pressed

    .. blockimg:: pybricks_blockHubStopButton_EssentialHub

    .. blockimg:: pybricks_blockHubStopButton_EssentialHub_none
        :stack:

    .. automethod:: pybricks.hubs::EssentialHub.system.set_stop_button

    .. rubric:: Utilisation de l'IMU

    .. blockimg:: pybricks_blockImuStatus_EssentialHub_ready

    .. automethod:: pybricks.hubs::EssentialHub.imu.ready

    .. blockimg:: pybricks_blockImuStatus_EssentialHub_stationary

    .. automethod:: pybricks.hubs::EssentialHub.imu.stationary

    .. blockimg:: pybricks_blockImuUp_EssentialHub

    .. automethod:: pybricks.hubs::EssentialHub.imu.up

    .. blockimg:: pybricks_blockTilt_EssentialHub_imu.tilt.pitch

    .. blockimg:: pybricks_blockTilt_EssentialHub_imu.tilt.roll
        :stack:

    .. automethod:: pybricks.hubs::EssentialHub.imu.tilt

    .. blockimg:: pybricks_blockImuAcceleration_EssentialHub

    .. automethod:: pybricks.hubs::EssentialHub.imu.acceleration

    .. blockimg:: pybricks_blockImuRotation_EssentialHub_imu.angular_velocity

    .. automethod:: pybricks.hubs::EssentialHub.imu.angular_velocity

    .. blockimg:: pybricks_blockImuGetHeading_EssentialHub

    .. automethod:: pybricks.hubs::EssentialHub.imu.heading

    .. blockimg:: pybricks_blockImuResetHeading_EssentialHub

    .. automethod:: pybricks.hubs::EssentialHub.imu.reset_heading

    .. blockimg:: pybricks_blockImuRotation_EssentialHub_imu.rotation

    .. automethod:: pybricks.hubs::EssentialHub.imu.rotation

    .. automethod:: pybricks.hubs::EssentialHub.imu.orientation

    .. automethod:: pybricks.hubs::EssentialHub.imu.settings

    .. rubric:: Utilisation de la messagerie Bluetooth sans connexion

    .. blockimg:: pybricks_blockBleBroadcast_EssentialHub

    .. automethod:: pybricks.hubs::EssentialHub.ble.broadcast

    .. blockimg:: pybricks_blockBleObserve_EssentialHub

    .. automethod:: pybricks.hubs::EssentialHub.ble.observe

    .. automethod:: pybricks.hubs::EssentialHub.ble.signal_strength

    .. automethod:: pybricks.hubs::EssentialHub.ble.version

    .. rubric:: Utilisation de la batterie

    .. blockimg:: pybricks_blockBatteryMeasure_EssentialHub_battery.voltage

    .. automethod:: pybricks.hubs::EssentialHub.battery.voltage

    .. blockimg:: pybricks_blockBatteryMeasure_EssentialHub_battery.current

    .. automethod:: pybricks.hubs::EssentialHub.battery.current

    .. rubric:: Obtenir le statut du chargeur

    .. automethod:: pybricks.hubs::EssentialHub.charger.connected

    .. automethod:: pybricks.hubs::EssentialHub.charger.current

    .. automethod:: pybricks.hubs::EssentialHub.charger.status

    .. rubric:: Contrôle du système

    .. automethod:: pybricks.hubs::EssentialHub.system.name

    .. automethod:: pybricks.hubs::EssentialHub.system.storage

        Vous pouvez stocker jusqu'à 512 octets de données sur ce hub.

    .. blockimg:: pybricks_blockHubShutdown_EssentialHub

    .. automethod:: pybricks.hubs::EssentialHub.system.shutdown

    .. automethod:: pybricks.hubs::EssentialHub.system.reset_reason

Exemples de lumière d'état
--------------------------

Allumer et éteindre la lumière
******************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/light_off_essentialhub.py

Changer la luminosité et utiliser des couleurs personnalisées
*************************************************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/light_hsv_essentialhub.py

Faire clignoter la lumière
**************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/light_blink_essentialhub.py

Créer des animations lumineuses
*******************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/light_animate_essentialhub.py

Exemples d'IMU
---------------

Tester quelle direction est vers le haut
****************************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/imu_up_essentialhub.py

Lire la valeur de l'inclinaison
*******************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/imu_tilt_essentialhub.py

Utiliser une orientation personnalisée du hub
*********************************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/imu_tilt_blast_essentialhub.py

Lire les vecteurs d'accélération et de vitesse angulaire
********************************************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/imu_read_vector_essentialhub.py

Lire l'accélération et la vitesse angulaire sur un axe
******************************************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/imu_read_scalar_essentialhub.py

Exemples de Bluetooth
---------------------

Diffuser des données vers d'autres hubs
***************************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/ble_broadcast_essentialhub.py

Observer les données d'autres hubs
**********************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/ble_observe_essentialhub.py

Exemples de système
-------------------

Utiliser le bouton d'arrêt pendant votre programme
**************************************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/button_single_essentialhub.py

Éteindre le hub
***************

.. literalinclude::
    ../../../examples/pup/hub_common/build/system_shutdown_essentialhub.py
