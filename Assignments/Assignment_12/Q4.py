# Python Program to Form a New String where the First Character and
# the Last Character have been Exchanged


string = str(input('Enter a String :'))

# new_string = string[-1] + string[1:-1] + string[0]

# print(new_string)

new_string = ''

new_string = new_string + string[len(string) - 1] 

i = 1 

while i < len(string) - 1:
    new_string = new_string + string[i] 
    i = i + 1 


new_string = new_string + string[0]


print('Original String :' , string)
print('New String :' , new_string)