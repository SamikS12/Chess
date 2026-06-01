from enum import Enum
import pygame

#PIECES BLACK & WHITE
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

class Piece(Enum):
    def __init__(self, color, position):
        self.color = color         
        self.position = position 
        self.piece = piece

    def isValidMove(self):

class ChessState: