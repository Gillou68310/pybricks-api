.. pybricks-requirements::

Couleur
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. autoclass:: pybricks.parameters.Color
    :no-members:

    .. rubric:: Couleurs saturées

    Ces couleurs ont une saturation et une luminosité maximales. Elles
    diffèrent uniquement par la teinte.

    .. autoattribute:: RED

        .. pybricks-color:: RED

    .. autoattribute:: ORANGE

        .. pybricks-color:: ORANGE

    .. autoattribute:: YELLOW

        .. pybricks-color:: YELLOW

    .. autoattribute:: GREEN

        .. pybricks-color:: GREEN

    .. autoattribute:: CYAN

        .. pybricks-color:: CYAN

    .. autoattribute:: BLUE

        .. pybricks-color:: BLUE

    .. autoattribute:: VIOLET

        .. pybricks-color:: VIOLET

    .. autoattribute:: MAGENTA

        .. pybricks-color:: MAGENTA

    .. rubric:: Couleurs non saturées

    Ces couleurs ont une teinte et une saturation nulles. Elles diffèrent
    uniquement par la luminosité.

    Lors de la détection de ces couleurs à l'aide de capteurs, leurs valeurs
    dépendent beaucoup de la distance à l'objet. Si la distance entre le
    capteur et l'objet n'est pas constante dans votre robot, il est préférable
    d'utiliser uniquement l'une de ces couleurs dans vos programmes.

    .. autoattribute:: WHITE

        .. pybricks-color:: WHITE

    .. autoattribute:: GRAY

        .. pybricks-color:: GRAY

    .. autoattribute:: BLACK

        Cela représente des objets sombres qui reflètent encore une très
        petite quantité de lumière.

        .. pybricks-color:: BLACK

    .. autoattribute:: NONE

        Cela représente l'obscurité totale, sans réflexion ni lumière du tout.

        .. pybricks-color:: NONE

.. rubric:: Créer vos propres couleurs

Cet exemple montre les bases des propriétés des couleurs et comment définir de
nouvelles couleurs.

.. literalinclude::
    ../../../examples/pup/parameters/color_basics.py

Cet exemple montre des cas d'utilisation plus avancés de la classe ``Color``.

.. literalinclude::
    ../../../examples/pup/parameters/color_advanced.py
