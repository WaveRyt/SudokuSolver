import sys
from sudoku import solve
from input import make_board, compute

def main():
    print("Enter the Sudoku Board")
    print("Enter each row in a line, each cell separated by space. Use '.' for empty cells")

    board = make_board()
    
    try:
        rows, cols, boxes = compute(board)
    except TypeError:
        return
    
    if solve(board, rows, cols, boxes):
        print("Solved")

        for row in board:
            print(* row)
    else:
        print("No Solution Found")

if __name__ == "__main__":
    main()