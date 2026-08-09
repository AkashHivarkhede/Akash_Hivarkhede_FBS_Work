# Write a program to remove all occurrences of a given element in the list.


list = [10 , 20 , 30 , 10 , 20 , 10 , 50 , 40]\

num = 10

new_list = []

for i in list:
    if i != num:
        new_list.append(i)

print('Original List :', list)
print('List after removing :' , new_list)