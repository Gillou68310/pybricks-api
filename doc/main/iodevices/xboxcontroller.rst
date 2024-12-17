.. pybricks-requirements:: xbox-controller

Manette Xbox
^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../main/diagrams_source/xboxcontroller.png
   :width: 60 %

.. blockimg:: pybricks_variables_set_xbox_controller

.. autoclass:: pybricks.iodevices.XboxController
  :no-members:

  .. blockimg:: pybricks_blockButtonIsPressed_XboxController

  .. automethod:: pybricks.iodevices::XboxController.buttons.pressed

    Les boutons incluent :

      * ``Button.A``, ``Button.B``, ``Button.X``, ``Button.Y``.
      * ``Button.UP``, ``Button.DOWN``, ``Button.LEFT``, ``Button.RIGHT``
        (croix directionnelle). Au maximum deux de ces boutons peuvent être
        pressés en même temps.
      * ``Button.LB`` et ``Button.RB`` (pare-chocs).
      * ``Button.LJ`` et ``Button.RJ`` (appuyer sur les joysticks).
      * ``Button.VIEW``, ``Button.MENU``, ``Button.GUIDE`` (le logo Xbox), et
        ``Button.UPLOAD``.
      * ``Button.P1``, ``Button.P2``, ``Button.P3``, et ``Button.P4`` (Elite
        Series 2 uniquement). Appuyer sur les palettes peut également être
        détecté comme d'autres pressions de boutons, selon le profil
        actuellement actif.

  .. blockimg:: pybricks_blockJoystickValue_lj_x

  .. blockimg:: pybricks_blockJoystickValue_lj_y
      :stack:

  .. automethod:: pybricks.iodevices::XboxController.joystick_left

  .. blockimg:: pybricks_blockJoystickValue_rj_x

  .. blockimg:: pybricks_blockJoystickValue_rj_y
      :stack:

  .. automethod:: pybricks.iodevices::XboxController.joystick_right

  .. blockimg:: pybricks_blockJoystickValue_lt

  .. blockimg:: pybricks_blockJoystickValue_rt
      :stack:

  .. automethod:: pybricks.iodevices::XboxController.triggers

  .. blockimg:: pybricks_blockJoystickValue_dpad

  .. automethod:: pybricks.iodevices::XboxController.dpad

  .. blockimg:: pybricks_blockJoystickValue_profile

  .. automethod:: pybricks.iodevices::XboxController.profile

  .. blockimg:: pybricks_blockGamepadRumble_default

  .. blockimg:: pybricks_blockGamepadRumble_default_with_list
      :stack:

  .. blockimg:: pybricks_blockGamepadRumble_with_options
      :stack:

  .. automethod:: pybricks.iodevices::XboxController.rumble

.. _xbox-controller-pairing:

Instructions de jumelage de la manette Xbox
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
La première fois que vous utilisez une manette avec un hub, vous devrez les
jumeler : Allumez la manette, puis appuyez et maintenez le bouton de jumelage
à l'arrière de la manette pendant quelques secondes. Lorsque vous le relâchez,
le bouton Xbox commence à clignoter plus rapidement. Ensuite, démarrez votre
programme.

Lorsque le jumelage et la connexion sont réussis, le bouton Xbox cesse de
clignoter et reste allumé tant que le programme est en cours d'exécution.

Connexions répétées
===================

Si vous continuez à utiliser la même manette avec le même hub, vous pouvez
simplement allumer la manette la prochaine fois et le hub se connectera
automatiquement à elle lorsque votre programme avec cette classe sera exécuté.

La manette Xbox n'accepte cette connexion simplifiée qu'avec le dernier
appareil connecté. Donc, si vous vous connectez à nouveau à votre console Xbox
ou à un autre hub, vous devrez les jumeler à nouveau comme décrit ci-dessus.

Manettes compatibles
====================

Toutes les manettes Xbox sorties depuis 2016 sont compatibles. Cela inclut la
manette de la One S (``1708`` de 2016), l'Elite Series 2 (``1797`` de 2019),
et la Series X/S (``1914`` de 2020), qui est le dernier modèle à ce jour.

.. raw:: html

  <p>Voir aussi <a href="https://en.wikipedia.org/wiki/Xbox_Wireless_Controller#Summary" target="_blank">
  cet aperçu</a> des numéros de modèle incluant des images de
  chaque manette.</p>

Mise à jour de la manette Xbox
==============================

Si vous utilisez fréquemment la manette Xbox avec votre console, votre manette
est probablement déjà à jour. Si vous ne l'avez pas utilisée depuis un certain
temps ou si vous en avez acheté une récemment, vous devrez peut-être la mettre
à jour.

Pour mettre à jour la manette sans console, vous pouvez utiliser l'application
Accessoires Xbox sur un ordinateur Windows. Vous pouvez la télécharger depuis
le Microsoft Store. Connectez la manette via USB à l'ordinateur et suivez les
instructions dans l'application pour cliquer sur "Mettre à jour maintenant".

Limitations du Technic Hub
==========================

En raison des limitations du Technic Hub, le hub se déconnectera de
l'ordinateur lors de la recherche de la manette Xbox. Cela signifie que vous
ne pourrez pas voir la sortie de la commande ``print``. De plus, vous devrez
vous reconnecter à l'ordinateur si vous souhaitez modifier votre programme.
