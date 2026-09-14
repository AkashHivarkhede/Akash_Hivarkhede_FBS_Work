# WAP to calculate m to the power n using recursion

def power(m, n):

    if n == 0:
        return 1

    return m * power(m, n - 1)


m = int(input("Enter value of m: "))
n = int(input("Enter value of n: "))

print("Answer =", power(m, n))