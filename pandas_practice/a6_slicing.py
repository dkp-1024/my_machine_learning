import numpy as np
import pandas as pd
#import tensorflow as tf 
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

dates = pd.date_range('20130101',periods=6)
df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
# print(df)

#get first n rows from the data frame
print(df[:3])

#slice based on date range
print(df['20130101':'20130104'])

#slicing based on column names
print(df.loc[:,['A','B']])

#slicing based on both row index labels and column names
df.loc['20130102':'20130103',['A','B']]

#slicing based on index of columns
df.iloc[3] #returns 4th row (index is 3rd)
# A    0.918203
# B   -0.158800
# C   -0.964063
# D   -1.990779
# Name: 2013-01-04 00:00:00, dtype: float64


#returns a specific range of rows
df.iloc[2:4, 0:2]

#returns specific rows and columns using lists containing columns or row indexes
df.iloc[[1,5],[0,2]] 

'''
Similarly, we can do Boolean indexing based on column values as well. 
This helps in filtering a data set based on a pre-defined condition.
'''

print(df[df.A > 1])

#we can copy the data set
df2 = df.copy()
df2['E']=['one', 'one','two','three','four','three']
print(df2)

#select rows based on column values
df2[df2['E'].isin(['two','four'])]

#select all rows except those with two and four
df2[~df2['E'].isin(['two','four'])]

#list all columns where A is greater than C
df.query('A > C')

#using OR condition
df.query('A < B | C > A')






