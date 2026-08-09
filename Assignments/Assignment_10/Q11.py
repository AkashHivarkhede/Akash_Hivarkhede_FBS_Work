# Write a program to print all numbers which are divisible by m and n in the list.

numbers = [10, 15, 20, 30, 40, 60, 90]

m = int(input('Enter m :'))
n = int(input('Enter n :'))

for i in numbers:
    if i % n == 0 and i % m == 0:
        print(i)