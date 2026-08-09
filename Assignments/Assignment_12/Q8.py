# Python Program to Remove the Characters of Odd Index Values in a String

string = str(input('Enter a String :'))

new_string = ''

for ch in range(len(string)):
    if ch % 2 == 0:
        new_string = new_string + string[ch]

print('Modified String :',new_string)