# Python Program to Put Even and Odd elements of a List into two Different Lists

def separate_even_odd(list):
    even_list = []
    odd_list = []

    for i in list:
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)
    
    return even_list , odd_list
    
list = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , 10]

even , odd = separate_even_odd(list)

print('Original List :', list)
print('Evne List :', even)
print('Odd List : ', odd)
