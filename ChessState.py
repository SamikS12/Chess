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
                    #print(f"Black pawns on:{blackPawnCords}")
                if board[row][col] == "wp":
                    whitePawnCords.append((row, col))
                    #print(f"White pawns on:{whitePawnCords}")

        whitePawns = []
        blackPawns = []
        whitePawns.append(whitePawnCords)
        blackPawns.append(blackPawnCords)

        print(f"White pawns on:{whitePawns}")
        print(f"Black pawns on:{blackPawns}")

        return moves 

    def getValidKnightMove(self, board):
        moves = []
        whiteKnightCords = []
        blackKnightCords = []

        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == "bn":
                    blackKnightCords.append((row, col))
                    #print(f"Black pawns on:{blackPawnCords}")
                if board[row][col] == "wn":
                    whiteKnightCords.append((row, col))
                    #print(f"White pawns on:{whitePawnCords}")

        whiteKnights = []
        blackKnights = []
        whiteKnights.append(whiteKnightCords)
        blackKnights.append(blackKnightCords)

        print(f"White Knights on:{whiteKnights}")
        print(f"Black Knights on:{blackKnights}")

        return moves 

    def getValidBishopMove(self, board):
        moves = []
        whiteBishopCords = []
        blackBishopCords = []

        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == "bb":
                    blackBishopCords.append((row, col))
                    #print(f"Black pawns on:{blackPawnCords}")
                if board[row][col] == "wb":
                    whiteBishopCords.append((row, col))
                    #print(f"White pawns on:{whitePawnCords}")

        whiteBishops = []
        blackBishops = []
        whiteBishops.append(whiteBishopCords)
        blackBishops.append(blackBishopCords)

        print(f"White Bishops on:{whiteBishops}")
        print(f"Black Bishops on:{blackBishops}")

        return moves 

    def getValidRookMove(self, board):
        moves = []
        whiteRookCords = []
        blackRookCords = []

        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == "br":
                    blackRookCords.append((row, col))
                    #print(f"Black pawns on:{blackPawnCords}")
                if board[row][col] == "wr":
                    whiteRookCords.append((row, col))
                    #print(f"White pawns on:{whitePawnCords}")

        whiteRooks = []
        blackRooks = []
        whiteRooks.append(whiteRookCords)
        blackRooks.append(blackRookCords)

        print(f"White Rooks on:{whiteRooks}")
        print(f"Black Rooks on:{blackRooks}")

        return moves 

    def getValidQueenMove(self, board):
        moves = []
        whiteQueenCords = []
        blackQueenCords = []

        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == "bq":
                    blackQueenCords.append((row, col))
                    #print(f"Black pawns on:{blackPawnCords}")
                if board[row][col] == "wq":
                    whiteQueenCords.append((row, col))
                    #print(f"White pawns on:{whitePawnCords}")

        whiteQueens = []
        blackQueens = []
        whiteQueens.append(whiteQueenCords)
        blackQueens.append(blackQueenCords)

        print(f"White Queen on:{whiteQueens}")
        print(f"Black Queen on:{blackQueens}")

        return moves

    def getValidKingMove(self, board):
        moves = []
        whiteKingCords = []
        blackKingCords = []

        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == "bk":
                    blackKingCords.append((row, col))
                    #print(f"Black pawns on:{blackPawnCords}")
                if board[row][col] == "wk":
                    whiteKingCords.append((row, col))
                    #print(f"White pawns on:{whitePawnCords}")

        whiteKings = []
        blackKings = []
        whiteKings.append(whiteKingCords)
        blackKings.append(blackKingCords)

        print(f"White King on:{whiteKings}")
        print(f"Black King on:{blackKings}")

        return moves

