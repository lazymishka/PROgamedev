import pygame
import time
pygame.init()
screen=pygame.display.set_mode((600, 700))
imgbox = pygame.image.load(r"C:\Users\laila\OneDrive\Desktop\python game development\right o game\happy birthday.jpg")
imgbox = pygame.transform.scale(imgbox, (600,700))
birthimg = pygame.image.load(r"C:\Users\laila\OneDrive\Desktop\python game development\right o game\birthdaycake.jpg")
birthimg = pygame.transform.scale(birthimg, (600, 700))
pinkimg = pygame.image.load(r"C:\Users\laila\OneDrive\Desktop\python game development\right o game\pink-cake_820667-32.jpg")
pinkimg = pygame.transform.scale(pinkimg, (600,700))
while True:
    screen.blit(imgbox, (0, 0))
    pygame.display.update()
    time.sleep(2)
    screen.blit(birthimg, (0, 0))
    pygame.display.update()
    time.sleep(2)
    screen.blit(pinkimg, (0, 0))
    pygame.display.update()
    time.sleep(2)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
