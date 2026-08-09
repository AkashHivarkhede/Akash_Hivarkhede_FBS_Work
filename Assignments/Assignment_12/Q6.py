# Python Program to Take in a String and Replace Every Blank Space with Hyphen


string = str(input('Enter a String :')) 

new_string = ''

for ch in string:

    if ch == ' ': 
        new_string = new_string + '-' 
    else:
        new_string = new_string + ch


print('Original String :', string)
print('Modified String :', new_string)