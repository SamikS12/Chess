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

    def flipBoard(self):
        self.board = self.board[::-1]
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece:
                    if piece[0] == "w":
                        self.board[row][col] = "b" + piece[1]
                    else:
                        self.board[row][col] = "w" + piece[1]

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

        if (self.color == "w"):
            if (x - 1 >= 0) and (board[x - 1][y] == ""):
                moves.append((x - 1, y))
                if (x == 6) and (board[x - 1][y] == "") and (board[x - 2][y] == ""):
                    moves.append((x - 2, y))
            for dc in [-1, 1]:
                nx, ny = x - 1, y + dc
                if 0 <= nx < 8 and 0 <= ny < 8:
                    target = board[nx][ny]
                    if target and target[0] == "b":
                        moves.append((nx, ny))
        else:
            if (x + 1 <= 7) and (board[x + 1][y] == ""):
                moves.append((x + 1, y))
            if (x == 1) and (board[x + 1][y] == "") and (board[x + 2][y] == ""):
                moves.append((x + 2, y))
            for dc in [-1, 1]:
                nx, ny = x + 1, y + dc
                if 0 <= nx < 8 and 0 <= ny < 8:
                    target = board[nx][ny]
                    if target and target[0] == "w":
                        moves.append((nx, ny))

        return moves

    def getValidKnightMove(self, board):
        moves = []
        row, col = self.position

        directions = [(-2, -1),(-2, 1), (-1, -2),(-1, 2),(1,-2),(1,2),(2,-1),(2,1)]

        for dRow, dCol in directions:
            r = row + dRow
            c = col + dCol

            if 0 <= r < 8 and 0 <= c < 8:
                piece = board[r][c]

                if piece == "" or piece[0] != self.color:
                    moves.append((r, c))
        return moves

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
        moves = []
        row, col = self.position

        directions = [(-1, 0),  (1, 0),   (0, -1),  (0, 1), (-1, 1),  (1, 1),   (1, -1),  (-1, -1)]

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
                if newPos == "" or newPos[0] != self.color:
                    moves.append((newX, newY))

        return moves

    def getValidCastle(self, board):
        pass