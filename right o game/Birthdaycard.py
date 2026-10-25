import pygame
pygame.init()
screen=pygame.display.set_mode((600, 700))
while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()