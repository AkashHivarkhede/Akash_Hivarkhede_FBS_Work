# Python Program to find larger string without using built-in functions.

str1 = "Python"
str2 = "Programming"

count1 = 0
count2 = 0

for char in str1:
    count1 += 1

for char in str2:
    count2 += 1

if count1 > count2:
    print("Larger string:", str1)
elif count2 > count1:
    print("Larger string:", str2)
else:
    print("Both strings are equal in length")