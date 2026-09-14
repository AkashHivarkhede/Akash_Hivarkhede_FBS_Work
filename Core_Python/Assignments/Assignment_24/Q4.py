# Implement a producer-consumer problem with a limited buffer of size 5. Create two
# producer threads and two consumer threads. Producers produce items, and consumers
# consume them. Ensure proper synchronization to avoid buffer overflows or underflows.

import threading
import time

buffer = []

condition = threading.Condition()

def producer(name, start):
    for i in range(start, start + 5):

        with condition:

            while len(buffer) == 5:
                condition.wait()

            item = i
            buffer.append(item)

            print(name, "produced:", item)
            print("Buffer:", buffer)

            condition.notify_all()

        time.sleep(0.5)


def consumer(name):
    for i in range(5):

        with condition:

            while len(buffer) == 0:
                condition.wait()

            item = buffer.pop(0)

            print(name, "consumed:", item)
            print("Buffer:", buffer)

            condition.notify_all()

        time.sleep(0.8)


producer1 = threading.Thread(
    target=producer,
    args=("Producer-1", 1)
)

producer2 = threading.Thread(
    target=producer,
    args=("Producer-2", 6)
)


consumer1 = threading.Thread(
    target=consumer,
    args=("Consumer-1",)
)

consumer2 = threading.Thread(
    target=consumer,
    args=("Consumer-2",)
)


producer1.start()
producer2.start()
consumer1.start()
consumer2.start()


producer1.join()
producer2.join()
consumer1.join()
consumer2.join()

print("\nProgram completed.")