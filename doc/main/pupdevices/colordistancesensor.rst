.. pybricks-requirements::

Capteur de Couleur et de Distance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../main/cad/output/pupdevice-colordistance.png
   :width: 35 %

.. blockimg:: pybricks_variables_set_color_distance_sensor_colordistancesensor_default

.. blockimg:: pybricks_variables_set_color_distance_sensor_colordistancesensor_detectable_colors

.. autoclass:: pybricks.pupdevices.ColorDistanceSensor
    :no-members:

    .. blockimg:: pybricks_blockColor_ColorDistanceSensor_color

    .. automethod:: pybricks.pupdevices.ColorDistanceSensor.color

    .. blockimg:: pybricks_blockLightReflection_ColorDistanceSensor

    .. automethod:: pybricks.pupdevices.ColorDistanceSensor.reflection

    .. blockimg:: pybricks_blockLightAmbient_ColorDistanceSensor

    .. automethod:: pybricks.pupdevices.ColorDistanceSensor.ambient

    .. blockimg:: pybricks_blockDistance_ColorDistanceSensor

    .. automethod:: pybricks.pupdevices.ColorDistanceSensor.distance

    .. blockimg:: pybricks_blockColor_ColorDistanceSensor_hsv

    .. automethod:: pybricks.pupdevices.ColorDistanceSensor.hsv

    .. automethod:: pybricks.pupdevices.ColorDistanceSensor.detectable_colors

    .. rubric:: Lumière intégrée

    Ce capteur dispose d'une lumière intégrée. Vous pouvez la rendre rouge,
    verte, bleue ou l'éteindre. Si vous utilisez le capteur pour mesurer
    quelque chose par la suite, la lumière se rallume automatiquement à la
    couleur par défaut pour cette méthode de détection.

    .. blockimg:: pybricks_blockLightOnColor_colordistancesensor_on

    .. automethod:: pybricks.pupdevices::ColorDistanceSensor.light.on

    .. blockimg:: pybricks_blockLightOnColor_colordistancesensor_off

    .. automethod:: pybricks.pupdevices::ColorDistanceSensor.light.off

Exemples
-------------------

Mesurer la couleur
******************

.. literalinclude::
    ../../../examples/pup/sensor_color_distance/color_print.py


Attendre une couleur
********************

.. literalinclude::
    ../../../examples/pup/sensor_color_distance/wait_for_color.py

Mesurer la distance et faire clignoter la lumière
*************************************************

.. literalinclude::
    ../../../examples/pup/sensor_color_distance/distance_blink.py

Lire la teinte, la saturation, la valeur
****************************************

.. literalinclude::
    ../../../examples/pup/sensor_color_distance/hsv.py

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
    ../../../examples/pup/sensor_color_distance/detectable_colors.py
