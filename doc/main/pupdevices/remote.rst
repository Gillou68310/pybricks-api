.. pybricks-requirements::

Télécommande
^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: ../../main/cad/output/pupdevice-remote.png
   :width: 60 %

.. blockimg:: pybricks_variables_set_remote_connect_any

.. blockimg:: pybricks_variables_set_remote_connect_name
    :stack:

.. autoclass:: pybricks.pupdevices.Remote
  :no-members:

  .. automethod:: pybricks.pupdevices::Remote.name

  .. blockimg:: pybricks_blockLightOnColor_remote_on

  .. automethod:: pybricks.pupdevices::Remote.light.on

  .. blockimg:: pybricks_blockLightOnColor_remote_on

  .. automethod:: pybricks.pupdevices::Remote.light.off

  .. blockimg:: pybricks_blockButtonIsPressed_Remote

  .. automethod:: pybricks.pupdevices::Remote.buttons.pressed

  .. automethod:: pybricks.pupdevices::Remote.disconnect

Exemples
--------

Vérifier quels boutons sont pressés
***********************************

.. literalinclude::
    ../../../examples/pup/remote/basics.py

Changer la couleur de la lumière de la télécommande
***************************************************

.. literalinclude::
    ../../../examples/pup/remote/set_color_basic.py

Changer la couleur de la lumière en utilisant les boutons
*********************************************************

.. literalinclude::
    ../../../examples/pup/remote/set_color.py

Utiliser le paramètre de délai d'attente
****************************************

Vous pouvez utiliser l'argument ``timeout`` pour changer la durée pendant
laquelle le hub recherche la télécommande. Si vous choisissez ``None``, il
recherchera indéfiniment.

.. literalinclude::
    ../../../examples/pup/remote/timeout_none.py

Si la télécommande n'a pas été trouvée dans le délai spécifié ``timeout``, une
:ref:`OSError <OSError>` est levée. Vous pouvez intercepter cette exception
pour exécuter d'autres codes si la télécommande n'est pas disponible.

.. literalinclude::
    ../../../examples/pup/remote/timeout_exception.py

Changer le nom de la télécommande
*********************************

Vous pouvez changer le nom Bluetooth de la télécommande. Le nom par défaut
d'usine est ``Handset``.

.. blockimg:: pybricks_variables_set_remote_connect_rename

.. literalinclude::
    ../../../examples/pup/remote/set_name.py

Vous pouvez spécifier ce nom lors de la connexion à la télécommande. Cela vous
permet de choisir la bonne si plusieurs télécommandes sont à proximité.

.. blockimg:: pybricks_variables_set_remote_connect_name

.. literalinclude::
    ../../../examples/pup/remote/use_name.py
