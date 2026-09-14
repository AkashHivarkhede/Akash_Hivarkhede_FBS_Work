#         1
#       2 3 2
#     3 4 5 4 3
#   4 5 6 7 6 5 4
# 5 6 7 8 9 8 7 6 5


n = 5

for i in range(1, n + 1):

    # Spaces
    for j in range(n - i):
        print("  ", end="")

    # Increasing numbers
    for j in range(i):
        print(i + j, end=" ")

    # Decreasing numbers
    for j in range(i - 2, -1, -1):
        print(i + j, end=" ")

    print()