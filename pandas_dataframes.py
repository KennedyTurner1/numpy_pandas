import pandas as pd

grades_dict = {'Wally': [87,96,70], 'Ava': [100,87,90], 
        'Sam' : [94,77,90], 'Katie' : [100,81,82], 
        'Bob' : [83,65,85]}

grades = pd.DataFrame(grades_dict)

print(grades)

#print(grades) #columns are keys, tests are the values

grades.index = ['Test1', 'Test2', 'Test3']

#print(grades)

#print(grades.Sam) #string indexes can have string attributes

#print(grades.loc[['Test1','Test2'],['Ava','Katie']]) #location method, grab all of test one scores

print(grades.iloc[1]) #give the index rather than the name, test 2 

#print(grades.iloc[0:2]) #shows all exams

#print(grades)

#print(grades[grades>90]) #Nan is a pandas representation of not a number.

#print(grades[(grades>=80) & (grades<90)]) #grades between 80 and 89

#print(grades.at['Test2','Ava']) 

#grades.at['Test2','Ava'] = 100 #permanent change

#print(grades)

#print(grades.iat[1,2]) #77, row[1], column[2]

#grades.iat[1,2] = 87

#print(grades)

#pd.set_option('precision',2) #sets the entire program to 2 decimal points

#print(grades.describe()) #gives a lot of info

#we want the average of the test, not the average of the student

#print(grades.T) #tests and columns and students as rows

#print(grades.T.mean()) #transpose the tests

#let's do some sorting

#we can sort by indexes or sort by values

#print(grades.sort_index(ascending=False)) #it changed the order of the tests, #default axis is 0 (axis of the rows)

#print(grades.sort_index(axis=1)) #axis 0 is by rows, axis 1 is columns

#sort by values

#print(grades.sort_values(by='Test1', axis=1, ascending=False))

#print(grades.T.sort_values(by='Test1', ascending=False))

#print(grades.loc['Test1'].sort_values(ascending=False))