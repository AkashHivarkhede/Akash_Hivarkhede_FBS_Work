# Create a 3x3 array of integers and access:
#     a. The second element of the first row.
#     b. The third column of the 2nd row.
#     c. A subarray with the first two rows and last two columns.


import numpy as np

arr = np.arange(1 , 10).reshape(3,3)

#  a. The second element of the first row.

# print(arr[0][1])
print(arr[0,1])

# b. The third column of the 2nd row.
print(arr[1][2])

# c. A subarray with the first two rows and last two columns.
print(arr[0:2 , 1:3])
