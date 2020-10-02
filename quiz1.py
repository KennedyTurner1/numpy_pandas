import pandas as pd

df = pd.read_csv('Holiday Schedule Ranking 2019.csv') #makes a dataframe

schedule = df.set_index('Employee') #set the index as employee
 
flip = schedule.T

my_dict = {}
emp_list = []
index = 0
for column in flip: #for column in dataframe
    rank = flip.sort_values(by=column, ascending=True) #sort every column by the date
    small_list = flip.nsmallest(3, column) #shorten the column to the smallest 3
    '''
    for row in small_list: #for row in shortened column
        
        emp_list.append(employee)
        my_dict[date] = emp_list
    '''
print(rank)

#we need to sort by the rows
