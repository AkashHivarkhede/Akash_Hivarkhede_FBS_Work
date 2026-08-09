# Python Program to Count the Number of Vowels in a String

string = str(input('Enter a string :'))
count = 0
for ch in string:
    if ch in "aeiou":
        count = count + 1

print('Number of Vowels in String :', count)