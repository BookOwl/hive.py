#!python3
import sys
import hive

helptext = '''
Help:
Hive is a simple logic and math game. You play by entering the number of a tile (1 - 19).
This flips that tile, but it also flips other all the other tiles touching it.
The coordinates of the hexes are
  01 02 03
 04 05 06 07
08 09 10 11 12
 13 14 15 16
  17 18 19
You start out with all the tiles set to 0. If you can get every tile set to 1, you win!

Credits:
The original game was created by Scratch user @silverdroid. This port was created by @BookOwl.
You can find the original game at https://scratch.mit.edu/projects/92205108/
You can find the Scratch forum topic for discussing strategy at https://scratch.mit.edu/discuss/topic/179092/
'''
nummoves = 0

def main():
    game = hive.Hive()
    printintro()
    while True:
        printstatus(game)
        makemove(game)
        if game.won():
            gameover()
        print()

def printintro():
    print("Hive - The Game")
    print("Ported from the Scratch game Hive by @silverdroid")
    print("Press h for help")
    print()

def printstatus(game):
    global nummoves
    nummoves += 1
    print("Move #%s" % nummoves)
    print(game)

def makemove(game):
    global nummoves
    move = input("Enter your move: ")
    try:
        game.makeMove(int(move))
    except ValueError:
        nummoves -= 1
        if move == 'h':
            print(helptext)
        else:
            print("You did not enter a number between 1 and 19. Try again.")

def gameover():
    print("You won!")
    print("You used %s moves!" % nummoves)
    print("Thanks for playing!")
    input()
    sys.exit()

if __name__ == '__main__':
    main()
