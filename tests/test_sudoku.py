import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from sudoku import solve
from input import compute

def make_board(string: str):
    board = []

    for line in string.strip().split('\n'):
        line = line.strip()

        if not line:
            continue

        row = line.split()

        if len(row) != 9:
            raise ValueError(f"Invalid row length: Expected 9, got {len(row)}")
        
        for cell in row:
            if cell != '.' and (cell < '1' or cell > '9'):
                raise ValueError(f"Invalid cell value: Expected integer in range [1, 9], got {cell}")
        
        board.append(row)
    
    if len(board) != 9:
        raise ValueError(f"Invalid number of rows: Expected 9, got {len(board)}")
    
    return board

def test_solvable():
    puzzle = """
    5 3 . . 7 . . . .
    6 . . 1 9 5 . . .
    . 9 8 . . . . 6 .
    8 . . . 6 . . . 3
    4 . . 8 . 3 . . 1
    7 . . . 2 . . . 6
    . 6 . . . . 2 8 .
    . . . 4 1 9 . . 5
    . . . . 8 . . 7 9
    """

    expected = """
    5 3 4 6 7 8 9 1 2
    6 7 2 1 9 5 3 4 8
    1 9 8 3 4 2 5 6 7
    8 5 9 7 6 1 4 2 3
    4 2 6 8 5 3 7 9 1
    7 1 3 9 2 4 8 5 6
    9 6 1 5 3 7 2 8 4
    2 8 7 4 1 9 6 3 5
    3 4 5 2 8 6 1 7 9
    """

    board = make_board(puzzle)
    expected_board = make_board(expected)

    try:
        rows, cols, boxes = compute(board)
    except TypeError:
        assert False

    assert solve(board, rows, cols, boxes)

    assert board == expected_board


def test_invalid():
    puzzle = """
    5 5 . . 7 . . . .
    6 . . 1 9 5 . . .
    . 9 8 . . . . 6 .
    8 . . . 6 . . . 3
    4 . . 8 . 3 . . 1
    7 . . . 2 . . . 6
    . 6 . . . . 2 8 .
    . . . 4 1 9 . . 5
    . . . . 8 . . 7 9
    """


    board = make_board(puzzle)

    try:
        rows, cols, boxes = compute(board)
    except TypeError:
        return

    assert False

def test_unsolvable():
    puzzle = """
    8 . . . . . . . .
    . . 3 6 . . . . .
    . 7 . . 9 . 2 . .
    . 5 . . . 7 . . .
    . . . . 4 5 7 . .
    . . . 1 . . . 3 .
    . . 1 . . . . 6 8
    . . 8 5 . . . 1 .
    . 9 . . . . 4 . .
    """


    board = make_board(puzzle)

    try:
        rows, cols, boxes = compute(board)
    except TypeError:
        assert False

    assert solve(board, rows, cols, boxes) is False

