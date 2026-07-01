# WAP to check if given number Strong Number.

n = int(input("Enter a number :"))  # 145

original = n # 145
sum = 0 # 120 # 144

while n > 0:   # 145 > 0 # 14 > 0 # 1 > 0 # 0 > 0
    digit = n % 10   # 5 # 4 # 1
    fact = 1

    for i in range(1 , digit + 1): # 1 , 5 # 1, 4 # 1 , 1
        fact *= i # 1 , 2 , 5 , 24 , 120 # 1 , 2 , 3 , 24 # 1
    
    sum += fact # 120 # 24 # 1 

    n = n // 10 # 14 # 1 # 0

if(sum == original): 
    print(original ,'is a strong number.')
else:
    print(original , 'is not a strong number.')