# Python Program to Calculate the Length of a String Without Using a Library Function

string = str(input('Enter a String :'))

length = 0

for i in string:
    length = length + 1 

print("Length of a String :", length)