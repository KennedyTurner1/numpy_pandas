import numpy as np
import random

print("Let's play Tic-Tac-Toe!")
print("You will play X's and the computer will play O's")

board = np.full((3,3),'')

print("This is the starting board")
print(board)

repeat = True
while repeat == True:
    print("Place the X based on the row/column position, not the index value")
    row_input = int(input("row number: "))
    col_input = int(input("column number: "))
    row = row_input - 1
    col = col_input - 1
    board[row, col] = 'X'
    count_row = np.count_nonzero(board == 'X', axis=1)
    count_col = np.count_nonzero(board == 'X', axis=0)
    print(f"This is your move \n {board}")
    if count_row[0] == 3 or count_row[1] == 3 or count_row[2] == 3:
        print("You got 3 X's in a row, you win!")
        repeat = False
    elif count_col[0] == 3 or count_col[1] == 3 or count_col[2] == 3:
        print("You got 3 X's in a column, you win!")
        repeat = False
    elif board[0,0] == "X" and board[1,1] == "X" and board[2,2] == "X":
        print("You got 3 X's in a diagonal, you win!")
        repeat = False
    if repeat:
        c_row_input = random.randint(0,2) #try this 
        c_col_input = random.randint(0,2)
        while board[c_row_input, c_col_input] == "X" or board[c_row_input, c_col_input] == "O": #if spot is filled
            c_row_input = random.randint(0,2) #get a new spot until it's not filled
            c_col_input = random.randint(0,2)
        board[c_row_input, c_col_input] = 'O' #place computers spot
        print(f"This is computer's move \n {board}")
        c_count_row = np.count_nonzero(board == 'O', axis=1)
        c_count_col = np.count_nonzero(board == 'O', axis=0)
        if c_count_row[0] == 3 or c_count_row[1] == 3 or c_count_row[2] == 3:
            print("The computer got 3 O's in a row, you lose.")
            repeat = False
        elif c_count_col[0] == 3 or c_count_col[1] == 3 or c_count_col[2] ==3:
            print("The computer got 3 O's in a column, you lose.")
            repeat = False
        elif board[0,0] == "O" and board[1,1] == "O" and board[2,2] == "O":
            print("You got 3 O's in a diagonal, you lose.")
            repeat = False
                
