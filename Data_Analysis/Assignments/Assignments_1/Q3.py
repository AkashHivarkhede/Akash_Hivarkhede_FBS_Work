# Perform the following operations on an array of mobile phones prices 6999, 7500,
# 11999, 27899, 14999, 9999.
#         a. Create a 1d-array of mobile phones prices
#         b. Convert this array to float type
#         c. Append a new mobile having price of 13999 Rs. to this array
#         d. Reverse this array of mobile phones prices
#         e. Apply GST of 18% on mobile phones prices and update this array.
#         f. Sort the array in descending order of price
#         g. What is the average mobile phone price
#         h. What is the difference b/w maximum and minimum price

import numpy as np

# a. Create a 1d-array of mobile phones prices
prices = np.array([6999, 7500, 11999, 27899, 14999, 9999])
print("Original prices array:")
print(prices)

# b. Convert this array to float type
prices = prices.astype(float)
print("Prices array after converting to float type:")
print(prices)

# c. Append a new mobile having price of 13999 Rs. to this array
prices = np.append(prices, 13999)
print("Prices array after appending new price:")
print(prices)

# d. Reverse this array of mobile phones prices
prices = prices[::-1]
print("Prices array after reversing:")
print(prices)

# e. Apply GST of 18% on mobile phones prices and update this array.
prices = prices * 1.18
print("Prices array after applying GST of 18%:")
print(prices)

# f. Sort the array in descending order of price
prices = np.sort(prices)[::-1]
print("Prices array after sorting in descending order:")
print(prices)

# g. What is the average mobile phone price
average_price = np.mean(prices)
print("Average mobile phone price:")
print(average_price)

# h. What is the difference b/w maximum and minimum price
difference = np.max(prices) - np.min(prices)
print("Differecne between max and min price:")
print(prices)
