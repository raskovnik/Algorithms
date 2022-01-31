board = [[7,0,2,0,5,0,6,0,0],
        [0,0,0,0,0,3,0,0,0],
        [1,0,0,0,0,9,5,0,0],
        [8,0,0,0,0,0,0,9,0],
        [0,4,3,0,0,0,7,5,0],
        [0,9,0,0,0,0,0,0,8],
        [0,0,9,7,0,0,0,0,5],
        [0,0,0,2,0,0,0,0,0],
        [0,0,7,0,4,0,2,0,3]]

def print_board(board):
    for r in board:
        print(r)
    print("\n")

def is_in_column(board, col, number):
    for row in range(0, 9):
        if board[row][col] == number: return True
    return False

def is_in_row(board, row, number):
    for col in range(0, 9):
        if board[row][col] == number: return True
    return False

def is_in_box(board, row, col, number):
    l_row = row - row % 3
    l_col = col - col % 3
    for i in range(l_row, l_row + 3):
        for j in range(l_col, l_col + 3):
            if board[i][j] == number: return True
    return False

def is_valid_position(board, row, col, number):
    if not is_in_column(board, col, number) and not is_in_row(board, row, number) and not is_in_box(board, row, col, number): return True; False

def solve(board):
    empties = 0
    for i in range(0, 9):
        for j in range(0, 9):
            if board[i][j] == 0:
                for num in range(1, 10):
                    if is_valid_position(board, i, j, num):
                        board[i][j] = num
                        if solve(board) == True: return True; 
                        else:
                            board[i][j] = 0
                            empties+=1

                return False
    return empties == 0

if __name__ == "__main__":
    print_board(board)
    if solve(board) == True:
        print("Solved:\n")
        print_board(board)
    else: print("Board cannot be solved")
