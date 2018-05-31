import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf
import numpy as np
data = np.random.randint(1000, size=10000)

print("creating the random 1000 integers out of the size of 100000")
print((data))
