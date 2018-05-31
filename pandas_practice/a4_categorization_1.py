import numpy as np
import pandas as pd
#import tensorflow as tf 
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
bins = [18, 25, 35, 60, 100]


# Also, we can pass a unique name to each label.
bin_names = ['Youth', 'YoungAdult', 'MiddleAge', 'Senior']
new_cats = pd.cut(ages, bins,labels=bin_names)
print(pd.value_counts(new_cats))

#we can also calculate their cumulative sum
# pd.value_counts(new_cats).cumsum()
print(pd.value_counts(new_cats).cumsum())
