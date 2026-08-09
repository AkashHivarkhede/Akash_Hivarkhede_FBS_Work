# Python Program to count number of digits and letters in a string.

string = str(input('Enter a string :'))

digitCount = 0
lettersCount = 0

for ch in string:
    if (ch >= 'A' and ch <= 'Z') or (ch >= 'a' and ch <= 'z'):
        lettersCount += 1 
    elif ch >= '0' and ch <= '9':
        digitCount += 1 


print('Number of digits :', digitCount)
print('Number of letters :', lettersCount)
