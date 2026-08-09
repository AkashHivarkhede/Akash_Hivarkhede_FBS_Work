# Write a Program to input two angles from user and find third angle of the triangle.

angle1 = float(input('Enter the first angle :'))
angle2 = float(input('Enter the second angle :'))

angle3 = 180 - (angle1 + angle2)

print(f'Third Angle : {angle3}')