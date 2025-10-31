import random
import copy


def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)
    return None


def valid(board, num, pos):
    r, c = pos
    # Row
    for j in range(9):
        if board[r][j] == num and j != c:
            return False
    # Column
    for i in range(9):
        if board[i][c] == num and i != r:
            return False
    # Box
    br = (r // 3) * 3
    bc = (c // 3) * 3
    for i in range(br, br + 3):
        for j in range(bc, bc + 3):
            if board[i][j] == num and (i, j) != pos:
                return False
    return True


def solve(board):
    empty = find_empty(board)
    if not empty:
        return True
    r, c = empty
    for num in range(1, 10):
        if valid(board, num, (r, c)):
            board[r][c] = num
            if solve(board):
                return True
            board[r][c] = 0
    return False


def count_solutions(board, limit=2):
    # Count solutions up to `limit` (stop early when >= limit)
    empty = find_empty(board)
    if not empty:
        return 1
    r, c = empty
    total = 0
    for num in range(1, 10):
        if valid(board, num, (r, c)):
            board[r][c] = num
            total += count_solutions(board, limit)
            board[r][c] = 0
            if total >= limit:
                return total
    return total


def generate_full_board():
    board = [[0] * 9 for _ in range(9)]
    # Fill board using backtracking with randomized order
    def fill(board):
        empty = find_empty(board)
        if not empty:
            return True
        r, c = empty
        nums = list(range(1, 10))
        random.shuffle(nums)
        for num in nums:
            if valid(board, num, (r, c)):
                board[r][c] = num
                if fill(board):
                    return True
                board[r][c] = 0
        return False

    fill(board)
    return board


def make_puzzle(full_board, clues=30):
    # Remove numbers from full_board to reach `clues` remaining cells.
    board = copy.deepcopy(full_board)
    cells = [(i, j) for i in range(9) for j in range(9)]
    random.shuffle(cells)
    to_remove = 81 - clues
    for (r, c) in cells:
        if to_remove <= 0:
            break
        backup = board[r][c]
        board[r][c] = 0
        # Ensure uniqueness of solution (try to keep unique)
        if count_solutions(copy.deepcopy(board), limit=2) != 1:
            board[r][c] = backup
        else:
            to_remove -= 1
    return board


def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print('-' * 21)
        row = ''
        for j in range(9):
            if j % 3 == 0 and j != 0:
                row += '| '
            val = board[i][j]
            row += ('. ' if val == 0 else f'{val} ')
        print(row.strip())


def parse_move(s):
    # Expect: r c v  with 1-based indices or commands
    parts = s.strip().split()
    if len(parts) == 3:
        try:
            r = int(parts[0]) - 1
            c = int(parts[1]) - 1
            v = int(parts[2])
            return ('set', r, c, v)
        except ValueError:
            return None
    return None


def play_cli(difficulty='medium'):
    # difficulty -> clues mapping
    diff_map = {'easy': 36, 'medium': 30, 'hard': 24}
    clues = diff_map.get(difficulty, 30)
    full = generate_full_board()
    puzzle = make_puzzle(full, clues=clues)
    state = copy.deepcopy(puzzle)

    print('\nSimple Sudoku CLI')
    print('Commands: "r c v" to set (1-based), "hint" for a hint, "solve" to reveal solution, "quit" to exit')
    while True:
        print('\nCurrent board:')
        print_board(state)
        if state == full:
            print('\nSelamat — Anda menyelesaikan puzzle!')
            break
        cmd = input('\nMasukkan perintah atau gerakan: ').strip().lower()
        if cmd in ('quit', 'q', 'exit'):
            print('Keluar. Terima kasih telah bermain.')
            break
        if cmd == 'solve':
            print('\nSolusi:')
            print_board(full)
            break
        if cmd == 'hint':
            # find an empty cell and show the correct number
            for i in range(9):
                for j in range(9):
                    if state[i][j] == 0:
                        print(f'Hint: baris {i+1} kolom {j+1} = {full[i][j]}')
                        state[i][j] = full[i][j]
                        break
                else:
                    continue
                break
            continue
        move = parse_move(cmd)
        if not move:
            print('Perintah tidak dimengerti. Gunakan format: r c v (mis. "1 3 9") atau hint/solve/quit')
            continue
        _, r, c, v = move
        if not (0 <= r < 9 and 0 <= c < 9 and 1 <= v <= 9):
            print('Indeks atau nilai di luar jangkauan.')
            continue
        if puzzle[r][c] != 0:
            print('Anda tidak boleh mengubah sel yang sudah diberi sebagai clue.')
            continue
        if not valid(state, v, (r, c)):
            print('Gerakan tidak valid menurut aturan Sudoku.')
            continue
        state[r][c] = v


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Simple Sudoku CLI')
    parser.add_argument('--difficulty', '-d', choices=['easy','medium','hard'], default='medium')
    args = parser.parse_args()
    play_cli(args.difficulty)
