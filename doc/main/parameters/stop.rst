.. pybricks-requirements::

Arrêt
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. class:: Stop

    Action après l'arrêt du moteur.

    .. autoattribute:: pybricks.parameters.Stop.COAST
        :annotation:

    .. autoattribute:: pybricks.parameters.Stop.COAST_SMART
        :annotation:

    .. autoattribute:: pybricks.parameters.Stop.BRAKE
        :annotation:

    .. autoattribute:: pybricks.parameters.Stop.HOLD
        :annotation:

    .. autoattribute:: pybricks.parameters.Stop.NONE
        :annotation:

    Le tableau suivant montre comment chacun des types d'arrêt de base ajoute
    un niveau supplémentaire de résistance au mouvement. Dans ces exemples,
    ``m`` est un :class:`Motor <pybricks.pupdevices.Motor>` et ``d`` est une
    :class:`DriveBase <pybricks.robotics.DriveBase>`. Les exemples
    montrent également comment courir à zéro vitesse se compare à ces types
    d'arrêt.

    +--------+------------+--------+-------------+---------------+-----------------------------------------+
    | | Type | | Friction | | Back | | Speed     |  | Angle kept | | Examples                              |
    |        |            | | EMF  | | kept at 0 |  | at target  |                                         |
    +========+============+========+=============+===============+=========================================+
    | Coast  | +          |        |             |               | | ``m.stop()``                          |
    |        |            |        |             |               | | ``m.run_target(500, 90, Stop.COAST)`` |
    +--------+------------+--------+-------------+---------------+-----------------------------------------+
    | Brake  | +          | +      |             |               | | ``m.brake()``                         |
    |        |            |        |             |               | | ``m.run_target(500, 90, Stop.BRAKE)`` |
    +--------+------------+--------+-------------+---------------+-----------------------------------------+
    |        | +          | +      | +           |               | | ``m.run(0)``                          |
    |        |            |        |             |               | | ``d.drive(0, 0)``                     |
    +--------+------------+--------+-------------+---------------+-----------------------------------------+
    | Hold   | +          | +      | +           | +             | | ``m.hold()``                          |
    |        |            |        |             |               | | ``m.run_target(500, 90, Stop.HOLD)``  |
    |        |            |        |             |               | | ``d.straight(0)``                     |
    |        |            |        |             |               | | ``d.straight(100)``                   |
    +--------+------------+--------+-------------+---------------+-----------------------------------------+
