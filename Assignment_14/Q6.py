# Write a Python program to find the two numbers whose product is
# maximum among all the pairs in a given list of numbers. Use the Python set.

numbers = [2, 5, 3, 8, 6, 4]

num_set = set(numbers)

maximum = 0
pair = ()

for i in num_set:
    for j in num_set:

        if i != j:
            product = i * j

            if product > maximum:
                maximum = product
                pair = (i, j)

print("Two numbers:", pair)
print("Maximum product:", maximum)