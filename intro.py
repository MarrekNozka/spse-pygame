import pgzrun
from pgzero.actor import Actor

WIDTH = 500
HEIGHT = 300


class Bat(Actor):
    xspeed = 0
    yspeed = 0

    def __init__(self, *args, **kwargs):
        super().__init__('paddle_blu', *args, **kwargs)
        self.x = WIDTH /2
        self.y = HEIGHT - self.height

    def update(self):
        self.x += self.xspeed
        self.y += self.yspeed
        if self.right > WIDTH or self.left < 0:
            self.xspeed = - self.xspeed



batA = Bat()
batA.xspeed = 5

batB = Bat()
batB.y = 50
batB.xspeed = -3



def update():
    batA.update()
    batB.update()



def draw():
    screen.fill((0,128,100))
    batA.draw()
    batB.draw()


pgzrun.go()
