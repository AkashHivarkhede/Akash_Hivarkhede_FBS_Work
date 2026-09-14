# Create two arrays of shape (2, 3): arr1 and arr2. Perform element-wise addition,
# subtraction, multiplication, and division on them.

import numpy as np

arr1 = np.array([
    [1 , 2 , 3],
    [4 , 5 , 6]
])


arr2 = np.array([
    [7 , 8 , 9],
    [10 , 11 , 12]
])

addition = arr1 + arr2
print('Addition :')
print(addition)

subtraction = arr2 - arr1
print('Subtraction :')
print(subtraction)

multiplication = arr2 * arr1
print('Multiplication :')
print(multiplication)

division = arr2 / arr1
print('Division :')
print(division)