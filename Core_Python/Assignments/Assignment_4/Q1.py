# WAP to print all even numbers until n.

num = int(input('Enter a number :'))

for i in range(num + 1):
    if(i % 2 == 0):
        print(i)