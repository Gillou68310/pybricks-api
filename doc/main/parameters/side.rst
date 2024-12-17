.. pybricks-requirements::

Côté
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. class:: Side

    Côté d'un hub ou d'un capteur. Ces dispositifs sont principalement des
    boîtes rectangulaires avec six côtés :

    .. autoattribute:: pybricks.parameters.Side.TOP
        :annotation:

    .. autoattribute:: pybricks.parameters.Side.BOTTOM
        :annotation:

    .. autoattribute:: pybricks.parameters.Side.FRONT
        :annotation:

    .. autoattribute:: pybricks.parameters.Side.BACK
        :annotation:

    .. autoattribute:: pybricks.parameters.Side.LEFT
        :annotation:

    .. autoattribute:: pybricks.parameters.Side.RIGHT
        :annotation:


    Les écrans ou les matrices de lumière n'ont que quatre côtés. Pour
    ceux-ci, ``TOP`` est traité de la même manière que ``FRONT``, et
    ``BOTTOM`` est traité de la même manière que ``BACK``. Les diagrammes
    ci-dessous définissent les côtés pour les dispositifs pertinents.

    **Prime Hub**

    .. figure:: ../../main/diagrams/orientation_primehub.png
        :width: 60%

    **Inventor Hub**

    .. figure:: ../../main/diagrams/orientation_inventorhub.png
        :width: 60%

    **Essential Hub**

    .. figure:: ../../main/diagrams/orientation_essentialhub.png
        :width: 60%

    **Move Hub**

    .. figure:: ../../main/diagrams/orientation_movehub.png
        :width: 60%

    **Technic Hub**

    .. figure:: ../../main/diagrams/orientation_technichub.png
        :width: 60%

    .. versionchanged:: 3.2

        Changement du côté avant.

    **Capteur d'inclinaison**

    .. figure:: ../../main/diagrams/orientation_tiltsensor.png
        :width: 50%
