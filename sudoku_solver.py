def print_board(board):
    """
    Prints the Sudoku board in a tabular format.
    """
    for row in board:
        print("| " + " | ".join(str(num) for num in row) + " |")

def solve_sudoku(board):
    """
    Solves a Sudoku puzzle using the backtracking algorithm.
    """
    row, col = find_next_empty(board)
    
    if row is None:
        return True

    for num in range(1, 10):
        if is_valid_move(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            
            board[row][col] = 0
    
    return False

def find_next_empty(board):
    """
    Finds the next empty cell on the board.
    """
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col
    return None, None

def is_valid_move(board, row, col, num):
    """
    Checks if a number is valid in the given cell.
    """
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
        
    box_row = (row // 3) * 3
    box_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[box_row+i][box_col+j] == num:
                return False
    
    return True

board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
]
solve_sudoku