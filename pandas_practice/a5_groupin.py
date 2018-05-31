import numpy as np
import pandas as pd
#import tensorflow as tf 
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
'''
Let's proceed and learn about grouping data and creating pivots in pandas. 
It's an immensely important data analysis method which you'd probably have to use on every data set you work with.
'''

df = pd.DataFrame({'key1' : ['a', 'a', 'b', 'b', 'a'],
                   'key2' : ['one', 'two', 'one', 'two', 'one'],
                   'data1' : np.random.randn(5),
                   'data2' : np.random.randn(5)})
print(df)

#calculate the mean of data1 column by key1
grouped = df['data1'].groupby(df['key1'])
print(grouped.mean())
