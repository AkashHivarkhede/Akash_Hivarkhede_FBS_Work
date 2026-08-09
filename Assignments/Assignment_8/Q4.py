# Sum of all odd numbers between 1 to n


def sum_odd(n):
    total = 0

    for i in range(1 , n + 1):
        if i % 2 == 0:
            total += i 
    
    return total


n = int(input('Enter a number : '))
print(f'Sum of odd number : {sum_odd(n)}')