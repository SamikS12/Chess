#ChessState.py
class ChessState:
    def __init__(self):
        self.board = [
            ["br", "bn", "bb", "bq", "bk", "bb", "bn", "br"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["",   "",   "",   "",   "",   "",   "",   ""],
            ["",   "",   "",   "",   "",   "",   "",   ""],
            ["",   "",   "",   "",   "",   "",   "",   ""],
            ["",   "",   "",   "",   "",   "",   "",   ""],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wr", "wn", "wb", "wq", "wk", "wb", "wn", "wr"],
        ]

class Piece:
    def __init__(self, pieceCode, position):
        self.pieceCode = pieceCode
        self.color = pieceCode[0]
        self.type = pieceCode[1]
        self.position = position

    def getValidPawnMove(self, board):
        moves = []
        return moves 

    def getValidKnightMove(self, board):
        moves = []
        return moves

    def getValidBishopMove(self, board):
        moves = []
        return moves

    def getValidRookMove(self, board):
        moves = []
        return moves

    def getValidQueenMove(self, board):
        moves = []
        return moves

    def getValidKingMove(self, board):
        moves = []
        return moves

