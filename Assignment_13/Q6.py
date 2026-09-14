# Python Program to Multiply All the Items in a Dictionary

dict = { 'a': 5, 'b':5, 'c':5 }

mul = 1

for value in dict.values():
    mul *= value

print("Multiplication of all the items in the dictionary:", mul)