# WAP to print Armstrong number within a given range


def is_armstrong(num):
    temp = num
    digits = len(str(num))
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10

    return total == num


start_range = int(input("Enter the start of the range: "))
end_range = int(input("Enter the end of the range: "))

for num in range(start_range, end_range + 1):
    if is_armstrong(num):
        print(num)


