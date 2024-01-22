import pygame, sys
from pygame.locals import QUIT

pygame.init()
w = 400
h = 400
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption('Hello World!')
screen.fill((255, 255, 255))


def stick_guy(x, y, size):
    gap = size//5
    pygame.draw.circle(screen, (0,0,0), (x,y), gap, width=1)
    pygame.draw.line(screen, (0,0,0), (x,y+gap), (x, y+2*gap))
    pygame.draw.line(screen, (0,0,0), (x,y+2*gap), (x+gap, y+3*gap))
    pygame.draw.line(screen, (0,0,0), (x,y+2*gap), (x-gap, y+3*gap))


stick_guy(100, 100, 100)
stick_guy(200, 200, 50)



pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
