# SPDX-License-Identifier: MIT
# Copyright (c) 2018-2023 The Pybricks Authors

"""Module de robotique pour l'API Pybricks."""

from __future__ import annotations

from typing import Tuple, Optional, overload, TYPE_CHECKING

from . import _common
from .parameters import Stop

if TYPE_CHECKING:
    from ._common import Motor, MaybeAwaitable
    from .parameters import Number


class DriveBase:
    """Un véhicule robotique avec deux roues motrices et une roue de support
    ou roulette optionnelle.

    En spécifiant les dimensions de votre robot, cette classe
    facilite la conduite sur une distance donnée en millimètres ou le virage
    d'un nombre donné de degrés.

    Les distances, rayons ou vitesses de conduite **positifs** signifient
    conduire **vers l'avant**. **Négatif** signifie **vers l'arrière**.

    Les angles et taux de virage **positifs** signifient tourner **à droite**.
    **Négatif** signifie **à gauche**. Donc, vu de dessus,
    positif signifie dans le sens des aiguilles d'une montre et négatif signifie dans le sens inverse des aiguilles d'une montre.

    Voir la section `measuring`_ pour des conseils sur la mesure et l'ajustement des valeurs de diamètre
    et d'écartement des essieux.
    """

    distance_control = _common.Control()
    """La distance parcourue et la vitesse de conduite sont contrôlées par un PID
    contrôleur. Vous pouvez utiliser cet attribut pour changer ses paramètres.
    Voir l'attribut :ref:`motor control <settings>` pour un aperçu des
    méthodes disponibles. L'attribut ``distance_control`` a la même
    fonctionnalité, mais les paramètres s'appliquent à chaque millimètre parcouru par la
    base mobile, au lieu des degrés tournés par un moteur."""

    heading_control = _common.Control()
    """L'angle de rotation du robot et le taux de virage sont contrôlés par un PID
    contrôleur. Vous pouvez utiliser cet attribut pour changer ses paramètres.
    Voir l'attribut :ref:`motor control <settings>` pour un aperçu des
    méthodes disponibles. L'attribut ``heading_control`` a la même
    fonctionnalité, mais les paramètres s'appliquent à chaque degré de rotation de la
    base mobile entière (vue de dessus) au lieu des degrés tournés par un
    moteur."""

    def __init__(
        self,
        left_motor: Motor,
        right_motor: Motor,
        wheel_diameter: Number,
        axle_track: Number,
    ):
        """DriveBase(left_motor, right_motor, wheel_diameter, axle_track)

        Arguments:
            left_motor (Motor):
                Le moteur qui entraîne la roue gauche.
            right_motor (Motor):
                Le moteur qui entraîne la roue droite.
            wheel_diameter (Number, mm): Diamètre des roues.
            axle_track (Number, mm): Distance entre les points où
                les deux roues touchent le sol.
        """

    def drive(self, speed: Number, turn_rate: Number) -> None:
        """drive(speed, turn_rate)

        Commence à conduire à la vitesse et au taux de virage spécifiés. Les deux valeurs sont
        mesurées au point central entre les roues du robot.

        Arguments:
            speed (Number, mm/s): Vitesse du robot.
            turn_rate (Number, deg/s): Taux de virage du robot.
        """

    def stop(self) -> None:
        """stop()

        Arrête le robot en laissant les moteurs tourner librement."""

    def brake(self) -> None:
        """brake()

        Arrête le robot en freinant passivement les moteurs.
        """

    def distance(self) -> int:
        """distance() -> int: mm

        Obtient la distance parcourue estimée.

        Retourne :
            Distance parcourue depuis la dernière réinitialisation.
        """

    def angle(self) -> int:
        """angle() -> int: deg

        Obtient l'angle de rotation estimé de la base mobile.

        Retourne :
            Angle accumulé depuis la dernière réinitialisation.
        """

    def state(self) -> Tuple[int, int, int, int]:
        """state() -> Tuple[int, int, int, int]

        Obtient l'état du robot.

        Retourne :
            Tuple de la distance, de la vitesse de conduite, de l'angle et du taux de virage du robot.
        """

    def reset(self) -> None:
        """reset()

        Réinitialise la distance parcourue estimée et l'angle à 0."""

    @overload
    def settings(
        self,
        straight_speed: Optional[Number] = None,
        straight_acceleration: Optional[Number] = None,
        turn_rate: Optional[Number] = None,
        turn_acceleration: Optional[Number] = None,
    ) -> None: ...

    @overload
    def settings(self) -> Tuple[int, int, int, int]: ...

    def settings(self, *args):
        """
        settings(straight_speed, straight_acceleration, turn_rate, turn_acceleration)
        settings() -> Tuple[int, int, int, int]

        Configure la vitesse et l'accélération de la base mobile.

        Si vous ne donnez aucun argument, cela retourne les valeurs actuelles sous forme de tuple.

        Les valeurs initiales sont automatiquement configurées en fonction de votre diamètre
        de roue et de votre écartement des essieux. Elles sont sélectionnées de manière à ce que votre robot
        roule à environ 40% de sa vitesse maximale.

        Les valeurs de vitesse données ici ne s'appliquent pas à la méthode :meth:`.drive`,
        car vous fournissez vos propres valeurs de vitesse en tant qu'arguments dans cette méthode.

        Arguments:
            straight_speed (Number, mm/s): Vitesse en ligne droite du robot.
            straight_acceleration (Number, mm/s²): Accélération et décélération
                en ligne droite du robot. Fournissez un tuple avec
                deux valeurs pour définir l'accélération et la décélération séparément.
            turn_rate (Number, deg/s): Taux de virage du robot.
            turn_acceleration (Number, deg/s²): Accélération angulaire et
                décélération du robot. Fournissez un tuple avec
                deux valeurs pour définir l'accélération et la décélération séparément.
        """

    def straight(
        self, distance: Number, then: Stop = Stop.HOLD, wait: bool = True
    ) -> MaybeAwaitable:
        """straight(distance, then=Stop.HOLD, wait=True)

        Conduit en ligne droite sur une distance donnée, puis s'arrête.

        Arguments:
            distance (Number, mm): Distance à parcourir.
            then (Stop): Que faire après l'arrêt.
            wait (bool): Attendre que la manœuvre soit terminée avant de continuer
                         avec le reste du programme.
        """

    def turn(
        self, angle: Number, then: Stop = Stop.HOLD, wait: bool = True
    ) -> MaybeAwaitable:
        """turn(angle, then=Stop.HOLD, wait=True)

        Tourne sur place d'un angle donné, puis s'arrête.

        Arguments:
            angle (Number, deg): Angle du virage.
            then (Stop): Que faire après l'arrêt.
            wait (bool): Attendre que la manœuvre soit terminée avant de continuer
                         avec le reste du programme.
        """

    def curve(
        self, radius: Number, angle: Number, then: Stop = Stop.HOLD, wait: bool = True
    ) -> MaybeAwaitable:
        """curve(radius, angle, then=Stop.HOLD, wait=True)

        Conduit un arc le long d'un cercle d'un rayon donné, sur un angle donné.

        Arguments:
            radius (Number, mm): Rayon du cercle.
            angle (Number, deg): Angle le long du cercle.
            then (Stop): Que faire après l'arrêt.
            wait (bool): Attendre que la manœuvre soit terminée avant de continuer
                         avec le reste du programme.
        """

    def done(self) -> bool:
        """done() -> bool

        Vérifie si une commande ou une manœuvre en cours est terminée.

        Retourne :
            ``True`` si la commande est terminée, ``False`` sinon.
        """

    def stalled(self) -> bool:
        """stalled() -> bool

        Vérifie si la base mobile est actuellement bloquée.

        Elle est bloquée lorsqu'elle ne peut pas atteindre la vitesse ou la position cible, même
        avec le signal d'actionnement maximal.

        Retourne :
            ``True`` si la base mobile est bloquée, ``False`` sinon.
        """

    def use_gyro(self, use_gyro: bool) -> None:
        """use_gyro(use_gyro)

        Choisissez ``True`` pour utiliser le capteur gyroscopique pour tourner et conduire
        en ligne droite. Choisissez ``False`` pour ne compter que sur les capteurs de rotation
        intégrés du moteur.

        Arguments:
            use_gyro (bool): ``True`` pour activer, ``False`` pour désactiver.
        """


class Car:
    """Un véhicule avec un moteur de direction et un ou plusieurs moteurs pour la conduite.

    Lorsque vous utilisez cette classe, le moteur de direction trouvera automatiquement la
    position centrale. Cela détermine également quel angle correspond à 100%
    de direction.
    """

    def __init__(
        self,
        steer_motor: Motor,
        drive_motors: Motor | Tuple[Motor, ...],
        torque_limit: Number = 100,
    ):
        """Car(steer_motor, drive_motors, torque_limit=100)

        Arguments:
            steer_motor (Motor):
                Le moteur qui dirige les roues avant.
            drive_motors (Motor): Le moteur qui entraîne les roues. Utilisez un tuple
                pour plusieurs moteurs.
            torque_limit (Number, %): La limite de couple maximale utilisée pour trouver les
                points de fin pour le mécanisme de direction, en pourcentage du
                couple maximal du moteur de direction.
        """

    def steer(self, percentage: Number) -> None:
        """steer(percentage)

        Dirige les roues avant d'une certaine quantité. Pour une direction à 100%,
        il tourne à droite de l'angle déterminé lors de l'initialisation.
        Pour une direction à -100%, il tourne à gauche et 0% signifie tout droit.

        Arguments:
            steering (Number, %): Quantité pour diriger les roues avant.
        """

    def drive_power(self, power: Number) -> None:
        """drive_power(power)

        Conduit la voiture à un niveau de puissance donné. Les valeurs positives conduisent vers l'avant,
        les valeurs négatives conduisent vers l'arrière.

        La valeur ``power`` est utilisée pour régler la tension du moteur en pourcentage de
        la tension de la batterie. En dessous de 10%, la voiture laissera les roues en roue libre
        pour rouler en douceur au lieu de freiner brusquement.

        Cette commande est utile pour les applications de télécommande où vous souhaitez
        une réponse instantanée aux pressions sur les boutons ou aux mouvements du joystick.

        Arguments:
            speed (Number, %): Vitesse de la voiture.
        """

    def drive_speed(self, speed: Number) -> None:
        """drive_speed(speed)

        Conduit la voiture à une vitesse de moteur donnée. Les valeurs positives conduisent vers l'avant,
        les valeurs négatives conduisent vers l'arrière.

        Cette commande est utile pour une conduite plus précise avec une accélération
        et une décélération en douceur. Cela augmente automatiquement la puissance
        pour maintenir la vitesse lorsque vous traversez des obstacles.

        Arguments:
            speed (Number, deg/s): Vitesse angulaire des moteurs de conduite.
        """


# HACK: hide from jedi
if TYPE_CHECKING:
    del Motor
    del Number
    del MaybeAwaitable
    del Stop
