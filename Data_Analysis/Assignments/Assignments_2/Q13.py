# Create a 4x4 array of random integers. Find the maximum, minimum, and mean of the entire array.

import numpy as np

arr = np.random.randint(1, 100 , size = (4,4))

print(arr)
print()

print('Maximum :' , np.max(arr))
print('Minimum :' , np.min(arr))
print('Mean :' , np.mean(arr))