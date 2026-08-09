# Write a program to create a duplicate of an existing list. It should not point to same list.


list = [10 , 20 , 30 , 40 , 50]

duplicate = []

for i in list:
    duplicate.append(i)


print(id(list))
print(id(duplicate))
