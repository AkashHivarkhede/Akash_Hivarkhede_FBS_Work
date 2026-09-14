# Write a program to solve the following series :
# a. 1! + 2! + 3! + 4! + .....n!
# b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)
# c. Find the sum of a geometric series from 1 to n where the common ratio is 2.
# d. S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10
# e. x - x2/3 + x3/5 - x4/7 + .... to n terms



# Sum of factorial series

# a. 1! + 2! + 3! + 4! + ..... + n!

def factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    return fact


def factorial_series(n):
    total = 0

    for i in range(1, n + 1):
        total = total + factorial(i)

    return total


n = int(input("Enter n: "))

print("Sum =", factorial_series(n))


# b. N + N² + N³ + N⁴ + ..... + Nᴺ

# Sum of power series

def power_series(n):
    total = 0

    for i in range(1, n + 1):
        total = total + n ** i

    return total


n = int(input("Enter N: "))

print("Sum =", power_series(n))


# c. Geometric series from 1 to n, common ratio = 2


def geometric_series(n):
    total = 0
    term = 1

    for i in range(1, n + 1):
        total = total + term
        term = term * 2

    return total
    


n = int(input("Enter number of terms: "))

print("Sum =", geometric_series(n))




# d. S = a + a²/2 + a³/3 + ...... + a¹⁰/10


def series(a):
    total = 0

    for i in range(1, 11):
        total = total + (a ** i) / i

    return total


a = int(input("Enter value of a: "))

print("Sum =", series(a))


# e. x - x2/3 + x3/5 - x4/7 + .... to n terms


def series(x, n):
    total = 0

    for i in range(1, n + 1):

        term = (x ** i) / (2 * i - 1)

        if i % 2 == 1:
            total = total + term
        else:
            total = total - term

    return total


x = int(input("Enter value of x: "))
n = int(input("Enter number of terms: "))

print("Sum =", series(x, n))