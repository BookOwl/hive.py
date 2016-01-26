#!python3
import sys
import hive

helptext = '''
Help:
Hive is a simple logic and math game. You play by entering the row and column of a tile.
This flips that tile, but it also flips other all the other tiles touching it.
For example, the coordinates for a Hive game of size 2 are:
  1,1 1,2
2,1 2,2 2,3
  3,1 3,2

You start out with all the tiles set to 0. If you can get every tile set to 1, you win!

Credits:
The original game was created by Scratch user @silverdroid. This port was created by @BookOwl.
You can find the original game at https://scratch.mit.edu/projects/92205108/
You can find the Scratch forum topic for discussing strategy at https://scratch.mit.edu/discuss/topic/179092/
'''
nummoves = 0

def main():
    n = printintro()
    game = hive.Hive(n)
    while True:
        printstatus(game)
        makemove(game)
        if game.won():
            print(game)
            gameover()
        print()

def printintro():
    print("Hive - The Game")
    print("Ported from the Scratch game Hive by @silverdroid")
    print("Press h for help")
    n = int(input("How large is the board? The original board is of size 3. "))
    print()
    return n

def printstatus(game):
    global nummoves
    nummoves += 1
    print("Move #%s" % nummoves)
    print(game)

def makemove(game):
    global nummoves
    move = input("Enter your move: ").split(",")
    row, col = move[0].strip(), move[1].strip()
    try:
        game.makeMove(int(row) - 1, int(col) - 1)
    except ValueError:
        nummoves -= 1
        if move == 'h':
            print(helptext)
        else:
            print("You did not enter a valid coordinate. Try again.")

def gameover():
    print("You won!")
    print("You used %s moves!" % nummoves)
    print("Thanks for playing!")
    input()
    sys.exit()

if __name__ == '__main__':
    main()
