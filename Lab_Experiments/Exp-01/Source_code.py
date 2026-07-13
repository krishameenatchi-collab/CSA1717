# 8 Queens Problem using Backtracking
N = 8
board = [[0 for _ in range(N)] for _ in range(N)]
def is_safe(board, row, col):
    # Check left side of current row
    for i in range(col):
        if board[row][i] == 1:
            return False
    # Check upper-left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    # Check lower-left diagonal
    i, j = row, col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1
    return True
def solve(board, col):
    if col >= N:
        return True
    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = 1
            if solve(board, col + 1):
                return True
            board[i][col] = 0
    return False
if solve(board, 0):
    print("Solution Found:\n")
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()
else:
    print("No solution exists.")
