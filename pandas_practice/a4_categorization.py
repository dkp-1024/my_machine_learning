# 27 December 2017 (Wednesday)22:32
import numpy as np
import pandas as pd
#import tensorflow as tf 
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

# we'll learn to categorize (bin) continuous variables.
ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
# We'll divide the ages into bins such as 18-25, 26-35,36-60 and 60 and above.

#Understand the output - '(' means the value is included in the bin, '[' means the value is excluded
bins = [18, 25, 35, 60, 100]
cats = pd.cut(ages, bins)
print(cats)
# [(18, 25], (18, 25], (18, 25], (25, 35], (18, 25], ..., (25, 35], (60, 100], (35, 60], (35, 60], (25, 35]]
# Length: 12
# Categories (4, object): [(18, 25] < (25, 35] < (35, 60] < (60, 100]]


#To include the right bin value, we can do:
print(pd.cut(ages,bins,right=False))
# [[18, 25), [18, 25), [25, 35), [25, 35), [18, 25), ..., [25, 35), [60, 100), [35, 60), [35, 60), [25, 35)]
# Length: 12
# Categories (4, object): [[18, 25) < [25, 35) < [35, 60) < [60, 100)]


#pandas library intrinsically assigns an encoding to categorical variables.
# print(cats.labels)
print(cats.codes)
# array([0, 0, 0, 1, 0, 0, 2, 1, 3, 2, 2, 1], dtype=int8)


#Let's check how many observations fall under each bin
print(pd.value_counts(cats))
# print(cats)
# (18, 25]     5
# (35, 60]     3
# (25, 35]     3
# (60, 100]    1
# dtype: int64

