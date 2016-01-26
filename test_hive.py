import hive

def test_creation():
    g = hive.Hive(1)
    assert g.board == [[False]]
    g = hive.Hive(2)
    assert g.board == [
    [False, False],
    [False, False, False],
    [False, False]
    ]
def test_str():
    g = hive.Hive(2)
    assert str(g) == ' 0 0 \n0 0 0\n 0 0 '
def test_getNeighborhood():
    g = hive.Hive(3)
    hood1 = g.getNeighborhood(0,0)
    assert set(hood1) == {(0,0), (0, 1), (1,0), (1,1)}
    hood2 = g.getNeighborhood(2,2)
    assert set(hood2) == {(2, 2), (2, 1), (2, 3), (1, 1), (1, 2), (3, 1), (3, 2)}
    hood3 = g.getNeighborhood(4,1)
    assert set(hood3) == {(4,1), (4,0), (4,2), (3,1), (3,2)}
    hood4 = g.getNeighborhood(3,2)
    assert set(hood4) == {(2,2),(2,3),(3,1),(3,2),(3,3),(4,1),(4,2)}
def test_makeMove():
    g = hive.Hive(2)
    g.makeMove(1,1)
    assert g.board == [
    [True, True],
    [True, True, True],
    [True, True]
    ]
    g = hive.Hive(3)
    g.makeMove(0,0)
    assert g.getSpot(0,0) and g.getSpot(0,1) and g.getSpot(1,0) and g.getSpot(1,1)
def test_won():
    g = hive.Hive(2)
    g.makeMove(1,1)
    assert g.won() == True
def test_makeMoves():
    g = hive.Hive(3)
    g.makeMoves([(0,0), (0,1), (1,1), (2,0), (2,3), (3,1), (4,0), (4,1)])
    assert g.won() == True
def test_getSpot():
    g = hive.Hive(2)
    g.board[1][1] = True
    assert g.getSpot(1,1) == True
def test_setSpot():
    g = hive.Hive(2)
    g.setSpot(1,1,True)
    assert g.getSpot(1,1) == True
def test_toggle():
    g = hive.Hive(2)
    s1 = g.getSpot(1,1)
    g._toggle([(1,1)])
    s2 = g.getSpot(1,1)
    assert s1 == (not s2)
def test_numSpots():
    n1 = hive.Hive.numSpots(1)
    n2 = hive.Hive.numSpots(2)
    n3 = hive.Hive.numSpots(3)
    n4 = hive.Hive.numSpots(4)
    assert n1 == 1
    assert n2 == 7
    assert n3 == 19
    assert n4 == 37
def test_getPossibleMoves():
    g = hive.Hive(2)
    possible_moves = [(0,0),(0,1),(1,0),(1,1),(1,2),(2,0),(2,1)]
    assert g.getPossibleMoves() == possible_moves
