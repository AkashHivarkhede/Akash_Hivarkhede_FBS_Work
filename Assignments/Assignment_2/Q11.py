# Write a program to reverse three-digit number.

# Input a three-digit number
num = int(input("Enter a three-digit number: "))

# Extract digits
unit = num % 10
tens = (num // 10) % 10
hundreds = num // 100

# Reverse the number
reverse = (unit * 100) + (tens * 10) + hundreds

# Display result
print("Reversed number =", reverse)