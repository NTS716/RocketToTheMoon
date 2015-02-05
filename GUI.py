import pygame
from pygame.locals import *
import sys

#Initialize Pygame
pygame.init()

#Create the display and caption the window
SCREEN = pygame.display.set_mode((800,600))
pygame.display.set_caption("Rocket to the Moon")

#Create the clock object and fps
clock = pygame.time.Clock()
fps = 60

#Main pygame loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    clock.tick(fps)
