# Reshape a 3x3 matrix into a 1D array.

import numpy as np

arr = np.array([
    [1 , 2 , 3],
    [4 , 5 , 6],
    [7 , 8 , 9],
])

new_arr = arr.reshape(-1)

print(new_arr)