.. pybricks-requirements:: stm32-extra stm32-float

:mod:`umath <umath>` -- Fonctions mathématiques
===============================================

.. module:: umath

Ce module MicroPython est similaire au `math module`_ en Python.

Voir aussi les :ref:`fonctions mathématiques intégrées<builtinmath>` qui
peuvent être utilisées sans rien importer.

Arrondi et signe
----------------

.. blockimg:: pybricks_blockMathOp_roundup

.. autofunction:: umath.ceil

.. blockimg:: pybricks_blockMathOp_rounddown

.. autofunction:: umath.floor

.. autofunction:: umath.trunc

.. autofunction:: umath.fmod

.. autofunction:: umath.fabs

.. autofunction:: umath.copysign

Puissances et logarithmes
-------------------------

.. autodata:: umath.e

.. blockimg:: pybricks_blockMathOp_exp

.. autofunction:: umath.exp

.. blockimg:: pybricks_blockMathArithmetic_power

.. blockimg:: pybricks_blockMathOp_pow10

.. autofunction:: umath.pow

.. blockimg:: pybricks_blockMathOp_ln

.. autofunction:: umath.log

.. blockimg:: pybricks_blockMathOp_root

.. autofunction:: umath.sqrt

Trigonométrie
-------------

.. autodata:: umath.pi

.. autofunction:: umath.degrees

.. autofunction:: umath.radians

.. blockimg:: pybricks_blockMathOp_sin

.. autofunction:: umath.sin

.. blockimg:: pybricks_blockMathOp_asin

.. autofunction:: umath.asin

.. blockimg:: pybricks_blockMathOp_cos

.. autofunction:: umath.cos

.. blockimg:: pybricks_blockMathOp_acos

.. autofunction:: umath.acos

.. blockimg:: pybricks_blockMathOp_tan

.. autofunction:: umath.tan

.. blockimg:: pybricks_blockMathOp_atan

.. autofunction:: umath.atan

.. blockimg:: pybricks_blockMathOp_atan2

.. autofunction:: umath.atan2

Autres fonctions mathématiques
------------------------------

.. autofunction:: umath.isfinite

.. autofunction:: umath.isinfinite

.. autofunction:: umath.isnan

.. autofunction:: umath.modf

.. autofunction:: umath.frexp

.. autofunction:: umath.ldexp

.. _math module: https://docs.python.org/3.5/library/math.html#module-math
