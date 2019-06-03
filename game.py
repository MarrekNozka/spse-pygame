from conf import SCREEN_HEIGHT, SCREEN_WIDTH
from bat import Bat
from ball import Ball
from brick import Brick


class Game(object):
    __press_keys = set()  # down keys
    __bat = None
    __ball = None
    __bricks = []
    __run = False

    def __init__(self) -> None:
        self.__bat = Bat()
        self.__ball = Ball()
        self.__bricks.append(
            Brick(SCREEN_WIDTH / 2 + 100, SCREEN_HEIGHT / 2 + 50)
        )
        for i in range(1, 11):
            self.__bricks.append(Brick(50 + self.__bricks[-1].width * i, 100))

    def start(self):
        self.__ball.x = SCREEN_WIDTH / 2
        self.__ball.y = SCREEN_HEIGHT / 2
        self.__ball.speedx = 3
        self.__ball.speedy = 3
        self.__run = True

    def game_over(self):
        self.__ball.speedx = 0
        self.__ball.speedy = 0
        self.__run = False

    def update(self):
        if not self.__run:
            return
        ball = self.__ball
        for brick in self.__bricks:
            if brick.colliderect(self.__ball):
                if brick.left <= ball.x and brick.right >= ball.x:
                    self.__ball.reflection_y()
                else:
                    self.__ball.reflection_x()
                self.__bricks.remove(brick)
        if self.__ball.bottom >= SCREEN_HEIGHT - 2:
            self.game_over()
        if self.__bat.colliderect(self.__ball):
            self.__ball.reflection_y(self.__press_keys)
        self.__bat.update(self.__press_keys)
        self.__ball.update()

    def draw(self):
        self.__bat.draw()
        self.__ball.draw()
        for b in self.__bricks:
            b.draw()

    def handle_key_down(self, key):
        self.__press_keys.add(key)

    def handle_key_up(self, key):
        self.__press_keys.remove(key)
