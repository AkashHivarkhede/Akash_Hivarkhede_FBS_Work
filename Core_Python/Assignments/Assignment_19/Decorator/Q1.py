# Develop a memoization decorator that caches the results of function
# calls and returns the cached result when the same inputs occur again.
# This can greatly improve the performance of recursive or
# computationally intensive functions.


def memoize(func):

    cache = {}

    def wrapper(n):

        if n in cache:
            print("Returning cached result...")
            return cache[n]

        result = func(n)
        cache[n] = result

        return result

    return wrapper


@memoize
def fibonacci(n):

    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input("Enter a number: "))

print("Fibonacci:", fibonacci(n))