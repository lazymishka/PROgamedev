import pygame
pygame.init()
screen=pygame.display.set_mode((600, 700))
imgbox = pygame.image.load(r"C:\Users\laila\OneDrive\Desktop\python game development\right o game\happy birthday.jpg")
while True:
    screen.blit(imgbox, (0, 0))
    pygame.display.update()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()