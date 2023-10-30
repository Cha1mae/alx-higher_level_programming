#!/usr/bin/python3
import sys


def is_safe(board, row, col, n):
    """
    Check if placing a queen at board[row][col] is safe.
    """
    for col_index in range(col):
        if board[row][col_index] == 1:
            return False
    for row_index, col_index in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[row_index][col_index] == 1:
            return False
    for row_index, col_index in zip(range(row, n, 1), range(col, -1, -1)):
        if board[row_index][col_index] == 1:
            return False
    return True


def solve_nqueens(n):
    """
    Solve the N-Queens problem for a board of size n x n.
    """
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_nqueens_util(board, 0, n, solutions)
    return solutions


def solve_nqueens_util(board, col, n, solutions):
    """
    Utility function to solve the N-Queens problem recursively.
    """
    if col == n:
        solution = []
        for row_index in range(n):
            for col_index in range(n):
                if board[row_index][col_index] == 1:
                    solution.append([row_index, col_index])
        solutions.append(solution)
        return True
    res = False
    for row_index in range(n):
        if is_safe(board, row_index, col, n):
            board[row_index][col] = 1
            res = solve_nqueens_util(board, col + 1, n, solutions) or res
            board[row_index][col] = 0
    return res


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    solutions = solve_nqueens(N)
    for sol in solutions:
        print(sol)
