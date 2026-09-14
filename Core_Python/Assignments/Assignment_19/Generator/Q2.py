# Implement a generator function that yields palindrome numbers.
# Palindromes are numbers that read the same backward as forward
# (e.g., 121, 1331). Generate palindromes lazily and infinitely.


def palindrome():
    num = 0

    while True:
        if str(num) == str(num)[::-1]:
            yield num

        num = num + 1


# Create generator
p = palindrome()

# Generate first 20 palindrome numbers
for i in range(20):
    print(next(p), end=" ")