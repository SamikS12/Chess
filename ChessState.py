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
        whitePawnCords = []
        blackPawnCords = []

        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == "bp":
                    blackPawnCords.append((row, col))
                    print(f"Black pawns on:{blackPawnCords}")
                if board[row][col] == "wp":
                    whitePawnCords.append((row, col))
                    print(f"White pawns on:{whitePawnCords}")

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

