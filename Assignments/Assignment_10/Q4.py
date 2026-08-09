# Write a program to reverse the list.

def reverse_list(list):
    left = 0
    right = len(list) - 1

    while left < right:
        list[left] , list[right] = list[right] , list[left]
        left += 1
        right -= 1

list = [10 , 20 , 30 , 40 , 50]

print('Befor reverse :' , list)
reverse_list(list)
print('After reverse :' , list)
