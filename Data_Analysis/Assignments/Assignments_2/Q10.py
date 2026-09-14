# Create a 2x2 matrix A and a 2x2 matrix B. Perform matrix multiplication using np.dot() or
# the @ operator.

import numpy as np

A = np.array([
    [1 , 2],
    [3 , 4]
])

B = np.array([
    [5 , 6],
    [7 , 8]
])

print('Multiplication Using np.dot :\n' , np.dot(A , B))
print('Multiplication Using @ operator :\n' , A @ B)