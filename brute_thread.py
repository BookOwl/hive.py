#!python3
import _thread as thread
import itertools, pprint, queue, time
import hive

print_lock = thread.allocate_lock()
def safeprint(*args, **kargs):
    with print_lock:
        print(*args, **kargs)

sols_queue = queue.Queue()

def brute(moves):
    g = hive.Hive(size)
    g.makeMoves(moves)
    if g.won():
        safeprint("Found solution: %s" % str(moves))
        sols_queue.put(moves)

def producer(i):
    num_tested[i] = 0
    making_data[i] = False
    safeprint("Producer %s" % i)
    spots = hive.Hive(size).getPossibleMoves()
    for seq in itertools.combinations(spots, i):
        brute(seq)
        num_tested[i] += 1
    safeprint("Bruted through all move sequences of length %s" % i)
    del num_tested[i]
    making_data[i] = True

safeprint("Hive Brute Forcer - Threaded")
size = int(input("Enter the size of the board: "))
minMoves = int(input("Enter min number of moves: "))
numMoves = int(input("Enter max number of moves: "))
safeprint("Starting threads...")
making_data = {}
num_tested = {}
for i in range(minMoves, numMoves+1):
    thread.start_new_thread(producer, (i,))
time.sleep(0.25)
while not all(making_data.values()):
    s = ""
    for k in sorted(num_tested):
        s += "%s: %s,\t" % (k, num_tested[k])
    safeprint(s)
    time.sleep(1)
safeprint("Done")
