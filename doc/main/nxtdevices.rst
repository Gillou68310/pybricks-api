:mod:`nxtdevices <pybricks.nxtdevices>` -- Appareils NXT
========================================================

.. automodule:: pybricks.nxtdevices
    :no-members:

Moteur NXT
^^^^^^^^^^

Ce moteur fonctionne comme un moteur LEGO MINDSTORMS EV3 Large. Vous pouvez
l'utiliser dans vos programmes en utilisant la classe :mod:`Motor <.ev3devices>`.

Capteur tactile NXT
^^^^^^^^^^^^^^^^^^^

.. figure:: ../main/cad/output/nxtdevice-touch.png
   :width: 18 %

.. autoclass:: pybricks.nxtdevices.TouchSensor
    :no-members:

    .. automethod:: pybricks.nxtdevices.TouchSensor.pressed

Capteur de lumière NXT
^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../main/cad/output/nxtdevice-light.png
   :width: 18 %

.. autoclass:: pybricks.nxtdevices.LightSensor

Capteur de couleur NXT
^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../main/cad/output/nxtdevice-color.png
   :width: 18 %

.. autoclass:: pybricks.nxtdevices.ColorSensor
    :no-members:

    .. automethod:: pybricks.nxtdevices.ColorSensor.color

    .. automethod:: pybricks.nxtdevices.ColorSensor.ambient

    .. automethod:: pybricks.nxtdevices.ColorSensor.reflection

    .. automethod:: pybricks.nxtdevices.ColorSensor.rgb

    .. rubric:: Détection avancée des couleurs

    .. automethod:: pybricks.nxtdevices.ColorSensor.hsv

    .. automethod:: pybricks.nxtdevices.ColorSensor.detectable_colors

    .. rubric:: Lumière intégrée

    Ce capteur a une lumière intégrée. Vous pouvez la rendre rouge, verte,
    bleue, ou l'éteindre.

    .. automethod:: pybricks.nxtdevices::ColorSensor.light.on

    .. automethod:: pybricks.nxtdevices::ColorSensor.light.off

Capteur ultrasonique NXT
^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../main/cad/output/nxtdevice-ultrasonic.png
   :width: 24 %

.. autoclass:: pybricks.nxtdevices.UltrasonicSensor

Capteur sonore NXT
^^^^^^^^^^^^^^^^^^

.. figure:: ../main/cad/output/nxtdevice-sound.png
   :width: 18 %

.. autoclass:: pybricks.nxtdevices.SoundSensor

Capteur de température NXT
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../main/cad/output/nxtdevice-temperature.png
   :width: 32 %

.. autoclass:: pybricks.nxtdevices.TemperatureSensor

Compteur d'énergie NXT
^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../main/cad/output/nxtdevice-energy.png
   :width: 30 %

.. autoclass:: pybricks.nxtdevices.EnergyMeter

Adaptateur Vernier
^^^^^^^^^^^^^^^^^^

.. autoclass:: pybricks.nxtdevices.VernierAdapter

**Exemple : Utilisation du capteur de température de surface.**

.. literalinclude:: ../../examples/ev3/vernier_surface_temperature/main.py
