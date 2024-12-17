.. pybricks-requirements:: primehub

Prime Hub / Inventor Hub
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../main/cad/output/hub-spike-inventor.png
    :width: 80%

.. blockimg:: pybricks_variables_set_inventor_hub_option0

.. blockimg:: pybricks_variables_set_inventor_hub_option4
    :stack:

.. class:: InventorHub

    Cette classe est identique à la classe ``PrimeHub``, montrée ci-dessous.
    Les deux classes fonctionnent sur les deux hubs.

    Ces hubs sont complètement identiques. Ils utilisent le même firmware
    Pybricks.

.. blockimg:: pybricks_variables_set_prime_hub_option0

.. blockimg:: pybricks_variables_set_prime_hub_option4
    :stack:

.. autoclass:: pybricks.hubs.PrimeHub
    :no-members:

    .. rubric:: Utilisation de la lumière d'état du hub

    .. figure:: ../../main/diagrams/primehub_light.png
        :width: 22 em

    .. blockimg:: pybricks_blockLightOnColor_primehub_on

    .. automethod:: pybricks.hubs::PrimeHub.light.on

    .. blockimg:: pybricks_blockLightOnColor_primehub_off

    .. automethod:: pybricks.hubs::PrimeHub.light.off

    .. automethod:: pybricks.hubs::PrimeHub.light.blink

    .. automethod:: pybricks.hubs::PrimeHub.light.animate

    .. rubric:: Utilisation de l'affichage de la matrice lumineuse

    .. figure:: ../../main/diagrams/primehub_display.png
        :width: 22 em

    .. automethod:: pybricks.hubs::PrimeHub.display.orientation

    .. blockimg:: pybricks_blockLightMatrixDo_light_matrix_off

    .. automethod:: pybricks.hubs::PrimeHub.display.off

    .. blockimg:: pybricks_blockLightMatrixDo_light_matrix_pixel

    .. automethod:: pybricks.hubs::PrimeHub.display.pixel

    .. automethod:: pybricks.hubs::PrimeHub.display.icon

    .. automethod:: pybricks.hubs::PrimeHub.display.animate

    .. blockimg:: pybricks_blockLightMatrixDo_light_matrix_number

    .. automethod:: pybricks.hubs::PrimeHub.display.number

    .. blockimg:: pybricks_blockLightMatrixDo_light_matrix_symbol

    .. automethod:: pybricks.hubs::PrimeHub.display.char

    .. automethod:: pybricks.hubs::PrimeHub.display.text

    .. rubric:: Utilisation des boutons

    .. figure:: ../../main/diagrams/primehub_buttons.png
        :width: 22 em

    .. blockimg:: pybricks_blockButtonIsPressed_PrimeHub

    .. automethod:: pybricks.hubs::PrimeHub.buttons.pressed

    .. blockimg:: pybricks_blockHubStopButton_PrimeHub

    .. blockimg:: pybricks_blockHubStopButton_PrimeHub_none
        :stack:

    .. automethod:: pybricks.hubs::PrimeHub.system.set_stop_button

    .. rubric:: Utilisation de l'IMU

    .. blockimg:: pybricks_blockImuStatus_PrimeHub_ready

    .. automethod:: pybricks.hubs::PrimeHub.imu.ready

    .. blockimg:: pybricks_blockImuStatus_PrimeHub_stationary

    .. automethod:: pybricks.hubs::PrimeHub.imu.stationary

    .. blockimg:: pybricks_blockImuUp_PrimeHub

    .. automethod:: pybricks.hubs::PrimeHub.imu.up

    .. blockimg:: pybricks_blockTilt_PrimeHub_imu.tilt.pitch

    .. blockimg:: pybricks_blockTilt_PrimeHub_imu.tilt.roll
        :stack:

    .. automethod:: pybricks.hubs::PrimeHub.imu.tilt

    .. blockimg:: pybricks_blockImuAcceleration_PrimeHub

    .. automethod:: pybricks.hubs::PrimeHub.imu.acceleration

    .. blockimg:: pybricks_blockImuRotation_PrimeHub_imu.angular_velocity

    .. automethod:: pybricks.hubs::PrimeHub.imu.angular_velocity

    .. blockimg:: pybricks_blockImuGetHeading_PrimeHub

    .. automethod:: pybricks.hubs::PrimeHub.imu.heading

    .. blockimg:: pybricks_blockImuResetHeading_PrimeHub

    .. automethod:: pybricks.hubs::PrimeHub.imu.reset_heading

    .. blockimg:: pybricks_blockImuRotation_PrimeHub_imu.rotation

    .. automethod:: pybricks.hubs::PrimeHub.imu.rotation

    .. automethod:: pybricks.hubs::PrimeHub.imu.orientation

    .. automethod:: pybricks.hubs::PrimeHub.imu.settings

    .. rubric:: Utilisation du haut-parleur

    .. automethod:: pybricks.hubs::PrimeHub.speaker.volume

    .. automethod:: pybricks.hubs::PrimeHub.speaker.beep

    .. automethod:: pybricks.hubs::PrimeHub.speaker.play_notes

    .. rubric:: Utilisation de la messagerie Bluetooth sans connexion

    .. blockimg:: pybricks_blockBleBroadcast_PrimeHub

    .. automethod:: pybricks.hubs::PrimeHub.ble.broadcast

    .. blockimg:: pybricks_blockBleObserve_PrimeHub

    .. automethod:: pybricks.hubs::PrimeHub.ble.observe

    .. automethod:: pybricks.hubs::PrimeHub.ble.signal_strength

    .. automethod:: pybricks.hubs::PrimeHub.ble.version

    .. rubric:: Utilisation de la batterie

    .. blockimg:: pybricks_blockBatteryMeasure_PrimeHub_battery.voltage

    .. automethod:: pybricks.hubs::PrimeHub.battery.voltage

    .. blockimg:: pybricks_blockBatteryMeasure_PrimeHub_battery.current

    .. automethod:: pybricks.hubs::PrimeHub.battery.current

    .. rubric:: Obtenir l'état du chargeur

    .. automethod:: pybricks.hubs::PrimeHub.charger.connected

    .. automethod:: pybricks.hubs::PrimeHub.charger.current

    .. automethod:: pybricks.hubs::PrimeHub.charger.status

    .. rubric:: Contrôle du système

    .. automethod:: pybricks.hubs::PrimeHub.system.name

    .. automethod:: pybricks.hubs::PrimeHub.system.storage

        Vous pouvez stocker jusqu'à 512 octets de données sur ce hub.

    .. blockimg:: pybricks_blockHubShutdown_PrimeHub

    .. automethod:: pybricks.hubs::PrimeHub.system.shutdown

    .. automethod:: pybricks.hubs::PrimeHub.system.reset_reason

.. note:: Les exemples ci-dessous utilisent la classe ``PrimeHub``. Les exemples fonctionnent bien
        sur les deux hubs car ils sont identiques. Si vous préférez, vous pouvez
        changer cela en ``InventorHub``.

Exemples de lumière d'état
--------------------------

Allumer et éteindre la lumière
******************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/light_off_primehub.py

Changer la luminosité et utiliser des couleurs personnalisées
*************************************************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/light_hsv_primehub.py

Faire clignoter la lumière
**************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/light_blink_primehub.py

Créer des animations lumineuses
*******************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/light_animate_primehub.py

Exemples d'affichage de matrice
-------------------------------

Afficher des images
*******************

.. literalinclude::
    ../../../examples/pup/hub_primehub/display_image.py

Afficher des nombres
********************

.. literalinclude::
    ../../../examples/pup/hub_primehub/display_number.py

Afficher du texte
*****************

.. literalinclude::
    ../../../examples/pup/hub_primehub/display_text.py

Afficher des pixels individuels
*******************************

.. literalinclude::
    ../../../examples/pup/hub_primehub/display_pixel.py

Changer l'orientation de l'affichage
************************************

.. literalinclude::
    ../../../examples/pup/hub_primehub/display_orientation.py

.. literalinclude::
    ../../../examples/pup/hub_primehub/display_orientation_imu.py

.. _make_icons:

Créer vos propres images
************************

.. literalinclude::
    ../../../examples/pup/hub_primehub/display_matrix.py

Combiner des icônes pour créer des expressions
**********************************************

.. literalinclude::
    ../../../examples/pup/hub_primehub/display_expression.py

Afficher des animations
***********************

.. literalinclude::
    ../../../examples/pup/hub_primehub/display_animate.py

Exemples de bouton
------------------

Détecter les pressions sur les boutons
**************************************

.. literalinclude::
    ../../../examples/pup/hub_primehub/button_main.py

Exemples d'IMU
--------------

Tester quelle direction est vers le haut
****************************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/imu_up_primehub.py

Lire la valeur de l'inclinaison
*******************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/imu_tilt_primehub.py

Utiliser une orientation personnalisée du hub
*********************************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/imu_tilt_blast_primehub.py

Lire les vecteurs d'accélération et de vitesse angulaire
********************************************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/imu_read_vector_primehub.py

Lire l'accélération et la vitesse angulaire sur un axe
******************************************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/imu_read_scalar_primehub.py

Exemples Bluetooth
------------------

Diffuser des données vers d'autres hubs
***************************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/ble_broadcast_primehub.py

Observer les données d'autres hubs
**********************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/ble_observe_primehub.py

Exemples de système
-------------------

Changer la combinaison de boutons d'arrêt
*****************************************

.. literalinclude::
    ../../../examples/pup/hub_primehub/button_stop.py

Éteindre le hub
***************

.. literalinclude::
    ../../../examples/pup/hub_common/build/system_shutdown_primehub.py

