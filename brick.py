from pgzero.actor import Actor


class Brick(Actor):
    __img = "brick_yellow"

    def __init__(self, x, y, *args, **kwargs):
        super().__init__(self.__img, *args, **kwargs)
        self.x = x
        self.y = y
