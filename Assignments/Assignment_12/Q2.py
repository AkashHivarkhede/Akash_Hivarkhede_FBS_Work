# Python Program to Remove the nth Index Character from a Non-Empty String

string = str(input("Enter a string :"))

n = int(input('Enter the index to remove :'))

result = ''
i = 0 

while i < len(string):
    if i != n:
        result = result + string[i]

    i = i + 1

print("Origanal String :" , string)
print("Modified String :" , result)

