# SPDX-License-Identifier: MIT
# Copyright (c) 2021 The Pybricks Authors
#
# Portions of documentation copied from:
# https://raw.githubusercontent.com/micropython/micropython/1e6d18c915ccea0b6a19ffec9710d33dd7e5f866/docs/library/uerrno.rst
# Copyright (c) 2014-2021, Damien P. George, Paul Sokolovsky, and contributors

"""
Ce module fournit l'accès aux codes d'erreur symboliques pour l'exception `OSError`.
"""

from typing import Dict

EAGAIN: int
"""
L'opération n'est pas terminée et doit être réessayée bientôt.
"""

EBUSY: int
"""
Le périphérique ou la ressource est occupé et ne peut pas être utilisé pour le moment.
"""

ECANCELED: int
"""
L'opération a été annulée.
"""

EINVAL: int
"""
Un argument invalide a été donné. Habituellement, ``ValueError`` est utilisé à la place.
"""

EIO: int
"""
Une erreur non spécifiée s'est produite.
"""

ENODEV: int
"""
Le périphérique n'a pas été trouvé. Par exemple, un capteur ou un moteur n'est pas branché dans le port correct.
"""

EOPNOTSUPP: int
"""
L'opération n'est pas prise en charge sur ce hub ou sur le périphérique connecté.
"""

EPERM: int
"""
L'opération ne peut pas être effectuée dans l'état actuel.
"""

ETIMEDOUT: int
"""
L'opération a expiré.
"""

# TODO: ev3dev has additional constants
# https://github.com/pybricks/pybricks-micropython/blob/11f19bc9c24fde66aa8ad42233a345e6683f5beb/bricks/ev3dev/mpconfigport.h#L156-L203

errorcode: Dict[int, str]
"""
Dictionnaire qui mappe les codes d'erreur numériques aux chaînes de caractères avec le code d'erreur symbolique.
"""
