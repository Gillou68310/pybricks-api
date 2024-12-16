# SPDX-License-Identifier: MIT
# SPDX-License-Identifier: PSF-2.0
# Copyright (c) 2021 The Pybricks Authors
#
# Portions of documentation copied from:
# https://raw.githubusercontent.com/micropython/micropython/1e6d18c915ccea0b6a19ffec9710d33dd7e5f866/docs/library/builtins.rst
# Copyright (c) 2014-2021, Damien P. George, Paul Sokolovsky, and contributors
#
# Portions of the documentation copied from:
# https://docs.python.org/3/library/builtins.html
# https://docs.python.org/3/library/constants.html
# https://docs.python.org/3/library/stdtypes.html
# https://docs.python.org/3/library/exceptions.html
# Copyright (c) 2001-2021 Python Software Foundation

"""
Les fonctions et exceptions suivantes peuvent être utilisées sans rien importer.

La plupart des fonctions et classes de ce module n'acceptent pas d'arguments nommés.
"""

from typing import (
    Any,
    Callable,
    Dict,
    Hashable,
    Iterable,
    Iterator,
    List,
    Literal,
    Mapping,
    Sequence,
    SupportsComplex,
    SupportsFloat,
    SupportsInt,
    Tuple,
    TypeVar,
    Union,
    overload,
)

import uio
import usys


# These get overridden later on, but we still want to use the originals
# for the purpose of typing the doc strings.
_bool = bool
_bytearray = bytearray
_bytes = bytes
_callable = callable
_classmethod = classmethod
_complex = complex
_dict = dict
_float = float
_int = int
_str = str
_type = type

_Self = TypeVar("_Self")

# Functions and types


def abs(x: Any) -> Any:
    """abs(x) -> Any

    Retourne la valeur absolue d'un nombre.

    L'argument peut être un entier, un
    nombre à virgule flottante, ou tout objet implémentant ``__abs__()``.
    Si l'argument est un nombre complexe, sa magnitude est retournée.

    Arguments:
        x (Any): La valeur.

    Retourne :
        Valeur absolue de ``x``.
    """


def all(x: Iterable) -> _bool:
    """all(x) -> bool

    Vérifie si tous les éléments de l'itérable sont vrais.

    Équivalent à ::

        def all(x):
            for element in x:
                if not element:
                    return False
            return True

    Arguments:
        x (Iterable): L'itérable à vérifier.

    Retourne :
        ``True`` si l'itérable ``x`` est vide ou si tous les éléments
        sont vrais. Sinon ``False``.
    """


def any(x: Iterable) -> _bool:
    """any(x) -> bool

    Vérifie si au moins un élément de l'itérable est vrai.

    Équivalent à ::

        def any(x):
            for element in x:
                if element:
                    return True
            return False

    Arguments:
        x (Iterable): L'itérable à vérifier.

    Retourne :
        ``True`` si au moins un élément dans ``x`` est vrai. Sinon ``False``.
    """


def bin(x: Any) -> _str:
    """bin(x) -> str

    Convertit un entier en sa représentation binaire. Le résultat est une
    chaîne de caractères préfixée par ``0b``. Le résultat est une expression Python valide.
    Par exemple, ``bin(5)`` donne ``"0b101"``.

    Arguments:
        x (int): Valeur à convertir.

    Retourne :
        Une chaîne représentant la forme binaire de l'entrée.
    """


class bool:
    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, x: Any) -> None:
        ...

    def __init__(self, *args) -> None:
        """
        bool(​)
        bool(x)

        Crée une valeur booléenne, qui est soit ``True`` soit ``False``.

        La valeur d'entrée est convertie en utilisant la procédure standard de test de vérité.
        Si aucune valeur d'entrée n'est donnée, elle est supposée être ``False``.

        Arguments:
            x: Valeur à convertir.

        Retourne :
            Résultat du test de vérité.
        """


class bytes:
    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, source: _int) -> None:
        ...

    @overload
    def __init__(self, source: Union[_bytes, _bytearray, Iterable[_int]]) -> None:
        ...

    @overload
    def __init__(self, source: _str, encoding: _str) -> None:
        ...

    def __init__(self, *args):
        r"""
        bytes(​)
        bytes(integer)
        bytes(iterable)
        bytes(string, encoding)

        Crée un nouvel objet ``bytes``, qui est une séquence d'entiers
        dans la plage :math:`0 \leq x \leq 255`. Cet objet est *immutable*,
        ce qui signifie que vous *ne pouvez pas* changer son contenu après l'avoir créé.

        Si aucun argument n'est donné, cela crée un objet ``bytes`` vide.

        Arguments:
            integer (int): Si l'argument est un seul entier, cela crée
              un objet ``bytes`` de zéros. L'argument spécifie combien.
            iterable (iter): Si l'argument est un objet ``bytearray``, ``bytes``
              ou un autre itérable d'entiers, cela crée un objet ``bytes``
              avec la même séquence d'octets que l'argument.
            string (str): Si l'argument est une chaîne, cela crée un objet ``bytes``
              contenant la chaîne encodée.
            encoding (str): Spécifie quel encodage utiliser pour l'argument ``string``.
              Seul ``"utf-8"`` est pris en charge.
        """


class bytearray:
    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, source: _int) -> None:
        ...

    @overload
    def __init__(self, source: Union[_bytes, _bytearray, _str, Iterable[_int]]) -> None:
        ...

    def __init__(self, *args):
        r"""
        bytearray(​)
        bytearray(integer)
        bytearray(iterable)
        bytearray(string)

        Crée un nouvel objet ``bytearray``, qui est une séquence d'entiers
        dans la plage :math:`0 \leq x \leq 255`. Cet objet est *mutable*, ce qui
        signifie que vous *pouvez* changer son contenu après l'avoir créé.

        Si aucun argument n'est donné, cela crée un objet ``bytearray`` vide.

        Arguments:
            integer (int): Si l'argument est un seul entier, cela crée
              un objet ``bytearray`` de zéros. L'argument spécifie combien.
            iterable (iter): Si l'argument est un objet ``bytearray``, ``bytes``
              ou un autre itérable d'entiers, cela crée
              un objet ``bytearray`` avec la même séquence d'octets que l'argument.
            string (str): Si l'argument est une chaîne, cela crée
              un objet ``bytearray`` contenant la chaîne encodée.
        """


def callable(object: Any) -> _bool:
    """
    callable(object) -> bool

    Vérifie si un objet est appelable.

    Arguments:
        object: Objet à vérifier.

    Retourne :
        ``True`` si l'argument objet semble appelable, ``False`` sinon.
    """


def chr(x: _int) -> _str:
    """chr(x) -> str

    Retourne la chaîne représentant un caractère dont le code Unicode est l'entier ``x``.
    C'est l'inverse de :meth:`ord`. Par exemple, ``chr(97)`` donne ``"a"``.

    Arguments:
        x (int): Valeur à convertir (0-255).

    Retourne :
        Une chaîne avec un caractère, correspondant à la valeur Unicode donnée.
    """


def classmethod(method: _callable) -> _callable:
    """
    Transforme une méthode en méthode de classe.
    """


class complex:
    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(
        self, real: Union[_float, SupportsFloat, _complex, SupportsComplex]
    ) -> None:
        ...

    @overload
    def __init__(
        self,
        real: Union[_float, SupportsFloat, _complex, SupportsComplex],
        imag: Union[_float, SupportsFloat, _complex, SupportsComplex],
    ) -> None:
        ...

    @overload
    def __init__(self, value: _str) -> None:
        ...

    def __init__(self, *args) -> None:
        """
        complex(string)
        complex(a=0, b=0)

        Crée un nombre complexe à partir d'une chaîne ou d'une paire de nombres.

        Si une chaîne est donnée, elle doit être de la forme ``'1+2j'``.
        Si une paire de nombres est fournie, le résultat est calculé
        comme : ``a + b * j``.

        Arguments:
            string (str): Une chaîne de la forme ``'1+2j'``.
            a (float ou complex): Un nombre réel ou complexe.
            b (float ou complex): Un nombre réel ou complexe.

        Retourne :
            Le nombre complexe résultant.
        """


class dict:
    @overload
    def __init(self) -> None:
        ...

    @overload
    def __init(self, **kwargs) -> None:
        ...

    def __init__(self, *args, **kwargs) -> None:
        """
        dict(**kwargs)
        dict(mapping, **kwargs)
        dict(iterable, **kwargs)

        Crée un objet dictionnaire.

        Voir la documentation standard
        `Python <https://docs.python.org/3/library/stdtypes.html#mapping-types-dict>`_
        pour une référence complète avec des exemples.
        """


@overload
def dir() -> List[_str]:
    ...


@overload
def dir(object: Any) -> List[_str]:
    ...


def dir(*args) -> List[_str]:
    """
    dir() -> List[str]
    dir(object) -> List[str]

    Obtient une liste d'attributs d'un objet.

    Si aucun argument objet n'est donné, cette fonction obtient la liste des noms dans le
    scope local actuel.

    Arguments:
        object: Objet à vérifier pour les attributs valides.

    Retourne :
        Liste des attributs de l'objet ou liste des noms dans le scope local actuel.
    """


@overload
def divmod(a: _int, b: _int) -> Tuple[_int, _int]:
    ...


@overload
def divmod(a: _float, b: _float) -> Tuple[_float, _float]:
    ...


def divmod(a, b):
    """
    divmod(a, b) -> Tuple[int, int]

    Obtient le quotient et le reste pour la division de deux entiers.

    Voir la documentation standard `Python divmod
    <https://docs.python.org/3/library/functions.html#divmod>`_ pour
    le comportement attendu lorsque ``a`` ou ``b`` sont des nombres à virgule flottante
    à la place.

    Arguments:
        a (int): Numérateur.
        b (int): Dénominateur.

    Retourne :
        Un tuple avec le quotient ``a // b`` et le reste ``a % b``.
    """


class enumerate:
    @overload
    def __init__(self, iterable: Iterable) -> None:
        ...

    @overload
    def __init__(self, iterable: Iterable, start: _int) -> None:
        ...

    def __init__(self, *args) -> None:
        """
        enumerate(iterable, start=0)

        Énumère un itérateur existant en ajoutant un index numérique.

        Cette fonction est équivalente à ::

            def enumerate(sequence, start=0):
                n = start
                for elem in sequence:
                    yield n, elem
                    n += 1
        """


@overload
def eval(expression: _str) -> Any:
    ...


@overload
def eval(expression: _str, globals: _dict) -> Any:
    ...


@overload
def eval(expression: _str, globals: _dict, locals: Mapping) -> Any:
    ...


def eval(*args):
    """
    eval(expression) -> Any
    eval(expression, globals) -> Any
    eval(expression, globals, locals) -> Any

    Évalue le résultat d'une expression.

    Les erreurs de syntaxe sont signalées comme des exceptions.

    Arguments:
        expression (str): Expression à évaluer.
        globals (dict): Si donné, cela contrôle quelles fonctions sont disponibles
            pour être utilisées dans l'expression. Par défaut, le scope global est accessible.
        locals (dict): Si donné, cela contrôle quelles fonctions sont disponibles
            pour être utilisées dans l'expression. Par défaut, le même que ``globals``.

    Retourne :
        La valeur obtenue en exécutant l'expression.
    """


@overload
def exec(object: Any) -> None:
    ...


@overload
def exec(object: Any, globals: _dict) -> None:
    ...


@overload
def exec(object: Any, globals: _dict, locals: Mapping) -> None:
    ...


def exec(*args):
    """
    exec(expression)
    exec(expression, globals)
    exec(expression, globals, locals)

    Exécute du code MicroPython.

    Les erreurs de syntaxe sont signalées comme des exceptions.

    Arguments:
        expression (str): Code à exécuter.
        globals (dict): Si donné, cela contrôle quelles fonctions sont disponibles
            pour être utilisées dans l'expression. Par défaut, le scope global est accessible.
        locals (dict): Si donné, cela contrôle quelles fonctions sont disponibles
            pour être utilisées dans l'expression. Par défaut, le même que ``globals``.
    """


class float:
    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, x: _int) -> None:
        ...

    @overload
    def __init__(self, x: SupportsFloat) -> None:
        ...

    @overload
    def __init__(self, x: _str) -> None:
        ...

    def __init__(self, *args) -> None:
        """float(x=0.0)

        Crée un nombre à virgule flottante à partir d'un objet donné.

        Arguments:
            x (int ou float ou str): Nombre ou chaîne à convertir.
        """


@overload
def getattr(object: Any, name: _str) -> Any:
    ...


@overload
def getattr(object: Any, name: _str, default: Any) -> Any:
    ...


def getattr(*args):
    """
    getattr(object, name) -> Any
    getattr(object, name, default) -> Any

    Recherche l'attribut appelé ``name`` dans l'objet donné ``object``.

    Arguments:
        object: Objet dans lequel rechercher l'attribut.
        name (str): Nom de l'attribut.
        default: Objet à retourner si l'attribut n'est pas trouvé.

    Retourne :
        Retourne la valeur de l'attribut nommé.
    """


def globals() -> Dict[_str, Any]:
    """
    globals() -> dict

    Obtient un dictionnaire représentant la table des symboles globaux actuelle.

    Retourne :
        Le dictionnaire des globaux.
    """


def hasattr(object: Any, name: _str) -> _bool:
    """
    hasattr(object, name) -> bool

    Vérifie si un attribut existe sur un objet.

    Arguments:
        object: Objet dans lequel rechercher l'attribut.
        name (str): Nom de l'attribut.

    Retourne :
        ``True`` si un attribut de ce nom existe, ``False`` sinon.
    """


def hash(object: Any) -> _int:
    """
    hash(object) -> int

    Obtient la valeur de hachage d'un objet, si l'objet le prend en charge.

    Arguments:
        object: Objet pour lequel obtenir une valeur de hachage.

    Retourne :
        La valeur de hachage.
    """


@overload
def help() -> None:
    ...


@overload
def help(object: Any) -> None:
    ...


def help(*args) -> None:
    """
    help()
    help(object)

    Obtenir des informations sur un objet.

    Si aucun argument n'est donné, cette fonction imprime des instructions pour utiliser le
    REPL. Si l'argument est ``"modules"``, elle imprime les modules disponibles.

    Arguments:
        object: Objet pour lequel imprimer des informations d'aide.
    """


def hex(x: int) -> _str:
    """hex(x) -> str

    Convertit un entier en sa représentation hexadécimale. Le résultat est une
    chaîne en minuscules préfixée par ``0x``. Le résultat est une expression Python
    valide. Par exemple, ``hex(25)`` donne ``"0x19"``.

    Arguments:
        x (int): Valeur à convertir.

    Retourne :
        Une chaîne représentant la forme hexadécimale de l'entrée.
    """


def id(object: Any) -> _int:
    """
    id(object) -> int

    Obtient l'*identité* d'un objet. C'est un entier qui est garanti
    unique et constant pour cet objet pendant sa durée de vie.

    Arguments:
        object: Objet dont obtenir l'identifiant.

    Retourne :
        L'identifiant.
    """


@overload
def input() -> _str:
    ...


@overload
def input(prompt: _str) -> _str:
    ...


def input(*args) -> _str:
    """input() -> str
    input(prompt) -> str

    Obtient une entrée de l'utilisateur dans la fenêtre du terminal. Il attend jusqu'à ce que
    l'utilisateur appuie sur :kbd:`Enter`.

    Arguments:
        prompt (str): Si donné, cela est imprimé d'abord dans la fenêtre du terminal.
            Cela peut être utilisé pour poser une question afin que l'utilisateur sache quoi taper.

    Retourne :
        Tout ce que l'utilisateur a tapé avant d'appuyer sur :kbd:`Enter`.
    """


class int:
    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, x: _str) -> None:
        ...

    @overload
    def __init__(self, x: _str, base: _int) -> None:
        ...

    @overload
    def __init__(self, x: Union[_int, SupportsInt]) -> None:
        ...

    def __init__(self, *args) -> None:
        """int(x=0)

        Crée un entier.

        Arguments:
            x (int ou float ou str): Objet à convertir.
        """

    def to_bytes(self, length: _int, byteorder: Literal["little", "big"]) -> _bytes:
        """
        to_bytes(length, byteorder) -> bytes

        Obtient une représentation en :class:`bytes` de l'entier.

        Arguments:
            length (int): Combien d'octets utiliser.
            byteorder (str): Choisissez ``"big"`` pour mettre l'octet le plus significatif
                en premier. Choisissez ``"little"`` pour mettre l'octet le moins significatif
                en premier.

        Retourne :
            Séquence d'octets qui représente l'entier.
        """

    @_classmethod
    def from_bytes(cls, _bytes: _bytes, byteorder: Literal["little", "big"]) -> _int:
        """from_bytes(bytes, byteorder) -> int

        Convertit une séquence d'octets en le nombre qu'elle représente.

        Arguments:
            bytes (bytes): Les octets à convertir.
            byteorder (str): Choisissez ``"big"`` si l'octet le plus significatif est
                le premier élément. Choisissez ``"little"`` si l'octet le moins significatif
                est le premier élément.

        Retourne :
            Le nombre représenté par les octets.
        """


def isinstance(object: Any, classinfo: Union[_type, Tuple[_type]]) -> _bool:
    """
    isinstance(object, classinfo) -> bool

    Vérifie si un objet est une instance d'une certaine classe.

    Arguments:
        object: Objet dont vérifier le type.
        classinfo (type ou tuple): Informations sur la classe.

    Retourne :
        ``True`` si l'argument ``object`` est une instance de l'argument ``classinfo``
        ou d'une sous-classe de celui-ci.
    """


def issubclass(cls: _type, classinfo: Union[_type, Tuple[_type]]) -> _bool:
    """
    issubclass(cls, classinfo) -> bool

    Vérifie si une classe est une sous-classe d'une autre classe.

    Arguments:
        cls: Type de classe.
        classinfo (type ou tuple): Informations sur la classe.

    Retourne :
        ``True`` si ``cls`` est une sous-classe de ``classinfo``.
    """


def iter(object: Union[Iterable, Sequence]) -> Iterator:
    """
    iter(object) -> Iterator

    Obtient l'itérateur de l'objet si disponible.

    Arguments:
        object: Objet pour lequel obtenir l'itérateur.

    Retourne :
        L'itérateur.
    """


def len(s: Sequence) -> _int:
    """
    len(s) -> int

    Obtient la longueur (le nombre d'éléments) d'un objet.

    Arguments:
        s (Sequence): La séquence dont obtenir la longueur.

    Retourne :
        La longueur.
    """


class list:
    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, iterable: Iterable) -> None:
        ...

    def __init__(self, *args) -> None:
        """
        list(​)
        list(iterable)

        Crée une nouvelle liste. Si aucun argument n'est donné, cela crée un
        objet ``list`` vide.

        Une liste est *mutable*, ce qui signifie que vous *pouvez* changer son contenu
        après l'avoir créée.

        Arguments:
            iterable (iter): Itérable à partir duquel construire la liste.
        """


def locals() -> _dict:
    """
    locals() -> dict

    Obtient un dictionnaire représentant la table des symboles locaux actuelle.

    Retourne :
        Le dictionnaire des locaux.
    """


def map(function: Callable, iterable: Iterable, *args: Any) -> Iterator:
    """
    map(function, iterable) -> Iterator
    map(function, iterable1, iterable2...) -> Iterator

    Crée un nouvel itérateur qui applique la fonction donnée à chaque élément de
    l'itérable donné et renvoie les résultats.

    Arguments:
        function (callable): Fonction qui calcule un résultat pour un élément de
            l'itérable(s). Le nombre d'arguments de cette fonction doit correspondre
            au nombre d'itérables donnés.
        iterable (iter): Un ou plusieurs itérables sources à partir desquels tirer des données.
            Avec plusieurs itérables, l'itérateur s'arrête lorsque le plus court
            itérable est épuisé.

    Retourne :
        Le nouvel itérateur mappé.
    """


@overload
def max(iterable: Iterable) -> Any:
    ...


@overload
def max(arg1: Any, arg2: Any, *args: Any) -> Any:
    ...


def max(*args):
    """
    max(iterable) -> Any
    max(arg1, arg2, ....) -> Any

    Obtient l'objet avec la plus grande valeur.

    L'argument peut être un seul itérable, ou n'importe quel nombre d'objets.

    Retourne :
        L'objet avec la plus grande valeur.
    """


@overload
def min(iterable: Iterable) -> Any:
    ...


@overload
def min(arg1: Any, arg2: Any, *args: Any) -> Any:
    ...


def min(*args):
    """
    min(iterable) -> Any
    min(arg1, arg2, ....) -> Any

    Obtient l'objet avec la plus petite valeur.

    L'argument peut être un seul itérable, ou n'importe quel nombre d'objets.

    Retourne :
        L'objet avec la plus petite valeur.
    """


def next(iterator: Iterator) -> Any:
    """
    next(iterator) -> Any

    Récupère l'élément suivant de l'itérateur en appelant sa méthode ``__next__()``.

    Arguments:
        iterator (iter): Objet générateur initialisé à partir duquel tirer la prochaine
            valeur.

    Retourne :
        La prochaine valeur du générateur.
    """


class object:
    def __init__(self) -> None:
        """
        Crée un nouvel objet sans caractéristiques.
        """


def oct(x: _int) -> _str:
    """oct(x) -> str

    Convertit un entier en sa représentation octale. Le résultat est une
    chaîne préfixée par ``0o``. Le résultat est une expression Python
    valide. Par exemple, ``oct(25)`` donne ``"0o31"``.

    Arguments:
        x (int): Valeur à convertir.

    Retourne :
        Une chaîne représentant la forme octale de l'entrée.
    """


# .. function:: open()


def ord(c: _str) -> _int:
    """ord(c) -> int

    Convertit une chaîne composée d'un caractère Unicode
    correspondant. C'est l'inverse de :meth:`chr`.

    Arguments:
        c (str): Caractère à convertir.

    Retourne :
        Nombre représentant le caractère (0--255).
    """


def pow(base: Union[_int, _float], exp: Union[_int, _float]) -> Union[_int, _float]:
    """
    pow(base, exp) -> Number

    Élève la base à l'exposant donné : :math:`\\text{base}^{\\mathrm{exp}}`.

    C'est la même chose que de faire ``base ** exp``.

    Arguments:
        base (Number): La base.
        exp (Number): L'exposant.

    Retourne :
        Le résultat.
    """


@overload
def print(*objects):
    ...


@overload
def print(*objects, sep: _str = " ", end: _str = "\n", file: uio.FileIO = usys.stdin):
    ...


def print(*args):
    """print(*objects, sep=" ", end="\\n", file=usys.stdin)

    Imprime du texte ou d'autres objets dans la fenêtre du terminal.

    Arguments:
        objects: Zéro ou plusieurs objets à imprimer.

    Arguments par mot-clé:
        sep (str): Ceci est imprimé entre les objets, s'il y en a plus d'un.
        end (str): Ceci est imprimé après le dernier objet.
        file (FileIO): Par défaut, le résultat est imprimé dans la fenêtre du terminal. Cet
              argument vous permet de l'imprimer dans un fichier à la place, si les fichiers sont
              pris en charge.
    """


class range:
    @overload
    def __init__(self, stop: _int) -> None:
        ...

    @overload
    def __init__(self, start: _int, stop: _int) -> None:
        ...

    @overload
    def __init__(self, start: _int, stop: _int, step: _int) -> None:
        ...

    def __init__(self, *args) -> None:
        """
        range(stop)
        range(start, stop)
        range(start, stop, step)

        Crée un générateur qui renvoie des valeurs de ``start`` à
        ``stop``, avec des incréments de ``step``.

        Arguments:
            start (int): Valeur de départ. Par défaut, ``0`` si un seul argument est donné.
            stop (int): Point de terminaison. Cette valeur n'est *pas* incluse.
            step (int): Incrément entre les valeurs. Par défaut, ``1`` si un seul
                ou deux arguments sont donnés.
        """


def repr(x: Any) -> _str:
    """repr(object) -> str

    Obtient la chaîne qui représente un objet.

    Arguments:
        x (object): Objet à convertir.

    Retourne :
        Représentation sous forme de chaîne implémentée par la méthode ``__repr__`` de l'objet.
    """


def reversed(seq: Sequence) -> Iterator:
    """
    reversed(seq) -> Iterator

    Obtient un itérateur qui renvoie les valeurs de la séquence dans l'ordre inverse, si
    pris en charge.

    Arguments:
        seq: Séquence à partir de laquelle tirer des échantillons.

    Retourne :
        Itérateur qui renvoie les valeurs dans l'ordre inverse, en commençant par la dernière valeur.
    """


@overload
def round(number: _float) -> _int:
    ...


@overload
def round(number: _float, ndigits: _int) -> _float:
    ...


def round(*args):
    """
    round(number) -> int
    round(number, ndigits) -> float

    Arrondit un nombre à un nombre donné de chiffres après la virgule.

    Si ``ndigits`` est omis ou ``None``, il renvoie l'entier le plus proche.

    L'arrondissement avec un ou plusieurs chiffres après la virgule ne tronquera pas toujours
    les zéros de fin. Pour imprimer des nombres joliment, formatez les chaînes à la place ::

        # imprimer deux décimales
        print('mon nombre: %.2f' % number)
        print('mon nombre: {:.2f}'.format(number))
        print(f'mon nombre: {number:.2f}')

    Arguments:
        number (float): Le nombre à arrondir.
        ndigits (int): Le nombre de chiffres restant après la virgule.
    """


class set:
    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, iterable: Iterable[Hashable]) -> None:
        ...

    def __init__(self, *args) -> None:
        """
        set()
        set(iterable)

        Crée un nouvel ensemble.

        Sans arguments, crée un nouvel ensemble vide, sinon crée un ensemble
        contenant des éléments uniques de *iterable*.

        Les ensembles peuvent également être créés en utilisant un littéral d'ensemble ::

            mon_ensemble = {1, 2, 3}

        Les éléments d'un ensemble doivent être hachables. Il n'y a que quelques types, comme
        :class:`list` qui ne sont pas hachables.

        Arguments:
            iterable: Un itérable d'objets hachables.
        """

    def copy(self: _Self) -> _Self:
        """
        copy() -> set

        Renvoie une copie superficielle de l'ensemble.

        Retourne :
            Un nouvel ensemble.
        """

    def difference(self: _Self, *others: set) -> _Self:
        """
        difference(other1, other2, ...) -> set

        Renvoie un nouvel ensemble avec des éléments qui ne sont dans aucun des autres ensembles.

        La différence peut également être calculée en utilisant l'opérateur ``-`` ::

            diff = s - other

        Arguments:
            others: 1 ou plusieurs autres ensembles.

        Retourne :
            Un nouvel ensemble.
        """

    def intersection(self: _Self, *others: set) -> _Self:
        """
        intersection(other1, other2, ...) -> set

        Renvoie un nouvel ensemble avec des éléments communs entre cet ensemble et
        tous les autres ensembles.

        L'intersection peut également être calculée en utilisant l'opérateur ``&`` ::

            intersect = s & other

        Arguments:
            others: 1 ou plusieurs autres ensembles.

        Retourne :
            Un nouvel ensemble.
        """

    def isdisjoint(self, other: set) -> bool:
        """
        isdisjoint(other) -> bool

        Teste si un ensemble et *other* n'ont aucun élément en commun.

        Arguments:
            other: Un autre ensemble.

        Retourne :
            ``True`` si cet ensemble n'a aucun élément en commun avec *other*,
            sinon ``False``.
        """

    def issubset(self, other: set) -> bool:
        """
        issubset(other) -> bool

        Teste si un ensemble est un sous-ensemble de *other*.

        Le test peut également être effectué en utilisant l'opérateur ``<=`` ::

            if s <= other:
                # s est un sous-ensemble de other
                ...

        Arguments:
            other: Un autre ensemble.

        Retourne :
            ``True`` si cet ensemble est un sous-ensemble de *other*, sinon ``False``.
        """

    def issuperset(self, other: set) -> bool:
        """
        issuperset(other) -> bool

        Teste si un ensemble est un sur-ensemble de *other*.

        Le test peut également être effectué en utilisant l'opérateur ``>=`` ::

            if s >= other:
                # s est un sur-ensemble de other
                ...

        Arguments:
            other: Un autre ensemble.

        Retourne :
            ``True`` si cet ensemble est un sur-ensemble de *other*, sinon ``False``.
        """

    def symmetric_difference(self: _Self, other: set) -> _Self:
        """
        symmetric_difference(other) -> bool

        Renvoie un nouvel ensemble avec des éléments dans un ensemble ou l'autre mais pas dans les deux.

        La différence symétrique peut également être calculée en utilisant l'opérateur ``^`` ::

            diff = s ^ other

        Arguments:
            other: Un autre ensemble.

        Retourne :
            Un nouvel ensemble.
        """

    def union(self: _Self, *others: set) -> _Self:
        """
        union(other1, other2, ...) -> set

        Renvoie un nouvel ensemble avec des éléments de cet ensemble et de tous les autres ensembles.

        L'union peut également être calculée en utilisant l'opérateur ``|`` ::

            u = s | other

        Arguments:
            others: 1 ou plusieurs autres ensembles.

        Retourne :
            Un nouvel ensemble.
        """

    def __contains__(self, item: Hashable) -> bool:
        ...

    def __len__(self) -> int:
        ...

    def __bool__(self) -> bool:
        ...

    def __gt__(self, other: set) -> bool:
        ...

    def __lt__(self, other: set) -> bool:
        ...

    def __ge__(self, other: set) -> bool:
        ...

    def __le__(self, other: set) -> bool:
        ...

    def __eq__(self, other: set) -> bool:
        ...

    def __ne__(self, other: set) -> bool:
        ...

    def __sub__(self: _Self, other: set) -> _Self:
        ...

    def __and__(self: _Self, other: set) -> _Self:
        ...

    def __or__(self: _Self, other: set) -> _Self:
        ...

    def __xor__(self: _Self, other: set) -> _Self:
        ...


def setattr(object: Any, name: _str, value: Any) -> None:
    """
    setattr(object, name, value)

    Assigne une valeur à un attribut, à condition que l'objet le permette.

    C'est le pendant de :meth:`getattr`.

    Arguments:
        object: Objet dans lequel stocker l'attribut.
        name (str): Nom de l'attribut.
        value: Valeur à stocker.
    """


class slice:
    @overload
    def __init__(self, stop: _int) -> None:
        ...

    @overload
    def __init__(self, start: _int, stop: _int) -> None:
        ...

    @overload
    def __init__(self, start: _int, stop: _int, step: _int) -> None:
        ...

    def __init__(self, *args) -> None:
        """
        slice(​)

        La création d'instances de cette classe n'est pas prise en charge.

        Utilisez plutôt la syntaxe d'indexation. Par
        exemple : ``a[start:stop:step]`` ou ``a[start:stop, i]``.
        """


def sorted(iterable: Iterable, key=None, reverse=False) -> List:
    """
    Trie les objets.

    Arguments:
        iterable (iter): Objets à trier. Cela peut également être un générateur qui
            renvoie un nombre fini d'objets.
        key (callable): Fonction ``def(item) -> int`` qui mappe un objet à une
            valeur numérique. Cela est utilisé pour déterminer l'ordre des éléments triés.
        reverse (bool): Si trié en ordre inverse, en mettant la valeur la plus élevée
            en premier.

    Retourne :
        Une nouvelle liste avec les éléments triés.
    """


def staticmethod(method: _callable) -> _callable:
    """
    Transforme une méthode en méthode statique.
    """


class str:
    @overload
    def __init__(self, object: Any = "") -> None:
        ...

    @overload
    def __init__(
        self, object: _bytes = b"", encoding: _str = "utf-8", errors: _str = "strict"
    ) -> None:
        ...

    def __init__(self) -> None:
        """
        str(​)
        str(object)
        str(object, encoding)

        Obtient la représentation sous forme de chaîne d'un objet.

        Si aucun argument n'est donné, cela crée un objet ``str`` vide.

        Arguments:
            object: Si seul cet argument est donné, cela renvoie la représentation
              sous forme de chaîne de l'objet.
            encoding (str): Si le premier argument est un objet ``bytearray`` ou ``bytes``
              et que l'argument encoding est ``"utf-8"``, cela décodera
              les données d'octets pour obtenir une représentation sous forme de chaîne.
        """


@overload
def sum(iterable: Iterable) -> _int:
    ...


@overload
def sum(iterable: Iterable, start: _int) -> _int:
    ...


def sum(*args):
    """
    sum(iterable) -> Number
    sum(iterable, start) -> Number

    Additionne les éléments de l'itérable et la valeur de départ.

    Arguments:
        iterable (iter): Valeurs à additionner, en commençant par la première valeur.
        start (Number): Valeur ajoutée au total.

    Retourne :
        La somme totale.
    """


@overload
def super() -> _type:
    ...


@overload
def super(type: _type) -> _type:
    ...


@overload
def super(type: _type, object_or_type: Any) -> _type:
    ...


def super(*args):
    """
    super() -> type
    super(type) -> type
    super(type, object_or_type) -> type

    Obtient un objet qui délègue les appels de méthode à un parent, ou une classe sœur
    du type donné.

    Retourne :
        L'objet `super()` correspondant.
    """


class tuple:
    @overload
    def __init__(self):
        ...

    @overload
    def __init__(self, iterable: Iterable):
        ...

    def __init__(self, *args) -> None:
        """
        tuple(​)
        tuple(iterable)

        Crée un nouveau tuple. Si aucun argument n'est donné, cela crée un
        objet ``tuple`` vide.

        Un tuple est *immutable*, ce qui signifie que vous *ne pouvez pas* changer son
        contenu après l'avoir créé.

        Arguments:
            iterable (iter): Itérable à partir duquel construire le tuple.
        """


class type:
    def __init__(self, object: Any) -> None:
        """type(object)

        Obtient le type d'un objet. Cela peut être utilisé pour vérifier si un objet
        est une instance d'une classe particulière.

        Arguments:
            object: Objet dont vérifier le type.
        """


def zip(*iterables: Iterable) -> Iterable[Tuple]:
    """
    zip(iter_a, iter_b, ...) -> Iterable[Tuple]

    Renvoie un itérateur de tuples, où le *i*-ème tuple contient le *i*-ème
    élément de chacune des séquences ou itérables d'argument. L'itérateur
    s'arrête lorsque le plus court itérable d'entrée est épuisé.

    Avec un seul argument itérable, il renvoie un itérateur de 1-tuples.
    Sans arguments, il renvoie un itérateur vide.

    Cette fonctionnalité est équivalente à ::

        def zip(*iterables):
            sentinel = object()
            iterators = [iter(it) for it in iterables]
            while iterators:
                result = []
                for it in iterators:
                    elem = next(it, sentinel)
                    if elem is sentinel:
                        return
                    result.append(elem)
                yield tuple(result)

    Arguments:
        iter_a (iter): Le premier itérable. Cela fournit la première valeur pour
            chacun des tuples renvoyés.
        iter_b (iter): Le deuxième itérable. Cela fournit la deuxième valeur dans
            chacun des tuples renvoyés. Et ainsi de suite.

    Retourne :
        Un nouvel itérateur qui renvoie des tuples contenant les valeurs des
        itérables individuels.
    """


# base exceptions


class BaseException:
    """
    La classe de base pour toutes les exceptions intégrées.

    Elle n'est pas destinée à être directement héritée par des classes définies par l'utilisateur (pour cela,
    utilisez :class:`Exception`).
    """

    args: Tuple
    """
    Le tuple des arguments donnés au constructeur de l'exception.
    """


class Exception(BaseException):
    """
    Toutes les exceptions intégrées sont dérivées de cette classe.

    Toutes les exceptions définies par l'utilisateur doivent également être dérivées de cette classe.
    """


class ArithmeticError(Exception):
    """
    La classe de base pour les exceptions intégrées qui sont levées pour diverses
    erreurs arithmétiques.
    """


class LookupError(Exception):
    """
    La classe de base pour les exceptions qui sont levées lorsqu'une clé ou un index utilisé
    sur une correspondance ou une séquence est invalide.
    """


# concrete exceptions


class AssertionError(Exception):
    """
    Levée lorsqu'une instruction assert échoue.
    """


class AttributeError(Exception):
    """
    Levée lorsqu'une référence ou une affectation d'attribut échoue.
    """


class EOFError(Exception):
    """
    Levée lorsque la fonction :meth:`input` rencontre une condition de fin de fichier (EOF)
    sans lire de données.
    """


class GeneratorExit(BaseException):
    """
    Levée lorsqu'un générateur ou une coroutine est fermé.
    """


class ImportError(Exception):
    """
    Levée lorsque l'instruction ``import`` est incapable de charger un module.
    """


class IndentationError(SyntaxError):
    """
    Classe de base pour les erreurs de syntaxe liées à une indentation incorrecte.
    """


class IndexError(LookupError):
    """
    Levée lorsqu'un sous-script de séquence est hors de portée.
    """


class KeyError(LookupError):
    """
    Levée lorsqu'une clé de correspondance (dictionnaire) n'est pas trouvée dans l'ensemble des clés existantes.
    """


class KeyboardInterrupt(BaseException):
    """
    Levée lorsque l'utilisateur appuie sur la touche d'interruption (normalement :kbd:`Ctrl` :kbd:`C`).
    """


class MemoryError(Exception):
    """
    Levée lorsqu'une opération manque de mémoire.
    """


class NameError(Exception):
    """
    Levée lorsqu'un nom local ou global n'est pas trouvé.
    """


class NotImplementedError(RuntimeError):
    """
    Dans les classes de base définies par l'utilisateur, les méthodes abstraites doivent lever cette exception
    lorsqu'elles nécessitent que les classes dérivées remplacent la méthode, ou pendant que la
    classe est en cours de développement pour indiquer que la véritable implémentation doit encore
    être ajoutée.
    """


class OSError(Exception):
    """
    Cette exception est levée par le firmware, qui est
    le système d'exploitation qui s'exécute sur le hub.
    Par exemple, il
    lève une ``OSError`` si vous appelez ``Motor(Port.A)`` lorsqu'il n'y a pas de
    moteur sur le port A.
    """

    errno: _int
    """
    Spécifie quel type de ``OSError`` s'est produit, comme indiqué dans le
    module :mod:`uerrno`.
    """


class OverflowError(ArithmeticError):
    """
    Levée lorsque le résultat d'une opération arithmétique est trop grand pour être représenté.
    """


class RuntimeError(Exception):
    """
    Levée lorsqu'une erreur est détectée qui ne relève d'aucune des autres catégories.

    La valeur associée est une chaîne indiquant ce qui a précisément mal tourné.
    """


class StopIteration(Exception):
    """
    Levée par la fonction intégrée :meth:`next` et la méthode ``__next__()`` d'un itérateur
    pour signaler qu'il n'y a plus d'éléments produits par l'itérateur.

    Les fonctions génératrices doivent retourner au lieu de lever cette exception directement.
    """


class SyntaxError(Exception):
    """
    Levée lorsque l'analyseur rencontre une erreur de syntaxe.
    """


class SystemExit(BaseException):
    """
    Levée lorsque vous appuyez sur le bouton d'arrêt sur le hub ou dans l'application Pybricks Code.
    """


class TypeError(Exception):
    """
    Levée lorsqu'une opération ou une fonction est appliquée à un objet de type inapproprié.
    """


class ValueError(Exception):
    """
    Levée lorsqu'une opération ou une fonction reçoit un argument qui a le bon
    type mais une valeur inappropriée. Cela est utilisé lorsque la situation n'est
    pas décrite par une exception plus précise telle que :class:`IndexError`.
    """


class ZeroDivisionError(ArithmeticError):
    """
    Levée lorsque le deuxième argument d'une opération de division ou de modulo est zéro.
    """
