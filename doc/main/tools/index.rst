.. pybricks-requirements::

:mod:`tools <pybricks.tools>` -- Outils à usage général
========================================================

.. automodule:: pybricks.tools
    :no-members:

Outils de synchronisation
-------------------------

.. blockimg:: pybricks_blockWaitTime

.. autofunction:: wait

.. blockimg:: pybricks_variables_set_stopwatch

.. autoclass:: pybricks.tools.StopWatch
    :no-members:

    .. blockimg:: pybricks_blockStopWatchTime

    .. automethod:: pybricks.tools.StopWatch.time

    .. blockimg:: pybricks_blockStopWatchDo_StopWatch_pause

    .. automethod:: pybricks.tools.StopWatch.pause

    .. blockimg:: pybricks_blockStopWatchDo_StopWatch_resume

    .. automethod:: pybricks.tools.StopWatch.resume

    .. blockimg:: pybricks_blockStopWatchDo_StopWatch_reset

    .. automethod:: pybricks.tools.StopWatch.reset

Outils d'entrée
---------------

.. blockimg:: pybricks_blockReadInput_read_input_first_byte

.. blockimg:: pybricks_blockReadInput_read_input_first_char
    :stack:

.. blockimg:: pybricks_blockReadInput_read_input_last_byte
    :stack:

.. blockimg:: pybricks_blockReadInput_read_input_last_char
    :stack:

.. autofunction:: pybricks.tools.read_input_byte

.. versionchanged:: 3.3

    Ajout des options ``last`` et ``chr``.

.. pybricks-requirements:: light-matrix

.. autofunction:: pybricks.tools.hub_menu

.. literalinclude::
    ../../../examples/pup/tools/hub_menu.py

Outils d'algèbre linéaire
-------------------------

.. versionchanged:: 3.3

    Ces outils étaient précédemment situés dans le module
    ``pybricks.geometry``.

.. pybricks-requirements:: stm32-float

.. autoclass:: pybricks.tools.Matrix
    :no-members:

    .. autoattribute:: pybricks.tools::Matrix.T

    .. autoattribute:: pybricks.tools::Matrix.shape

.. pybricks-requirements:: stm32-float

.. blockimg:: pybricks_blockVector

.. autofunction:: pybricks.tools.vector

.. autofunction:: pybricks.tools.cross

Multitâche
----------

.. versionadded:: 3.3

Pybricks prend en charge le multitâche coopératif en utilisant les mots-clés
``async`` et ``await``. Cela permet aux opérations qui prennent normalement du
temps de s'exécuter en parallèle avec d'autres opérations.

.. blockimg:: pybricks_blockMultiTask

.. autofunction:: pybricks.tools.multitask

.. autofunction:: pybricks.tools.run_task

L'exemple suivant montre comment utiliser le multitâche pour faire avancer un
robot, puis tourner et déplacer une pince en même temps, puis reculer.

.. literalinclude::
    ../../../examples/pup/robotics/drivebase_async.py

.. class:: coroutine

.. class:: await

Chaque fois que vous voyez une fonction ou une méthode préfixée par ``await``,
cela signifie qu'elle prend en charge le multitâche. Lors de l'exécution d'une
coroutine avec ``run_task``, toutes les méthodes et fonctions préfixées par
``await`` agiront comme des coroutines.

Si vous n'utilisez pas le multitâche, vous pouvez ignorer le mot-clé ``await``
et écrire des programmes comme d'habitude. Plus précisément, lorsque
``run_task`` n'est pas utilisé, les fonctions préfixées par ``await`` agiront
comme des fonctions normales.
