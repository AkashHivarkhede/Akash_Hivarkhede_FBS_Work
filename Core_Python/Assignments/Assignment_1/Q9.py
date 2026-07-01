# Write a program to enter base and height of a triangle and find its area.

base = float(input('Enter the base of the triangle :'))
height = float(input('Enter the height of the triangle :'))

area = (height * base) / 2 

print(f'Area of Triangle : {area:.2f}')