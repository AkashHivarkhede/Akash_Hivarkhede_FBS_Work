# Write a program to find sum of all elements of list

def sum_of_num(list):
    total = 0
    for i in range(len(list)):
        total += list[i] 
    
    return total

numbers = [10 , 20 , 30 , 40 , 50]


print('List :' , numbers)
print('Sum :' , sum_of_num(numbers))