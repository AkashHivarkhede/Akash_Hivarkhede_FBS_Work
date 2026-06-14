# Write a program to check if user has entered correct userid and password.

import random

userId = 'admin'
password = 'admin123'


uId = str(input('Enter User Id :'))
passw = str(input('Enter Password :'))

if(uId == userId and passw == password):
    print('Login Successfully')
else:
    print("Please enter valid user Id and password.")