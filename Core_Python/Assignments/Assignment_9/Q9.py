# WAP to check whether a number is prime or not using recursion

def prime(num, i):

    if i == 1:
        return True

    if num % i == 0:
        return False

    return prime(num, i - 1)


n = int(input("Enter a number: "))

if n <= 1:
    print("Not a Prime Number")
elif prime(n, n - 1):
    print("Prime Number")
else:
    print("Not a Prime Number")