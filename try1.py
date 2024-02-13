import pygame, sys
from pygame.locals import QUIT

pygame.init()
w = 800
h = 600
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption('Hello World!')
screen.fill((255, 255, 255))

import my_functions as f
# TODO draw grid



# TODO horiz lines


# TODO square with circle



# TODO X shape




pygame.display.update()                                 
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
  



