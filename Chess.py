#Chess.py
import pygame
from ChessState import ChessState, Piece
import os


pygame.init()
os.environ['SDL_VIDEO_WINDOW_POS'] = '750,50'
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
            colorType = game.board[row][col]
            if colorType and colorType in pieceImages:
                img = pygame.transform.scale(pieceImages[colorType], (SQUARE_SIZE, SQUARE_SIZE))
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
                colorType = game.board[row][col]

                if selectedSquare is None:
                    if colorType:
                        selectedSquare = clickedSquare
                        piece = Piece(colorType, clickedSquare)

                        if (piece.type == "p"):
                            validMoves = piece.getValidPawnMove(game.board)
                        elif (piece.type == "n"):
                            validMoves = piece.getValidKnightMove(game.board)
                        elif (piece.type == "b"):
                            validMoves = piece.getValidBishopMove(game.board)
                        elif (piece.type == "r"):
                            validMoves = piece.getValidRookMove(game.board)
                        elif (piece.type == "q"):
                            validMoves = piece.getValidQueenMove(game.board)
                        elif (piece.type == "k"):
                            validMoves = piece.getValidKingMove(game.board)

                else:
                    if clickedSquare in validMoves:
                        x, y = selectedSquare
                        game.board[row][col] = game.board[x][y]
                        game.board[x][y] = ""

                        selectedSquare = None
                        validMoves = []

                        game.whitesTurn = False

                        #pygame.transform.flip(boardImg, True, False)

                    elif clickedSquare == selectedSquare:
                        selectedSquare = None
                        validMoves = []

                        game.whitesTurn = False
                    

                        #pygame.transform.flip(boardImg, True, False)

    screen.fill((255, 255, 255))
    drawBoard()
    drawPieces()
    pygame.display.flip()

pygame.quit()


