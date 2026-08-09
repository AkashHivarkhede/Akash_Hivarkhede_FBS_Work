# Write a program to swap two numbers without using third variable.

# Input two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Swap without using third variable
a = a + b
b = a - b
a = a - b

# Display swapped numbers
print("After swapping:")
print("First number =", a)
print("Second number =", b)