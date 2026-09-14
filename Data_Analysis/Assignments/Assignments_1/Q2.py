# Write code to replace the odd numbers by -1 in the array created by using random.randint( 1 , 50,20)

import numpy as np

arr = np.random.randint(1, 50 , 20)

print("Original array:")
print(arr)

arr[arr % 2 != 0] = -1

print("Array after replacing odd numbers with -1:")
print(arr)