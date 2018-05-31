import numpy as np 
x = np.arange(10)
print(x)
# array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

#from start to 4th position
print(x[:5])
# array([0, 1, 2, 3, 4])

#from 4th position to end
print(x[4:])
# array([4, 5, 6, 7, 8, 9])

#from 4th to 6th position
print(x[4:7])
# array([4, 5, 6])

#return elements at even place
print(x[ : : 2])
# array([0, 2, 4, 6, 8])

#return elements from first position step by two
print(x[1::2])
# array([1, 3, 5, 7, 9])

#reverse the array
print(x[::-1])
# array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])