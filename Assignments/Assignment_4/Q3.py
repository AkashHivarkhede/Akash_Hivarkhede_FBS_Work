# WAP to print sum of series upto n.

n = int(input('Enter a number :'))
total = 0 

for i in range(1 , n + 1):
    total += i 

print(total)