# Find the transpose of matrix A and matrix B. Transpose = converting rows into columns and columns into rows 


import numpy as np

A = np.array([
    [1 , 2],
    [3 , 4]
])

B = np.array([
    [5 , 6],
    [7 , 8]
])

Transpose_A = A.T
Transpose_B = B.T 

print('Transpose of A :')
print(Transpose_A)

print('Transpose of B:')
print(Transpose_B)