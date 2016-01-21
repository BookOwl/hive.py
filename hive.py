class Hive:
    def __init__(self):
        "Create a new Hive game"
        self.board = [False] * 19

    def makeMove(self, spot):
        """Makes a move at the location given by spot, which must be an int in the range of 1 to 19, inclusive.
        Throws a ValueError given invalid input."""
        if  spot == 1:
            self._toggle([1,2,4,5])
        elif spot == 2:
            self._toggle([1, 2, 3, 5, 6])
        elif spot == 3:
            self._toggle([2,3,6,7])
        elif spot == 4:
            self._toggle([1,4,5,8,9])
        elif spot == 5:
            self._toggle([1,2,4,5,6,9,10])
        elif spot == 6:
            self._toggle([2,3,5,6,7,10,11])
        elif spot == 7:
            self._toggle([3,6,7,11,12])
        elif spot == 8:
            self._toggle([4,8,9,13])
        elif spot == 9:
            self._toggle([4,5,8,9,10,13,14])
        elif spot == 10:
            self._toggle([5,6,9,10,11,14,15])
        elif spot == 11:
            self._toggle([6,7,10,11,12,15,16])
        elif spot == 12:
            self._toggle([7,11,12,16])
        elif spot == 13:
            self._toggle([8,9,13,14,17])
        elif spot == 14:
            self._toggle([9,10,13,14,15,17,18])
        elif spot == 15:
            self._toggle([10,11,14,15,16,18,19])
        elif spot == 16:
            self._toggle([11,12,15,16,19])
        elif spot == 17:
            self._toggle([13,14,17,18])
        elif spot == 18:
            self._toggle([14,15,17,18,19])
        elif spot == 19:
            self._toggle([15,16,18,19])
        else:
            raise ValueError("Invalid Move!")

    def makeMoves(self, moves):
        """Makes a series of moves given.
        Equivalent to
        for move in moves:
            game.makeMove(move)"""
        for move in moves:
            self.makeMove(move)

    def _toggle(self, spots):
        "Internal method. Toggles a spot on the board."
        for spot in spots:
            self.board[spot-1] = not self.board[spot-1]

    def won(self):
        "Returns True if the game is in a winning condition (all spots 1)"
        return all(self.board)

    def __str__(self):
        "Returns a properly formated string of the board"
        s = ''
        b = [str(int(s)) for s in self.board]
        s += '  %s %s %s  \n' % tuple(b[:3])
        s += ' %s %s %s %s \n' % tuple(b[3:7])
        s += '%s %s %s %s %s\n' % tuple(b[7:12])
        s += ' %s %s %s %s \n' % tuple(b[12:16])
        s += '  %s %s %s' % tuple(b[16:])
        return s
