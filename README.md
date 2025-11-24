# Sudoku Solver

A Sudoku solving tool implemented in Python for solving **standard 9×9 Sudoku puzzles**.
The program validates the puzzle and solves it using a backtracking algorithm enhanced with the MRV (Minimum Remaining Values) heuristic.

---

## Features

- Solve any **standard 9×9 Sudoku**
- MRV-based heuristic for faster search
- Full validation of rows, columns, and 3×3 boxes
- Clean, modular Python implementation
- Supports input via terminal or file redirection

---

## Files

| File | Description |
|------|-------------|
| `sudoku.py` | Solves the board using backtracking + MRV |
| `input.py` | Board parsing and constraint initialization |
| `main.py` | Entry point for solving puzzles |
| `tests/test_sudoku.py` | Pytest-based unit tests for solvable, unsolvable and invalid cases |

---

## Solver Overview

The solver uses:

### **Backtracking Search**
Systematically fills empty cells and backtracks on conflicts.

### **MRV Heuristic**
Selects the cell with the **fewest possible digits** to reduce branching.

### **Constraint Sets**
Tracks digits present in:
- Each row (`rows[r]`)
- Each column (`cols[c]`)
- Each 3×3 box (`boxes[b]`)

Empty cells are represented by `.`.

---

## Run Instructions

### Solve Interactively

From the project root:

```bash
python src/main.py
```

---

## Running Tests (pytest)

Ensure pytest is installed:

```bash
pip install pytest
```

Run all tests:

```bash
python -m pytest
```
---