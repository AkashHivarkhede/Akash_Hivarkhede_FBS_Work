# Given a 2D array, find its shape and size. Create a 5x4 array with random integers between
# 1 and 100, and print the shape and size.


import numpy as np


arr = np.random.randint(1,101,20)

arr2D = np.array(arr).reshape(5,4)
# arr2D = np.random.randint(1,101, size=(5,4))

print(arr2D.shape)
print(arr2D.size)