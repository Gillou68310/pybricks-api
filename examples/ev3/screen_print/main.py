#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from pybricks.tools import wait
from pybricks.media.ev3dev import Font

# Le chargement des polices à partir du fichier prend du temps, il est donc préférable de les charger
# une seule fois au début du programme comme ceci :
tiny_font = Font(size=6)
big_font = Font(size=24, bold=True)
chinese_font = Font(size=24, lang="zh-cn")

# Initialiser l'EV3
ev3 = EV3Brick()

# Dire bonjour
ev3.screen.print("Hello!")

# Dire bonjour en petit
ev3.screen.set_font(tiny_font)
ev3.screen.print("hello")

# Dire bonjour en grand
ev3.screen.set_font(big_font)
ev3.screen.print("HELLO")

# Dire bonjour en chinois
ev3.screen.set_font(chinese_font)
ev3.screen.print("你好")

# Attendre un peu pour regarder l'écran
wait(5000)
