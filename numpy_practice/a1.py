#load the library and check its version, just to make sure we aren't using an older version
import numpy as np
print(np.__version__)
#'1.12.1'

#create a list comprising numbers from 0 to 9
L = list(range(10))

#converting integers to string - this style of handling lists is known as list comprehension.
#List comprehension offers a versatile way to handle list manipulations tasks easily. We'll learn about them in future tutorials. Here's an example.  

[str(c) for c in L]
print(L)
[print(type(item)) for item in L]

