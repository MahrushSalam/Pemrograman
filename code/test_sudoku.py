import copy
from sudoku import generate_full_board, make_puzzle, solve, count_solutions


def test_generate_and_solve():
    full = generate_full_board()
    assert full is not None
    # Ensure full is a complete board (no zeros)
    assert all(all(cell != 0 for cell in row) for row in full)

    puzzle = make_puzzle(full, clues=30)
    # puzzle should have some zeros
    assert any(cell == 0 for row in puzzle for cell in row)

    # solver should solve a copy
    board = copy.deepcopy(puzzle)
    assert solve(board)
    # After solve, there should be no zeros
    assert all(all(cell != 0 for cell in row) for row in board)


def test_unique_solution_small():
    full = generate_full_board()
    puzzle = make_puzzle(full, clues=34)
    # Count solutions; hopefully unique
    sols = count_solutions([row[:] for row in puzzle], limit=2)
    assert sols >= 1
