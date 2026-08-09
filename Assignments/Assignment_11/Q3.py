# Python Program to Sort the List According to the Second Element in Sublist

def sort_second_ele(list):
    for i in range(len(list)):
        for j in range(len(list) - i - 1):
            if list[j][1] > list[j + 1][1]:
                list[j][1] , list[j + 1][1] = list[j + 1][1] , list[j][1]


list = [[1, 5], [3, 2], [2, 8], [4, 1]]
print('Original List :' , list)
sort_second_ele(list)
print('Sorted List :', list)