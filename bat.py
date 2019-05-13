from conf import SCREEN_WIDTH, SCREEN_HEIGHT
from pgzero.actor import Actor


class Bat(Actor):
    __speed = 7
    __img = 'paddle_blu'

    def __init__(self, *args, **kwargs):
        super().__init__(self.__img, *args, **kwargs)
        self.x = SCREEN_WIDTH / 2
        self.y = SCREEN_HEIGHT - self.height*0.7

    def update(self):
        pass

    def move_left(self):
        if self.left > 2:
            self.x -= self.__speed

    def move_right(self):
        if self.right < SCREEN_WIDTH - 2:
            self.x += self.__speed
