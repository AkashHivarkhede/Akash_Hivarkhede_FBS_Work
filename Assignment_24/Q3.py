# Implement two threads to print lowercase and uppercase alphabets concurrently from
# 'a' to 'z' and 'A' to 'Z'.

import threading

def print_lowercase():
    for ch in range(ord('a'), ord('z') + 1):
        print(chr(ch), end=" ")


def print_uppercase():
    for ch in range(ord('A'), ord('Z') + 1):
        print(chr(ch), end=" ")


lower_thread = threading.Thread(target=print_lowercase)
upper_thread = threading.Thread(target=print_uppercase)

lower_thread.start()
upper_thread.start()

lower_thread.join()
upper_thread.join()

print("\nProgram completed.")