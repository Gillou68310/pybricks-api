.. pybricks-requirements::

Lumière
^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../main/cad/output/pupdevice-light.png
   :width: 35 %

.. blockimg:: pybricks_variables_set_light

.. autoclass:: pybricks.pupdevices.Light
    :no-members:

    .. blockimg:: pybricks_blockLightOn_light_on

    .. automethod:: pybricks.pupdevices.Light.on

    .. blockimg:: pybricks_blockLightOn_light_off

    .. automethod:: pybricks.pupdevices.Light.off

Exemples
--------

Faire clignoter la lumière
**************************

.. literalinclude::
    ../../../examples/pup/light/basics.py

Changer progressivement la luminosité
*************************************

.. literalinclude::
    ../../../examples/pup/light/math.py
