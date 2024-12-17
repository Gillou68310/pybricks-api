.. pybricks-requirements::

Capteur de Couleur
^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../main/diagrams/sensor_color_lights.png
   :width: 70 %

.. blockimg:: pybricks_variables_set_color_sensor_colorsensor_default

.. blockimg:: pybricks_variables_set_color_sensor_colorsensor_detectable_colors

.. autoclass:: pybricks.pupdevices.ColorSensor
    :no-members:

    .. blockimg:: pybricks_blockColor_ColorSensor_color

    .. automethod:: pybricks.pupdevices.ColorSensor.color

    .. blockimg:: pybricks_blockLightReflection_ColorSensor

    .. automethod:: pybricks.pupdevices.ColorSensor.reflection

    .. blockimg:: pybricks_blockLightAmbient_ColorSensor

    .. automethod:: pybricks.pupdevices.ColorSensor.ambient

    .. rubric:: Détection avancée des couleurs

    .. blockimg:: pybricks_blockColor_ColorSensor_hsv

    .. automethod:: pybricks.pupdevices.ColorSensor.hsv

    .. automethod:: pybricks.pupdevices.ColorSensor.detectable_colors

    .. rubric:: Lumières intégrées

    Ce capteur dispose de 3 lumières intégrées. Vous pouvez ajuster la
    luminosité de chaque lumière. Si vous utilisez le capteur pour mesurer
    quelque chose, les lumières seront allumées ou éteintes selon les besoins
    de la mesure.

    .. blockimg:: pybricks_blockLightOn_colorsensor_on

    .. blockimg:: pybricks_blockLightOn_colorsensor_on_list
        :stack:

    .. automethod:: pybricks.pupdevices::ColorSensor.lights.on

    .. blockimg:: pybricks_blockLightOn_colorsensor_off

    .. automethod:: pybricks.pupdevices::ColorSensor.lights.off


Exemples
-------------------

Mesurer la couleur et la réflexion
**********************************

.. literalinclude::
    ../../../examples/pup/sensor_color/color_print.py


Attendre une couleur
********************

.. literalinclude::
    ../../../examples/pup/sensor_color/wait_for_color.py


Lire la teinte, la saturation et la valeur *réfléchies*
*******************************************************

.. literalinclude::
    ../../../examples/pup/sensor_color/hsv.py


Changer les couleurs détectables
********************************

Par défaut, le capteur est configuré pour détecter le rouge, le jaune, le
vert, le bleu, le blanc ou aucune couleur, ce qui convient à de nombreuses
applications.

Pour de meilleurs résultats dans votre application, vous pouvez mesurer vos
couleurs souhaitées à l'avance et dire au capteur de ne rechercher que ces
couleurs. Assurez-vous de les mesurer à la **même distance et dans les mêmes
conditions d'éclairage** que dans votre application finale. Vous obtiendrez
alors des résultats très précis même pour les couleurs qui sont autrement
difficiles à détecter.

.. literalinclude::
    ../../../examples/pup/sensor_color/detectable_colors.py

Lire la teinte, la saturation, la valeur et la couleur *ambiantes*
******************************************************************

.. literalinclude::
    ../../../examples/pup/sensor_color/color_ambient.py

Faire clignoter les lumières intégrées
**************************************

.. literalinclude::
    ../../../examples/pup/sensor_color/lights_blink.py

Éteindre les lumières à la fin du programme
*******************************************

.. literalinclude::
    ../../../examples/pup/sensor_color/cleanup.py
