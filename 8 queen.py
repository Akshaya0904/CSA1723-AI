N = 8

def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or abs(board[i]-col) == abs(i-row):
            return False
    return True

def solve(board, row):
    if row == N:
        for i in range(N):
            line = ""
            for j in range(N):
                line += "Q " if board[i] == j else ". "
            print(line)
        print("\nResult: Hence, the simple python program for 8-Queen problem is done.")
        return True
    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            if solve(board, row+1):
                return True
    return False

board = [-1]*N
solve(board, 0)
