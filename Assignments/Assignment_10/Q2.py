
# Write a program to find maximum and minimum element in a list.

def max_min_ele(list):
    max = list[0]
    min = list[0]
    for i in range(1 , len(list)):
        if max < list[i]:
            max = list[i]
        elif min > list[i]:
            min = list[i]
    return max , min

numbers = [20 , 10 , 30 , 40 , 50]

min = min(numbers)

res = list(max_min_ele(numbers))

print('Maximun number :', res[0] )
print('Minimum number :', res[1])