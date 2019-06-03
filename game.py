from bat import Bat
from ball import Ball


class Game(object):
    __press_keys = []

    __bat = None
    __ball = None

    def __init__(self) -> None:
        self.__bat = Bat()
        self.__ball = Ball()

    def start(self):
        self.__ball.speedx = 4
        self.__ball.speedy = 4

    def update(self):
        if self.__bat.colliderect(self.__ball):
            self.__ball.reflection(self.__press_keys)
        self.__bat.update(self.__press_keys)
        self.__ball.update()

    def draw(self):
        self.__bat.draw()
        self.__ball.draw()

    def handle_key_down(self, key):
        self.__press_keys.append(key)

    def handle_key_up(self, key):
        self.__press_keys.remove(key)
