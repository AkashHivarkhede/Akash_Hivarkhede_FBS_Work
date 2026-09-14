# Write a generator function that mimics the behavior of the built-in
# range() function. The generator should take start, stop, and step
# arguments and yield numbers within the specified range.

def my_range(start, stop, step):

    if step > 0:
        while start < stop:
            yield start
            start = start + step

    elif step < 0:
        while start > stop:
            yield start
            start = start + step


start = int(input("Enter start: "))
stop = int(input("Enter stop: "))
step = int(input("Enter step: "))

for num in my_range(start, stop, step):
    print(num, end=" ")