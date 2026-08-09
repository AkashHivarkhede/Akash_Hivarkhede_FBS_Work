# Python Program to Merge Two Lists and Sort it

def bubble_sort(ml):
    size = len(ml)
    for i in range(0 , size):
        for j in range(0 , size -1 ):
            if ml[j] > ml[j + 1]:
                ml[j] , ml[j + 1] = ml[j + 1] , ml[j]


list1 = [10 , 5 , 30 , 20]
list2 = [15, 25, 35, 1]

ml = list1 + list2

bubble_sort(ml)
print("Merged and Sorted List :", ml)


