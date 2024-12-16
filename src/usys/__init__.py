# SPDX-License-Identifier: MIT
# Copyright (c) 2021 The Pybricks Authors
#
# Portions of documentation copied from:
# https://raw.githubusercontent.com/micropython/micropython/1e6d18c915ccea0b6a19ffec9710d33dd7e5f866/docs/library/sys.rst
# Copyright (c) 2014-2021, Damien P. George, Paul Sokolovsky, and contributors

"""
Ce module fournit un sous-ensemble du module standard Python ``sys``.
"""

from typing import Tuple

from uio import FileIO as _FileIO

stdin: _FileIO = _FileIO()
"""
Ceci est un objet flux (:class:`uio.FileIO`) qui reçoit des entrées d'un
terminal connecté, le cas échéant.

Voir aussi :func:`kbd_intr <micropython.kbd_intr>` pour désactiver
``KeyboardInterrupt`` lors du passage de données binaires via ``stdin``.
"""

stdout: _FileIO = _FileIO()
"""
Ceci est un objet flux (:class:`uio.FileIO`) qui envoie des sorties à un
terminal connecté, le cas échéant.
"""

stderr: _FileIO = _FileIO()
"""
Alias pour :data:`stdout`.
"""

implementation: Tuple[str, Tuple[int, int, int], str, int] = (
    "micropython",
    (1, 19, 1),
    "NAME Hub with PROCESSOR",
    6,
)
"""
Tuple de version de MicroPython. Voir le format et l'exemple ci-dessous.
"""

version: str = "3.4.0; Pybricks MicroPython v3.2.0b5 on 2022-11-11"
"""
Version de compatibilité Python, version Pybricks et date de construction.
Voir le format et l'exemple ci-dessous.
"""

version_info: Tuple[int, int, int] = (3, 4, 0)
"""Version de compatibilité Python. Voir le format et l'exemple ci-dessous."""
