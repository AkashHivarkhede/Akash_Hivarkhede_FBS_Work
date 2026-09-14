# Find the row-wise and column-wise sums.

import numpy as np

arr = np.array([
    [1 , 2 , 3],
    [4 , 5 , 6],
    [7 , 8 , 9]
])

print('Row-wise Sum :' , np.sum(arr, axis=1))
print('Column-wise Sum :' , np.sum(arr, axis=0))