'''
create an empty board              [[,,,]
                                    [,,,]
                                    [,,,]]
print to screen
initialize a boolean variable
repeat = True
while repeat = True
1. ask for row, column (2,2)
2. place the item on the board 
3. print the board                 [[,,,]
                                    [,X,]
                                    [,,,]]
4. Count the X's by the row's & columns
5. if any element in array = 3, the user wins!
6. get computer 
7. while board[row,column] == 'X' or 'O':
        repeat getrow and column
8. put it on the board
9. print board
10. get row count and column count for computer by using rand.int
11. if the element is occupied move to the next row, column 
11. Count the X's by the row's & columns
12. if any element in array = 3, the computer wins!
13. Repeat False if computer wins

Don't worry about the first or second user thing

count_row = np.count_nonzero(myarray == 'X', axis=1)
print(count_row)

count_vol = np.count_nonzero(myarray == 'X', axis=0)
print(count_col)
'''