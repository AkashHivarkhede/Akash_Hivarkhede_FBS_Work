# Write a program to print first n prime numbers.
def is_prime(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    if count == 2:
        return True
    else:
        return False

n = int(input("Enter the number of prime numbers to print: "))
count = 0
i = 2
while count < n:
    if is_prime(i):
        print(i)
        count += 1
    i += 1