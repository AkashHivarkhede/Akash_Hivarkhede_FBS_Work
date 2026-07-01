# WAP to check if a given number is prime number or not.

n = int(input('Enter a number :'))

prime = False

for i in range(n):
    if(n % 2 == 0):
        prime = True
    else:
        prime = False
        

if(prime == 0):
    print(f'{n} is prime.')
else:
    print(f'{n} is not prime.')