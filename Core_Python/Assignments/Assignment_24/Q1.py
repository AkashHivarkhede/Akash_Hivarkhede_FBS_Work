# Calculate the sum of squares of numbers from 1 to 100 using four threads. Divide the
# range equally among the threads, and each thread calculates the sum of squares for its
# range. Finally, combine the results to get the total sum of squares.


import threading
def sum_of_squares(start, end, results, index):

    total = 0

    for i in range(start, end + 1):
        total = total + (i * i)

    results[index] = total


results = [0, 0, 0, 0]


t1 = threading.Thread(
    target=sum_of_squares,
    args=(1, 25, results, 0)
)

t2 = threading.Thread(
    target=sum_of_squares,
    args=(26, 50, results, 1)
)

t3 = threading.Thread(
    target=sum_of_squares,
    args=(51, 75, results, 2)
)

t4 = threading.Thread(
    target=sum_of_squares,
    args=(76, 100, results, 3)
)


t1.start()
t2.start()
t3.start()
t4.start()


t1.join()
t2.join()
t3.join()
t4.join()


total = results[0] + results[1] + results[2] + results[3]


print("Thread 1 Result:", results[0])
print("Thread 2 Result:", results[1])
print("Thread 3 Result:", results[2])
print("Thread 4 Result:", results[3])

print("Total Sum of Squares:", total)