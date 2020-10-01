import numpy as np
'''
grades = np.array([[87, 96, 70], [100, 87, 90],[94, 77, 90],
                   [100, 81, 82]])



grades.sum()

grades.min()

grades.max()

grades.mean()

grades.std()

grades.var()


Many calculation methods can be performed on specific array dimensions,
known as the array’s axes. These methods receive an axis keyword argument
that specifies which dimension to use in the calculation, giving you a
quick way to perform calculations by row or column in a two-dimensional array.

grades.mean(axis=0)

# So 95.25 above is the average of the first column’s grades (87, 100, 94 and 100)

# specifying axis=1 performs the calculation on all the column values
# within each individual row. To calculate each student’s average grade for
# all exams, we can use:

grades.mean(axis=1)



NumPy offers dozens of standalone universal functions (or ufuncs) that perform various element-wise operations.


#Let’s create an array and calculate the square root of its values, using the sqrt universal function:

numbers = np.array([1,4,9,16,25,36])

np.sqrt(numbers)


# Let’s add two arrays with the same shape, using the add universal function:

numbers2 = np.arange(1, 7) * 10

np.add(numbers, numbers2)



# Let’s use the multiply universal function to multiply every element of numbers2 by the scalar value 5:

np.multiply(numbers2, 5)


# Let’s reshape numbers2 into a 2-by-3 array, then multiply its values by a one-dimensional array of three elements:

numbers3 = numbers2.reshape(2, 3)

numbers4 = np.array([2, 4, 6])

np.multiply(numbers3, numbers4)

 This works because numbers4 has the same length as each row of numbers3, so NumPy can apply the multiply operation by
 treating numbers4 as if it were the following array:

array([[2, 4, 6],
[2, 4, 6]]    


# Indexing and Slicing

# To select an element in a two-dimensional array, specify a tuple containing the element’s row and column indices
# in square brackets (as in snippet [4]):

grades = np.array([[87, 96, 70], [100, 87, 90],
                   [94, 77, 90], [100, 81, 82]])


grades[0, 1] # row 0, column 1
#96


# To select a single row, specify only one index in square brackets:
grades[1]
#array([100,  87,  90])


# To select multiple sequential rows, use slice notation (remember upper limit is not included):
grades[0:2]
#array([[ 87,  96,  70],
#       [100,  87,  90]])


# To select multiple non-sequential rows, use a list of row indices:
grades[[1, 3]]
#array([[100,  87,  90],
#       [100,  81,  82]])


# You can select subsets of the columns by providing a tuple specifying the row(s) and column(s) to select.
# Each can be a specific index, a slice or a list. Let’s select only the elements in the first column:

grades[:, 0]

# The 0 after the comma indicates that we’re selecting only column 0.

# The : before the comma indicates which rows within that column to select. In this case, : is a slice representing all rows.


# You can select consecutive columns using a slice:

grades[:, 1:3]
array([[96, 70],
       [87, 90],
       [77, 90],
       [81, 82]])  


# or specific columns using a list of column indices:

grades[:, [0, 2]]

array([[ 87,  70],
       [100,  90],
       [ 94,  90],
       [100,  82]])




Use NumPy random-number generation to create an array of twelve random grades
in the range 60 through 100, then reshape the result into a 3-by-4 array.
Calculate the average of all the grades, the averages of the grades for each test
and the averages of the grades for each student.

import numpy as np

grades = np.random.randint(60, 101, 12).reshape(3, 4)

print(grades)

array([[94, 72, 76, 91],
       [65, 78, 66, 70],
       [65, 60, 63, 72]])

grades.mean()
Out[4]: 72.66666666666667

grades.mean(axis=0)
Out[5]: array([74.66666667, 70.        , 68.33333333, 77.66666667])

grades.mean(axis=1)
Out[6]: array([83.25, 69.75, 65. ])




#Shallow copies (view), create a view to the original array

#The array method view returns a new array object with a view of the original array

numbers = np.arange(1, 6)
#array([1, 2, 3, 4, 5])


numbers2 = numbers.view() #not a copy, just a view
#but a change to a view will be a change to the original
#array([1, 2, 3, 4, 5])


print(numbers2)
#To prove that numbers2 views the same data as numbers, let’s modify an element in numbers,

numbers[1] *= 10

print(numbers)
print(numbers2)
#array([ 1, 20, 3, 4, 5])


#Similarly, changing a value in the view also changes that value in the original array:
numbers2[1] /= 10

print(numbers)
#array([1, 2, 3, 4, 5])


#Slice Views

#Slices also create views. Let’s make numbers2 a slice that views only the first three elements of numbers:

numbers2 = numbers[0:3]

print(numbers2)

#array([1, 2, 3])

#to verify it is a view, lets modify an element in the original array and see the view array
numbers[1] *= 20



print(numbers2) #changes the second element in numbers 2 as well.
#array([ 1, 40, 3])



#Deep copies
#The array method copy returns a new array object with a deep copy of the original array

numbers2 = numbers.copy() #view and copy are differenet

#print(numbers2)


# To prove that numbers2 has a separate copy of the data in numbers, let’s modify an element in numbers,
# then display both arrays:

numbers[1] *= 10

#print(numbers)
#array([ 1, 20, 3, 4, 5])


#print(numbers2)
#array([ 1, 2, 3, 4, 5])



#The array methods reshape and resize both enable you to change an array’s dimensions. Method reshape returns a
#view (shallow copy) of the original array with the new dimensions. It does not modify the original array:


grades = np.array([[87, 96, 70], [100, 87, 90]]) #2 students, 3 tests each


print(grades.reshape(1, 6)) #1 row, 6 columns, just creates a view

#array([[ 87, 96, 70, 100, 87, 90]])

#Method resize modifies the original array’s shape:


grades.resize(1, 6)

#array([[ 87, 96, 70, 100, 87, 90]])



#Method flatten deep copies the original array’s data:

flattened = grades.flatten() #puts it in one row


#alternatively, Method ravel produces a view (shallow copy) of the original array, which shares the grades array’s data:


raveled = grades.ravel() #put it in one row, same as flatten

print(grades)

print(raveled)

#confirm that they share the same data

raveled[0] = 100

print(grades)

raveled[6] = 99
#this will give an error. Why? index error

raveled[5] = 99

#since it is a view (shallow copy) and they share the same data, we can look at grades to see that the 6th element has been updated.
print(grades)




#You can quickly transpose an array’s rows and columns—that is “flip” the array, so the rows become the columns and
#the columns become the rows. The T attribute returns a transposed view (shallow copy) of the array. 

grades.T


#Transposing does not modify the original array:
grades


#You can combine arrays by adding more columns or more rows—known as horizontal stacking and vertical stacking.
'''
#HSTACK, stacks horizontally
#Let’s assume grades2 represents three additional exam grades for the two students in the grades array.

grades = np.array([[87, 96, 70], [100, 87, 90]]) 
grades2 = np.array([[94, 77, 90], [100, 81, 82]])

#We can combine grades and grades2 with NumPy’s hstack
h_grades = np.hstack((grades, grades2))

#new array
print(h_grades)

#old array is not affected
print(grades)


#VSTACK, stacks vertically

#let’s assume that grades2 represents two more students’ grades on three exams.
v_grades = np.vstack((grades, grades2))
print(v_grades)



























