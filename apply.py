import pygame, sys
from pygame.locals import QUIT

pygame.init()
w = 400
h = 300
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption('Hello World!')
screen.fill((255, 255, 255))

import my_functions as mf
# TODO draw grid


# TODO two_part_flag


# TODO four_part_flag


# TODO crosshair


# TODO vert_lines

pygame.display.update()           
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


