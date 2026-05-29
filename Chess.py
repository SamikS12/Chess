import pygame
import time
from datetime import datetime
from sys import platform
import os
from copy import deepcopy

pygame.init()
screen = pygame.display.set_mode((900, 750), pygame.RESIZABLE)

board = pygame.image.load("Chess_Board/brown.png").convert_alpha()

bp = pygame.image.load("Chess_Pieces/bp.png").convert_alpha() #black pawn
bn = pygame.image.load("Chess_Pieces/bn.png").convert_alpha() #black knight
bb = pygame.image.load("Chess_Pieces/bb.png").convert_alpha() #black bishop
br = pygame.image.load("Chess_Pieces/br.png").convert_alpha() #black rook  
bq = pygame.image.load("Chess_Pieces/bq.png").convert_alpha() #black queen
bk = pygame.image.load("Chess_Pieces/bk.png").convert_alpha() #black king  

wp = pygame.image.load("Chess_Pieces/wp.png").convert_alpha() #white pawn
wn = pygame.image.load("Chess_Pieces/wn.png").convert_alpha() #white knight
wb = pygame.image.load("Chess_Pieces/wb.png").convert_alpha() #white bishop
wr = pygame.image.load("Chess_Pieces/wr.png").convert_alpha() #white rook  
wq = pygame.image.load("Chess_Pieces/wq.png").convert_alpha() #white queen
wk = pygame.image.load("Chess_Pieces/wk.png").convert_alpha() #white king  

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill((255, 255, 255))
    scaled_image = pygame.transform.scale(board, (750, 750))
    screen.blit(scaled_image, (0, 0))
    
    pygame.display.flip()

pygame.quit()
