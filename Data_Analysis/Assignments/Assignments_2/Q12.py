# Create a 3x3 array and a 1D array with 3 elements. Add the 1D array to the 2D array.
# Explain how broadcasting works in this operation.

import numpy as np

arr2D = np.arange(1,10).reshape(3,3)
arr = np.array([1 , 2 , 3])

print(arr2D)
print()
print('Addition :\n' , arr + arr2D)

