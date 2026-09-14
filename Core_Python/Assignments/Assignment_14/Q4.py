# Write a Python program that finds all pairs of elements in a list whose sum is equal to a given value.

number_list = [2, 4, 3, 5, 7, 8, 9, 1]

value = int(input("Enter the sum values : "))

for i in range(len(number_list)):
    for j in range(i + 1, len(number_list)):

        if number_list[i] + number_list[j] == value:
            print(f"Pair found: ({number_list[i]}, {number_list[j]})")




