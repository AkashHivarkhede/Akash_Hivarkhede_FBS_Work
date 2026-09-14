# 1                 1
# 1 2             2 1
# 1 2 3         3 2 1
# 1 2 3 4     4 3 2 1
# 1 2 3 4 5 4 3 2 1 1


n = 5

for i in range(1, n + 1):

    # Left side
    for j in range(1, i + 1):
        print(j, end=" ")

    # Middle spaces
    for j in range(2 * (n - i)):
        print("  ", end=" ")

    # Right side
    for j in range(i, 0, -1):
        print(j, end=" ")

    print()