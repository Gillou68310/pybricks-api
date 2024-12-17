.. pybricks-requirements:: stm32-extra

:mod:`usys` -- Fonctions spécifiques au système
============================================================

Ce module MicroPython est un sous-ensemble du `sys module`_ en Python.

.. rubric:: Flux d'entrée et de sortie

.. module:: usys

.. autodata:: usys.stdin
    :annotation:

.. autodata:: usys.stdout
    :annotation:

.. autodata:: usys.stderr
    :annotation:

.. rubric:: Informations sur la version

.. autodata:: implementation
    :annotation:

.. autodata:: version
    :annotation:

.. autodata:: version_info
    :annotation:

Exemples
---------------

Informations sur la version
*******************************

.. literalinclude::
    ../../../examples/micropython/usys/pybricks_version.py

.. literalinclude::
    ../../../examples/micropython/usys/micropython_version.py

Entrée et sortie standard
*******************************

Le flux ``stdin`` peut être utilisé pour capturer des entrées via la fenêtre
d'entrée/sortie de Pybricks Code. Voir le projet `keyboard input`_ pour
apprendre comment cela fonctionne. Cette approche peut être étendue pour
échanger des données avec tout `other device`_ également.

.. _keyboard input: https://pybricks.com/projects/tutorials/wireless/hub-to-device/pc-keyboard/
.. _other device: https://pybricks.com/projects/tutorials/wireless/hub-to-device/

.. _sys module: https://docs.python.org/3.5/library/sys.html
