# Python Program to Sum All the Items in a Dictionary

dict = { 'a': 100, 'b':200, 'c':300 , 'd':400, 'e':500}

sum = 0

for value in dict.values():
    sum += value

print("Sum of all the items in the dictionary:", sum)