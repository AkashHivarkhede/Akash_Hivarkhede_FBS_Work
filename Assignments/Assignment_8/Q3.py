# Write a program to find sum of following series using functions :
# 1+ 2 + 3 + 4+..... + n sum of number 
# 1!+ 2! + 3! + 4!+..... + n! sum of factorial 
# 1^1 + 2^2 + 3^3+ ...... n^n sum of power 


def sum_series(n):
    total = 0
    
    for i in range(1 ,n + 1):
        total += i

    return total

num = int(input("Enter a number : "))
print(f'Sum of digits is {sum_series(num)}')


def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i

    return fact

def factorial_series(n):
    total = 0

    for i in range(1 , n + 1):
        total = total + factorial(i)
    
    return total

n = int(input('Enter a number : '))
print("Sum = ", factorial_series(n))


def power(base, exponent):
    result = 1

    for i in range(exponent):
        result = result * base

    return result


def power_series(n):
    total = 0

    for i in range(1, n + 1):
        total = total + power(i, i)

    return total


n = int(input("Enter n: "))

print("Sum =", power_series(n))

