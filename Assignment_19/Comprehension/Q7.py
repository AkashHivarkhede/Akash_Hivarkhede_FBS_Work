# Use a nested list comprehension to find all of the numbers from
# 1–1000 that are divisible by any single digit.


numbers = [i for i in range(1, 1001)
           if any(i % j == 0 for j in range(1, 10))]

print(numbers)