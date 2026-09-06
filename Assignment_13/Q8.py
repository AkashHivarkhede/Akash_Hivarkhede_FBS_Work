# Python Program to Count the Frequency of Words Appearing in a String Using a Dictionary

str = input("Enter a string: ")

words = str.split()

frequency = {}

for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

print("Frequency of words in the string:")
for word, count in frequency.items():
    print(f"{word}: {count}")