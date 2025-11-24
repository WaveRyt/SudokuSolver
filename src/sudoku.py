from typing import List, Set, Optional

ALL_POSSIBLE = set(i for i in range(1, 10))

def box_idx(r: int, c: int) -> int:
    return (r // 3) * 3 + (c // 3)

def solve(board: List[List[str]], rows: List[Set[int]], cols: List[Set[int]], boxes: List[Set[int]]) -> bool:
    best_row, best_col = -1, -1
    best_allowed = None
    best_count = 10

    for r in range(9):
        for c in range(9):
            if board[r][c] == '.':
                allowed = ALL_POSSIBLE.difference(rows[r] | cols[c] | boxes[box_idx(r, c)])

                if not allowed:
                    return False

                cnt = len(allowed)

                if cnt < best_count:
                    best_count = cnt 
                    best_row = r 
                    best_col = c 
                    best_allowed = allowed

                    if best_count == 1:
                        break
        
        if best_count == 1:
            break
    
    if best_row == -1:
        return True
    
    for n in best_allowed:
        rows[best_row].add(n)
        cols[best_col].add(n)
        boxes[box_idx(r, c)].add(n)
        board[r][c] = str(n)

        if solve(board, rows, cols, boxes):
            return True
        
        rows[best_row].remove(n)
        cols[best_col].remove(n)
        boxes[box_idx(r, c)].remove(n)
        board[r][c] = '.'
    
    return False