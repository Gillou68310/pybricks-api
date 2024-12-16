# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2023 The Pybricks Authors

"""Outils communs pour le timing, la journalisation des données et l'algèbre linéaire."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional, Sequence, Tuple, overload, Coroutine

if TYPE_CHECKING:
    from ._common import MaybeAwaitable, MaybeAwaitableTuple
    from .parameters import Number


def wait(time: Number) -> MaybeAwaitable:
    """wait(time)

    Met en pause le programme utilisateur pendant une durée spécifiée.

    Arguments:
        time (Number, ms): Durée de l'attente.
    """


class StopWatch:
    """Un chronomètre pour mesurer les intervalles de temps. Semblable à la fonction chronomètre
    sur votre téléphone."""

    def __init__(self): ...

    def time(self) -> int:
        """time() -> int: ms

        Obtient le temps actuel du chronomètre.

        Retourne :
            Temps écoulé.
        """

    def pause(self) -> None:
        """pause()

        Met en pause le chronomètre."""

    def resume(self) -> None:
        """resume()

        Reprend le chronomètre."""

    def reset(self) -> None:
        """reset()

        Réinitialise le temps du chronomètre à 0.

        L'état de fonctionnement n'est pas affecté :

        * S'il était en pause, il reste en pause (mais maintenant à 0).
        * S'il était en cours d'exécution, il reste en cours d'exécution (mais recommence à partir de 0).
        """


class DataLog:
    """Créer un fichier et enregistrer des données."""

    def __init__(
        self,
        *headers: str,
        name: str = "log",
        timestamp: bool = True,
        extension: str = "csv",
        append: bool = False,
    ):
        """DataLog(*headers, name='log', timestamp=True, extension='csv', append=False)

        Arguments:
            headers (str, str, ...): En-têtes de colonnes. Ce sont les
                noms des colonnes de données. Par exemple, choisissez ``'time'`` et
                ``'angle'``.
            name (str): Nom du fichier.
            timestamp (bool): Choisissez ``True`` pour ajouter la date et l'heure au
                nom du fichier. De cette façon, votre fichier a un nom unique.
                Choisissez ``False`` pour omettre le timestamp.
            extension (str): Extension de fichier.
            append (bool): Choisissez ``True`` pour rouvrir un fichier de journal de données existant
                et y ajouter des données. Choisissez ``False`` pour effacer les données existantes.
                Si le fichier n'existe pas encore, un fichier vide sera
                créé de toute façon.
        """

    def log(self, *values: Any) -> None:
        """log(value1, value2, ...)

        Enregistre une ou plusieurs valeurs sur une nouvelle ligne dans le fichier.

        Arguments:
            values (object, object, ...): Un ou plusieurs objets ou valeurs.
        """


class Matrix:
    """Représentation mathématique d'une matrice. Elle prend en charge
    l'addition (``A + B``), la soustraction (``A - B``),
    et la multiplication de matrices (``A * B``) pour des matrices de taille compatible.

    Elle prend également en charge la multiplication scalaire (``c * A`` ou ``A * c``)
    et la division scalaire (``A / c``).

    Un objet :class:`.Matrix` est immuable."""

    def __add__(self, other) -> Matrix: ...

    def __iadd__(self, other) -> Matrix: ...

    def __sub__(self, other) -> Matrix: ...

    def __isub__(self, other) -> Matrix: ...

    def __mul__(self, other) -> Matrix: ...

    def __rmul__(self, other) -> Matrix: ...

    def __imul__(self, other) -> Matrix: ...

    def __truediv__(self, other) -> Matrix: ...

    def __itruediv__(self, other) -> Matrix: ...

    def __floordiv__(self, other) -> Matrix: ...

    def __ifloordiv__(self, other) -> Matrix: ...

    def __init__(self, rows: Sequence[Sequence[float]]):
        """Matrix(rows)

        Arguments:
            rows (list): Liste de lignes. Chaque ligne est elle-même une liste de nombres.

        """

    @property
    def T(self) -> Matrix:  # noqa: N802
        """Retourne une nouvelle :class:`.Matrix` qui est la transposée de la
        matrice d'origine."""

    @property
    def shape(self) -> Tuple[int, int]:
        """Retourne un tuple (``m``, ``n``),
        où ``m`` est le nombre de lignes et ``n`` est le nombre de colonnes.
        """


@overload
def vector(x: float, y: float) -> Matrix:
    """
    Fonction pratique pour créer une :class:`.Matrix` avec la forme (``2``, ``1``).

    Arguments:
        x (float): Coordonnée x du vecteur.
        y (float): Coordonnée y du vecteur.

    Retourne :
        Une matrice avec la forme d'un vecteur colonne.
    """


@overload
def vector(x: float, y: float, z: float) -> Matrix:
    """
    Fonction pratique pour créer une :class:`.Matrix` avec la forme (``3``, ``1``).

    Arguments:
        x (float): Coordonnée x du vecteur.
        y (float): Coordonnée y du vecteur.
        z (float): Coordonnée z du vecteur.

    Retourne :
        Une matrice avec la forme d'un vecteur colonne.
    """


def vector(*args):
    """
    vector(x, y) -> Matrix
    vector(x, y, z) -> Matrix

    Fonction pratique pour créer une :class:`.Matrix` avec la
    forme (``2``, ``1``) ou (``3``, ``1``).

    Arguments:
        x (float): Coordonnée x du vecteur.
        y (float): Coordonnée y du vecteur.
        z (float): Coordonnée z du vecteur (optionnel).

    Retourne :
        Une matrice avec la forme d'un vecteur colonne.
    """


def cross(a: Matrix, b: Matrix) -> Matrix:
    """
    cross(a, b) -> Matrix

    Obtient le produit vectoriel ``a`` × ``b`` de deux vecteurs.

    Arguments:
        a (Matrix): Un vecteur tridimensionnel.
        b (Matrix): Un vecteur tridimensionnel.

    Retourne :
        Le produit vectoriel, également un vecteur tridimensionnel.
    """


def read_input_byte(last: bool = False, chr: bool = False) -> Optional[int | str]:
    """
    read_input_byte() -> int | str | None

    Lit un octet à partir de l'entrée standard sans bloquer et le supprime du
    tampon d'entrée.

    Arguments:
        last (bool): Choisissez ``True`` pour lire le dernier octet (le plus récent) dans le tampon et ignorer le reste.
                     Choisissez ``False`` pour lire uniquement le premier octet (le plus ancien).
        chr (bool): Choisissez ``True`` pour convertir le résultat en une chaîne de caractères d'un seul caractère.

    Retourne :
        L'octet qui a été lu, sous forme de valeur numérique (``0`` à ``255``) ou
        de chaîne (par exemple ``"B"``). Retourne ``None`` si aucune donnée n'est disponible. Si
        ``chr=True``, il retourne également ``None`` si l'octet lu ne peut pas
        être imprimé en tant que caractère.
    """


def hub_menu(*symbols: int | str) -> int | str:
    """
    hub_menu(symbol1, symbol2, ...) -> int | str

    Affiche un menu sur l'écran du hub et attend que l'utilisateur sélectionne un élément
    en utilisant les boutons. Peut être utilisé dans votre propre programme de menu qui vous permet
    de choisir lequel de vos autres programmes exécuter.

    Notez que ceci est juste une fonction pratique qui combine l'affichage,
    les boutons et les attentes pour créer un menu simple. Cela signifie qu'elle peut être utilisée
    n'importe où dans un programme, pas seulement au début.

    Arguments:
        symbol1 (int ou str): Le premier symbole à afficher dans le menu.
        symbol2 (int ou str): Le deuxième symbole, et ainsi de suite...

    Retourne :
        Le symbole sélectionné.
    """


def multitask(*coroutines: Coroutine, race=False) -> MaybeAwaitableTuple:
    """
    multitask(coroutine1, coroutine2, ...) -> Tuple

    Exécute plusieurs coroutines simultanément. Cela crée une nouvelle coroutine qui
    peut être utilisée comme n'importe quelle autre, y compris dans une autre instruction ``multitask``.

    Arguments:
        coroutines (coroutine, coroutine, ...): Une ou plusieurs coroutines à exécuter
            en parallèle.
        race (bool): Choisissez ``False`` pour attendre que toutes les coroutines se terminent.
            Choisissez ``True`` pour attendre qu'une coroutine se termine et ensuite
            annuler les autres, comme si c'était une "course".

    Retourne :
        Tuple des valeurs de retour de chaque coroutine. Les coroutines non terminées
        auront ``None`` comme valeur de retour.
    """


def run_task(coroutine: Coroutine) -> Optional[bool]:
    """
    run_task(coroutine) -> bool | None

    Exécute une coroutine du début à la fin tout en bloquant le reste du
    programme. Cela est principalement utilisé pour exécuter la coroutine principale d'un programme.

    Les appels à cette fonction ne sont pas autorisés à être imbriqués.

    Arguments:
        coroutine (coroutine): La coroutine principale à exécuter.

    Retourne :
        Si aucune ``coroutine`` n'est donnée, cette fonction retourne si la
        boucle d'exécution est actuellement active (``True``) ou non (``False``).
    """


# HACK: hide from jedi
if TYPE_CHECKING:
    del Number
    del MaybeAwaitable
    del MaybeAwaitableTuple
