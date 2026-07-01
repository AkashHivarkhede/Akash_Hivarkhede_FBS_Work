# WAP to print all numbers in a range divisible by a given number.

n = int(input('Enter the number :'))
start = int(input('Enter the starting number :'))
end = int(input('Enter the ending number :'))


for i in range(start , end + 1):
    if(i % n == 0):
        print(i)
