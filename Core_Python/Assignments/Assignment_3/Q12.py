# Write a program to check if given 3 digit number is a palindrome or not.

num = int(input("Enter a 3-digit number: "))

original = num

# Extract digits
digit1 = num % 10
num = num // 10

digit2 = num % 10
num = num // 10

digit3 = num % 10

# Reverse the number
reverse = digit1 * 100 + digit2 * 10 + digit3

# Check palindrome
if original == reverse:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")