# Write a program to check if entered number is a palindrome or not.

# WAP to check if entered number is palindrome or not

def reverse_number(num):

    rev = 0

    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10

    return rev


def is_palindrome(num):

    rev = reverse_number(num)

    if num == rev:
        return True
    else:
        return False


n = int(input("Enter a number: "))

if is_palindrome(n):
    print("Number is Palindrome")
else:
    print("Number is not Palindrome")