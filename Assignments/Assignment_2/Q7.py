# Find the sum of three-digit number.

# Input a three-digit number
num = int(input("Enter a three-digit number: "))

# Extract digits
unit = num % 10
tens = (num // 10) % 10
hundreds = num // 100

# Calculate sum of digits
sum_digits = hundreds + tens + unit

# Display result
print("Sum of digits =", sum_digits)