# Python Program to Find the Second Largest Number in a List Using Bubble Sort

def second_largest(list):
    size = len(list)
    for i in range(1 , size):
        for j in range(0 , size - i):
            if list[j] > list[j + 1]:
                list[j] , list[j + 1] = list[j + 1] , list[j]

    print('Second Largest :' , list[-2])


list = [10 , 5 , 20 , 30 , 25 , 15 , 35 , 50 , 45]
second_largest(list)

