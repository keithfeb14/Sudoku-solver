import numpy as np

def sudoku_solver(sudoku):
    def is_grid_valid(sudoku):  #Initally checks if the input grid is a valid input. 
        for row in range(9):
            for col in range(9):
                num = sudoku[row, col]
                if num != 0:
                    sudoku[row, col] = 0
                    if not valid_num(sudoku, row, col, num):
                        return False
                    sudoku[row, col] = num
        return True

    def valid_num(sudoku, row, col, num): # Check if the number already exists in the same row, column, or box
        if num in sudoku[row]:
            return False
        if num in sudoku[:, col]:
            return False
        #Checking 3x3 box 
        row_start = (row // 3) * 3
        col_start = (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if sudoku[row_start + i, col_start + j] == num:
                    return False
        return True




    def solve(sudoku): #DFS backtracking search done recursively 
        for row in range(9):
            for col in range(9):
                if sudoku[row, col] == 0:
                    for num in range(1, 10):
                        if valid_num(sudoku, row, col, num):
                            sudoku[row, col] = num
                            if solve(sudoku):
                                return True
                            sudoku[row, col] = 0
                    return False
        return True

    if not is_grid_valid(sudoku):
        return np.full((9, 9), -1)

    solved_sudoku = np.copy(sudoku)
    if solve(solved_sudoku):
        return solved_sudoku
    else:
        return np.full((9, 9), -1)
