# Python Program to Replace all Occurrences of ‘a’ with $ in a String

text = str(input('Enter a string :'))

result = ''

for ch in text:
    if ch == 'a':
        result += '$'
    else:
        result += ch 

print("Original String :" , text)
print("Modified String :" , result)

