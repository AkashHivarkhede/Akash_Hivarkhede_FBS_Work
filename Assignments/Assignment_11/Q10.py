# Write a program to print list after removing even numbers.


def removeing_even(list):
    new_list = []
    for i in list:
        if i % 2 != 0:
            new_list.append(i)

    return new_list       


list = [1 , 2 , 3 , 4 , 5]
print("Original List:", list)
print("List after removing even numbers:", removeing_even(list))
