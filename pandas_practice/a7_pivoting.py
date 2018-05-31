import numpy as np
import pandas as pd
#import tensorflow as tf 
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

#create a data frame
data = pd.DataFrame({'group': ['a', 'a', 'a', 'b','b', 'b', 'c', 'c','c'],
                 'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})
print(data)

#calculate means of each group
data.pivot_table(values='ounces',index='group',aggfunc=np.mean)

#calculate count by each group
print(data.pivot_table(values='ounces',index='group',aggfunc='count'))
