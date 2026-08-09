# Python Program to Sort a List According to the Length of the Elements within the list.

def List_Ac_Length(fruits):
    size = len(fruits)

    for i in range(size):
        for j in range(i + 1, size):
            if len(fruits[i]) > len(fruits[j]):
                fruits[i] , fruits[j] = fruits[j] , fruits[i]


fruits = ["apple", "kiwi", "banana", "fig", "orange"]
List_Ac_Length(fruits)
print(fruits)