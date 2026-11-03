import pgzrun
from random import randint

W = 800
H = 600

title = "Flappy Ball"

R = randint(0, 255)
G = randint(0, 255)
B = randint(0, 255)
CLR= R, G, B

GRAVITY = 2000

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = 200
        self.vy = 0
        self.radius = 40

    def draw(self):
        pos = (self.x,self.y)
        screen.draw.filled_circle(pos, self.radius, CLR)

ball = Ball(50, 100)
def draw():
    screen.clear()
    ball.draw()

def update(dt):
  uy = ball.vy
  ball.vy += GRAVITY * dt
  ball.y += (uy + ball.vy)* 0.5 * dt

  if ball.y > H - ball.radius:
      ball.y = H - ball.radius
      ball.vy = -ball.vy * 0.5

  ball.x += ball.vx * dt
  if ball.x > W - ball.radius or ball.x < ball.radius:
      ball.vx = -ball.vx

pgzrun.go()

