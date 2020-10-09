import pandas as pd

series1 = pd.Series([7,11,13,17])

#print(series1)

series2 = pd.Series(100.0, range(5))

#print(series2)

import numpy as np  
random = np.random.randint(0,101,20)
series3 = pd.Series(random)
print(series3.describe())

print(series3)

temperatures = pd.Series([98.6, 98.9, 100.2, 97.9], index=['Julie', 'Charlie', 'Sam', 'Andrea'])
print(temperatures)

mydict = {}
for name, temp in temperatures.items():
    mydict[name] = temp
print(mydict)

series5 = pd.Series(mydict)
print(series5)