import pgzrun
from random import randint

pygame.init()

W = 800
H = 600

title = "Flappy Ball"

ball_color = (
    randint(0,255),
    randint(0.255),
    randint(0.255)
)

GRAVITY = 2000

class Ball:
    def __int__(self, x, y):
        self.x = x
        self.y = y
        self.