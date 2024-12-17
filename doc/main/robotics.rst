:mod:`robotics <pybricks.robotics>` -- Robotique et bases de conduite
=====================================================================

.. automodule:: pybricks.robotics
    :no-members:

.. pybricks-requirements::

.. blockimg:: pybricks_variables_set_drive_base

.. autoclass:: pybricks.robotics.DriveBase
    :no-members:

    .. rubric:: Conduire sur une distance ou un angle donné

    Utilisez les commandes suivantes pour conduire sur une distance donnée ou
    tourner d'un angle donné.

    Cela est mesuré à l'aide des capteurs de rotation internes. Parce que les
    roues peuvent glisser en mouvement, la distance parcourue et l'angle ne
    sont que des estimations.

    .. blockimg:: pybricks_blockDriveBaseDrive_drivebase_drive_straight

    .. automethod:: pybricks.robotics.DriveBase.straight

    .. blockimg:: pybricks_blockDriveBaseDrive_drivebase_drive_turn

    .. automethod:: pybricks.robotics.DriveBase.turn

    .. blockimg:: pybricks_blockDriveBaseDrive_drivebase_drive_curve

    .. automethod:: pybricks.robotics.DriveBase.curve

    .. blockimg:: pybricks_blockDriveBaseConfigure_drivebase_straight_speed

    .. blockimg:: pybricks_blockDriveBaseConfigure_drivebase_straight_acceleration

    .. blockimg:: pybricks_blockDriveBaseConfigure_drivebase_turn_rate

    .. blockimg:: pybricks_blockDriveBaseConfigure_drivebase_turn_acceleration

    .. automethod:: pybricks.robotics.DriveBase.settings

    .. automethod:: pybricks.robotics.DriveBase.done

    .. rubric:: Conduire indéfiniment

    Utilisez :meth:`.drive` pour commencer à conduire à une vitesse et une
    direction souhaitées.

    Il continue jusqu'à ce que vous utilisiez :meth:`.stop` ou changiez de
    direction en utilisant à nouveau :meth:`.drive`. Par exemple, vous pouvez
    conduire jusqu'à ce qu'un capteur soit déclenché, puis vous arrêter ou
    faire demi-tour.

    .. blockimg:: pybricks_blockDriveBaseDrive_drivebase_drive_forever

    .. automethod:: pybricks.robotics.DriveBase.drive

    .. blockimg:: pybricks_blockDriveBaseStop_coast

    .. automethod:: pybricks.robotics.DriveBase.stop

    .. blockimg:: pybricks_blockDriveBaseStop_brake

    .. automethod:: pybricks.robotics.DriveBase.brake

    .. blockimg:: pybricks_blockDriveBaseStop_hold

    .. rubric:: Mesurer

    .. blockimg:: pybricks_blockDriveBaseMeasure_drivebase_get_distance

    .. automethod:: pybricks.robotics.DriveBase.distance

    .. blockimg:: pybricks_blockDriveBaseMeasure_drivebase_get_angle

    .. automethod:: pybricks.robotics.DriveBase.angle

    .. blockimg:: pybricks_blockDriveBaseMeasure_drivebase_get_speed

    .. blockimg:: pybricks_blockDriveBaseMeasure_drivebase_get_turn_rate

    .. automethod:: pybricks.robotics.DriveBase.state

    .. automethod:: pybricks.robotics.DriveBase.reset

    .. automethod:: pybricks.robotics.DriveBase.stalled

    .. pybricks-requirements:: gyro

    .. rubric:: Conduire avec le gyroscope

    .. blockimg:: pybricks_blockDriveBaseUseGyro

    .. automethod:: pybricks.robotics.DriveBase.use_gyro

    Si votre hub n'est pas monté à plat dans votre robot, assurez-vous de
    spécifier les paramètres ``top_side`` et ``front_side`` lorsque vous
    initialisez le :class:`PrimeHub() <pybricks.hubs.PrimeHub>`,
    :class:`InventorHub() <pybricks.hubs.PrimeHub>`,
    :class:`EssentialHub() <pybricks.hubs.EssentialHub>`, ou
    :class:`TechnicHub() <pybricks.hubs.TechnicHub>`. De cette façon, votre
    robot sait quelle rotation mesurer lors des virages.

    Le gyroscope dans chaque hub est un peu différent, ce qui peut entraîner
    une erreur de quelques degrés pour les grands virages, ou de nombreux
    petits virages dans la même direction. Par exemple, vous devrez peut-être
    utiliser :meth:`turn(357) <pybricks.robotics.DriveBase.turn>` ou
    :meth:`turn(362) <pybricks.robotics.DriveBase.turn>` sur votre robot pour
    effectuer un tour complet.

    Par défaut, cette classe essaie de maintenir la position du robot après un
    mouvement. Cela signifie que les roues tourneront si vous soulevez le
    robot, dans le but de maintenir son angle de cap. Pour éviter cela, vous
    pouvez choisir ``then=Stop.COAST`` dans votre dernière commande
    :meth:`straight <pybricks.robotics.DriveBase.straight>`,
    :meth:`turn <pybricks.robotics.DriveBase.turn>`, ou
    :meth:`curve <pybricks.robotics.DriveBase.curve>`.

    .. _measuring:

    .. rubric:: Mesurer et valider les dimensions du robot

    Comme première estimation, vous pouvez mesurer le ``wheel_diameter`` et le
    ``axle_track`` avec une règle. Parce qu'il est difficile de voir où les
    roues touchent effectivement le sol, vous pouvez estimer le ``axle_track``
    comme la distance entre le milieu des roues.

    Si vous n'avez pas de règle, vous pouvez utiliser une poutre LEGO pour
    mesurer. La distance centre à centre des trous est de 8 mm. Pour certains
    pneus, le diamètre est imprimé sur le côté. Par exemple, 62.4 x 20
    signifie que le diamètre est de 62.4 mm et que la largeur est de 20 mm.

    En pratique, la plupart des roues se compressent légèrement sous le poids
    de votre robot. Pour vérifier, faites parcourir 1000 mm à votre robot en
    utilisant ``my_robot.straight(1000)`` et mesurez la distance réellement
    parcourue. Compensez comme suit :

        - Si votre robot ne parcourt **pas assez loin**, **diminuez**
          légèrement la valeur de ``wheel_diameter``.
        - Si votre robot parcourt **trop loin**, **augmentez** légèrement la
          valeur de ``wheel_diameter``.

    Les arbres de moteur et les essieux se plient légèrement sous la charge du
    robot, ce qui rapproche le point de contact des roues du milieu de votre
    robot. Pour vérifier, faites tourner votre robot de 360 degrés en
    utilisant ``my_robot.turn(360)`` et vérifiez qu'il est revenu au même
    endroit :

        - Si votre robot ne tourne **pas assez**, **augmentez** légèrement la
          valeur de ``axle_track``.
        - Si votre robot tourne **trop**, **diminuez** légèrement la valeur de
          ``axle_track``.

    Lors de ces ajustements, ajustez toujours d'abord le ``wheel_diameter``,
    comme indiqué ci-dessus. Assurez-vous de tester à la fois les virages et
    la conduite en ligne droite après avoir terminé.

    .. rubric:: Utiliser les moteurs de la DriveBase individuellement

    Après avoir créé un objet :class:`.DriveBase`, vous pouvez toujours
    utiliser ses deux moteurs individuellement. Si vous démarrez un moteur,
    l'autre moteur s'arrêtera automatiquement. De même, si un moteur est déjà
    en marche et que vous faites bouger la base de conduite, la manœuvre
    d'origine est annulée et la base de conduite prendra le relais.

    .. rubric:: Paramètres avancés

    La méthode :meth:`.settings` est utilisée pour ajuster les paramètres
    couramment utilisés comme la vitesse et l'accélération par défaut pour les
    manœuvres en ligne droite et les virages. Utilisez les attributs suivants
    pour ajuster des paramètres de contrôle plus avancés.

    .. autoattribute:: pybricks.robotics.DriveBase.distance_control
        :annotation:

    .. autoattribute:: pybricks.robotics.DriveBase.heading_control
        :annotation:

    .. versionchanged:: 3.2

        Les méthodes :meth:`done` et :meth:`stalled` ont été déplacées.

.. pybricks-requirements::

.. blockimg:: pybricks_variables_set_car

.. versionadded:: 3.4

.. autoclass:: pybricks.robotics.Car
    :no-members:

    .. blockimg:: pybricks_blockCarSteer

    .. automethod:: pybricks.robotics.Car.steer

    .. blockimg:: pybricks_blockCarDrive_car_drive_at_power

    .. automethod:: pybricks.robotics.Car.drive_power

    .. blockimg:: pybricks_blockCarDrive_car_drive_at_speed

    .. automethod:: pybricks.robotics.Car.drive_speed

Exemples
-------------------

Conduire en ligne droite et tourner sur place avec une base de conduite
***********************************************************************

Ce programme montre les bases de la conduite et du virage.

.. literalinclude::
    ../../examples/pup/robotics/drivebase_basics.py

Contrôler à distance une voiture avec direction des roues avant
***************************************************************

Ce programme montre comment vous pouvez conduire une voiture avec direction
des roues avant en utilisant la :class:`télécommande <pybricks.pupdevices.Remote>`.

Dans ce programme, les ports correspondent à ceux du `LEGO Technic 42099
Off-Roader <https://pybricks.com/projects/sets/technic/42099-off-roader/>`_,
mais vous pouvez utiliser n'importe quelle autre voiture avec direction des
roues avant. Si votre véhicule n'a qu'un seul moteur de traction, vous pouvez
utiliser un seul moteur au lieu d'un ensemble de moteurs comme ci-dessous.

.. literalinclude::
    ../../examples/pup/robotics/car_remote.py
