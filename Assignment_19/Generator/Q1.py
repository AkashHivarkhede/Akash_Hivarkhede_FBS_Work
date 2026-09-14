# We want to generate Fibonacci numbers up to a certain limit.
# Instead of computing and storing the entire sequence in memory,
# create generator to yield Fibonacci numbers one by one,
# conserving memory and allowing for easy iteration.


def fibonacci(limit):
    a = 0
    b = 1

    while a <= limit:
        yield a
        a, b = b, a + b


limit = int(input("Enter the limit: "))

print("Fibonacci numbers:")

for num in fibonacci(limit):
    print(num, end=" ")