from conf import SCREEN_WIDTH, SCREEN_HEIGHT
from pgzero.actor import Actor
import pygame


class Ball(Actor):
    __img = "ball_blue"
    speedx = 0
    speedy = 0

    def __init__(self, *args, **kwargs):
        super().__init__(self.__img, *args, **kwargs)
        self.x = SCREEN_WIDTH / 2
        self.y = SCREEN_HEIGHT / 2

    def update(self):
        if self.left <= 0 or self.right >= SCREEN_WIDTH:
            self.reflection_x()
        if self.top <= 0:
            self.reflection_y()
        self.x += self.speedx
        self.y += self.speedy

    def reflection_x(self):
        self.speedx = -self.speedx

    def reflection_y(self, press_keys=tuple()):
        if pygame.K_LEFT in press_keys:
            self.speedx -= 1
        if pygame.K_RIGHT in press_keys:
            self.speedx += 1
        self.speedy = -self.speedy
