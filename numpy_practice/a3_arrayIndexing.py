# 27 December 2017 (Wednesday)19:39
import numpy as np 

x1 = np.array([4, 3, 4, 4, 8, 4])
print(x1)
# array([4, 3, 4, 4, 8, 4])

#assess value to index zero
print("this is the 0th index of the array just created", x1[0])
# 4
#assess fifth value
print("this is just the 5th element of just created array", x1[4])
# 8
#get the last value
print("an very elegent way of getting last element of the array just created", x1[-1])
# 4
#get the second last value
print("getting second last element of the array", x1[-2])
# 8

#in a multidimensional array, we need to specify row and column index
x2 = np.array([[3, 7, 5, 5],
      			[0, 1, 5, 9],
      			[3, 0, 5, 0]])
print("a multi-dimensional array - ")
print(x2)

#1st row and 2nd column value
print(x2[2,3])
# 0

#3rd row and last value from the 3rd column
print(x2[2,-1])
# 0

#replace value at 0,0 index
x2[0,0] = 12
print(x2)
# array([[12,  7,  5,  5],
#       [ 0,  1,  5,  9],
#       [ 3,  0,  5,  0]])
