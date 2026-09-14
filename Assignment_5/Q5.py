# Write a program to print prime numbers between 1 to 100.

def is_prime(num):

    count = 0

    for i in range(1, num + 1):
        if num % i == 0:
            count += 1

    if count == 2:
        return True
    else:
        return False


for i in range(1, 101):
    if is_prime(i):
        print(i)