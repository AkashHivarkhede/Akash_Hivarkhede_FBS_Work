# WAP to check if given number is Armstrong or not using recursive function

def count_digits(num):
    if num == 0:
        return 0

    return 1 + count_digits(num // 10)


def armstrong(num, digits):

    if num == 0:
        return 0

    digit = num % 10

    return digit ** digits + armstrong(num // 10, digits)


n = int(input("Enter a number: "))

digits = count_digits(n)

result = armstrong(n, digits)

if result == n:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")