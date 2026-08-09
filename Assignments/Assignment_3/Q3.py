# Write a program to input angles of a triangle and check whether triangle is valid or not.

# Input the three angles of the triangle
a = float(input("Enter first angle: "))
b = float(input("Enter second angle: "))
c = float(input("Enter third angle: "))

# Check whether the triangle is valid
if (a > 0 and b > 0 and c > 0) and (a + b + c == 180):
    print("The triangle is valid.")
else:
    print("The triangle is not valid.")