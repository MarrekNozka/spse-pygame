#!/usr/bin/env python3
#
# hra Arkanoid
from conf import SCREEN_WIDTH, SCREEN_HEIGHT
import pgzrun
from game import Game


WIDTH = SCREEN_WIDTH
HEIGHT = SCREEN_HEIGHT

press_keys = []
game = Game()


def update():
    game.update()


def draw():
    screen.fill((0, 128, 100))
    game.draw()


def on_key_down(key):
    game.handle_key_down(key)


def on_key_up(key):
    if key == keys.SPACE:
        game.start()
    game.handle_key_up(key)


pgzrun.go()
