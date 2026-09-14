# Sum of all prime numbers between 1 to n

def prime(num):

    count = 0

    for i in range(1, num + 1):
        if num % i == 0:
            count = count + 1

    if count == 2:
        return True
    else:
        return False


def prime_sum(n):

    total = 0

    for i in range(1, n + 1):
        if prime(i):
            total = total + i

    return total


n = int(input("Enter n: "))

print("Sum of prime numbers =", prime_sum(n))