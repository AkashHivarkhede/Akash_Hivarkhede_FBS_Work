# Write a program to find the second largest element in the list.

def second_largest(list):
    largest = list[0]
    second_lg = 0 

    for i in range(len(list)):
        if list[i] > largest:
            second_lg = largest
            largest = list[i]
        elif(list[i] > second_lg and list[i] < largest):
            second_lg = list[i]

    return second_lg

numbers = [10 , 20 , 30 , 40 , 50]

print(f'Second largest is {second_largest(numbers)}.')