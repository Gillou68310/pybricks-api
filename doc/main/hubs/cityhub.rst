.. pybricks-requirements:: cityhub

City Hub
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. figure:: ../../main/cad/output/hub-city.png
    :width: 30%

.. blockimg:: pybricks_variables_set_city_hub_option0

.. blockimg:: pybricks_variables_set_city_hub_option3
    :stack:

.. autoclass:: pybricks.hubs.CityHub
    :no-members:

    .. rubric:: Utilisation de la lumière d'état du hub

    .. blockimg:: pybricks_blockLightOnColor_cityhub_on

    .. automethod:: pybricks.hubs::CityHub.light.on

    .. blockimg:: pybricks_blockLightOnColor_cityhub_off

    .. automethod:: pybricks.hubs::CityHub.light.off

    .. automethod:: pybricks.hubs::CityHub.light.blink

    .. automethod:: pybricks.hubs::CityHub.light.animate

    .. rubric:: Utilisation de la messagerie Bluetooth sans connexion

    .. blockimg:: pybricks_blockBleBroadcast_CityHub

    .. automethod:: pybricks.hubs::CityHub.ble.broadcast

    .. blockimg:: pybricks_blockBleObserve_CityHub

    .. automethod:: pybricks.hubs::CityHub.ble.observe

    .. automethod:: pybricks.hubs::CityHub.ble.signal_strength

    .. automethod:: pybricks.hubs::CityHub.ble.version

    .. rubric:: Utilisation de la batterie

    .. blockimg:: pybricks_blockBatteryMeasure_CityHub_battery.voltage

    .. automethod:: pybricks.hubs::CityHub.battery.voltage

    .. blockimg:: pybricks_blockBatteryMeasure_CityHub_battery.current

    .. automethod:: pybricks.hubs::CityHub.battery.current

    .. rubric:: Bouton et contrôle du système

    .. blockimg:: pybricks_blockButtonIsPressed_CityHub

    .. automethod:: pybricks.hubs::CityHub.buttons.pressed

    .. blockimg:: pybricks_blockHubStopButton_CityHub

    .. blockimg:: pybricks_blockHubStopButton_CityHub_none
        :stack:

    .. automethod:: pybricks.hubs::CityHub.system.set_stop_button

    .. automethod:: pybricks.hubs::CityHub.system.name

    .. automethod:: pybricks.hubs::CityHub.system.storage

        Vous pouvez stocker jusqu'à 128 octets de données sur ce hub. Les
        données sont effacées lorsque vous mettez à jour le firmware Pybricks
        ou si vous restaurez le firmware d'origine.

    .. blockimg:: pybricks_blockHubShutdown_CityHub

    .. automethod:: pybricks.hubs::CityHub.system.shutdown

    .. automethod:: pybricks.hubs::CityHub.system.reset_reason

Exemples de lumière d'état
--------------------------

Allumer et éteindre la lumière
******************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/light_off_cityhub.py

Changer la luminosité et utiliser des couleurs personnalisées
*************************************************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/light_hsv_cityhub.py

Faire clignoter la lumière
**************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/light_blink_cityhub.py

Créer des animations lumineuses
*******************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/light_animate_cityhub.py


Exemples de Bluetooth
---------------------

Diffuser des données à d'autres hubs
************************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/ble_broadcast_cityhub.py

Observer les données d'autres hubs
**********************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/ble_observe_cityhub.py


Exemples de bouton et de système
--------------------------------

Utiliser le bouton d'arrêt pendant votre programme
**************************************************

.. literalinclude::
    ../../../examples/pup/hub_common/build/button_single_cityhub.py

Éteindre le hub
***************

.. literalinclude::
    ../../../examples/pup/hub_common/build/system_shutdown_cityhub.py
