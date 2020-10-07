
import pandas as pd

file_object = open('Holiday Schedule Ranking 2019.csv', 'r') #open file

data = pd.read_csv(file_object, index_col=0).T #makes a dataframe with index 'employee'
                                            #df with preferences

file_object.close() #close file

file_object = open('Holiday Schedule Ranking 2019.csv', 'r') #open file again

schedule = pd.read_csv(file_object, index_col=0) #create empty dataframe

for column in schedule.columns: #put 0 as the value for all columns
    schedule[column].values[:] = 0

data['SUM of DATE'] = data.apply(lambda x:x.sum(), axis=1) #adding column

data = data.sort_values(by='SUM of DATE', ascending=False) #sorting by column

data = data.T #transpose back

import numpy as np

for date in data.columns: #for column in dataframe
    date_series=data[date].nsmallest(5, keep='all') #shorten the row to the smallest 5 in case of  tie
    total_scheduled = 0 #employees per date can't be more than 4
    for employee, preference in date_series.items(): #for row in shortened column 
        if schedule.loc[employee][:].count() > 2 and total_scheduled >= 3: #I really did try to look up the count non zeros professor b 
            schedule.at[employee, date] = 0
        else:
            schedule.at[employee, date] = preference
            total_scheduled += 1
        
schedule.replace(0,'',inplace=True)

print(schedule)

schedule.to_csv('Final_Schedule.csv')

print('DONE')

