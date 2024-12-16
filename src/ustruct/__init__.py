# SPDX-License-Identifier: MIT
# Copyright (c) 2021 The Pybricks Authors
#
# Portions of documentation copied from:
# https://raw.githubusercontent.com/micropython/micropython/1e6d18c915ccea0b6a19ffec9710d33dd7e5f866/docs/library/ustruct.rst
# Copyright (c) 2014-2021, Damien P. George, Paul Sokolovsky, and contributors

"""
Ce module fournit des fonctions pour convertir entre les valeurs Python et les structures de données de type C.
"""

from typing import Union, Tuple


def calcsize(format: str) -> int:
    """
    Obtient la taille des données correspondant à une chaîne de format.

    Arguments:
        format (str): Chaîne de format des données.

    Retourne :
        Le nombre d'octets nécessaires pour représenter ce format.
    """


def pack(format: str, *values) -> bytes:
    """
    pack(format, value1, value2, ...)

    Emballe les valeurs en utilisant le format donné.

    Arguments:
        format (str): Chaîne de format des données.

    Retourne :
        Les données encodées sous forme d'octets.
    """


def pack_into(format: str, buffer: bytearray, offset: int, *values) -> bytes:
    """
    pack_into(format, buffer, offset, value1, value2, ...)

    Encode les valeurs en utilisant le format donné et les écrit dans un tampon donné.

    Arguments:
        format (str): Chaîne de format des données.
        buffer (bytearray): Tampon pour stocker les données encodées.
        offset (int): Décalage à partir du début du tampon. Utilisez une valeur négative
            pour compter à partir de la fin du tampon.
    """


def unpack(format: str, data: Union[bytes, bytearray]) -> Tuple:
    """
    unpack(format, data) -> Tuple

    Décode les données binaires en utilisant le format donné.

    Arguments:
        format (str): Chaîne de format des données.
        data (bytes ou bytearray): Données à déballer.

    Retourne :
        Les données décodées sous forme de tuple de valeurs.
    """


def unpack_from(format: str, data: Union[bytes, bytearray], offset: int) -> Tuple:
    """
    unpack_from(format, data, offset) -> Tuple

    Décode les données binaires d'un tampon en utilisant le format donné.

    Arguments:
        format (str): Chaîne de format des données.
        data (bytes ou bytearray): Tampon de données à déballer.
        offset (int): Décalage à partir du début des données. Utilisez une valeur négative
            pour compter à partir de la fin des données.

    Retourne :
        Les données décodées sous forme de tuple de valeurs.
    """
