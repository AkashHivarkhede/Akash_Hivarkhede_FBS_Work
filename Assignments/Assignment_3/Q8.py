# Write a program to prompt user to enter userid and password. After verifying
# userid and password display a 4 digit random number and ask user to enter the
# same. If user enters the same number then show him success message otherwise
# failed. (Something like captcha)

import random

userId = 'admin'
password = 'admin123'

captcha = random.randint(1000 , 9999)

uId = str(input('Enter User Id :'))
passw = str(input('Enter Password :'))

if(uId == userId and passw == password):
    print(f'Captcha : {captcha}')
    cap = int(input('Enter Captcha :'))
    if(captcha == cap):
        print('Login Successfully')
    else:
        print('Please enter valid number.')
else:
    print("Please enter valid user Id and password.")