# Write a Python program to find all the unique words and count the
# frequency of occurrence from a given list of strings. Use Python set data type.


strings = ["apple", "banana", "apple", "orange", "banana", "kiwi", "grape", "kiwi"]

words = [] 

for string in strings:
    words.extend(string.split())


unique_words = set(words)

frequency = {}

for word in unique_words:
    frequency[word] = words.count(word)

print("Unique words:", unique_words)

print("Frequency of occurrence:")

for word, count in frequency.items():
    print(f"{word}: {count}")