# Write a program to calculate area of circle


def area_of_circle(radius):
    PI = 3.14
    return PI * radius * radius

r = float(input('Enter a radius : '))
res = area_of_circle(r)

print(f'Area of circle is {res}.')