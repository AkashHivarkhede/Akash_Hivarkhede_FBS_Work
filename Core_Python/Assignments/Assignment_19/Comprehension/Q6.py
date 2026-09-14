# Use a dictionary comprehension to count the length of each word
# in a sentence (take input from user)

sentence = input("Enter a sentence: ")

words = sentence.split()

result = {word: len(word) for word in words}

print(result)