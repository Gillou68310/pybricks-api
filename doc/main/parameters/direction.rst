.. pybricks-requirements::

Direction
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. class:: Direction

    Direction de rotation pour les valeurs de vitesse ou d'angle positives.

    .. autoattribute:: pybricks.parameters.Direction.CLOCKWISE
        :annotation:

    .. autoattribute:: pybricks.parameters.Direction.COUNTERCLOCKWISE
        :annotation:

    +--------------------------------+-------------------+-------------------+
    | ``positive_direction =``       | Vitesse positive: | Vitesse négative: |
    +================================+===================+===================+
    | ``Direction.CLOCKWISE``        | sens horaire      | sens antihoraire  |
    +--------------------------------+-------------------+-------------------+
    | ``Direction.COUNTERCLOCKWISE`` | sens antihoraire  | sens horaire      |
    +--------------------------------+-------------------+-------------------+

    En général, le sens horaire est défini en **regardant l'arbre du moteur,
    comme en regardant une horloge**. Certains moteurs ont deux arbres. En cas
    de doute, référez-vous au diagramme dans la documentation de la classe
    ``Motor``.
