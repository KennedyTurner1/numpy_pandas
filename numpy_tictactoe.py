import numpy as np


board = np.array([['', '', ''], 
                  ['', '', ''], 
                  ['', '', '']])
print("This is the starting board")
print(board)

count_row = np.count_nonzero(board == 'X', axis=1)
print(count_row)

count_col = np.count_nonzero(board == 'X', axis=0)
print(count_col)

repeat = True
while repeat:
    if count_row or count_col != 3:
        row_input = int(input("row number: "))
        col_input = int(input("column number: "))
        myarray[row_input, col_input] = 'X'
        print(myarray)
    else:
        repeat = False
        print("user wins!")
