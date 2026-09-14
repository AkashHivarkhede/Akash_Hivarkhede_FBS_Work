# WAP to check if a given number is Armstrong number or not. For each task create separate functions.

def count_digits(num):
    count = 0

    while num > 0:
        count = count + 1
        num = num // 10

    return count


def is_armstrong(num):

    digits = count_digits(num)

    temp = num
    total = 0

    while temp > 0:
        digit = temp % 10
        total = total + digit ** digits
        temp = temp // 10

    if total == num:
        return True
    else:
        return False


n = int(input("Enter a number: "))

if is_armstrong(n):
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")