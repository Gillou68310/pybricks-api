.. pybricks-requirements:: technichub

Technic Hub
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../main/cad/output/hub-technic.png
    :width: 40%

.. blockimg:: pybricks_variables_set_technic_hub_option0

.. blockimg:: pybricks_variables_set_technic_hub_option4
    :stack:

.. autoclass:: pybricks.hubs.TechnicHub
    :no-members:

    .. rubric:: Utilisation de la lumière d'état du hub

    .. blockimg:: pybricks_blockLightOnColor_technichub_on

    .. automethod:: pybricks.hubs::TechnicHub.light.on

    .. blockimg:: pybricks_blockLightOnColor_technichub_off

    .. automethod:: pybricks.hubs::TechnicHub.light.off

    .. automethod:: pybricks.hubs::TechnicHub.light.blink

    .. automethod:: pybricks.hubs::TechnicHub.light.animate

    .. rubric:: Utilisation de l'IMU

    .. blockimg:: pybricks_blockImuStatus_TechnicHub_ready

    .. automethod:: pybricks.hubs::TechnicHub.imu.ready

    .. blockimg:: pybricks_blockImuStatus_TechnicHub_stationary

    .. automethod:: pybricks.hubs::TechnicHub.imu.stationary

    .. blockimg:: pybricks_blockImuUp_TechnicHub

    .. automethod:: pybricks.hubs::TechnicHub.imu.up

    .. blockimg:: pybricks_blockTilt_TechnicHub_imu.tilt.pitch

    .. blockimg:: pybricks_blockTilt_TechnicHub_imu.tilt.roll
        :stack:

    .. automethod:: pybricks.hubs::TechnicHub.imu.tilt

    .. blockimg:: pybricks_blockImuAcceleration_TechnicHub

    .. automethod:: pybricks.hubs::TechnicHub.imu.acceleration

    .. blockimg:: pybricks_blockImuRotation_TechnicHub_imu.angular_velocity

    .. automethod:: pybricks.hubs::TechnicHub.imu.angular_velocity

    .. blockimg:: pybricks_blockImuGetHeading_TechnicHub

    .. automethod:: pybricks.hubs::TechnicHub.imu.heading

    .. blockimg:: pybricks_blockImuResetHeading_TechnicHub

    .. automethod:: pybricks.hubs::TechnicHub.imu.reset_heading

    .. blockimg:: pybricks_blockImuRotation_TechnicHub_imu.rotation

    .. automethod:: pybricks.hubs::TechnicHub.imu.rotation

    .. automethod:: pybricks.hubs::TechnicHub.imu.orientation

    .. automethod:: pybricks.hubs::TechnicHub.imu.settings

    .. rubric:: Utilisation de la messagerie Bluetooth sans connexion

    .. blockimg:: pybricks_blockBleBroadcast_TechnicHub

    .. automethod:: pybricks.hubs::TechnicHub.ble.broadcast

    .. blockimg:: pybricks_blockBleObserve_TechnicHub

    .. automethod:: pybricks.hubs::TechnicHub.ble.observe

    .. automethod:: pybricks.hubs::TechnicHub.ble.signal_strength

    .. automethod:: pybricks.hubs::TechnicHub.ble.version

    .. rubric:: Utilisation de la batterie

    .. blockimg:: pybricks_blockBatteryMeasure_TechnicHub_battery.voltage

    .. automethod:: pybricks.hubs::TechnicHub.battery.voltage

    .. blockimg:: pybricks_blockBatteryMeasure_TechnicHub_battery.current

    .. automethod:: pybricks.hubs::TechnicHub.battery.current

    .. rubric:: Bouton et contrôle du système

    .. blockimg:: pybricks_blockButtonIsPressed_TechnicHub

    .. automethod:: pybricks.hubs::TechnicHub.buttons.pressed

    .. blockimg:: pybricks_blockHubStopButton_TechnicHub

    .. blockimg:: pybricks_blockHubStopButton_TechnicHub_none
        :stack:

    .. automethod:: pybricks.hubs::TechnicHub.system.set_stop_button

    .. automethod:: pybricks.hubs::TechnicHub.system.name

    .. automethod:: pybricks.hubs::TechnicHub.system.storage

        Vous pouvez stocker jusqu'à 128 octets de données sur ce hub. Les
        données sont effacées lorsque vous mettez à jour le firmware Pybricks
        ou si vous restaurez le firmware d'origine.

    .. blockimg:: pybricks_blockHubShutdown_TechnicHub

    .. automethod:: pybricks.hubs::TechnicHub.system.shutdown

    .. automethod:: pybricks.hubs::TechnicHub.system.reset_reason

Exemples de lumière d'état
--------------------------

Allumer et éteindre la lumière
******************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/light_off_technichub.py

Changer la luminosité et utiliser des couleurs personnalisées
*************************************************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/light_hsv_technichub.py

Faire clignoter la lumière
**************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/light_blink_technichub.py

Créer des animations lumineuses
*******************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/light_animate_technichub.py

Exemples d'IMU
--------------

Tester quelle direction est vers le haut
****************************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/imu_up_technichub.py

Lire la valeur de l'inclinaison
*******************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/imu_tilt_technichub.py

Utiliser une orientation personnalisée du hub
*********************************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/imu_tilt_blast_technichub.py

Lire les vecteurs d'accélération et de vitesse angulaire
********************************************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/imu_read_vector_technichub.py

Lire l'accélération et la vitesse angulaire sur un axe
******************************************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/imu_read_scalar_technichub.py

Exemples Bluetooth
------------------

Diffuser des données vers d'autres hubs
***************************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/ble_broadcast_technichub.py

Observer les données d'autres hubs
**********************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/ble_observe_technichub.py

Exemples de bouton et de système
--------------------------------

Utiliser le bouton d'arrêt pendant votre programme
**************************************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/button_single_technichub.py

Éteindre le hub
***************

.. literalinclude::
    ../../../examples/pup/hub_common/build/system_shutdown_technichub.py
