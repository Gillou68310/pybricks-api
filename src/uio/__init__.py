# SPDX-License-Identifier: MIT
# Copyright (c) 2022 The Pybricks Authors
#
# Portions of documentation copied from:
# https://raw.githubusercontent.com/micropython/micropython/1e6d18c915ccea0b6a19ffec9710d33dd7e5f866/docs/library/uio.rst
# Copyright (c) 2014-2021, Damien P. George, Paul Sokolovsky, and contributors

"""
Ce module contient des objets ``stream`` qui se comportent comme des fichiers.
"""

# TODO: open() is not implemented on Powered Up hubs

from typing import overload, Union

# TODO: MicroPython streams implement '__enter__', '__exit__', 'close', 'read',
# 'readinto', 'readline', 'write', 'flush', 'seek', 'tell'
# and are iterable


class BytesIO:
    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, data: Union[bytes, bytearray]) -> None:
        ...

    @overload
    def __init__(self, alloc_size: int) -> None:
        ...

    def __init__(self, *args) -> None:
        """
        BytesIO(​)
        BytesIO(data)
        BytesIO(alloc_size)

        Un flux binaire utilisant un tampon de bytes en mémoire.

        Arguments:
            data (bytes ou bytearray): Objet optionnel de type bytes
                contenant des données initiales.
            alloc_size (int): Nombre optionnel de bytes préalloués. Ce
                paramètre est unique à MicroPython. Il n'est pas recommandé de
                l'utiliser dans le code utilisateur final.
        """

    def getvalue(self) -> bytes:
        """
        getvalue() -> bytes

        Obtient le contenu du tampon sous-jacent.
        """


class StringIO:
    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, string: str) -> None:
        ...

    @overload
    def __init__(self, alloc_size: int) -> None:
        ...

    def __init__(self, *args) -> None:
        """
        StringIO(​)
        StringIO(string)
        StringIO(alloc_size)

        Un flux utilisant un tampon de chaîne en mémoire.

        Arguments:
            string (str): Chaîne optionnelle avec des données initiales.
            alloc_size (int): Nombre optionnel de bytes préalloués. Ce
                paramètre est unique à MicroPython. Il n'est pas recommandé de
                l'utiliser dans le code utilisateur final.
        """

    def getvalue(self) -> str:
        """
        getvalue() -> str

        Obtient le contenu du tampon sous-jacent.
        """


class FileIO:
    """
    Ce type représente un fichier ouvert en mode binaire avec ``open(name, 'rb')``.
    Vous ne devez pas instancier cette classe directement.
    """
