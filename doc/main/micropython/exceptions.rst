Exceptions et erreurs
=====================

Cette section répertorie toutes les exceptions disponibles par ordre
alphabétique.

.. autoclass:: ubuiltins.ArithmeticError
    :no-members:

.. autoclass:: ubuiltins.AssertionError
    :no-members:

.. autoclass:: ubuiltins.AttributeError
    :no-members:

.. autoclass:: ubuiltins.BaseException
    :no-members:

.. autoclass:: ubuiltins.EOFError
    :no-members:

.. autoclass:: ubuiltins.Exception
    :no-members:

.. autoclass:: ubuiltins.GeneratorExit
    :no-members:

.. autoclass:: ubuiltins.ImportError
    :no-members:

.. autoclass:: ubuiltins.IndentationError
    :no-members:

.. autoclass:: ubuiltins.IndexError
    :no-members:

.. autoclass:: ubuiltins.KeyboardInterrupt
    :no-members:

.. autoclass:: ubuiltins.KeyError
    :no-members:

.. autoclass:: ubuiltins.LookupError
    :no-members:

.. autoclass:: ubuiltins.MemoryError
    :no-members:

.. autoclass:: ubuiltins.NameError
    :no-members:

.. autoclass:: ubuiltins.NotImplementedError
    :no-members:

.. _OSError:

.. autoclass:: ubuiltins.OSError
    :noindex:

.. autoclass:: ubuiltins.OverflowError
    :no-members:

.. autoclass:: ubuiltins.RuntimeError
    :no-members:

.. autoclass:: ubuiltins.StopIteration
    :no-members:

.. autoclass:: ubuiltins.SyntaxError
    :no-members:

.. autoclass:: ubuiltins.SystemExit
    :no-members:

.. autoclass:: ubuiltins.TypeError
    :no-members:

.. autoclass:: ubuiltins.ValueError
    :no-members:

.. autoclass:: ubuiltins.ZeroDivisionError
    :no-members:

Exemples
---------------------

Débogage dans le terminal REPL
******************************

.. literalinclude::
    ../../../examples/micropython/keyboard_interrupt.py

Exécution du code lorsque le bouton d'arrêt est pressé
******************************************************

.. literalinclude::
    ../../../examples/micropython/system_exit.py

.. _device_detection:

Détection des appareils à l'aide de ``OSError``
***********************************************

.. literalinclude::
    ../../../examples/micropython/oserror.py
