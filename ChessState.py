#from enum import Enum
import pygame
import sys 


#PIECES BLACK & WHITE
# bp = pygame.image.load("Chess_Pieces/bp.png").convert_alpha() #black pawn
# bn = pygame.image.load("Chess_Pieces/bn.png").convert_alpha() #black knight
# bb = pygame.image.load("Chess_Pieces/bb.png").convert_alpha() #black bishop
# br = pygame.image.load("Chess_Pieces/br.png").convert_alpha() #black rook  
# bq = pygame.image.load("Chess_Pieces/bq.png").convert_alpha() #black queen
# bk = pygame.image.load("Chess_Pieces/bk.png").convert_alpha() #black king  

# wp = pygame.image.load("Chess_Pieces/wp.png").convert_alpha() #white pawn
# wn = pygame.image.load("Chess_Pieces/wn.png").convert_alpha() #white knight
# wb = pygame.image.load("Chess_Pieces/wb.png").convert_alpha() #white bishop
# wr = pygame.image.load("Chess_Pieces/wr.png").convert_alpha() #white rook  
# wq = pygame.image.load("Chess_Pieces/wq.png").convert_alpha() #white queen
# wk = pygame.image.load("Chess_Pieces/wk.png").convert_alpha() #white king  


class ChessState:
    def __init__(self):
        self.whiteToMove = True
        self.board = [
            ["br", "bn", "bb", "bq", "bk", "bb", "bn", "br"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wr", "wn", "wb", "wq", "wk", "wb", "wn", "wr"]]

        self.moveLog = [] 

    def main(self): 
        printBoard()

    if __name__ == "__main__":
        main()

    def getValidPawnMove(self):
        return validMoves

    def getValidKnightMove(self):
        return validMoves

    def getValidBishopMove(self):
        return validMoves

    def getValidRookMove(self):
        return validMoves

    def getValidQueenMove(self):
        return validMoves

    def getValidKingMove(self):
        return validMoves
        
    def makeMove(self, startRow, startCol, endRow, endCol):

        pieceMoved = self.board[startRow][startCol]

        if pieceMoved == "":
            return False

        self.board[endRow][endCol] = pieceMoved
        self.board[startRow][startCol] = ""

        self.moveLog.append(
            ((startRow, startCol), (endRow, endCol), pieceMoved))

        self.whiteToMove = not self.whiteToMove

        return True

    def getPiece(self, row, col):
        return self.board[row][col]

    def printBoard(self):
        for row in self.board:
            print(row)