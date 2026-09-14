# Create a 1D array of 12 elements. Reshape it into a 3x4 2D array.

import numpy as np

arr = np.arange(1,13)

reshape = arr.reshape(3,4)

print(reshape)