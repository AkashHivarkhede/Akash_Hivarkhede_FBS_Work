# Write a program to create a new list from existing list which contains cube of each number of list.


def cube_fun(list):
    result = []
    for i in range(len(list)):
        res = list[i]
        res = res * res * res
        result.append(res)
    return result


list = [1 , 2 , 3 , 4 , 5]

result = cube_fun(list)
print('Cube List:',result)


def cubefun(numbers):
    newList = []
    for i in numbers:
        newList.append(i ** 3)
    return newList

numbers = [1 , 2 , 3 , 4 , 5]

print('Original List:', numbers)
print('Cube List:' , cube_fun(numbers))

