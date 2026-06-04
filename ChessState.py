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
        whiteKnightCords = []
        blackKnightCords = []

        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == "bn":
                    blackKnightCords.append((row, col))
                    print(f"Black knight on:{blackKnightCords}")
                if board[row][col] == "wn":
                    whiteKnightCords.append((row, col))
                    print(f"White knight on:{whiteKnightCords}")

        return moves 

    def getValidBishopMove(self, board):
        moves = []
        whiteBishopCords = []
        blackBishopCords = []

        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == "bb":
                    blackBishopCords.append((row, col))
                    print(f"Black bishop on:{blackBishopCords}")
                if board[row][col] == "wb":
                    whiteBishopCords.append((row, col))
                    print(f"White bishop on:{whiteBishopCords}")

        return moves 

    def getValidRookMove(self, board):
        moves = []
        whiteRookCords = []
        blackRookCords = []

        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == "br":
                    blackRookCords.append((row, col))
                    print(f"Black rook on:{blackRookCords}")
                if board[row][col] == "wr":
                    whiteRookCords.append((row, col))
                    print(f"White rook on:{whiteRookCords}")

        return moves 

    def getValidQueenMove(self, board):
        moves = []
        whiteQueenCords = []
        blackQueenCords = []

        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == "bq":
                    blackQueenCords.append((row, col))
                    print(f"Black queen on:{blackQueenCords}")
                if board[row][col] == "wq":
                    whiteQueenCords.append((row, col))
                    print(f"White queen on:{whiteQueenCords}")

        return moves

    def getValidKingMove(self, board):
        moves = []
        whiteKingCords = []
        blackKingCords = []

        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == "bk":
                    blackKingCords.append((row, col))
                    print(f"Black king on:{blackKingCords}")
                if board[row][col] == "wk":
                    whiteKingCords.append((row, col))
                    print(f"White king on:{whiteKingCords}")

        return moves

