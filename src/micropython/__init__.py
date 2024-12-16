# SPDX-License-Identifier: MIT
# Copyright (c) 2021 The Pybricks Authors
#
# Documentation copied from:
# https://raw.githubusercontent.com/micropython/micropython/master/docs/library/micropython.rst
# Copyright (c) 2014-2021, Damien P. George, Paul Sokolovsky, and contributors

"""
Accéder et contrôler les internes de MicroPython.
"""

from typing import Any, overload


@overload
def const(value: int) -> int:
    ...


@overload
def const(value: str) -> str:
    ...


@overload
def const(value: float) -> float:
    ...


@overload
def const(value: tuple) -> tuple:
    ...


def const(value):
    """
    const(value) -> Any

    Déclare la valeur comme une constante, ce qui rend votre code plus efficace.

    Pour réduire encore l'utilisation de la mémoire, préfixez son nom par un
    underscore (``_ORANGES``). Cette constante ne peut être utilisée que dans le
    même fichier.

    Si vous souhaitez importer la valeur d'un autre module, utilisez un nom sans
    underscore (``APPLES``). Cela utilise un peu plus de mémoire.

    Arguments:
        value (int ou float ou str ou tuple): La valeur littérale à rendre constante.

    Retourne :
        La valeur constante.
    """


@overload
def opt_level() -> int:
    ...


@overload
def opt_level(level: int) -> None:
    ...


def opt_level(*args):
    """
    Définit le niveau d'optimisation pour le code compilé sur le hub :

    0. Les instructions d'assertion sont activées. La variable intégrée ``__debug__`` est
       ``True``. Les numéros de ligne du script sont sauvegardés, afin qu'ils puissent être signalés lorsqu'une
       Exception se produit.
    1. Les assertions sont ignorées et ``__debug__`` est ``False``.
       Les numéros de ligne du script sont sauvegardés.
    2. Les assertions sont ignorées et ``__debug__`` est ``False``.
       Les numéros de ligne du script sont sauvegardés.
    3. Les assertions sont ignorées et ``__debug__`` est ``False``.
       Les numéros de ligne du script ne sont *pas* sauvegardés.

    Cela s'applique uniquement au code que vous exécutez dans le REPL, car les scripts réguliers
    sont déjà compilés avant d'être envoyés au hub.

    Arguments:
        level (int): Le niveau à définir.

    Retourne :
        Si aucun argument n'est donné, cela retourne le niveau d'optimisation actuel.
    """


@overload
def mem_info() -> None:
    ...


@overload
def mem_info(verbose: Any) -> None:
    ...


def mem_info(*args):
    """
    mem_info()
    mem_info(verbose)

    Affiche des informations sur l'utilisation de la pile et de la mémoire heap.

    Arguments:
        verbose: Si une valeur est donnée, cela affiche également l'ensemble de la mémoire heap.
            Cela indique quels blocs sont utilisés et lesquels sont libres.
    """


@overload
def qstr_info() -> None:
    ...


@overload
def qstr_info(verbose: Any) -> None:
    ...


def qstr_info(*args):
    """
    qstr_info()
    qstr_info(verbose)

    Affiche combien de chaînes sont internées et combien de RAM elles utilisent.

    MicroPython utilise l'internement de chaînes pour économiser à la fois la RAM et la ROM.
    Cela évite d'avoir à stocker des copies en double de la même chaîne.

    Arguments:
        verbose: Si une valeur est donnée, cela affiche également les noms de toutes
            les chaînes internées en RAM.
    """


def stack_use() -> int:
    """
    stack_use() -> int

    Vérifie la quantité de pile utilisée. Cela peut être utilisé pour
    calculer les différences d'utilisation de la pile à différents points d'un script.

    Retourne :
        La quantité de pile utilisée.
    """


def heap_lock() -> None:
    """
    heap_lock()

    Verrouille la mémoire heap. Lorsqu'elle est verrouillée, aucune allocation de mémoire ne peut se produire. Une
    ``MemoryError`` sera levée si une allocation de mémoire heap est tentée.
    """


def heap_unlock() -> int:
    """
    heap_unlock() -> int

    Déverrouille la mémoire heap. L'allocation de mémoire est à nouveau autorisée.

    Si :func:`heap_lock()` a été appelé plusieurs fois, :func:`heap_unlock()`
    doit être appelé le même nombre de fois pour rendre la mémoire heap à nouveau disponible.

    Retourne :
        La profondeur de verrouillage après le déverrouillage. Elle est ``0`` une fois déverrouillée.
    """


def kbd_intr(chr: int) -> None:
    """
    kbd_intr(chr)

    Définit le caractère qui déclenche une exception ``KeyboardInterrupt`` lorsque
    vous le tapez dans la fenêtre de saisie. Par défaut, il est réglé sur ``3``,
    ce qui correspond à la pression sur :kbd:`Ctrl` :kbd:`C`.

    Arguments:
        chr (int): Caractère qui doit lever l'exception ``KeyboardInterrupt``.
            Choisissez ``-1`` pour désactiver cette fonctionnalité.
    """
