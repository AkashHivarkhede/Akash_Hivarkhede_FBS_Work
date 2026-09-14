# WAP to find sum of series using recursive functions
# 1! + 2! + 3! + 4! + ..... + n!
# Two recursive functions: fact() and sum()


def fact(n):

    if n == 0 or n == 1:
        return 1

    return n * fact(n - 1)


def sum(n):

    if n == 0:
        return 0

    return fact(n) + sum(n - 1)


n = int(input("Enter n: "))

print("Sum =", sum(n))