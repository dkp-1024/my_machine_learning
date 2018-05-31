import numpy as np 

#You can concatenate two or more arrays at once.
x = np.array([1, 2, 3])
y = np.array([3, 2, 1])
z = [21,21,21]
print(np.concatenate([x, y,z]))
# array([ 1,  2,  3,  3,  2,  1, 21, 21, 21])

#You can also use this function to create 2-dimensional arrays.
grid = np.array([[1,2,3],[4,5,6]])
print(np.concatenate([grid,grid]))
# array([[1, 2, 3],
#       [4, 5, 6],
#       [1, 2, 3],
#       [4, 5, 6]])

#Using its axis parameter, you can define row-wise or column-wise matrix
print(np.concatenate([grid,grid],axis=1))
# array([[1, 2, 3, 1, 2, 3],
#       [4, 5, 6, 4, 5, 6]])

# ............COMBINING 2D ARRAY WITH 1D ARRAY..................#
x = np.array([3,4,5])
grid = np.array([[1,2,3],[17,18,19]])
print(np.vstack([x,grid]))
# array([[ 3,  4,  5],
#       [ 1,  2,  3],
#       [17, 18, 19]])

#Similarly, you can add an array using np.hstack
z = np.array([[9],[9]])
print(np.hstack([grid,z]))
# array([[ 1,  2,  3,  9],
#       [17, 18, 19,  9]])

# split the arrays based on pre-defined positions
x = np.arange(10)
print(x)
# array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

x1,x2,x3 = np.split(x,[3,6])
print(x1,x2,x3)
# [0 1 2] [3 4 5] [6 7 8 9]

grid = np.arange(16).reshape((4,4))
grid
upper,lower = np.vsplit(grid,[2])
print ("upper part ", upper, '\n', "lower part", lower)
# (array([[0, 1, 2, 3],
#        [4, 5, 6, 7]]), array([[ 8,  9, 10, 11],
#        [12, 13, 14, 15]]))

# YOU CAN DO VARIOUS OPERATIONS ON THE ARRAYS AS WELL







