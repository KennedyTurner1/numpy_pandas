'''
use numpy random-number generator to create an array
of twelve random grades in the range 60-100, then reshape
the result into a 3 x 4 array. Calculate the average of all the 
grades, the averages of the grades for each test and
the averages of the grades for each student. 3 students, 4 tests
'''
import numpy as np

grades = np.random.randint(60,101,12).reshape(3,4)

print(grades)

#the average of all the grades

print("All grades", grades.mean())

print("average by each test", grades.mean(axis=0)) #x axis

print("average by each student", grades.mean(axis=1)) #y axis


