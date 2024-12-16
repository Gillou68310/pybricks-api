# SPDX-License-Identifier: MIT
# Copyright (c) 2021 The Pybricks Authors
#
# Portions of documentation copied from:
# https://raw.githubusercontent.com/micropython/micropython/1e6d18c915ccea0b6a19ffec9710d33dd7e5f866/docs/library/uselect.rst
# Copyright (c) 2014-2021, Damien P. George, Paul Sokolovsky, and contributors

"""
Ce module fournit des fonctions pour attendre efficacement des événements sur plusieurs flux.
"""

from typing import IO, Iterator, List, Tuple, overload

POLLIN: int
"""
Les données sont disponibles pour la lecture.
"""

POLLOUT: int
"""
Plus de données peuvent être écrites.
"""

POLLERR: int
"""
Une condition d'erreur s'est produite sur le flux associé. Doit être gérée explicitement
sinon les appels ultérieurs à :meth:`poll` peuvent retourner immédiatement.
"""

POLLHUP: int
"""
Une déconnexion s'est produite sur le flux associé. Doit être gérée explicitement
sinon les appels ultérieurs à :meth:`poll` peuvent retourner immédiatement.
"""


class Poll:
    def register(self, object: IO, eventmask: int) -> None:
        """
        register(object, eventmask=POLLOUT | POLLOUT)

        Enregistre un objet flux pour le polling. L'objet flux sera maintenant
        surveillé pour les événements. Si un événement se produit, il fait partie de la
        valeur de retour de :meth:`poll`.

        Si cette méthode est appelée à nouveau pour le même objet flux, l'objet
        ne sera pas enregistré à nouveau, mais les indicateurs ``eventmask`` seront
        mis à jour, comme si on appelait :meth:`modify()`.

        Arguments:
            object (FileIO): Flux à enregistrer pour le polling.
            eventmask (int): Quels événements utiliser. Doit être ``POLLIN``,
                ``POLLOUT``, ou leur disjonction logique : ``POLLIN | POLLOUT``.
        """

    def unregister(self, object: IO) -> None:
        """
        unregister(poll)

        Désenregistre un objet du polling.

        Arguments:
            object (FileIO): Flux à désenregistrer du polling.
        """

    def modify(self, obj: IO, eventmask: int) -> None:
        """
        modify(object, eventmask)

        Modifie le masque d'événements pour l'objet flux.

        Arguments:
            object (FileIO): Flux à enregistrer pour le polling.
            eventmask (int): Quels événements utiliser.

        Lève :
            ``OSError``: Si l'objet n'est pas enregistré. L'erreur est ``ENOENT``.
        """

    @overload
    def poll(self) -> List[Tuple[IO, int]]:
        ...

    @overload
    def poll(self, timeout: int) -> List[Tuple[IO, int]]:
        ...

    def poll(self, timeout: int = -1, /) -> List[Tuple[IO, int]]:
        """
        poll(timeout=-1) -> List[Tuple[FileIO, int]]

        Attendre jusqu'à ce qu'au moins un des objets enregistrés ait un nouvel événement ou
        une condition exceptionnelle prête à être gérée.

        Arguments:
            timeout (int): Timeout en millisecondes. Choisissez ``0`` pour retourner
                immédiatement ou choisissez ``-1`` pour attendre indéfiniment.

        Retourne :
            Une liste de tuples. Il y a un tuple (``object``, ``eventmask``, ...)
            pour chaque objet avec un événement, ou aucun tuple s'il n'y a pas
            d'événements à gérer. La valeur ``eventmask``
            est une combinaison de drapeaux de polling pour indiquer ce qui s'est passé. Cela peut
            inclure ``POLLERR`` et ``POLLHUP`` même s'ils n'ont pas été enregistrés.
        """

    @overload
    def ipoll(self) -> Iterator[Tuple[IO, int]]:
        ...

    @overload
    def ipoll(self, timeout: int) -> Iterator[Tuple[IO, int]]:
        ...

    @overload
    def ipoll(self, timeout: int, flags: int) -> Iterator[Tuple[IO, int]]:
        ...

    def ipoll(self, timeout: int = -1, flags: int = 0, /) -> Iterator[Tuple[IO, int]]:
        """
        ipoll(timeout=-1, flags=1) -> Iterator[Tuple[FileIO, int]]

        Tout d'abord, comme :meth:`poll`, attendre jusqu'à ce qu'au moins un des objets enregistrés
        ait un nouvel événement ou une condition exceptionnelle prête à être gérée.

        Mais au lieu d'une liste, cette méthode retourne un itérateur pour une efficacité accrue.
        L'itérateur renvoie un tuple (``object``, ``eventmask``, ...)
        à la fois, et le remplace lors de la génération de la valeur suivante. Si vous
        avez besoin des valeurs plus tard, assurez-vous de les copier explicitement.

        Arguments:
            timeout (int): Timeout en millisecondes. Choisissez ``0`` pour retourner
                immédiatement ou choisissez ``-1`` pour attendre indéfiniment.
            flags (int): Si défini à ``1``, un comportement one-shot pour les événements est
                utilisé. Cela signifie que les flux pour lesquels des événements se sont produits
                auront leurs masques d'événements automatiquement réinitialisés en utilisant
                ``poll.modify(obj, 0)``. De cette façon, les nouveaux événements pour un tel flux
                ne seront pas traités jusqu'à ce qu'un nouveau masque soit défini avec :meth:`modify`,
                ce qui est utile pour les planificateurs d'E/S asynchrones.
        """


def poll() -> Poll:
    """
    Crée une instance de la classe :class:`Poll`.

    Retourne :
        L'instance :class:`Poll`.
    """
