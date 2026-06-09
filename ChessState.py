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
    def __init__(self, colorType, position):
        self.colorType = colorType
        self.color = colorType[0]
        self.type = colorType[1]
        self.position = position
        self.whitesTurn = True 

    def getValidPawnMove(self, board):
        moves = []
        x, y = self.position

        if(self.whitesTurn == True):
            if (self.color == "w"):
                if (x - 1 >= 0) and (board[x - 1][y] == ""):
                    moves.append((x - 1, y))
                if (x == 6) and (board[x - 1][y] == "") and (board[x - 2][y] == ""):
                    moves.append((x - 2, y))
        else:
            if (x + 1 <= 7) and (board[x + 1][y] == ""):
                moves.append((x + 1, y))
            if (x == 1) and (board[x + 1][y] == "") and (board[x + 2][y] == ""):
                moves.append((x + 2, y))

        return moves

    def getValidKnightMove(self, board):
        return []

    def getValidBishopMove(self, board):
        moves = []
        row, col = self.position

        directions = [(-1, 1),  (1, 1),   (1, -1),  (-1, -1)]

        for dRow, dCol in directions:
            r = row + dRow
            c = col + dCol

            while 0 <= r < 8 and 0 <= c < 8:
                piece = board[r][c]

                if piece == "":
                    moves.append((r, c))

                elif piece[0] != self.color:
                    moves.append((r, c))
                    break

                else:
                    break

                r += dRow
                c += dCol

        return moves

    def getValidRookMove(self, board):
        moves = []
        row, col = self.position

        directions = [(-1, 0),  (1, 0),   (0, -1),  (0, 1)]

        for dRow, dCol in directions:
            r = row + dRow
            c = col + dCol

            while 0 <= r < 8 and 0 <= c < 8:
                piece = board[r][c]

                if piece == "":
                    moves.append((r, c))

                elif piece[0] != self.color:
                    moves.append((r, c))
                    break

                else:
                    break

                r += dRow
                c += dCol

        return moves

    def getValidQueenMove(self, board):
        straightMoves = []
        diagMoves = []
        moves = []

        row, col = self.position

        Rdirections = [(-1, 0),  (1, 0),   (0, -1),  (0, 1)]

        for dRow, dCol in Rdirections:
            r = row + dRow
            c = col + dCol

            while 0 <= r < 8 and 0 <= c < 8:
                piece = board[r][c]
                if piece == "":
                    straightMoves.append((r, c))
                elif piece[0] != self.color:
                    straightMoves.append((r, c))
                    break
                else:
                    break
                r += dRow
                c += dCol
        moves.append(straightMoves) 

        Bdirections = [(-1, 1),  (1, 1),   (1, -1),  (-1, -1)]

        for bRow, bCol in Bdirections:
            r = row + dRow
            c = col + dCol
            while 0 <= r < 8 and 0 <= c < 8:
                piece = board[r][c]
                if piece == "":
                    diagMovesoves.append((r, c))
                elif piece[0] != self.color:
                    diagMoves.append((r, c))
                    break
                else:
                    break
                r += bRow
                c += bCol
        moves.append(diagMoves)

        return moves

    def getValidKingMove(self, board):
        moves = []
        x, y = self.position
        curColor = board[x][y]

        change = [
            (-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,0), (1,1), (1,-1)
        ]

        for changeX, changeY in change:
            newX = x + changeX
            newY = y + changeY

            if (0 <= newX <= 7) and (0 <= newY <= 7):
                newPos = board[newX][newY]
                if newPos == "":
                    moves.append((newX, newY))
                
        return moves

    def getValidCastle(self, board):
        pass
