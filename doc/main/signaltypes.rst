Signaux et Unités
=================

De nombreuses commandes vous permettent de spécifier des arguments en termes
de quantités physiques bien connues. Cette page donne un aperçu de chaque
quantité et de son unité.

Nombres
~~~~~~~

.. autodata:: pybricks.parameters.Number
  :noindex:

Temps
~~~~~

.. _time:

temps : ms
----------

Toutes les valeurs de temps et de durée sont mesurées en millisecondes (ms).

Par exemple, la durée du mouvement avec ``run_time``, et la durée de
:func:`wait <.tools.wait>` sont spécifiées en millisecondes.

Angles et mouvement angulaire
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _angle:

angle : deg
-----------

Tous les angles sont mesurés en degrés (deg). Une rotation complète correspond
à 360 degrés.

Par exemple, les valeurs d'angle d'un ``Motor`` ou du ``GyroSensor`` sont
exprimées en degrés.

.. _speed:

vitesse de rotation : deg/s
---------------------------

La vitesse de rotation, ou *vélocité angulaire* décrit la vitesse à laquelle
quelque chose tourne, exprimée en nombre de degrés par seconde (deg/s).

Par exemple, les valeurs de vitesse de rotation d'un ``Motor`` ou du
``GyroSensor`` sont exprimées en degrés par seconde.

Bien que nous recommandions de travailler avec des degrés par seconde dans vos
programmes, vous pouvez utiliser le tableau suivant pour convertir entre les
unités couramment utilisées.

+-----------+-------+-----------+
|           | deg/s | rpm       |
+-----------+-------+-----------+
| 1 deg/s = | 1     | 1/6=0.167 |
+-----------+-------+-----------+
| 1 rpm =   | 6     | 1         |
+-----------+-------+-----------+

.. _acceleration:

accélération de rotation : deg/s²
---------------------------------

L'accélération de rotation, ou *accélération angulaire* décrit la vitesse à
laquelle la vitesse de rotation change. Cela s'exprime comme le changement du
nombre de degrés par seconde, pendant une seconde (deg/s²). Cela s'écrit aussi
communément :math:`deg/s^2`.

Par exemple, vous pouvez ajuster le réglage de l'accélération de rotation d'un
``Motor`` pour changer la douceur ou la rapidité avec laquelle il atteint le
point de consigne de vitesse constante.

Distance et mouvement linéaire
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _distance:

distance : mm
-------------

Les distances sont exprimées en millimètres (mm) autant que possible.

Par exemple, la valeur de distance du ``UltrasonicSensor`` est mesurée en
millimètres.

Bien que nous recommandions de travailler avec des millimètres dans vos
programmes, vous pouvez utiliser le tableau suivant pour convertir entre les
unités couramment utilisées.

+---------+------+-----+--------+
|         | mm   | cm  | inch   |
+---------+------+-----+--------+
| 1 mm =  | 1    | 0.1 | 0.0394 |
+---------+------+-----+--------+
| 1 cm =  | 10   | 1   | 0.394  |
+---------+------+-----+--------+
| 1 inch =| 25.4 | 2.54| 1      |
+---------+------+-----+--------+

.. _dimension:

dimension : mm
--------------

Les dimensions sont exprimées en millimètres (mm), tout comme les distances.

Par exemple, le diamètre d'une roue est mesuré en millimètres.

.. _linspeed:

vitesse : mm/s
--------------

Les vitesses linéaires sont exprimées en millimètres par seconde (mm/s).

Par exemple, la vitesse d'un véhicule robotique est exprimée en mm/s.

.. _linacceleration:

accélération linéaire : mm/s²
-----------------------------

L'accélération linéaire décrit la vitesse à laquelle la vitesse change. Cela
s'exprime comme le changement des millimètres par seconde, pendant une seconde
(mm/s²). Cela s'écrit aussi communément :math:`mm/s^2`.

Par exemple, vous pouvez ajuster le réglage de l'accélération d'une
:class:`DriveBase <.robotics.DriveBase>` pour changer la douceur ou la
rapidité avec laquelle elle atteint le point de consigne de vitesse constante.

Unités approximatives et relatives
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _percentage:

pourcentage : %
---------------

Certains signaux n'ont pas d'unités spécifiques. Ils vont d'un minimum (0%) à
un maximum (100%). Des types spécifiques de pourcentages sont :ref:`distances
relatives <relativedistance>` ou :ref:`luminosité <brightness>`.

Un autre exemple est le volume sonore, qui va de 0% (silencieux) à 100% (très
fort).

.. _relativedistance:

distance relative : %
---------------------

Certaines mesures de distance ne fournissent pas une valeur précise avec une
unité spécifique, mais elles vont de très proche (0%) à très loin (100%).
Celles-ci sont appelées distances relatives.

Par exemple, la valeur de distance du ``InfraredSensor`` est une distance
relative.

.. _brightness:

luminosité : %
--------------

La luminosité perçue d'une lumière est exprimée en pourcentage. Elle est de 0%
lorsque la lumière est éteinte et de 100% lorsque la lumière est complètement
allumée. Lorsque vous choisissez 50%, cela signifie que la lumière est perçue
comme environ deux fois moins lumineuse pour l'œil humain.

Force et couple
~~~~~~~~~~~~~~~

.. _force:

force : N
---------

Les valeurs de force sont exprimées en newtons (N).

Bien que nous recommandions de travailler avec des newtons dans vos
programmes, vous pouvez utiliser le tableau suivant pour convertir vers et
depuis d'autres unités.

+---------+------+-------+-----------------------------+
|         | mN   | N     | lbf                         |
+---------+------+-------+-----------------------------+
| 1 mN =  | 1    | 0.001 | :math:`2.248 \cdot 10^{-4}` |
+---------+------+-------+-----------------------------+
| 1 N =   | 1000 | 1     | 0.2248                      |
+---------+------+-------+-----------------------------+
| 1 lbf = | 4448 | 4.448 | 1                           |
+---------+------+-------+-----------------------------+

.. _torque:

couple : mNm
------------

Les valeurs de couple sont exprimées en millinewtonmètre (mNm) sauf indication
contraire.

Électricité
~~~~~~~~~~~

.. _voltage:

tension : mV
------------

Les tensions sont exprimées en millivolt (mV).

Par exemple, vous pouvez vérifier la tension de la batterie.

.. _current:

courant : mA
------------

Les courants électriques sont exprimés en milliampère (mA).

Par exemple, vous pouvez vérifier le courant fourni par la batterie.

.. _energy:

énergie : J
-----------

L'énergie stockée ou la consommation d'énergie peuvent être exprimées en
Joules (J).

.. _power:

puissance : mW
--------------

La puissance est le taux auquel l'énergie est stockée ou consommée. Elle est
exprimée en milliwatt (mW).

Environnement ambiant
~~~~~~~~~~~~~~~~~~~~~

.. _frequency:

fréquence : Hz
--------------

Les fréquences sonores sont exprimées en Hertz (Hz).

Par exemple, vous pouvez choisir la fréquence d'un bip pour changer la
hauteur.

.. _temperature:

température : °C
----------------

La température est mesurée en degrés Celsius (°C). Pour convertir en degrés
Fahrenheit (°F) ou Kelvin (K), vous pouvez utiliser les formules de conversion
suivantes :

    :math:`^{\circ}\kern1pt\!F =\kern1pt^{\circ}\kern1pt\!C \cdot \frac{9}{5} + 32`.

    :math:`K =\kern1pt^{\circ}\kern1pt\!C + 273.15`.

.. _hue:

teinte : deg
------------

La teinte d'une couleur (0-359 degrés).

.. _robotframe:

Cadres de référence
~~~~~~~~~~~~~~~~~~~

Le module Pybricks et cette documentation utilisent les conventions suivantes :

- X : Positif signifie vers l'avant. Négatif signifie vers l'arrière.
- Y : Positif signifie vers la gauche. Négatif signifie vers la droite.
- Z : Positif signifie vers le haut. Négatif signifie vers le bas.

Pour vous assurer que toutes les mesures du hub (comme l'accélération) ont la
valeur et le signe corrects, vous pouvez spécifier comment le hub est monté
dans votre création. Cela ajuste les mesures afin qu'il soit facile de voir
comment votre *robot* se déplace, plutôt que comment le *hub* se déplace.

Par exemple, le hub peut être monté à l'envers dans votre conception. Si vous
configurez les paramètres comme indiqué dans :numref:`fig_imuexamples`, les
mesures du hub seront ajustées en conséquence. De cette façon, une valeur
d'accélération positive dans la direction X signifie que votre *robot*
accélère vers l'avant, même si le *hub* accélère vers l'arrière.

.. _fig_imuexamples:

.. figure:: ../main/diagrams/imuexamples.png
   :width: 100 %

   Comment configurer les paramètres ``top_side`` et ``front_side`` pour trois
   conceptions de robots différentes. La même technique peut être appliquée à
   d'autres hubs et à d'autres créations, en notant dans quelle direction le
   haut et l'avant de la :class:`Side <Side>` du hub pointent. L'exemple à
   gauche est la configuration par défaut.
