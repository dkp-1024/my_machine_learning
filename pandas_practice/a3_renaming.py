import numpy as np
import pandas as pd
# import tensorflow as tf 
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
'''
how to rename column names and axis (row names).
'''
data = pd.DataFrame(np.arange(12).reshape((3, 4)),index=['Ohio', 'Colorado', 'New York'],columns=['one', 'two', 'three', 'four'])
# print(data)

#Using rename function
data.rename(index = {'Ohio':'SanF'}, columns={'one':'one_p','two':'two_p'},inplace=True)
# print(data)

#You can also use string functions
data.rename(index = str.upper, columns=str.title,inplace=True)
# print(data)

