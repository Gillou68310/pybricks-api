Classes et fonctions intégrées
==============================

Les classes et fonctions présentées sur cette page peuvent être utilisées sans
importer quoi que ce soit.

Entrée et sortie
----------------

.. pybricks-requirements:: stm32-extra

.. autofunction:: ubuiltins.input

.. pybricks-requirements::

.. blockimg:: pybricks_blockPrint_print_basic

.. blockimg:: pybricks_blockPrint_print_multiple

.. autofunction:: ubuiltins.print

Types de base
-------------

.. pybricks-requirements::

.. blockimg:: pybricks_blockLogicTrueFalse_false

.. blockimg:: pybricks_blockLogicTrueFalse_true

.. autoclass:: ubuiltins.bool

.. pybricks-requirements:: stm32-float

.. autoclass:: ubuiltins.complex

.. pybricks-requirements::

.. autoclass:: ubuiltins.dict

.. pybricks-requirements:: stm32-float

.. autoclass:: ubuiltins.float

.. pybricks-requirements::

.. autoclass:: ubuiltins.int
    :no-members:

    .. automethod:: ubuiltins.int.to_bytes

    .. automethod:: ubuiltins.int.from_bytes

.. pybricks-requirements::

.. autoclass:: ubuiltins.object

.. pybricks-requirements::

.. autoclass:: ubuiltins.type

Séquences
---------

.. pybricks-requirements:: stm32-extra

.. autoclass:: ubuiltins.bytearray

.. pybricks-requirements::

.. autoclass:: ubuiltins.bytes

.. pybricks-requirements::

.. blockimg:: pybricks_blockListLength

.. autofunction:: ubuiltins.len

.. pybricks-requirements::

.. blockimg:: pybricks_blockListCreate_list_empty
    :stack:

.. blockimg:: pybricks_blockListCreate_list_3
    :stack:

.. blockimg:: pybricks_blockListUnpack
    :stack:

.. blockimg:: pybricks_blockListGet_list_get_first
    :stack:

.. blockimg:: pybricks_blockListGet_list_get_index
    :stack:

.. blockimg:: pybricks_blockListGet_list_get_last
    :stack:

.. blockimg:: pybricks_blockListGet_list_get_random
    :stack:

.. blockimg:: pybricks_blockListSet_list_insert_first
    :stack:

.. blockimg:: pybricks_blockListSet_list_insert_index
    :stack:

.. blockimg:: pybricks_blockListSet_list_insert_last
    :stack:

.. blockimg:: pybricks_blockListSet_list_remove_first
    :stack:

.. blockimg:: pybricks_blockListSet_list_remove_index
    :stack:

.. blockimg:: pybricks_blockListSet_list_remove_last
    :stack:

.. blockimg:: pybricks_blockListSet_list_set_first
    :stack:

.. blockimg:: pybricks_blockListSet_list_set_index
    :stack:

.. blockimg:: pybricks_blockListSet_list_set_last
    :stack:

.. autoclass:: ubuiltins.list

.. pybricks-requirements:: stm32-extra

.. autoclass:: ubuiltins.set

.. pybricks-requirements:: stm32-extra

.. autoclass:: ubuiltins.slice

.. pybricks-requirements::

.. blockimg:: pybricks_blockTextLiteral

.. autoclass:: ubuiltins.str

.. pybricks-requirements::

.. autoclass:: ubuiltins.tuple

Itérateurs
----------

.. pybricks-requirements::

.. autofunction:: ubuiltins.all

.. pybricks-requirements::

.. autofunction:: ubuiltins.any

.. pybricks-requirements:: stm32-extra

.. autoclass:: ubuiltins.enumerate

.. pybricks-requirements::

.. autofunction:: ubuiltins.iter

.. pybricks-requirements::

.. autofunction:: ubuiltins.map

.. pybricks-requirements::

.. autofunction:: ubuiltins.next

.. pybricks-requirements::

.. autoclass:: ubuiltins.range

.. pybricks-requirements:: stm32-extra

.. autofunction:: ubuiltins.reversed

.. pybricks-requirements::

.. autofunction:: ubuiltins.sorted

.. pybricks-requirements::

.. autofunction:: ubuiltins.zip

Fonctions de conversion
-----------------------

.. pybricks-requirements::

.. autofunction:: ubuiltins.bin

.. pybricks-requirements::

.. autofunction:: ubuiltins.chr

.. pybricks-requirements::

.. autofunction:: ubuiltins.hex

.. pybricks-requirements::

.. autofunction:: ubuiltins.oct

.. pybricks-requirements::

.. autofunction:: ubuiltins.ord

.. pybricks-requirements::

.. autofunction:: ubuiltins.repr

.. _builtinmath:

Fonctions mathématiques
-----------------------

Voir aussi :mod:`umath` pour les opérations mathématiques en virgule
flottante.

.. pybricks-requirements::

.. blockimg:: pybricks_blockMathOp_abs

.. autofunction:: ubuiltins.abs

.. pybricks-requirements::

.. autofunction:: ubuiltins.divmod

.. pybricks-requirements::

.. blockimg:: pybricks_blockMathOp_max

.. autofunction:: ubuiltins.max

.. pybricks-requirements::

.. blockimg:: pybricks_blockMathOp_min

.. autofunction:: ubuiltins.min

.. pybricks-requirements::

.. autofunction:: ubuiltins.pow

.. pybricks-requirements::

.. blockimg:: pybricks_blockMathOp_round

.. autofunction:: ubuiltins.round

.. pybricks-requirements::

.. autofunction:: ubuiltins.sum

Fonctions d'exécution
---------------------

.. pybricks-requirements::

.. autofunction:: ubuiltins.eval

.. pybricks-requirements::

.. autofunction:: ubuiltins.exec

.. pybricks-requirements::

.. autofunction:: ubuiltins.globals

.. pybricks-requirements::

.. autofunction:: ubuiltins.hash

.. pybricks-requirements:: stm32-extra

.. autofunction:: ubuiltins.help

.. pybricks-requirements::

.. autofunction:: ubuiltins.id

.. pybricks-requirements::

.. autofunction:: ubuiltins.locals

Fonctions de classe
-------------------

.. pybricks-requirements::

.. autofunction:: ubuiltins.callable

.. pybricks-requirements::

.. autofunction:: ubuiltins.dir

.. pybricks-requirements::

.. autofunction:: ubuiltins.getattr

.. pybricks-requirements::

.. autofunction:: ubuiltins.hasattr

.. pybricks-requirements::

.. autofunction:: ubuiltins.isinstance

.. pybricks-requirements::

.. autofunction:: ubuiltins.issubclass

.. pybricks-requirements::

.. autofunction:: ubuiltins.setattr

.. pybricks-requirements::

.. autofunction:: ubuiltins.super

Décorateurs de méthode
----------------------

.. pybricks-requirements::

.. autodecorator:: ubuiltins.classmethod

.. pybricks-requirements::

.. autodecorator:: ubuiltins.staticmethod
