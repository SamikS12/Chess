import pygame
import time
from datetime import datetime
from sys import platform
import os
from copy import deepcopy

pygame.init()
screen = pygame.display.set_mode((750, 750), pygame.RESIZABLE)

img = pygame.image.load("Chess/Chess_Board/brown.png").convert_alpha()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill((0, 0, 0))
    scaled_image = pygame.transform.scale(img, (750, 750))
    screen.blit(scaled_image, (0, 0))
    
    pygame.display.flip()

pygame.quit()
