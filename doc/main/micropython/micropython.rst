.. pybricks-requirements:: stm32-extra

:mod:`micropython` -- Internes de MicroPython
=============================================

.. automodule:: micropython
    :no-members:

.. autofunction:: micropython.const

.. autofunction:: micropython.heap_lock

.. autofunction:: micropython.heap_unlock

.. autofunction:: micropython.kbd_intr

.. autofunction:: micropython.mem_info

.. autofunction:: micropython.opt_level

.. autofunction:: micropython.qstr_info

.. autofunction:: micropython.stack_use


Exemples
---------------------

Utilisation des constantes pour l'efficacité
********************************************

.. literalinclude::
    ../../../examples/micropython/const.py

Vérification de la RAM libre
****************************

.. literalinclude::
    ../../../examples/micropython/memuse.py

Cela imprime des informations dans le format montré ci-dessous. Dans cet
exemple pour le SPIKE Prime Hub, il reste 257696 octets (251 KB) de mémoire
pour les variables de votre code. ::

    stack: 372 out of 40184
    GC: total: 258048, used: 352, free: 257696
    No. of 1-blocks: 4, 2-blocks: 2, max blk sz: 8, max free sz: 16103


Obtenir plus de statistiques sur la mémoire
*******************************************

.. literalinclude::
    ../../../examples/micropython/memstat.py
