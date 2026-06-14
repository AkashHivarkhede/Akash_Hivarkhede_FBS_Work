# Write a program to check if person is eligible to marry or not (male age >=21 and
# female age>=18)

gender = str(input('Enter Gender F/M:'))
age = int(input('Enter Age :'))

if(gender.lower() == 'f' and age >= 18):
    print('Your are Eligible to Marry.')
elif(gender.lower() == 'm' and age >= 21):
    print('Your are Eligible to Marry.')
else:
    print('Your are not Elgible to Marry.')

