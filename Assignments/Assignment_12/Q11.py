# Python Program to count number of lowercase characters in a string.

string = str(input('Enter a String :'))

count = 0

for ch in string:
    if ch >= 'a' and ch <= 'z':
        count += 1

print('Number of lowercase characters :', count)