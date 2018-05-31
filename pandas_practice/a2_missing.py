# 27 December 2017 (Wednesday)22:17
import pandas as pd
import numpy as np  
'''
A quick method for imputing missing values is by filling the missing value with any random number. 
Not just missing values, you may find lots of outliers in your data set, which might require replacing. 
Let's see how can we replace values.
'''

#Series function from pandas are used to create arrays
data = pd.Series([1., -999., 2., -999., -1000., 3.])
print(data)

#replace -999 with NaN values
data.replace(-999, np.nan,inplace=True)
print(data)

data.drop(data.index, inplace = True)

#We can also replace multiple values at once.
data = pd.Series([1., -999., 2., -999., -1000., 3.])
data.replace([-999,-1000],np.nan,inplace=True)
print(data)

