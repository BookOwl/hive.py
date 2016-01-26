#!python3
import itertools, pprint
import hive

def brute(sizeBoard, numMoves):
    SPOTS = hive.Hive(sizeBoard).getPossibleMoves()
    sols = []
    for seq in itertools.combinations(SPOTS, numMoves):
        game = hive.Hive(sizeBoard)
        game.makeMoves(seq)
        if game.won():
            sols.append(seq)
    return sols

if __name__ == '__main__':
    print("Hive Brute Forcer")
    s = int(input("Enter size of board: "))
    n = int(input("Enter number of moves: "))
    print("Brute Forcing...")
    sols = brute(s, n)
    print("Found %s solutions." % len(sols))
    pprint.pprint(sols)
