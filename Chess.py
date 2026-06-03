#Chess.py
import pygame
from ChessState import ChessState, Piece

pygame.init()
screen = pygame.display.set_mode((750, 750), pygame.RESIZABLE)
pygame.display.set_caption("Chess")

boardImg = pygame.image.load("Chess_Board/brown.png").convert_alpha()

#PIECES BLACK & WHITE
pieceImages = {
    "bp": pygame.image.load("Chess_Pieces/bp.png").convert_alpha(), #black pawn
    "bn": pygame.image.load("Chess_Pieces/bn.png").convert_alpha(), #black knight
    "bb": pygame.image.load("Chess_Pieces/bb.png").convert_alpha(), #black bishop
    "br": pygame.image.load("Chess_Pieces/br.png").convert_alpha(), #black rook
    "bq": pygame.image.load("Chess_Pieces/bq.png").convert_alpha(), #black queen
    "bk": pygame.image.load("Chess_Pieces/bk.png").convert_alpha(), #black king
    "wp": pygame.image.load("Chess_Pieces/wp.png").convert_alpha(), #white pawn
    "wn": pygame.image.load("Chess_Pieces/wn.png").convert_alpha(), #white knight
    "wb": pygame.image.load("Chess_Pieces/wb.png").convert_alpha(), #white bishop
    "wr": pygame.image.load("Chess_Pieces/wr.png").convert_alpha(), #white rook
    "wq": pygame.image.load("Chess_Pieces/wq.png").convert_alpha(), #white queen
    "wk": pygame.image.load("Chess_Pieces/wk.png").convert_alpha(), #white king
}

BOARD_SIZE = 750
SQUARE_SIZE = BOARD_SIZE // 8

game = ChessState()
selectedSquare = None
validMoves = []

def pixelToSquare(x, y):
    col = x // SQUARE_SIZE
    row = y // SQUARE_SIZE
    return row, col

def drawBoard():
    scaledBoard = pygame.transform.scale(boardImg, (BOARD_SIZE, BOARD_SIZE))
    screen.blit(scaledBoard, (0, 0))

def drawPieces():
    for row in range(8):
        for col in range(8):
            pieceCode = game.board[row][col]
            if pieceCode and pieceCode in pieceImages:
                img = pygame.transform.scale(pieceImages[pieceCode], (SQUARE_SIZE, SQUARE_SIZE))
                screen.blit(img, (col * SQUARE_SIZE, row * SQUARE_SIZE))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = pygame.mouse.get_pos()
            if mouseX < BOARD_SIZE and mouseY < BOARD_SIZE:
                clickedSquare = pixelToSquare(mouseX, mouseY)
                row, col = clickedSquare
                pieceCode = game.board[row][col]

                if selectedSquare is None:
                    if pieceCode:
                        selectedSquare = clickedSquare
                        piece = Piece(pieceCode, clickedSquare)
                        validMoves = piece.getValidPawnMove(game.board)
                else:
                    if clickedSquare in validMoves:
                        sr, sc = selectedSquare
                        game.board[row][col] = game.board[sr][sc]
                        game.board[sr][sc] = ""
                        selectedSquare = None
                        validMoves = []
                    elif clickedSquare == selectedSquare:
                        selectedSquare = None
                        validMoves = []

    screen.fill((255, 255, 255))
    drawBoard()
    drawPieces()
    pygame.display.flip()

pygame.quit()

