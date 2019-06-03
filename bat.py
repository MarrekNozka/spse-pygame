from conf import SCREEN_WIDTH, SCREEN_HEIGHT
from pgzero.actor import Actor
import pygame


class Bat(Actor):
    __speed = 10
    __img = "paddle_blue"

    def __init__(self, *args, **kwargs):
        super().__init__(self.__img, *args, **kwargs)
        self.x = SCREEN_WIDTH / 2
        self.y = SCREEN_HEIGHT - self.height * 0.7

    def update(self, press_keys):
        if pygame.K_LEFT in press_keys:
            self.move_left()
        if pygame.K_RIGHT in press_keys:
            self.move_right()

    def move_left(self):
        if self.left > 2:
            self.x -= self.__speed

    def move_right(self):
        if self.right < SCREEN_WIDTH - 2:
            self.x += self.__speed
