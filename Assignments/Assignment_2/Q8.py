# Write a program to swap two numbers using third variable. 
# Input two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Swap using third variable
temp = a
a = b
b = temp

# Display swapped numbers
print("After swapping:")
print("First number =", a)
print("Second number =", b)