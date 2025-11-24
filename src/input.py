import sys
from typing import List, Tuple, Set
from sudoku import box_idx

def make_board() -> List[List[str]]:
    board = []

    for line in sys.stdin:
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
    
        if len(board) == 9:
            return board

def compute(board: List[List[str]]) -> Tuple[List[Set[int]], List[Set[int]], List[Set[int]]]:
    rows = [set() for i in range(9)]
    cols = [set() for i in range(9)]
    boxes = [set() for i in range(9)]

    for r in range(9):
        for c in range(9):
            ch = board[r][c]

            if ch != '.':
                num = int(ch)
                if num in rows[r] or num in cols[c] or num in boxes[box_idx(r, c)]:
                    print("Invalid puzzle\n")
                    return

                rows[r].add(num)
                cols[c].add(num)
                boxes[box_idx(r, c)].add(num)
    
    return rows, cols, boxes
