# numbers = list(map(int, input("Enter list elements separated by space: ").split()))

numbers = [10 , 20 , 30 , 40 , 50 , 20 , 10]
result = []

for i in numbers:
    found = False

    for j in result:
        if i == j:
            found = True
            break

    if found == False:
        result.append(i)

print("List after removing duplicates:", result)