import copy

class Hive:
    def __init__(self, N):
        "Create a new Hive game"
        self.N = N
        self.board = []
        for i in range(N, 2*N -1):
            self.board.append([False] * i)
        self.board.append([False] * (2 * N -1))
        self.board.extend(reversed(copy.deepcopy(self.board[:-1])))

    def getSpot(self, x, y):
        "Returns the state of the spot given by the zero-based coordinates x, y"
        return self.board[x][y]

    def setSpot(self, x, y, value):
        "Sets the state of the spot given by the zero-based coordinates x, y to value"
        self.board[x][y] = value

    def makeMove(self, x, y):
        """Makes a move at the location given by spot, which must be an int in the range of 1 to 19, inclusive.
        Throws a ValueError given invalid input."""
        self._toggle(self.getNeighborhood(x, y))

    def makeMoves(self, moves):
        """Makes a series of moves given.
        Equivalent to
        for move in moves:
            game.makeMove(*move)"""
        for move in moves:
            self.makeMove(*move)

    def _toggle(self, spots):
        "Internal method. Toggles a spot on the board."
        for spot in spots:
            state = self.getSpot(spot[0], spot[1])
            self.setSpot(spot[0], spot[1], not state)

    def won(self):
        "Returns True if the game is in a winning condition (all spots 1)"
        for row in self.board:
            if not all(row):
                return False
        return True

    def __str__(self):
        "Returns a properly formated string of the board"
        b = []
        for r in self.board:
            b.append([str(int(i)) for i in r])

        s = ''
        for (i, row) in enumerate(b[:self.N-1], start=1):
            s += ' ' * (self.N - i)
            s += ' '.join(row)
            s += ' ' * (self.N - i)
            s += '\n'
        s += ' '.join(b[self.N - 1])
        s += '\n'
        for (i, row) in enumerate(b[self.N:], start=self.N+1):
            s += ' ' * (i - self.N)
            s += ' '.join(row)
            s += ' ' * (i - self.N)
            s += '\n'
        return s[:-1]

    def getNeighborhood(self, x, y):
        m = self.N - 1
        hood = [(x, y - 1), (x, y), (x, y + 1)]
        if x > m:
            hood.extend([(x - 1, y), (x - 1, y + 1), (x + 1, y - 1), (x + 1, y)])
        elif x < m:
            hood.extend([(x - 1, y - 1), (x - 1, y), (x + 1, y), (x + 1, y + 1)])
        elif x == m:
            hood.extend([(x - 1, y - 1), (x - 1, y), (x + 1, y - 1), (x + 1, y)])
        for cord in tuple(hood):
            if ((cord[0] < 0 or cord[1] < 0) or (cord[0] >= len(self.board) or cord[1] >= len(self.board[cord[0]]))):
                hood.remove(cord)
        return hood

    def getPossibleMoves(self):
        moves = []
        for (x, row) in enumerate(self.board):
            for y in range(len(row)):
                moves.append((x,y))
        return moves

    @staticmethod
    def numSpots(N):
        "Returns the number of spots in a Hive board of size N."
        if N == 1:
            return 1
        else:
            return Hive.numSpots(N-1) + 6 * (N - 1)
