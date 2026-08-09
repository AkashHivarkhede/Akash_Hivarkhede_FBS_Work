# Write a program to calculate area of rectangle


def area_of_rect(length , width):
    return length * width


length = float(input('Enter length : '))
width = float(input('Enter width :'))

print(f'Area of Rectangle is : {area_of_rect(length , width)}')