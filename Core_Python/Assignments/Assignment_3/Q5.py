# Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.

# Input the three sides of the triangle
a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

# Check the type of triangle
if a == b == c:
    print("The triangle is an Equilateral Triangle.")
elif a == b or b == c or a == c:
    print("The triangle is an Isosceles Triangle.")
else:
    print("The triangle is a Scalene Triangle.")