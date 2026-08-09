# Write a program to calculate area of an equilateral triangle.¶
import math

a = float(input("Enter the side length: "))

area = (math.sqrt(3) / 4) * a * a

print(f"Area of Equilateral Triangle = {area:.2f}")