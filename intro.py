#!/usr/bin/env python3
#
# hra Arkanoid
#
from bat import Bat
from conf import SCREEN_WIDTH, SCREEN_HEIGHT
import pgzrun

WIDTH = SCREEN_WIDTH
HEIGHT = SCREEN_HEIGHT

press_keys = []

bat = Bat()


def update():
    if keys.LEFT in press_keys:
        bat.move_left()
    if keys.RIGHT in press_keys:
        bat.move_right()


def draw():
    screen.fill((0, 128, 100))
    bat.draw()


def on_key_down(key):
    press_keys.append(key)


def on_key_up(key):
    press_keys.remove(key)


pgzrun.go()
